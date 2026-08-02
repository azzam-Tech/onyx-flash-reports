import re

def modify_app_py():
    path = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Inject into TABS
    tabs_pattern = r'(\{"id":"debt_movement_summary",.*?"sql":""\},)'
    
    new_report_tab = r''' {"id":"net_debt_movement_summary","title":"حركة المديونية الصافية للمبيعات (مرن)","fn":"run_net_debt_movement_summary","params":[
      {"name":"year_val","label":"السنة","type":"select","default":"2026","options":[["2026","2026"],["2025","2025"],["2024","2024"],["2023","2023"],["2022","2022"]]},
      {"name":"period_type","label":"نوع التقرير","type":"select","default":"monthly","options":[["monthly","شهري"],["quarterly","ربعي"],["semi_annual","نصفي"],["annual","سنوي"]]},
      {"name":"period_val","label":"الشهر / الربع / النصف","type":"select","default":"all","options":[
        ["all","الكل / كامل السنة"],
        ["1","01 - يناير / Q1 / H1"],
        ["2","02 - فبراير / Q2 / H2"],
        ["3","03 - مارس / Q3"],
        ["4","04 - إبريل / Q4"],
        ["5","05 - مايو"],
        ["6","06 - يونيو"],
        ["7","07 - يوليو"],
        ["8","08 - أغسطس"],
        ["9","09 - سبتمبر"],
        ["10","10 - أكتوبر"],
        ["11","11 - نوفمبر"],
        ["12","12 - ديسمبر"]
      ]},
      {"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترات الزمنية"]]},
      {"name":"exclude_suppliers","label":"استبعاد تسويات الموردين (إخفاء السوالب)","type":"select","default":"1","options":[["1","استبعاد (الصافي الحقيقي)"],["0","إبقاء (مطابق لأونكس)"]]}
    ],"sql":""},'''
    
    def repl_tabs(m):
        return m.group(1) + '\n' + new_report_tab
        
    content = re.sub(tabs_pattern, repl_tabs, content, count=1, flags=re.DOTALL)
    
    # 2. Extract run_debt_movement_summary function
    start_str = "def run_debt_movement_summary(rpt, args):"
    end_str = "return cols, rows"
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str, start_idx)
    
    if start_idx == -1 or end_idx == -1:
        print("Could not find function!")
        return
        
    end_idx += len(end_str)
    
    orig_func = content[start_idx:end_idx]
    
    # 3. Create the new function by modifying the original
    new_func = orig_func.replace('def run_debt_movement_summary', 'def run_net_debt_movement_summary')
    
    # Add exclude_suppliers param extraction
    param_extract = '    grp_by = args.get("grp_by", "cc")\n    exclude_suppliers = args.get("exclude_suppliers", "1")'
    new_func = new_func.replace('    grp_by = args.get("grp_by", "cc")', param_extract)
    
    # Add supplier filter logic
    supplier_logic = """
    supplier_filter = "AND p.C_CODE IS NOT NULL AND TO_CHAR(p.A_CODE) LIKE '121%'" if exclude_suppliers == "1" else "AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)"
    
    sql = f\"\"\"
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 {supplier_filter}
"""
    
    old_sql_start = """    sql = f\"\"\"
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)"""
        
    new_func = new_func.replace(old_sql_start, supplier_logic)
    
    old_sql_close = """    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)"""
        
    new_sql_close = """    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 {supplier_filter}"""
        
    new_func = new_func.replace(old_sql_close, new_sql_close)
    
    # 4. Inject the new function immediately after the original
    content = content[:end_idx] + '\n\n' + new_func + '\n' + content[end_idx:]
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Successfully modified app.py!")

if __name__ == "__main__":
    modify_app_py()
