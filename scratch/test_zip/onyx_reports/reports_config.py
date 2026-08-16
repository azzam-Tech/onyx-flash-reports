import os
import json
import calendar
from datetime import datetime
import calendar
from datetime import datetime

def get_current_month_range():
    now = datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    return f"{year}-{month:02d}-01", f"{year}-{month:02d}-{last_day:02d}"

def get_default_date_from():
    return get_current_month_range()[0]

def get_default_date_to():
    return get_current_month_range()[1]

SETTINGS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "settings.json")
# كل ما يخص الربح: يُخفى عند تفعيل "إخفاء الربح"
PROFIT_TABS = {"prof"}
PROFIT_REPORTS = {"fin/income_statement", "fin/cost_centers"}
def _load_raw():
    try:
        with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}
def load_hidden_raw():
    d = _load_raw()
    return set(d.get("tabs", [])), set(d.get("reports", []))
def load_hide_profit():
    return bool(_load_raw().get("hide_profit"))
def load_hidden():
    """المجموعات الفعّالة المطبَّقة على الواجهة (تشمل إخفاء الربح إن كان مفعّلاً)."""
    tabs, reps = load_hidden_raw()
    if load_hide_profit():
        tabs = tabs | PROFIT_TABS
        reps = reps | PROFIT_REPORTS
    return tabs, reps
def save_hidden(tabs, reports, hide_profit=False):
    try:
        with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
            json.dump({"tabs": list(tabs), "reports": list(reports),
                       "hide_profit": bool(hide_profit)}, f, ensure_ascii=False)
    except Exception as e:
        print("settings save error:", e)

GLOBALS_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "globals.json")

