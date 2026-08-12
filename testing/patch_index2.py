import re

file_path = 'privet/onyx_reports/templates/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Add DataTables CSS to head
if "jquery.dataTables.min.css" not in html:
    dt_css = """
<link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
<style>
.dataTables_wrapper { direction: rtl; padding: 10px; }
.dataTables_wrapper .dataTables_filter { float: left; text-align: left; }
.dataTables_wrapper .dataTables_length { float: right; }
table.dataTable thead th, table.dataTable tfoot th { text-align: right; border-bottom: 1px solid #e2e8f0; }
table.dataTable.no-footer { border-bottom: 1px solid #e2e8f0; }
.dataTables_wrapper .dataTables_paginate .paginate_button { padding: 4px 10px; margin-left: 2px; }
</style>
</head>"""
    html = html.replace('</head>', dt_css)

# 2. Add DataTables JS and jQuery to body end
if "jquery.dataTables.min.js" not in html:
    dt_js = """
<script src="https://code.jquery.com/jquery-3.7.1.min.js"></script>
<script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
<script>
$(document).ready(function() {
    if($('#mainTable').length){
        var table = $('#mainTable').DataTable({
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/ar.json"
            },
            "pageLength": 100,
            "lengthMenu": [[50, 100, 500, -1], [50, 100, 500, "الكل"]],
            "scrollX": true,
            "ordering": true,
            "bSortClasses": false
        });
        
        $('#mainTable').on('order.dt', function () {
            let order = table.order();
            if(order && order.length > 0) {
                let colIndex = order[0][0];
                let dir = order[0][1];
                let $th = $(table.column(colIndex).header());
                let colName = $th.text().trim();
                
                let exps = document.querySelectorAll('.exp');
                exps.forEach(a => {
                    try {
                        let url = new URL(a.href, window.location.origin);
                        url.searchParams.set('sort_col', colName);
                        url.searchParams.set('sort_dir', dir);
                        a.href = url.pathname + url.search;
                    } catch(e){}
                });
            }
        });
    }
});
</script>
</body>"""
    html = html.replace('</body>', dt_js)

# 3. Replace table block using DOTALL regex
old_table_pattern = r'<div class="tw"><table><thead><tr>\{\% for c in cols \%\}(.*?)</tbody></table></div>'
new_table = """<div class="tw" style="overflow-x:hidden;">
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
</div>"""

if not 'id="mainTable"' in html:
    html, n = re.subn(old_table_pattern, new_table, html, flags=re.DOTALL)
    print(f"Replaced table blocks: {n}")

# 4. Remove the old sortTable JS block
old_sort_js = r'function sortTable\(colIndex\)\s*\{[\s\S]*?a\.href = url\.pathname \+ url\.search;\s*\n\s*\}\);\s*\}'
html, m = re.subn(old_sort_js, '', html)
print(f"Removed sortTable instances: {m}")

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
