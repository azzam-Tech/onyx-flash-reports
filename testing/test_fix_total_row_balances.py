import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn, run_report, find_report

def smart_add_total_row(cols, rows):
    if not rows:
        return cols, rows
        
    totals = [0.0] * len(cols)
    is_numeric = [False] * len(cols)
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        
        # Only exclude code/date/phone/name or EXACT running balance column 'الرصيد' (when not debit/credit)
        if any(x in col_name for x in ['كود', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'اسم', 'عنوان', 'ملاحظات', 'بيان', 'مستند']):
            continue
        if col_name == 'كود' or col_name == 'رقم' or col_name == 'الرصيد':
            continue
            
        for row in rows[:10]:
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
        if row and len(row) > 1 and str(row[1]).strip() == "رصيد افتتاحي":
            continue
        for col_idx in range(len(cols)):
            if is_numeric[col_idx]:
                val = row[col_idx]
                if val is not None and val != "":
                    if isinstance(val, str):
                        try:
                            totals[col_idx] += float(val.replace(',', ''))
                        except ValueError:
                            pass
                    else:
                        totals[col_idx] += float(val)
                        
    total_row = []
    has_total_label = False
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        # Single running balance column in account statement
        if col_name == 'الرصيد' or col_name == 'balance':
            total_row.append(str(rows[-1][col_idx]) if rows else "0.00")
        elif is_numeric[col_idx]:
            val = totals[col_idx]
            if val == 0:
                total_row.append("0.00")
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
from app import run_sql_report
cols, raw_rows = run_sql_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-12-31"})
cols, fixed_rows = smart_add_total_row(cols, raw_rows)

print(f"FIXED TOTAL ROW FOR {rpt['id']}:")
print("COLUMNS:", cols)
print("TOTAL ROW:", fixed_rows[0])
