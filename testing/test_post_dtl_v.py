import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='IAS_POST_DTL'", con)
        print("Columns in IAS_POST_DTL:")
        print(df[df['COLUMN_NAME'].str.contains('V_')])
except Exception as e:
    print(e)
