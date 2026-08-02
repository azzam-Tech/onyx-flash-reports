import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)

i_code = 'OS32ATVHD'
w_code = 131
dates = ['2026-06-26', '2026-06-27', '2026-06-28', '2026-06-29', '2026-06-30']

query = """
SELECT SUM(DECODE(NVL(mv.IN_OUT,0), 1, NVL(mv.I_QTY,0), -NVL(mv.I_QTY,0))) as balance
FROM IAS20261.ITEM_MOVEMENT mv
WHERE mv.I_CODE = :1
  AND mv.W_CODE = :2
  AND mv.I_DATE <= TO_DATE(:3, 'YYYY-MM-DD')
"""

cur = conn.cursor()
print("Balance for Warehouse 131 (OS32ATVHD):")
for d in dates:
    cur.execute(query, [i_code, w_code, d])
    bal = cur.fetchone()[0]
    print(f"Date: {d} -> Balance: {bal or 0}")

conn.close()
