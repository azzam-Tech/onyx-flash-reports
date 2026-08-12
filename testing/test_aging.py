import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
from database import get_conn
import pandas as pd

try:
    con = get_conn()
    
    # Old Query
    df_old = pd.read_sql("""
     WITH pay AS (SELECT C_CODE, SUM(NVL(CR_AMT,0)) paid FROM IAS20261.IAS_POST_DTL
                  WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE('2026-07-31','YYYY-MM-DD')+1
                  GROUP BY C_CODE),
     charges AS (SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0) amt,
                   SUM(NVL(p.DR_AMT,0)) OVER (PARTITION BY p.C_CODE ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) cum
                 FROM IAS20261.IAS_POST_DTL p
                 WHERE NVL(p.DOC_POST,0)=1 AND p.C_CODE IS NOT NULL AND NVL(p.DR_AMT,0)>0
                   AND p.DOC_DATE < TO_DATE('2026-07-31','YYYY-MM-DD')+1),
     openit AS (SELECT ch.C_CODE, GREATEST(0,LEAST(ch.amt,ch.cum-NVL(pay.paid,0))) unpaid,
                   TRUNC(TO_DATE('2026-07-31','YYYY-MM-DD'))-TRUNC(ch.DOC_DATE) age
                FROM charges ch LEFT JOIN pay ON pay.C_CODE=ch.C_CODE)
     SELECT SUM(o.unpaid) AS TOTAL_UNPAID
     FROM openit o
     WHERE o.unpaid>0
    """, con)
    print("OLD TOTAL UNPAID:", df_old.iloc[0]['TOTAL_UNPAID'])

    # New Query
    df_new = pd.read_sql("""
     WITH pay AS (SELECT C_CODE, SUM(NVL(CR_AMT,0)) paid FROM IAS20261.IAS_POST_DTL
                  WHERE (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2)) AND C_CODE IS NOT NULL
                    AND DOC_DATE < TO_DATE('2026-07-31','YYYY-MM-DD')+1
                  GROUP BY C_CODE),
     charges AS (SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0) amt,
                   SUM(NVL(p.DR_AMT,0)) OVER (PARTITION BY p.C_CODE ORDER BY p.DOC_DATE,p.DOC_NO,p.DOC_SER
                        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW) cum
                 FROM IAS20261.IAS_POST_DTL p
                 WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2)) AND p.C_CODE IS NOT NULL AND NVL(p.DR_AMT,0)>0
                   AND p.DOC_DATE < TO_DATE('2026-07-31','YYYY-MM-DD')+1),
     openit AS (SELECT ch.C_CODE, GREATEST(0,LEAST(ch.amt,ch.cum-NVL(pay.paid,0))) unpaid,
                   TRUNC(TO_DATE('2026-07-31','YYYY-MM-DD'))-TRUNC(ch.DOC_DATE) age
                FROM charges ch LEFT JOIN pay ON pay.C_CODE=ch.C_CODE)
     SELECT SUM(o.unpaid) AS TOTAL_UNPAID
     FROM openit o
     WHERE o.unpaid>0
    """, con)
    print("NEW TOTAL UNPAID:", df_new.iloc[0]['TOTAL_UNPAID'])

except Exception as e:
    print("Error:", e)
