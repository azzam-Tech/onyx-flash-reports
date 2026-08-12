import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='COST_CENTER'", con)
        print("COST_CENTER columns:")
        print(df)
except Exception as e:
    print(e)
