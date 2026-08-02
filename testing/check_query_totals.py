import oracledb

try:
    oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
except Exception as e:
    pass

conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

def test_sql(grp_by):
    year_val = "2026"
    period_type = "monthly"
    period_val = "04"
    date_from = '2026-04-01'
    date_to = '2026-04-30'
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_col_debt = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
    elif grp_by == "cc":
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_col_debt = "TO_CHAR(p.CC_CODE)"
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
    
    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col_debt}
    ),
    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
          AND (p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1)
        GROUP BY {grp_col_debt}
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
      UNION
      SELECT grp_code FROM close_debt
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col,
           NVL(SUM(c.close_bal), 0) as close_bal
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    LEFT JOIN close_debt c ON c.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    """
    
    try:
        cur.execute(sql, {"date_from": date_from, "date_to": date_to})
        print(f"SUCCESS {grp_by}: Returned {len(cur.fetchall())} rows")
    except Exception as e:
        print(f"ERROR {grp_by}: {e}")

test_sql("rep")
test_sql("cc")
