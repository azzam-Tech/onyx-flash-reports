import os
from dotenv import load_dotenv
import oracledb

load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\db.env")

lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    pass

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

rep_code = '144'
date_to_str = '2026-08-31'

sql_test = """
    WITH custs AS (
        SELECT TO_CHAR(C_CODE) as c_code, TO_CHAR(C_VENDOR) as v_code
        FROM IAS20261.CUSTOMER
        WHERE TO_CHAR(REP_CODE) = :rep_code
    ),
    cust_debt AS (
        SELECT TO_CHAR(p.C_CODE) as c_code, SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as debt
        FROM IAS20261.IAS_POST_DTL p
        JOIN custs c ON TO_CHAR(p.C_CODE) = c.c_code
        WHERE p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
          -- AND NVL(p.DOC_POST, 0) = 1
        GROUP BY TO_CHAR(p.C_CODE)
    ),
    vendor_bal AS (
        SELECT TO_CHAR(V_CODE) as v_code, SUM(NVL(CR_AMT,0) - NVL(DR_AMT,0)) as bal
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND V_CODE IS NOT NULL 
          AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
        GROUP BY TO_CHAR(V_CODE)
    )
    SELECT SUM(
        NVL(d.debt, 0) - 
        CASE 
            WHEN c.v_code IS NOT NULL AND NVL(v.bal, 0) > 0 THEN v.bal 
            ELSE 0 
        END
    )
    FROM custs c
    LEFT JOIN cust_debt d ON c.c_code = d.c_code
    LEFT JOIN vendor_bal v ON c.v_code = v.v_code
"""

sql_test_no_vendor = """
    WITH custs AS (
        SELECT TO_CHAR(C_CODE) as c_code
        FROM IAS20261.CUSTOMER
        WHERE TO_CHAR(REP_CODE) = :rep_code
    )
    SELECT SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as debt
    FROM IAS20261.IAS_POST_DTL p
    JOIN custs c ON TO_CHAR(p.C_CODE) = c.c_code
    WHERE p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
      -- AND NVL(p.DOC_POST, 0) = 1
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_test, {'rep_code': rep_code, 'dt': date_to_str})
        row = cur.fetchone()
        print("DEBT (VENDOR LINKED, CUST.REP):", row[0])

        cur.execute(sql_test_no_vendor, {'rep_code': rep_code, 'dt': date_to_str})
        row = cur.fetchone()
        print("DEBT (NO VENDOR, CUST.REP):", row[0])
