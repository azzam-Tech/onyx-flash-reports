# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, session
from config import check_permission, load_hidden
from reports_config import TABS, find_report
from report_handlers import run_report, lookups

reports_bp = Blueprint('reports', __name__)

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
def api_report_data(tab_id, report_id):
    username = session.get('username')
    # if not check_permission(username, tab_id, report_id):
    #     return jsonify({"error": "غير مصرح لك بعرض هذا التقرير."}), 403
        
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
        
        cols, rows = run_report(rpt, request.args)
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
        return jsonify({"error": str(e)}), 500
