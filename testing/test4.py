import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='WAREHOUSES'", con)
        print("Columns in WAREHOUSES:")
        print(df)
        df2 = pd.read_sql("SELECT table_name FROM all_tables WHERE owner='IAS20261' AND table_name LIKE '%WARE%'", con)
        print("Tables like WARE:")
        print(df2)
except Exception as e:
    print(e)
