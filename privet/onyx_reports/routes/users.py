# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, session
from config import load_users, save_users
from reports_config import TABS

users_bp = Blueprint('users', __name__)

@users_bp.route("/api/users_manage", methods=["GET", "POST"])
def api_users_manage():
    if request.method == "GET":
        users = load_users()
        safe_users = {}
        for uname, udata in users.items():
            safe_users[uname] = {
                "role": udata.get("role", "user"),
                "allowed_tabs": udata.get("allowed_tabs", []),
                "allowed_reports": udata.get("allowed_reports", [])
            }
        
        tabs_data = []
        for t in TABS:
            reports_data = [{"id": r["id"], "title": r["title"]} for r in t["reports"]]
            tabs_data.append({"id": t["id"], "title": t["title"], "reports": reports_data})
            
        return jsonify({"users": safe_users, "tabs": tabs_data})

    elif request.method == "POST":
        if session.get("role") != "admin":
            return jsonify({"error": "Unauthorized"}), 403
            
        data = request.json
        if not data:
            return jsonify({"error": "No data provided"}), 400
            
        action = data.get("action")
        username = data.get("username", "").strip()
        users = load_users()
        
        if action == "add_or_update" and username:
            password = data.get("password")
            role = data.get("role", "user")
            
            allowed_tabs = data.get("allowed_tabs", [])
            allowed_reports = data.get("allowed_reports", [])
            
            if role == "admin":
                allowed_tabs = ["*"]
                allowed_reports = ["*"]
                
            users[username] = {
                "password": password if password else users.get(username, {}).get("password", ""),
                "role": role,
                "allowed_tabs": allowed_tabs,
                "allowed_reports": allowed_reports
            }
            save_users(users)
            return jsonify({"success": True})
            
        elif action == "delete" and username:
            if username in users and username != "admin":
                del users[username]
                save_users(users)
                return jsonify({"success": True})
            return jsonify({"error": "Cannot delete this user"}), 400
            
        return jsonify({"error": "Invalid action"}), 400
