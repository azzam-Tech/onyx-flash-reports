import os
import sys
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
date_to_str = '2026-07-31'

sql_test = """
    WITH custs AS (
        SELECT TO_CHAR(C_CODE) as c_code, TO_CHAR(C_VENDOR) as v_code
        FROM IAS20261.CUSTOMER
    ),
    cust_debt AS (
        SELECT TO_CHAR(p.C_CODE) as c_code, SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as debt
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.C_CODE IS NOT NULL
          AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
          AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)
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
        d.debt - 
        CASE 
            WHEN c.v_code IS NOT NULL AND v.bal > 0 THEN v.bal 
            ELSE 0 
        END
    )
    FROM cust_debt d
    LEFT JOIN custs c ON c.c_code = d.c_code
    LEFT JOIN vendor_bal v ON c.v_code = v.v_code
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_test, {'rep_code': rep_code, 'dt': date_to_str})
        row = cur.fetchone()
        print("RAW SQL DEBT (VENDOR LINKED, JULY 31):", row[0])
