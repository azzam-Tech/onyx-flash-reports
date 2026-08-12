import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

try:
    with get_conn() as con:
        df = pd.read_sql("SELECT C_CODE, C_A_NAME, C_VENDOR FROM IAS20261.CUSTOMER WHERE C_VENDOR IS NOT NULL AND ROWNUM <= 10", con)
        print("Linked Customers:")
        print(df)
except Exception as e:
    print(e)
