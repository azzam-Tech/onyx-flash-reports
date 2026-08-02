import os
import oracledb

lib = os.environ.get("ORA_LIB_DIR", r"C:\oracle64\instantclient_19_23")
try:
    oracledb.init_oracle_client(lib_dir=lib)
except Exception as e:
    pass

# Use the exact DB connection details from app.py
DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "192.168.1.10:1521/ORCL")

conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)

def test_profit_summary():
    # This is the OLD logic for prof_summary (flawed)
    sql_old = """
      SELECT SUM(rev) as sales, SUM(cst) as cost
      FROM (SELECT NVL(d.I_QTY,0)*(NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)+NVL(d.OTHR_AMT,0)) rev,
                   NVL(d.I_QTY,0)*NVL(d.STK_COST,0) cst
            FROM IAS20261.IAS_BILL_DTL d JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
            WHERE m.BILL_DOC_TYPE IN (1,4)
              AND m.BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND m.BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1)
    """
    
    # This is the NEW logic for prof_summary (Mathematically matching the Sales report)
    sql_new = """
      WITH s AS (
        SELECT d.I_CODE,
               CASE WHEN m.BILL_DOC_TYPE IN (1,4) THEN 1 WHEN m.BILL_DOC_TYPE IN (2,5) THEN -1 ELSE 0 END as sign,
               NVL(d.I_QTY,0) as qty,
               NVL(d.I_PRICE,0) as price,
               NVL(d.DIS_AMT,0) as line_disc,
               CASE WHEN NVL(m.BILL_AMT,0)=0 THEN 0 ELSE ((NVL(d.I_QTY,0)*NVL(d.I_PRICE,0))/m.BILL_AMT)*NVL(m.DISC_AMT,0) END as hdr_disc,
               NVL(d.STK_COST,0) as unit_cost
        FROM IAS20261.IAS_BILL_DTL d
        JOIN IAS20261.IAS_BILL_MST m ON m.BILL_SER=d.BILL_SER
        WHERE m.BILL_DOC_TYPE IN (1,4,2,5)
          AND m.BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND m.BILL_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
      ),
      ext_disc AS (
        SELECT SUM(NVL(CR_AMT,0)) as ext_disc
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND DOC_DATE < TO_DATE('2026-06-30','YYYY-MM-DD')+1
          AND DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
      )
      SELECT
        (SELECT SUM(((qty * price) - line_disc - hdr_disc) * sign) FROM s) - (SELECT NVL(MAX(ext_disc),0) FROM ext_disc) as net_sales,
        (SELECT SUM(qty * unit_cost * sign) FROM s) as net_cost
      FROM DUAL
    """
    
    cur = conn.cursor()
    cur.execute(sql_old)
    old_sales, old_cost = cur.fetchone()
    
    cur.execute(sql_new)
    new_sales, new_cost = cur.fetchone()
    
    print("=== اختبار تطابق الأرباح والمبيعات (شهر 6 - 2026) ===")
    print("النتائج القديمة (التي كانت تتجاهل المردودات والخصومات):")
    print(f"1) المبيعات المحسوبة: {old_sales:,.2f}")
    print(f"2) التكلفة المحسوبة: {old_cost:,.2f}")
    print(f"3) مجمل الربح القديم: {old_sales - old_cost:,.2f}")
    print("-" * 60)
    print("النتائج الجديدة (بعد تطبيق المعادلة المحاسبية الدقيقة):")
    print(f"1) صافي المبيعات الحقيقي: {new_sales:,.2f}  <-- (يجب أن يتطابق مع تقارير المبيعات: 16,929,956.94)")
    print(f"2) تكلفة المبيعات الحقيقية (بعد المرتجعات): {new_cost:,.2f}")
    print(f"3) مجمل الربح الحقيقي والدقيق: {new_sales - new_cost:,.2f}")
    print("=" * 60)
    
    if abs(new_sales - 16929956.94) < 1:
        print("✅ نجاح باهر: إجمالي المبيعات داخل تقرير الأرباح يتطابق تماماً بنسبة 100% مع تقرير المبيعات!")
    else:
        print("❌ تحذير: لا يزال هناك فارق، المبيعات غير متطابقة.")

test_profit_summary()
