# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from datetime import datetime
import time
from config import load_hide_profit

dashboard_bp = Blueprint('dashboard', __name__)

_DASH_CACHE = {}

def compute_dash(f, t):
    from database import get_pooled_conn
    b = {"f": f, "t": t}
    P="TO_DATE(:f,'YYYY-MM-DD')"; Q="TO_DATE(:t,'YYYY-MM-DD')+1"
    d = {"sales":0,"collect":0,"purch":0,"gross":0,"netprofit":0,"recv":0,"invval":0,"vat":0,
         "months":[],"msales":[],"mcollect":[],"mpurch":[],"rep_labels":[],"rep_vals":[],"itm_labels":[],"itm_vals":[]}
    try:
        sqls = {
            "purch": "SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "gross": "SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_BILL_DTL x JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q,
            "gross_ret": "SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_RT_BILL_DTL x JOIN IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q,
            "netprofit": "SELECT NVL(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),0) FROM IAS_POST_DTL p JOIN ACCOUNT a ON a.A_CODE=p.A_CODE WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2 AND p.DOC_DATE>="+P+" AND p.DOC_DATE<"+Q,
            "invval": "SELECT NVL(SUM(NVL(I_QTY,0)*NVL(IN_OUT,0)*NVL(STK_COST,0)),0) FROM ITEM_MOVEMENT WHERE I_DATE<"+Q,
            "ov": "SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "ov_ret": "SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q,
            "iv": "SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "mp": "SELECT TO_CHAR(BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,'YYYY-MM')",
            "rs": "SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE), SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_BILL_MST m LEFT JOIN SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE)",
            "rs_ret": "SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE_BILL), SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_RT_BILL_MST m LEFT JOIN SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE_BILL WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE_BILL)",
            "its": "SELECT NVL(i.I_NAME, x.I_CODE), SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_BILL_DTL x JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER LEFT JOIN IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE)",
            "its_ret": "SELECT NVL(i.I_NAME, x.I_CODE), SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_RT_BILL_DTL x JOIN IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER LEFT JOIN IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE)"
        }

        results = {}
        with get_pooled_conn() as con:
            with con.cursor() as cur:
                for key, sql in sqls.items():
                    try:
                        cur.execute(sql, {k:v for k,v in b.items() if (":"+k) in sql})
                        if key in ["purch", "gross", "gross_ret", "netprofit", "invval", "ov", "ov_ret", "iv"]:
                            r = cur.fetchone()
                            results[key] = round(float(r[0]),2) if r and r[0] is not None else 0.0
                        else:
                            m = {}
                            for r in cur.fetchall():
                                m[str(r[0])] = round(float(r[1] or 0),2)
                            results[key] = m
                    except Exception as e:
                        import logging
                        logging.getLogger(__name__).error("Exception occurred:", exc_info=True)
                        results[key] = (0.0 if key not in ["mp", "rs", "rs_ret", "its", "its_ret"] else {})
        
        try:
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
                    col_q = f"""
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
                    """
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
                    
                    mc_q = f"""
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
                    """
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
            mc_dict = {}

        d["purch"] = results["purch"]
        d["gross"] = round(results["gross"] - results["gross_ret"], 2)
        d["netprofit"] = results["netprofit"]
        d["recv"] = results.get("recv", 0.0)
        d["invval"] = results["invval"]
        d["vat"] = round((results["ov"] - results["ov_ret"]) - results["iv"], 2)
        
        mp = results.get("mp", {})
        months = sorted(set(list(ms_dict.keys()) + list(mc_dict.keys()) + list(mp.keys())))
        d["months"] = months
        d["msales"] = [ms_dict.get(x, 0.0) for x in months]
        d["mcollect"] = [mc_dict.get(x, 0.0) for x in months]
        d["mpurch"] = [mp.get(x, 0.0) for x in months]
        
        rs = results["rs"]; rs_ret = results["rs_ret"]
        rs_net = {k: round(rs.get(k,0) - rs_ret.get(k,0), 2) for k in set(list(rs)+list(rs_ret))}
        for k, v in sorted(rs_net.items(), key=lambda item: item[1], reverse=True):
            if v != 0:
                d["rep_labels"].append(str(k))
                d["rep_vals"].append(v)
        
        its = results["its"]; its_ret = results["its_ret"]
        its_net = {k: round(its.get(k,0) - its_ret.get(k,0), 2) for k in set(list(its)+list(its_ret))}
        for k, v in sorted(its_net.items(), key=lambda item: item[1], reverse=True)[:50]:
            if v != 0:
                d["itm_labels"].append(str(k)[:22])
                d["itm_vals"].append(v)
    except Exception as e:
        d["err"]=str(e)
    return d

@dashboard_bp.route("/api/dashboard")
def api_dashboard():
    try:
        from report_handlers import get_date_range
        year_val = request.args.get("year_val", str(datetime.now().year))
        period_type = request.args.get("period_type", "monthly")
        period_val = request.args.get("period_val", "all")
        
        d_from, d_to = get_date_range(year_val, period_type, period_val)
        force_refresh = request.args.get("force_refresh", "0")
        
        current_time = time.time()
        
        # التنظيف التلقائي لمنع تسرب الذاكرة (Memory Leak)
        expired_keys = [k for k, v in _DASH_CACHE.items() if current_time - v['time'] >= 900]
        for k in expired_keys:
            del _DASH_CACHE[k]
        
        cache_key = f"{year_val}_{period_type}_{period_val}"
            
        if force_refresh != "1" and cache_key in _DASH_CACHE:
            dash_data = _DASH_CACHE[cache_key]['data']
        else:
            dash_data = compute_dash(d_from, d_to)
            _DASH_CACHE[cache_key] = {'time': current_time, 'data': dash_data}
            
        hide_profit = load_hide_profit()
        
        return jsonify({
            "data": dash_data,
            "hide_profit": hide_profit,
            "date_from": d_from,
            "date_to": d_to
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500
