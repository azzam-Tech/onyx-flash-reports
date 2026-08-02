import os
import calendar
from datetime import datetime
import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception as e:
    print("thick warn:", e)

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def get_conn():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

def test_period_movement(year_val="2026"):
    con = get_conn()
    cur = con.cursor()

    # Get list of months
    months = [f"{year_val}-{m:02d}" for m in range(1, 13)]

    print(f"\nPeriod Debt Movement Roll-Forward for Year {year_val}:")
    print(f"{'Period':<10} | {'Opening Debt':<15} | {'Sales (VAT)':<15} | {'Collection':<15} | {'Closing Debt':<15}")
    print("-" * 80)

    for m_str in months:
        date_from = f"{m_str}-01"
        yr = int(year_val)
        m = int(m_str.split("-")[1])
        last_day = calendar.monthrange(yr, m)[1]
        date_to = f"{m_str}-{last_day:02d}"

        # Opening Debt before date_from
        cur.execute("SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)),0) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL AND DOC_DATE < TO_DATE(:d, 'YYYY-MM-DD')", {"d": date_from})
        open_bal = float(cur.fetchone()[0] or 0)

        # Net Sales
        cur.execute("SELECT NVL(SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)),0) FROM IAS20261.IAS_BILL_MST WHERE BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND BILL_DATE >= TO_DATE(:f, 'YYYY-MM-DD') AND BILL_DATE < TO_DATE(:t, 'YYYY-MM-DD')+1", {"f": date_from, "t": date_to})
        sales = float(cur.fetchone()[0] or 0)

        cur.execute("SELECT NVL(SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)),0) FROM IAS20261.IAS_RT_BILL_MST WHERE RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8) AND RT_BILL_DATE >= TO_DATE(:f, 'YYYY-MM-DD') AND RT_BILL_DATE < TO_DATE(:t, 'YYYY-MM-DD')+1", {"f": date_from, "t": date_to})
        returns = float(cur.fetchone()[0] or 0)

        cur.execute("SELECT NVL(ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2),0) FROM IAS20261.IAS_POST_DTL WHERE DOC_TYPE=15 AND NVL(CR_AMT,0)>0 AND NVL(DOC_POST,0)=1 AND DOC_DATE >= TO_DATE(:f, 'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:t, 'YYYY-MM-DD')+1", {"f": date_from, "t": date_to})
        ext_disc = float(cur.fetchone()[0] or 0)

        net_sales_vat = (sales - returns - ext_disc) * 1.15

        # Collection
        sql_col = """
        WITH col_trans AS (
          SELECT CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
          FROM IAS20261.IAS_POST_DTL
          WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
            AND DOC_DATE >= TO_DATE(:f,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:t,'YYYY-MM-DD')+1
          UNION ALL
          SELECT 0, 0, 0, 0, CR_AMT
          FROM IAS20261.IAS_POST_DTL
          WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
            AND DOC_DATE >= TO_DATE(:f,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:t,'YYYY-MM-DD')+1
          UNION ALL
          SELECT 0, CR_AMT, 0, 0, 0
          FROM IAS20261.IAS_POST_DTL
          WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
            AND DOC_DATE >= TO_DATE(:f,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:t,'YYYY-MM-DD')+1
          UNION ALL
          SELECT 0, 0, NVL(p.DR_AMT,0), 0, 0
          FROM IAS20261.IAS_BILL_MST b
          JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
          WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
            AND b.BILL_DATE >= TO_DATE(:f,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:t,'YYYY-MM-DD')+1
          UNION ALL
          SELECT 0, 0, 0, CR_AMT, 0
          FROM IAS20261.IAS_POST_DTL
          WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
            AND DOC_DATE >= TO_DATE(:f,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:t,'YYYY-MM-DD')+1
        )
        SELECT NVL(SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret), 0) FROM col_trans
        """
        cur.execute(sql_col, {"f": date_from, "t": date_to})
        collection = float(cur.fetchone()[0] or 0)

        closing_bal = open_bal + net_sales_vat - collection
        if sales != 0 or collection != 0 or open_bal != 0:
            print(f"{m_str:<10} | {open_bal:15,.2f} | {net_sales_vat:15,.2f} | {collection:15,.2f} | {closing_bal:15,.2f}")

    con.close()

test_period_movement("2026")
