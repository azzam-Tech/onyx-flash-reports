import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    with get_conn() as con:
        df = pd.read_sql("""
            SELECT table_name, column_name 
            FROM all_tab_columns 
            WHERE owner='IAS20261' 
              AND (column_name = 'W_A_NAME' OR column_name LIKE '%WH_NAME%')
        """, con)
        print(df)
except Exception as e:
    print(e)
