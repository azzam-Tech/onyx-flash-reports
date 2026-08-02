with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

start_pos = content.find('{"id":"by_item","title":"حسب الصنف"')
end_pos = content.find('{"id":"by_customer","title":"حسب العميل"')

new_by_item_report = """{"id":"by_item","title":"حسب الصنف","params":[DFROM,DTO,ITM,REP],"sql":\"\"\"
    WITH dtl_disc_sum AS (
        SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
        FROM IAS20261.IAS_BILL_DTL
        GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
    ),
    rt_dtl_disc_sum AS (
        SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
        FROM IAS20261.IAS_RT_BILL_DTL
        GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
    ),
    item_sales AS (
        SELECT dt.I_CODE as item_code,
               NVL(dt.I_QTY,0) as sale_qty,
               0 as return_qty,
               (NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0)) as gross_amt,
               NVL(dt.DIS_AMT,0) as item_disc,
               CASE WHEN NVL(b.BILL_AMT,0) > 0 THEN
                   ((NVL(dt.I_QTY,0) * NVL(dt.I_PRICE,0)) / b.BILL_AMT) * GREATEST(0, NVL(b.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
               ELSE 0 END as extra_header_disc
        FROM IAS20261.IAS_BILL_DTL dt
        JOIN IAS20261.IAS_BILL_MST b 
          ON b.BILL_DOC_TYPE = dt.BILL_DOC_TYPE AND b.BILL_NO = dt.BILL_NO AND b.BILL_SER = dt.BILL_SER
        LEFT JOIN dtl_disc_sum dds 
          ON dds.BILL_DOC_TYPE = dt.BILL_DOC_TYPE AND dds.BILL_NO = dt.BILL_NO AND dds.BILL_SER = dt.BILL_SER
        LEFT JOIN IAS20261.IAS_ITM_MST m ON TO_CHAR(m.I_CODE) = TO_CHAR(dt.I_CODE)
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND (:i_code IS NULL OR TO_CHAR(dt.I_CODE) = :i_code OR m.I_NAME LIKE '%' || :i_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
    ),
    item_returns AS (
        SELECT rdt.I_CODE as item_code,
               0 as sale_qty,
               NVL(rdt.I_QTY,0) as return_qty,
               -(NVL(rdt.I_QTY,0) * NVL(rdt.I_PRICE,0)) as gross_amt,
               -NVL(rdt.DIS_AMT,0) as item_disc,
               -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                   ((NVL(rdt.I_QTY,0) * NVL(rdt.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
               ELSE 0 END as extra_header_disc
        FROM IAS20261.IAS_RT_BILL_DTL rdt
        JOIN IAS20261.IAS_RT_BILL_MST r 
          ON r.RT_BILL_DOC_TYPE = rdt.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = rdt.RT_BILL_NO AND r.RT_BILL_SER = rdt.RT_BILL_SER
        LEFT JOIN rt_dtl_disc_sum rdds 
          ON rdds.RT_BILL_DOC_TYPE = rdt.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO = rdt.RT_BILL_NO AND rdds.RT_BILL_SER = rdt.RT_BILL_SER
        LEFT JOIN IAS20261.IAS_ITM_MST m ON TO_CHAR(m.I_CODE) = TO_CHAR(rdt.I_CODE)
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND (:i_code IS NULL OR TO_CHAR(rdt.I_CODE) = :i_code OR m.I_NAME LIKE '%' || :i_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
    ),
    all_item_trans AS (
        SELECT * FROM item_sales
        UNION ALL
        SELECT * FROM item_returns
    )
    SELECT t.item_code AS "كود الصنف",
           MAX(m.I_NAME) AS "اسم الصنف",
           TO_CHAR(SUM(t.sale_qty),'FM999,999,990.00') AS "كمية المبيعات",
           TO_CHAR(SUM(t.return_qty),'FM999,999,990.00') AS "كمية المردودات (-)",
           TO_CHAR(SUM(t.sale_qty - t.return_qty),'FM999,999,990.00') AS "صافي الكمية المباعة",
           TO_CHAR(SUM(t.gross_amt),'FM999,999,990.00') AS "إجمالي قيمة المبيعات",
           TO_CHAR(SUM(t.item_disc + t.extra_header_disc),'FM999,999,990.00') AS "إجمالي الخصومات (-)",
           TO_CHAR(SUM(t.gross_amt - t.item_disc - t.extra_header_disc),'FM999,999,990.00') AS "الصافي بدون الضريبة"
    FROM all_item_trans t
    LEFT JOIN IAS20261.IAS_ITM_MST m ON TO_CHAR(m.I_CODE) = TO_CHAR(t.item_code)
    GROUP BY t.item_code
    ORDER BY SUM(t.gross_amt - t.item_disc - t.extra_header_disc) DESC
    FETCH FIRST 300 ROWS ONLY\"\"\"},\n    """

if start_pos != -1 and end_pos != -1:
    content = content[:start_pos] + new_by_item_report + content[end_pos:]
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched by_item report query in app.py!")
else:
    print(f"Error finding positions: start={start_pos}, end={end_pos}")
