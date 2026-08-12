import os

file_path = 'privet/onyx_reports/templates/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
in_table_block = False
in_sort_js = False

for i, line in enumerate(lines):
    # Detect start of table block
    if '<div class="tw"><table><thead><tr>{% for c in cols %}<th onclick="sortTable({{loop.index0}})' in line:
        in_table_block = True
        # insert new block
        new_lines.append("""<div class="tw" style="overflow-x:hidden;">
  <table id="mainTable" class="display nowrap" style="width:100%">
    <thead>
      {% if rpt.id == 'detailed_stock_pivot' %}
      <tr>
        <th colspan="6" style="text-align:center; background:#f8fafc;">معلومات الصنف</th>
        <th colspan="7" style="text-align:center; background:#4f46e5; color:#fff;">الرصيد الافتتاحي</th>
        <th colspan="2" style="text-align:center; background:#0ea5e9; color:#fff;">الحركة (صادر / وارد)</th>
        <th colspan="7" style="text-align:center; background:#10b981; color:#fff;">الرصيد النهائي</th>
      </tr>
      <tr>
        {% for c in cols %}
          {% set clean_c = c|replace('افتتاحي ', '')|replace('نهائي ', '')|replace('صادر (مبيعات/تحويل)', 'صادر')|replace('وارد (مشتريات/استرجاع)', 'وارد') %}
          <th>{{ clean_c }}</th>
        {% endfor %}
      </tr>
      {% else %}
      <tr>
        {% for c in cols %}
          <th>{{ c }}</th>
        {% endfor %}
      </tr>
      {% endif %}
    </thead>
    
    {% set has_total = rows and ((rows[0][0]|string|trim) == 'الإجمالي' or (rows[0][1]|string|trim) == 'الإجمالي') %}
    {% if has_total %}
      {% set data_rows = rows[1:] %}
    {% else %}
      {% set data_rows = rows %}
    {% endif %}

    <tbody>
      {% for row in data_rows %}
        {% set r1 = (row[1]|string).strip() %}
        {% set cls = '' %}
        {% if 'رصيد الفترة صافي' in r1 %}
          {% set cls = 'prof-row1' %}
        {% elif 'الرصيد النهائي صافي' in r1 %}
          {% set cls = 'prof-row2' %}
        {% endif %}
        <tr class="{{ cls }}">
          {% for cell in row %}
            <td>{{ '' if cell is none else cell }}</td>
          {% endfor %}
        </tr>
      {% endfor %}
    </tbody>

    {% if has_total %}
    <tfoot>
      <tr class="tot-row" style="background: #e2e8f0; font-weight: bold; color: #0f172a;">
        {% for cell in rows[0] %}
          <td style="border-top:2px solid #cbd5e1; border-bottom:2px solid #cbd5e1;">{{ '' if cell is none else cell }}</td>
        {% endfor %}
      </tr>
    </tfoot>
    {% endif %}
  </table>
</div>\n""")
        continue
        
    if in_table_block:
        if '</tbody></table></div>' in line:
            in_table_block = False
        continue

    # Detect sortTable JS
    if 'function sortTable(colIndex) {' in line:
        in_sort_js = True
        continue
        
    if in_sort_js:
        if '      });' in line and 'a.href =' in lines[i-1]:
            pass
        if '    }' in line and i > 500 and in_sort_js: # rough guess, usually ends with }
            if i+1 < len(lines) and '</script>' in lines[i+1]:
                in_sort_js = False
        continue
        
    new_lines.append(line)

# Handle JS block cleanup safely using regex on the result string
html = "".join(new_lines)

# Remove the sortTable function precisely
import re
html = re.sub(r'function sortTable\(colIndex\)\s*\{[\s\S]*?a\.href = url\.pathname \+ url\.search;\s*\n\s*\}\);\s*\}', '', html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("index.html patched using line parser")
