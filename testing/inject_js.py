import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Locate the end of PAGE = """...</body></html>"""
js_script = """
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        const typeSelect = document.querySelector('select[name="p_type"]');
        const valSelect = document.querySelector('select[name="p_val"]');
        if(typeSelect && valSelect) {
          const valWrapper = valSelect.parentElement; // Usually a div grouping label + select
          
          function updateOptions() {
            const val = typeSelect.value;
            valSelect.innerHTML = ''; // clear options
            valWrapper.style.display = 'block';
            
            let options = [];
            if(val === 'month') {
              for(let i=1; i<=12; i++) options.push([i, "شهر " + i]);
            } else if(val === 'quarter') {
              options = [[1, 'الربع الأول'], [2, 'الربع الثاني'], [3, 'الربع الثالث'], [4, 'الربع الرابع']];
            } else if(val === 'half') {
              options = [[1, 'النصف الأول'], [2, 'النصف الثاني']];
            } else if(val === 'year') {
              valWrapper.style.display = 'none';
            }
            
            options.forEach(opt => {
              const el = document.createElement('option');
              el.value = opt[0];
              el.textContent = opt[1];
              valSelect.appendChild(el);
            });
            
            // try to re-select previous value if any from URL
            const urlParams = new URLSearchParams(window.location.search);
            const prevVal = urlParams.get('p_val');
            if(prevVal) {
                valSelect.value = prevVal;
                if(!valSelect.value) valSelect.value = options.length > 0 ? options[0][0] : '';
            }
          }
          
          typeSelect.addEventListener('change', updateOptions);
          updateOptions(); // call on load
        }
      });
    </script>
"""

# Replace </body></html> inside PAGE definition
if '</body></html>"""' in content and 'const typeSelect = document.querySelector' not in content:
    content = content.replace('</body></html>"""', js_script + '</body></html>"""', 1)
    with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
        f.write(content)
    print("SUCCESS")
else:
    print("ALREADY INJECTED OR NOT FOUND")
