import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    con = get_conn()
    df = pd.read_sql("""
    SELECT 
        SUM(CASE WHEN dt.IN_OUT = -1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as OLD_OUT,
        SUM(CASE WHEN dt.IN_OUT = 1 THEN NVL(dt.I_QTY,0) ELSE 0 END) as OLD_IN,
        SUM(CASE WHEN dt.IN_OUT = -1 
          AND NOT EXISTS (
            SELECT 1 FROM IAS20261.ITEM_MOVEMENT t2 
            WHERE t2.DOC_NO = dt.DOC_NO AND t2.DOC_SER = dt.DOC_SER AND t2.I_CODE = dt.I_CODE AND t2.IN_OUT = 1 
            AND t2.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
          ) THEN NVL(dt.I_QTY,0) ELSE 0 END) as NEW_OUT,
        SUM(CASE WHEN dt.IN_OUT = 1 
          AND NOT EXISTS (
            SELECT 1 FROM IAS20261.ITEM_MOVEMENT t2 
            WHERE t2.DOC_NO = dt.DOC_NO AND t2.DOC_SER = dt.DOC_SER AND t2.I_CODE = dt.I_CODE AND t2.IN_OUT = -1 
            AND t2.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
          ) THEN NVL(dt.I_QTY,0) ELSE 0 END) as NEW_IN
    FROM IAS20261.ITEM_MOVEMENT dt
    WHERE dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
    """, con)
    print(df.to_string())
except Exception as e:
    print("Error:", e)
