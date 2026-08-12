import re
import os

file_path = 'privet/onyx_reports/templates/index.html'

with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace DataTables JS
old_js = r'<script>\s*\$\(document\)\.ready\(function\(\)\s*\{(.*?)\}\);\s*</script>'

new_js = """<script>
$(document).ready(function() {
    if($('#mainTable').length){
        var table = $('#mainTable').DataTable({
            "language": {
                "url": "//cdn.datatables.net/plug-ins/1.13.6/i18n/ar.json",
                "search": "بحث سريع:",
                "searchPlaceholder": "اكتب للبحث في التقرير...",
                "lengthMenu": "عرض _MENU_ سجل"
            },
            "pageLength": 100,
            "lengthMenu": [[50, 100, 500, -1], [50, 100, 500, "الكل"]],
            "scrollX": true,
            "ordering": true,
            "bSortClasses": false,
            initComplete: function () {
                this.api().columns().every(function () {
                    let column = this;
                    
                    // Create select element
                    let select = document.createElement('select');
                    select.add(new Option('جميع الحالات', ''));
                    select.style.display = 'block';
                    select.style.width = '100%';
                    select.style.marginTop = '6px';
                    select.style.fontSize = '12px';
                    select.style.padding = '4px';
                    select.style.borderRadius = '6px';
                    select.style.border = '1px solid #cbd5e1';
                    select.style.fontWeight = '500';
                    select.style.color = '#0f172a';
                    select.style.background = '#f8fafc';
                    select.style.outline = 'none';
                    select.style.cursor = 'pointer';
                    
                    // Prevent sorting when clicking on select
                    select.addEventListener('click', function (e) {
                        e.stopPropagation();
                    });
                    
                    // Apply listener for user change in value
                    select.addEventListener('change', function () {
                        var val = $.fn.dataTable.util.escapeRegex(select.value);
                        column.search(val ? '^' + val + '$' : '', true, false).draw();
                    });
                    
                    // Append to header cell
                    column.header().appendChild(select);
                    
                    // Add list of options
                    column.data().unique().sort().each(function (d, j) {
                        let text = d ? String(d).replace(/<[^>]*>?/gm, '').trim() : '';
                        // Ignore empty text or the total row text
                        if (text && text !== 'الإجمالي') {
                            select.add(new Option(text, text));
                        }
                    });
                });
            }
        });
        
        $('#mainTable').on('order.dt', function () {
            let order = table.order();
            if(order && order.length > 0) {
                let colIndex = order[0][0];
                let dir = order[0][1];
                let $th = $(table.column(colIndex).header());
                // Get text without the select options text
                let colName = $th.clone().children().remove().end().text().trim();
                
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
</script>"""

html = re.sub(old_js, new_js, html, flags=re.DOTALL)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)
print("JS filter dropdowns patched successfully.")