def load_globals():
    try:
        with open(GLOBALS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return {}

def save_globals(data):
    try:
        with open(GLOBALS_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print("globals save error:", e)


def resolve_period_from_code(c_code, period_type):
    c = str(c_code)
    if period_type == "monthly":
        try:
            if "-" in c: return [int(c.split("-")[1])]
        except: pass
    elif period_type == "quarterly":
        try:
            q = int(c.replace("Q", ""))
            return [q*3 - 2, q*3 - 1, q*3]
        except: pass
    elif period_type == "semi_annual":
        if "H1" in c or "الأول" in c: return [1,2,3,4,5,6]
        if "H2" in c or "الثاني" in c: return [7,8,9,10,11,12]
    return []

def get_target_amount(year_val, period_type, period_val, grp_by, row_code=None):
    if grp_by not in ("rep", "cc", "period"):
        return 0.0
    
    globals_data = load_globals()
    year_targets = globals_data.get(year_val, {})
    if not year_targets:
        return 0.0
        
    months_to_sum = []
    if grp_by == "period":
        months_to_sum = resolve_period_from_code(row_code, period_type)
    else:
        if period_val == "all":
            months_to_sum = list(range(1, 13))
        else:
            if period_type == "monthly":
                try: months_to_sum = [int(period_val)]
                except: pass
            elif period_type == "quarterly":
                try:
                    q = int(period_val)
                    months_to_sum = [q*3 - 2, q*3 - 1, q*3]
                except: pass
            elif period_type == "semi_annual":
                if period_val == "1": months_to_sum = [1, 2, 3, 4, 5, 6]
                elif period_val == "2": months_to_sum = [7, 8, 9, 10, 11, 12]
            
    total_target = 0.0
    if grp_by in ("rep", "cc") and row_code:
        rep_targets = year_targets.get(str(row_code), {})
        for m in months_to_sum:
            total_target += float(rep_targets.get(str(m), 0.0))
    elif grp_by == "period":
        for r_code, rep_targets in year_targets.items():
            for m in months_to_sum:
                total_target += float(rep_targets.get(str(m), 0.0))
                
    return total_target

DFROM = {"name":"date_from","label":"من تاريخ","type":"date","get_default": get_default_date_from}
DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","get_default": get_default_date_to}
PYEAR = {"name":"p_year","label":"السنة","type":"text","default":str(datetime.now().year)}
REP   = {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""}
INCR  = {"name":"inc_rcpt","label":"سندات القبض","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCN  = {"name":"inc_net","label":"قيود الشبكة المنفصلة","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCC  = {"name":"inc_cash","label":"المبيعات النقدية","type":"select","default":"1","options":[["1","تضمين"],["0","استبعاد"]]}
INCRT = {"name":"inc_ret","label":"المرتجع النقدي (خصم)","type":"select","default":"1","options":[["1","خصم"],["0","تجاهل"]]}
INCEX = {"name":"inc_ext","label":"إشعار خصم مستقل (خصم)","type":"select","default":"0","hidden":True,"options":[["1","خصم"],["0","تجاهل"]]}
AGETR = {"name":"aging_ranges","label":"فترات الأعمار بالأيام (مفصولة بفارزة)","type":"text","default":"2,30,60,90,120"}
GRP   = {"name":"grp_by","label":"تجميع حسب","type":"select","default":"rep","options":[["rep","المندوب"],["cc","مركز التكلفة"],["cst","العميل"]]}
CST   = {"name":"c_code","label":"العميل (اختياري)","type":"text","default":""}
ITM   = {"name":"i_code","label":"الصنف (اختياري)","type":"text","default":""}
BTYPE = {"name":"bill_type","label":"نوع المستند","type":"select","default":"",
         "options":[["","الكل"],["1","مبيعات نقدية"],["4","مبيعات آجلة"],["2","مرتجع نقدي"],["5","مرتجع آجل"]]}
EMPST   = {"name":"emp_status","label":"حالة الموظف","type":"select","default":"","options":[["","الكل"],["1","نشط فقط"],["0","موقوف/مستقيل"]]}
PAYWAY  = {"name":"pay_way","label":"طريقة استلام الراتب","type":"select","default":"","options":[["","الكل"],["2","تحويل بنكي"],["1","تسليم نقدي"]]}
EMPSRCH = {"name":"emp_search","label":"بحث بالاسم/الكود","type":"text","default":""}
MINAMT  = {"name":"min_amt","label":"المبلغ من (أكبر من)","type":"number","default":""}
MAXAMT  = {"name":"max_amt","label":"المبلغ إلى (أقل من)","type":"number","default":""}
TXTSRCH = {"name":"text_search","label":"بحث بالاسم/البيان","type":"text","default":""}

TABS = [

 {"id":"summary","title":"ملخص التقارير","icon":"M13 3h8v8h-8zM3 13h8v8H3zM13 13h8v8h-8zM3 3h8v8H3z","reports":[
       {"id":"workflow_summary","title":"ملخص سير العمل","fn":"run_workflow_summary","params":[
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
{"id":"debt_movement_summary","title":"تقرير حركة المديونية والتحصيل الدوري","fn":"run_debt_movement_summary","params":[
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
      {"name":"rep_code","label":"المندوب (مجموعة العملاء)","type":"select","default":"","options":[["", "الكل (جميع المناديب)"], ["101", "101 - مندوب عاصمة المجد"], ["102", "102 - مندوب الغنامية"], ["103", "103 - مندوب الدار البيضاء"], ["104", "104 - مندوب جدة"], ["105", "105 - مندوب خميس مشيط"], ["106", "106 - مندوب المهرجان"], ["107", "107 - مندوب 1"], ["108", "108 - مندوب 2"], ["109", "109 - مندوب 3"], ["110", "110 - مندوب 4"], ["111", "111 - مندوب 5"], ["112", "112 - مندوب 6"], ["113", "113 - مندوب الشيكات"], ["114", "114 - مندوب الصيانة"], ["115", "115 - مندوب نواس"], ["116", "116 - مندوب المهرجان"], ["117", "117 - مندوب عبدالله يسلم"], ["118", "118 - مندوب ياسر شرمان"], ["119", "119 - مندوب جاسر"], ["120", "120 - مندوب عمر الفقية"], ["121", "121 - مندوب الطيب"], ["122", "122 - مندوب عبده"], ["123", "123 - درمه سالم / جاسر"], ["124", "124 - مندوب عبدالسلام"], ["125", "125 - مندوب جابر"], ["126", "126 - مندوب عامر"], ["127", "127 - مندوب بيجو"], ["128", "128 - المندوب علي المصري نون"], ["129", "129 - دماج"], ["131", "131 - المنصة الالكترونية"], ["141", "141 - مندوب عبدالله النهدي"], ["142", "142 - مندوب احمد الحلو"], ["143", "143 - مندوب طه المصري"], ["144", "144 - مندوب محمد سالم"], ["145", "145 - مندوب اقبال الهندي"], ["146", "146 - مندوب ابو صالح"], ["147", "147 - مندوب عبدالله يسلم"], ["148", "148 - مندوب ياسر شرمان"], ["149", "149 - مندوب جاسر الهندي"], ["150", "150 - مندوب عمر الفقيه"], ["151", "151 - مندوب احمد اخو الطيب"], ["152", "152 - مندوب عبده الهندي"], ["153", "153 - مندوب ديفيد الهندي"], ["154", "154 - مندوب عبدالسلام"], ["155", "155 - مندوب جابر الهندي"], ["156", "156 - الادارة"], ["157", "157 - مندوب بيجو الهندي"], ["158", "158 - مندوب منصة اعتماد صالح سعيد"], ["159", "159 - مندوب صالح سويد"], ["160", "160 - مندوب زيد احتياط"], ["161", "161 - مندوب راضي"], ["162", "162 - مندوب عبدالسلام"], ["163", "163 - مندوب سالم النهدي"], ["164", "164 - مندوب زيد احتياك"], ["165", "165 - مخزن الطيب الدمام"], ["166", "166 - مندوب احتياطي ابو خالد"], ["167", "167 - مندوب شوقي كشافات"], ["168", "168 - مندوب موقع سرين"], ["169", "169 - مندوب نون"], ["170", "170 - مندوب امازون"], ["171", "171 - مندوب رامي شرمان"], ["172", "172 - مندوب مواقع اكترونية خارجية"], ["173", "173 - مندوب عبدالجبار"], ["174", "174 - مندوب سلرررر"], ["175", "175 - هيثم عبدالباقي"]]}
    ],"sql":""},
    {"id":"critical_debts","title":"الديون الخطرة وتوقف العملاء (مؤشر خطر)","params":[{"name":"days_threshold","label":"أيام التوقف (الحد الأدنى)","type":"number","default":"90"}],"sql":"""
      WITH customer_balances AS (
          SELECT C_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as balance
          FROM IAS20261.IAS_POST_DTL
          WHERE NVL(DOC_POST,0) = 1 AND C_CODE IS NOT NULL
          GROUP BY C_CODE
          HAVING SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) > 1000
      ),
      last_activity AS (
          SELECT C_CODE,
                 MAX(CASE WHEN NVL(CR_AMT,0) > 0 THEN DOC_DATE END) as last_payment_date,
                 MAX(CASE WHEN NVL(DR_AMT,0) > 0 AND DOC_TYPE = 4 THEN DOC_DATE END) as last_invoice_date
          FROM IAS20261.IAS_POST_DTL
          WHERE NVL(DOC_POST,0) = 1 AND C_CODE IS NOT NULL
          GROUP BY C_CODE
      )
      SELECT c.C_CODE AS "كود العميل",
             MAX(cust.C_A_NAME) AS "اسم العميل",
             MAX(sm.REPRS_A_NAME) AS "المندوب",
             TO_CHAR(c.balance, 'FM999,999,990.00') AS "المديونية الحالية",
             TO_CHAR(la.last_payment_date, 'YYYY-MM-DD') AS "تاريخ آخر سداد",
             TRUNC(SYSDATE) - TRUNC(la.last_payment_date) AS "أيام التوقف عن السداد",
             TO_CHAR(la.last_invoice_date, 'YYYY-MM-DD') AS "تاريخ آخر سحب",
             TRUNC(SYSDATE) - TRUNC(la.last_invoice_date) AS "أيام التوقف عن السحب"
      FROM customer_balances c
      JOIN last_activity la ON c.C_CODE = la.C_CODE
      JOIN IAS20261.CUSTOMER cust ON c.C_CODE = cust.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(cust.REP_CODE) = TO_CHAR(sm.REPRS_CODE)
      WHERE (TRUNC(SYSDATE) - TRUNC(la.last_payment_date) >= :days_threshold OR la.last_payment_date IS NULL)
        AND (TRUNC(SYSDATE) - TRUNC(la.last_invoice_date) >= :days_threshold OR la.last_invoice_date IS NULL)
      GROUP BY c.C_CODE, c.balance, la.last_payment_date, la.last_invoice_date
      ORDER BY c.balance DESC
    """},
 {"id":"net_debt_movement_summary","title":"حركة المديونية الصافية للمبيعات (مرن)","fn":"run_net_debt_movement_summary","params":[
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
      {"name":"rep_code","label":"المندوب (مجموعة العملاء)","type":"select","default":"","options":[["", "الكل (جميع المناديب)"], ["101", "101 - مندوب عاصمة المجد"], ["102", "102 - مندوب الغنامية"], ["103", "103 - مندوب الدار البيضاء"], ["104", "104 - مندوب جدة"], ["105", "105 - مندوب خميس مشيط"], ["106", "106 - مندوب المهرجان"], ["107", "107 - مندوب 1"], ["108", "108 - مندوب 2"], ["109", "109 - مندوب 3"], ["110", "110 - مندوب 4"], ["111", "111 - مندوب 5"], ["112", "112 - مندوب 6"], ["113", "113 - مندوب الشيكات"], ["114", "114 - مندوب الصيانة"], ["115", "115 - مندوب نواس"], ["116", "116 - مندوب المهرجان"], ["117", "117 - مندوب عبدالله يسلم"], ["118", "118 - مندوب ياسر شرمان"], ["119", "119 - مندوب جاسر"], ["120", "120 - مندوب عمر الفقية"], ["121", "121 - مندوب الطيب"], ["122", "122 - مندوب عبده"], ["123", "123 - درمه سالم / جاسر"], ["124", "124 - مندوب عبدالسلام"], ["125", "125 - مندوب جابر"], ["126", "126 - مندوب عامر"], ["127", "127 - مندوب بيجو"], ["128", "128 - المندوب علي المصري نون"], ["129", "129 - دماج"], ["131", "131 - المنصة الالكترونية"], ["141", "141 - مندوب عبدالله النهدي"], ["142", "142 - مندوب احمد الحلو"], ["143", "143 - مندوب طه المصري"], ["144", "144 - مندوب محمد سالم"], ["145", "145 - مندوب اقبال الهندي"], ["146", "146 - مندوب ابو صالح"], ["147", "147 - مندوب عبدالله يسلم"], ["148", "148 - مندوب ياسر شرمان"], ["149", "149 - مندوب جاسر الهندي"], ["150", "150 - مندوب عمر الفقيه"], ["151", "151 - مندوب احمد اخو الطيب"], ["152", "152 - مندوب عبده الهندي"], ["153", "153 - مندوب ديفيد الهندي"], ["154", "154 - مندوب عبدالسلام"], ["155", "155 - مندوب جابر الهندي"], ["156", "156 - الادارة"], ["157", "157 - مندوب بيجو الهندي"], ["158", "158 - مندوب منصة اعتماد صالح سعيد"], ["159", "159 - مندوب صالح سويد"], ["160", "160 - مندوب زيد احتياط"], ["161", "161 - مندوب راضي"], ["162", "162 - مندوب عبدالسلام"], ["163", "163 - مندوب سالم النهدي"], ["164", "164 - مندوب زيد احتياك"], ["165", "165 - مخزن الطيب الدمام"], ["166", "166 - مندوب احتياطي ابو خالد"], ["167", "167 - مندوب شوقي كشافات"], ["168", "168 - مندوب موقع سرين"], ["169", "169 - مندوب نون"], ["170", "170 - مندوب امازون"], ["171", "171 - مندوب رامي شرمان"], ["172", "172 - مندوب مواقع اكترونية خارجية"], ["173", "173 - مندوب عبدالجبار"], ["174", "174 - مندوب سلرررر"], ["175", "175 - هيثم عبدالباقي"]]},
      {"name":"exclude_suppliers","label":"استبعاد تسويات الموردين (إخفاء السوالب)","type":"select","default":"1","options":[["1","استبعاد (الصافي الحقيقي)"],["0","إبقاء (مطابق لأونكس)"]]}
    ],"sql":""}, {"id":"statement_analytic","title":"كشف حساب تحليلي","params":[{"name":"ac_code_dtl","label":"الحساب التحليلي","type":"text","default":"1381"},DFROM,DTO],"sql":"""
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE (AC_CODE_DTL = :ac_code_dtl OR C_V_CODE = :ac_code_dtl OR V_C_CODE = :ac_code_dtl) AND NVL(DOC_POST,0)=1
           AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
       ),
       trans AS (
         SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC, p.REF_NO,
                NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=1 AND d.LANG_NO=1
         WHERE (p.AC_CODE_DTL = :ac_code_dtl OR p.C_V_CODE = :ac_code_dtl OR p.V_C_CODE = :ac_code_dtl) AND NVL(p.DOC_POST,0)=1
           AND NVL(p.DOC_TYPE,0) <> 0
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","رقم المرجع","مدين","دائن","الرصيد" FROM (
         SELECT NULL AS "التاريخ",
                NULL AS "نوع المستند",
                NULL AS "رقم المستند",
                'الرصيد الإفتتاحي' AS "البيان",
                NULL AS "رقم المرجع",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                NULL AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'),
                t.jv_name,
                TO_CHAR(t.DOC_NO),
                t.DOC_DESC,
                t.REF_NO,
                TO_CHAR(t.dr,'FM999,999,990.00'),
                TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3"""}, {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """}, {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO
       SELECT 'Dynamic' as "Placeholder" FROM DUAL
       """}, {"id":"true_income_statement","title":"قائمة الدخل (الحقيقية)","params":[DFROM,DTO,REP],"sql":"""
        WITH gl_base AS (
          SELECT 
              A_CODE as acc_code,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(DR_AMT,0) ELSE 0 END) as op_dr,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(CR_AMT,0) ELSE 0 END) as op_cr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_POST_DTL
          WHERE (:rep_code IS NULL OR REP_CODE = :rep_code OR CC_CODE = :rep_code)
            AND NVL(DOC_POST,0)=1
            AND (
                A_CODE LIKE '31102%' OR A_CODE LIKE '31104%' OR A_CODE LIKE '31105%' OR A_CODE LIKE '31109%' OR A_CODE LIKE '31110%' OR
                A_CODE LIKE '32101%' OR A_CODE LIKE '32201%' OR A_CODE LIKE '32401%' OR A_CODE LIKE '32801%' OR
                A_CODE LIKE '41101%' OR A_CODE LIKE '41202%'
            )
          GROUP BY A_CODE
        ),
        inv_cogs AS (
          SELECT 
              '311010001' as acc_code,
              SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_dr,
              0 as op_cr,
              SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_dr,
              0 as mv_cr
          FROM IAS20261.IAS_BILL_MST m
          JOIN IAS20261.IAS_BILL_DTL d ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
          WHERE (:rep_code IS NULL OR m.REP_CODE = :rep_code OR m.CC_CODE = :rep_code)
        ),
        inv_cogs_ret AS (
          SELECT 
              '311030001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_RT_BILL_MST r
          JOIN IAS20261.IAS_RT_BILL_DTL d ON r.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = d.RT_BILL_NO AND r.RT_BILL_SER = d.RT_BILL_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code OR r.CC_CODE = :rep_code)
            AND r.PREV_YEAR IS NULL
        ),
        inv_cogs_ret_prev AS (
          SELECT 
              '311060001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_RT_BILL_MST r
          JOIN IAS20261.IAS_RT_BILL_DTL d ON r.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = d.RT_BILL_NO AND r.RT_BILL_SER = d.RT_BILL_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code OR r.CC_CODE = :rep_code)
            AND r.PREV_YEAR IS NOT NULL
        ),
        all_data AS (
          SELECT * FROM gl_base
          UNION ALL
          SELECT * FROM inv_cogs
          UNION ALL
          SELECT * FROM inv_cogs_ret
          UNION ALL
          SELECT * FROM inv_cogs_ret_prev
        )
        SELECT 
            d.acc_code AS "الرقم", 
            MAX(a.A_NAME) AS "الاسم",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_dr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_cr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي دائن",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_dr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_cr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة دائن",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) > 0 
                   THEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة مدين",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) > 0 
                   THEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة دائن"
        FROM all_data d
        LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = d.acc_code
        GROUP BY d.acc_code
        ORDER BY d.acc_code
      """}
 ,
   {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT],"sql":"""

      WITH 
      grp AS (
        SELECT 'rep' as typ, TO_CHAR(REPRS_CODE) as cd, MAX(REPRS_A_NAME) as nm FROM IAS20261.SALES_MAN GROUP BY TO_CHAR(REPRS_CODE)
        UNION ALL 
        SELECT 'cc' as typ, TO_CHAR(CC_CODE) as cd, MAX(CC_A_NAME) as nm FROM IAS20261.COST_CENTERS GROUP BY TO_CHAR(CC_CODE)
        UNION ALL
        SELECT 'cst' as typ, TO_CHAR(C_CODE) as cd, MAX(C_A_NAME) as nm FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)
        UNION ALL
        SELECT 'cst' as typ, 'UNKNOWN' as cd, 'عميل نقدي عام' as nm FROM DUAL
      ),
      all_trans AS (
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END as grp_code,
               CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
               0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
        FROM IAS20261.IAS_BILL_MST b
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      ),
      base AS (
        SELECT grp_code,
               SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown, SUM(unposted_rcpt) unposted_rcpt, SUM(unposted_unknown) unposted_unknown,
               (CASE WHEN :inc_rcpt='1' THEN (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown)) ELSE 0 END
              + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
              + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
              - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
              ) total_inc
        FROM all_trans
        WHERE grp_code IS NOT NULL
          AND (:rep_code IS NULL OR (:grp_by = 'rep' AND grp_code = :rep_code))
        GROUP BY grp_code
      )
      SELECT * FROM (
        SELECT b.grp_code AS "الكود", NVL(MAX(g.nm), b.grp_code) AS "الجهة / الاسم",
               TO_CHAR(MAX(b.rcpt),'FM999,999,990.00')      AS "سندات القبض",
               TO_CHAR(MAX(b.unposted_rcpt),'FM999,999,990.00') AS "سندات غير مرحلة",
               TO_CHAR(MAX(b.unposted_unknown),'FM999,999,990.00') AS "غير مرحلة (بدون عميل)",
               TO_CHAR(MAX(b.rcpt_unknown),'FM999,999,990.00') AS "إيداعات وتسويات (بدون عميل)",
               TO_CHAR(MAX(b.net_jrn),'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
               TO_CHAR(MAX(b.cash_sales),'FM999,999,990.00') AS "المبيعات النقدية",
               TO_CHAR(MAX(b.inv_disc),'FM999,999,990.00')   AS "الخصم في الفاتورة",
               TO_CHAR(MAX(b.ext_notice),'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
               TO_CHAR(MAX(b.cash_ret),'FM999,999,990.00')   AS "المرتجع النقدي (-)",
               TO_CHAR(MAX(b.total_inc),'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base b
        LEFT JOIN grp g ON g.cd = b.grp_code AND g.typ = :grp_by
        WHERE (b.rcpt > 0 OR b.net_jrn > 0 OR b.cash_sales > 0 OR b.cash_ret > 0 OR b.inv_disc > 0 OR b.ext_notice > 0 OR b.rcpt_unknown > 0 OR b.unposted_rcpt > 0 OR b.unposted_unknown > 0)
        GROUP BY b.grp_code
        ORDER BY MAX(b.total_inc) DESC
      ) 
"""}]},
 {"id":"dash","title":"لوحة القيادة","icon":"M3 13h8V3H3zM13 21h8V3h-8zM3 21h8v-6H3z","dash":True,"reports":[{"id":"overview","title":"نظرة عامة","params":[{"name":"date_from","label":"من تاريخ","type":"date","default":"2026-07-01"},{"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-12-31"}]}]},
 {"id":"sales","title":"المبيعات","icon":"M4 20V10M10 20V4M16 20v-7M22 20H2","reports":[
   {"id":"bills","title":"فواتير المبيعات","params":[DFROM,DTO,BTYPE,REP,CST],"sql":"""
    WITH sales_invoices AS (
      SELECT CASE b.BILL_DOC_TYPE 
               WHEN 1 THEN 'مبيعات نقدية' 
               WHEN 4 THEN 'مبيعات آجلة' 
               ELSE 'مبيعات أخرى' 
             END AS doc_type_name,
             b.BILL_DOC_TYPE as doc_type,
             b.BILL_NO as bill_no,
             b.BILL_DATE as bill_date,
             TO_CHAR(b.C_CODE) as c_code,
             c.C_A_NAME as c_name,
             TO_CHAR(b.REP_CODE) as rep_code,
             sm.REPRS_A_NAME as rep_name,
             NVL(b.BILL_AMT,0) as gross_amt,
             NVL(b.DISC_AMT,0) as disc_amt,
             NVL(b.VAT_AMT,0) as vat_amt,
             (NVL(b.BILL_AMT,0) - NVL(b.DISC_AMT,0) + NVL(b.VAT_AMT,0) + NVL(b.OTHR_AMT,0)) as net_amt,
             NVL(b.BILL_POST,0) as bill_post
      FROM IAS20261.IAS_BILL_MST b
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(b.REP_CODE)
      WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND b.BILL_DOC_TYPE IN (1,4,8)
        AND (:bill_type IS NULL OR TO_CHAR(b.BILL_DOC_TYPE) = :bill_type)
        AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
        AND (:c_code IS NULL OR TO_CHAR(b.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
    ),
    return_invoices AS (
      SELECT CASE r.RT_BILL_DOC_TYPE 
               WHEN 1 THEN 'مرتجع مبيعات نقدي' 
               WHEN 4 THEN 'مرتجع مبيعات آجل' 
               ELSE 'مرتجع مبيعات' 
             END AS doc_type_name,
             r.RT_BILL_DOC_TYPE as doc_type,
             r.RT_BILL_NO as bill_no,
             r.RT_BILL_DATE as bill_date,
             TO_CHAR(r.C_CODE) as c_code,
             c.C_A_NAME as c_name,
             TO_CHAR(r.REP_CODE) as rep_code,
             sm.REPRS_A_NAME as rep_name,
             -NVL(r.BILL_AMT,0) as gross_amt,
             -NVL(r.DISC_AMT_MST,0) as disc_amt,
             -NVL(r.VAT_AMT,0) as vat_amt,
             -(NVL(r.BILL_AMT,0) - NVL(r.DISC_AMT_MST,0) + NVL(r.VAT_AMT,0)) as net_amt,
             NVL(r.RT_BILL_POST,0) as bill_post
      FROM IAS20261.IAS_RT_BILL_MST r
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = r.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
      WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
        AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND r.RT_BILL_DOC_TYPE IN (1,4,8)
        AND (:bill_type IS NULL OR TO_CHAR(r.RT_BILL_DOC_TYPE) = :bill_type OR (:bill_type = '2' AND r.RT_BILL_DOC_TYPE = 1) OR (:bill_type = '5' AND r.RT_BILL_DOC_TYPE = 4))
        AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
        AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
    ),
    all_bills AS (
      SELECT * FROM sales_invoices
      UNION ALL
      SELECT * FROM return_invoices
    )
    SELECT doc_type_name AS "نوع المستند",
           bill_no AS "رقم الفاتورة",
           TO_CHAR(bill_date,'YYYY-MM-DD') AS "التاريخ",
           NVL(c_code, 'مباشر') AS "كود العميل",
           NVL(c_name, 'عميل نقدي') AS "اسم العميل",
           NVL(rep_name, rep_code) AS "المندوب",
           TO_CHAR(gross_amt,'FM999,999,990.00') AS "المبلغ قبل الخصم",
           TO_CHAR(disc_amt,'FM999,990.00') AS "الخصم",
           TO_CHAR(vat_amt,'FM999,999,990.00') AS "الضريبة",
           TO_CHAR(net_amt,'FM999,999,990.00') AS "الصافي شامل الضريبة",
           CASE bill_post WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
    FROM all_bills
    ORDER BY bill_date DESC, bill_no DESC"""},
    {"id":"by_item","title":"حسب الصنف","params":[DFROM,DTO,ITM,REP],"sql":"""
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
    ORDER BY SUM(t.gross_amt - t.item_disc - t.extra_header_disc) DESC"""},
    {"id":"by_customer","title":"حسب العميل","params":[DFROM,DTO,CST,REP],"sql":"""
    WITH sales_mst AS (
        SELECT TO_CHAR(b.C_CODE) as c_code,
               TO_CHAR(b.REP_CODE) as rep_code,
               1 as is_sale,
               0 as is_ret,
               NVL(b.BILL_AMT,0) as gross_amt,
               NVL(b.DISC_AMT,0) as disc_amt,
               0 as ext_disc,
               NVL(b.VAT_AMT,0) as vat_amt,
               NVL(b.OTHR_AMT,0) as othr_amt
        FROM IAS20261.IAS_BILL_MST b
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND b.C_CODE IS NOT NULL
          AND (:c_code IS NULL OR TO_CHAR(b.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code)
    ),
    returns_mst AS (
        SELECT TO_CHAR(r.C_CODE) as c_code,
               TO_CHAR(r.REP_CODE) as rep_code,
               0 as is_sale,
               1 as is_ret,
               NVL(r.BILL_AMT,0) as gross_amt,
               NVL(r.DISC_AMT_MST,0) as disc_amt,
               0 as ext_disc,
               NVL(r.VAT_AMT,0) as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_RT_BILL_MST r
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = r.C_CODE
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND r.C_CODE IS NOT NULL
          AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
    ),
    ext_disc_notes AS (
        SELECT TO_CHAR(p.C_CODE) as c_code,
               TO_CHAR(p.REP_CODE) as rep_code,
               0 as is_sale,
               0 as is_ret,
               0 as gross_amt,
               0 as disc_amt,
               NVL(p.CR_AMT,0) as ext_disc,
               0 as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
        WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.C_CODE IS NOT NULL
          AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
          AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code)
    ),
    all_cust_trans AS (
        SELECT * FROM sales_mst
        UNION ALL
        SELECT * FROM returns_mst
        UNION ALL
        SELECT * FROM ext_disc_notes
    )
    SELECT t.c_code AS "كود العميل",
           MAX(c.C_A_NAME) AS "اسم العميل",
           MAX(sm.REPRS_A_NAME) AS "المندوب",
           SUM(t.is_sale) AS "فواتير مبيعات",
           SUM(t.is_ret) AS "فواتير مرتجعات",
           TO_CHAR(SUM(t.gross_amt * t.is_sale),'FM999,999,999,990.00') AS "المبيعات",
           TO_CHAR(SUM(t.gross_amt * t.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
           TO_CHAR(SUM(t.disc_amt * t.is_sale - t.disc_amt * t.is_ret),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
           TO_CHAR(SUM(t.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt + t.vat_amt + t.othr_amt) * t.is_sale - (t.gross_amt - t.disc_amt + t.vat_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
    FROM all_cust_trans t
    LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(t.c_code)
    LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
    GROUP BY t.c_code
    ORDER BY SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc) DESC"""},
    {"id":"by_salesman","title":"حسب المندوب","params":[DFROM,DTO,REP],"sql":"""
    WITH sales_mst AS (
        SELECT TO_CHAR(b.REP_CODE) as rep_code,
               TO_CHAR(b.C_CODE) as c_code,
               1 as is_sale,
               0 as is_ret,
               NVL(b.BILL_AMT,0) as gross_amt,
               NVL(b.DISC_AMT,0) as disc_amt,
               0 as ext_disc,
               NVL(b.VAT_AMT,0) as vat_amt,
               NVL(b.OTHR_AMT,0) as othr_amt
        FROM IAS20261.IAS_BILL_MST b
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(b.REP_CODE)
        WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND b.BILL_DOC_TYPE IN (1,4,8)
          AND b.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(b.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    returns_mst AS (
        SELECT TO_CHAR(r.REP_CODE) as rep_code,
               TO_CHAR(r.C_CODE) as c_code,
               0 as is_sale,
               1 as is_ret,
               NVL(r.BILL_AMT,0) as gross_amt,
               NVL(r.DISC_AMT_MST,0) as disc_amt,
               0 as ext_disc,
               NVL(r.VAT_AMT,0) as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_RT_BILL_MST r
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
        WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND r.RT_BILL_DOC_TYPE IN (1,4,8)
          AND r.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    ext_disc_notes AS (
        SELECT TO_CHAR(p.REP_CODE) as rep_code,
               TO_CHAR(p.C_CODE) as c_code,
               0 as is_sale,
               0 as is_ret,
               0 as gross_amt,
               0 as disc_amt,
               NVL(p.CR_AMT,0) as ext_disc,
               0 as vat_amt,
               0 as othr_amt
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.REP_CODE)
        WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.REP_CODE IS NOT NULL
          AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
    ),
    all_rep_trans AS (
        SELECT * FROM sales_mst
        UNION ALL
        SELECT * FROM returns_mst
        UNION ALL
        SELECT * FROM ext_disc_notes
    )
    SELECT t.rep_code AS "كود المندوب",
           MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
           COUNT(DISTINCT t.c_code) AS "عدد العملاء",
           SUM(t.is_sale) AS "فواتير مبيعات",
           SUM(t.is_ret) AS "فواتير مرتجعات",
           TO_CHAR(SUM(t.gross_amt * t.is_sale),'FM999,999,999,990.00') AS "المبيعات",
           TO_CHAR(SUM(t.gross_amt * t.is_ret),'FM999,999,999,990.00') AS "المردودات (-)",
           TO_CHAR(SUM(t.disc_amt * t.is_sale - t.disc_amt * t.is_ret),'FM999,999,999,990.00') AS "خصم الفواتير والأصناف (-)",
           TO_CHAR(SUM(t.ext_disc),'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الصافي قبل الضريبة",
           TO_CHAR(SUM((t.gross_amt - t.disc_amt + t.vat_amt + t.othr_amt) * t.is_sale - (t.gross_amt - t.disc_amt + t.vat_amt) * t.is_ret - t.ext_disc),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
    FROM all_rep_trans t
    LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
    GROUP BY t.rep_code
    ORDER BY SUM((t.gross_amt - t.disc_amt) * t.is_sale - (t.gross_amt - t.disc_amt) * t.is_ret - t.ext_disc) DESC"""},
    {"id":"net_sales_cc","title":"صافي المبيعات مع الخصومات (مراكز التكلفة)","params":[DFROM,DTO,{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},{"name":"inc_ext","label":"إشعار خصم مستقل (خصم)","type":"select","default":"0","options":[["1","خصم"],["0","تجاهل"]]}],"sql":"""
       WITH sales_data AS (
           SELECT CC_CODE,
                  SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
           FROM IAS20261.IAS_BILL_MST
           WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
             AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
             AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
           GROUP BY CC_CODE
       ),
       returns_data AS (
           SELECT CC_CODE,
                  SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
           FROM IAS20261.IAS_RT_BILL_MST
           WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
             AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
             AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
           GROUP BY CC_CODE
       ),
       discount_notice AS (
           SELECT CC_CODE, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
           FROM IAS20261.IAS_POST_DTL
           WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
             AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
             AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
           GROUP BY CC_CODE
       )
       SELECT NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) AS "رقم مركز التكلفة",
              MAX(cc.CC_A_NAME) AS "اسم مركز التكلفة",
              TO_CHAR(SUM(NVL(s.sales, 0)),'FM999,999,999,990.00') AS "إجمالي المبيعات",
              TO_CHAR(SUM(NVL(r.returns, 0)),'FM999,999,999,990.00') AS "مردود المبيعات (-)",
              TO_CHAR(CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END,'FM999,999,999,990.00') AS "إشعار خصم مستقل (-)",
              TO_CHAR(
                SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - (CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END),
                'FM999,999,999,990.00'
              ) AS "صافي المبيعات"
       FROM sales_data s
       FULL OUTER JOIN returns_data r ON s.CC_CODE = r.CC_CODE
       FULL OUTER JOIN discount_notice d ON NVL(s.CC_CODE, r.CC_CODE) = d.CC_CODE
       LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE = NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
       WHERE (:cc_code IS NULL OR NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) = :cc_code)
       GROUP BY NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
       HAVING (SUM(NVL(s.sales, 0)) <> 0 OR SUM(NVL(r.returns, 0)) <> 0 OR SUM(NVL(d.ext_disc, 0)) <> 0)
       ORDER BY SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - (CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END) DESC
    """},
    {"id":"sales_collection_summary","title":"صافي المبيعات وإجمالي التحصيل حسب الفترة","fn":"run_sales_collection_summary","params":[
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
      {"name":"rep_code","label":"المندوب (مجموعة العملاء)","type":"select","default":"","options":[["", "الكل (جميع المناديب)"], ["101", "101 - مندوب عاصمة المجد"], ["102", "102 - مندوب الغنامية"], ["103", "103 - مندوب الدار البيضاء"], ["104", "104 - مندوب جدة"], ["105", "105 - مندوب خميس مشيط"], ["106", "106 - مندوب المهرجان"], ["107", "107 - مندوب 1"], ["108", "108 - مندوب 2"], ["109", "109 - مندوب 3"], ["110", "110 - مندوب 4"], ["111", "111 - مندوب 5"], ["112", "112 - مندوب 6"], ["113", "113 - مندوب الشيكات"], ["114", "114 - مندوب الصيانة"], ["115", "115 - مندوب نواس"], ["116", "116 - مندوب المهرجان"], ["117", "117 - مندوب عبدالله يسلم"], ["118", "118 - مندوب ياسر شرمان"], ["119", "119 - مندوب جاسر"], ["120", "120 - مندوب عمر الفقية"], ["121", "121 - مندوب الطيب"], ["122", "122 - مندوب عبده"], ["123", "123 - درمه سالم / جاسر"], ["124", "124 - مندوب عبدالسلام"], ["125", "125 - مندوب جابر"], ["126", "126 - مندوب عامر"], ["127", "127 - مندوب بيجو"], ["128", "128 - المندوب علي المصري نون"], ["129", "129 - دماج"], ["131", "131 - المنصة الالكترونية"], ["141", "141 - مندوب عبدالله النهدي"], ["142", "142 - مندوب احمد الحلو"], ["143", "143 - مندوب طه المصري"], ["144", "144 - مندوب محمد سالم"], ["145", "145 - مندوب اقبال الهندي"], ["146", "146 - مندوب ابو صالح"], ["147", "147 - مندوب عبدالله يسلم"], ["148", "148 - مندوب ياسر شرمان"], ["149", "149 - مندوب جاسر الهندي"], ["150", "150 - مندوب عمر الفقيه"], ["151", "151 - مندوب احمد اخو الطيب"], ["152", "152 - مندوب عبده الهندي"], ["153", "153 - مندوب ديفيد الهندي"], ["154", "154 - مندوب عبدالسلام"], ["155", "155 - مندوب جابر الهندي"], ["156", "156 - الادارة"], ["157", "157 - مندوب بيجو الهندي"], ["158", "158 - مندوب منصة اعتماد صالح سعيد"], ["159", "159 - مندوب صالح سويد"], ["160", "160 - مندوب زيد احتياط"], ["161", "161 - مندوب راضي"], ["162", "162 - مندوب عبدالسلام"], ["163", "163 - مندوب سالم النهدي"], ["164", "164 - مندوب زيد احتياك"], ["165", "165 - مخزن الطيب الدمام"], ["166", "166 - مندوب احتياطي ابو خالد"], ["167", "167 - مندوب شوقي كشافات"], ["168", "168 - مندوب موقع سرين"], ["169", "169 - مندوب نون"], ["170", "170 - مندوب امازون"], ["171", "171 - مندوب رامي شرمان"], ["172", "172 - مندوب مواقع اكترونية خارجية"], ["173", "173 - مندوب عبدالجبار"], ["174", "174 - مندوب سلرررر"], ["175", "175 - هيثم عبدالباقي"]]}
    ],"sql":""},
    {"id":"workflow_summary","title":"ملخص سير العمل","fn":"run_workflow_summary","params":[
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
    {"id":"debt_movement_summary","title":"تقرير حركة المديونية والتحصيل الدوري","fn":"run_debt_movement_summary","params":[
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
      {"name":"rep_code","label":"المندوب (مجموعة العملاء)","type":"select","default":"","options":[["", "الكل (جميع المناديب)"], ["101", "101 - مندوب عاصمة المجد"], ["102", "102 - مندوب الغنامية"], ["103", "103 - مندوب الدار البيضاء"], ["104", "104 - مندوب جدة"], ["105", "105 - مندوب خميس مشيط"], ["106", "106 - مندوب المهرجان"], ["107", "107 - مندوب 1"], ["108", "108 - مندوب 2"], ["109", "109 - مندوب 3"], ["110", "110 - مندوب 4"], ["111", "111 - مندوب 5"], ["112", "112 - مندوب 6"], ["113", "113 - مندوب الشيكات"], ["114", "114 - مندوب الصيانة"], ["115", "115 - مندوب نواس"], ["116", "116 - مندوب المهرجان"], ["117", "117 - مندوب عبدالله يسلم"], ["118", "118 - مندوب ياسر شرمان"], ["119", "119 - مندوب جاسر"], ["120", "120 - مندوب عمر الفقية"], ["121", "121 - مندوب الطيب"], ["122", "122 - مندوب عبده"], ["123", "123 - درمه سالم / جاسر"], ["124", "124 - مندوب عبدالسلام"], ["125", "125 - مندوب جابر"], ["126", "126 - مندوب عامر"], ["127", "127 - مندوب بيجو"], ["128", "128 - المندوب علي المصري نون"], ["129", "129 - دماج"], ["131", "131 - المنصة الالكترونية"], ["141", "141 - مندوب عبدالله النهدي"], ["142", "142 - مندوب احمد الحلو"], ["143", "143 - مندوب طه المصري"], ["144", "144 - مندوب محمد سالم"], ["145", "145 - مندوب اقبال الهندي"], ["146", "146 - مندوب ابو صالح"], ["147", "147 - مندوب عبدالله يسلم"], ["148", "148 - مندوب ياسر شرمان"], ["149", "149 - مندوب جاسر الهندي"], ["150", "150 - مندوب عمر الفقيه"], ["151", "151 - مندوب احمد اخو الطيب"], ["152", "152 - مندوب عبده الهندي"], ["153", "153 - مندوب ديفيد الهندي"], ["154", "154 - مندوب عبدالسلام"], ["155", "155 - مندوب جابر الهندي"], ["156", "156 - الادارة"], ["157", "157 - مندوب بيجو الهندي"], ["158", "158 - مندوب منصة اعتماد صالح سعيد"], ["159", "159 - مندوب صالح سويد"], ["160", "160 - مندوب زيد احتياط"], ["161", "161 - مندوب راضي"], ["162", "162 - مندوب عبدالسلام"], ["163", "163 - مندوب سالم النهدي"], ["164", "164 - مندوب زيد احتياك"], ["165", "165 - مخزن الطيب الدمام"], ["166", "166 - مندوب احتياطي ابو خالد"], ["167", "167 - مندوب شوقي كشافات"], ["168", "168 - مندوب موقع سرين"], ["169", "169 - مندوب نون"], ["170", "170 - مندوب امازون"], ["171", "171 - مندوب رامي شرمان"], ["172", "172 - مندوب مواقع اكترونية خارجية"], ["173", "173 - مندوب عبدالجبار"], ["174", "174 - مندوب سلرررر"], ["175", "175 - هيثم عبدالباقي"]]}
    ],"sql":""}
  ]},

 {"id":"ar","title":"العملاء والمدينون","icon":"M9 8a3 3 0 100-6 3 3 0 000 6zM3 20c0-3 3-5 6-5s6 2 6 5","reports":[
   {"id":"balances","title":"أرصدة العملاء","params":[DTO,CST,REP],"sql":"""
      SELECT p.C_CODE AS "كود العميل",
             MAX(c.C_A_NAME) AS "اسم العميل",
             MAX(c.REP_CODE) AS "المندوب",
             TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد (مدين)"
      FROM IAS20261.IAS_POST_DTL p
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=p.C_CODE
      WHERE p.C_CODE IS NOT NULL
        AND NVL(p.DOC_POST,0)=1
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) LIKE '%' || :c_code || '%' OR c.C_A_NAME LIKE '%' || :c_code || '%')
        AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)
      GROUP BY p.C_CODE
      HAVING SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) <> 0
      ORDER BY SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)) DESC"""},
    {"id":"statement","title":"كشف حساب عميل","params":[{"name":"c_code","label":"كود العميل","type":"text","default":"1381"},DFROM,DTO],"sql":"""
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE C_CODE = :c_code AND NVL(DOC_POST,0)=1
           AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
       ),
       trans AS (
         SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC,
                NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=1 AND d.LANG_NO=1
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
       ) ORDER BY s1, s2, s3"""},
    {"id":"statement_analytic","title":"كشف حساب تحليلي","params":[{"name":"ac_code_dtl","label":"الحساب التحليلي","type":"text","default":"1381"},DFROM,DTO],"sql":"""
       WITH open_bal AS (
         SELECT NVL(SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)),0) as bal
         FROM IAS20261.IAS_POST_DTL
         WHERE (AC_CODE_DTL = :ac_code_dtl OR C_V_CODE = :ac_code_dtl OR V_C_CODE = :ac_code_dtl) AND NVL(DOC_POST,0)=1
           AND (DOC_DATE < TO_DATE(:date_from,'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
       ),
       trans AS (
         SELECT p.DOC_DATE, NVL(d.JV_NAME, 'قيد يومية') AS jv_name, p.DOC_NO, p.DOC_DESC, p.REF_NO,
                NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr, p.DOC_SER
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=1 AND d.LANG_NO=1
         WHERE (p.AC_CODE_DTL = :ac_code_dtl OR p.C_V_CODE = :ac_code_dtl OR p.V_C_CODE = :ac_code_dtl) AND NVL(p.DOC_POST,0)=1
           AND NVL(p.DOC_TYPE,0) <> 0
           AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       )
       SELECT "التاريخ","نوع المستند","رقم المستند","البيان","رقم المرجع","مدين","دائن","الرصيد" FROM (
         SELECT NULL AS "التاريخ",
                NULL AS "نوع المستند",
                NULL AS "رقم المستند",
                'الرصيد الإفتتاحي' AS "البيان",
                NULL AS "رقم المرجع",
                TO_CHAR(CASE WHEN bal>0 THEN bal ELSE 0 END,'FM999,999,990.00') AS "مدين",
                TO_CHAR(CASE WHEN bal<0 THEN -bal ELSE 0 END,'FM999,999,990.00') AS "دائن",
                NULL AS "الرصيد",
                TO_DATE('1900-01-01','YYYY-MM-DD') s1, 0 s2, 0 s3
         FROM open_bal
         UNION ALL
         SELECT TO_CHAR(t.DOC_DATE,'YYYY-MM-DD'),
                t.jv_name,
                TO_CHAR(t.DOC_NO),
                t.DOC_DESC,
                t.REF_NO,
                TO_CHAR(t.dr,'FM999,999,990.00'),
                TO_CHAR(t.cr,'FM999,999,990.00'),
                TO_CHAR((SELECT NVL(bal,0) FROM open_bal) + SUM(t.dr-t.cr) OVER (ORDER BY t.DOC_DATE, t.DOC_NO, t.DOC_SER), 'FM999,999,990.00'),
                t.DOC_DATE s1, t.DOC_NO s2, t.DOC_SER s3
         FROM trans t
       ) ORDER BY s1, s2, s3"""},
    {"id":"aging","title":"أعمار الديون","fn":"run_cust_aging","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},
     DTO,
     AGETR,
     {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""},
     {"name":"c_code","label":"كود العميل (اختياري)","type":"text","default":""}
   ]},
   {"id":"dormant","title":"العملاء الخاملون","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"أيام الخمول","type":"number","default":"90"}],"sql":"""
     SELECT * FROM (
       SELECT c.C_CODE AS "كود العميل", c.C_A_NAME AS "اسم العميل", c.REP_CODE AS "المندوب",
              TO_CHAR(lb.last_bill,'YYYY-MM-DD') AS "آخر فاتورة",
              (TRUNC(TO_DATE(:as_of,'YYYY-MM-DD'))-TRUNC(lb.last_bill)) AS "أيام منذ آخر تعامل"
       FROM IAS20261.CUSTOMER c
       LEFT JOIN (SELECT C_CODE, MAX(BILL_DATE) last_bill FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) GROUP BY C_CODE) lb ON lb.C_CODE=c.C_CODE
       WHERE NVL(c.INACTIVE,0)=0 AND (lb.last_bill IS NULL OR lb.last_bill < TO_DATE(:as_of,'YYYY-MM-DD') - :days)
       ORDER BY lb.last_bill NULLS FIRST
     ) """}
]},
 {"id":"dts","title":"التوزيع والمناديب","icon":"M3 13l3-7h7l3 4h4v5M3 13h17M6 18a2 2 0 100-4 2 2 0 000 4zm11 0a2 2 0 100-4 2 2 0 000 4z","reports":[
        {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT],"sql":"""

      WITH 
      grp AS (
        SELECT 'rep' as typ, TO_CHAR(REPRS_CODE) as cd, MAX(REPRS_A_NAME) as nm FROM IAS20261.SALES_MAN GROUP BY TO_CHAR(REPRS_CODE)
        UNION ALL 
        SELECT 'cc' as typ, TO_CHAR(CC_CODE) as cd, MAX(CC_A_NAME) as nm FROM IAS20261.COST_CENTERS GROUP BY TO_CHAR(CC_CODE)
        UNION ALL
        SELECT 'cst' as typ, TO_CHAR(C_CODE) as cd, MAX(C_A_NAME) as nm FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)
        UNION ALL
        SELECT 'cst' as typ, 'UNKNOWN' as cd, 'عميل نقدي عام' as nm FROM DUAL
      ),
      all_trans AS (
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END as grp_code,
               CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
               0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
        FROM IAS20261.IAS_BILL_MST b
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      ),
      base AS (
        SELECT grp_code,
               SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown, SUM(unposted_rcpt) unposted_rcpt, SUM(unposted_unknown) unposted_unknown,
               (CASE WHEN :inc_rcpt='1' THEN (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown)) ELSE 0 END
              + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
              + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
              - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
              ) total_inc
        FROM all_trans
        WHERE grp_code IS NOT NULL
          AND (:rep_code IS NULL OR (:grp_by = 'rep' AND grp_code = :rep_code))
        GROUP BY grp_code
      )
      SELECT * FROM (
        SELECT b.grp_code AS "الكود", NVL(MAX(g.nm), b.grp_code) AS "الجهة / الاسم",
               TO_CHAR(MAX(b.rcpt),'FM999,999,990.00')      AS "سندات القبض",
               TO_CHAR(MAX(b.unposted_rcpt),'FM999,999,990.00') AS "سندات غير مرحلة",
               TO_CHAR(MAX(b.unposted_unknown),'FM999,999,990.00') AS "غير مرحلة (بدون عميل)",
               TO_CHAR(MAX(b.rcpt_unknown),'FM999,999,990.00') AS "إيداعات وتسويات (بدون عميل)",
               TO_CHAR(MAX(b.net_jrn),'FM999,999,990.00')   AS "قيود الشبكة المنفصلة",
               TO_CHAR(MAX(b.cash_sales),'FM999,999,990.00') AS "المبيعات النقدية",
               TO_CHAR(MAX(b.inv_disc),'FM999,999,990.00')   AS "الخصم في الفاتورة",
               TO_CHAR(MAX(b.ext_notice),'FM999,999,990.00') AS "إشعار خصم مستقل (-)",
               TO_CHAR(MAX(b.cash_ret),'FM999,999,990.00')   AS "المرتجع النقدي (-)",
               TO_CHAR(MAX(b.total_inc),'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM base b
        LEFT JOIN grp g ON g.cd = b.grp_code AND g.typ = :grp_by
        WHERE (b.rcpt > 0 OR b.net_jrn > 0 OR b.cash_sales > 0 OR b.cash_ret > 0 OR b.inv_disc > 0 OR b.ext_notice > 0 OR b.rcpt_unknown > 0 OR b.unposted_rcpt > 0 OR b.unposted_unknown > 0)
        GROUP BY b.grp_code
        ORDER BY MAX(b.total_inc) DESC
      ) 
"""},
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO
       SELECT 'Dynamic' as "Placeholder" FROM DUAL
       """},
        {"id":"perf_aging_exact","title":"أعمار التحصيل (مطابق أونكس 100%)","params":[DFROM,DTO,REP],"sql":"""
      WITH cr AS (
        SELECT C_CODE,
          SUM(CASE WHEN PER_NO BETWEEN 0 AND 30   THEN DR_AMT ELSE 0 END) pos,
          SUM(CASE WHEN PER_NO BETWEEN -30 AND -1 THEN DR_AMT ELSE 0 END) neg,
          SUM(CASE WHEN PER_NO BETWEEN 31 AND 60  THEN DR_AMT ELSE 0 END) b2,
          SUM(CASE WHEN PER_NO BETWEEN 61 AND 90  THEN DR_AMT ELSE 0 END) b3,
          SUM(CASE WHEN PER_NO BETWEEN 91 AND 120 THEN DR_AMT ELSE 0 END) b4,
          SUM(CASE WHEN PER_NO > 120              THEN DR_AMT ELSE 0 END) b5,
          SUM(DR_AMT) crlim
        FROM IAS20261.IAS_CRLIMIT_TMP
        WHERE DOC_TYPE<>1 AND DOC_TYPE_REF IN (1,2)
          AND PAID_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND PAID_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY C_CODE),
      co AS (
        SELECT C_CODE, SUM(CR_AMT) col FROM IAS20261.IAS_COL_TMP
        WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY C_CODE),
      perc AS (
        SELECT cr.C_CODE,
          CASE WHEN cr.pos > 0 THEN cr.pos + cr.neg + GREATEST(0, NVL(co.col,0) - cr.crlim) ELSE 0 END b1,
          cr.b2, cr.b3, cr.b4, cr.b5
        FROM cr LEFT JOIN co ON co.C_CODE = cr.C_CODE)
      SELECT * FROM (
        SELECT c.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
               COUNT(DISTINCT perc.C_CODE) AS "عدد العملاء",
               TO_CHAR(SUM(perc.b1),'FM999,999,990.00') AS "0-30",
               TO_CHAR(SUM(perc.b2),'FM999,999,990.00') AS "31-60",
               TO_CHAR(SUM(perc.b3),'FM999,999,990.00') AS "61-90",
               TO_CHAR(SUM(perc.b4),'FM999,999,990.00') AS "91-120",
               TO_CHAR(SUM(perc.b5),'FM999,999,990.00') AS "أكثر من 120",
               TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
        FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
        LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
        WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
        GROUP BY c.REP_CODE ORDER BY SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5) DESC
      ) 
"""}
  ]},
  {"id":"pur","title":"المشتريات والموردون","icon":"M6 6h15l-1.5 9h-12zM6 6L5 3H2M9 20a1 1 0 100-2 1 1 0 000 2zm9 0a1 1 0 100-2 1 1 0 000 2z","reports":[
   {"id":"pi_bills","title":"فواتير المشتريات","params":[DFROM,DTO,{"name":"v_code","label":"المورد (اختياري)","type":"text","default":""}],"sql":"""
     SELECT BILL_NO AS "رقم الفاتورة", TO_CHAR(BILL_DATE,'YYYY-MM-DD') AS "التاريخ",
            V_CODE AS "كود المورد", V_NAME AS "اسم المورد",
            TO_CHAR(NVL(BILL_AMT,0),'FM999,999,990.00') AS "المبلغ",
            TO_CHAR(NVL(DISC_AMT,0),'FM999,999,990.00') AS "الخصم",
            TO_CHAR(NVL(VAT_AMT,0),'FM999,999,990.00') AS "الضريبة",
            TO_CHAR(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0),'FM999,999,990.00') AS "الصافي",
            CASE NVL(BILL_POST,0) WHEN 1 THEN 'مرحّلة' ELSE 'غير مرحّلة' END AS "الحالة"
     FROM IAS20261.IAS_PI_BILL_MST
     WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND (:v_code IS NULL OR V_CODE = :v_code)
     ORDER BY BILL_DATE DESC, BILL_NO DESC"""},
   {"id":"pi_by_vendor","title":"حسب المورد","params":[DFROM,DTO],"sql":"""
     SELECT V_CODE AS "كود المورد", MAX(V_NAME) AS "اسم المورد", COUNT(*) AS "عدد الفواتير",
            TO_CHAR(SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)),'FM999,999,999,990.00') AS "صافي قبل الضريبة",
            TO_CHAR(SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),'FM999,999,999,990.00') AS "الإجمالي بالضريبة"
     FROM IAS20261.IAS_PI_BILL_MST
     WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY V_CODE ORDER BY SUM(NVL(BILL_AMT,0)-NVL(DISC_AMT,0)) DESC"""},
   {"id":"pi_by_item","title":"حسب الصنف","params":[DFROM,DTO,{"name":"i_code","label":"الصنف (اختياري)","type":"text","default":""}],"sql":"""
     SELECT dt.I_CODE AS "كود الصنف", MAX(m.I_NAME) AS "اسم الصنف",
            ROUND(SUM(NVL(dt.I_QTY,0)),2) AS "إجمالي الكمية",
            TO_CHAR(ROUND(SUM(NVL(dt.I_QTY,0)*NVL(dt.I_PRICE,0)),2),'FM999,999,999,990.00') AS "قيمة المشتريات",
            COUNT(DISTINCT b.BILL_NO) AS "عدد الفواتير"
     FROM IAS20261.IAS_PI_BILL_DTL dt
     JOIN IAS20261.IAS_PI_BILL_MST b ON b.BILL_DOC_TYPE=dt.BILL_DOC_TYPE AND b.BILL_NO=dt.BILL_NO AND b.BILL_SER=dt.BILL_SER
     LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE=dt.I_CODE
     WHERE b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       AND (:i_code IS NULL OR dt.I_CODE = :i_code)
     GROUP BY dt.I_CODE ORDER BY SUM(NVL(dt.I_QTY,0)*NVL(dt.I_PRICE,0)) DESC"""},
   {"id":"vendor_statement","title":"كشف حساب مورد","params":[{"name":"v_code","label":"كود المورد","type":"text","default":"222"},DFROM,DTO],"sql":"""
     SELECT "التاريخ","نوع المستند","رقم المستند","البيان","مدين","دائن","الرصيد" FROM (
       SELECT TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') AS "التاريخ", d.JV_NAME AS "نوع المستند",
              p.DOC_NO AS "رقم المستند", p.DOC_DESC AS "البيان",
              TO_CHAR(NVL(p.DR_AMT,0),'FM999,999,990.00') AS "مدين",
              TO_CHAR(NVL(p.CR_AMT,0),'FM999,999,990.00') AS "دائن",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) OVER (ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER),'FM999,999,990.00') AS "الرصيد",
              p.DOC_DATE s1, p.DOC_NO s2, p.DOC_SER s3
       FROM IAS20261.IAS_POST_DTL p
       LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=1 AND d.LANG_NO=1
       WHERE p.V_CODE = :v_code AND NVL(p.DOC_POST,0)=1
         AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       ORDER BY p.DOC_DATE, p.DOC_NO, p.DOC_SER
     )"""},
   {"id":"vendor_aging","title":"أعمار الدائنين","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"}],"sql":"""
     WITH pay AS (SELECT V_CODE, SUM(NVL(DR_AMT,0)) paid FROM IAS20261.IAS_POST_DTL
                  WHERE NVL(DOC_POST,0)=1 AND V_CODE IS NOT NULL GROUP BY V_CODE),
     charges AS (SELECT p.V_CODE, p.DOC_DATE, NVL(p.CR_AMT,0) amt,
                   SUM(NVL(p.CR_AMT,0)) OVER (PARTITION BY p.V_CODE ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) cum
                 FROM IAS20261.IAS_POST_DTL p WHERE NVL(p.DOC_POST,0)=1 AND p.V_CODE IS NOT NULL AND NVL(p.CR_AMT,0)>0),
     openit AS (SELECT ch.V_CODE, GREATEST(0,LEAST(ch.amt,ch.cum-NVL(pay.paid,0))) unpaid,
                   TRUNC(TO_DATE(:as_of,'YYYY-MM-DD'))-TRUNC(ch.DOC_DATE) age
                FROM charges ch JOIN pay ON pay.V_CODE=ch.V_CODE)
     SELECT o.V_CODE AS "كود المورد", MAX(v.V_NAME) AS "اسم المورد",
            TO_CHAR(SUM(CASE WHEN o.age<=30 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "0-30",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 31 AND 60 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "31-60",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 61 AND 90 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "61-90",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 91 AND 120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "91-120",
            TO_CHAR(SUM(CASE WHEN o.age>120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "أكثر من 120",
            TO_CHAR(SUM(o.unpaid),'FM999,999,990.00') AS "الإجمالي"
     FROM openit o LEFT JOIN (SELECT V_CODE, MAX(V_NAME) V_NAME FROM IAS20261.IAS_PI_BILL_MST GROUP BY V_CODE) v ON v.V_CODE=o.V_CODE
     WHERE o.unpaid>0 GROUP BY o.V_CODE ORDER BY SUM(o.unpaid) DESC"""},
 ]},
 {"id":"fin","title":"المالية والمحاسبة","icon":"M4 20V4h16v16zM8 16v-4M12 16V8M16 16v-6","reports":[
   {"id":"trial_balance","title":"ميزان المراجعة","params":[DFROM,DTO],"sql":"""
     SELECT * FROM (
       SELECT p.A_CODE AS "رقم الحساب", MAX(a.A_NAME) AS "اسم الحساب",
              TO_CHAR(SUM(NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي مدين",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "إجمالي دائن",
              TO_CHAR(SUM(NVL(p.DR_AMT,0)-NVL(p.CR_AMT,0)),'FM999,999,999,990.00') AS "الرصيد"
       FROM IAS20261.IAS_POST_DTL p LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY p.A_CODE HAVING SUM(NVL(p.DR_AMT,0))<>0 OR SUM(NVL(p.CR_AMT,0))<>0
       ORDER BY p.A_CODE
     ) """},
   {"id":"income_statement","title":"قائمة الدخل","params":[DFROM,DTO],"sql":"""
     SELECT NVL(pa.A_NAME, a.A_PARENT) AS "البند",
            TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "الصافي"
     FROM IAS20261.IAS_POST_DTL p
     JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
     LEFT JOIN IAS20261.ACCOUNT pa ON pa.A_CODE=a.A_PARENT
     WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
       AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
     GROUP BY a.A_PARENT, pa.A_NAME
     ORDER BY SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) DESC"""},
   {"id":"cost_centers","title":"مراكز التكلفة","params":[DFROM,DTO],"sql":"""
     SELECT * FROM (
       SELECT p.CC_CODE AS "مركز التكلفة", MAX(cc.CC_A_NAME) AS "الاسم",
              TO_CHAR(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),'FM999,999,999,990.00') AS "صافي الربح/الخسارة"
       FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       LEFT JOIN IAS20261.COST_CENTERS cc ON cc.CC_CODE=p.CC_CODE
       WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
         AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY p.CC_CODE HAVING SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0))<>0
       ORDER BY SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) DESC
     ) """},
   {"id":"journal","title":"قيود اليومية","params":[{"name":"date_from","label":"من تاريخ","type":"date","default":"2026-07-01"},{"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"a_code","label":"الحساب (اختياري)","type":"text","default":""}],"sql":"""
     SELECT * FROM (
       SELECT TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') AS "التاريخ", d.JV_NAME AS "نوع القيد",
              p.DOC_NO AS "رقم المستند", p.A_CODE AS "رقم الحساب", a.A_NAME AS "اسم الحساب",
              p.DOC_DESC AS "البيان",
              TO_CHAR(NVL(p.DR_AMT,0),'FM999,999,990.00') AS "مدين",
              TO_CHAR(NVL(p.CR_AMT,0),'FM999,999,990.00') AS "دائن"
       FROM IAS20261.IAS_POST_DTL p
       LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
       LEFT JOIN IAS20261.JV_TYPES d ON d.JV_TYPE=p.JV_TYPE
       WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
         AND (:a_code IS NULL OR p.A_CODE = :a_code)
       ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC, p.DOC_SER
     ) """},
        
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO
       SELECT 'Dynamic' as "Placeholder" FROM DUAL
       """},
   {"id":"perf_aging_exact","title":"أعمار التحصيل (مطابق أونكس 100%)","params":[DFROM,DTO,REP],"sql":"""
     WITH cr AS (
       SELECT C_CODE,
         SUM(CASE WHEN PER_NO BETWEEN 0 AND 30   THEN DR_AMT ELSE 0 END) pos,
         SUM(CASE WHEN PER_NO BETWEEN -30 AND -1 THEN DR_AMT ELSE 0 END) neg,
         SUM(CASE WHEN PER_NO BETWEEN 31 AND 60  THEN DR_AMT ELSE 0 END) b2,
         SUM(CASE WHEN PER_NO BETWEEN 61 AND 90  THEN DR_AMT ELSE 0 END) b3,
         SUM(CASE WHEN PER_NO BETWEEN 91 AND 120 THEN DR_AMT ELSE 0 END) b4,
         SUM(CASE WHEN PER_NO > 120              THEN DR_AMT ELSE 0 END) b5,
         SUM(DR_AMT) crlim
       FROM IAS20261.IAS_CRLIMIT_TMP
       WHERE DOC_TYPE<>1 AND DOC_TYPE_REF IN (1,2)
         AND PAID_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND PAID_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY C_CODE),
     co AS (
       SELECT C_CODE, SUM(CR_AMT) col FROM IAS20261.IAS_COL_TMP
       WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
       GROUP BY C_CODE),
     perc AS (
       SELECT cr.C_CODE,
         CASE WHEN cr.pos > 0 THEN cr.pos + cr.neg + GREATEST(0, NVL(co.col,0) - cr.crlim) ELSE 0 END b1,
         cr.b2, cr.b3, cr.b4, cr.b5
       FROM cr LEFT JOIN co ON co.C_CODE = cr.C_CODE)
     SELECT * FROM (
       SELECT c.REP_CODE AS "كود المندوب", MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
              COUNT(DISTINCT perc.C_CODE) AS "عدد العملاء",
              TO_CHAR(SUM(perc.b1),'FM999,999,990.00') AS "0-30",
              TO_CHAR(SUM(perc.b2),'FM999,999,990.00') AS "31-60",
              TO_CHAR(SUM(perc.b3),'FM999,999,990.00') AS "61-90",
              TO_CHAR(SUM(perc.b4),'FM999,999,990.00') AS "91-120",
              TO_CHAR(SUM(perc.b5),'FM999,999,990.00') AS "أكثر من 120",
              TO_CHAR(SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5),'FM999,999,990.00') AS "إجمالي التحصيل"
       FROM perc JOIN IAS20261.CUSTOMER c ON c.C_CODE=perc.C_CODE
       LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=c.REP_CODE
       WHERE (:rep_code IS NULL OR c.REP_CODE = :rep_code)
       GROUP BY c.REP_CODE ORDER BY SUM(perc.b1+perc.b2+perc.b3+perc.b4+perc.b5) DESC
     ) """},
 ]},
 {"id":"tax","title":"الضريبة","icon":"M4 4h16v4H4zM6 8v12M18 8v12M4 20h16M9 12h6M9 16h6","reports":[
   {"id":"vat_decl","title":"الإقرار الضريبي (شهري)","params":[],"sql":"""
     SELECT PRD_NM AS "الفترة",
       TO_CHAR(-(SUM(CASE WHEN DOC_TYPE IN (4,5,15) THEN DOC_AMT_VAT ELSE 0 END)),'FM999,999,999,990.00') AS "المبيعات الخاضعة",
       TO_CHAR(-(SUM(CASE WHEN DOC_TYPE IN (4,5,15) THEN VAT_AMT ELSE 0 END)),'FM999,999,999,990.00') AS "ضريبة المخرجات",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (6,7,16) THEN DOC_AMT_VAT ELSE 0 END),'FM999,999,999,990.00') AS "المشتريات الخاضعة",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (6,7,16) THEN VAT_AMT ELSE 0 END),'FM999,999,999,990.00') AS "ضريبة المدخلات",
       TO_CHAR(SUM(CASE WHEN DOC_TYPE IN (1,3) THEN VAT_AMT ELSE 0 END),'FM999,999,999,990.00') AS "تعديلات",
       TO_CHAR(-(SUM(VAT_AMT)),'FM999,999,999,990.00') AS "صافي الضريبة المستحقة"
     FROM IAS20261.GNR_TAX_SUM_VW
     GROUP BY PRD_NO, PRD_NM ORDER BY PRD_NO"""},
   {"id":"vat_out","title":"تفصيل ضريبة المخرجات","params":[],"sql":"""
     SELECT PRD_NM AS "الفترة", DOC_TYP_NAME AS "نوع المستند",
       TO_CHAR(-(SUM(DOC_AMT_VAT)),'FM999,999,999,990.00') AS "الوعاء الخاضع",
       TO_CHAR(-(SUM(VAT_AMT)),'FM999,999,999,990.00') AS "الضريبة"
     FROM IAS20261.GNR_TAX_SUM_VW WHERE DOC_TYPE IN (4,5,15)
     GROUP BY PRD_NO, PRD_NM, DOC_TYPE, DOC_TYP_NAME ORDER BY PRD_NO, DOC_TYPE"""},
   {"id":"vat_in","title":"تفصيل ضريبة المدخلات","params":[],"sql":"""
     SELECT PRD_NM AS "الفترة", DOC_TYP_NAME AS "نوع المستند",
       TO_CHAR(SUM(DOC_AMT_VAT),'FM999,999,999,990.00') AS "الوعاء الخاضع",
       TO_CHAR(SUM(VAT_AMT),'FM999,999,999,990.00') AS "الضريبة"
     FROM IAS20261.GNR_TAX_SUM_VW WHERE DOC_TYPE IN (6,7,16,1,3)
     GROUP BY PRD_NO, PRD_NM, DOC_TYPE, DOC_TYP_NAME ORDER BY PRD_NO, DOC_TYPE"""},
 ]},
   {"id":"prof","title":"الربحية","icon":"M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z","reports":[
    {"id":"prof_summary","title":"ملخّص مجمل الربح للفترة","params":[DFROM,DTO,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT NVL(d.I_QTY,0) as qty,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
      ),
      return_lines AS (
          SELECT -NVL(rd.I_QTY,0) as qty,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      ext_disc_notes AS (
          SELECT SUM(NVL(CR_AMT,0)) as ext_disc
          FROM IAS20261.IAS_POST_DTL
          WHERE DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
            AND (:rep_code IS NULL OR TO_CHAR(REP_CODE) = :rep_code)
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
      ),
      totals AS (
          SELECT SUM(gross_rev - line_disc - extra_header_disc) as net_bill_rev,
                 SUM(cost) as total_cogs
          FROM all_lines
      )
      SELECT TO_CHAR(t.net_bill_rev - NVL(e.ext_disc,0),'FM999,999,999,990.00') AS "المبيعات (بلا ضريبة)",
             TO_CHAR(t.total_cogs,'FM999,999,999,990.00') AS "تكلفة المبيعات",
             TO_CHAR((t.net_bill_rev - NVL(e.ext_disc,0)) - t.total_cogs,'FM999,999,999,990.00') AS "مجمل الربح",
             TO_CHAR(ROUND(100 * ((t.net_bill_rev - NVL(e.ext_disc,0)) - t.total_cogs) / NULLIF(t.net_bill_rev - NVL(e.ext_disc,0), 0), 1), 'FM990.0') || ' %' AS "الهامش"
      FROM totals t
      CROSS JOIN ext_disc_notes e"""},
    {"id":"net_profit","title":"صافي الربح للفترة (بعد كل المصاريف)","params":[DFROM,DTO],"sql":"""
      SELECT
        TO_CHAR(SUM(CASE WHEN nt>0 THEN nt ELSE 0 END),'FM999,999,999,990.00') AS "الإيرادات",
        TO_CHAR(SUM(CASE WHEN nt<0 THEN -nt ELSE 0 END),'FM999,999,999,990.00') AS "المصاريف",
        TO_CHAR(SUM(nt),'FM999,999,999,990.00') AS "صافي الربح"
      FROM (SELECT p.A_CODE, SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)) nt
            FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE
            WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2
              AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            GROUP BY p.A_CODE)"""},
    {"id":"prof_item","title":"ربحية الصنف","params":[DFROM,DTO,ITM,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT d.I_CODE as item_code,
                 NVL(d.I_QTY,0) as qty,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS20261.IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(d.I_CODE)
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:i_code IS NULL OR TO_CHAR(d.I_CODE) = :i_code OR im.I_NAME LIKE '%' || :i_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
      ),
      return_lines AS (
          SELECT rd.I_CODE as item_code,
                 -NVL(rd.I_QTY,0) as qty,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS20261.IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(rd.I_CODE)
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:i_code IS NULL OR TO_CHAR(rd.I_CODE) = :i_code OR im.I_NAME LIKE '%' || :i_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
      )
      SELECT * FROM (
        SELECT t.item_code AS "كود الصنف",
               MAX(im.I_NAME) AS "اسم الصنف",
               TO_CHAR(SUM(t.qty),'FM999,999,990.00') AS "الكمية المباعة",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc),'FM999,999,999,990.00') AS "المبيعات",
               TO_CHAR(SUM(t.cost),'FM999,999,999,990.00') AS "التكلفة",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost),'FM999,999,999,990.00') AS "الربح",
               TO_CHAR(ROUND(100 * (SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost)) / NULLIF(SUM(t.gross_rev - t.line_disc - t.extra_header_disc), 0), 1), 'FM990.0') || ' %' AS "هامش"
        FROM all_lines t
        LEFT JOIN IAS20261.IAS_ITM_MST im ON TO_CHAR(im.I_CODE) = TO_CHAR(t.item_code)
        GROUP BY t.item_code
        ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc) - SUM(t.cost) DESC
      ) """},
    {"id":"prof_cust","title":"ربحية العميل","params":[DFROM,DTO,CST,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT TO_CHAR(m.C_CODE) as c_code,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(m.C_CODE)
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:c_code IS NULL OR TO_CHAR(m.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code)
      ),
      return_lines AS (
          SELECT TO_CHAR(r.C_CODE) as c_code,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(r.C_CODE)
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:c_code IS NULL OR TO_CHAR(r.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code)
      ),
      ext_disc_notes AS (
          SELECT TO_CHAR(p.C_CODE) as c_code,
                 0 as gross_rev,
                 0 as line_disc,
                 0 as extra_header_disc,
                 NVL(p.CR_AMT,0) as ext_disc,
                 0 as cost
          FROM IAS20261.IAS_POST_DTL p
          LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(p.C_CODE)
          WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
            AND (:c_code IS NULL OR TO_CHAR(p.C_CODE) = :c_code OR c.C_A_NAME LIKE '%' || :c_code || '%')
            AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code)
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
          UNION ALL
          SELECT * FROM ext_disc_notes
      )
      SELECT * FROM (
        SELECT NVL(t.c_code, 'مباشر') AS "كود العميل",
               NVL(MAX(c.C_A_NAME), 'عميل نقدي') AS "اسم العميل",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc),'FM999,999,999,990.00') AS "المبيعات",
               TO_CHAR(SUM(t.cost),'FM999,999,999,990.00') AS "التكلفة",
               TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost),'FM999,999,999,990.00') AS "الربح",
               TO_CHAR(ROUND(100 * (SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost)) / NULLIF(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc), 0), 1), 'FM990.0') || ' %' AS "هامش"
        FROM all_lines t
        LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = TO_CHAR(t.c_code)
        GROUP BY t.c_code
        ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost) DESC
      ) """},
    {"id":"prof_rep","title":"ربحية المندوب","params":[DFROM,DTO,REP],"sql":"""
      WITH dtl_disc_sum AS (
          SELECT BILL_DOC_TYPE, BILL_NO, BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_BILL_DTL GROUP BY BILL_DOC_TYPE, BILL_NO, BILL_SER
      ),
      rt_dtl_disc_sum AS (
          SELECT RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER, SUM(NVL(DIS_AMT,0)) as tot_dtl_disc
          FROM IAS20261.IAS_RT_BILL_DTL GROUP BY RT_BILL_DOC_TYPE, RT_BILL_NO, RT_BILL_SER
      ),
      sales_lines AS (
          SELECT TO_CHAR(m.REP_CODE) as rep_code,
                 (NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) as gross_rev,
                 NVL(d.DIS_AMT,0) as line_disc,
                 CASE WHEN NVL(m.BILL_AMT,0) > 0 THEN
                     ((NVL(d.I_QTY,0) * NVL(d.I_PRICE,0)) / m.BILL_AMT) * GREATEST(0, NVL(m.DISC_AMT,0) - NVL(dds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 (NVL(d.I_QTY,0) * NVL(d.STK_COST,0)) as cost
          FROM IAS20261.IAS_BILL_DTL d
          JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND m.BILL_NO=d.BILL_NO AND m.BILL_SER=d.BILL_SER
          LEFT JOIN dtl_disc_sum dds ON dds.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND dds.BILL_NO=d.BILL_NO AND dds.BILL_SER=d.BILL_SER
          LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(m.REP_CODE)
          WHERE m.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND m.BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(m.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
      ),
      return_lines AS (
          SELECT TO_CHAR(r.REP_CODE) as rep_code,
                 -(NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) as gross_rev,
                 -NVL(rd.DIS_AMT,0) as line_disc,
                 -CASE WHEN NVL(r.BILL_AMT,0) > 0 THEN
                     ((NVL(rd.I_QTY,0) * NVL(rd.I_PRICE,0)) / r.BILL_AMT) * GREATEST(0, NVL(r.DISC_AMT_MST,0) - NVL(rdds.tot_dtl_disc,0))
                 ELSE 0 END as extra_header_disc,
                 0 as ext_disc,
                 -(NVL(rd.I_QTY,0) * NVL(rd.STK_COST,0)) as cost
          FROM IAS20261.IAS_RT_BILL_DTL rd
          JOIN IAS20261.IAS_RT_BILL_MST r ON r.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND r.RT_BILL_NO=rd.RT_BILL_NO AND r.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN rt_dtl_disc_sum rdds ON rdds.RT_BILL_DOC_TYPE=rd.RT_BILL_DOC_TYPE AND rdds.RT_BILL_NO=rd.RT_BILL_NO AND rdds.RT_BILL_SER=rd.RT_BILL_SER
          LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(r.REP_CODE)
          WHERE r.RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND r.RT_BILL_DOC_TYPE IN (1,4,8)
            AND (:rep_code IS NULL OR TO_CHAR(r.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
      ),
      ext_disc_notes AS (
          SELECT TO_CHAR(p.REP_CODE) as rep_code,
                 0 as gross_rev,
                 0 as line_disc,
                 0 as extra_header_disc,
                 NVL(p.CR_AMT,0) as ext_disc,
                 0 as cost
          FROM IAS20261.IAS_POST_DTL p
          LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.REP_CODE)
          WHERE p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
            AND p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
            AND (:rep_code IS NULL OR TO_CHAR(p.REP_CODE) = :rep_code OR sm.REPRS_A_NAME LIKE '%' || :rep_code || '%')
      ),
      all_lines AS (
          SELECT * FROM sales_lines
          UNION ALL
          SELECT * FROM return_lines
          UNION ALL
          SELECT * FROM ext_disc_notes
      )
      SELECT t.rep_code AS "كود المندوب",
             MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
             TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc),'FM999,999,999,990.00') AS "المبيعات",
             TO_CHAR(SUM(t.cost),'FM999,999,999,990.00') AS "التكلفة",
             TO_CHAR(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost),'FM999,999,999,990.00') AS "الربح",
             TO_CHAR(ROUND(100 * (SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost)) / NULLIF(SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc), 0), 1), 'FM990.0') || ' %' AS "هامش"
      FROM all_lines t
      LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(t.rep_code)
      WHERE t.rep_code IS NOT NULL
      GROUP BY t.rep_code ORDER BY SUM(t.gross_rev - t.line_disc - t.extra_header_disc - t.ext_disc) - SUM(t.cost) DESC"""},
    {"id":"true_income_statement","title":"قائمة الدخل (الحقيقية)","params":[DFROM,DTO,REP],"sql":"""
        WITH gl_base AS (
          SELECT 
              A_CODE as acc_code,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(DR_AMT,0) ELSE 0 END) as op_dr,
              SUM(CASE WHEN DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(CR_AMT,0) ELSE 0 END) as op_cr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(DR_AMT,0) ELSE 0 END) as mv_dr,
              SUM(CASE WHEN DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(CR_AMT,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_POST_DTL
          WHERE (:rep_code IS NULL OR REP_CODE = :rep_code OR CC_CODE = :rep_code)
            AND NVL(DOC_POST,0)=1
            AND (
                A_CODE LIKE '31102%' OR A_CODE LIKE '31104%' OR A_CODE LIKE '31105%' OR A_CODE LIKE '31109%' OR A_CODE LIKE '31110%' OR
                A_CODE LIKE '32101%' OR A_CODE LIKE '32201%' OR A_CODE LIKE '32401%' OR A_CODE LIKE '32801%' OR
                A_CODE LIKE '41101%' OR A_CODE LIKE '41202%'
            )
          GROUP BY A_CODE
        ),
        inv_cogs AS (
          SELECT 
              '311010001' as acc_code,
              SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_dr,
              0 as op_cr,
              SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_dr,
              0 as mv_cr
          FROM IAS20261.IAS_BILL_MST m
          JOIN IAS20261.IAS_BILL_DTL d ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
          WHERE (:rep_code IS NULL OR m.REP_CODE = :rep_code OR m.CC_CODE = :rep_code)
        ),
        inv_cogs_ret AS (
          SELECT 
              '311030001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_RT_BILL_MST r
          JOIN IAS20261.IAS_RT_BILL_DTL d ON r.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = d.RT_BILL_NO AND r.RT_BILL_SER = d.RT_BILL_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code OR r.CC_CODE = :rep_code)
            AND r.PREV_YEAR IS NULL
        ),
        inv_cogs_ret_prev AS (
          SELECT 
              '311060001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(d.I_QTY,0) * NVL(d.I_PRICE_LEV_NO,0) ELSE 0 END) as mv_cr
          FROM IAS20261.IAS_RT_BILL_MST r
          JOIN IAS20261.IAS_RT_BILL_DTL d ON r.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND r.RT_BILL_NO = d.RT_BILL_NO AND r.RT_BILL_SER = d.RT_BILL_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code OR r.CC_CODE = :rep_code)
            AND r.PREV_YEAR IS NOT NULL
        ),
        all_data AS (
          SELECT * FROM gl_base
          UNION ALL
          SELECT * FROM inv_cogs
          UNION ALL
          SELECT * FROM inv_cogs_ret
          UNION ALL
          SELECT * FROM inv_cogs_ret_prev
        )
        SELECT 
            d.acc_code AS "الرقم", 
            MAX(a.A_NAME) AS "الاسم",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_dr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.op_cr),0),2), 0),'FM999,999,990.00') AS "الرصيد الافتتاحي دائن",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_dr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة مدين",
            TO_CHAR(NULLIF(ROUND(NVL(SUM(d.mv_cr),0),2), 0),'FM999,999,990.00') AS "رصيد الحركة دائن",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) > 0 
                   THEN (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) - (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة مدين",
            TO_CHAR(NULLIF(ROUND(
              CASE WHEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0)) > 0 
                   THEN (NVL(SUM(d.op_cr),0) + NVL(SUM(d.mv_cr),0)) - (NVL(SUM(d.op_dr),0) + NVL(SUM(d.mv_dr),0))
                   ELSE 0 END, 2), 0), 'FM999,999,990.00'
            ) AS "الأرصدة دائن"
        FROM all_data d
        LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = d.acc_code
        GROUP BY d.acc_code
        ORDER BY d.acc_code
      """}
  ]},
 {"id":"stock","title":"المخزون","icon":"M3 7l9-4 9 4-9 4zM3 7v10l9 4 9-4V7M12 11v10","reports":[
    {"id":"detailed_stock_pivot","title":"حركة وأرصدة المخزون الشامل","params":[DFROM,DTO],"sql":"""
        WITH item_groups AS (
            SELECT 
                m.I_CODE,
                MAX(m.I_NAME) AS I_NAME,
                MAX(gd.G_A_NAME) AS main_grp,
                MAX(mg.MNG_A_NAME) AS sub_main_grp,
                MAX(sg.SUBG_A_NAME) AS sub_grp,
                MAX(dg.DETAIL_A_NAME) AS dtl_grp
            FROM IAS20261.IAS_ITM_MST m
            LEFT JOIN IAS20261.GROUP_DETAILS gd ON gd.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_MAINSUB_GRP_DTL mg ON mg.MNG_CODE = m.MNG_CODE AND mg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_SUB_GRP_DTL sg ON sg.SUBG_CODE = m.SUBG_CODE AND sg.MNG_CODE = m.MNG_CODE AND sg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_DETAIL_GROUP dg ON dg.DET_I_CODE = m.DETAIL_NO AND dg.SUBG_CODE = m.SUBG_CODE AND dg.MNG_CODE = m.MNG_CODE AND dg.G_CODE = m.G_CODE
            GROUP BY m.I_CODE
        ),
        inventory_mov AS (
            SELECT 
                dt.I_CODE,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 105 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_105,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 103 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_103,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 121 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_121,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 122 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_122,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 118 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_118,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 108 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_108,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') AND W_CODE = 119 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as op_bal_119,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as sales_rtn_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_qty,
                SUM(CASE WHEN I_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as pur_rtn_qty,
                
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 105 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_105,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 103 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_103,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 121 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_121,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 122 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_122,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 118 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_118,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 108 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_108,
                SUM(CASE WHEN I_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 AND W_CODE = 119 THEN NVL(dt.I_QTY,0) * NVL(IN_OUT,1) ELSE 0 END) as end_bal_119
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119) OR dt.DOC_TYPE IN (1, 2, 3, 4)
            GROUP BY dt.I_CODE
        )
        SELECT 
            ig.main_grp AS "المجموعة الرئيسية",
            ig.sub_main_grp AS "الفرعية",
            ig.sub_grp AS "تحت الفرعية",
            ig.dtl_grp AS "التفصيلية",
            ig.I_CODE AS "رقم الصنف",
            ig.I_NAME AS "اسم الصنف",
            
            TO_CHAR(NVL(im.op_bal_105, 0), 'FM999,999,990.00') AS "افتتاحي 105",
            TO_CHAR(NVL(im.op_bal_103, 0), 'FM999,999,990.00') AS "افتتاحي 103",
            TO_CHAR(NVL(im.op_bal_121, 0), 'FM999,999,990.00') AS "افتتاحي 121",
            TO_CHAR(NVL(im.op_bal_122, 0), 'FM999,999,990.00') AS "افتتاحي 122",
            TO_CHAR(NVL(im.op_bal_118, 0), 'FM999,999,990.00') AS "افتتاحي 118",
            TO_CHAR(NVL(im.op_bal_108, 0), 'FM999,999,990.00') AS "افتتاحي 108",
            TO_CHAR(NVL(im.op_bal_119, 0), 'FM999,999,990.00') AS "افتتاحي 119",
            
            TO_CHAR(NVL(im.sales_qty, 0), 'FM999,999,990.00') AS "المبيعات",
            TO_CHAR(NVL(im.sales_rtn_qty, 0), 'FM999,999,990.00') AS "مردود المبيعات",
            TO_CHAR(NVL(im.pur_qty, 0), 'FM999,999,990.00') AS "المشتريات",
            TO_CHAR(NVL(im.pur_rtn_qty, 0), 'FM999,999,990.00') AS "مردود المشتريات",
            
            TO_CHAR(NVL(im.end_bal_105, 0), 'FM999,999,990.00') AS "نهائي 105",
            TO_CHAR(NVL(im.end_bal_103, 0), 'FM999,999,990.00') AS "نهائي 103",
            TO_CHAR(NVL(im.end_bal_121, 0), 'FM999,999,990.00') AS "نهائي 121",
            TO_CHAR(NVL(im.end_bal_122, 0), 'FM999,999,990.00') AS "نهائي 122",
            TO_CHAR(NVL(im.end_bal_118, 0), 'FM999,999,990.00') AS "نهائي 118",
            TO_CHAR(NVL(im.end_bal_108, 0), 'FM999,999,990.00') AS "نهائي 108",
            TO_CHAR(NVL(im.end_bal_119, 0), 'FM999,999,990.00') AS "نهائي 119"
            
        FROM item_groups ig
        JOIN inventory_mov im ON ig.I_CODE = im.I_CODE
        WHERE NVL(im.op_bal_105,0) <> 0 OR NVL(im.op_bal_103,0) <> 0 OR NVL(im.op_bal_121,0) <> 0 OR NVL(im.op_bal_122,0) <> 0 OR NVL(im.op_bal_118,0) <> 0 OR NVL(im.op_bal_108,0) <> 0 OR NVL(im.op_bal_119,0) <> 0
           OR NVL(im.sales_qty,0) <> 0 OR NVL(im.pur_qty,0) <> 0 OR NVL(im.sales_rtn_qty,0) <> 0 OR NVL(im.pur_rtn_qty,0) <> 0
           OR NVL(im.end_bal_105,0) <> 0 OR NVL(im.end_bal_103,0) <> 0 OR NVL(im.end_bal_121,0) <> 0 OR NVL(im.end_bal_122,0) <> 0 OR NVL(im.end_bal_118,0) <> 0 OR NVL(im.end_bal_108,0) <> 0 OR NVL(im.end_bal_119,0) <> 0
        ORDER BY ig.main_grp, ig.I_CODE
    """},

          {"id":"monthly_movement_pivot","title":"حركة الأصناف الشهرية (مبيعات/مشتريات)","params":[PYEAR],"sql":"""
        WITH item_groups AS (
            SELECT 
                m.I_CODE,
                MAX(m.I_NAME) AS I_NAME,
                MAX(gd.G_A_NAME) AS main_grp,
                MAX(mg.MNG_A_NAME) AS sub_main_grp,
                MAX(sg.SUBG_A_NAME) AS sub_grp,
                MAX(dg.DETAIL_A_NAME) AS dtl_grp
            FROM IAS20261.IAS_ITM_MST m
            LEFT JOIN IAS20261.GROUP_DETAILS gd ON gd.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_MAINSUB_GRP_DTL mg ON mg.MNG_CODE = m.MNG_CODE AND mg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_SUB_GRP_DTL sg ON sg.SUBG_CODE = m.SUBG_CODE AND sg.MNG_CODE = m.MNG_CODE AND sg.G_CODE = m.G_CODE
            LEFT JOIN IAS20261.IAS_DETAIL_GROUP dg ON dg.DET_I_CODE = m.DETAIL_NO AND dg.SUBG_CODE = m.SUBG_CODE AND dg.MNG_CODE = m.MNG_CODE AND dg.G_CODE = m.G_CODE
            GROUP BY m.I_CODE
        ),
        inventory_mov AS (
            SELECT 
                dt.I_CODE,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '01' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m01_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '02' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m02_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '03' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m03_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '04' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m04_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '05' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m05_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '06' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m06_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '07' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m07_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '08' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m08_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '09' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m09_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '10' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m10_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '11' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m11_pur_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_sales,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 3 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_sales_rtn,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 2 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_pur,
                SUM(CASE WHEN TO_CHAR(I_DATE, 'MM') = '12' AND DOC_TYPE = 4 THEN NVL(dt.I_QTY,0) ELSE 0 END) as m12_pur_rtn
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.DOC_TYPE IN (1, 2, 3, 4) AND TO_CHAR(dt.I_DATE, 'YYYY') = :p_year
            GROUP BY dt.I_CODE
        )
        SELECT 
            ig.main_grp AS "المجموعة الرئيسية",
            ig.sub_main_grp AS "الفرعية",
            ig.sub_grp AS "تحت الفرعية",
            ig.dtl_grp AS "التفصيلية",
            ig.I_CODE AS "رقم الصنف",
            ig.I_NAME AS "اسم الصنف",
            TO_CHAR(NVL(im.m01_sales, 0), 'FM999,999,990.00') AS "مبيعات ش1",
            TO_CHAR(NVL(im.m01_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش1",
            TO_CHAR(NVL(im.m01_pur, 0), 'FM999,999,990.00') AS "مشتريات ش1",
            TO_CHAR(NVL(im.m01_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش1",
            TO_CHAR(NVL(im.m02_sales, 0), 'FM999,999,990.00') AS "مبيعات ش2",
            TO_CHAR(NVL(im.m02_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش2",
            TO_CHAR(NVL(im.m02_pur, 0), 'FM999,999,990.00') AS "مشتريات ش2",
            TO_CHAR(NVL(im.m02_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش2",
            TO_CHAR(NVL(im.m03_sales, 0), 'FM999,999,990.00') AS "مبيعات ش3",
            TO_CHAR(NVL(im.m03_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش3",
            TO_CHAR(NVL(im.m03_pur, 0), 'FM999,999,990.00') AS "مشتريات ش3",
            TO_CHAR(NVL(im.m03_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش3",
            TO_CHAR(NVL(im.m04_sales, 0), 'FM999,999,990.00') AS "مبيعات ش4",
            TO_CHAR(NVL(im.m04_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش4",
            TO_CHAR(NVL(im.m04_pur, 0), 'FM999,999,990.00') AS "مشتريات ش4",
            TO_CHAR(NVL(im.m04_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش4",
            TO_CHAR(NVL(im.m05_sales, 0), 'FM999,999,990.00') AS "مبيعات ش5",
            TO_CHAR(NVL(im.m05_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش5",
            TO_CHAR(NVL(im.m05_pur, 0), 'FM999,999,990.00') AS "مشتريات ش5",
            TO_CHAR(NVL(im.m05_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش5",
            TO_CHAR(NVL(im.m06_sales, 0), 'FM999,999,990.00') AS "مبيعات ش6",
            TO_CHAR(NVL(im.m06_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش6",
            TO_CHAR(NVL(im.m06_pur, 0), 'FM999,999,990.00') AS "مشتريات ش6",
            TO_CHAR(NVL(im.m06_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش6",
            TO_CHAR(NVL(im.m07_sales, 0), 'FM999,999,990.00') AS "مبيعات ش7",
            TO_CHAR(NVL(im.m07_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش7",
            TO_CHAR(NVL(im.m07_pur, 0), 'FM999,999,990.00') AS "مشتريات ش7",
            TO_CHAR(NVL(im.m07_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش7",
            TO_CHAR(NVL(im.m08_sales, 0), 'FM999,999,990.00') AS "مبيعات ش8",
            TO_CHAR(NVL(im.m08_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش8",
            TO_CHAR(NVL(im.m08_pur, 0), 'FM999,999,990.00') AS "مشتريات ش8",
            TO_CHAR(NVL(im.m08_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش8",
            TO_CHAR(NVL(im.m09_sales, 0), 'FM999,999,990.00') AS "مبيعات ش9",
            TO_CHAR(NVL(im.m09_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش9",
            TO_CHAR(NVL(im.m09_pur, 0), 'FM999,999,990.00') AS "مشتريات ش9",
            TO_CHAR(NVL(im.m09_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش9",
            TO_CHAR(NVL(im.m10_sales, 0), 'FM999,999,990.00') AS "مبيعات ش10",
            TO_CHAR(NVL(im.m10_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش10",
            TO_CHAR(NVL(im.m10_pur, 0), 'FM999,999,990.00') AS "مشتريات ش10",
            TO_CHAR(NVL(im.m10_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش10",
            TO_CHAR(NVL(im.m11_sales, 0), 'FM999,999,990.00') AS "مبيعات ش11",
            TO_CHAR(NVL(im.m11_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش11",
            TO_CHAR(NVL(im.m11_pur, 0), 'FM999,999,990.00') AS "مشتريات ش11",
            TO_CHAR(NVL(im.m11_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش11",
            TO_CHAR(NVL(im.m12_sales, 0), 'FM999,999,990.00') AS "مبيعات ش12",
            TO_CHAR(NVL(im.m12_sales_rtn, 0), 'FM999,999,990.00') AS "مردود مبيعات ش12",
            TO_CHAR(NVL(im.m12_pur, 0), 'FM999,999,990.00') AS "مشتريات ش12",
            TO_CHAR(NVL(im.m12_pur_rtn, 0), 'FM999,999,990.00') AS "مردود مشتريات ش12"
        FROM item_groups ig
        JOIN inventory_mov im ON ig.I_CODE = im.I_CODE
        ORDER BY ig.main_grp, ig.I_CODE
    """},

      {"id":"warehouse_rebalancing","title":"إعادة التوازن (نقل المخزون لتفادي الشراء)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":"""
        WITH wh_stock AS (
            SELECT mv.I_CODE, mv.W_CODE,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as qty
            FROM IAS20261.ITEM_MOVEMENT mv
            WHERE mv.W_CODE IN ('105', '103', '121', '122', '118', '108', '119')
              AND mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY mv.I_CODE, mv.W_CODE
        ),
        item_matrix AS (
            SELECT I_CODE,
                   SUM(CASE WHEN W_CODE = '105' THEN qty ELSE 0 END) as w_105,
                   SUM(CASE WHEN W_CODE = '103' THEN qty ELSE 0 END) as w_103,
                   SUM(CASE WHEN W_CODE = '121' THEN qty ELSE 0 END) as w_121,
                   SUM(CASE WHEN W_CODE = '122' THEN qty ELSE 0 END) as w_122,
                   SUM(CASE WHEN W_CODE = '118' THEN qty ELSE 0 END) as w_118,
                   SUM(CASE WHEN W_CODE = '108' THEN qty ELSE 0 END) as w_108,
                   SUM(CASE WHEN W_CODE = '119' THEN qty ELSE 0 END) as w_119,
                   MAX(qty) as max_qty,
                   MIN(qty) as min_qty,
                   SUM(qty) as tot_qty
            FROM wh_stock
            GROUP BY I_CODE
            HAVING SUM(qty) > 0
        )
        SELECT m.I_CODE AS "رمز الصنف",
               i.I_NAME AS "اسم الصنف",
               TO_CHAR(m.tot_qty, 'FM999,999,990') AS "إجمالي الأرصدة (كل الفروع)",
               TO_CHAR(m.w_103, 'FM999,999,990') AS "الغنامية عيظه (103)",
               TO_CHAR(m.w_121, 'FM999,999,990') AS "جده (121)",
               TO_CHAR(m.w_122, 'FM999,999,990') AS "الشمال (122)",
               TO_CHAR(m.w_105, 'FM999,999,990') AS "الغنامية نصرالله (105)",
               TO_CHAR(m.w_118, 'FM999,999,990') AS "الجنوب خميس مشيط (118)",
               TO_CHAR(m.w_119, 'FM999,999,990') AS "الدمام (119)",
               TO_CHAR(m.w_108, 'FM999,999,990') AS "المنصورية 1 (108)"
        FROM item_matrix m
        JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = m.I_CODE
        WHERE m.min_qty = 0 AND m.max_qty > 0
          AND (:i_code IS NULL OR m.I_CODE = :i_code)
        ORDER BY m.tot_qty DESC
      """},
      {"id":"dead_stock_value","title":"القيمة المالية للركود (مراكز التكلفة)","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"أيام الركود","type":"number","default":"90"}],"sql":"""
        WITH stock_movements AS (
            SELECT mv.W_CODE,
                   mv.I_CODE,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as qty,
                   MAX(NVL(mv.STK_COST,0)) as unit_cost,
                   MAX(CASE WHEN NVL(mv.IN_OUT,0) <> 1 THEN mv.I_DATE END) as last_out_date
            FROM IAS20261.ITEM_MOVEMENT mv
            WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            GROUP BY mv.W_CODE, mv.I_CODE
            HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) > 0
        )
        SELECT s.W_CODE AS "رقم المستودع",
               MAX(w.W_A_NAME) AS "اسم المستودع",
               COUNT(s.I_CODE) AS "عدد الأصناف",
               TO_CHAR(SUM(s.qty), 'FM999,999,990.00') AS "الكمية",
               TO_CHAR(SUM(s.qty * s.unit_cost), 'FM999,999,990.00') AS "القيمة المالية"
        FROM stock_movements s
        LEFT JOIN (
           SELECT '103' as W_CODE, 'الغنامية عيظه' as W_A_NAME FROM DUAL UNION ALL
           SELECT '121' as W_CODE, 'جده' as W_A_NAME FROM DUAL UNION ALL
           SELECT '122' as W_CODE, 'الشمال' as W_A_NAME FROM DUAL UNION ALL
           SELECT '105' as W_CODE, 'الغنامية نصرالله' as W_A_NAME FROM DUAL UNION ALL
           SELECT '118' as W_CODE, 'الجنوب خميس مشيط' as W_A_NAME FROM DUAL UNION ALL
           SELECT '119' as W_CODE, 'الدمام' as W_A_NAME FROM DUAL UNION ALL
           SELECT '108' as W_CODE, 'المنصورية 1' as W_A_NAME FROM DUAL
        ) w ON w.W_CODE = TO_CHAR(s.W_CODE)
        WHERE (TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(s.last_out_date) >= :days
               OR s.last_out_date IS NULL)
        GROUP BY s.W_CODE
        ORDER BY SUM(s.qty * s.unit_cost) DESC
      """},
      {"id":"smart_replenishment","title":"ذكاء المشتريات (تغطية المخزون)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"فترة سحب المبيعات (أيام)","type":"number","default":"90"},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":"""
        WITH stock AS (
            SELECT mv.I_CODE, 
                   MAX(i.I_NAME) as I_NAME,
                   SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as current_qty
            FROM IAS20261.ITEM_MOVEMENT mv
            LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE = mv.I_CODE
            WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
            AND (:i_code IS NULL OR mv.I_CODE = :i_code)
            GROUP BY mv.I_CODE
            HAVING SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) > 0
        ),
        sales AS (
            SELECT dt.I_CODE, 
                   SUM(CASE WHEN dt.IN_OUT = -1 AND dt.DOC_TYPE IN (1, 7) THEN NVL(dt.I_QTY,0) 
                            WHEN dt.IN_OUT = 1 AND dt.DOC_TYPE = 3 THEN -NVL(dt.I_QTY,0) 
                            ELSE 0 END) as sold_qty
            FROM IAS20261.ITEM_MOVEMENT dt
            WHERE dt.I_DATE >= TO_DATE(:as_of,'YYYY-MM-DD') - :days 
              AND dt.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
              AND (:i_code IS NULL OR dt.I_CODE = :i_code)
            GROUP BY dt.I_CODE
        )
        SELECT s.I_CODE AS "رمز الصنف", 
               s.I_NAME AS "اسم الصنف",
               TO_CHAR(s.current_qty, 'FM999,999,990.00') AS "الرصيد الحالي",
               TO_CHAR(NVL(sa.sold_qty, 0), 'FM999,999,990.00') AS "إجمالي السحب",
               TO_CHAR(NVL(sa.sold_qty, 0) / :days, 'FM999,999,990.00') AS "متوسط السحب اليومي",
               CASE WHEN NVL(sa.sold_qty, 0) > 0 THEN
                  TO_CHAR(s.current_qty / (sa.sold_qty / :days), 'FM999,999,990')
               ELSE 'ركود تام' END AS "أيام التغطية المتبقية",
               CASE 
                  WHEN NVL(sa.sold_qty, 0) <= 0 THEN 'مكدس (لا يوجد سحب)'
                  WHEN (s.current_qty / (sa.sold_qty / :days)) < 15 THEN 'حرج (شراء فوري)'
                  WHEN (s.current_qty / (sa.sold_qty / :days)) <= 60 THEN 'مستقر'
                  ELSE 'مكدس (فائض)'
               END AS "حالة الصنف"
        FROM stock s
        LEFT JOIN sales sa ON sa.I_CODE = s.I_CODE
        ORDER BY 
            CASE 
               WHEN NVL(sa.sold_qty, 0) <= 0 THEN 999999
               ELSE s.current_qty / (sa.sold_qty / :days) 
            END ASC
        """},
      
    {"id":"stock_bal","title":"أرصدة الأصناف","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"w_code","label":"المستودع (اختياري)","type":"text","default":""},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":"""
      SELECT * FROM (
        SELECT mv.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))),'FM999,999,990.00') AS "الرصيد",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '103' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الغنامية عيظه (103)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '121' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "جده (121)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '122' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الشمال (122)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '105' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الغنامية نصرالله (105)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '118' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الجنوب خميس مشيط (118)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '119' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "الدمام (119)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE = '108' THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "المنصورية 1 (108)",
               TO_CHAR(SUM(CASE WHEN mv.W_CODE NOT IN ('103','121','122','105','118','119','108') THEN DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0)) ELSE 0 END), 'FM999,999,990.00') AS "مستودعات أخرى",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)),'FM999,999,999,990.00') AS "قيمة الرصيد (تقريبية)"
        FROM IAS20261.ITEM_MOVEMENT mv LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=mv.I_CODE
        WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
          AND (:w_code IS NULL OR mv.W_CODE = :w_code)
          AND (:i_code IS NULL OR mv.I_CODE = :i_code)
        GROUP BY mv.I_CODE HAVING SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) <> 0
        ORDER BY SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)) DESC
      ) """},
    {"id":"stock_move","title":"حركة صنف","params":[{"name":"i_code","label":"كود الصنف","type":"text","default":""},DFROM,DTO],"sql":"""
      SELECT * FROM (
        SELECT TO_CHAR(mv.I_DATE,'DD/MM/YYYY') AS "التاريخ", mv.DOC_NO AS "المستند",
               CASE NVL(mv.IN_OUT,0) WHEN 1 THEN 'وارد' ELSE 'صادر' END AS "الاتجاه",
               TO_CHAR(NVL(mv.I_QTY,0),'FM999,999,990.00') AS "الكمية",
               TO_CHAR(NVL(mv.STK_COST,0),'FM999,999,990.00') AS "التكلفة",
               mv.W_CODE AS "المستودع"
        FROM IAS20261.ITEM_MOVEMENT mv
        WHERE mv.I_CODE = :i_code
          AND mv.I_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND mv.I_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        ORDER BY mv.I_DATE, mv.DOC_NO
      ) """},
    {"id":"stock_dormant","title":"الأصناف الراكدة (لم تُبَع)","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"أيام الركود","type":"number","default":"90"}],"sql":"""
      SELECT * FROM (
        SELECT mv.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))),'FM999,999,990.00') AS "الرصيد",
               TO_CHAR(MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END),'DD/MM/YYYY') AS "آخر صرف",
               TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END)) AS "أيام منذ آخر صرف"
        FROM IAS20261.ITEM_MOVEMENT mv LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=mv.I_CODE
        WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
        GROUP BY mv.I_CODE
        HAVING SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) > 0
           AND ( MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END) IS NULL
                 OR TRUNC(TO_DATE(:as_of,'YYYY-MM-DD')) - TRUNC(MAX(CASE WHEN NVL(mv.IN_OUT,0)<>1 THEN mv.I_DATE END)) >= :days )
        ORDER BY SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))) DESC
      ) """},
    {"id":"main_wh_movement","title":"حركة الأصناف (7 مستودعات)","fn":"run_main_wh_movement","params":[{"name":"i_code","label":"كود الصنف (اختياري)","type":"text","default":""},DFROM,DTO],"sql":""},
  ]},
  {"id":"general","title":"تقارير عامة","icon":"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z","reports":[
    {"id":"detailed_net_jrn","title":"قيود الشبكة التفصيلي","params":[DFROM,DTO,REP,CST],"sql":"""
      SELECT TO_CHAR(p.DOC_DATE,'YYYY-MM-DD') AS "التاريخ",
             p.DOC_NO AS "رقم القيد",
             p.C_CODE AS "كود العميل",
             MAX(c.C_A_NAME) AS "اسم العميل",
             p.REP_CODE AS "كود المندوب",
             MAX(sm.REPRS_A_NAME) AS "اسم المندوب",
             p.A_CODE AS "كود الحساب",
             MAX(a.A_NAME) AS "اسم الحساب",
             MAX(p.DOC_DESC) AS "البيان",
             TO_CHAR(SUM(NVL(p.CR_AMT,0)),'FM999,999,990.00') AS "المبلغ"
      FROM IAS20261.IAS_POST_DTL p
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
      LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE = p.REP_CODE
      LEFT JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
      WHERE NVL(p.DOC_POST,0) = 1 
        AND p.DOC_TYPE = 1 
        AND p.JV_TYPE = 2 
        AND NVL(p.CR_AMT,0) > 0
        AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
        AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        AND (:rep_code IS NULL OR p.REP_CODE = :rep_code)
        AND (:c_code IS NULL OR p.C_CODE = :c_code)
      GROUP BY p.DOC_DATE, p.DOC_NO, p.C_CODE, p.REP_CODE, p.A_CODE
      ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
    """}
  ]},
  {"id":"hr","title":"الموظفين والرواتب","icon":"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z","reports":[
         {"id":"emp_directory","title":"كشف ورصيد الموظفين الشامل (170 موظف)","params":[EMPST,EMPSRCH],"sql":"""
         SELECT e.EMP_NO AS "كود الموظف",
                TRIM(e.EMP_L_NM) AS "اسم الموظف والوظيفة",
                TO_CHAR(e.STRT_WRK_DATE, 'YYYY-MM-DD') AS "تاريخ المباشرة",
                CASE WHEN NVL(e.INACTIVE, 0) = 0 THEN 'نشط' ELSE 'موقوف/مستقيل' END AS "حالة الموظف",
                CASE WHEN e.SLRY_PAY_WAY = 2 THEN 'تحويل بنكي' WHEN e.SLRY_PAY_WAY = 1 THEN 'تسليم نقدي' ELSE 'غير محدد' END AS "طريقة استلام الراتب",
                CASE WHEN NVL(e.SLRY_CALC, 0) = 1 THEN 'شهري' WHEN NVL(e.SLRY_CALC, 0) = 2 THEN 'يومي' ELSE 'معياري' END AS "احتساب الراتب",
                TO_CHAR(NVL(e.WRK_HRS_DY, 8)) AS "ساعات العمل/يوم",
                TO_CHAR(NVL(e.WRK_DY_MNTH, 30)) AS "أيام العمل/شهر"
         FROM IAS20261.S_EMP e
         WHERE (:emp_status IS NULL OR (:emp_status = '1' AND NVL(e.INACTIVE, 0) = 0) OR (:emp_status = '0' AND NVL(e.INACTIVE, 0) = 1))
           AND (:emp_search IS NULL OR TO_CHAR(e.EMP_NO) LIKE '%' || :emp_search || '%' OR e.EMP_L_NM LIKE '%' || :emp_search || '%')
         ORDER BY e.EMP_NO
         """},
         {"id":"payroll_financial_summary","title":"كشف الرواتب والتأمينات والبدلات المالي (إجمالي)","params":[DFROM,DTO],"sql":"""
         SELECT p.A_CODE AS "كود الحساب",
                a.A_NAME AS "اسم البند المحاسبي",
                COUNT(*) AS "عدد الحركات",
                TO_CHAR(SUM(NVL(p.DR_AMT,0)), 'FM999,999,990.00') AS "إجمالي الصرف والرواتب",
                TO_CHAR(SUM(NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "إجمالي التسويات والدائن",
                TO_CHAR(SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)), 'FM999,999,990.00') AS "الصافي المالي"
         FROM IAS20261.IAS_POST_DTL p
         JOIN IAS20261.ACCOUNT a ON a.A_CODE = p.A_CODE
         WHERE (p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%' OR p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '21104%')
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
         GROUP BY p.A_CODE, a.A_NAME
         ORDER BY SUM(NVL(p.DR_AMT,0)) DESC
         """},
         {"id":"employee_advances_loans","title":"كشف حركة ورصيد رواتب وسلف الموظفين (بالفرز والمبالغ)","params":[DFROM,DTO,MINAMT,MAXAMT,TXTSRCH],"sql":"""
         SELECT TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') AS "التاريخ",
                p.DOC_NO AS "رقم المستند",
                CASE p.DOC_TYPE WHEN 1 THEN 'قيد يومية' WHEN 2 THEN 'سند قبض' WHEN 3 THEN 'سند صرف' ELSE 'قيد أونكس' END AS "نوع المستند",
                NVL(sm.REPRS_A_NAME, TO_CHAR(p.CC_CODE)) AS "الجهة / مركز التكلفة",
                TO_CHAR(NVL(p.DR_AMT, 0), 'FM999,999,990.00') AS "سلفة / راتب / مدين",
                TO_CHAR(NVL(p.CR_AMT, 0), 'FM999,999,990.00') AS "سداد / تسوية / دائن",
                NVL(p.DOC_DESC, 'قيد تلقائي') AS "اسم الموظف / البيان والتفاصيل"
         FROM IAS20261.IAS_POST_DTL p
         LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = TO_CHAR(p.CC_CODE)
         WHERE (p.A_CODE LIKE '11402%' OR p.A_CODE LIKE '321%' OR p.A_CODE LIKE '324%')
           AND NVL(p.DOC_POST, 0) = 1
           AND p.DOC_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD') + 1
           AND (:min_amt IS NULL OR NVL(p.DR_AMT, 0) >= TO_NUMBER(:min_amt) OR NVL(p.CR_AMT, 0) >= TO_NUMBER(:min_amt))
           AND (:max_amt IS NULL OR (NVL(p.DR_AMT, 0) <= TO_NUMBER(:max_amt) AND NVL(p.CR_AMT, 0) <= TO_NUMBER(:max_amt)))
           AND (:text_search IS NULL OR p.DOC_DESC LIKE '%' || :text_search || '%' OR sm.REPRS_A_NAME LIKE '%' || :text_search || '%')
         ORDER BY p.DOC_DATE DESC, p.DOC_NO DESC
         """},
         {"id":"salesmen_hr_link","title":"ربط المناديب بسجل الموظفين","params":[REP],"sql":"""
         SELECT sm.REPRS_CODE AS "كود المندوب",
                sm.REPRS_A_NAME AS "اسم المندوب في المبيعات",
                NVL(e.EMP_NO, sm.REPRS_CODE) AS "كود الموظف المربوط",
                NVL(TRIM(e.EMP_L_NM), 'غير موصول برقم موظف') AS "اسم الموظف في HR",
                CASE WHEN e.EMP_NO IS NOT NULL THEN 'مربوط بسجل HR' ELSE 'غير مربوط' END AS "حالة الربط"
         FROM IAS20261.SALES_MAN sm
         LEFT JOIN IAS20261.S_EMP e ON e.EMP_NO = sm.REPRS_CODE
         WHERE (:rep_code IS NULL OR sm.REPRS_CODE = :rep_code)
         ORDER BY sm.REPRS_CODE
         """}
  ]},
]

TABMAP = {t["id"]: t for t in TABS}


def find_report(tab, rid):
    t = TABMAP.get(tab) or TABS[0]
    for r in t['reports']:
        if r['id'] == rid:
            return t, r
    return t, t['reports'][0]
