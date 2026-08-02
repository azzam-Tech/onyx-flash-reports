import oracledb
import os

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def check_banks():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    cur.execute("SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER='IAS20261' AND TABLE_NAME LIKE '%BANK%'")
    print("Bank tables in IAS20261:", cur.fetchall())

    cur.execute("""
        SELECT TABLE_NAME 
        FROM ALL_TABLES 
        WHERE OWNER LIKE 'IAS%' AND (TABLE_NAME LIKE '%BANK%' OR TABLE_NAME LIKE '%BNK%')
    """)
    print("All Bank tables:", cur.fetchall())

    # Test joining S_EMP with S_EMP_BNK
    sql_emp = """
        SELECT e.EMP_NO,
               NVL(TRIM(e.FRST_L_NM || ' ' || e.SCND_L_NM || ' ' || e.THRD_L_NM || ' ' || e.LST_L_NM), e.EMP_L_NM) as emp_name,
               CASE WHEN e.CTZNSHP = 1 THEN 'سعودي' ELSE 'مقيم' END as ctz,
               NVL(TO_CHAR(e.SCL_SCRTY_NO), '-') as gosi_no,
               NVL(e.INSRNCE_NO, '-') as ins_no,
               NVL(e.EMP_INSRNCE_AMT, 0) as ins_amt,
               CASE WHEN e.SLRY_PAY_WAY = 2 THEN 'تحويل بنكي' WHEN e.SLRY_PAY_WAY = 1 THEN 'نقدي' ELSE 'أخرى' END as pay_way,
               b.BNK_NO,
               b.BNK_IBAN
        FROM IAS20261.S_EMP e
        LEFT JOIN IAS20261.S_EMP_BNK b ON b.EMP_NO = e.EMP_NO AND NVL(b.SLRY_FLG, 1) = 1
        WHERE NVL(e.INACTIVE, 0) = 0
        ORDER BY e.EMP_NO
    """
    cur.execute(sql_emp)
    rows = cur.fetchall()
    print(f"\nFetched {len(rows)} active employees. Sample 10:")
    for r in rows[:10]:
        print(" ", r)

    conn.close()

if __name__ == "__main__":
    check_banks()
