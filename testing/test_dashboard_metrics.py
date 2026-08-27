import os
from dotenv import load_dotenv
import oracledb
from datetime import datetime

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

def get_metrics(rep_code, date_from, date_to):
    sql = """
    WITH sales_base AS (
        SELECT SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
          AND TRIM(REP_CODE) = TRIM(:rep_code)
    ),
    returns_base AS (
        SELECT SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
          AND TRIM(REP_CODE) = TRIM(:rep_code)
    ),
    col_trans AS (
      SELECT p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
        AND TRIM(p.REP_CODE) = TRIM(:rep_code)
      UNION ALL
      SELECT 0, p.CR_AMT, 0, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
        AND TRIM(p.REP_CODE) = TRIM(:rep_code)
      UNION ALL
      SELECT 0, 0, NVL(p.DR_AMT,0), 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
        AND TRIM(b.REP_CODE) = TRIM(:rep_code)
      UNION ALL
      SELECT 0, 0, 0, p.CR_AMT
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE <= TO_DATE(:date_to,'YYYY-MM-DD')
        AND TRIM(p.REP_CODE) = TRIM(:rep_code)
    )
    SELECT 
      (SELECT NVL(sales, 0) FROM sales_base) - (SELECT NVL(returns, 0) FROM returns_base) as net_sales,
      (SELECT NVL(SUM(rcpt + net_jrn + cash_sales - cash_ret), 0) FROM col_trans) as total_collection
    FROM DUAL
    """
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, {'date_from': date_from, 'date_to': date_to, 'rep_code': rep_code})
            return cur.fetchone()

print("Testing rep 141, year 2026:")
metrics = get_metrics('141', '2026-01-01', '2026-12-31')
print("Net Sales (Year):", metrics[0])
print("Collections (Year):", metrics[1])

print("Testing rep 141, month 8:")
metrics = get_metrics('141', '2026-08-01', '2026-08-31')
print("Net Sales (Month):", metrics[0])
print("Collections (Month):", metrics[1])
