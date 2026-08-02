import re

filepath = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

old_block = r'(\{"id":"net_sales_cc".*?"sql":""")(.*?)(\"""\})'

new_sql = """
      WITH sales_data AS (
          SELECT CC_CODE,
                 SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT,0)) as sales
          FROM IAS20261.IAS_BILL_MST
          WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
            AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND BILL_DOC_TYPE IN (1,4)
          GROUP BY CC_CODE
      ),
      returns_data AS (
          SELECT CC_CODE,
                 SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT,0)) as returns
          FROM IAS20261.IAS_RT_BILL_MST
          WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
            AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND RT_BILL_DOC_TYPE IN (1,4)
          GROUP BY CC_CODE
      ),
      discount_notice AS (
          SELECT CC_CODE, SUM(NVL(CR_AMT,0)) as ext_disc
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
             TO_CHAR(SUM(NVL(d.ext_disc, 0)),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
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
   """

# Need to be very careful to only replace group 2
content = re.sub(old_block, r'\g<1>' + new_sql + r'\g<3>', content, flags=re.DOTALL)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("net_sales_cc patched!")
