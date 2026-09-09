import oracledb
import os

oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
dsn = oracledb.makedsn("100.100.1.100", 1521, service_name="ORCL")

try:
    conn = oracledb.connect(user="ULT", password="ULT2017", dsn=dsn)
    cur = conn.cursor()
    
    # Query all packages and procedures in IAS20261
    sql = """
        SELECT OBJECT_NAME, OBJECT_TYPE
        FROM ALL_OBJECTS 
        WHERE OWNER = 'IAS20261'
          AND OBJECT_TYPE IN ('PACKAGE', 'PROCEDURE')
        ORDER BY OBJECT_TYPE, OBJECT_NAME
    """
    cur.execute(sql)
    rows = cur.fetchall()
    
    output_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\onyx_procedures_list.txt"
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(f"Total Objects Found: {len(rows)}\n")
        f.write("="*40 + "\n")
        for r in rows:
            f.write(f"[{r[1]}] {r[0]}\n")
            
    print(f"Successfully wrote {len(rows)} procedures/packages to onyx_procedures_list.txt")
except Exception as e:
    print("Error:", e)
finally:
    if 'conn' in locals():
        conn.close()
