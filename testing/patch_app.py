import re

with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Find from `AND b.BILL_DOC_TYPE IN (1,4,2,5)` down to `{"id":"ar"`
pattern = r'(AND b\.BILL_DOC_TYPE IN \(1,4,2,5\)\s*\n\s*\),)(.*?)(\s*\{\"id\":\"ar\")'

clean_middle = '''
        UNION ALL
        SELECT REP_CODE, C_CODE,
               0 as is_sale, 0 as is_ret, 0 as sign,
               0 as amt, 0 as disc, NVL(CR_AMT,0) as ext_disc, 0 as vat, 0 as othr
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
      )
      SELECT s.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
             COUNT(DISTINCT s.C_CODE) AS "عدد العملاء",
             SUM(s.is_sale) AS "فواتير مبيعات",
             SUM(s.is_ret) AS "فواتير مرتجعات",
             TO_CHAR(SUM(s.amt * s.is_sale),'FM999,999,999,990.00') AS "المبيعات",
             TO_CHAR(SUM(s.amt * s.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
             TO_CHAR(SUM(s.disc * s.sign),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
             TO_CHAR(SUM(s.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
             TO_CHAR(SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
             TO_CHAR(SUM((s.amt - s.disc + s.vat + s.othr) * s.sign) - SUM(s.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
      FROM s LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=s.REP_CODE
      WHERE s.REP_CODE IS NOT NULL
      GROUP BY s.REP_CODE 
      ORDER BY SUM((s.amt - s.disc) * s.sign) - SUM(s.ext_disc) DESC 
      FETCH FIRST 300 ROWS ONLY"""},
    {"id":"net_sales_cc","title":"صافي المبيعات مع الخصومات (مراكز التكلفة)","params":[DFROM,DTO,{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},{"name":"inc_ext","label":"إشعار خصم مستقل (خصم)","type":"select","default":"0","options":[["1","خصم"],["0","تجاهل"]]}],"sql":"""
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
       )
       SELECT NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) AS "رقم مركز التكلفة",
              MAX(cc.CC_A_NAME) AS "اسم مركز التكلفة",
              TO_CHAR(SUM(NVL(s.sales, 0)),'FM999,999,999,990.00') AS "إجمالي المبيعات",
              TO_CHAR(SUM(NVL(r.returns, 0)),'FM999,999,999,990.00') AS "مردود المبيعات (-)",
              TO_CHAR(CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END,'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(
                SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - (CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END),
                'FM999,999,999,990.00'
              ) AS "صافي المبيعات"
       FROM sales_data s
       FULL OUTER JOIN returns_data r ON s.CC_CODE = r.CC_CODE
       FULL OUTER JOIN discount_notice d ON NVL(s.CC_CODE, r.CC_CODE) = d.CC_CODE
       LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE = NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
       WHERE (:cc_code IS NULL OR NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) = :cc_code)
       GROUP BY NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
       HAVING (SUM(NVL(s.sales, 0)) <> 0 OR SUM(NVL(r.returns, 0)) <> 0 OR SUM(NVL(d.ext_disc, 0)) <> 0)
       ORDER BY SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - (CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END) DESC
    """},
    {"id":"sales_collection_summary","title":"صافي المبيعات وإجمالي التحصيل حسب الفترة","params":[
      {"name":"year_val","label":"السنة","type":"select","default":"2026","options":[["2026","2026"],["2025","2025"],["2024","2024"],["2023","2023"],["2022","2022"]]},
      {"name":"period_type","label":"نوع التقرير","type":"select","default":"monthly","options":[["monthly","شهري"],["quarterly","ربعي"],["semi_annual","نصفي"],["annual","سنوي"]]},
      {"name":"period_val","label":"الشهر / الربع / النصف","type":"select","default":"all","options":[
        ["all","الكل / كامل السنة"],
        ["1","01 - يناير / Q1 / H1"],
        ["2","02 - فبراير / Q2 / H2"],
        ["3","03 - مارس / Q3"],
        ["4","04 - إبريل / Q4"],
        ["5","05 - مايو"],
        ["6","06 - يونيو"],
        ["7","07 - يوليو"],
        ["8","08 - أغسطس"],
        ["9","09 - سبتمبر"],
        ["10","10 - أكتوبر"],
        ["11","11 - نوفمبر"],
        ["12","12 - ديسمبر"]
      ]},
      {"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["period","الفترات الزمنية"]]}
    ],"sql":""}
  ]},
'''

new_content = re.sub(pattern, r'\1' + clean_middle + r'\3', content, flags=re.DOTALL)
if new_content != content:
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Patched app.py with regex successfully!")
else:
    print("Regex match failed.")
