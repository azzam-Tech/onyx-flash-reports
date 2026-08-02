import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

new_report = """   {"id":"sales_vs_collection","title":"المبيعات مقابل التحصيل","params":[DFROM,DTO],"sql":\"\"\"
     WITH sales_data AS (
         SELECT CC_CODE,
                SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
         FROM IAS20261.IAS_BILL_MST
         WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
           AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
           AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
         GROUP BY CC_CODE
     ),
     returns_data AS (
         SELECT CC_CODE,
                SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
         FROM IAS20261.IAS_RT_BILL_MST
         WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
           AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
           AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
         GROUP BY CC_CODE
     ),
     discount_notice AS (
         SELECT CC_CODE, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
         FROM IAS20261.IAS_POST_DTL
         WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
           AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         GROUP BY CC_CODE
     ),
     net_sales AS (
         SELECT NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) AS CC_CODE,
                SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales_amt
         FROM sales_data s
         FULL OUTER JOIN returns_data r ON s.CC_CODE = r.CC_CODE
         FULL OUTER JOIN discount_notice d ON NVL(s.CC_CODE, r.CC_CODE) = d.CC_CODE
         GROUP BY NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
     ),
     all_trans AS (
         SELECT TO_CHAR(CC_CODE) as grp_code,
                CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(CC_CODE), 0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(b.CC_CODE), 0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
         FROM IAS20261.IAS_BILL_MST b
         JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
         WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
           AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         UNION ALL
         SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
         FROM IAS20261.IAS_POST_DTL
         WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
           AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     ),
     base_collection AS (
         SELECT grp_code,
                (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown) + SUM(net_jrn) + SUM(cash_sales) - SUM(cash_ret)) as total_inc
         FROM all_trans
         WHERE grp_code IS NOT NULL
         GROUP BY grp_code
     )
     SELECT NVL(ns.CC_CODE, bc.grp_code) AS "المركز",
            MAX(cc.CC_A_NAME) AS "اسم المركز",
            TO_CHAR(SUM(NVL(ns.net_sales_amt, 0)), 'FM999,999,999,990.00') AS "صافي المبيعات",
            TO_CHAR(SUM(NVL(ns.net_sales_amt, 0)) * 1.15, 'FM999,999,999,990.00') AS "صافي المبيعات بالضريبة",
            TO_CHAR(SUM(NVL(bc.total_inc, 0)), 'FM999,999,999,990.00') AS "إجمالي التحصيل"
     FROM net_sales ns
     FULL OUTER JOIN base_collection bc ON ns.CC_CODE = bc.grp_code
     LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE = NVL(ns.CC_CODE, bc.grp_code)
     GROUP BY NVL(ns.CC_CODE, bc.grp_code)
     HAVING (SUM(NVL(ns.net_sales_amt, 0)) <> 0 OR SUM(NVL(bc.total_inc, 0)) <> 0)
     ORDER BY SUM(NVL(ns.net_sales_amt, 0)) DESC
     FETCH FIRST 300 ROWS ONLY\"\"\"},
"""

target = 'ORDER BY b.BILL_DATE DESC, b.BILL_NO DESC FETCH FIRST 300 ROWS ONLY"""},'

if target in content:
    content = content.replace(target, target + "\n" + new_report)
    with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
        f.write(content)
    print("SUCCESS")
else:
    print("FAILED to find target")
