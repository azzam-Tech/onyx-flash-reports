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
            "sales": "SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "sales_ret": "SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q,
            "collect": "SELECT NVL(SUM(NVL(CR_AMT,0)),0) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q,
            "purch": "SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "gross": "SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_BILL_DTL x JOIN IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q,
            "gross_ret": "SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_RT_BILL_DTL x JOIN IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q,
            "netprofit": "SELECT NVL(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),0) FROM IAS_POST_DTL p JOIN ACCOUNT a ON a.A_CODE=p.A_CODE WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2 AND p.DOC_DATE>="+P+" AND p.DOC_DATE<"+Q,
            "recv": "SELECT NVL(SUM(bal),0) FROM (SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) bal FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND DOC_DATE<"+Q+" GROUP BY C_CODE HAVING SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0))>0)",
            "invval": "SELECT NVL(SUM(NVL(I_QTY,0)*NVL(IN_OUT,0)*NVL(STK_COST,0)),0) FROM ITEM_MOVEMENT WHERE I_DATE<"+Q,
            "ov": "SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "ov_ret": "SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q,
            "iv": "SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q,
            "ms": "SELECT TO_CHAR(BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,'YYYY-MM')",
            "ms_ret": "SELECT TO_CHAR(RT_BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q+" GROUP BY TO_CHAR(RT_BILL_DATE,'YYYY-MM')",
            "mc": "SELECT TO_CHAR(DOC_DATE,'YYYY-MM'), SUM(CR_AMT) FROM (SELECT DOC_DATE, CR_AMT FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" UNION ALL SELECT DOC_DATE, CR_AMT FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" UNION ALL SELECT DOC_DATE, CR_AMT FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" UNION ALL SELECT b.BILL_DATE AS DOC_DATE, NVL(p.DR_AMT,0) AS CR_AMT FROM IAS_BILL_MST b JOIN IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%' WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0 AND b.BILL_DATE>="+P+" AND b.BILL_DATE<"+Q+" UNION ALL SELECT DOC_DATE, -CR_AMT FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND TO_CHAR(A_CODE) LIKE '111%' AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+") GROUP BY TO_CHAR(DOC_DATE,'YYYY-MM')",
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
                        if key in ["sales", "sales_ret", "collect", "purch", "gross", "gross_ret", "netprofit", "recv", "invval", "ov", "ov_ret", "iv"]:
                            r = cur.fetchone()
                            results[key] = round(float(r[0]),2) if r and r[0] is not None else 0.0
                        else:
                            m = {}
                            for r in cur.fetchall():
                                m[str(r[0])] = round(float(r[1] or 0),2)
                            results[key] = m
                    except Exception as e:
                        logger.error("Exception occurred:", exc_info=True)
                        results[key] = (0.0 if key not in ["ms", "ms_ret", "mc", "mp", "rs", "rs_ret", "its", "its_ret"] else {})

        sales = results["sales"]; sales_ret = results["sales_ret"]
        d["sales"] = round(sales - sales_ret, 2)
        d["collect"] = results["collect"]
        d["purch"] = results["purch"]
        d["gross"] = round(results["gross"] - results["gross_ret"], 2)
        d["netprofit"] = results["netprofit"]
        d["recv"] = results["recv"]
        d["invval"] = results["invval"]
        d["vat"] = round((results["ov"] - results["ov_ret"]) - results["iv"], 2)
        
        ms = results["ms"]; ms_ret = results["ms_ret"]
        mc = results["mc"]; mp = results["mp"]
        
        months=sorted(set(list(ms)+list(ms_ret)+list(mc)+list(mp)))
        d["months"]=months
        d["msales"]=[round(ms.get(x,0) - ms_ret.get(x,0), 2) for x in months]
        d["mcollect"]=[mc.get(x,0) for x in months]
        d["mpurch"]=[mp.get(x,0) for x in months]
        
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
        d_from = request.args.get("date_from", datetime.now().strftime("%Y-01-01"))
        d_to = request.args.get("date_to", datetime.now().strftime("%Y-12-31"))
        force_refresh = request.args.get("force_refresh", "0")
        
        cache_key = f"{d_from}_{d_to}"
        current_time = time.time()
        
        # التنظيف التلقائي لمنع تسرب الذاكرة (Memory Leak)
        expired_keys = [k for k, v in _DASH_CACHE.items() if current_time - v['time'] >= 900]
        for k in expired_keys:
            del _DASH_CACHE[k]
            
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
