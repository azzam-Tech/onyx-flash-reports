import os
import oracledb
import pandas as pd

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)

i_code = 'OS32ATVHD'

query_transfers = """
SELECT TO_CHAR(mv.I_DATE, 'YYYY-MM-DD') as i_date,
       mv.DOC_TYPE,
       mv.DOC_NO,
       mv.W_CODE,
       mv.IN_OUT,
       mv.I_QTY
FROM IAS20261.ITEM_MOVEMENT mv
WHERE mv.I_CODE = :1
  AND mv.I_DATE >= TO_DATE('2026-06-25', 'YYYY-MM-DD')
  AND mv.I_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
  AND mv.DOC_TYPE IN (7, 8)  -- Assuming 7/8 are transfers (Out/In)
ORDER BY mv.DOC_NO, mv.I_DATE
"""

cur = conn.cursor()
cur.execute(query_transfers, [i_code])
for r in cur.fetchall():
    print(r)

conn.close()
