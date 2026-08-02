with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

start_pos = content.find('{"id":"statement"')
end_pos = content.find('{"id":"aging"')

new_sql = """{"id":"statement","title":"كشف حساب عميل","params":[{"name":"c_code","label":"كود العميل","type":"text","default":"1381"},DFROM,DTO],"sql":\"\"\"
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
           AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
       ),
       trans AS (
         SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC,
                NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
         WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
           AND NVL(p.DOC_TYPE,0) <> 0
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
         SELECT TO_CHAR(TO_DATE(:date_from,'YYYY-MM-DD')-1, 'YYYY-MM-DD') AS "التاريخ",
                'رصيد افتتاحي' AS "نوع المستند",
                NULL AS "رقم المستند",
                'رصيد ما قبل الفترة' AS "البيان",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                TO_CHAR(NVL(bal,0),'FM999,999,990.00') AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'),
                t.jv_name,
                t.DOC_NO,
                t.DOC_DESC,
                TO_CHAR(t.dr,'FM999,999,990.00'),
                TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3 FETCH FIRST 1000 ROWS ONLY\"\"\"},\n    """

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + new_sql + content[end_pos:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully replaced statement query in app.py!")
else:
    print(f"Error finding positions: start={start_pos}, end={end_pos}")
