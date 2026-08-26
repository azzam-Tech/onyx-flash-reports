import re

with open(r'privet\onyx_reports\routes\dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the try/except blocks calling run_cust_aging and run_debt_movement_summary
old_block = """        try:
            from modules.ar.services import run_cust_aging
            _, rows = run_cust_aging({}, {'date_to': t, 'vendor_link': '1'})
            results["recv"] = round(sum(float(str(r[-1]).replace(',', '')) for r in rows), 2)
        except Exception as e:
            results["recv"] = 0.0


        try:
            from modules.sales.services import run_debt_movement_summary
            args = {
                'date_from': f,
                'date_to': t,
                'grp_by': 'period',
                'period_type': 'monthly',
                'period_val': 'all'
            }
            # row: [period, desc, open_bal, net_sales_vat, collect, diff, ratio, close_bal, ...]
            _, rows = run_debt_movement_summary({}, args)
            
            d["sales"] = round(sum(float(str(r[3]).replace(',','')) for r in rows), 2)
            d["collect"] = round(sum(float(str(r[4]).replace(',','')) for r in rows), 2)
            
            ms_dict = {str(r[0]): float(str(r[3]).replace(',','')) for r in rows}
            mc_dict = {str(r[0]): float(str(r[4]).replace(',','')) for r in rows}
        except Exception as e:
            import logging
            logging.getLogger(__name__).error("debt_movement_summary Exception:", exc_info=True)
            d["sales"] = 0.0
            d["collect"] = 0.0
            ms_dict = {}
            mc_dict = {}"""

new_block = """        try:
            with get_pooled_conn() as con:
                with con.cursor() as cur:
                    # Fast Receivables Calculation (with Vendor Link = 1 logic)
                    cur.execute("SELECT TO_CHAR(C_CODE), SUM(NVL(DR_AMT,0)), SUM(NVL(CR_AMT,0)) FROM IAS_POST_DTL WHERE C_CODE IS NOT NULL AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1 GROUP BY TO_CHAR(C_CODE)", {'dt': t})
                    debts = {c: (float(dr), float(cr)) for c, dr, cr in cur.fetchall()}
                    
                    cur.execute("SELECT TO_CHAR(C_CODE), TO_CHAR(C_VENDOR) FROM CUSTOMER WHERE C_VENDOR IS NOT NULL")
                    cmap = {c: v for c, v in cur.fetchall()}
                    
                    cur.execute("SELECT TO_CHAR(V_CODE), SUM(NVL(CR_AMT,0) - NVL(DR_AMT,0)) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND V_CODE IS NOT NULL AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1 GROUP BY TO_CHAR(V_CODE)", {'dt': t})
                    vb = {v: float(b) for v, b in cur.fetchall()}
                    
                    total_recv = 0.0
                    for c, (dr, cr) in debts.items():
                        v_id = cmap.get(c)
                        v_bal = vb.get(v_id, 0.0) if v_id else 0.0
                        total_recv += max(0, dr - (cr + (v_bal if v_bal > 0 else 0.0)))
                    results["recv"] = round(total_recv, 2)
                    
                    # Fast Sales & Collections Calculation
                    P = "TO_DATE(:f,'YYYY-MM-DD')"
                    Q = "TO_DATE(:t,'YYYY-MM-DD')+1"
                    
                    # Net Sales
                    sales_base = f"SELECT SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) FROM IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE >= {P} AND BILL_DATE < {Q}"
                    returns_base = f"SELECT SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) FROM IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE >= {P} AND RT_BILL_DATE < {Q}"
                    ext_disc_base = f"SELECT ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) FROM IAS_POST_DTL WHERE DOC_TYPE=15 AND NVL(CR_AMT,0)>0 AND NVL(DOC_POST,0)=1 AND DOC_DATE >= {P} AND DOC_DATE < {Q}"
                    
                    cur.execute(sales_base, {'f': f, 't': t})
                    s_val = cur.fetchone()[0] or 0.0
                    cur.execute(returns_base, {'f': f, 't': t})
                    r_val = cur.fetchone()[0] or 0.0
                    cur.execute(ext_disc_base, {'f': f, 't': t})
                    e_val = cur.fetchone()[0] or 0.0
                    
                    net_sales = float(s_val) - float(r_val) - float(e_val)
                    d["sales"] = round(net_sales * 1.15, 2) # Including VAT
                    
                    # Total Collection
                    col_q = f\"\"\"
                    SELECT SUM(rcpt) FROM (
                      SELECT SUM(CR_AMT) as rcpt FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL AND DOC_DATE >= {P} AND DOC_DATE < {Q}
                      UNION ALL
                      SELECT SUM(CR_AMT) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL AND DOC_DATE >= {P} AND DOC_DATE < {Q}
                      UNION ALL
                      SELECT SUM(CR_AMT) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL AND DOC_DATE >= {P} AND DOC_DATE < {Q}
                      UNION ALL
                      SELECT SUM(NVL(p.DR_AMT,0)) FROM IAS_BILL_MST b JOIN IAS_POST_DTL p ON p.DOC_NO=b.BILL_NO AND p.DOC_SER=b.BILL_SER AND p.DOC_TYPE=4 AND TO_CHAR(p.A_CODE) LIKE '111%' WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT>0 AND b.BILL_DATE >= {P} AND b.BILL_DATE < {Q}
                      UNION ALL
                      SELECT SUM(-CR_AMT) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0 AND DOC_DATE >= {P} AND DOC_DATE < {Q}
                    )
                    \"\"\"
                    cur.execute(col_q, {'f': f, 't': t})
                    d["collect"] = round(float(cur.fetchone()[0] or 0.0), 2)
                    
                    # Chart Data (Monthly)
                    ms_q = f"SELECT TO_CHAR(BILL_DATE, 'YYYY-MM'), SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) FROM IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE >= {P} AND BILL_DATE < {Q} GROUP BY TO_CHAR(BILL_DATE, 'YYYY-MM')"
                    mr_q = f"SELECT TO_CHAR(RT_BILL_DATE, 'YYYY-MM'), SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) FROM IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE >= {P} AND RT_BILL_DATE < {Q} GROUP BY TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
                    me_q = f"SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) FROM IAS_POST_DTL WHERE DOC_TYPE=15 AND NVL(CR_AMT,0)>0 AND NVL(DOC_POST,0)=1 AND DOC_DATE >= {P} AND DOC_DATE < {Q} GROUP BY TO_CHAR(DOC_DATE, 'YYYY-MM')"
                    
                    ms_dict = {}
                    cur.execute(ms_q, {'f': f, 't': t})
                    for mo, val in cur.fetchall(): ms_dict[mo] = float(val or 0.0)
                    cur.execute(mr_q, {'f': f, 't': t})
                    for mo, val in cur.fetchall(): ms_dict[mo] = ms_dict.get(mo, 0.0) - float(val or 0.0)
                    cur.execute(me_q, {'f': f, 't': t})
                    for mo, val in cur.fetchall(): ms_dict[mo] = ms_dict.get(mo, 0.0) - float(val or 0.0)
                    
                    for mo in ms_dict:
                        ms_dict[mo] = round(ms_dict[mo] * 1.15, 2)
                    
                    mc_q = f\"\"\"
                    SELECT mo, SUM(rcpt) FROM (
                      SELECT TO_CHAR(DOC_DATE, 'YYYY-MM') as mo, SUM(CR_AMT) as rcpt FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL AND DOC_DATE >= {P} AND DOC_DATE < {Q} GROUP BY TO_CHAR(DOC_DATE, 'YYYY-MM')
                      UNION ALL
                      SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), SUM(CR_AMT) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL AND DOC_DATE >= {P} AND DOC_DATE < {Q} GROUP BY TO_CHAR(DOC_DATE, 'YYYY-MM')
                      UNION ALL
                      SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), SUM(CR_AMT) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL AND DOC_DATE >= {P} AND DOC_DATE < {Q} GROUP BY TO_CHAR(DOC_DATE, 'YYYY-MM')
                      UNION ALL
                      SELECT TO_CHAR(b.BILL_DATE, 'YYYY-MM'), SUM(NVL(p.DR_AMT,0)) FROM IAS_BILL_MST b JOIN IAS_POST_DTL p ON p.DOC_NO=b.BILL_NO AND p.DOC_SER=b.BILL_SER AND p.DOC_TYPE=4 AND TO_CHAR(p.A_CODE) LIKE '111%' WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT>0 AND b.BILL_DATE >= {P} AND b.BILL_DATE < {Q} GROUP BY TO_CHAR(b.BILL_DATE, 'YYYY-MM')
                      UNION ALL
                      SELECT TO_CHAR(DOC_DATE, 'YYYY-MM'), SUM(-CR_AMT) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0 AND DOC_DATE >= {P} AND DOC_DATE < {Q} GROUP BY TO_CHAR(DOC_DATE, 'YYYY-MM')
                    ) GROUP BY mo
                    \"\"\"
                    mc_dict = {}
                    cur.execute(mc_q, {'f': f, 't': t})
                    for mo, val in cur.fetchall(): mc_dict[mo] = round(float(val or 0.0), 2)
                    
        except Exception as e:
            import logging
            logging.getLogger(__name__).error("Dashboard Fast SQL Exception:", exc_info=True)
            results["recv"] = 0.0
            d["sales"] = 0.0
            d["collect"] = 0.0
            ms_dict = {}
            mc_dict = {}"""

content = content.replace(old_block, new_block)

with open(r'privet\onyx_reports\routes\dashboard.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Dashboard backend replaced with Fast SQL.")
