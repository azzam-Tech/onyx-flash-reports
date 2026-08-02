with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update statement SQL query in app.py
old_statement_sql = """       WITH open_bal AS (
         SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
           AND DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD')
       ),
       trans AS (
         SELECT p.DOC_DATE, d.JV_NAME, p.DOC_NO, p.DOC_DESC, NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
         WHERE p.C_CODE = :c_code AND NVL(p.DOC_POST,0)=1
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
         SELECT TO_CHAR(TO_DATE(:date_from,'YYYY-MM-DD')-1, 'YYYY-MM-DD') AS "التاريخ", 'رصيد افتتاحي' AS "نوع المستند",
                NULL AS "رقم المستند", 'رصيد ما قبل الفترة' AS "البيان",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                TO_CHAR(NVL(bal,0),'FM999,999,990.00') AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'), t.JV_NAME, t.DOC_NO, t.DOC_DESC,
                TO_CHAR(t.dr,'FM999,999,990.00'), TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3 FETCH FIRST 1000 ROWS ONLY"""

new_statement_sql = """       WITH open_bal AS (
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
       ) ORDER BY s1, s2, s3 FETCH FIRST 1000 ROWS ONLY"""

if old_statement_sql in content:
    content = content.replace(old_statement_sql, new_statement_sql)
    print("Updated statement query successfully!")
else:
    print("Warning: old_statement_sql not found cleanly, checking alternative replacement.")

# 2. Update add_total_row to handle running balance column ('الرصيد') correctly
old_add_total_row = """    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower()
        if any(x in col_name for x in ['كود', 'رقم', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'اسم', 'حساب']):
            continue"""

new_add_total_row = """    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower()
        if any(x in col_name for x in ['كود', 'رقم', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'اسم', 'حساب', 'الرصيد', 'balance']):
            continue"""

if old_add_total_row in content:
    content = content.replace(old_add_total_row, new_add_total_row)
    print("Updated add_total_row is_numeric check for 'الرصيد'!")

# Update total_row formation in add_total_row to set 'الرصيد' to the last row's balance
old_total_formation = """    for col_idx in range(len(cols)):
        if is_numeric[col_idx]:
            total_row.append(f"{totals[col_idx]:,.2f}")
        else:
            if not has_total_label and not any(x in str(cols[col_idx]).lower() for x in ['كود', 'رقم', 'code', 'no']):
                total_row.append("الإجمالي")
                has_total_label = True
            elif not has_total_label and col_idx == 0:
                total_row.append("الإجمالي")
                has_total_label = True
            else:
                total_row.append("")"""

new_total_formation = """    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower()
        if 'الرصيد' in col_name or 'balance' in col_name:
            # For running balance columns, set total to the final row's balance instead of summing rows
            total_row.append(str(rows[-1][col_idx]) if rows else "0.00")
        elif is_numeric[col_idx]:
            total_row.append(f"{totals[col_idx]:,.2f}")
        else:
            if not has_total_label and not any(x in str(cols[col_idx]).lower() for x in ['كود', 'رقم', 'code', 'no']):
                total_row.append("الإجمالي")
                has_total_label = True
            elif not has_total_label and col_idx == 0:
                total_row.append("الإجمالي")
                has_total_label = True
            else:
                total_row.append("")"""

if old_total_formation in content:
    content = content.replace(old_total_formation, new_total_formation)
    print("Updated total_row formation for running balance column!")

with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished patching app.py!")
