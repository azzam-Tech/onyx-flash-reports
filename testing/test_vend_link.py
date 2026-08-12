import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='CUSTOMER'", con)
        print("V columns:")
        print(df[df['COLUMN_NAME'].str.contains('V_') | df['COLUMN_NAME'].str.contains('VEND')])
except Exception as e:
    print(e)
