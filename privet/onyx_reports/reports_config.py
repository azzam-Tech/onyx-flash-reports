from utils.logger import logger
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
    {"id":"critical_debts","title":"الديون الخطرة وتوقف العملاء (مؤشر خطر)","params":[{"name":"days_threshold","label":"أيام التوقف (الحد الأدنى)","type":"number","default":"90"}],"sql":""},
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
    ],"sql":""}, {"id":"statement_analytic","title":"كشف حساب تحليلي","params":[{"name":"ac_code_dtl","label":"الحساب التحليلي","type":"text","default":"1381"},DFROM,DTO],"sql":""}, {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":""}, {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":""}, {"id":"true_income_statement","title":"قائمة الدخل (الحقيقية)","params":[DFROM,DTO,REP],"sql":""}
 ,
   {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT],"sql":""}]},

 {"id":"sales","title":"المبيعات","icon":"M4 20V10M10 20V4M16 20v-7M22 20H2","reports":[
   {"id":"bills","title":"فواتير المبيعات","params":[DFROM,DTO,BTYPE,REP,CST],"sql":""},
    {"id":"by_item","title":"حسب الصنف","params":[DFROM,DTO,ITM,REP],"sql":""},
    {"id":"by_customer","title":"حسب العميل","params":[DFROM,DTO,CST,REP],"sql":""},
    {"id":"by_salesman","title":"حسب المندوب","params":[DFROM,DTO,REP],"sql":""},
    {"id":"net_sales_cc","title":"صافي المبيعات مع الخصومات (مراكز التكلفة)","params":[DFROM,DTO,{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},{"name":"inc_ext","label":"إشعار خصم مستقل (خصم)","type":"select","default":"0","options":[["1","خصم"],["0","تجاهل"]]}],"sql":""},
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
   {"id":"balances","title":"أرصدة العملاء","params":[DTO,CST,REP],"sql":""},
    {"id":"statement","title":"كشف حساب عميل","params":[{"name":"c_code","label":"كود العميل","type":"text","default":"1381"},DFROM,DTO],"sql":""},
    {"id":"statement_analytic","title":"كشف حساب تحليلي","params":[{"name":"ac_code_dtl","label":"الحساب التحليلي","type":"text","default":"1381"},DFROM,DTO],"sql":""},
    {"id":"aging","title":"أعمار الديون","fn":"run_cust_aging","params":[{"name":"vendor_link","label":"عميل مرتبط بمورد","type":"checkbox","default":"0"},{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},
     DTO,
     AGETR,
     {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""},
     {"name":"c_code","label":"كود العميل (اختياري)","type":"text","default":""}
   ]},
   {"id":"dormant","title":"العملاء الخاملون","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"أيام الخمول","type":"number","default":"90"}],"sql":""}
]},
 {"id":"dts","title":"التوزيع والمناديب","icon":"M3 13l3-7h7l3 4h4v5M3 13h17M6 18a2 2 0 100-4 2 2 0 000 4zm11 0a2 2 0 100-4 2 2 0 000 4z","reports":[
        {"id":"collection_adopted","title":"التحصيل المعتمد (ديناميكي)","params":[DFROM,DTO,GRP,REP,INCR,INCN,INCC,INCRT],"sql":""},
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":""},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":""},
        {"id":"perf_aging_exact","title":"أعمار التحصيل (مطابق أونكس 100%)","params":[DFROM,DTO,REP],"sql":""}
  ]},
  {"id":"pur","title":"المشتريات والموردون","icon":"M6 6h15l-1.5 9h-12zM6 6L5 3H2M9 20a1 1 0 100-2 1 1 0 000 2zm9 0a1 1 0 100-2 1 1 0 000 2z","reports":[
   {"id":"pi_bills","title":"فواتير المشتريات","params":[DFROM,DTO,{"name":"v_code","label":"المورد (اختياري)","type":"text","default":""}],"sql":""},
   {"id":"pi_by_vendor","title":"حسب المورد","params":[DFROM,DTO],"sql":""},
   {"id":"pi_by_item","title":"حسب الصنف","params":[DFROM,DTO,{"name":"i_code","label":"الصنف (اختياري)","type":"text","default":""}],"sql":""},
   {"id":"vendor_statement","title":"كشف حساب مورد","params":[{"name":"v_code","label":"كود المورد","type":"text","default":"222"},DFROM,DTO],"sql":""},
   {"id":"vendor_aging","title":"أعمار الدائنين","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"}],"sql":""},
 ]},
 {"id":"fin","title":"المالية والمحاسبة","icon":"M4 20V4h16v16zM8 16v-4M12 16V8M16 16v-6","reports":[
   {"id":"trial_balance","title":"ميزان المراجعة","params":[DFROM,DTO],"sql":""},
   {"id":"income_statement","title":"قائمة الدخل","params":[DFROM,DTO],"sql":""},
   {"id":"cost_centers","title":"مراكز التكلفة","params":[DFROM,DTO],"sql":""},
   {"id":"journal","title":"قيود اليومية","params":[{"name":"date_from","label":"من تاريخ","type":"date","default":"2026-07-01"},{"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"a_code","label":"الحساب (اختياري)","type":"text","default":""}],"sql":""},
        
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":""},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[{"name":"grp_code","label":"مجموعة العملاء (اختياري)","type":"text","default":""},{"name":"cc_code","label":"مركز التكلفة (اختياري)","type":"text","default":""},DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":""},
   {"id":"perf_aging_exact","title":"أعمار التحصيل (مطابق أونكس 100%)","params":[DFROM,DTO,REP],"sql":""},
 ]},
 {"id":"tax","title":"الضريبة","icon":"M4 4h16v4H4zM6 8v12M18 8v12M4 20h16M9 12h6M9 16h6","reports":[
   {"id":"vat_decl","title":"الإقرار الضريبي (شهري)","params":[],"sql":""},
   {"id":"vat_out","title":"تفصيل ضريبة المخرجات","params":[],"sql":""},
   {"id":"vat_in","title":"تفصيل ضريبة المدخلات","params":[],"sql":""},
 ]},
   {"id":"prof","title":"الربحية","icon":"M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z","reports":[
    {"id":"prof_summary","title":"ملخّص مجمل الربح للفترة","params":[DFROM,DTO,REP],"sql":""},
    {"id":"net_profit","title":"صافي الربح للفترة (بعد كل المصاريف)","params":[DFROM,DTO],"sql":""},
    {"id":"prof_item","title":"ربحية الصنف","params":[DFROM,DTO,ITM,REP],"sql":""},
    {"id":"prof_cust","title":"ربحية العميل","params":[DFROM,DTO,CST,REP],"sql":""},
    {"id":"prof_rep","title":"ربحية المندوب","params":[DFROM,DTO,REP],"sql":""},
    {"id":"true_income_statement","title":"قائمة الدخل (الحقيقية)","params":[DFROM,DTO,REP],"sql":""}
  ]},
 {"id":"stock","title":"المخزون","icon":"M3 7l9-4 9 4-9 4zM3 7v10l9 4 9-4V7M12 11v10","reports":[
    {"id":"detailed_stock_pivot","pivot_type":"detailed_stock","title":"حركة وأرصدة المخزون الشامل","params":[DFROM,DTO],"sql":""},

          {"id":"monthly_movement_pivot","pivot_type":"monthly_movement","title":"حركة الأصناف الشهرية (مبيعات/مشتريات)","params":[PYEAR],"sql":""},

      {"id":"warehouse_rebalancing","title":"إعادة التوازن (نقل المخزون لتفادي الشراء)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":""},
      {"id":"dead_stock_value","title":"القيمة المالية للركود (مراكز التكلفة)","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"أيام الركود","type":"number","default":"90"}],"sql":""},
      {"id":"smart_replenishment","title":"ذكاء المشتريات (تغطية المخزون)","params":[{"name":"as_of","label":"إلى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"فترة سحب المبيعات (أيام)","type":"number","default":"90"},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":""},
      
    {"id":"stock_bal","title":"أرصدة الأصناف","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"w_code","label":"المستودع (اختياري)","type":"text","default":""},{"name":"i_code","label":"رقم الصنف (اختياري)","type":"text","default":""}],"sql":""},
    {"id":"stock_move","title":"حركة صنف","params":[{"name":"i_code","label":"كود الصنف","type":"text","default":""},DFROM,DTO],"sql":""},
    {"id":"stock_dormant","title":"الأصناف الراكدة (لم تُبَع)","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"days","label":"أيام الركود","type":"number","default":"90"}],"sql":""},
    {"id":"main_wh_movement","title":"حركة الأصناف (7 مستودعات)","fn":"run_main_wh_movement","params":[{"name":"i_code","label":"كود الصنف (اختياري)","type":"text","default":""},DFROM,DTO],"sql":""},
  ]},
  {"id":"general","title":"تقارير عامة","icon":"M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zm-5 14H7v-2h7v2zm3-4H7v-2h10v2zm0-4H7V7h10v2z","reports":[
    {"id":"daily_expenses","title":"تقرير المصاريف اليومية","hide_from_menu":True,"params":[
      DFROM, DTO,
      {"name":"ac_code","label":"رقم الحساب (اختياري)","type":"text","default":""},
      {"name":"text_search","label":"بحث في البيان (اختياري)","type":"text","default":""}
    ],"sql":""},
    {"id":"detailed_net_jrn","title":"قيود الشبكة التفصيلي","params":[DFROM,DTO,REP,CST],"sql":""}
  ]},
  {"id":"hr","title":"الموظفين والرواتب","icon":"M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z","reports":[
         {"id":"emp_directory","title":"كشف ورصيد الموظفين الشامل (170 موظف)","params":[EMPST,EMPSRCH],"sql":""},
         {"id":"payroll_financial_summary","title":"كشف الرواتب والتأمينات والبدلات المالي (إجمالي)","params":[DFROM,DTO],"sql":""},
         {"id":"employee_advances_loans","title":"كشف حركة ورصيد رواتب وسلف الموظفين (بالفرز والمبالغ)","params":[DFROM,DTO,MINAMT,MAXAMT,TXTSRCH],"sql":""},
         {"id":"salesmen_hr_link","title":"ربط المناديب بسجل الموظفين","params":[REP],"sql":""}
  ]},
]

TABMAP = {t["id"]: t for t in TABS}


def find_report(tab, rid):
    t = TABMAP.get(tab) or TABS[0]
    for r in t['reports']:
        if r['id'] == rid:
            return t, r
    return t, t['reports'][0]
