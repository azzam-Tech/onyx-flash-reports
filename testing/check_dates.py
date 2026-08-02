import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)

cur = conn.cursor()

print("--- ITEM_MOVEMENT ---")
cur.execute("SELECT DOC_TYPE, DOC_NO, TO_CHAR(I_DATE, 'YYYY-MM-DD'), W_CODE, I_QTY FROM IAS20261.ITEM_MOVEMENT WHERE I_CODE = 'OS32ATVHD' AND DOC_NO=11 AND DOC_TYPE=4")
for r in cur.fetchall():
    print(r)

print("--- IAS_RT_PUR_MST ---")
cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='IAS_RT_PUR_MST' AND OWNER='IAS20261'")
cols = [r[0] for r in cur.fetchall()]
# Check what date columns exist
date_cols = [c for c in cols if 'DATE' in c]
print("Date Columns in IAS_RT_PUR_MST:", date_cols)

cur.execute("SELECT RT_PUR_NO, " + ", ".join(date_cols) + " FROM IAS20261.IAS_RT_PUR_MST WHERE RT_PUR_NO=11")
for r in cur.fetchall():
    print(r)

print("--- IAS_POST_MST ---")
# See if there's a POST_MST or POST_DTL for this
cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='IAS_POST_MST' AND OWNER='IAS20261'")
post_cols = [r[0] for r in cur.fetchall()]
if post_cols:
    post_date_cols = [c for c in post_cols if 'DATE' in c]
    print("Date Columns in IAS_POST_MST:", post_date_cols)
    try:
        cur.execute("SELECT DOC_NO, " + ", ".join(post_date_cols) + " FROM IAS20261.IAS_POST_MST WHERE DOC_NO_REF='11' AND DOC_TYPE=4")
        for r in cur.fetchall():
            print(r)
    except:
        pass

cur.close()
conn.close()
