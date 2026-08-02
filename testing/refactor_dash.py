import sys

new_func = """def compute_dash(f, t):
    b = {"f": f, "t": t}
    P="TO_DATE(:f,'YYYY-MM-DD')"; Q="TO_DATE(:t,'YYYY-MM-DD')+1"
    d = {"sales":0,"collect":0,"purch":0,"gross":0,"netprofit":0,"recv":0,"invval":0,"vat":0,
         "months":[],"msales":[],"mcollect":[],"mpurch":[],"rep_labels":[],"rep_vals":[],"itm_labels":[],"itm_vals":[]}
    try:
        with get_conn() as con:
            cur = con.cursor()
            def sc(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); r=cur.fetchone()
                    return round(float(r[0]),2) if r and r[0] is not None else 0.0
                except Exception: return 0.0
            def rw(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); return cur.fetchall()
                except Exception: return []
            def mm(sql):
                m={}
                for r in rw(sql):
                    m[str(r[0])]=round(float(r[1] or 0),2)
                return m

            sales = sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            sales_ret = sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q)
            d["sales"] = round(sales - sales_ret, 2)

            d["collect"]=sc("SELECT NVL(SUM(NVL(CR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q)
            
            d["purch"]=sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            
            gross = sc("SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q)
            gross_ret = sc("SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_RT_BILL_DTL x JOIN IAS20261.IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q)
            d["gross"] = round(gross - gross_ret, 2)
            
            d["netprofit"]=sc("SELECT NVL(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2 AND p.DOC_DATE>="+P+" AND p.DOC_DATE<"+Q)
            
            d["recv"]=sc("SELECT NVL(SUM(bal),0) FROM (SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) bal FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND DOC_DATE<"+Q+" GROUP BY C_CODE HAVING SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0))>0)")
            
            d["invval"]=sc("SELECT NVL(SUM(NVL(I_QTY,0)*NVL(IN_OUT,0)*NVL(STK_COST,0)),0) FROM IAS20261.ITEM_MOVEMENT WHERE I_DATE<"+Q)
            
            ov = sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            ov_ret = sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q)
            ov_net = ov - ov_ret
            
            iv = sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["vat"]=round(ov_net-iv,2)
            
            ms=mm("SELECT TO_CHAR(BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,'YYYY-MM')")
            ms_ret=mm("SELECT TO_CHAR(RT_BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q+" GROUP BY TO_CHAR(RT_BILL_DATE,'YYYY-MM')")
            
            mc=mm("SELECT TO_CHAR(DOC_DATE,'YYYY-MM'), SUM(NVL(CR_AMT,0)) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" GROUP BY TO_CHAR(DOC_DATE,'YYYY-MM')")
            mp=mm("SELECT TO_CHAR(BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,'YYYY-MM')")
            
            months=sorted(set(list(ms)+list(ms_ret)+list(mc)+list(mp)))
            d["months"]=months
            d["msales"]=[round(ms.get(x,0) - ms_ret.get(x,0), 2) for x in months]
            d["mcollect"]=[mc.get(x,0) for x in months]
            d["mpurch"]=[mp.get(x,0) for x in months]
            
            rs = mm("SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE), SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_MST m LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE)")
            rs_ret = mm("SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE_BILL), SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_RT_BILL_MST m LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE_BILL WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE_BILL)")
            
            rs_net = {k: round(rs.get(k,0) - rs_ret.get(k,0), 2) for k in set(list(rs)+list(rs_ret))}
            for k, v in sorted(rs_net.items(), key=lambda item: item[1], reverse=True):
                if v != 0:
                    d["rep_labels"].append(str(k))
                    d["rep_vals"].append(v)
            
            its = mm("SELECT NVL(i.I_NAME, x.I_CODE), SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE)")
            its_ret = mm("SELECT NVL(i.I_NAME, x.I_CODE), SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_RT_BILL_DTL x JOIN IAS20261.IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE)")
            
            its_net = {k: round(its.get(k,0) - its_ret.get(k,0), 2) for k in set(list(its)+list(its_ret))}
            for k, v in sorted(its_net.items(), key=lambda item: item[1], reverse=True)[:50]:
                if v != 0:
                    d["itm_labels"].append(str(k)[:22])
                    d["itm_vals"].append(v)
    except Exception as e:
        d["err"]=str(e)
    return d\n"""

with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    content = f.read()

import re
old_func_pattern = re.compile(r'def compute_dash\(f, t\):.*?return d\n', re.DOTALL)

if not old_func_pattern.search(content):
    print('Pattern not found!')
else:
    new_content = old_func_pattern.sub(new_func, content)
    with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print('compute_dash replaced successfully.')
