# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

old_charts_html = '''<div class="gcharts" style="grid-template-columns: 1fr 1fr 1fr;">
          <div class="gc" style="grid-column: span 2;"><h3>المبيعات والتحصيل شهرياً</h3><canvas id="c1" height="250"></canvas></div>
          <div class="gc" style="display:flex; flex-direction:column; align-items:center;"><h3>أفضل 5 مناديب</h3><div style="width:100%; max-width:250px; flex:1;"><canvas id="c2"></canvas></div></div>
          <div class="gc" style="display:flex; flex-direction:column; align-items:center;"><h3>أفضل 5 أصناف</h3><div style="width:100%; max-width:250px; flex:1;"><canvas id="c3"></canvas></div></div>
          <div class="gc" style="grid-column: span 2;"><h3>المشتريات شهرياً</h3><canvas id="c4" height="250"></canvas></div>
        </div>'''

new_charts_html = '''<div class="gcharts" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
          <div class="gc" style="grid-column: 1 / -1;"><h3>المبيعات والتحصيل شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c1"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 مناديب</h3><div style="position:relative;height:250px;width:100%"><canvas id="c2"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 أصناف</h3><div style="position:relative;height:250px;width:100%"><canvas id="c3"></canvas></div></div>
          <div class="gc" style="grid-column: 1 / -1;"><h3>المشتريات شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c4"></canvas></div></div>
        </div>'''

if old_charts_html in text:
    text = text.replace(old_charts_html, new_charts_html)
else:
    # Use regex fallback
    text = re.sub(r'<div class="gcharts" style="grid-template-columns: 1fr 1fr 1fr;">.*?</div>\s*</div>\s*</div>\s*</div>', new_charts_html, text, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Chart containers fixed!")
