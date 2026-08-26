import os
from datetime import datetime

now = datetime.now()
year_start = f"{now.year}-01-01"
year_end = f"{now.year}-12-31"

handlers_file = 'privet/onyx_reports/report_handlers.py'
with open(handlers_file, 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace("'2026-01-01'", f"'{year_start}'")
text = text.replace("'2026-12-31'", f"'{year_end}'")
text = text.replace("'2026-07-31'", f"'{year_end}'") # fallback if any

with open(handlers_file, 'w', encoding='utf-8') as f:
    f.write(text)

print("report_handlers.py fixed!")
