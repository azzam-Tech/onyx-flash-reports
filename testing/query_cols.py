import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn
import pandas as pd

try:
    con = get_conn()
    df = pd.read_sql("SELECT COLUMN_NAME FROM all_tab_columns WHERE table_name = 'ITEM_MOVEMENT'", con)
    print(df['COLUMN_NAME'].tolist())
except Exception as e:
    print("Error:", e)
