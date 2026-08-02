# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add APP_PIN
if 'APP_PIN =' not in text:
    text = text.replace('SETTINGS_PIN = os.environ.get("SETTINGS_PIN", "00900")',
                        'SETTINGS_PIN = os.environ.get("SETTINGS_PIN", "00900")\nAPP_PIN = os.environ.get("APP_PIN", "12345")')

# 2. Add Before Request & Login routes
auth_logic = '''
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

'''

if '@app.before_request' not in text:
    # Insert after app definition
    text = re.sub(r'(DB_DSN\s*=\s*os\.environ\.get\("ORA_DSN",.*?\n)', r'\1\n' + auth_logic + '\n', text)

# 3. Add Logout to the Sidebar in PAGE template
logout_html = '''<a href="/logout" class="menu-item"><span class="icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h4"></path><polyline points="16 17 21 12 16 7"></polyline><line x1="21" y1="12" x2="9" y2="12"></line></svg></span> تسجيل خروج</a>'''
if 'href="/logout"' not in text:
    text = text.replace('<a href="/settings" class="menu-item">', logout_html + '\n      <a href="/settings" class="menu-item">')

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Authentication layer added!")
