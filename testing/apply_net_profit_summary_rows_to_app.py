app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update add_total_row to accept rpt_id and generate profit summary rows for true_income_statement
idx_def = content.find('def add_total_row(')
if idx_def == -1:
    print("ERROR: def add_total_row not found!")
    sys.exit(1)

end_idx_def = content.find('def ', idx_def + 10)

new_add_total_row = """def add_total_row(cols, rows, rpt_id=""):
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
    
    # Net Profit summary rows for true_income_statement
    if rpt_id == "true_income_statement" and len(cols) == 8:
        mv_dr = totals[4] if is_numeric[4] else 0.0
        mv_cr = totals[5] if is_numeric[5] else 0.0
        period_net = mv_cr - mv_dr
        
        bal_dr = totals[6] if is_numeric[6] else 0.0
        bal_cr = totals[7] if is_numeric[7] else 0.0
        final_net = bal_cr - bal_dr
        
        p_row = ["", "رصيد الفترة صافي الربح", "", "", "", "", "", ""]
        if period_net >= 0:
            p_row[5] = f"{period_net:,.2f}"
        else:
            p_row[4] = f"{abs(period_net):,.2f}"
        summary_rows.append(tuple(p_row))
        
        f_row = ["", "الرصيد النهائي صافي الربح", "", "", "", "", "", ""]
        if final_net >= 0:
            f_row[7] = f"{final_net:,.2f}"
        else:
            f_row[6] = f"{abs(final_net):,.2f}"
        summary_rows.append(tuple(f_row))
                
    return cols, summary_rows + rows

"""

content = content[:idx_def] + new_add_total_row + content[end_idx_def:]

# 2. Update run_report call to pass rpt["id"] to add_total_row
run_rpt_old = "return add_total_row(cols, rows)"
run_rpt_new = "return add_total_row(cols, rows, rpt.get('id', ''))"
content = content.replace(run_rpt_old, run_rpt_new)

# 3. Add CSS styling for prof-row1 and prof-row2
css_old = "tr.tot-row td { background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }"
css_new = """tr.tot-row td { background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }
tr.prof-row1 td { background: #dcfce7 !important; color: #15803d !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 1.5px solid #bbf7d0 !important; }
tr.prof-row2 td { background: #dbeafe !important; color: #1e40af !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #93c5fd !important; }"""
if css_old in content:
    content = content.replace(css_old, css_new)

# 4. Update Jinja tbody rendering in Jinja template
tbody_old = '<tbody>{% for row in rows %}<tr class="{{ \'tot-row\' if (loop.first and (row[0]==\'الإجمالي\' or row[1]==\'الإجمالي\')) else \'\' }}">{% for cell in row %}<td>{{ \'\' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody>'
tbody_new = '<tbody>{% for row in rows %}{% set r0 = (row[0]|string).strip() %}{% set r1 = (row[1]|string).strip() %}{% set cls = \'\' %}{% if r0==\'الإجمالي\' or r1==\'الإجمالي\' %}{% set cls = \'tot-row\' %}{% elif \'رصيد الفترة صافي\' in r1 %}{% set cls = \'prof-row1\' %}{% elif \'الرصيد النهائي صافي\' in r1 %}{% set cls = \'prof-row2\' %}{% endif %}<tr class="{{ cls }}">{% for cell in row %}<td>{{ \'\' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody>'

if tbody_old in content:
    content = content.replace(tbody_old, tbody_new)

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("APPLIED NET PROFIT SUMMARY ROWS AND STYLING TO APP.PY SUCCESSFULLY!")
