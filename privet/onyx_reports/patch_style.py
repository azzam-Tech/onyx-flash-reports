# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# The new beautiful CSS
new_style = '''STYLE = """<style>
 :root {
   --nav1: #0f172a; --nav2: #1e293b; --nav-accent: #38bdf8;
   --bg: #f8fafc; --card: #ffffff;
   --ink: #334155; --ink-dark: #0f172a; --muted: #94a3b8;
   --primary: #0ea5e9; --primary-hover: #0284c7;
   --teal: #10b981; --teald: #059669; --tealsoft: #d1fae5;
   --line: #e2e8f0; --sh: 0 4px 20px rgba(15, 23, 42, 0.04);
   --sh-hover: 0 10px 30px rgba(15, 23, 42, 0.08);
 }
 @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;600;700;800;900&display=swap');
 * { box-sizing: border-box; margin: 0; padding: 0; }
 body { font-family: 'Cairo', Tahoma, sans-serif; background: var(--bg); color: var(--ink); direction: rtl; line-height: 1.6; }
 a { text-decoration: none; color: inherit; transition: all 0.3s ease; }
 .app { display: flex; min-height: 100vh; }
 .sb { width: 84px; background: linear-gradient(180deg, var(--nav1), var(--nav2)); display: flex; flex-direction: column; align-items: center; padding: 24px 0; gap: 16px; border-top-left-radius: 30px; border-bottom-left-radius: 30px; flex-shrink: 0; box-shadow: 4px 0 24px rgba(0,0,0,0.1); z-index: 10; margin: 10px 0 10px 10px; border: 1px solid rgba(255,255,255,0.05); }
 .sb .brand { width: 48px; height: 48px; border-radius: 14px; background: linear-gradient(135deg, var(--primary), var(--teal)); display: flex; align-items: center; justify-content: center; color: #fff; margin-bottom: 12px; box-shadow: 0 4px 12px rgba(16,185,129,0.3); }
 .sb .brand svg { width: 26px; height: 26px; stroke: #fff; }
 .sb a { color: #94a3b8; width: 60px; height: 60px; border-radius: 18px; display: flex; flex-direction: column; align-items: center; justify-content: center; font-size: 11px; font-weight: 700; gap: 6px; transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); }
 .sb a:hover { color: #fff; background: rgba(255,255,255,0.08); transform: translateY(-2px); }
 .sb a.on { background: rgba(255,255,255,0.12); color: var(--nav-accent); box-shadow: inset 3px 0 0 var(--nav-accent); }
 .sb svg { width: 24px; height: 24px; stroke: currentColor; fill: none; stroke-width: 2; transition: all 0.3s ease; }
 .sb a.on svg { transform: scale(1.15); stroke-width: 2.5; }
 .main { flex: 1; min-width: 0; display: flex; flex-direction: column; padding: 10px 20px 20px 20px; }
 .top { display: flex; align-items: center; gap: 16px; padding: 14px 10px 24px; }
 .logo { height: 44px; filter: drop-shadow(0 2px 4px rgba(0,0,0,0.05)); }
 .ttl { font-weight: 900; font-size: 20px; color: var(--ink-dark); letter-spacing: -0.5px; } .ttl b { color: var(--primary); }
 .wrap { padding: 0 10px 26px; }
 .pills { display: flex; gap: 12px; flex-wrap: wrap; margin-bottom: 24px; }
 .pill { background: rgba(255,255,255,0.6); backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px); border: 1px solid rgba(255,255,255,0.8); border-radius: 16px; padding: 10px 20px; font-size: 14px; font-weight: 800; color: #64748b; box-shadow: var(--sh); transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: pointer; }
 .pill:hover { transform: translateY(-3px); box-shadow: var(--sh-hover); color: var(--primary); background: #fff; }
 .pill.on { background: linear-gradient(135deg, var(--primary), var(--teal)); color: #fff; border-color: transparent; box-shadow: 0 8px 20px rgba(14, 165, 233, 0.25); }
 .filters { background: rgba(255,255,255,0.8); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border: 1px solid #fff; border-radius: 24px; padding: 22px 28px; margin-bottom: 24px; display: grid; grid-template-columns: repeat(auto-fit,minmax(180px,1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); }
 .filters label { display: block; font-size: 14px; color: #475569; font-weight: 800; margin-bottom: 8px; }
 .filters input, .filters select { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 14px; font-family: inherit; font-size: 14px; font-weight: 700; color: var(--ink-dark); background: #f8fafc; transition: all 0.3s ease; }
 .filters input:focus, .filters select:focus { outline: none; border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(14, 165, 233, 0.15); }
 .filters .btn { background: linear-gradient(135deg, var(--primary), var(--primary-hover)); color: #fff; border: 0; padding: 13px 22px; border-radius: 14px; font-weight: 900; cursor: pointer; font-size: 15px; box-shadow: 0 6px 16px rgba(14, 165, 233, 0.25); transition: all 0.3s ease; }
 .filters .btn:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(14, 165, 233, 0.35); }
 h1 { font-size: 24px; font-weight: 900; margin-bottom: 16px; color: var(--ink-dark); display: flex; align-items: center; gap: 12px; }
 h1::before { content: ""; display: inline-block; width: 6px; height: 26px; background: linear-gradient(180deg, var(--primary), var(--teal)); border-radius: 6px; }
 .cnt { color: var(--muted); font-size: 14px; font-weight: 700; margin: 4px 6px 14px; }
 .tw { overflow-x: auto; background: rgba(255,255,255,0.9); backdrop-filter: blur(24px); border: 1px solid rgba(255,255,255,0.6); border-radius: 24px; box-shadow: var(--sh); }
 table { border-collapse: collapse; width: 100%; min-width: 600px; }
 thead th { background: rgba(248, 250, 252, 0.95); backdrop-filter: blur(12px); color: #475569; padding: 18px 16px; text-align: right; font-size: 14px; font-weight: 900; white-space: nowrap; position: sticky; top: 0; border-bottom: 2px solid var(--line); z-index: 5; }
 tbody td { padding: 16px; border-bottom: 1px solid #f1f5f9; font-size: 14px; font-weight: 700; color: var(--ink); white-space: nowrap; transition: all 0.2s ease; }
 tbody tr:hover td { background: #f0f9ff; color: var(--primary-hover); transform: scale(1.002); }
 .err { background: #fef2f2; color: #b91c1c; padding: 18px 24px; border-radius: 18px; border: 1px solid #fecaca; font-weight: 800; font-size: 15px; box-shadow: 0 6px 16px rgba(239, 68, 68, 0.08); }
 @media(max-width:640px){.filters{grid-template-columns:1fr 1fr}.wrap{padding:4px 14px 20px} .sb { width: 64px; margin: 0; border-radius: 0; padding: 12px 0; } .sb a { width: 48px; height: 48px; font-size: 0; } .sb a svg { margin: 0; }}
 .rhead { display: flex; align-items: center; gap: 14px; margin-bottom: 20px; } .rhead h1 { margin: 0; flex: 1; } .exps { display: flex; gap: 12px; } 
 .exp { border: 0; border-radius: 12px; padding: 11px 20px; font-weight: 900; font-size: 14px; color: #fff; cursor: pointer; text-decoration: none; display: inline-flex; align-items: center; justify-content: center; transition: all 0.3s ease; box-shadow: 0 6px 14px rgba(0,0,0,0.12); } 
 .exp:hover { transform: translateY(-3px); box-shadow: 0 8px 20px rgba(0,0,0,0.2); filter: brightness(1.1); }
 .exp.xl { background: linear-gradient(135deg, #10b981, #059669); } .exp.pf { background: linear-gradient(135deg, #ef4444, #b91c1c); }

 .gdwrap { background: linear-gradient(135deg, #e0f2fe 0%, #d1fae5 50%, #ede9fe 100%); border-radius: 28px; padding: 28px; box-shadow: inset 0 2px 24px rgba(255,255,255,0.6); }
 .gkpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; margin-bottom: 28px; }
 .gk { background: rgba(255,255,255,0.65); backdrop-filter: blur(28px); -webkit-backdrop-filter: blur(28px); border: 1px solid rgba(255,255,255,0.9); border-radius: 24px; padding: 22px; display: flex; align-items: center; gap: 18px; box-shadow: 0 12px 34px rgba(15,23,42,0.06); transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1); cursor: default; }
 .gk:hover { transform: translateY(-5px); box-shadow: 0 16px 44px rgba(15,23,42,0.1); background: rgba(255,255,255,0.85); }
 .gk .gic { width: 58px; height: 58px; border-radius: 18px; display: flex; align-items: center; justify-content: center; font-size: 26px; flex-shrink: 0; box-shadow: 0 6px 16px rgba(0,0,0,0.06); }
 .gk .gl { font-size: 14px; font-weight: 800; color: #64748b; margin-bottom: 4px; } .gk .gv { font-size: 24px; font-weight: 900; color: var(--ink-dark); letter-spacing: -0.5px; }
 .gcharts { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
 .gc { background: rgba(255,255,255,0.65); backdrop-filter: blur(28px); -webkit-backdrop-filter: blur(28px); border: 1px solid rgba(255,255,255,0.9); border-radius: 24px; padding: 24px; box-shadow: 0 12px 34px rgba(15,23,42,0.06); transition: all 0.3s ease; }
 .gc:hover { box-shadow: 0 16px 44px rgba(15,23,42,0.1); background: rgba(255,255,255,0.85); }
 .gc h3 { font-size: 17px; font-weight: 900; margin: 0 0 20px; color: var(--ink-dark); }
 @media(max-width:900px){.gkpis{grid-template-columns:repeat(2,1fr)}.gcharts{grid-template-columns:1fr}}
</style>"""'''

# Replace using regex
pattern = re.compile(r'STYLE\s*=\s*\"\"\"<style>.*?</style>\"\"\"', re.DOTALL)
text = pattern.sub(new_style.replace('\\', '\\\\'), text)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("UI Redesign complete!")
