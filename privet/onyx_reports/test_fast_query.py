from database import get_conn
import time

query_slow = """
SELECT c.C_CODE, 
       (SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)), 0) 
        FROM IAS20261.IAS_POST_DTL 
        WHERE (C_CODE = c.C_CODE OR C_V_CODE = TO_CHAR(c.C_CODE) OR V_C_CODE = TO_CHAR(c.C_CODE)) 
        AND NVL(DOC_POST,0) = 1) as ACTUAL_BALANCE
FROM IAS20261.CUSTOMER c
WHERE ROWNUM <= 5
"""

query_fast = """
WITH CustBal AS (
    SELECT C_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as BAL
    FROM IAS20261.IAS_POST_DTL 
    WHERE C_CODE IS NOT NULL AND NVL(DOC_POST,0) = 1
    GROUP BY C_CODE
),
VendBal AS (
    SELECT C_V_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as BAL
    FROM IAS20261.IAS_POST_DTL 
    WHERE C_V_CODE IS NOT NULL AND V_CODE IS NOT NULL AND NVL(DOC_POST,0) = 1
    GROUP BY C_V_CODE
)
SELECT 
    c.C_CODE,
    NVL(cb.BAL, 0) + NVL(vb.BAL, 0) as ACTUAL_BALANCE
FROM IAS20261.CUSTOMER c
LEFT JOIN CustBal cb ON c.C_CODE = cb.C_CODE
LEFT JOIN VendBal vb ON TO_CHAR(c.C_CODE) = vb.C_V_CODE
WHERE ROWNUM <= 5
"""

with get_conn() as con:
    with con.cursor() as cur:
        # Test Fast
        t0 = time.time()
        cur.execute(query_fast)
        res_fast = cur.fetchall()
        t1 = time.time()
        print(f"Fast query took {t1-t0:.2f} seconds")
        print(res_fast)
        
        # Test Slow
        t0 = time.time()
        cur.execute(query_slow)
        res_slow = cur.fetchall()
        t1 = time.time()
        print(f"Slow query took {t1-t0:.2f} seconds")
        print(res_slow)
