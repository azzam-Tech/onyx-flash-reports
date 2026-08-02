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

def run_sales_collection_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    
    sql = """
    WITH sales_base AS (
        SELECT CC_CODE,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY CC_CODE
    ),
    returns_base AS (
        SELECT CC_CODE,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY CC_CODE
    ),
    ext_disc_base AS (
        SELECT CC_CODE, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY CC_CODE
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE) AS CC_CODE,
               SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.CC_CODE = r.CC_CODE
        FULL OUTER JOIN ext_disc_base d ON NVL(s.CC_CODE, r.CC_CODE) = d.CC_CODE
        GROUP BY NVL(NVL(s.CC_CODE, r.CC_CODE), d.CC_CODE)
    ),
    col_trans AS (
      SELECT TO_CHAR(CC_CODE) as cc_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as ext_notice, 0 as rcpt_unknown, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, 0, CR_AMT
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, CR_AMT, 0, 0, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(b.CC_CODE), 0, 0, NVL(p.DR_AMT,0) - NVL(b.DISC_AMT,0), 0, 0, 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, 0, 0, CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT TO_CHAR(CC_CODE), 0, 0, 0, 0, 0, CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT cc_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret + rcpt_unknown) as total_collection
      FROM col_trans
      GROUP BY cc_code
    )
    SELECT NVL(TO_CHAR(ns.CC_CODE), cs.cc_code) AS cc_code,
           MAX(cc.CC_A_NAME) AS cc_name,
           NVL(SUM(ns.net_sales), 0) AS net_sales,
           NVL(SUM(cs.total_collection), 0) AS total_col
    FROM net_sales_summary ns
    FULL OUTER JOIN col_summary cs ON TO_CHAR(ns.CC_CODE) = cs.cc_code
    LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = NVL(TO_CHAR(ns.CC_CODE), cs.cc_code)
    WHERE NVL(TO_CHAR(ns.CC_CODE), cs.cc_code) IS NOT NULL
    GROUP BY NVL(TO_CHAR(ns.CC_CODE), cs.cc_code)
    HAVING NVL(SUM(ns.net_sales), 0) <> 0 OR NVL(SUM(cs.total_collection), 0) <> 0
    ORDER BY SUM(ns.net_sales) DESC
    """
    
    cols = ["رمز مركز التكلفة", "اسم مركز التكلفة", "صافي المبيعات", "إجمالي التحصيل", "الفرق (المبيعات - التحصيل)", "نسبة التحصيل"]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, {"date_from": date_from, "date_to": date_to})
            for c_code, c_name, ns, col in cur.fetchall():
                ns_val = float(ns or 0.0)
                col_val = float(col or 0.0)
                diff = ns_val - col_val
                ratio_str = f"{(col_val / ns_val * 100):.1f}%" if ns_val > 0 else "0.0%"
                
                rows.append((
                    c_code,
                    c_name or ("مركز " + str(c_code)),
                    f"{ns_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff:,.2f}",
                    ratio_str
                ))
                
    return cols, rows

cols, rows = run_sales_collection_summary({}, {"year_val": "2026", "period_type": "monthly", "period_val": "6"})
print("Cols:", cols)
print("Rows count:", len(rows))
for r in rows[:5]:
    print(r)
