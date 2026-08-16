import sys
import re

handlers_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\report_handlers.py'
config_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\reports_config.py'

# 1. Modify report_handlers.py
with open(handlers_path, 'r', encoding='utf-8') as f:
    handlers_content = f.read()

func_code = """
def run_workflow_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    rep_code = args.get("rep_code", "")
    if not rep_code:
        rep_code = None
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ""
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_col = "TO_CHAR(p.C_CODE)"
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(p.C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
        rep_filter = "AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(p.DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(p.DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else:
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
    else:
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f\"\"\"
    WITH sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,
               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    ),
    all_codes AS (
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col
    FROM all_codes ac
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
      {rep_filter}
      GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    \"\"\"

    cols = [
        code_label,
        name_label,
        "صافي المبيعات شامل الضريبة",
        "إجمالي التحصيل",
        "الفرق (المبيعات - التحصيل)",
        "نسبة التحصيل",
        "إجمالي المبيعات بدون الضريبة",
        "الهدف",
        "الفرق (الهدف - المبيعات)"
    ]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            params = {"date_from": date_from, "date_to": date_to}
            if ":rep_code" in sql: params["rep_code"] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, ns_vat, ns_no_vat, col in cur.fetchall():
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                
                total_due = ns_vat_val
                if total_due > 0:
                    col_ratio = (col_val / total_due) * 100
                else:
                    col_ratio = 0.0
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                diff_sales_col = ns_vat_val - col_val
                diff_target_sales = target_val - ns_no_vat_val if target_val > 0 else 0.0
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff_sales_col:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{ns_no_vat_val:,.2f}",
                    target_str,
                    f"{diff_target_sales:,.2f}" if target_val > 0 else ""
                ))
                
    return cols, rows

"""

if "def run_workflow_summary" not in handlers_content:
    handlers_content += "\n" + func_code
    
    # Update add_total_row
    old_logic = 'if rpt_id == "debt_movement_summary" and len(cols) >= 11:'
    new_logic = '''if rpt_id == "debt_movement_summary" and len(cols) >= 11:
        try:
            t_open = totals[2] if is_numeric[2] else 0.0
            t_sales_vat = totals[3] if is_numeric[3] else 0.0
            t_col = totals[4] if is_numeric[4] else 0.0
            t_sales_no_vat = totals[8] if is_numeric[8] else 0.0
            t_target = totals[9] if is_numeric[9] else 0.0
            
            if t_target > 0:
                total_row[10] = f"{t_target - t_sales_no_vat:,.2f}"
            
            t_due = t_open + t_sales_vat
            if t_due > 0:
                total_row[6] = f"{(t_col / t_due) * 100:,.2f}%"
        except Exception:
            pass

    if rpt_id == "workflow_summary" and len(cols) >= 9:
        try:
            t_sales_vat = totals[2] if is_numeric[2] else 0.0
            t_col = totals[3] if is_numeric[3] else 0.0
            t_sales_no_vat = totals[6] if is_numeric[6] else 0.0
            t_target = totals[7] if is_numeric[7] else 0.0
            
            if t_target > 0:
                total_row[8] = f"{t_target - t_sales_no_vat:,.2f}"
            
            t_due = t_sales_vat
            if t_due > 0:
                total_row[5] = f"{(t_col / t_due) * 100:,.2f}%"
        except Exception:
            pass
            
    if False:'''
    handlers_content = handlers_content.replace(old_logic, new_logic)

    with open(handlers_path, 'w', encoding='utf-8') as f:
        f.write(handlers_content)


# 2. Modify reports_config.py
with open(config_path, 'r', encoding='utf-8') as f:
    config_content = f.read()

config_entry = """    {"id":"workflow_summary","title":"ملخص سير العمل","fn":"run_workflow_summary","params":[
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
      {"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترة الزمنية"]]},
      {"name":"rep_code","label":"تصفية بمندوب معين (اختياري)","type":"text","default":""}
    ]},
"""

if "workflow_summary" not in config_content:
    # insert after debt_movement_summary in TABS
    old_tab_entry = '{"id":"debt_movement_summary","title":"تقرير حركة المديونية والتحصيل الدوري","fn":"run_debt_movement_summary"'
    # We find the full block of debt_movement_summary in TABS and insert workflow_summary right before it or after it.
    idx = config_content.find(old_tab_entry)
    if idx != -1:
        config_content = config_content[:idx] + config_entry + config_content[idx:]
        
    # insert in REPORTS array as well (this is near the end)
    old_report_entry = '    {"id":"debt_movement_summary","title":"تقرير حركة المديونية والتحصيل الدوري","fn":"run_debt_movement_summary"'
    idx2 = config_content.rfind(old_report_entry)
    if idx2 != -1 and idx2 != idx:
        config_content = config_content[:idx2] + config_entry + config_content[idx2:]
        
    with open(config_path, 'w', encoding='utf-8') as f:
        f.write(config_content)
