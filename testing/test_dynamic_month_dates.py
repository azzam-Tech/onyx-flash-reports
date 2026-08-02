import calendar
from datetime import datetime

def get_current_month_dates():
    now = datetime.now()
    year = now.year
    month = now.month
    last_day = calendar.monthrange(year, month)[1]
    
    dfrom = f"{year}-{month:02d}-01"
    dto = f"{year}-{month:02d}-{last_day:02d}"
    return dfrom, dto

dfrom, dto = get_current_month_dates()
print(f"Current dynamic month dates: FROM = {dfrom}, TO = {dto}")

# Test for month 8 (August)
def test_month_dates(year, month):
    last_day = calendar.monthrange(year, month)[1]
    return f"{year}-{month:02d}-01", f"{year}-{month:02d}-{last_day:02d}"

print("Month 8 (August) dynamic dates:", test_month_dates(2026, 8))
print("Month 9 (September) dynamic dates:", test_month_dates(2026, 9))
print("Month 12 (December) dynamic dates:", test_month_dates(2026, 12))
