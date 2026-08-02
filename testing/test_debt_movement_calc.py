import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def test_debt_movement():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    date_from = "2026-01-01"
    date_to = "2026-12-31"

    print("=== 1. Testing Opening Debt query with DOC_TYPE=0 vs Without ===")
    cur.execute("""
        SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)),0) as open_bal_old
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
          AND DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD')
    """, {"date_from": date_from})
    old_open = cur.fetchone()[0]

    cur.execute("""
        SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)),0) as open_bal_new
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
          AND (DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
    """, {"date_from": date_from})
    new_open = cur.fetchone()[0]

    print(f"Old Opening Debt (without DOC_TYPE=0): {old_open:,.2f} SAR")
    print(f"New Opening Debt (with DOC_TYPE=0):    {new_open:,.2f} SAR")

    print("\n=== 2. Checking IAS_BILL_MST BILL_AMT vs VAT_AMT ===")
    cur.execute("""
        SELECT BILL_NO, BILL_AMT, DISC_AMT_MST, VAT_AMT, (NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as net_with_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DOC_TYPE IN (1,4) AND ROWNUM <= 5
    """)
    for r in cur.fetchall():
        print("  Bill row:", r)

    print("\n=== 3. Testing Debt Movement Summary for 2026 ===")
    sql = """
    WITH open_debt AS (
        SELECT TO_CHAR(CC_CODE) as grp_code,
               SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
          AND (DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(DOC_TYPE,0) = 0)
        GROUP BY TO_CHAR(CC_CODE)
    ),
    sales_base AS (
        SELECT TO_CHAR(CC_CODE) as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY TO_CHAR(CC_CODE)
    ),
    returns_base AS (
        SELECT TO_CHAR(CC_CODE) as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY TO_CHAR(CC_CODE)
    ),
    ext_disc_base AS (
        SELECT TO_CHAR(CC_CODE) as grp_code, SUM(NVL(CR_AMT,0)) as ext_disc_with_vat
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY TO_CHAR(CC_CODE)
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,
               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      SELECT TO_CHAR(CC_CODE) as grp_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, CR_AMT
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(b.CC_CODE), 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, 0, 0, CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    ),
    all_codes AS (
      SELECT grp_code FROM open_debt
      UNION
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
    )
    SELECT ac.grp_code,
           MAX(cc.CC_A_NAME) as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    """
    cur.execute(sql, {"date_from": date_from, "date_to": date_to})
    rows = cur.fetchall()
    print(f"Summary query returned {len(rows)} Cost Center rows:")
    tot_ob, tot_vat_sales, tot_no_vat, tot_col, tot_closing = 0, 0, 0, 0, 0
    for r in rows:
        ob = r[2]
        ns_vat = r[3]
        ns_no_vat = r[4]
        col = r[5]
        closing = ob + ns_vat - col
        tot_ob += ob
        tot_vat_sales += ns_vat
        tot_no_vat += ns_no_vat
        tot_col += col
        tot_closing += closing
        print(f" CC {r[0]} ({r[1]}): Open={ob:,.2f} | Sales+VAT={ns_vat:,.2f} | Col={col:,.2f} | Closing={closing:,.2f}")

    print(f"\nTOTAL COMPANY SUMMARY:")
    print(f"  المديونية الافتتاحية: {tot_ob:,.2f}")
    print(f"  المبيعات شامل الضريبة: {tot_vat_sales:,.2f}")
    print(f"  المبيعات بدون الضريبة: {tot_no_vat:,.2f}")
    print(f"  إجمالي التحصيل: {tot_col:,.2f}")
    print(f"  المديونية النهائية: {tot_closing:,.2f}")

    conn.close()

if __name__ == "__main__":
    test_debt_movement()
