import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn, run_sql_report, find_report

tab, rpt = find_report("prof", "true_income_statement")
cols, raw_rows = run_sql_report(rpt, {"date_from": "2026-01-01", "date_to": "2026-12-31", "rep_code": ""})

def add_total_row_with_profit(cols, rows, rpt_id=""):
    if not rows:
        return cols, rows
        
    totals = [0.0] * len(cols)
    is_numeric = [False] * len(cols)
    has_values = [False] * len(cols)
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        
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
                
    summary_rows = [tuple(total_row)]
    
    # For true_income_statement, add the two Net Profit summary rows
    if rpt_id == "true_income_statement" and len(cols) == 8:
        # col 4: رصيد الحركة مدين, col 5: رصيد الحركة دائن
        mv_dr = totals[4] if is_numeric[4] else 0.0
        mv_cr = totals[5] if is_numeric[5] else 0.0
        period_net = mv_cr - mv_dr
        
        # col 6: الأرصدة مدين, col 7: الأرصدة دائن
        bal_dr = totals[6] if is_numeric[6] else 0.0
        bal_cr = totals[7] if is_numeric[7] else 0.0
        final_net = bal_cr - bal_dr
        
        # Row 1: رصيد الفترة صافي الربح
        p_row = ["", "رصيد الفترة صافي الربح", "", "", "", "", "", ""]
        if period_net >= 0:
            p_row[5] = f"{period_net:,.2f}" # Credit (Profit)
        else:
            p_row[4] = f"{abs(period_net):,.2f}" # Debit (Loss)
        summary_rows.append(tuple(p_row))
        
        # Row 2: الرصيد النهائي صافي الربح
        f_row = ["", "الرصيد النهائي صافي الربح", "", "", "", "", "", ""]
        if final_net >= 0:
            f_row[7] = f"{final_net:,.2f}" # Credit (Profit)
        else:
            f_row[6] = f"{abs(final_net):,.2f}" # Debit (Loss)
        summary_rows.append(tuple(f_row))
                
    return cols, summary_rows + rows

cols, fixed_rows = add_total_row_with_profit(cols, raw_rows, "true_income_statement")

print(f"PROFIT SUMMARY ROWS FOR {rpt['id']}:")
print("ROW 0 (الإجمالي):", fixed_rows[0])
print("ROW 1 (رصيد الفترة صافي الربح):", fixed_rows[1])
print("ROW 2 (الرصيد النهائي صافي الربح):", fixed_rows[2])
