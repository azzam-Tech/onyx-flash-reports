import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AR8MSWIN1256'
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')

cur = con.cursor()
query = """
SELECT CUST_F_NM, CUST_L_NM, C_CMPNY_NM, BUILDING_NO, STREET, DSTRCT_NM, PBOX, ADD_NO, CR_NO, C_TAX_CODE, TEL_NO, MOBILE_NO, ADDRESS
FROM IAS20261.IAS_CASH_CUSTMR
WHERE CUST_CODE = '0560035950'
"""
try:
    cur.execute(query)
    columns = [col[0] for col in cur.description]
    rows = cur.fetchall()
    with open("cash_customer_result.txt", "w", encoding="utf-8") as f:
        for row in rows:
            for i, val in enumerate(row):
                if val is not None:
                    f.write(f"{columns[i]}: {val}\n")
            f.write("-" * 20 + "\n")
except Exception as e:
    with open("cash_customer_result.txt", "w", encoding="utf-8") as f:
        f.write(str(e))
