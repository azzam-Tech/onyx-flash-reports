# -*- coding: utf-8 -*-
"""لوحة تقارير SREEN — Flask + Oracle (RTL). تبويبات رئيسية وفرعية موصولة بالاستعلامات."""

import os
import json
import oracledb
import io
from urllib.parse import urlencode
from datetime import datetime
from flask import Flask, request, render_template_string, Response, session

app = Flask(__name__)
app.secret_key = os.environ.get("SREEN_SECRET", "sreen-reports-2026-secret-key")
SETTINGS_PIN = os.environ.get("SETTINGS_PIN", "00900")
APP_PIN = os.environ.get("APP_PIN", "00900")

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib) if _lib else oracledb.init_oracle_client()
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

LOGIN_PAGE = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <title>تسجيل الدخول - نظام التقارير</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;800&display=swap');
    body { margin: 0; padding: 0; background-color: #f4f5f8; font-family: 'Cairo', sans-serif; display: flex; align-items: center; justify-content: center; height: 100vh; }
    .card { background: #fff; padding: 40px; border-radius: 16px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); text-align: center; max-width: 400px; width: 100%; border-top: 6px solid #4f46e5; }
    h2 { color: #1e293b; font-weight: 800; margin-bottom: 5px; }
    p { color: #64748b; margin-bottom: 25px; }
    input[type=password] { width: 100%; padding: 12px; margin-bottom: 20px; border: 2px solid #e2e8f0; border-radius: 8px; font-size: 16px; text-align: center; font-family: inherit; font-weight: 600; box-sizing: border-box; }
    input[type=password]:focus { outline: none; border-color: #4f46e5; }
    button { background: #4f46e5; color: #fff; border: none; border-radius: 8px; padding: 12px 20px; font-size: 16px; cursor: pointer; width: 100%; font-weight: 600; transition: background 0.2s; }
    button:hover { background: #4338ca; }
    .err { color: #ef4444; background: #fee2e2; padding: 10px; border-radius: 8px; margin-bottom: 15px; font-size: 14px; }
  


</style>


</head>
<body>
  <div class="card">
    <svg width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="#4f46e5" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-bottom:10px;"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"></rect><path d="M7 11V7a5 5 0 0 1 10 0v4"></path></svg>
    <h2>نظام التقارير</h2>
    <p>يرجى إدخال رمز المرور للمتابعة</p>
    {% if error %}<div class="err">{{ error }}</div>{% endif %}
    <form method="POST">
      <input type="password" name="pin" placeholder="الرمز السري (PIN)" autofocus required>
      <button type="submit">دخول آمن</button>
    </form>
  </div>
</body>
</html>"""

from flask import redirect

@app.before_request
def require_login():
    if request.endpoint not in ('login', 'static') and not session.get('logged_in'):
        return redirect('/login')

@app.route("/login", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        if request.form.get("pin") == APP_PIN:
            session['logged_in'] = True
            return redirect('/')
        else:
            error = "الرمز غير صحيح، حاول مرة أخرى."
    return render_template_string(LOGIN_PAGE, error=error)

@app.route("/logout")
def logout():
    session.pop('logged_in', None)
    return redirect('/login')



def get_conn():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

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
      {"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترات الزمنية"]]}
    ],"sql":""},
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
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
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
       ) ORDER BY s1, s2, s3"""}, {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """}, {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
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
              SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_dr,
              0 as op_cr,
              SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_dr,
              0 as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
          JOIN IAS20261.IAS_BILL_MST m 
            ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
           AND m.BILL_NO = im.DOC_NO 
           AND m.BILL_SER = im.DOC_SER
          WHERE (:rep_code IS NULL OR m.REP_CODE = :rep_code)
            AND im.DOC_TYPE = 1 
            AND NVL(im.I_QTY,0) > 0
        ),
        inv_cogs_ret AS (
          SELECT 
              '311030001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
          JOIN IAS20261.IAS_RT_BILL_MST r
            ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
           AND r.RT_BILL_NO = im.DOC_NO 
           AND r.RT_BILL_SER = im.DOC_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
            AND im.DOC_TYPE = 3
            AND r.PREV_YEAR IS NULL
            AND NVL(im.I_QTY,0) > 0
        ),
        inv_cogs_ret_prev AS (
          SELECT 
              '311060001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
          JOIN IAS20261.IAS_RT_BILL_MST r
            ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
           AND r.RT_BILL_NO = im.DOC_NO 
           AND r.RT_BILL_SER = im.DOC_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
            AND im.DOC_TYPE = 3
            AND r.PREV_YEAR IS NOT NULL
            AND NVL(im.I_QTY,0) > 0
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
      {"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترات الزمنية"]]}
    ],"sql":""},
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
      {"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترات الزمنية"]]}
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
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
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
         LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
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
    {"id":"aging","title":"أعمار الديون","params":[
     DTO,
     {"name":"rep_code","label":"المندوب (اختياري)","type":"text","default":""},
     {"name":"c_code","label":"كود العميل (اختياري)","type":"text","default":""}
   ],"sql":"""
     WITH pay AS (SELECT C_CODE, SUM(NVL(CR_AMT,0)) paid FROM IAS20261.IAS_POST_DTL
                  WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
                  GROUP BY C_CODE),
     charges AS (SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0) amt,
                   SUM(NVL(p.DR_AMT,0)) OVER (PARTITION BY p.C_CODE ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) cum
                 FROM IAS20261.IAS_POST_DTL p
                 WHERE NVL(p.DOC_POST,0)=1 AND p.C_CODE IS NOT NULL AND NVL(p.DR_AMT,0)>0
                   AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1),
     openit AS (SELECT ch.C_CODE, GREATEST(0,LEAST(ch.amt,ch.cum-NVL(pay.paid,0))) unpaid,
                   TRUNC(TO_DATE(:date_to,'YYYY-MM-DD'))-TRUNC(ch.DOC_DATE) age
                FROM charges ch LEFT JOIN pay ON pay.C_CODE=ch.C_CODE)
     SELECT o.C_CODE AS "كود العميل", MAX(c.C_A_NAME) AS "اسم العميل", MAX(c.REP_CODE) AS "المندوب",
            TO_CHAR(SUM(CASE WHEN o.age<=30 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "0-30",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 31 AND 60 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "31-60",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 61 AND 90 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "61-90",
            TO_CHAR(SUM(CASE WHEN o.age BETWEEN 91 AND 120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "91-120",
            TO_CHAR(SUM(CASE WHEN o.age>120 THEN o.unpaid ELSE 0 END),'FM999,999,990.00') AS "أكثر من 120",
            TO_CHAR(SUM(o.unpaid),'FM999,999,990.00') AS "الإجمالي"
     FROM openit o LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE=o.C_CODE
     WHERE o.unpaid>0 AND (:rep_code IS NULL OR c.REP_CODE = :rep_code)
       AND (:c_code IS NULL OR o.C_CODE = :c_code)
     GROUP BY o.C_CODE ORDER BY SUM(o.unpaid) DESC"""},
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
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
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
       LEFT JOIN IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS d ON d.DOC_TYPE=p.DOC_TYPE AND d.JV_TYPE=p.JV_TYPE AND d.LANG_NO=1
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
        
        {"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_analytical","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
       -- This report dynamically processes valid collections via Python FIFO per customer
       SELECT 'Dynamic Analytical' as "Placeholder" FROM DUAL
       """},
        {"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT],"sql":"""
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
              SUM(CASE WHEN m.BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_dr,
              0 as op_cr,
              SUM(CASE WHEN m.BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND m.BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_dr,
              0 as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
          JOIN IAS20261.IAS_BILL_MST m 
            ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
           AND m.BILL_NO = im.DOC_NO 
           AND m.BILL_SER = im.DOC_SER
          WHERE (:rep_code IS NULL OR m.REP_CODE = :rep_code)
            AND im.DOC_TYPE = 1 
            AND NVL(im.I_QTY,0) > 0
        ),
        inv_cogs_ret AS (
          SELECT 
              '311030001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
          JOIN IAS20261.IAS_RT_BILL_MST r
            ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
           AND r.RT_BILL_NO = im.DOC_NO 
           AND r.RT_BILL_SER = im.DOC_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
            AND im.DOC_TYPE = 3
            AND r.PREV_YEAR IS NULL
            AND NVL(im.I_QTY,0) > 0
        ),
        inv_cogs_ret_prev AS (
          SELECT 
              '311060001' as acc_code,
              0 as op_dr,
              SUM(CASE WHEN r.RT_BILL_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as op_cr,
              0 as mv_dr,
              SUM(CASE WHEN r.RT_BILL_DATE >= TO_DATE(:date_from, 'YYYY-MM-DD') AND r.RT_BILL_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1 THEN NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) ELSE 0 END) as mv_cr
          FROM IAS20261.ITEM_MOVEMENT im
          JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
          LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
          JOIN IAS20261.IAS_RT_BILL_MST r
            ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
           AND r.RT_BILL_NO = im.DOC_NO 
           AND r.RT_BILL_SER = im.DOC_SER
          WHERE (:rep_code IS NULL OR r.REP_CODE = :rep_code)
            AND im.DOC_TYPE = 3
            AND r.PREV_YEAR IS NOT NULL
            AND NVL(im.I_QTY,0) > 0
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
    {"id":"stock_bal","title":"أرصدة الأصناف","params":[{"name":"as_of","label":"حتى تاريخ","type":"date","default":"2026-07-31"},{"name":"w_code","label":"المستودع (اختياري)","type":"text","default":""}],"sql":"""
      SELECT * FROM (
        SELECT mv.I_CODE AS "كود الصنف", MAX(i.I_NAME) AS "اسم الصنف",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))),'FM999,999,990.00') AS "الرصيد",
               TO_CHAR(SUM(DECODE(NVL(mv.IN_OUT,0),1,NVL(mv.I_QTY,0),-NVL(mv.I_QTY,0))*NVL(mv.STK_COST,0)),'FM999,999,999,990.00') AS "قيمة الرصيد (تقريبية)"
        FROM IAS20261.ITEM_MOVEMENT mv LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=mv.I_CODE
        WHERE mv.I_DATE < TO_DATE(:as_of,'YYYY-MM-DD')+1
          AND (:w_code IS NULL OR mv.W_CODE = :w_code)
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
    for r in t["reports"]:
        if r["id"] == rid:
            return t, r
    return t, t["reports"][0]

def run_perf_aging_fifo(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    
    is_dynamic = (rpt.get("id") == "perf_aging_dynamic")
    
    rep_code = args.get("rep_code")
    if is_dynamic:
        inc_rcpt = str(args.get("inc_rcpt", "1")) == "1"
        inc_net  = str(args.get("inc_net", "1")) == "1"
        inc_cash = str(args.get("inc_cash", "1")) == "1"
        inc_ret  = str(args.get("inc_ret", "1")) == "1"
        inc_ext  = False
    else:
        inc_rcpt = True
        inc_net  = False
        inc_cash = False
        inc_ret  = False
        inc_ext  = False
    if rep_code:
        rep_code = rep_code.split(" - ")[0].strip()
    
    date_from_str = args.get("date_from", "")
    date_to_str = args.get("date_to", "")
    if not date_from_str: date_from_str = "2026-07-01"
    if not date_to_str: date_to_str = "2026-07-31"
    
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT C_CODE, REP_CODE FROM IAS20261.CUSTOMER")
            cust_rep = {str(c): str(r) for c, r in cur.fetchall()}
                
            cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN")
            rep_name = {str(c): n for c, n in cur.fetchall()}

            # Get Cash Sales for the period (no C_CODE needed)
            sql_cash = """
                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))
                FROM IAS20261.IAS_BILL_MST b
                JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(b.REP_CODE)
            """
            cur.execute(sql_cash, {"df": date_from_str, "dt": date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}

            # Get Cash Returns without C_CODE
            sql_ret_null = """
                SELECT NVL(TO_CHAR(REP_CODE), 'UNKNOWN'), SUM(NVL(CR_AMT,0))
                FROM IAS20261.IAS_POST_DTL
                WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0
                  AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(REP_CODE)
            """
            cur.execute(sql_ret_null, {"df": date_from_str, "dt": date_to_str})
            cash_ret_null_by_rep = {r: float(amt) for r, amt in cur.fetchall()}

            # Fetch relevant debits and credits from IAS_POST_DTL
            rep_filter = " AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)" if rep_code else ""
            binds_fifo = {}
            if rep_code: binds_fifo["rep_code"] = rep_code
            sql = f"""
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
                    AND p.C_CODE IS NOT NULL
                    {rep_filter}
            """
            cur.execute(sql, binds_fifo)
            byc = defaultdict(lambda: {"debits": [], "credits": []})
            
            for ccode, ddate, dr, cr, dtype, jvtype, acode in cur.fetchall():
                if ccode is None: continue
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                
                valid_cr = 0.0
                if cr > 0:
                    if not is_dynamic:
                        valid_cr = cr
                    else:
                        if dtype == 2 and inc_rcpt:  # rcpt
                            valid_cr = cr
                        elif dtype == 1 and jvtype == 2 and inc_net:  # net_jrn
                            valid_cr = cr
                        elif dtype == 5 and acode and str(acode).startswith('111') and inc_ret:  # cash_ret
                            valid_cr = -cr
                        elif dtype == 15 and inc_ext:  # ext_notice
                            valid_cr = -cr
                
                if dr > 0:
                    byc[str(ccode)]["debits"].append((d, dr))
                if valid_cr != 0:
                    byc[str(ccode)]["credits"].append((d, valid_cr))

    aging_ranges_str = args.get("aging_ranges", "2,30,60,90,120")
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(",") if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]

    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append("0")
        elif prev == 0:
            bucket_labels.append(f"0-{lim}")
        else:
            bucket_labels.append(f"{prev+1}-{lim}")
        prev = lim
    bucket_labels.append(f"أكثر من {limits[-1]}")

    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)

    rep_results = defaultdict(lambda: {"cust_count": set(), "b": [0.0]*num_buckets, "total": 0.0})

    for ccode, evs in byc.items():
        r_code = cust_rep.get(ccode)
        if not r_code: continue
        if rep_code and r_code != rep_code: continue

        debits  = sorted(evs["debits"], key=lambda x: x[0])
        credits = sorted(evs["credits"], key=lambda x: x[0])
        
        dcum = 0.0; dint = []
        for (d, dr) in debits:
            lo = dcum; dcum += dr; dint.append((lo, dcum, d))
        ddates = [x[0] for x in debits]
        
        ccum = 0.0
        for (d, cr) in credits:
            clo = ccum; ccum += cr; chi = ccum
            if not (from_dt <= d <= to_dt):
                continue
            
            # Handle negative credits (deductions)
            lo_cr, hi_cr = min(clo, chi), max(clo, chi)
            is_negative = (cr < 0)
            
            rep_results[r_code]["cust_count"].add(ccode)
            rep_results[r_code]["total"] += cr
            
            for (lo, hi, idate) in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0: continue
                    
                    if is_negative: amt = -amt
                    
                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days
                    
                    rep_results[r_code]["b"][bucket_of(age)] += amt

    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                rep_results[r_code]["total"] += c_sales
                rep_results[r_code]["b"][0] += c_sales

    # Subtract cash returns without C_CODE
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and r_code != 'UNKNOWN': continue
            if c_ret > 0:
                rep_results[r_code]["total"] -= c_ret
                rep_results[r_code]["b"][0] -= c_ret

    cols = ["كود المندوب", "اسم المندوب", "عدد العملاء"] + bucket_labels + ["المبلغ المحصل"]
    rows = []
    
    for r_code, data in rep_results.items():
        # Avoid showing empty rows if net collection is 0 and buckets are 0
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        formatted_b = [f"{x:,.2f}" for x in data["b"]]
        row = (
            r_code,
            rep_name.get(r_code, r_code),
            len(data["cust_count"]),
        ) + tuple(formatted_b) + (f"{data['total']:,.2f}",)
        rows.append(row)
        
    tot_idx = len(cols) - 1
    rows.sort(key=lambda x: float(str(x[tot_idx]).replace(',','')), reverse=True)
    return cols, rows

MAIN_WAREHOUSES_CODES = ["105", "103", "121", "122", "118", "108", "119"]

def run_perf_aging_analytical(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    
    rep_code = args.get("rep_code")
    
    inc_rcpt = str(args.get("inc_rcpt", "1")) == "1"
    inc_net  = str(args.get("inc_net", "1")) == "1"
    inc_cash = str(args.get("inc_cash", "1")) == "1"
    inc_ret  = str(args.get("inc_ret", "1")) == "1"
    inc_ext  = False
    
    if rep_code:
        rep_code = rep_code.split(" - ")[0].strip()
    else:
        return ["تنبيه"], [("الرجاء اختيار المندوب أولاً من القائمة المنسدلة لعرض التقرير التحليلي.", "", "", "", "", "", "", "")]
    
    date_from_str = args.get("date_from", "")
    date_to_str = args.get("date_to", "")
    if not date_from_str: date_from_str = "2026-07-01"
    if not date_to_str: date_to_str = "2026-07-31"
    
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT C_CODE, REP_CODE, C_A_NAME FROM IAS20261.CUSTOMER")
            cust_rep = {}
            cust_names = {}
            for c, r, n in cur.fetchall():
                cust_rep[str(c)] = str(r)
                cust_names[str(c)] = str(n)
                
            cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN")
            rep_name = {str(c): n for c, n in cur.fetchall()}

            # Get Cash Sales for the period (no C_CODE needed)
            sql_cash = """
                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))
                FROM IAS20261.IAS_BILL_MST b
                JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(b.REP_CODE)
            """
            cur.execute(sql_cash, {"df": date_from_str, "dt": date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}

            # Get Cash Returns without C_CODE
            sql_ret_null = """
                SELECT NVL(TO_CHAR(REP_CODE), 'UNKNOWN'), SUM(NVL(CR_AMT,0))
                FROM IAS20261.IAS_POST_DTL
                WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0
                  AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(REP_CODE)
            """
            cur.execute(sql_ret_null, {"df": date_from_str, "dt": date_to_str})
            cash_ret_null_by_rep = {r: float(amt) for r, amt in cur.fetchall()}

            # Fetch relevant debits and credits from IAS_POST_DTL
            rep_filter = " AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)" if rep_code else ""
            binds_fifo = {}
            if rep_code: binds_fifo["rep_code"] = rep_code
            sql = f"""
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
                    AND p.C_CODE IS NOT NULL
                    {rep_filter}
            """
            cur.execute(sql, binds_fifo)
            byc = defaultdict(lambda: {"debits": [], "credits": []})
            
            for ccode, ddate, dr, cr, dtype, jvtype, acode in cur.fetchall():
                if ccode is None: continue
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                
                valid_cr = 0.0
                if cr > 0:
                    if dtype == 2 and inc_rcpt:  # rcpt
                        valid_cr = cr
                    elif dtype == 1 and jvtype == 2 and inc_net:  # net_jrn
                        valid_cr = cr
                    elif dtype == 5 and acode and str(acode).startswith('111') and inc_ret:  # cash_ret
                        valid_cr = -cr
                    elif dtype == 15 and inc_ext:  # ext_notice
                        valid_cr = -cr
                
                if dr > 0:
                    byc[str(ccode)]["debits"].append((d, dr))
                if valid_cr != 0:
                    byc[str(ccode)]["credits"].append((d, valid_cr))

    aging_ranges_str = args.get("aging_ranges", "2,30,60,90,120")
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(",") if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]

    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append("0")
        elif prev == 0:
            bucket_labels.append(f"0-{lim}")
        else:
            bucket_labels.append(f"{prev+1}-{lim}")
        prev = lim
    bucket_labels.append(f"أكثر من {limits[-1]}")

    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)

    cust_results = defaultdict(lambda: {"b": [0.0]*num_buckets, "total": 0.0})

    for ccode, evs in byc.items():
        r_code = cust_rep.get(ccode)
        if not r_code: continue
        if rep_code and r_code != rep_code: continue

        debits  = sorted(evs["debits"], key=lambda x: x[0])
        credits = sorted(evs["credits"], key=lambda x: x[0])
        
        dcum = 0.0; dint = []
        for (d, dr) in debits:
            lo = dcum; dcum += dr; dint.append((lo, dcum, d))
        ddates = [x[0] for x in debits]
        
        ccum = 0.0
        for (d, cr) in credits:
            clo = ccum; ccum += cr; chi = ccum
            if not (from_dt <= d <= to_dt):
                continue
            
            # Handle negative credits (deductions)
            lo_cr, hi_cr = min(clo, chi), max(clo, chi)
            is_negative = (cr < 0)
            
            cust_results[ccode]["total"] += cr
            
            for (lo, hi, idate) in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0: continue
                    
                    if is_negative: amt = -amt
                    
                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days
                    
                    cust_results[ccode]["b"][bucket_of(age)] += amt

    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                cust_results["CASH_SALES_" + str(r_code)]["total"] += c_sales
                cust_results["CASH_SALES_" + str(r_code)]["b"][0] += c_sales

    # Subtract cash returns without C_CODE
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and r_code != 'UNKNOWN': continue
            if c_ret > 0:
                cust_results["CASH_SALES_" + str(r_code)]["total"] -= c_ret
                cust_results["CASH_SALES_" + str(r_code)]["b"][0] -= c_ret

    cols = ["رقم العميل", "اسم العميل"] + bucket_labels + ["إجمالي التحصيل"]
    rows = []
    
    for ccode, data in cust_results.items():
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        
        if str(ccode).startswith("CASH_SALES_"):
            c_name = "مبيعات نقدية (للمندوب)"
            disp_code = "-"
        else:
            c_name = cust_names.get(str(ccode), str(ccode))
            disp_code = str(ccode)
            
        formatted_b = [f"{x:,.2f}" for x in data["b"]]
        row = (
            disp_code,
            c_name,
        ) + tuple(formatted_b) + (f"{data['total']:,.2f}",)
        rows.append(row)
        
    tot_idx = len(cols) - 1
    rows.sort(key=lambda x: float(str(x[tot_idx]).replace(',','')), reverse=True)
    return cols, rows


def run_main_wh_movement(rpt, args):
    from collections import defaultdict
    date_from_str = args.get("date_from", "2026-01-01")
    date_to_str = args.get("date_to", "2026-12-31")
    i_code_str = args.get("i_code", "").split(" - ")[0].strip()
    
    print(f"[DEBUG WH] date_from: {date_from_str}, date_to: {date_to_str}, i_code: {i_code_str}")
    
    wh_mapping = {
        "105": "مخزن عيضة",
        "103": "مخزن حسام",
        "121": "مخزن المنصورية",
        "122": "مخزن الدمام",
        "118": "مخزن تبوك",
        "108": "مخزن الجنوب",
        "119": "مخزن جده"
    }
    
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                codes_str = ",".join(MAIN_WAREHOUSES_CODES)
                cur.execute(f"SELECT W_CODE, W_NAME FROM IAS20261.WAREHOUSE_DETAILS WHERE W_CODE IN ({codes_str})")
                for w_code, w_name in cur.fetchall():
                    wh_mapping[str(w_code)] = w_name
    except Exception as e:
        print("Error fetching warehouse names dynamically:", e)

    wh_codes = MAIN_WAREHOUSES_CODES
    
    item_filter = ""
    if i_code_str:
        item_filter = " AND dt.I_CODE = :icode "
    
    sql = f"""
        SELECT
            dt.I_CODE,
            MAX(m.I_NAME),
            dt.W_CODE,
            SUM(NVL(dt.I_QTY, 0)) AS net_qty
        FROM IAS20261.ITEM_MOVEMENT dt
        LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = dt.I_CODE
        WHERE dt.I_DATE >= TO_DATE(:df, 'YYYY-MM-DD')
          AND dt.I_DATE < TO_DATE(:dt, 'YYYY-MM-DD') + 1
          AND dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
          AND dt.IN_OUT = -1
          {item_filter}
        GROUP BY dt.I_CODE, dt.W_CODE
        HAVING SUM(NVL(dt.I_QTY, 0)) > 0
    """
    
    params = {"df": date_from_str, "dt": date_to_str}
    if i_code_str:
        params["icode"] = i_code_str
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, params)
            results = cur.fetchall()
            print(f"[DEBUG WH] Query returned {len(results)} raw grouped rows.")
            
    items = defaultdict(lambda: {"name": "", "total": 0, "wh": defaultdict(float)})
    for i_code, i_name, w_code, net_qty in results:
        code_str = str(w_code)
        items[str(i_code)]["name"] = str(i_name)
        items[str(i_code)]["total"] += float(net_qty)
        items[str(i_code)]["wh"][code_str] += float(net_qty)
        
    cols = ["كود الصنف", "اسم الصنف", "الإجمالي"] + [wh_mapping[c] for c in wh_codes]
    rows = []
    for code, data in items.items():
        row = [code, data["name"], f"{data['total']:,.2f}"]
        for w_code in wh_codes:
            row.append(f"{data['wh'][w_code]:,.2f}")
        rows.append(tuple(row))
        
    rows.sort(key=lambda x: float(x[2].replace(',', '')), reverse=True)
    return cols, rows

def add_total_row(cols, rows, rpt_id=""):
    if not rows:
        return cols, rows
        
    totals = [0.0] * len(cols)
    is_numeric = [False] * len(cols)
    has_values = [False] * len(cols)
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        
        if any(x in col_name for x in ['كود', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'عنوان', 'ملاحظات', 'بيان', 'مستند', 'رمز', 'نسبة', 'اسم', 'حساب', 'رقم']):
            continue
        if col_name in ('الرصيد', 'balance'):
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
        if row and len(row) > 3 and str(row[3]).strip() in ("رصيد افتتاحي", "الرصيد الإفتتاحي"):
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

def get_date_range(year_str, period_type, period_val):
    try:
        yr = int(year_str)
    except:
        yr = datetime.now().year
        
    date_from = f"{yr}-01-01"
    date_to = f"{yr}-12-31"
    
    if period_type == "monthly" and period_val and period_val != "all":
        try:
            m = int(period_val)
            import calendar
            last_day = calendar.monthrange(yr, m)[1]
            date_from = f"{yr}-{m:02d}-01"
            date_to = f"{yr}-{m:02d}-{last_day:02d}"
        except:
            pass
    elif period_type == "quarterly" and period_val and period_val != "all":
        q_map = {
            "q1": (1, 3, 31), "1": (1, 3, 31),
            "q2": (4, 6, 30), "2": (4, 6, 30),
            "q3": (7, 9, 30), "3": (7, 9, 30),
            "q4": (10, 12, 31), "4": (10, 12, 31),
        }
        if period_val in q_map:
            sm, em, ed = q_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
    elif period_type == "semi_annual" and period_val and period_val != "all":
        h_map = {
            "h1": (1, 6, 30), "1": (1, 6, 30),
            "h2": (7, 12, 31), "2": (7, 12, 31),
        }
        if period_val in h_map:
            sm, em, ed = h_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
            
    return date_from, date_to

def run_sales_collection_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    
    if grp_by == "rep":
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_col = "TO_CHAR(REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(b.C_CODE)"
        grp_col = "TO_CHAR(C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
    elif grp_by == "customer":
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(b.C_CODE)"
        grp_col = "TO_CHAR(C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "NVL(ns.grp_code, cs.grp_code)"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
    else: # default cc
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_col = "TO_CHAR(CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f"""
    WITH sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      -- Posted receipts with customer
      SELECT {grp_col} as grp_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Unposted receipts with customer
      SELECT {grp_col}, 0, 0, 0, 0, CR_AMT
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Network journals with customer
      SELECT {grp_col}, 0, CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Cash Sales (posted DOC_TYPE=4)
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Cash Returns (posted DOC_TYPE=5)
      SELECT {grp_col}, 0, 0, 0, CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    )
    SELECT NVL(ns.grp_code, cs.grp_code) AS item_code,
           {name_expr} AS item_name,
           NVL(SUM(ns.net_sales), 0) AS net_sales,
           NVL(SUM(cs.total_collection), 0) AS total_col
    FROM net_sales_summary ns
    FULL OUTER JOIN col_summary cs ON ns.grp_code = cs.grp_code
    {join_table}
    WHERE NVL(ns.grp_code, cs.grp_code) IS NOT NULL
    GROUP BY NVL(ns.grp_code, cs.grp_code)
    HAVING NVL(SUM(ns.net_sales), 0) <> 0 OR NVL(SUM(cs.total_collection), 0) <> 0
    ORDER BY NVL(ns.grp_code, cs.grp_code)
    """
    
    cols = [code_label, name_label, "صافي المبيعات", "المبيعات شامل الضريبة", "إجمالي التحصيل", "الفرق (المبيعات - التحصيل)", "نسبة التحصيل", "الهدف"]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"date_from": date_from, "date_to": date_to})
            for c_code, c_name, ns, col in cur.fetchall():
                ns_val = float(ns or 0.0)
                ns_vat_val = ns_val * 1.15
                col_val = float(col or 0.0)
                diff = ns_val - col_val
                ratio_str = f"{(col_val / ns_val * 100):.1f}%" if ns_val > 0 else "0.0%"
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ns_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff:,.2f}",
                    ratio_str,
                    target_str
                ))
                
    return cols, rows

def run_debt_movement_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_col_debt = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_col = "TO_CHAR(p.C_CODE)"
        grp_col_debt = "TO_CHAR(NVL(p.C_CODE, p.C_V_CODE))"
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(p.C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
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
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
        grp_col_debt = grp_col
    else: # default cc
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_col_debt = grp_col
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col_debt}
    ),
    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
          AND (p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1)
        GROUP BY {grp_col_debt}
    ),
    sales_base AS (
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
      SELECT grp_code FROM open_debt
      UNION
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
      UNION
      SELECT grp_code FROM close_debt
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col,
           NVL(SUM(cd.close_bal), 0) as close_bal
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    LEFT JOIN close_debt cd ON cd.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    """

    cols = [
        code_label,
        name_label,
        "المديونية الافتتاحية",
        "صافي المبيعات شامل الضريبة",
        "إجمالي التحصيل",
        "الفرق (المبيعات - التحصيل)",
        "نسبة التحصيل",
        "المديونية النهائية",
        "إجمالي المبيعات بدون الضريبة",
        "الهدف",
        "الفرق (الهدف - المبيعات)"
    ]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"date_from": date_from, "date_to": date_to})
            for c_code, c_name, open_b, ns_vat, ns_no_vat, col, close_b in cur.fetchall():
                ob_val = float(open_b or 0.0)
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                closing_val = float(close_b or 0.0)
                
                total_due = ob_val + ns_vat_val
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
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff_sales_col:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    target_str,
                    f"{diff_target_sales:,.2f}" if target_val > 0 else ""
                ))
                
    return cols, rows

def run_net_debt_movement_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    exclude_suppliers = args.get("exclude_suppliers", "1")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_col_debt = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_col = "TO_CHAR(p.C_CODE)"
        grp_col_debt = "TO_CHAR(NVL(p.C_CODE, p.C_V_CODE))"
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(p.C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
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
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
        grp_col_debt = grp_col
    else: # default cc
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_col_debt = grp_col
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"


    supplier_filter = "AND p.C_CODE IS NOT NULL AND TO_CHAR(p.A_CODE) LIKE '121%'" if exclude_suppliers == "1" else "AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)"
    
    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 {supplier_filter}

          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col_debt}
    ),
    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 {supplier_filter}
          AND (p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1)
        GROUP BY {grp_col_debt}
    ),
    sales_base AS (
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
      SELECT grp_code FROM open_debt
      UNION
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
      UNION
      SELECT grp_code FROM close_debt
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col,
           NVL(SUM(cd.close_bal), 0) as close_bal
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    LEFT JOIN close_debt cd ON cd.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    """

    cols = [
        code_label,
        name_label,
        "المديونية الافتتاحية",
        "صافي المبيعات شامل الضريبة",
        "إجمالي التحصيل",
        "نسبة التحصيل",
        "المديونية النهائية",
        "إجمالي المبيعات بدون الضريبة",
        "الهدف"
    ]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"date_from": date_from, "date_to": date_to})
            for c_code, c_name, open_b, ns_vat, ns_no_vat, col, close_b in cur.fetchall():
                ob_val = float(open_b or 0.0)
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                closing_val = float(close_b or 0.0)
                
                total_due = ob_val + ns_vat_val
                if total_due > 0:
                    col_ratio = (col_val / total_due) * 100
                else:
                    col_ratio = 0.0
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    target_str
                ))
                
    return cols, rows


def run_sql_report(rpt, args):
    sql = rpt["sql"]
    binds = {}
    for p in rpt["params"]:
        pname = p["name"]
        raw = args.get(pname, p.get("default", ""))
        val = str(raw).split(" - ")[0].strip() if raw else ""
        if p.get("type") in ("date", "month"):
            if not val:
                if callable(p.get("get_default")):
                    val = p["get_default"]()
                elif p.get("default"):
                    val = p["default"]
                else:
                    val = get_default_date_from() if "from" in pname else get_default_date_to()
        binds[pname] = val
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, binds)
            cols = [d[0] for d in cur.description] if cur.description else []
            rows = cur.fetchall()
            sort_col = args.get("sort_col")
            sort_dir = args.get("sort_dir", "desc")
            if sort_col and sort_col in cols and rows:
                col_idx = cols.index(sort_col)
                def parse_sort_val(r):
                    v = r[col_idx]
                    if v is None: return float('-inf') if sort_dir == 'asc' else float('inf')
                    if isinstance(v, (int, float)): return v
                    if isinstance(v, str):
                        try: return float(v.replace(',', ''))
                        except: return v
                    return str(v)
                rows.sort(key=parse_sort_val, reverse=(sort_dir == 'desc'))
            return cols, rows

def run_report(rpt, args):
    if "fn" in rpt:
        func = globals().get(rpt["fn"])
        if func:
            cols, rows = func(rpt, args)
            return add_total_row(cols, rows, rpt.get('id', ''))
    if not rpt.get("sql"):
        return [], []
    cols, rows = run_sql_report(rpt, args)
    return add_total_row(cols, rows, rpt.get('id', ''))

def jv_options():
    global _JV_CACHE
    if _JV_CACHE is not None:
        return _JV_CACHE
    opts = [["","الكل"]]
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""SELECT p.JV_TYPE, MAX(j.JV_NAME) nm
                    FROM IAS20261.IAS_POST_DTL p
                    LEFT JOIN IAS20261.JV_TYPES j ON j.JV_TYPE=p.JV_TYPE
                    WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
                    GROUP BY p.JV_TYPE ORDER BY COUNT(*) DESC""")
                for t, nm in cur.fetchall():
                    if t is None: continue
                    code = str(int(t))
                    label = nm or ("بدون نوع" if int(t)==0 else "نوع "+code)
                    opts.append([code, label])
        _JV_CACHE = opts
        return _JV_CACHE
    except Exception:
        return [["","الكل"],["1","قيد يومية"],["2","قيود الشبكة"],["4","قيود دائنون"],["9","قيد ضريبي"],["11","رصيد افتتاحي للعملاء"],["0","بدون نوع"]]

_LK_CACHE = {}
def lookups(name):
    if name in _LK_CACHE:
        return _LK_CACHE[name]
    q = {
      "rep_code": "SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN WHERE REPRS_CODE IS NOT NULL ORDER BY REPRS_A_NAME",
      "c_code":   "SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER WHERE NVL(INACTIVE,0)=0 AND C_CODE IS NOT NULL ORDER BY C_A_NAME",
      "v_code":   "SELECT V_CODE, MAX(V_NAME) FROM IAS20261.IAS_PI_BILL_MST WHERE V_CODE IS NOT NULL GROUP BY V_CODE ORDER BY MAX(V_NAME)",
      "i_code":   "SELECT I_CODE, I_NAME FROM IAS20261.IAS_ITM_MST WHERE I_CODE IS NOT NULL ORDER BY I_NAME",
      "a_code":   "SELECT A_CODE, A_NAME FROM IAS20261.ACCOUNT WHERE A_CODE IS NOT NULL ORDER BY A_CODE",
    }.get(name)
    if not q:
        return []
    out = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(q)
                for code, nm in cur.fetchall():
                    if code is None:
                        continue
                    out.append(("%s - %s" % (str(code).strip(), (nm or "").strip())).strip(" -"))
        _LK_CACHE[name] = out
        return out
    except Exception:
        return []

STYLE = """<style>

/* Hide scrollbars completely while keeping scroll functionality */
::-webkit-scrollbar { display: none; }
* { -ms-overflow-style: none; scrollbar-width: none; }
.quick-dates { display: flex; gap: 12px; flex-wrap: wrap; margin-top: -12px; margin-bottom: -8px; align-items: center; justify-content: center; }
.quick-dates .btn-sm { background: #ffffff; border: 2px solid #e2e8f0; color: var(--ink-dark); padding: 10px 20px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
.quick-dates .btn-sm:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.15), 0 4px 6px -2px rgba(79, 70, 229, 0.05); background: #fefeff; }
.quick-dates .btn-sm:active, .quick-dates .btn-sm.active { background: var(--primary); border-color: var(--primary); color: #ffffff; transform: translateY(-1px); box-shadow: 0 6px 12px -2px rgba(79, 70, 229, 0.4); }
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');
:root {
  --bg: #f4f5f8;
  --sb-bg: #ffffff;
  --card-bg: #ffffff;
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --ink: #64748b;
  --ink-dark: #1e293b;
  --line: #f1f5f9;
  --sh: 0 10px 40px rgba(0,0,0,0.04);
}
body { background: var(--bg); color: var(--ink); font-family: 'Cairo', 'Inter', sans-serif; direction: rtl; margin:0; padding:0; box-sizing:border-box; }
* { box-sizing: border-box; margin:0; padding:0; }
a { text-decoration: none; }
.card { background: var(--card-bg); border-radius: 20px; padding: 24px; box-shadow: var(--sh); }
.app { display: flex; min-height: 100vh; padding: 20px; gap: 24px; }
.sb { width: 260px; background: var(--sb-bg); border-radius: 24px; display: flex; flex-direction: column; padding: 30px 20px; flex-shrink: 0; box-shadow: var(--sh); position: sticky; top: 20px; max-height: calc(100vh - 40px); overflow-y: auto; }
.brand { display: flex; align-items: center; gap: 12px; font-size: 24px; font-weight: 800; color: var(--ink-dark); margin-bottom: 40px; }
.brand svg { width: 32px; height: 32px; fill: var(--primary); }
.menu-lbl { font-size: 11px; font-weight: 700; color: #94a3b8; margin: 20px 10px 10px; letter-spacing: 1px; }
.sb a { display: flex; align-items: center; gap: 14px; padding: 14px 20px; border-radius: 16px; color: var(--ink); font-weight: 600; font-size: 15px; margin-bottom: 8px; transition: all 0.3s; }
.sb a:hover { background: #f8fafc; color: var(--ink-dark); }
.sb a.on { background: var(--primary); color: #fff; box-shadow: 0 10px 20px rgba(79, 70, 229, 0.25); }
.sb svg { width: 22px; height: 22px; stroke: currentColor; fill: none; stroke-width: 2; }
.sb a.on svg { stroke: #fff; }

.main { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.top { display: flex; align-items: center; padding: 10px 0 30px; gap: 15px; }
.logo { display:none; }
.ttl { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.wrap { display: flex; flex-direction: column; gap: 24px; }

.pills { display: flex; gap: 12px; flex-wrap: wrap; }
.pill { background: var(--card-bg); border-radius: 12px; padding: 12px 24px; font-size: 14px; font-weight: 600; color: var(--ink); box-shadow: var(--sh); transition: 0.3s; }
.pill:hover { transform: translateY(-2px); color: var(--primary); }
.pill.on { background: var(--primary); color: #fff; box-shadow: 0 10px 20px rgba(79, 70, 229, 0.25); }

.filters { background: var(--card-bg); border-radius: 20px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); margin-bottom: 0; }
.filters label { display: block; font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 8px; }
.filters input, .filters select { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 14px; font-weight: 500; color: var(--ink-dark); background: #f8fafc; outline: none; transition: 0.3s; }
.filters input:focus, .filters select:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1); }
.filters .btn { background: var(--primary); color: #fff; border: 0; padding: 14px 24px; border-radius: 12px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.3s; height: 46px; }
.filters .btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2); }

.tw { overflow-x: auto; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }
table { border-collapse: collapse; width: 100%;  }
thead th { position: sticky; top: 0; z-index: 10; background: #ffffff; white-space: nowrap; color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line);  }
tbody td { white-space: nowrap; padding: 6px 12px; border-bottom: 1px solid var(--line); font-size: 13px; font-weight: 500; color: var(--ink-dark);  transition: 0.2s; }
tbody tr:hover td { background: #f8fafc; }
tr.tot-row td { position: sticky; top: 35px; z-index: 9; background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }
tr.prof-row1 td { background: #dcfce7 !important; color: #15803d !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 1.5px solid #bbf7d0 !important; }
tr.prof-row2 td { background: #dbeafe !important; color: #1e40af !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #93c5fd !important; }

.rhead { display: flex; align-items: center; gap: 16px; margin-bottom: 10px; }
.rhead h1 { margin: 0; flex: 1; font-size: 20px; color: var(--ink-dark); font-weight: 800; border:0; padding:0; }
.rhead h1::before { display: none; }
.cnt { color: var(--ink); font-size: 13px; font-weight: 600; margin-bottom: 10px; }
.exps { display: flex; gap: 10px; }
.exp { border: 0; border-radius: 10px; padding: 10px 20px; font-weight: 600; font-size: 13px; color: #fff; cursor: pointer; transition: 0.3s; }
.exp:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.exp.xl { background: #10b981; } .exp.pf { background: #ef4444; }
.err { background: #fef2f2; color: #b91c1c; padding: 16px; border-radius: 12px; font-weight: 600; }

.gdwrap { display: flex; flex-direction: column; gap: 24px; }
.gkpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.gk { background: var(--card-bg); border-radius: 24px; padding: 24px; display: flex; flex-direction: column; gap: 16px; box-shadow: var(--sh); position: relative; overflow: hidden; }
.gk:nth-child(1) { background: var(--primary); color: #fff; }
.gk:nth-child(1) .gl { color: rgba(255,255,255,0.8); }
.gk:nth-child(1) .gv { color: #fff; }
.gk .gic { width: 48px; height: 48px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 20px; }
.gk:nth-child(1) .gic { background: rgba(255,255,255,0.2); }
.gk:nth-child(2) .gic { background: #dcfce7; color: #16a34a; }
.gk:nth-child(3) .gic { background: #ffedd5; color: #f97316; }
.gk:nth-child(4) .gic { background: #e0e7ff; color: #4f46e5; }
.gk:nth-child(5) .gic { background: #d1fae5; color: #059669; }
.gk:nth-child(6) .gic { background: #fee2e2; color: #dc2626; }
.gk:nth-child(7) .gic { background: #e0f2fe; color: #0284c7; }
.gk:nth-child(8) .gic { background: #fef3c7; color: #d97706; }
.gk .gl { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
.gk .gv { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.gcharts { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.gc { background: var(--card-bg); border-radius: 24px; padding: 24px; box-shadow: var(--sh); }
.gc h3 { font-size: 16px; font-weight: 700; margin: 0 0 20px; color: var(--ink-dark); }
.app-logo { color:#4f46e5; font-weight:900; font-size:26px; letter-spacing:-1px; }
.mobile-dropdown { display: none; }
.mobile-dropdown select { width: 100%; padding: 12px 16px; border: 2px solid var(--primary); border-radius: 12px; font-family: inherit; font-size: 15px; font-weight: 700; color: var(--primary); background: #f8fafc; outline: none; text-align: center; cursor: pointer; margin-bottom: 15px; box-shadow: var(--sh); }

@media(max-width:900px){
  .app { flex-direction:column; padding:10px; }
  .sb { width:100%; flex-direction:row; padding:10px; overflow-x:auto; border-radius:16px; gap:8px; align-items:flex-start; -webkit-overflow-scrolling: touch; }
  .brand { margin:0; padding-right:10px; align-self: center; }
  .brand span { display:none; }
  .menu-lbl { display:none; }
  .sb a { margin:0; padding:8px 10px; flex-shrink: 0; flex-direction: column; justify-content: center; gap: 5px; min-width: 65px; text-align: center; }
  .sb a span { display: block; font-size: 11px;  line-height: 1.2; }
  
  .top { flex-direction: column; align-items: center; gap: 8px; padding-bottom: 15px; text-align: center; }
  .app-logo { font-size: 20px; }
  .ttl { font-size: 18px; }
  
  .pills { display: none; }
  .mobile-dropdown { display: block; }
  
  .rhead { flex-direction: column; align-items: center; gap: 12px; text-align: center; }
  .exps { width: 100%; justify-content: center; gap: 15px; }
  .exp { flex: 1; text-align: center; padding: 12px; font-size: 14px; }
  
  .filters { grid-template-columns: 1fr; gap: 15px; padding: 16px; }
  .filters .btn { height: 50px; font-size: 15px; }
  
  .gkpis { grid-template-columns: repeat(2,1fr); gap: 15px; }
  .gk { padding: 16px; }
  .gk .gv { font-size: 20px; }
  .gcharts { grid-template-columns: 1fr; }
}

</style>"""

LOGO = '<div class="app-logo">تقارير الأونكس الحديثة</div>'

PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>تقارير SREEN</title>""" + STYLE + """</head><body>
<div class="app">
 <aside class="sb">
   <div class="brand"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span>Onyx Deck</span></div>
   <div class="menu-lbl">القائمة الرئيسية</div>
   
   {% for t in tabs %}{% if t.id not in hidden_tabs %}
     <a class="{{ 'on' if t.id==cur_tab else '' }}" href="/?tab={{t.id}}">
       <svg viewBox="0 0 24 24"><path d="{{t.icon}}"/></svg><span>{{ t.title }}</span></a>
   {% endif %}{% endfor %}
   <div class="menu-lbl" style="margin-top:auto">أدوات</div>
   <a href="/globals"><svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg><span>المتغيرات العامة</span></a>
   <a href="/settings"><svg viewBox="0 0 24 24"><path d="M4 6h9M4 12h5M4 18h7"/><circle cx="17" cy="6" r="2.3"/><circle cx="13" cy="12" r="2.3"/><circle cx="15" cy="18" r="2.3"/></svg><span>الإعدادات</span></a>
 </aside>
 <div class="main">
   <div class="wrap">
     {% if dash %}
     <div class="rhead"><h1>لوحة القيادة</h1></div>
     <form class="filters" method="get" action="/">
       <input type="hidden" name="tab" value="{{cur_tab}}"><input type="hidden" name="report" value="overview">
       <div><label>من تاريخ</label><input type="date" name="date_from" value="{{ binds.get('date_from') or '2026-01-01' }}"></div>
       <div><label>إلى تاريخ</label><input type="date" name="date_to" value="{{ binds.get('date_to') or '2026-12-31' }}"></div>
       <div><button class="btn" type="submit">تحديث</button></div>
     </form>
     {% if error %}<div class="err">خطأ: {{error}}</div>{% else %}
     <div class="gdwrap">
       <div class="gkpis">
         <div class="gk"><div class="gic" style="background:#dbeafe">💵</div><div><div class="gl">إجمالي المبيعات</div><div class="gv">{{ "{:,.0f}".format(dash.sales) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#dcfce7">💰</div><div><div class="gl">إجمالي التحصيل</div><div class="gv">{{ "{:,.0f}".format(dash.collect) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#ffedd5">🛒</div><div><div class="gl">إجمالي المشتريات</div><div class="gv">{{ "{:,.0f}".format(dash.purch) }}</div></div></div>
         {% if not hide_profit %}<div class="gk"><div class="gic" style="background:#ede9fe">📈</div><div><div class="gl">مجمل الربح</div><div class="gv">{{ "{:,.0f}".format(dash.gross) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#d1fae5">✅</div><div><div class="gl">صافي الربح</div><div class="gv">{{ "{:,.0f}".format(dash.netprofit) }}</div></div></div>{% endif %}
         <div class="gk"><div class="gic" style="background:#fee2e2">🧾</div><div><div class="gl">الذمم المدينة</div><div class="gv">{{ "{:,.0f}".format(dash.recv) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#e0f2fe">📦</div><div><div class="gl">قيمة المخزون</div><div class="gv">{{ "{:,.0f}".format(dash.invval) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#fef3c7">🏛️</div><div><div class="gl">صافي الضريبة</div><div class="gv">{{ "{:,.0f}".format(dash.vat) }}</div></div></div>
       </div>
       <div class="gcharts" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
          <div class="gc" style="grid-column: 1 / -1;"><h3>المبيعات والتحصيل شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c1"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 مناديب</h3><div style="position:relative;height:250px;width:100%"><canvas id="c2"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 أصناف</h3><div style="position:relative;height:250px;width:100%"><canvas id="c3"></canvas></div></div>
          <div class="gc" style="grid-column: 1 / -1;"><h3>المشتريات شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c4"></canvas></div></div>
        </div>
     </div>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: { backgroundColor: '#1e293b', padding: 14, titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' }, bodyFont: { size: 14, family: "'Cairo', sans-serif" }, cornerRadius: 10, displayColors: true, boxPadding: 6 }
         }
       };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32}
           ]
         },
         options: {
           ...commonOptions,
           plugins: { ...commonOptions.plugins, legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, font: { family: "'Cairo'", size: 13, weight: 'bold' } } } },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });

       // C2: Doughnut (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"doughnut",
         data:{
           labels:D.rep_labels.slice(0,5),
           datasets:[{data:D.rep_vals.slice(0,5), backgroundColor:["#4f46e5", "#38bdf8", "#10b981", "#f59e0b", "#8b5cf6"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C3: Doughnut (Items)
       new Chart(document.getElementById("c3"),{
         type:"doughnut",
         data:{
           labels:D.itm_labels.slice(0,5),
           datasets:[{data:D.itm_vals.slice(0,5), backgroundColor:["#f43f5e", "#d946ef", "#0ea5e9", "#14b8a6", "#eab308"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(16, 185, 129, 0.4)');
       grad4.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات", data:D.mpurch, borderColor:"#10b981", borderWidth: 3, backgroundColor: grad4, fill:true, tension:0.4, pointRadius: 0, pointHoverRadius: 6, pointBackgroundColor: "#fff", pointBorderColor: "#10b981", pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });
     });
     </script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: {
             backgroundColor: '#1e293b',
             padding: 14,
             titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' },
             bodyFont: { size: 14, family: "'Cairo', sans-serif" },
             cornerRadius: 10,
             displayColors: true,
             boxPadding: 6
           }
         },
         scales: {
           x: { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' } } },
           y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } }
         }
       };

       const horizontalOptions = JSON.parse(JSON.stringify(commonOptions));
       horizontalOptions.indexAxis = "y";
       horizontalOptions.scales.x = { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' } } };
       horizontalOptions.scales.y = { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32, borderSkipped: false},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32, borderSkipped: false}
           ]
         },
         options: {
           ...commonOptions,
           plugins: {
             ...commonOptions.plugins,
             legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, padding: 20, font: { family: "'Cairo'", size: 13, weight: 'bold' } } }
           }
         }
       });

       // C2: Horizontal Bar (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"bar",
         data:{
           labels:D.rep_labels,
           datasets:[{label: "مبيعات", data:D.rep_vals, backgroundColor:"#8b5cf6", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C3: Horizontal Bar (Items)
       new Chart(document.getElementById("c3"),{
         type:"bar",
         data:{
           labels:D.itm_labels,
           datasets:[{label: "مبيعات", data:D.itm_vals, backgroundColor:"#10b981", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(249, 115, 22, 0.4)');
       grad4.addColorStop(1, 'rgba(249, 115, 22, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات",
             data:D.mpurch,
             borderColor:"#f97316",
             borderWidth: 3,
             backgroundColor: grad4,
             fill:true,
             tension:0.4,
             pointRadius: 0,
             pointHoverRadius: 6,
             pointBackgroundColor: "#fff",
             pointBorderColor: "#f97316",
             pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false }
         }
       });
     });
     </script>
     {% endif %}
     {% else %}
     <div class="pills">
       {% for r in tab.reports %}{% if (cur_tab ~ '/' ~ r.id) not in hidden_reports %}
         <a class="pill {{ 'on' if r.id==rpt.id else '' }}" href="/?tab={{cur_tab}}&report={{r.id}}">{{ r.title }}</a>
       {% endif %}{% endfor %}
     </div>
     <div class="mobile-dropdown">
       <select onchange="window.location.href=this.value">
         {% for r in tab.reports %}{% if (cur_tab ~ '/' ~ r.id) not in hidden_reports %}
           <option value="/?tab={{cur_tab}}&report={{r.id}}" {{ 'selected' if r.id==rpt.id else '' }}>{{ r.title }}</option>
         {% endif %}{% endfor %}
       </select>
     </div>
     <div class="rhead">
  <h1>{{ rpt.title }}</h1>
  <div class="exps">
    <a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a>
    {% if rpt.id == 'collection_adopted' %}
      <select id="pdfModel" style="padding:4px 8px; border:1px solid #cbd5e1; border-radius:4px; margin-left:4px; font-family:inherit; font-size:13px;">
        <option value="1">PDF (النموذج الافتراضي)</option>
        <option value="2">PDF (نموذج 2)</option>
      </select>
      <button class="exp pf" style="border:none; cursor:pointer;" onclick="window.open('/print?{{qs|safe}}&model=' + document.getElementById('pdfModel').value, '_blank')">طباعة</button>
    {% else %}
      <a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a>
    {% endif %}
  </div>
</div>
     {% if rpt.params %}
     <form class="filters" method="get" action="/">
       <input type="hidden" name="tab" value="{{cur_tab}}"><input type="hidden" name="report" value="{{rpt.id}}">

       {% for p in rpt.params %}
         <div><label>{{p.label}}</label>
         {% if p.type=='select' %}
           <select name="{{p.name}}">{% for o in p.options %}<option value="{{o[0]}}" {{'selected' if binds.get(p.name)==o[0] else ''}}>{{o[1]}}</option>{% endfor %}</select>
         {% elif p.get('_list') %}
           <input type="text" name="{{p.name}}" list="dl_{{p.name}}" autocomplete="off" placeholder="ابحث بالكود أو الاسم" value="{{ binds.get(p.name) if binds.get(p.name) is not none else '' }}">
           <datalist id="dl_{{p.name}}">{% for o in p.get('_list') %}<option value="{{o}}"></option>{% endfor %}</datalist>
         {% else %}
           <input type="{{p.type}}" name="{{p.name}}" value="{{ binds.get(p.name) if binds.get(p.name) is not none else '' }}">
         {% endif %}
         </div>
       {% endfor %}
       <div><button class="btn" type="submit">عرض التقرير</button></div>
     </form>
      <script>
         document.addEventListener("DOMContentLoaded", function() {
             const pt = document.querySelector('select[name="period_type"]');
             const pv = document.querySelector('select[name="period_val"]');
             if(pt && pv) {
                 const allOpts = Array.from(pv.options).map(o => ({val: o.value, text: o.text}));
                 function updatePV() {
                     const t = pt.value;
                     const curVal = pv.value;
                     pv.innerHTML = '';
                     allOpts.forEach(o => {
                         let show = false;
                         let txt = o.text;
                         if(o.val === 'all') {
                             show = true;
                         } else {
                             const valNum = parseInt(o.val);
                             const parts = txt.split(' / ');
                             if (t === 'monthly' && valNum >= 1 && valNum <= 12) {
                                 show = true;
                                 txt = parts[0];
                             } else if (t === 'quarterly' && valNum >= 1 && valNum <= 4) {
                                 show = true;
                                 txt = parts[1] || txt;
                             } else if (t === 'semi_annual' && valNum >= 1 && valNum <= 2) {
                                 show = true;
                                 txt = parts[2] || txt;
                             }
                         }
                         if(show) {
                             const opt = document.createElement('option');
                             opt.value = o.val;
                             opt.text = txt;
                             pv.appendChild(opt);
                         }
                     });
                     if(!Array.from(pv.options).find(o => o.value === curVal)) {
                         pv.value = 'all';
                     } else {
                         pv.value = curVal;
                     }
                 }
                 pt.addEventListener('change', updatePV);
                 updatePV();
             }
         });
      </script>
     {% endif %}
     {% if rpt.params and 'date_from' in rpt.params|map(attribute='name') %}
     <div class="quick-dates">
         <button type="button" class="btn-sm" onclick="setDates('today', this)">اليوم</button>
         <button type="button" class="btn-sm" onclick="setDates('this_week', this)">هذا الأسبوع</button>
         <button type="button" class="btn-sm" onclick="setDates('this_month', this)">هذا الشهر</button>
         <button type="button" class="btn-sm" onclick="setDates('last_month', this)">الشهر السابق</button>
         <button type="button" class="btn-sm" onclick="setDates('this_year', this)">هذه السنة</button>
         <button type="button" class="btn-sm" onclick="setDates('last_year', this)">السنة السابقة</button>
     </div>
     <script>
         function setDates(range, btn) {
             document.querySelectorAll('.quick-dates .btn-sm').forEach(b => b.classList.remove('active'));
             if(btn) btn.classList.add('active');
             
             const dFrom = document.querySelector('input[name="date_from"]');
             const dTo = document.querySelector('input[name="date_to"]');
             if(!dFrom || !dTo) return;
             
             const today = new Date();
             let from = new Date();
             let to = new Date();

             if(range === 'today') {
                 // keep today
             } else if (range === 'this_week') {
                 const day = today.getDay();
                 from.setDate(today.getDate() - day);
             } else if (range === 'this_month') {
                 from = new Date(today.getFullYear(), today.getMonth(), 1);
                 to = new Date(today.getFullYear(), today.getMonth() + 1, 0);
             } else if (range === 'last_month') {
                 from = new Date(today.getFullYear(), today.getMonth() - 1, 1);
                 to = new Date(today.getFullYear(), today.getMonth(), 0);
             } else if (range === 'this_year') {
                 from = new Date(today.getFullYear(), 0, 1);
                 to = new Date(today.getFullYear(), 11, 31);
             } else if (range === 'last_year') {
                 from = new Date(today.getFullYear() - 1, 0, 1);
                 to = new Date(today.getFullYear() - 1, 11, 31);
             }

             const fmt = d => {
                 const m = String(d.getMonth() + 1).padStart(2, '0');
                 const day = String(d.getDate()).padStart(2, '0');
                 return `${d.getFullYear()}-${m}-${day}`;
             };
             
             dFrom.value = fmt(from);
             dTo.value = fmt(to);
             
             const form = dFrom.closest('form');
             if(form) form.submit();
         }
     </script>
     {% endif %}
     
     {% if error %}<div class="err">خطأ: {{error}}</div>
     {% else %}
       <div class="tw"><table><thead><tr>{% for c in cols %}<th onclick="sortTable({{loop.index0}})" style="cursor:pointer" title="اضغط للترتيب">{{c}} <span style="font-size:10px; opacity:0.5; margin-right:4px">↕</span></th>{% endfor %}</tr></thead>
       <tbody>{% for row in rows %}{% set r0 = (row[0]|string).strip() %}{% set r1 = (row[1]|string).strip() %}{% set cls = '' %}{% if r0=='الإجمالي' or r1=='الإجمالي' %}{% set cls = 'tot-row' %}{% elif 'رصيد الفترة صافي' in r1 %}{% set cls = 'prof-row1' %}{% elif 'الرصيد النهائي صافي' in r1 %}{% set cls = 'prof-row2' %}{% endif %}<tr class="{{ cls }}">{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody></table></div>
     {% endif %}
     {% endif %}
   </div>
 </div>
 <script>
 document.addEventListener('DOMContentLoaded', function() {
   var activeTab = document.querySelector('.sb a.on');
   if (activeTab) { activeTab.scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'center' }); }
   var activePill = document.querySelector('.pills a.on');
   if (activePill) { activePill.scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'center' }); }
 });

    function sortTable(colIndex) {
      const tbody = document.querySelector('tbody');
      if (!tbody) return;
      
      const rows = Array.from(tbody.querySelectorAll('tr'));
      if (rows.length <= 1) return; 
      
      const totalRow = rows.shift(); 
      
      let dir = tbody.getAttribute('data-sort-dir') === 'asc' ? 'desc' : 'asc';
      tbody.setAttribute('data-sort-dir', dir);
      
      rows.sort((a, b) => {
        let valA = a.children[colIndex].textContent.trim();
        let valB = b.children[colIndex].textContent.trim();
        
        let numA = parseFloat(valA.replace(/,/g, ''));
        let numB = parseFloat(valB.replace(/,/g, ''));
        
        let isNumA = !isNaN(numA) && valA !== '';
        let isNumB = !isNaN(numB) && valB !== '';
        
        let cmp = 0;
        if (isNumA && isNumB) {
          cmp = numA - numB;
        } else {
          cmp = valA.localeCompare(valB, 'ar');
        }
        
        return dir === 'asc' ? cmp : -cmp;
      });
      
      tbody.innerHTML = '';
      tbody.appendChild(totalRow);
      rows.forEach(r => tbody.appendChild(r));
      
      // Update PDF and Excel export links
      let exps = document.querySelectorAll('.exp');
      let colName = document.querySelectorAll('thead th')[colIndex].textContent.replace(' ↕', '').trim();
      exps.forEach(a => {
        let url = new URL(a.href, window.location.origin);
        url.searchParams.set('sort_col', colName);
        url.searchParams.set('sort_dir', dir);
        a.href = url.pathname + url.search;
      });
    }
 </script>
</body></html>"""

@app.route("/")
def index():
    hidden_tabs, hidden_reports = load_hidden()
    _vis = [t for t in TABS if t["id"] not in hidden_tabs] or TABS
    cur_tab = request.args.get("tab", _vis[0]["id"])
    rid = request.args.get("report", "")
    tab, rpt = find_report(cur_tab, rid)
    cur_tab = tab["id"]
    for _p in rpt["params"]:
        if _p.get("dynamic") == "jv": _p["options"] = jv_options()
        if _p["name"] in ("rep_code","c_code","v_code","i_code","a_code"): _p["_list"] = lookups(_p["name"])
    display = {p["name"]: request.args.get(p["name"]) or (p["get_default"]() if "get_default" in p else p.get("default","")) for p in rpt["params"]}
    qsp = {"tab": cur_tab, "report": rpt["id"]}
    for p in rpt["params"]: qsp[p["name"]] = request.args.get(p["name"]) or (p["get_default"]() if "get_default" in p else p.get("default",""))
    qs = urlencode(qsp)
    error = None; cols=[]; rows=[]; dash=None
    if tab.get("dash"):
        try:
            dash = compute_dash(request.args.get("date_from","2026-01-01"), request.args.get("date_to","2026-12-31"))
        except Exception as e:
            error = str(e)
    else:
        try:
            cols, rows = run_report(rpt, request.args)
        except Exception as e:
            error = str(e)
    return render_template_string(PAGE, tabs=TABS, tab=tab, cur_tab=cur_tab, rpt=rpt,
                                  binds=display, cols=cols, rows=rows, error=error, qs=qs, dash=dash, hidden_tabs=hidden_tabs, hidden_reports=hidden_reports, hide_profit=load_hide_profit())

PRINT_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<style>
@page { size: A4 landscape; margin: 10mm; }
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Cairo','Inter',Tahoma,sans-serif;direction:rtl;color:#1e293b;margin:0;font-size:11px;}
.hd{display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #4f46e5;padding-bottom:10px;margin-bottom:15px}
.hd h1{font-size:18px;margin:0;color:#0f172a;font-weight:800}
.hd .dt{font-size:11px;color:#64748b;margin-top:6px;font-weight:600}
.logo{height:35px}
.filt{font-size:11px;color:#475569;margin-bottom:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:8px 10px;font-weight:600}
.filt b{color:#4f46e5}
table{border-collapse:collapse;width:100%;table-layout:fixed;word-wrap:break-word;}
thead th{background:#4f46e5;color:#fff;padding:4px 4px;font-size:11px;text-align:right;border:1px solid #4338ca;font-weight:700}
tbody td{padding:3px 4px;font-size:11px;border:1px solid #e2e8f0;text-align:right;font-weight:500;color:#1e293b}
tbody tr:nth-child(even) td{background:#f8fafc}
tbody tr:first-child td{background:#eef2ff;font-weight:800;color:#3730a3;border-bottom:2px solid #a5b4fc} /* تمييز صف الإجمالي */
.ft{margin-top:20px;font-size:11px;color:#94a3b8;text-align:center;border-top:1px solid #e2e8f0;padding-top:10px;font-weight:600}

</style></head>
<body onload="setTimeout(function(){window.print()},250)">
<div class="hd">
  <h1 style="color:#4f46e5;font-weight:900;margin:0;font-size:26px">تقارير الأونكس الحديثة</h1>
  <div><h1>{{title}}</h1><div class="dt">تاريخ الطباعة: {{now}}</div></div>
</div>
{% if filt %}<div class="filt">الفلاتر — {% for f in filt %}<b>{{f[0]}}</b>: {{f[1]}}{% if not loop.last %} &nbsp;|&nbsp; {% endif %}{% endfor %}</div>{% endif %}
{% set hidden_cols = ["الخصم في الفاتورة", "إيداعات وتسويات (بدون عميل)"] %}
<table><thead><tr>{% for c in cols %}{% if c not in hidden_cols %}<th>{{c}}</th>{% endif %}{% endfor %}</tr></thead>
<tbody>{% for row in rows %}<tr>{% for cell in row %}{% if cols[loop.index0] not in hidden_cols %}<td>{{ '' if cell is none else cell }}</td>{% endif %}{% endfor %}</tr>{% endfor %}</tbody></table>
<div class="ft">لوحة تقارير SREEN — عدد الصفوف: {{rows|length}}</div>
</body></html>"""

@app.route("/export")
def export():
    tab, rpt = find_report(request.args.get("tab", TABS[0]["id"]), request.args.get("report",""))
    try:
        cols, rows = run_report(rpt, request.args)
    except Exception as e:
        return "خطأ: " + str(e), 500
    try:
        hidden_cols = ["الخصم في الفاتورة", "إيداعات وتسويات (بدون عميل)"]
        valid_indices = [i for i, col in enumerate(cols) if col not in hidden_cols]
        filtered_cols = [cols[i] for i in valid_indices]

        from openpyxl import Workbook
        from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
        from openpyxl.utils import get_column_letter
        wb = Workbook(); ws = wb.active; ws.title = "تقرير"
        ws.sheet_view.rightToLeft = True
        ws.append(filtered_cols)
        
        # تنسيق الرأس
        header_fill = PatternFill("solid", fgColor="4F46E5")
        header_font = Font(bold=True, color="FFFFFF")
        border = Border(left=Side(style='thin', color='E2E8F0'), 
                        right=Side(style='thin', color='E2E8F0'), 
                        top=Side(style='thin', color='E2E8F0'), 
                        bottom=Side(style='thin', color='E2E8F0'))
                        
        for cell in ws[1]:
            cell.font = header_font
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="right")
            cell.border = border
            
        # تنسيق صف الإجمالي (الصف الأول من البيانات وهو الصف الثاني في الإكسل)
        total_fill = PatternFill("solid", fgColor="EEF2FF")
        total_font = Font(bold=True, color="3730A3")
        
        for row_idx, r in enumerate(rows, start=2):
            filtered_r = [str(r[i]) if r[i] is not None else '' for i in valid_indices]
            ws.append(filtered_r)
            for cell_idx, cell in enumerate(ws[row_idx], start=1):
                cell.border = border
                cell.alignment = Alignment(horizontal="right")
                if row_idx == 2:  # صف الإجمالي
                    cell.fill = total_fill
                    cell.font = total_font

        for i in range(1, len(filtered_cols)+1):
            ws.column_dimensions[get_column_letter(i)].width = 22
            
        buf = io.BytesIO(); wb.save(buf); buf.seek(0)
        return Response(buf.getvalue(),
            mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            headers={"Content-Disposition": "attachment; filename=%s.xlsx" % rpt["id"]})
    except ImportError:
        import csv
        buf = io.StringIO()
        buf.write('\ufeff')
        writer = csv.writer(buf)
        writer.writerow(filtered_cols)
        for r in rows:
            filtered_r = [str(r[i]) if r[i] is not None else '' for i in valid_indices]
            writer.writerow(filtered_r)
        return Response(buf.getvalue().encode('utf-8'),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=%s.csv" % rpt["id"]})

@app.route("/print")
def printview():
    tab, rpt = find_report(request.args.get("tab", TABS[0]["id"]), request.args.get("report",""))
    try:
        cols, rows = run_report(rpt, request.args)
        model = request.args.get("model", "1")
        if model == "2" and rpt["id"] == "collection_adopted":
            new_cols = ["الرمز", "الاسم / الوصف", "إجمالي السندات", "قيود الشبكة المنفصلة", "صافي المبيعات النقدية", "الإجمالي النهائي"]
            new_rows = []
            for r in rows:
                def parse_num(v):
                    if not v: return 0.0
                    if isinstance(v, str):
                        try: return float(v.replace(',',''))
                        except: return 0.0
                    return float(v)
                
                tot_rcpt = parse_num(r[2]) + parse_num(r[3]) + parse_num(r[4])
                net_jrn = parse_num(r[6])
                net_cash = parse_num(r[7]) - parse_num(r[10])
                final_tot = tot_rcpt + net_jrn + net_cash
                
                fmt = lambda x: f"{x:,.2f}" if x != 0 else "0.00"
                new_rows.append((r[0], r[1], fmt(tot_rcpt), fmt(net_jrn), fmt(net_cash), fmt(final_tot)))
            
            cols = new_cols
            rows = new_rows

    except Exception as e:
        return "خطأ: " + str(e), 500
    filt = []
    for p in rpt["params"]:
        v = request.args.get(p["name"], p.get("default",""))
        if v not in ("", None): filt.append((p["label"], v))
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    title = rpt["title"] + (" (نموذج 2)" if request.args.get("model") == "2" else "")
    return render_template_string(PRINT_PAGE, title=title, cols=cols, rows=rows, filt=filt, now=now)

SETTINGS_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>الإعدادات</title>""" + STYLE + """</head><body>
<div class="app"><div class="main">
 <div class="wrap">
   <a class="back" href="/" style="color:#4f46e5;font-weight:700;display:inline-block;margin-bottom:10px">&#8594; رجوع للتقارير</a>
   {% if saved %}<div style="background:#e8f4ec;color:#1e7b34;padding:10px 14px;border-radius:8px;margin:6px 0 12px">تم حفظ الإعدادات</div>{% endif %}
   <h1>إظهار / إخفاء التبويبات والتقارير</h1>
   <p style="color:#6b7280;font-size:13px;margin-bottom:12px">ضع علامة على ما تريد إخفاءه من الواجهة، ثم احفظ.</p>
   <form method="post">
     <input type="hidden" name="action" value="save">
     <div class="card" style="margin-bottom:16px;border:2px solid #f59e0b;background:#fffbeb">
       <label style="font-weight:800;font-size:15px;color:#b45309"><input type="checkbox" name="hide_profit" {{ 'checked' if hide_profit else '' }}> 🔒 إخفاء كل ما يخص الربح من النظام</label>
       <div style="margin-top:6px;color:#92400e;font-size:12.5px">عند التفعيل يُخفى: تبويب «الربحية» بالكامل، بطاقتا «مجمل الربح» و«صافي الربح» في لوحة القيادة، وتقريرا «قائمة الدخل» و«مراكز التكلفة» في التبويب المالي.</div>
     </div>
     {% for t in tabs %}
       <div class="card" style="margin-bottom:12px">
         <label style="font-weight:700;font-size:15px"><input type="checkbox" name="tab_{{t.id}}" {{ 'checked' if t.id in hidden_tabs else '' }}> إخفاء التبويب كاملاً: {{t.title}}</label>
         <div style="margin-top:10px;padding-right:18px;display:flex;flex-wrap:wrap;gap:14px">
           {% for r in t.reports %}
             <label style="font-size:13px;color:#374151"><input type="checkbox" name="rep_{{t.id}}/{{r.id}}" {{ 'checked' if (t.id ~ '/' ~ r.id) in hidden_reports else '' }}> {{r.title}}</label>
           {% endfor %}
         </div>
       </div>
     {% endfor %}
     <button type="submit" style="background:#4f46e5;color:#fff;border:0;padding:12px 24px;border-radius:9px;font-weight:700;font-size:15px;cursor:pointer">حفظ الإعدادات</button>
   </form>
 </div>
</div></div></body></html>"""

GLOBALS_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>المتغيرات العامة</title>""" + STYLE + """
<style>
.tgt-table { width:100%; border-collapse:collapse; font-size:13px; }
.tgt-table th, .tgt-table td { border:1px solid #e2e8f0; padding:6px; text-align:center; }
.tgt-table th { background:#f8fafc; font-weight:700; color:#475569; position:sticky; top:0; }
.tgt-input { width:100%; min-width:70px; padding:4px; border:1px solid #cbd5e1; border-radius:4px; text-align:center; }
</style>
</head><body>
<div class="app"><div class="main">
 <div class="wrap">
   <a class="back" href="/" style="color:#4f46e5;font-weight:700;display:inline-block;margin-bottom:16px">&#8594; العودة للرئيسية</a>
   <div class="rhead">
     <h1>المتغيرات العامة (التارجت)</h1>
     {% if saved %}<div style="color:#10b981;font-weight:bold;margin-top:10px">تم الحفظ بنجاح!</div>{% endif %}
   </div>
   <form method="post" action="/globals">
     <div style="overflow-x:auto; max-height: 70vh; margin-bottom: 20px; border-radius: 8px; border: 1px solid #e2e8f0">
       <table class="tgt-table">
         <thead>
           <tr>
             <th style="min-width:150px">اسم المندوب</th>
             {% for m in range(1, 13) %}
             <th>شهر {{m}}</th>
             {% endfor %}
           </tr>
         </thead>
         <tbody>
           {% for rep in reps %}
           <tr>
             <td style="text-align:right">{{ rep.name }}</td>
             {% for m in range(1, 13) %}
             <td>
               <input type="number" class="tgt-input" 
                      name="target_{{rep.code}}_{{m}}" 
                      value="{{ targets.get(rep.code|string, {}).get(m|string, 1000000) }}">
             </td>
             {% endfor %}
           </tr>
           {% endfor %}
         </tbody>
       </table>
     </div>
     <button type="submit" style="background:#4f46e5;color:#fff;border:0;padding:12px 24px;border-radius:9px;font-weight:700;font-size:15px;cursor:pointer">حفظ المتغيرات</button>
   </form>
 </div>
</div></div></body></html>"""


PIN_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>رمز الدخول</title>""" + STYLE + """</head><body>
<div class="app"><div class="main">
 <div class="wrap">
   <a class="back" href="/" style="color:#4f46e5;font-weight:700;display:inline-block;margin-bottom:16px">&#8594; رجوع للتقارير</a>
   <div class="card" style="max-width:380px;margin:40px auto;text-align:center">
     <div style="font-size:40px;margin-bottom:6px">🔒</div>
     <h1 style="font-size:18px;margin:0 0 4px">تبويب الإعدادات محمي</h1>
     <p style="color:#6b7280;font-size:13px;margin:0 0 16px">أدخل رمز الدخول للمتابعة</p>
     {% if error %}<div class="err" style="margin-bottom:12px">رمز الدخول غير صحيح</div>{% endif %}
     <form method="post">
       <input type="password" name="pin" autofocus inputmode="numeric" placeholder="• • • • •"
              style="width:100%;text-align:center;letter-spacing:8px;font-size:22px;padding:12px;border:1.5px solid #cbd5e1;border-radius:10px;margin-bottom:14px">
       <button type="submit" style="width:100%;background:#4f46e5;color:#fff;border:0;padding:12px;border-radius:10px;font-weight:700;font-size:15px;cursor:pointer">دخول</button>
     </form>
   </div>
 </div>
</div></div></body></html>"""

@app.route("/settings/logout")
def settings_logout():
    session.pop("set_ok", None)
    return render_template_string(PIN_PAGE, error=False)

@app.route("/settings", methods=["GET","POST"])
def settings():
    # بوابة رمز الدخول
    if not session.get("set_ok"):
        if request.method == "POST" and request.form.get("pin") is not None:
            if request.form.get("pin") == SETTINGS_PIN:
                session["set_ok"] = True
            else:
                return render_template_string(PIN_PAGE, error=True)
        else:
            return render_template_string(PIN_PAGE, error=False)
    saved = False
    if request.method == "POST" and request.form.get("action") == "save":
        htabs = [t["id"] for t in TABS if request.form.get("tab_"+t["id"])]
        hreps = []
        for t in TABS:
            for r in t["reports"]:
                key = t["id"]+"/"+r["id"]
                if request.form.get("rep_"+key):
                    hreps.append(key)
        save_hidden(htabs, hreps, bool(request.form.get("hide_profit")))
        saved = True
    ht, hr = load_hidden_raw()
    return render_template_string(SETTINGS_PAGE, tabs=TABS, hidden_tabs=ht, hidden_reports=hr,
                                  saved=saved, hide_profit=load_hide_profit())




@app.route("/globals", methods=["GET","POST"])
def globals_page():
    if not session.get("set_ok"):
        if request.method == "POST" and request.form.get("pin") is not None:
            if request.form.get("pin") == SETTINGS_PIN:
                session["set_ok"] = True
            else:
                return render_template_string(PIN_PAGE, error=True)
        else:
            return render_template_string(PIN_PAGE, error=False)
            
    saved = False
    targets_data = load_globals()
    if not targets_data: targets_data = {}
    
    if request.method == "POST":
        for key in request.form:
            if key.startswith("target_2026_"):
                parts = key.split("_")
                if len(parts) == 4:
                    year = parts[1]
                    rep_code = parts[2]
                    month = parts[3]
                    try:
                        val = float(request.form[key])
                        if year not in targets_data: targets_data[year] = {}
                        if rep_code not in targets_data[year]: targets_data[year][rep_code] = {}
                        targets_data[year][rep_code][month] = val
                    except ValueError:
                        pass
        save_globals(targets_data)
        saved = True
        
    reps = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN ORDER BY REPRS_CODE")
                for c, n in cur.fetchall():
                    reps.append({"code": str(c), "name": n or str(c)})
    except Exception as e:
        print("Error loading reps:", e)
        
    return render_template_string(GLOBALS_PAGE, reps=reps, targets=targets_data.get("2026", {}), saved=saved)


DASHBOARD_PAGE = '''<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>لوحة القيادة SREEN</title>
     <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: { backgroundColor: '#1e293b', padding: 14, titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' }, bodyFont: { size: 14, family: "'Cairo', sans-serif" }, cornerRadius: 10, displayColors: true, boxPadding: 6 }
         }
       };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32}
           ]
         },
         options: {
           ...commonOptions,
           plugins: { ...commonOptions.plugins, legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, font: { family: "'Cairo'", size: 13, weight: 'bold' } } } },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });

       // C2: Doughnut (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"doughnut",
         data:{
           labels:D.rep_labels.slice(0,5),
           datasets:[{data:D.rep_vals.slice(0,5), backgroundColor:["#4f46e5", "#38bdf8", "#10b981", "#f59e0b", "#8b5cf6"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C3: Doughnut (Items)
       new Chart(document.getElementById("c3"),{
         type:"doughnut",
         data:{
           labels:D.itm_labels.slice(0,5),
           datasets:[{data:D.itm_vals.slice(0,5), backgroundColor:["#f43f5e", "#d946ef", "#0ea5e9", "#14b8a6", "#eab308"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(16, 185, 129, 0.4)');
       grad4.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات", data:D.mpurch, borderColor:"#10b981", borderWidth: 3, backgroundColor: grad4, fill:true, tension:0.4, pointRadius: 0, pointHoverRadius: 6, pointBackgroundColor: "#fff", pointBorderColor: "#10b981", pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });
     });
     </script>
<style>
 *{box-sizing:border-box;font-family:Tahoma,Arial}
 body{margin:0;background:#f1f5f9;color:#0f172a}
 .hd{background:linear-gradient(90deg,#0f766e,#134e4a);color:#fff;padding:14px 24px;display:flex;align-items:center;gap:14px;flex-wrap:wrap}
 .hd h1{margin:0;font-size:19px} .hd .sp{flex:1}
 .hd a{color:#fff;text-decoration:none;background:rgba(255,255,255,.15);padding:8px 14px;border-radius:8px;font-size:14px}
 .hd form{display:flex;gap:8px;align-items:center;font-size:13px}
 .hd input{padding:7px;border:0;border-radius:6px} .hd button{padding:8px 14px;border:0;border-radius:6px;background:#fbbf24;font-weight:700;cursor:pointer}
 .wrap{padding:22px;max-width:1300px;margin:auto}
 .kpis{display:grid;grid-template-columns:repeat(4,1fr);gap:14px;margin-bottom:22px}
 @media(max-width:900px){.kpis{grid-template-columns:repeat(2,1fr)}}
 .kpi{background:#fff;border-radius:14px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08);border-right:4px solid #0f766e}
 .kpi .l{color:#64748b;font-size:13px;margin-bottom:6px} .kpi .v{font-size:21px;font-weight:800}
 .kpi.g{border-color:#16a34a}.kpi.b{border-color:#2563eb}.kpi.o{border-color:#ea580c}.kpi.r{border-color:#dc2626}.kpi.p{border-color:#7c3aed}
 .charts{display:grid;grid-template-columns:1fr 1fr;gap:14px}
 @media(max-width:900px){.charts{grid-template-columns:1fr}}
 .ch{background:#fff;border-radius:14px;padding:16px;box-shadow:0 1px 3px rgba(0,0,0,.08)}
 .ch h3{margin:0 0 12px;font-size:15px}

</style></head><body>
 <div class="hd"><h1>📊 لوحة القيادة — SREEN</h1>
   <form method="get" action="/dashboard"><span>من</span><input type="date" name="date_from" value="{{f}}"><span>إلى</span><input type="date" name="date_to" value="{{t}}"><button type="submit">تحديث</button></form>
   <div class="sp"></div><a href="/">← التقارير</a></div>
 <div class="wrap">
   <div class="kpis">
     <div class="kpi b"><div class="l">إجمالي المبيعات</div><div class="v">{{ "{:,.0f}".format(data.sales) }}</div></div>
     <div class="kpi g"><div class="l">إجمالي التحصيل</div><div class="v">{{ "{:,.0f}".format(data.collect) }}</div></div>
     <div class="kpi o"><div class="l">إجمالي المشتريات</div><div class="v">{{ "{:,.0f}".format(data.purch) }}</div></div>
     {% if not hide_profit|default(false) %}<div class="kpi p"><div class="l">مجمل الربح</div><div class="v">{{ "{:,.0f}".format(data.gross) }}</div></div>
     <div class="kpi g"><div class="l">صافي الربح</div><div class="v">{{ "{:,.0f}".format(data.netprofit) }}</div></div>{% endif %}
     <div class="kpi r"><div class="l">الذمم المدينة</div><div class="v">{{ "{:,.0f}".format(data.recv) }}</div></div>
     <div class="kpi b"><div class="l">قيمة المخزون</div><div class="v">{{ "{:,.0f}".format(data.invval) }}</div></div>
     <div class="kpi o"><div class="l">صافي الضريبة</div><div class="v">{{ "{:,.0f}".format(data.vat) }}</div></div>
   </div>
   <div class="charts">
     <div class="ch"><h3>المبيعات والتحصيل شهرياً</h3><canvas id="c1" height="140"></canvas></div>
     <div class="ch"><h3>أفضل المناديب (مبيعات)</h3><canvas id="c2" height="140"></canvas></div>
     <div class="ch"><h3>أفضل الأصناف (مبيعات)</h3><canvas id="c3" height="140"></canvas></div>
     <div class="ch"><h3>المشتريات شهرياً</h3><canvas id="c4" height="140"></canvas></div>
   </div></div>
<script>
const D={{ data|tojson }};
Chart.defaults.font.family="Tahoma";
new Chart(c1,{type:"bar",data:{labels:D.months,datasets:[{label:"مبيعات",data:D.msales,backgroundColor:"#2563eb"},{label:"تحصيل",data:D.mcollect,backgroundColor:"#16a34a"}]}});
new Chart(c2,{type:"bar",data:{labels:D.rep_labels,datasets:[{label:"مبيعات",data:D.rep_vals,backgroundColor:"#0f766e"}]},options:{indexAxis:"y",plugins:{legend:{display:false}}}});
new Chart(c3,{type:"bar",data:{labels:D.itm_labels,datasets:[{label:"مبيعات",data:D.itm_vals,backgroundColor:"#ea580c"}]},options:{indexAxis:"y",plugins:{legend:{display:false}}}});
new Chart(c4,{type:"line",data:{labels:D.months,datasets:[{label:"مشتريات",data:D.mpurch,borderColor:"#ea580c",backgroundColor:"rgba(234,88,12,.12)",fill:true,tension:.3}]},options:{plugins:{legend:{display:false}}}});
</script></body></html>'''

def compute_dash(f, t):
    b = {"f": f, "t": t}
    P="TO_DATE(:f,'YYYY-MM-DD')"; Q="TO_DATE(:t,'YYYY-MM-DD')+1"
    d = {"sales":0,"collect":0,"purch":0,"gross":0,"netprofit":0,"recv":0,"invval":0,"vat":0,
         "months":[],"msales":[],"mcollect":[],"mpurch":[],"rep_labels":[],"rep_vals":[],"itm_labels":[],"itm_vals":[]}
    try:
        with get_conn() as con:
            cur = con.cursor()
            def sc(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); r=cur.fetchone()
                    return round(float(r[0]),2) if r and r[0] is not None else 0.0
                except Exception: return 0.0
            def rw(sql):
                try:
                    cur.execute(sql,{k:v for k,v in b.items() if (":"+k) in sql}); return cur.fetchall()
                except Exception: return []
            def mm(sql):
                m={}
                for r in rw(sql):
                    m[str(r[0])]=round(float(r[1] or 0),2)
                return m

            sales = sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            sales_ret = sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q)
            d["sales"] = round(sales - sales_ret, 2)

            d["collect"]=sc("SELECT NVL(SUM(NVL(CR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q)
            
            d["purch"]=sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            
            gross = sc("SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q)
            gross_ret = sc("SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_RT_BILL_DTL x JOIN IAS20261.IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q)
            d["gross"] = round(gross - gross_ret, 2)
            
            d["netprofit"]=sc("SELECT NVL(SUM(NVL(p.CR_AMT,0)-NVL(p.DR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL p JOIN IAS20261.ACCOUNT a ON a.A_CODE=p.A_CODE WHERE NVL(p.DOC_POST,0)=1 AND a.A_REPORT=2 AND p.DOC_DATE>="+P+" AND p.DOC_DATE<"+Q)
            
            d["recv"]=sc("SELECT NVL(SUM(bal),0) FROM (SELECT SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0)) bal FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND DOC_DATE<"+Q+" GROUP BY C_CODE HAVING SUM(NVL(DR_AMT,0)-NVL(CR_AMT,0))>0)")
            
            d["invval"]=sc("SELECT NVL(SUM(NVL(I_QTY,0)*NVL(IN_OUT,0)*NVL(STK_COST,0)),0) FROM IAS20261.ITEM_MOVEMENT WHERE I_DATE<"+Q)
            
            ov = sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            ov_ret = sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q)
            ov_net = ov - ov_ret
            
            iv = sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q)
            d["vat"]=round(ov_net-iv,2)
            
            ms=mm("SELECT TO_CHAR(BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,'YYYY-MM')")
            ms_ret=mm("SELECT TO_CHAR(RT_BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE>="+P+" AND RT_BILL_DATE<"+Q+" GROUP BY TO_CHAR(RT_BILL_DATE,'YYYY-MM')")
            
            mc=mm("SELECT TO_CHAR(DOC_DATE,'YYYY-MM'), SUM(CR_AMT) FROM (SELECT DOC_DATE, CR_AMT FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" UNION ALL SELECT DOC_DATE, CR_AMT FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" UNION ALL SELECT DOC_DATE, CR_AMT FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND C_CODE IS NOT NULL AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+" UNION ALL SELECT b.BILL_DATE AS DOC_DATE, NVL(p.DR_AMT,0) AS CR_AMT FROM IAS20261.IAS_BILL_MST b JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%' WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0 AND b.BILL_DATE>="+P+" AND b.BILL_DATE<"+Q+" UNION ALL SELECT DOC_DATE, -CR_AMT FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND TO_CHAR(A_CODE) LIKE '111%' AND DOC_DATE>="+P+" AND DOC_DATE<"+Q+") GROUP BY TO_CHAR(DOC_DATE,'YYYY-MM')")
            mp=mm("SELECT TO_CHAR(BILL_DATE,'YYYY-MM'), SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_PI_BILL_MST WHERE BILL_DATE>="+P+" AND BILL_DATE<"+Q+" GROUP BY TO_CHAR(BILL_DATE,'YYYY-MM')")
            
            months=sorted(set(list(ms)+list(ms_ret)+list(mc)+list(mp)))
            d["months"]=months
            d["msales"]=[round(ms.get(x,0) - ms_ret.get(x,0), 2) for x in months]
            d["mcollect"]=[mc.get(x,0) for x in months]
            d["mpurch"]=[mp.get(x,0) for x in months]
            
            rs = mm("SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE), SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_MST m LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE)")
            rs_ret = mm("SELECT NVL(sm.REPRS_A_NAME, m.REP_CODE_BILL), SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_RT_BILL_MST m LEFT JOIN IAS20261.SALES_MAN sm ON sm.REPRS_CODE=m.REP_CODE_BILL WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q+" GROUP BY NVL(sm.REPRS_A_NAME,m.REP_CODE_BILL)")
            
            rs_net = {k: round(rs.get(k,0) - rs_ret.get(k,0), 2) for k in set(list(rs)+list(rs_ret))}
            for k, v in sorted(rs_net.items(), key=lambda item: item[1], reverse=True):
                if v != 0:
                    d["rep_labels"].append(str(k))
                    d["rep_vals"].append(v)
            
            its = mm("SELECT NVL(i.I_NAME, x.I_CODE), SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_DTL x JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE=x.BILL_DOC_TYPE AND m.BILL_NO=x.BILL_NO AND m.BILL_SER=x.BILL_SER LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.BILL_DATE>="+P+" AND m.BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE)")
            its_ret = mm("SELECT NVL(i.I_NAME, x.I_CODE), SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.RT_BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_RT_BILL_DTL x JOIN IAS20261.IAS_RT_BILL_MST m ON m.RT_BILL_DOC_TYPE=x.RT_BILL_DOC_TYPE AND m.RT_BILL_NO=x.RT_BILL_NO AND m.RT_BILL_SER=x.RT_BILL_SER LEFT JOIN IAS20261.IAS_ITM_MST i ON i.I_CODE=x.I_CODE WHERE m.RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND m.RT_BILL_DATE>="+P+" AND m.RT_BILL_DATE<"+Q+" GROUP BY NVL(i.I_NAME,x.I_CODE)")
            
            its_net = {k: round(its.get(k,0) - its_ret.get(k,0), 2) for k in set(list(its)+list(its_ret))}
            for k, v in sorted(its_net.items(), key=lambda item: item[1], reverse=True)[:50]:
                if v != 0:
                    d["itm_labels"].append(str(k)[:22])
                    d["itm_vals"].append(v)
    except Exception as e:
        d["err"]=str(e)
    return d


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=False)
