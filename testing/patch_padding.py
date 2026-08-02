import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Replace STYLE padding
content = content.replace(
    "thead th{background:#4f46e5;color:#fff;padding:10px 12px;font-size:12px;text-align:right;border:1px solid #4338ca;font-weight:700}",
    "thead th{background:#4f46e5;color:#fff;padding:5px 8px;font-size:12px;text-align:right;border:1px solid #4338ca;font-weight:700}"
)

content = content.replace(
    "tbody td{padding:8px 12px;font-size:12px;border:1px solid #e2e8f0;text-align:right;font-weight:500;color:#1e293b}",
    "tbody td{padding:4px 8px;font-size:12px;border:1px solid #e2e8f0;text-align:right;font-weight:500;color:#1e293b}"
)

# And if there are any other occurrences of these paddings in PRINT_PAGE CSS, wait, they are the same strings so the above replace() without count will replace both in STYLE and PRINT_PAGE!
with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)

print("CSS Padding updated!")
