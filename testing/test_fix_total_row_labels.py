import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn, run_sql_report, find_report

def add_total_row(cols, rows):
    if not rows:
        return cols, rows
        
    totals = [0.0] * len(cols)
    is_numeric = [False] * len(cols)
    has_values = [False] * len(cols)
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        
        # Exclude code/date/phone/name or EXACT running balance column 'الرصيد' (when not debit/credit)
        if any(x in col_name for x in ['كود', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'عنوان', 'ملاحظات', 'بيان', 'مستند']):
            continue
        if col_name in ('كود', 'رقم', 'الرقم', 'اسم', 'الاسم', 'الحساب', 'اسم الحساب', 'الرصيد'):
            continue
            
        for row in rows:
            val = row[col_idx]
            if val is None or val == "": 
                continue
            if isinstance(val, (int, float)):
                is_numeric[col_idx] = True
                break
            if isinstance(val, str):
                try:
                    float(val.replace(',', ''))
                    is_numeric[col_idx] = True
                    break
                except ValueError:
                    pass
                    
    for row in rows:
        # Skip opening balance row in customer statement running balance
        if row and len(row) > 1 and str(row[1]).strip() == "رصيد افتتاحي":
            continue
        for col_idx in range(len(cols)):
            if is_numeric[col_idx]:
                val = row[col_idx]
                if val is not None and val != "":
                    if isinstance(val, str):
                        try:
                            totals[col_idx] += float(val.replace(',', ''))
                            has_values[col_idx] = True
                        except ValueError:
                            pass
                    else:
                        totals[col_idx] += float(val)
                        has_values[col_idx] = True
                        
    total_row = []
    has_total_label = False
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        # Single running balance column in account statement
        if col_name == 'الرصيد' or col_name == 'balance':
            total_row.append(str(rows[-1][col_idx]) if rows else "")
        elif is_numeric[col_idx]:
            val = totals[col_idx]
            if not has_values[col_idx] or val == 0:
                total_row.append("")
            else:
                total_row.append(f"{val:,.2f}")
        else:
            if not has_total_label:
                total_row.append("الإجمالي")
                has_total_label = True
            else:
                total_row.append("")
                
    return cols, [tuple(total_row)] + rows

# Test with true_income_statement report
tab, rpt = find_report("prof", "true_income_statement")
cols, raw_rows = run_sql_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-12-31"})
cols, fixed_rows = add_total_row(cols, raw_rows)

print(f"REFINED TOTAL ROW FOR {rpt['id']}:")
print("COLUMNS:", cols)
print("TOTAL ROW:", fixed_rows[0])
