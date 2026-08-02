import oracledb

oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

def run_query(sql, params={}):
    conn = oracledb.connect(user="RPT_USER", password="ULT2016", dsn="100.100.1.100:1521/ORCL")
    cursor = conn.cursor()
    cursor.execute(sql, params)
    columns = [col[0] for col in cursor.description]
    rows = cursor.fetchall()
    conn.close()
    return columns, rows

if __name__ == "__main__":
    sql = """
    SELECT 
        SUM(im.I_QTY * im.STK_COST)
    FROM IAS20261.ITEM_MOVEMENT im
    JOIN IAS20261.IAS_RT_BILL_MST r
      ON r.RT_BILL_DOC_TYPE = im.BILL_DOC_TYPE 
     AND r.RT_BILL_NO = im.DOC_NO 
     AND r.RT_BILL_SER = im.DOC_SER
    WHERE r.REP_CODE = 144
      AND im.DOC_TYPE = 2  -- Sales Return
      AND im.I_QTY > 0
      AND r.RT_BILL_DATE >= TO_DATE('2026-06-01', 'YYYY-MM-DD')
      AND r.RT_BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
    """
    try:
        cols, rows = run_query(sql)
        print("Return COGS:", rows)
    except Exception as e:
        print("Error:", e)
