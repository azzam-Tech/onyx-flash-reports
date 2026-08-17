import oracledb
import os

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

conn = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')
cur = conn.cursor()

# Get some sample expenses
query = """
SELECT d.DOC_NO, d.DOC_DATE, d.A_CODE, a.A_NAME, d.DOC_TYPE, d.DR_AMT, d.DOC_DESC 
FROM IAS_POST_DTL d
LEFT JOIN ACCOUNT a ON d.A_CODE = a.A_CODE
WHERE (d.DOC_DESC LIKE '%صيان%' OR d.DOC_DESC LIKE '%سيار%') 
  AND d.DR_AMT > 0 
  AND d.A_CODE LIKE '3%'
FETCH FIRST 10 ROWS ONLY
"""
cur.execute(query)
rows = cur.fetchall()

print("--- Sample Expenses ---")
for r in rows:
    print(f"Doc No: {r[0]}, Date: {r[1].strftime('%Y-%m-%d') if r[1] else ''}, Account: {r[2]} ({r[3]}), DocType: {r[4]}, Amount: {r[5]}, Desc: {r[6]}")

cur.close()
conn.close()
