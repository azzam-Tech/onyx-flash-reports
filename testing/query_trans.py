import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    con = get_conn()
    df = pd.read_sql("SELECT TABLE_NAME FROM all_tables WHERE TABLE_NAME LIKE '%TRANS%' AND owner='IAS20261'", con)
    print("Tables:", df['TABLE_NAME'].tolist())
except Exception as e:
    print("Error:", e)
