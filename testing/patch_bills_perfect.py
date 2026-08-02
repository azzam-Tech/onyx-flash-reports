with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

start_pos = content.find('{"id":"bills","title":"فواتير المبيعات"')
end_pos = content.find('{"id":"by_item","title":"حسب الصنف"')

new_bills_report = """{"id":"bills","title":"فواتير المبيعات","params":[DFROM,DTO,BTYPE,REP,CST],"sql":\"\"\"
    WITH sales_invoices AS (
      SELECT CASE b.BILL_DOC_TYPE 
               WHEN 1 THEN 'مبيعات نقدية' 
               WHEN 4 THEN 'مبيعات آجلة' 
               ELSE 'مبيعات أخرى' 
             END AS doc_type_name,
             b.BILL_DOC_TYPE as doc_type,
             b.BILL_NO as bill_no,
             b.BILL_DATE as bill_date,
             TO_CHAR(b.C_CODE) as c_code,
             c.C_A_NAME as c_name,
             TO_CHAR(b.REP_CODE) as rep_code,
             sm.REPRS_A_NAME as rep_name,
             NVL(b.BILL_AMT,0) as gross_amt,
             NVL(b.DISC_AMT,0) as disc_amt,
             NVL(b.VAT_AMT,0) as vat_amt,
             (NVL(b.BILL_AMT,0) - NVL(b.DISC_AMT,0) + NVL(b.VAT_AMT,0) + NVL(b.OTHR_AMT,0)) as net_amt,
             NVL(b.BILL_POST,0) as bill_post
      FROM IAS20261.IAS_BILL_MST b
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(b.REP_CODE)
      WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND b.BILL_DOC_TYPE IN (1,4,8)
        AND (:bill_type IS NULL OR TO_CHAR(b.BILL_DOC_TYPE) = :bill_type)
        AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
        AND (:c_code IS NULL OR TO_CHAR(b.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
    ),
    return_invoices AS (
      SELECT CASE r.RT_BILL_DOC_TYPE 
               WHEN 1 THEN 'مرتجع مبيعات نقدي' 
               WHEN 4 THEN 'مرتجع مبيعات آجل' 
               ELSE 'مرتجع مبيعات' 
             END AS doc_type_name,
             r.RT_BILL_DOC_TYPE as doc_type,
             r.RT_BILL_NO as bill_no,
             r.RT_BILL_DATE as bill_date,
             TO_CHAR(r.C_CODE) as c_code,
             c.C_A_NAME as c_name,
             TO_CHAR(r.REP_CODE) as rep_code,
             sm.REPRS_A_NAME as rep_name,
             -NVL(r.BILL_AMT,0) as gross_amt,
             -NVL(r.DISC_AMT_MST,0) as disc_amt,
             -NVL(r.VAT_AMT,0) as vat_amt,
             -(NVL(r.BILL_AMT,0) - NVL(r.DISC_AMT_MST,0) + NVL(r.VAT_AMT,0)) as net_amt,
             NVL(r.RT_BILL_POST,0) as bill_post
      FROM IAS20261.IAS_RT_BILL_MST r
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = r.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
      WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND r.RT_BILL_DOC_TYPE IN (1,4,8)
        AND (:bill_type IS NULL OR TO_CHAR(r.RT_BILL_DOC_TYPE) = :bill_type OR (:bill_type = '2' AND r.RT_BILL_DOC_TYPE = 1) OR (:bill_type = '5' AND r.RT_BILL_DOC_TYPE = 4))
        AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
        AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
    ),
    all_bills AS (
      SELECT * FROM sales_invoices
      UNION ALL
      SELECT * FROM return_invoices
    )
    SELECT doc_type_name AS "نوع المستند",
           bill_no AS "رقم الفاتورة",
           TO_CHAR(bill_date,'YYYY-MM-DD') AS "التاريخ",
           NVL(c_code, 'مباشر') AS "كود العميل",
           NVL(c_name, 'عميل نقدي') AS "اسم العميل",
           NVL(rep_name, rep_code) AS "المندوب",
           TO_CHAR(gross_amt,'FM999,999,990.00') AS "المبلغ قبل الخصم",
           TO_CHAR(disc_amt,'FM999,990.00') AS "الخصم",
           TO_CHAR(vat_amt,'FM999,999,990.00') AS "الضريبة",
           TO_CHAR(net_amt,'FM999,999,990.00') AS "الصافي شامل الضريبة",
           CASE bill_post WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
    FROM all_bills
    ORDER BY bill_date DESC, bill_no DESC
    FETCH FIRST 300 ROWS ONLY\"\"\"},\n    """

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + new_bills_report + content[end_pos:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched bills report query in app.py!")
else:
    print(f"Error finding positions: start={start_pos}, end={end_pos}")
