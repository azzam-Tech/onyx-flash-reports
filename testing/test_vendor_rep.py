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
    WITH cust_debt AS (
        SELECT TO_CHAR(p.C_CODE) as c_code, SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as debt
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.C_CODE IS NOT NULL
          AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
          AND TO_CHAR(p.REP_CODE) = :rep_code
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
            WHEN c.C_VENDOR IS NOT NULL AND v.bal > 0 THEN v.bal 
            ELSE 0 
        END
    )
    FROM cust_debt d
    LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = d.c_code
    LEFT JOIN vendor_bal v ON TO_CHAR(c.C_VENDOR) = v.v_code
"""

sql_test_no_vendor = """
    SELECT SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as debt
    FROM IAS20261.IAS_POST_DTL p
    WHERE p.C_CODE IS NOT NULL
      AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
      AND TO_CHAR(p.REP_CODE) = :rep_code
"""

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute(sql_test, {'rep_code': rep_code, 'dt': date_to_str})
        row = cur.fetchone()
        print("DEBT (VENDOR LINKED, REP ONLY):", row[0])

        cur.execute(sql_test_no_vendor, {'rep_code': rep_code, 'dt': date_to_str})
        row = cur.fetchone()
        print("DEBT (NO VENDOR, REP ONLY):", row[0])
