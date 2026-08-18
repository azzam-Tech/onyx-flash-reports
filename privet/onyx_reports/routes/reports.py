# -*- coding: utf-8 -*-
from functools import wraps
from flask import Blueprint, request, jsonify, session
from config import check_permission, load_hidden
from reports_config import TABS, find_report
from report_handlers import run_report, lookups, add_total_row

reports_bp = Blueprint('reports', __name__)

def require_report_permission(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        username = session.get('username')
        if not username:
            return jsonify({"error": "غير مصرح، الرجاء تسجيل الدخول أولاً."}), 401
            
        tab_id = kwargs.get('tab_id')
        report_id = kwargs.get('report_id')
        
        if tab_id and report_id:
            if not check_permission(username, tab_id, report_id):
                return jsonify({"error": "عذراً، لا تملك الصلاحية لعرض هذا التقرير."}), 403
                
        return f(*args, **kwargs)
    return decorated_function

@reports_bp.route("/api/tabs")
def api_tabs():
    username = session.get('username')
    hidden_tabs, hidden_reports = load_hidden()
    
    _vis = []
    for t in TABS:
        if t["id"] in hidden_tabs: continue
        if not check_permission(username, t["id"]): continue
        
        allowed_reports = []
        for r in t["reports"]:
            if r["id"] in hidden_reports: continue
            if not r.get("hide_from_menu", False):
                if check_permission(username, t["id"], r["id"]):
                    allowed_reports.append({"id": r["id"], "title": r["title"]})
        
        if allowed_reports:
            _vis.append({"id": t["id"], "title": t["title"], "reports": allowed_reports})
            
    return jsonify({"tabs": _vis})

@reports_bp.route("/api/reports/<tab_id>/<report_id>")
@require_report_permission
def api_report_data(tab_id, report_id):
    username = session.get('username')
        
    tab, rpt = find_report(tab_id, report_id)
    if not rpt:
        return jsonify({"error": "التقرير غير موجود"}), 404
        
    try:
        resolved_params = []
        for p in rpt.get('params', []):
            param_def = dict(p)
            if callable(param_def.get('get_default')):
                param_def['default'] = param_def['get_default']()
                del param_def['get_default']
            
            if param_def["name"] in ("rep_code", "c_code", "v_code", "i_code", "a_code", "cc_code", "grp_code"):
                if "options" not in param_def or not param_def["options"]:
                    try:
                        l_items = lookups(param_def["name"])
                        param_def["type"] = "select"
                        param_def["options"] = [["", "الكل / بدون تحديد"]] + [[x, x] for x in l_items]
                    except Exception as e:
                        print("Lookup error:", e)

            resolved_params.append(param_def)
            
        binds = dict(request.args)
        
        if tab_id == 'stock' or (tab_id == 'summary' and report_id in ('detailed_stock_pivot', 'dead_stock_value')):
            from modules.warehouses.services import handle_warehouse_report
            cols, rows = handle_warehouse_report(report_id, rpt, request.args)
        elif tab_id == 'sales' or (tab_id == 'summary' and report_id in ('workflow_summary', 'debt_movement_summary', 'net_debt_movement_summary')):
            from modules.sales.services import handle_sales_report
            cols, rows = handle_sales_report(report_id, rpt, request.args)
        elif tab_id == 'fin' or report_id in ('perf_aging_dynamic', 'perf_aging_dynamic_analytical', 'perf_aging_exact'):
            from modules.fin.services import handle_fin_report
            cols, rows = handle_fin_report(report_id, rpt, request.args)
        elif tab_id == 'ar' or (tab_id == 'summary' and report_id in ('statement_analytic', 'aging')):
            from modules.ar.services import handle_ar_report
            cols, rows = handle_ar_report(report_id, rpt, request.args)
        elif tab_id == 'pur':
            from modules.pur.services import handle_pur_report
            cols, rows = handle_pur_report(report_id, rpt, request.args)
        elif tab_id == 'general' or (tab_id == 'summary' and report_id == 'item_prices_and_stock'):
            from modules.general.services import handle_general_report
            cols, rows = handle_general_report(report_id, rpt, request.args)
        elif tab_id in ('tax', 'prof', 'dts', 'summary', 'hr'):
            import importlib
            module = importlib.import_module(f"modules.{tab_id}.services")
            handler = getattr(module, f"handle_{tab_id}_report")
            cols, rows = handler(report_id, rpt, request.args)
        else:
            cols, rows = run_report(rpt, request.args)
            
        # Add total row for all reports
        cols, rows = add_total_row(cols, rows, report_id)
            
        return jsonify({
            "cols": cols, 
            "rows": rows, 
            "params": resolved_params, 
            "binds": binds,
            "metadata": {
                "id": rpt.get("id"),
                "pivot_type": rpt.get("pivot_type", None)
            }
        })
    except Exception as e:
        print(f"Report execution error for {tab_id}/{report_id}:", e)
        return jsonify({"error": str(e)}), 500
