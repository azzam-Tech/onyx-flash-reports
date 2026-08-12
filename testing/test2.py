import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT table_name FROM all_tables WHERE owner='IAS20261' AND table_name LIKE '%WH%' OR table_name LIKE '%WAREHOUSE%'", con)
        print("Tables:")
        print(df)
except Exception as e:
    print(e)

with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    c = f.read()
    idx = c.find('"by_item"')
    print("--- by_item ---")
    print(c[idx:idx+2500])
