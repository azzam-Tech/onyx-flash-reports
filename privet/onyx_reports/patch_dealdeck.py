# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

dealdeck_style = '''STYLE = """<style>
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
.app { display: flex; min-height: 100vh; padding: 20px; gap: 24px; }
.sb { width: 260px; background: var(--sb-bg); border-radius: 24px; display: flex; flex-direction: column; padding: 30px 20px; flex-shrink: 0; box-shadow: var(--sh); }
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

.filters { background: var(--card-bg); border-radius: 20px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); margin-bottom: 24px; }
.filters label { display: block; font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 8px; }
.filters input, .filters select { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 14px; font-weight: 500; color: var(--ink-dark); background: #f8fafc; outline: none; transition: 0.3s; }
.filters input:focus, .filters select:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1); }
.filters .btn { background: var(--primary); color: #fff; border: 0; padding: 14px 24px; border-radius: 12px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.3s; height: 46px; }
.filters .btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2); }

.tw { overflow-x: auto; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }
table { border-collapse: collapse; width: 100%; min-width: 600px; }
thead th { color: var(--ink); padding: 16px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line); white-space: nowrap; }
tbody td { padding: 16px; border-bottom: 1px solid var(--line); font-size: 14px; font-weight: 500; color: var(--ink-dark); white-space: nowrap; transition: 0.2s; }
tbody tr:hover td { background: #f8fafc; }

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

@media(max-width:900px){.app{flex-direction:column;padding:10px;} .sb{width:100%;flex-direction:row;padding:15px;overflow-x:auto;border-radius:16px;gap:10px; align-items:center;} .brand{margin:0;padding-right:15px;} .brand span{display:none;} .menu-lbl{display:none;} .sb a{margin:0;padding:10px;} .sb a span{display:none;} .gkpis{grid-template-columns:repeat(2,1fr)}.gcharts{grid-template-columns:1fr}}
</style>"""'''

text = re.sub(r'STYLE\s*=\s*\"\"\"<style>.*?</style>\"\"\"', dealdeck_style.replace('\\', '\\\\'), text, flags=re.DOTALL)

# Also update the PAGE HTML structure for the new DealDeck sidebar
old_sb = ''' <aside class="sb">
   <div class="brand"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg></div>
   <a href="/dashboard"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3zM13 21h8V3h-8zM3 21h8v-6H3z"/></svg>لوحة</a>
   {% for t in tabs %}{% if t.id not in hidden_tabs %}
     <a class="{{ 'on' if t.id==cur_tab else '' }}" href="/?tab={{t.id}}">
       <svg viewBox="0 0 24 24"><path d="{{t.icon}}"/></svg>{{ t.title.split(' ')[0] }}</a>
   {% endif %}{% endfor %}
   <a href="/settings" style="margin-top:auto"><svg viewBox="0 0 24 24"><path d="M4 6h9M4 12h5M4 18h7"/><circle cx="17" cy="6" r="2.3"/><circle cx="13" cy="12" r="2.3"/><circle cx="15" cy="18" r="2.3"/></svg>إعدادات</a>
 </aside>'''

new_sb = ''' <aside class="sb">
   <div class="brand"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span>Onyx Deck</span></div>
   <div class="menu-lbl">القائمة الرئيسية</div>
   <a href="/dashboard" class="{{ 'on' if request.path == '/dashboard' else '' }}"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3zM13 21h8V3h-8zM3 21h8v-6H3z"/></svg><span>لوحة القيادة</span></a>
   {% for t in tabs %}{% if t.id not in hidden_tabs %}
     <a class="{{ 'on' if t.id==cur_tab else '' }}" href="/?tab={{t.id}}">
       <svg viewBox="0 0 24 24"><path d="{{t.icon}}"/></svg><span>{{ t.title }}</span></a>
   {% endif %}{% endfor %}
   <div class="menu-lbl" style="margin-top:auto">أدوات</div>
   <a href="/settings"><svg viewBox="0 0 24 24"><path d="M4 6h9M4 12h5M4 18h7"/><circle cx="17" cy="6" r="2.3"/><circle cx="13" cy="12" r="2.3"/><circle cx="15" cy="18" r="2.3"/></svg><span>الإعدادات</span></a>
 </aside>'''

if '<aside class="sb">' in text:
    text = text.replace(old_sb, new_sb)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("DealDeck UI applied!")
