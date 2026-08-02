import os

with open('testing/temp_aging.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('def run_perf_aging_fifo(rpt, args):', 'def run_perf_aging_analytical(rpt, args):')

content = content.replace('rep_results = defaultdict(lambda: {"cust_count": set(), "b": [0.0]*5, "total": 0.0})', 'cust_results = defaultdict(lambda: {"b": [0.0]*5, "total": 0.0})')
content = content.replace('rep_results[r_code]["cust_count"].add(ccode)\n            rep_results[r_code]["total"] += cr', 'cust_results[ccode]["total"] += cr')
content = content.replace('rep_results[r_code]["b"][bucket_of(age)] += amt', 'cust_results[ccode]["b"][bucket_of(age)] += amt')

content = content.replace('''
    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                rep_results[r_code]["total"] += c_sales
                rep_results[r_code]["b"][0] += c_sales
''', '''
    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                cust_results["CASH_SALES_" + str(r_code)]["total"] += c_sales
                cust_results["CASH_SALES_" + str(r_code)]["b"][0] += c_sales
''')

content = content.replace('''
    cols = ["كود المندوب", "اسم المندوب", "عدد العملاء", "0-30", "31-60", "61-90", "91-120", "أكثر من 120", "إجمالي التحصيل"]
    rows = []
    for r_code, data in rep_results.items():
        row = (
            r_code,
            rep_name.get(r_code, r_code),
            len(data["cust_count"]),
            f"{data['b'][0]:,.2f}",
            f"{data['b'][1]:,.2f}",
            f"{data['b'][2]:,.2f}",
            f"{data['b'][3]:,.2f}",
            f"{data['b'][4]:,.2f}",
            f"{data['total']:,.2f}"
        )
        rows.append(row)
        
    rows.sort(key=lambda x: float(x[8].replace(',','')), reverse=True)
    return cols, rows
''', '''
    cols = ["رقم العميل", "اسم العميل", "0-30", "31-60", "61-90", "91-120", "أكثر من 120", "إجمالي التحصيل"]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER")
            cust_names = {str(c): str(n) for c, n in cur.fetchall()}
            
    for ccode, data in cust_results.items():
        if str(ccode).startswith("CASH_SALES_"):
            c_name = "مبيعات نقدية (للمندوب)"
            disp_code = "-"
        else:
            c_name = cust_names.get(str(ccode), str(ccode))
            disp_code = str(ccode)
            
        row = (
            disp_code,
            c_name,
            f"{data['b'][0]:,.2f}",
            f"{data['b'][1]:,.2f}",
            f"{data['b'][2]:,.2f}",
            f"{data['b'][3]:,.2f}",
            f"{data['b'][4]:,.2f}",
            f"{data['total']:,.2f}"
        )
        rows.append(row)
        
    rows.sort(key=lambda x: float(x[7].replace(',','')), reverse=True)
    return cols, rows
''')

with open('testing/temp_aging_analytical.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Generated analytical function in temp_aging_analytical.py")
