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

sql = """
      WITH all_trans AS (
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END as grp_code,
               CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as inv_disc, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt, 0 as unposted_unknown
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, CR_AMT, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, 0, 0, CR_AMT
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, CR_AMT, 0, 0, 0, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(b.CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(b.C_CODE),'UNKNOWN') ELSE TO_CHAR(b.REP_CODE) END,
               0, 0, NVL(p.DR_AMT,0), NVL(b.DISC_AMT,0), 0, 0, 0, 0, 0
        FROM IAS20261.IAS_BILL_MST b
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
          AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, CR_AMT, 0, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, CR_AMT, 0, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=15 AND NVL(CR_AMT,0)>0
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        UNION ALL
        SELECT CASE WHEN :grp_by='cc' THEN TO_CHAR(CC_CODE) WHEN :grp_by='cst' THEN NVL(TO_CHAR(C_CODE),'UNKNOWN') ELSE TO_CHAR(REP_CODE) END,
               0, 0, 0, 0, 0, 0, CR_AMT, 0, 0
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      ),
      base AS (
        SELECT grp_code,
               SUM(rcpt) rcpt, SUM(net_jrn) net_jrn, SUM(cash_sales) cash_sales, SUM(inv_disc) inv_disc, SUM(cash_ret) cash_ret, SUM(ext_notice) ext_notice, SUM(rcpt_unknown) rcpt_unknown, SUM(unposted_rcpt) unposted_rcpt, SUM(unposted_unknown) unposted_unknown,
               (CASE WHEN :inc_rcpt='1' THEN (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown)) ELSE 0 END
              + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
              + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
              - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
              - CASE WHEN :inc_ext='1'  THEN SUM(ext_notice) ELSE 0 END
              + CASE WHEN :inc_rcpt='1' THEN SUM(rcpt_unknown) ELSE 0 END) AS total_col
        FROM all_trans
        GROUP BY grp_code
      )
      SELECT SUM(total_col), SUM(rcpt), SUM(unposted_rcpt), SUM(unposted_unknown), SUM(net_jrn), SUM(cash_sales), SUM(cash_ret), SUM(ext_notice), SUM(rcpt_unknown)
      FROM base
"""

con = get_conn()
cur = con.cursor()

print("Testing different parameter combinations for June 2026:")
target = 18431211.91

for inc_rcpt in ['0', '1']:
    for inc_net in ['0', '1']:
        for inc_cash in ['0', '1']:
            for inc_ret in ['0', '1']:
                for inc_ext in ['0', '1']:
                    binds = {
                        "date_from": "2026-06-01",
                        "date_to": "2026-06-30",
                        "grp_by": "rep",
                        "inc_rcpt": inc_rcpt,
                        "inc_net": inc_net,
                        "inc_cash": inc_cash,
                        "inc_ret": inc_ret,
                        "inc_ext": inc_ext
                    }
                    cur.execute(sql, binds)
                    r = cur.fetchone()
                    tot = float(r[0] or 0)
                    if abs(tot - target) < 1.0 or abs(tot - 18431211.91) < 1000:
                        print(f"MATCH FOUND! inc_rcpt={inc_rcpt}, inc_net={inc_net}, inc_cash={inc_cash}, inc_ret={inc_ret}, inc_ext={inc_ext} => Total={tot:,.2f}")

print("\nBreakdown of components for June 2026 (inc_rcpt=1, inc_net=1, inc_cash=1, inc_ret=1, inc_ext=0):")
binds_def = {
    "date_from": "2026-06-01",
    "date_to": "2026-06-30",
    "grp_by": "rep",
    "inc_rcpt": "1",
    "inc_net": "1",
    "inc_cash": "1",
    "inc_ret": "1",
    "inc_ext": "0"
}
cur.execute(sql, binds_def)
r = cur.fetchone()
print(f"Total: {r[0]:,.2f}")
print(f"Posted Receipts (rcpt): {r[1]:,.2f}")
print(f"Unposted Receipts (unposted_rcpt): {r[2]:,.2f}")
print(f"Unposted Unknown (unposted_unknown): {r[3]:,.2f}")
print(f"Net Network Journals (net_jrn): {r[4]:,.2f}")
print(f"Cash Sales (cash_sales): {r[5]:,.2f}")
print(f"Cash Returns (cash_ret): {r[6]:,.2f}")
print(f"External Notices (ext_notice): {r[7]:,.2f}")
print(f"Anonymous Receipts (rcpt_unknown): {r[8]:,.2f}")
