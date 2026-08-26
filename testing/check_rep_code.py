import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AR8MSWIN1256'
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')

cur = con.cursor()
query = """
SELECT COUNT(*), COUNT(REP_CODE)
FROM IAS20261.IAS_CASH_CUSTMR
"""
try:
    cur.execute(query)
    row = cur.fetchone()
    print(f"Total cash customers: {row[0]}")
    print(f"Cash customers with REP_CODE: {row[1]}")
    
    query2 = """
    SELECT REP_CODE, COUNT(*)
    FROM IAS20261.IAS_CASH_CUSTMR
    WHERE REP_CODE IS NOT NULL
    GROUP BY REP_CODE
    FETCH FIRST 5 ROWS ONLY
    """
    cur.execute(query2)
    rows2 = cur.fetchall()
    print("Sample REP_CODES:", rows2)
except Exception as e:
    print(str(e))
