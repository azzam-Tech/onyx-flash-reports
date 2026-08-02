import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Make the page landscape for better fitting, and reduce font size for print.
# In PRINT_PAGE:
new_style = """
<style>
@page { size: A4 landscape; margin: 10mm; }
*{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{font-family:'Cairo','Inter',Tahoma,sans-serif;direction:rtl;color:#1e293b;margin:0;font-size:11px;}
.hd{display:flex;align-items:center;justify-content:space-between;border-bottom:2px solid #4f46e5;padding-bottom:10px;margin-bottom:15px}
.hd h1{font-size:18px;margin:0;color:#0f172a;font-weight:800}
.hd .dt{font-size:11px;color:#64748b;margin-top:6px;font-weight:600}
.logo{height:35px}
.filt{font-size:11px;color:#475569;margin-bottom:10px;background:#f8fafc;border:1px solid #e2e8f0;border-radius:8px;padding:8px 10px;font-weight:600}
.filt b{color:#4f46e5}
table{border-collapse:collapse;width:100%;table-layout:fixed;word-wrap:break-word;}
thead th{background:#4f46e5;color:#fff;padding:4px 4px;font-size:11px;text-align:right;border:1px solid #4338ca;font-weight:700}
tbody td{padding:3px 4px;font-size:11px;border:1px solid #e2e8f0;text-align:right;font-weight:500;color:#1e293b}
"""

content = re.sub(r'<style>\s*@page\{margin:13mm\}[\s\S]*?tbody td\{padding:4px 8px;font-size:12px;border:1px solid #e2e8f0;text-align:right;font-weight:500;color:#1e293b\}', new_style.strip(), content)

# Also ensure table layout in UI doesn't hide anything.
# I already removed white-space nowrap and min-width.

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("Updated PRINT_PAGE style for landscape and fitting")
