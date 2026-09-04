import os
import json
from datetime import timedelta
from flask import Flask, session
from flask_login import LoginManager, UserMixin
from flask_wtf.csrf import CSRFProtect
from dotenv import load_dotenv

from app.database import get_conn
from app.local_db import init_local_db

load_dotenv()

# Initialize Local SQLite DB
init_local_db()

csrf = CSRFProtect()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

from app.models import User

@login_manager.user_loader
def load_user(user_id):
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("SELECT U_ID, REP_CODE, U_A_NAME FROM IAS20261.USER_R WHERE U_ID = :1", [user_id])
                row = cur.fetchone()
                if row:
                    return User(id=row[0], rep_code=row[1], name=row[2])
    except Exception as e:
        print("Error loading user:", e)
    return None

def create_app():
    app = Flask(__name__)
    
    # 1. Security & Sessions
    app.secret_key = os.getenv("SECRET_KEY", "fallback_dev_key_if_missing")
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=30)
    
    # Enable CSRF Protection globally
    csrf.init_app(app)
    
    # Auto reload templates
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    login_manager.init_app(app)
    
    # Make session permanent
    @app.before_request
    def make_session_permanent():
        session.permanent = True

    # I18N Engine
    LOCALES_DIR = os.path.join(os.path.dirname(__file__), 'locales')
    translations_cache = {}

    def load_translations(lang):
        if lang not in translations_cache:
            path = os.path.join(LOCALES_DIR, f"{lang}.json")
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    translations_cache[lang] = json.load(f)
            except Exception as e:
                print(f"Error loading {lang}.json: {e}")
                translations_cache[lang] = {}
        return translations_cache[lang]

    @app.context_processor
    def inject_i18n():
        lang = session.get('lang', 'ar')
        translations = load_translations(lang)
        
        def t(key):
            return translations.get(key, key)
        
        return {
            't': t,
            'current_lang': lang,
            'page_dir': 'rtl' if lang == 'ar' else 'ltr'
        }

    # Register Blueprints
    from app.routes.auth import auth_bp
    from app.routes.reports import reports_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(reports_bp)

    return app
