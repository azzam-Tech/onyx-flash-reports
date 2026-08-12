import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='CUSTOMER' AND (column_name LIKE '%GRP%' OR column_name LIKE '%GROUP%')", con)
        print("CUSTOMER table group columns:")
        print(df)
        df2 = pd.read_sql("SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='CUSTOMER_GROUP'", con)
        print("Columns in CUSTOMER_GROUP:")
        print(df2)
except Exception as e:
    print(e)
