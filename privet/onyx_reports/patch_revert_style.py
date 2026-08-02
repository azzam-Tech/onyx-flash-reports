# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# The original CSS
old_style = '''STYLE = """<style>
 :root{--nav1:#12333c;--nav2:#0c2027;--card:#fff;--ink:#20343a;--muted:#93a7ab;--teal:#22b3a3;--teald:#14867a;--tealsoft:#dcf1ec;--line:#eef3f1;--sh:0 8px 24px rgba(20,60,60,.06)}
 *{box-sizing:border-box;margin:0;padding:0} body{font-family:Tahoma,Arial,sans-serif;background:#e8f1ee;color:var(--ink);direction:rtl}
 a{text-decoration:none;color:inherit}
 .app{display:flex;min-height:100vh}
 .sb{width:76px;background:linear-gradient(180deg,var(--nav1),var(--nav2));display:flex;flex-direction:column;align-items:center;padding:18px 0;gap:14px;border-top-left-radius:26px;flex-shrink:0}
 .sb .brand{width:38px;height:38px;border-radius:10px;background:rgba(255,255,255,.12);display:flex;align-items:center;justify-content:center;color:#fff;margin-bottom:10px}
 .sb a{color:#7d9aa1;width:46px;height:46px;border-radius:13px;display:flex;flex-direction:column;align-items:center;justify-content:center;font-size:9px;gap:3px}
 .sb a.on{background:#fff;color:var(--teald)}
 .sb svg{width:22px;height:22px;stroke:currentColor;fill:none;stroke-width:1.9}
 .main{flex:1;min-width:0;display:flex;flex-direction:column}
 .top{display:flex;align-items:center;gap:14px;padding:16px 22px}
 .logo{height:40px}
 .ttl{font-weight:700;font-size:17px} .ttl b{color:var(--teald)}
 .wrap{padding:4px 22px 26px}
 .pills{display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px}
 .pill{background:#fff;border:1px solid var(--line);border-radius:11px;padding:9px 14px;font-size:13px;font-weight:600;color:#5a7379;box-shadow:var(--sh)}
 .pill.on{background:var(--teal);color:#fff;border-color:var(--teal)}
 .filters{background:#fff;border:1px solid var(--line);border-radius:14px;padding:14px;margin-bottom:16px;display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:12px;align-items:end;box-shadow:var(--sh)}
 .filters label{display:block;font-size:12px;color:#374151;font-weight:600;margin-bottom:5px}
 .filters input,.filters select{width:100%;padding:9px;border:1px solid #cbd5e1;border-radius:9px;font-family:inherit;font-size:13px}
 .filters .btn{background:var(--teal);color:#fff;border:0;padding:10px 16px;border-radius:9px;font-weight:700;cursor:pointer;font-size:14px}
 h1{font-size:18px;margin-bottom:12px;border-right:5px solid var(--teal);padding-right:10px}
 .cnt{color:var(--muted);font-size:13px;margin:4px 2px 8px}
 .tw{overflow-x:auto;background:#fff;border:1px solid var(--line);border-radius:14px;box-shadow:var(--sh)}
 table{border-collapse:collapse;width:100%;min-width:560px}
 thead th{background:var(--nav1);color:#fff;padding:11px 10px;text-align:right;font-size:12px;white-space:nowrap;position:sticky;top:0}
 tbody td{padding:9px 10px;border-bottom:1px solid #f0f4f3;font-size:12px;white-space:nowrap}
 tbody tr:nth-child(even) td{background:#fafcfb} tbody tr:hover td{background:#f0faf8}
 .err{background:#fdecee;color:#b80023;padding:14px;border-radius:12px;border:1px solid #f5c2c8}
 @media(max-width:640px){.filters{grid-template-columns:1fr 1fr}.wrap{padding:4px 14px 20px}}
 .rhead{display:flex;align-items:center;gap:10px;margin-bottom:12px} .rhead h1{margin:0;flex:1} .exps{display:flex;gap:8px} .exp{border:0;border-radius:9px;padding:8px 15px;font-weight:700;font-size:13px;color:#fff;cursor:pointer;text-decoration:none} .exp.xl{background:#1a8f5a} .exp.pf{background:#b80023}

 .gdwrap{background:linear-gradient(135deg,#e0ecff 0%,#dcf1ec 45%,#efe9ff 100%);border-radius:22px;padding:20px}
 .gkpis{display:grid;grid-template-columns:repeat(4,1fr);gap:15px;margin-bottom:18px}
 .gk{background:rgba(255,255,255,.5);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.65);border-radius:18px;padding:16px;display:flex;align-items:center;gap:13px;box-shadow:0 10px 30px rgba(30,60,90,.09)}
 .gk .gic{width:46px;height:46px;border-radius:14px;display:flex;align-items:center;justify-content:center;font-size:21px;flex-shrink:0}
 .gk .gl{font-size:12px;color:#475569;margin-bottom:3px} .gk .gv{font-size:19px;font-weight:800;color:#0f172a}
 .gcharts{display:grid;grid-template-columns:1fr 1fr;gap:15px}
 .gc{background:rgba(255,255,255,.5);backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);border:1px solid rgba(255,255,255,.65);border-radius:18px;padding:16px;box-shadow:0 10px 30px rgba(30,60,90,.09)}
 .gc h3{font-size:14px;margin:0 0 12px;color:#0f172a;border:0;padding:0}
 @media(max-width:900px){.gkpis{grid-template-columns:repeat(2,1fr)}.gcharts{grid-template-columns:1fr}}
</style>"""'''

# Replace using regex
pattern = re.compile(r'STYLE\s*=\s*\"\"\"<style>.*?</style>\"\"\"', re.DOTALL)
text = pattern.sub(old_style.replace('\\', '\\\\'), text)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("UI Reverted successfully!")
