import os
import calendar
from datetime import datetime
import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception as e:
    print("thick warn:", e)

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def get_date_range(year_str, period_type, period_val):
    try:
        yr = int(year_str)
    except:
        yr = datetime.now().year
        
    date_from = f"{yr}-01-01"
    date_to = f"{yr}-12-31"
    
    if period_type == "monthly" and period_val and period_val != "all":
        try:
            m = int(period_val)
            last_day = calendar.monthrange(yr, m)[1]
            date_from = f"{yr}-{m:02d}-01"
            date_to = f"{yr}-{m:02d}-{last_day:02d}"
        except:
            pass
    elif period_type == "quarterly" and period_val and period_val != "all":
        q_map = {
            "q1": (1, 3, 31), "1": (1, 3, 31),
            "q2": (4, 6, 30), "2": (4, 6, 30),
            "q3": (7, 9, 30), "3": (7, 9, 30),
            "q4": (10, 12, 31), "4": (10, 12, 31),
        }
        if period_val in q_map:
            sm, em, ed = q_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
    elif period_type == "semi_annual" and period_val and period_val != "all":
        h_map = {
            "h1": (1, 6, 30), "1": (1, 6, 30),
            "h2": (7, 12, 31), "2": (7, 12, 31),
        }
        if period_val in h_map:
            sm, em, ed = h_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
            
    return date_from, date_to

print("Testing Date Ranges:")
print("2026 Annual:", get_date_range("2026", "annual", "all"))
print("2026 Monthly (June):", get_date_range("2026", "monthly", "6"))
print("2026 Quarterly (Q2):", get_date_range("2026", "quarterly", "q2"))
print("2026 Semi-Annual (H1):", get_date_range("2026", "semi_annual", "h1"))
