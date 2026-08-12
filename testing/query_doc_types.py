import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn
import pandas as pd

try:
    con = get_conn()
    df = pd.read_sql("SELECT DOC_TYPE, IN_OUT, COUNT(*) as cnt, SUM(I_QTY) as qty FROM IAS20261.ITEM_MOVEMENT WHERE W_CODE IN (105, 103, 121, 122, 118, 108, 119) GROUP BY DOC_TYPE, IN_OUT ORDER BY DOC_TYPE, IN_OUT", con)
    print(df.to_string())
except Exception as e:
    print("Error:", e)
