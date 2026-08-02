import os
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

# Exact query from app.py for collection_adopted:
sql = """
      WITH 
      all_trans AS (
        SELECT TO_CHAR(REP_CODE) as grp_code,
               CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(REP_CODE),
               0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(REP_CODE),
               0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(REP_CODE),
               0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(b.REP_CODE),
               0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
        FROM IAS20261.IAS_BILL_MST b
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(REP_CODE),
               0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(REP_CODE),
               0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT TO_CHAR(REP_CODE),
               0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      )
      SELECT grp_code,
             SUM(rcpt) rcpt, SUM(unposted_rcpt) unposted_rcpt, SUM(unposted_unknown) unposted_unknown,
             SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown
      FROM all_trans
      GROUP BY grp_code
"""

con = get_conn()
cur = con.cursor()

binds = {"date_from": "2026-06-01", "date_to": "2026-06-30"}
cur.execute(sql, binds)
rows = cur.fetchall()

tot_rcpt = sum(r[1] for r in rows)
tot_unposted_rcpt = sum(r[2] for r in rows)
tot_unposted_unknown = sum(r[3] for r in rows)
tot_net_jrn = sum(r[4] for r in rows)
tot_cash_sales = sum(r[5] for r in rows)
tot_cash_ret = sum(r[6] for r in rows)
tot_ext_notice = sum(r[7] for r in rows)
tot_rcpt_unknown = sum(r[8] for r in rows)

print(f"rcpt: {tot_rcpt:,.2f}")
print(f"unposted_rcpt: {tot_unposted_rcpt:,.2f}")
print(f"unposted_unknown: {tot_unposted_unknown:,.2f}")
print(f"net_jrn: {tot_net_jrn:,.2f}")
print(f"cash_sales: {tot_cash_sales:,.2f}")
print(f"cash_ret: {tot_cash_ret:,.2f}")
print(f"ext_notice: {tot_ext_notice:,.2f}")
print(f"rcpt_unknown: {tot_rcpt_unknown:,.2f}")

tot_commercial = tot_rcpt + tot_unposted_rcpt + tot_unposted_unknown + tot_net_jrn + tot_cash_sales - tot_cash_ret
print(f"\nTotal Commercial Collection: {tot_commercial:,.2f}")
print(f"Target expected: 18,431,211.91")
print(f"Diff: {tot_commercial - 18431211.91:,.2f}")
