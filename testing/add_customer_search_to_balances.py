with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

start_pos = content.find('{"id":"balances"')
end_pos = content.find('{"id":"statement"')

new_balances_report = """{"id":"balances","title":"أرصدة العملاء","params":[DTO,CST,REP],"sql":\"\"\"
      SELECT p.C_CODE AS "كود العميل",
             MAX(c.C_A_NAME) AS "اسم العميل",
             MAX(c.REP_CODE) AS "المندوب",
             TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد (مدين)"
      FROM IAS20261.IAS_POST_DTL p
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=p.C_CODE
      WHERE p.C_CODE IS NOT NULL
        AND NVL(p.DOC_POST,0)=1
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) LIKE '%' || :c_code || '%' OR c.C_A_NAME LIKE '%' || :c_code || '%')
        AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)
      GROUP BY p.C_CODE
      HAVING SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) <> 0
      ORDER BY SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) DESC
      FETCH FIRST 300 ROWS ONLY\"\"\"},\n    """

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + new_balances_report + content[end_pos:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated balances report with customer search and rep filters!")
else:
    print(f"Error finding positions: start={start_pos}, end={end_pos}")
