import sys
from privet.onyx_reports.database import get_conn
import pandas as pd

with get_conn() as con:
    df = pd.read_sql("SELECT NVL(DOC_POST,0) as doc_post, DOC_TYPE, SUM(CR_AMT) as sum_cr, SUM(DR_AMT) as sum_dr FROM IAS_POST_DTL WHERE DOC_DATE >= TO_DATE('2026-08-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-09-01','YYYY-MM-DD') GROUP BY NVL(DOC_POST,0), DOC_TYPE ORDER BY 1, 2", con)
    print(df)
