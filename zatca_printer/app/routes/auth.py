from flask import Blueprint, request, jsonify, render_template, redirect, url_for, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from app.database import get_conn
from app.utils.helpers import decrypt_onyx_password
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('reports.dashboard'))
        
    if request.method == 'POST':
        rep_code = request.form.get('rep_code')
        password = request.form.get('password')
        
        try:
            with get_conn() as con:
                with con.cursor() as cur:
                    cur.execute("SELECT U_ID, REP_CODE, U_A_NAME, PASSWORD FROM IAS20261.USER_R WHERE REP_CODE = :1", [rep_code])
                    row = cur.fetchone()
                    if row:
                        u_id, r_code, u_name, encrypted_pwd = row
                        decrypted_pwd = decrypt_onyx_password(encrypted_pwd)
                        if password == decrypted_pwd:
                            from app import User
                            user = User(id=u_id, rep_code=r_code, name=u_name)
                            login_user(user)
                            session['rep_code'] = r_code
                            
                            # Capture the latest terminal (MAC) address used by this rep
                            try:
                                cur.execute("SELECT AD_TRMNL_NM FROM IAS20261.DTS_CST_VST_MST WHERE REP_CODE = :1 AND AD_TRMNL_NM IS NOT NULL ORDER BY VST_NO DESC FETCH FIRST 1 ROWS ONLY", [r_code])
                                term_row = cur.fetchone()
                                if term_row and term_row[0]:
                                    session['trmnl_nm'] = term_row[0]
                                else:
                                    session['trmnl_nm'] = 'WEB_PORTAL'
                            except Exception as e:
                                print("Error fetching terminal name:", e)
                                session['trmnl_nm'] = 'WEB_PORTAL'

                            return redirect(url_for('reports.dashboard'))
                        else:
                            flash('كلمة المرور غير صحيحة')
                    else:
                        flash('رقم المندوب غير موجود')
        except Exception as e:
            flash(f'خطأ في الاتصال بقاعدة البيانات: {str(e)}')
            
    return render_template('login.html')

@auth_bp.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('rep_code', None)
    return redirect(url_for('auth.login'))

@auth_bp.route('/set_lang/<lang>')
def set_lang(lang):
    if lang in ['ar', 'en']:
        session['lang'] = lang
    return redirect(request.referrer or url_for('auth.login'))
