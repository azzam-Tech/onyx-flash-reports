# -*- coding: utf-8 -*-
from flask import Flask, request, jsonify, session, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder='public', static_url_path='/')
CORS(app, supports_credentials=True)

app.secret_key = os.environ.get("SREEN_SECRET", "sreen-dev-secret-key")

@app.before_request
def set_target_year():
    from flask import request, g
    year_val = request.args.get('year_val')
    date_to = request.args.get('date_to')
    date_from = request.args.get('date_from')
    
    target_year = "2026"
    if year_val and len(year_val) == 4:
        target_year = year_val
    elif date_from and len(date_from) >= 4:
        target_year = date_from[:4]
    elif date_to and len(date_to) >= 4:
        target_year = date_to[:4]
        
    g.target_year = target_year

@app.before_request
def require_login():
    if request.method == 'OPTIONS':
        return None
    if request.path.startswith('/api/'):
        return None
    return None

# Import and register blueprints
from routes.auth import auth_bp
from routes.users import users_bp
from routes.settings import settings_bp
from routes.reports import reports_bp
from routes.dashboard import dashboard_bp

app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(settings_bp)
app.register_blueprint(reports_bp)
app.register_blueprint(dashboard_bp)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def serve_react(path):
    if path.startswith('api/'):
        return 'API route not found', 404
    public_dir = os.path.join(os.path.dirname(__file__), 'public')
    if path and os.path.exists(os.path.join(public_dir, path)):
        return send_from_directory(public_dir, path)
    return send_from_directory(public_dir, 'index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=False)
