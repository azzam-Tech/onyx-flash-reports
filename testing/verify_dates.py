import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

ref_no = '900002332'
print("--- VERIFYING INVOICE DATE CHANGES FOR REF_NO: 900002332 ---")

try:
    cur.execute(f"SELECT RT_BILL_DATE FROM IAS20261.IAS_PR_BILL_MST WHERE REF_NO='{ref_no}'")
    print(f"1. IAS_PR_BILL_MST (Invoice Date): {cur.fetchone()[0]}")
except Exception as e: print("Error 1", e)

try:
    cur.execute(f"SELECT COUNT(*), MIN(I_DATE), MAX(I_DATE) FROM IAS20261.ITEM_MOVEMENT WHERE REF_NO='{ref_no}'")
    res = cur.fetchone()
    print(f"2. ITEM_MOVEMENT (Inventory): {res[0]} items, Dates between {res[1]} and {res[2]}")
except Exception as e: print("Error 2", e)

try:
    cur.execute(f"SELECT DOC_DATE FROM IAS20261.IAS_POST_MST WHERE REF_NO='{ref_no}'")
    print(f"3. IAS_POST_MST (GL Master Date): {cur.fetchone()[0]}")
except Exception as e: print("Error 3", e)

try:
    cur.execute(f"SELECT COUNT(*), MIN(DOC_DATE) FROM IAS20261.IAS_POST_DTL WHERE REF_NO='{ref_no}'")
    res = cur.fetchone()
    print(f"4. IAS_POST_DTL (GL Details): {res[0]} lines, Date = {res[1]}")
except Exception as e: print("Error 4", e)

try:
    cur.execute(f"SELECT DOC_DATE, TAX_DUE_DATE FROM IAS20261.GNR_TAX_ITM_MOVMNT WHERE REF_NO='{ref_no}'")
    res = cur.fetchone()
    print(f"5. GNR_TAX_ITM_MOVMNT (Tax Dates): DOC_DATE={res[0]}, TAX_DUE_DATE={res[1]}")
except Exception as e: print("Error 5", e)

cur.close()
conn.close()
