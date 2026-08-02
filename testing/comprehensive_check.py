import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

print("========================================")
print("1. Identifying All Items in Invoice 900002332")
print("========================================")
cur.execute("SELECT I_CODE, I_QTY FROM IAS20261.ITEM_MOVEMENT WHERE REF_NO='900002332'")
items = cur.fetchall()
print(f"Items found: {items}")

print("\n========================================")
print("2. Checking Balances in Warehouse 131 on June 25")
print("========================================")
for item_code, qty in items:
    cur.execute(f'''
        SELECT SUM(DECODE(IN_OUT, 1, I_QTY, -I_QTY)) 
        FROM IAS20261.ITEM_MOVEMENT 
        WHERE I_CODE='{item_code}' AND W_CODE=131 AND I_DATE <= TO_DATE('2026-06-25', 'YYYY-MM-DD')
    ''')
    balance = cur.fetchone()[0] or 0
    print(f"Item {item_code}: Needs {qty}, Balance on Jun 25 = {balance}")

print("\n========================================")
print("3. Checking if Ghost Transfer Source Exists in 160")
print("========================================")
for item_code, qty in items:
    cur.execute(f"SELECT COUNT(*) FROM IAS20261.ITEM_MOVEMENT WHERE I_CODE='{item_code}' AND W_CODE=160 AND IN_OUT=1 AND ROWNUM=1")
    has_source = cur.fetchone()[0]
    print(f"Item {item_code}: Can we transfer from 160? {'Yes' if has_source > 0 else 'No'}")

print("\n========================================")
print("4. Finding Potential Hidden Tables (DOC_NO=11, DOC_TYPE=4)")
print("========================================")
cur.execute("SELECT TABLE_NAME FROM ALL_TABLES WHERE OWNER='IAS20261' AND TABLE_NAME NOT LIKE '%TMP%' AND TABLE_NAME NOT LIKE '%BR%'")
tables = [r[0] for r in cur.fetchall()]

hidden_tables = []
# We will just check a few known tricky ones instead of scanning 1000 tables.
tricky_tables = ['IAS_VNDR_LMT_PUR', 'IAS_VNDR_OPEN_STOCK', 'GLS_JRNAL_MST', 'GLS_JRNAL_DTL', 'IAS_RT_PUR_DTL', 'IAS_PR_BILL_DTL']
for t in tricky_tables:
    if t in tables:
        try:
            # Check if DOC_NO exists in this table
            cur.execute(f"SELECT COUNT(*) FROM IAS20261.{t} WHERE DOC_NO=11")
            if cur.fetchone()[0] > 0:
                print(f"FOUND DOC_NO=11 in {t} (Might be related!)")
                hidden_tables.append(t)
        except:
            pass

print("\n========================================")
print("5. Checking GL Posting Status")
print("========================================")
cur.execute("SELECT POST_DATE FROM IAS20261.IAS_POST_MST WHERE REF_NO='900002332'")
post_mst = cur.fetchone()
if post_mst:
    print(f"IAS_POST_MST POST_DATE = {post_mst[0]}")
else:
    print("Not found in IAS_POST_MST")

cur.close()
conn.close()
