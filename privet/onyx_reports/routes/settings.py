# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, session
from config import load_hidden, save_hidden, load_globals, save_globals, load_hide_profit, load_hidden_raw
from database import get_pooled_conn as get_db_connection

settings_bp = Blueprint('settings', __name__)

@settings_bp.route("/api/settings_manage", methods=["GET", "POST"])
def api_settings_manage():
    if session.get("role") != "admin":
        return jsonify({"error": "Unauthorized"}), 403
        
    if request.method == "GET":
        reps = []
        try:
            with get_db_connection() as conn:
                with conn.cursor() as cur:
                    cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN")
                    for c, n in cur.fetchall():
                        reps.append({"code": str(c), "name": n or str(c)})
        except Exception as e:
            print("Error loading reps:", e)
            
        targets_data = load_globals()
        ht, hr = load_hidden_raw()
        
        return jsonify({
            "reps": reps,
            "targets": targets_data.get("2026", {}),
            "hide_profit": load_hide_profit(),
            "hidden_tabs": list(ht),
            "hidden_reports": list(hr)
        })

    elif request.method == "POST":
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        hide_profit = bool(data.get("hide_profit", False))
        hidden_tabs = data.get("hidden_tabs", [])
        hidden_reports = data.get("hidden_reports", [])
        targets = data.get("targets", {})
        
        save_hidden(hidden_tabs, hidden_reports, hide_profit=hide_profit)
        
        targets_data = load_globals()
        if not targets_data:
            targets_data = {}
        targets_data["2026"] = targets
        save_globals(targets_data)
        
        return jsonify({"success": True})
