import oracledb
import os

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
conn = oracledb.connect(user='RPT_USER',password='ULT2016',dsn='100.100.1.100:1521/ORCL')
cur = conn.cursor()

try:
    cur.execute("""
        SELECT LEV_NO, PREV_I_PRICE, I_PRICE, AUD_DATE, AUD_U_ID 
        FROM IAS20261.IAS_ITEM_PRICE_HISTORY 
        WHERE I_CODE = 'SR121.' 
        ORDER BY AUD_DATE DESC 
        FETCH FIRST 5 ROWS ONLY
    """)
    rows = cur.fetchall()
    if not rows:
        print("No history found in IAS_ITEM_PRICE_HISTORY")
    else:
        for r in rows:
            print(f"Level: {r[0]}, Old Price: {r[1]}, New Price: {r[2]}, Date: {r[3]}, User: {r[4]}")
except Exception as e:
    print("Error:", e)

try:
    cur.execute("""
        SELECT LEV_NO, I_PRICE, UP_DATE, UP_U_ID
        FROM IAS20261.IAS_ITEM_PRICE
        WHERE I_CODE = 'SR121.'
    """)
    rows = cur.fetchall()
    print("\nCurrent IAS_ITEM_PRICE:")
    for r in rows:
        print(f"Level: {r[0]}, Price: {r[1]}, Update Date: {r[2]}, User: {r[3]}")
except Exception as e:
    print("Error:", e)
