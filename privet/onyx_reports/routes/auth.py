# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify, session
from config import load_users

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/api/login", methods=["POST"])
def api_login():
    data = request.json or {}
    pin = data.get("pin", "")
    
    users = load_users()
    
    found_username = None
    found_user_data = None
    for uname, udata in users.items():
        if udata.get("password") == pin:
            found_username = uname
            found_user_data = udata
            break
            
    if found_username:
        session['logged_in'] = True
        session['username'] = found_username
        session['role'] = found_user_data.get('role', 'user')
        return jsonify({
            "success": True, 
            "user": {
                "username": found_username,
                "role": session['role'],
                "allowed_tabs": found_user_data.get("allowed_tabs", []),
                "allowed_reports": found_user_data.get("allowed_reports", [])
            }
        })
    else:
        return jsonify({"success": False, "error": "رمز المرور غير صحيح"}), 401

@auth_bp.route("/api/session", methods=["GET"])
def api_session():
    if not session.get('logged_in'):
        return jsonify({"authenticated": False}), 401
    
    users = load_users()
    username = session.get('username')
    user_data = users.get(username, {})
    
    return jsonify({
        "authenticated": True,
        "user": {
            "username": username,
            "role": session.get('role', 'user'),
            "allowed_tabs": user_data.get("allowed_tabs", []),
            "allowed_reports": user_data.get("allowed_reports", [])
        }
    })

@auth_bp.route("/api/logout", methods=["POST"])
def api_logout():
    session.pop('logged_in', None)
    session.pop('username', None)
    session.pop('role', None)
    return jsonify({"success": True})
