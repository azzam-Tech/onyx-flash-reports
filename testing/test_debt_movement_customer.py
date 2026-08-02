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

def test_customer_grouping():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    date_from = "2026-01-01"
    date_to = "2026-07-28"

    grp_col = "TO_CHAR(p.C_CODE)"
    grp_sales = "TO_CHAR(C_CODE)"
    grp_sales_b = "TO_CHAR(p.C_CODE)"
    grp_ret = "TO_CHAR(C_CODE)"
    join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
    name_expr = "MAX(c.C_A_NAME)"

    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND p.C_CODE IS NOT NULL
          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col}
    ),
    sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
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
      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
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
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(cs.total_collection), 0) as total_col
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    HAVING NVL(SUM(o.open_bal),0)<>0 OR NVL(SUM(ns.net_sales_vat),0)<>0 OR NVL(SUM(cs.total_collection),0)<>0
    ORDER BY NVL(SUM(o.open_bal), 0) + NVL(SUM(ns.net_sales_vat), 0) - NVL(SUM(cs.total_collection), 0) DESC
    FETCH FIRST 10 ROWS ONLY
    """
    cur.execute(sql, {"date_from": date_from, "date_to": date_to})
    rows = cur.fetchall()
    print(f"Top 10 Debt Movement rows grouped BY CUSTOMER:")
    for r in rows:
        ob, ns, col = r[2], r[3], r[4]
        closing = ob + ns - col
        print(f" Customer {r[0]} ({r[1]}): Open={ob:,.2f} | Sales+VAT={ns:,.2f} | Col={col:,.2f} | Closing={closing:,.2f}")

    # Check 1978 specifically
    cur.execute(sql.replace("FETCH FIRST 10 ROWS ONLY", ""), {"date_from": date_from, "date_to": date_to})
    for r in cur.fetchall():
        if str(r[0]) == "1978":
            ob, ns, col = r[2], r[3], r[4]
            closing = ob + ns - col
            print(f"\n🎯 Customer 1978 Debt Movement: Open={ob:,.2f} | Sales+VAT={ns:,.2f} | Col={col:,.2f} | Closing={closing:,.2f}")

    conn.close()

if __name__ == "__main__":
    test_customer_grouping()
