import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

items = ['OS32ATVHD', 'OS70LW4KM', 'OS32SATVHD']

print("--- COST VARIANCE CHECK (June 26 to July 4) ---")
for item in items:
    cur.execute(f'''
        SELECT MIN(STK_COST), MAX(STK_COST), AVG(STK_COST), COUNT(*)
        FROM IAS20261.ITEM_MOVEMENT 
        WHERE I_CODE = '{item}' 
          AND I_DATE >= TO_DATE('2026-06-25', 'YYYY-MM-DD') 
          AND I_DATE <= TO_DATE('2026-07-05', 'YYYY-MM-DD')
    ''')
    res = cur.fetchone()
    min_c = res[0]
    max_c = res[1]
    avg_c = res[2]
    cnt = res[3]
    
    if cnt > 0:
        variance = max_c - min_c
        print(f"Item: {item}")
        print(f"  Movements: {cnt}")
        print(f"  Min Cost: {min_c:.4f}, Max Cost: {max_c:.4f}, Avg: {avg_c:.4f}")
        print(f"  Difference (Max - Min): {variance:.4f}")
        if variance > 1.0:
            print("  ⚠️ WARNING: Cost fluctuated during this period!")
        else:
            print("  ✅ SAFE: Cost is highly stable.")
    else:
        print(f"Item: {item} - No movements in this exact window.")
    print("-")

cur.close()
conn.close()
