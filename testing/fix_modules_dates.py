import os
from datetime import datetime
import calendar

now = datetime.now()
first_day = f"{now.year}-{now.month:02d}-01"
last_day = f"{now.year}-{now.month:02d}-{calendar.monthrange(now.year, now.month)[1]:02d}"
year_start = f"{now.year}-01-01"
year_end = f"{now.year}-12-31"

# Fix ar/services.py
ar_file = 'privet/onyx_reports/modules/ar/services.py'
with open(ar_file, 'r', encoding='utf-8') as f:
    ar_text = f.read()
ar_text = ar_text.replace("date_to_str = '2026-07-31'", f"date_to_str = '{last_day}'")
with open(ar_file, 'w', encoding='utf-8') as f:
    f.write(ar_text)

# Fix warehouses/services.py
wh_file = 'privet/onyx_reports/modules/warehouses/services.py'
with open(wh_file, 'r', encoding='utf-8') as f:
    wh_text = f.read()
wh_text = wh_text.replace("args.get('date_from', '2026-01-01')", f"args.get('date_from', '{year_start}')")
wh_text = wh_text.replace("args.get('date_to', '2026-12-31')", f"args.get('date_to', '{year_end}')")
wh_text = wh_text.replace("args.get('date_to', '2026-07-31')", f"args.get('date_to', '{last_day}')")
with open(wh_file, 'w', encoding='utf-8') as f:
    f.write(wh_text)

print("ar and warehouses fixed!")
