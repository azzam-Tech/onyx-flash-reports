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

def get_date_range(year_str, period_type, period_val):
    try:
        yr = int(year_str)
    except:
        yr = datetime.now().year
        
    date_from = f"{yr}-01-01"
    date_to = f"{yr}-12-31"
    
    if period_type == "monthly" and period_val and period_val != "all":
        try:
            m = int(period_val)
            last_day = calendar.monthrange(yr, m)[1]
            date_from = f"{yr}-{m:02d}-01"
            date_to = f"{yr}-{m:02d}-{last_day:02d}"
        except:
            pass
    elif period_type == "quarterly" and period_val and period_val != "all":
        q_map = {
            "q1": (1, 3, 31), "1": (1, 3, 31),
            "q2": (4, 6, 30), "2": (4, 6, 30),
            "q3": (7, 9, 30), "3": (7, 9, 30),
            "q4": (10, 12, 31), "4": (10, 12, 31),
        }
        if period_val in q_map:
            sm, em, ed = q_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
    elif period_type == "semi_annual" and period_val and period_val != "all":
        h_map = {
            "h1": (1, 6, 30), "1": (1, 6, 30),
            "h2": (7, 12, 31), "2": (7, 12, 31),
        }
        if period_val in h_map:
            sm, em, ed = h_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
            
    return date_from, date_to

def test_debt_movement(year_val="2026", period_type="monthly", period_val="6", grp_by="cc"):
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    print(f"Testing for Period: {date_from} to {date_to}, grp_by: {grp_by}")
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
    else: # default cc
        grp_col = "TO_CHAR(CC_CODE)"
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col} as grp_code,
               SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL
        WHERE NVL(DOC_POST,0)=1 AND C_CODE IS NOT NULL
          AND DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD')
        GROUP BY {grp_col}
    ),
    sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      SELECT {grp_col} as grp_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, 0, CR_AMT
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, CR_AMT, 0
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
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales), 0) as net_sales,
           NVL(SUM(cs.total_collection), 0) as total_col
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
    GROUP BY ac.grp_code
    HAVING NVL(SUM(o.open_bal),0) <> 0 OR NVL(SUM(ns.net_sales),0) <> 0 OR NVL(SUM(cs.total_collection),0) <> 0
    ORDER BY ac.grp_code
    """

    con = get_conn()
    cur = con.cursor()
    cur.execute(sql, {"date_from": date_from, "date_to": date_to})

    tot_open = 0.0
    tot_sales_vat = 0.0
    tot_col = 0.0
    tot_close = 0.0

    rows = cur.fetchall()
    print(f"\nResults for June 2026 (grp_by={grp_by}), Total Rows: {len(rows)}:")
    print(f"{'Code':<10} | {'Name':<25} | {'Open Debt':<15} | {'Sales (VAT)':<15} | {'Collection':<15} | {'Closing Debt':<15}")
    print("-" * 105)

    for code, name, ob, ns, col in rows[:10]:
        ob_v = float(ob or 0)
        ns_vat_v = float(ns or 0) * 1.15
        col_v = float(col or 0)
        close_v = ob_v + ns_vat_v - col_v

        tot_open += ob_v
        tot_sales_vat += ns_vat_v
        tot_col += col_v
        tot_close += close_v

        print(f"{str(code):<10} | {str(name or ''):<25} | {ob_v:15,.2f} | {ns_vat_v:15,.2f} | {col_v:15,.2f} | {close_v:15,.2f}")

    print("-" * 105)
    full_open = sum(float(r[2] or 0) for r in rows)
    full_sales_vat = sum(float(r[3] or 0) * 1.15 for r in rows)
    full_col = sum(float(r[4] or 0) for r in rows)
    full_close = full_open + full_sales_vat - full_col
    print(f"GRAND TOTALS: Open Debt={full_open:,.2f} | Sales (VAT)={full_sales_vat:,.2f} | Collection={full_col:,.2f} | Closing Debt={full_close:,.2f}")
    con.close()

for g in ["cc", "rep"]:
    test_debt_movement("2026", "monthly", "6", g)
