with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# Add MINAMT, MAXAMT, TXTSRCH after EMPSRCH
old_params = 'EMPSRCH = {"name":"emp_search","label":"بحث بالاسم/الكود","type":"text","default":""}'
new_params = """EMPSRCH = {"name":"emp_search","label":"بحث بالاسم/الكود","type":"text","default":""}
MINAMT  = {"name":"min_amt","label":"المبلغ من (أكبر من)","type":"number","default":""}
MAXAMT  = {"name":"max_amt","label":"المبلغ إلى (أقل من)","type":"number","default":""}
TXTSRCH = {"name":"text_search","label":"بحث بالاسم/البيان","type":"text","default":""}"""

if old_params in content:
    content = content.replace(old_params, new_params)
    print("Added MINAMT, MAXAMT, TXTSRCH parameter definitions!")

# Replace employee_advances_loans report block inside TABS
start_rep = content.find('{"id":"employee_advances_loans"')
end_rep = content.find('{"id":"salesmen_hr_link"')

new_report_block = """{"id":"employee_advances_loans","title":"كشف حركة ورصيد رواتب وسلف الموظفين (بالفرز والمبالغ)","params":[DFROM,DTO,MINAMT,MAXAMT,TXTSRCH],"sql":\"\"\"
         SELECT TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
                p.DOC_NO AS "رقم المستند",
                CASE p.DOC_TYPE WHEN 1 THEN 'قيد يومية' WHEN 2 THEN 'سند قبض' WHEN 3 THEN 'سند صرف' ELSE 'قيد أونكس' END AS "نوع المستند",
                NVL(sm.REPRS_A_NAME, TO_CHAR(p.CC_CODE)) AS "الجهة / مركز التكلفة",
                TO_CHAR(NVL(p.DR_AMT, 0), 'FM999,999,990.00') AS "سلفة / راتب / مدين",
                TO_CHAR(NVL(p.CR_AMT, 0), 'FM999,999,990.00') AS "سداد / تسوية / دائن",
                NVL(p.DOC_DESC, 'قيد تلقائي') AS "اسم الموظف / البيان والتفاصيل"
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.CC_CODE)
         WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
           AND (:min_amt IS NULL OR NVL(p.DR_AMT, 0) >= TO_NUMBER(:min_amt) OR NVL(p.CR_AMT, 0) >= TO_NUMBER(:min_amt))
           AND (:max_amt IS NULL OR (NVL(p.DR_AMT, 0) <= TO_NUMBER(:max_amt) AND NVL(p.CR_AMT, 0) <= TO_NUMBER(:max_amt)))
           AND (:text_search IS NULL OR p.DOC_DESC LIKE '%' || :text_search || '%' OR sm.REPRS_A_NAME LIKE '%' || :text_search || '%')
         ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
         FETCH FIRST 500 ROWS ONLY
         \"\"\"},\n         """

if start_rep != -1 and end_rep != -1:
    content = content[:start_rep] + new_report_block + content[end_rep:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated employee_advances_loans report with min/max amount & search filters!")
else:
    print(f"Error: start_rep={start_rep}, end_rep={end_rep}")
