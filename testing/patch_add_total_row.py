import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

new_func = """def add_total_row(cols, rows, rpt_id=""):
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
            total_row.append(str(rows[-1][col_idx]) if rows and rows[-1][col_idx] is not None else "0.00")
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
                
    return cols, [tuple(total_row)] + rows"""

old_func_pattern = re.compile(r'def add_total_row\(cols, rows, rpt_id=\"\"\):.*?return cols, \[tuple\(total_row\)\] \+ rows', re.DOTALL)
new_content = old_func_pattern.sub(new_func, content)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Patched add_total_row successfully.")
