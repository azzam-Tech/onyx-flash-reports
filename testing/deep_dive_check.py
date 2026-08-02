import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

print("--- DIMENSION 1: SALES & COGS (Cost of Goods Sold) ---")
# Did we sell OS32ATVHD between June 26 and July 4?
cur.execute('''
    SELECT I_DATE, DOC_NO, I_QTY, STK_COST 
    FROM IAS20261.ITEM_MOVEMENT 
    WHERE I_CODE = 'OS32ATVHD' AND W_CODE = 131 
      AND I_DATE >= TO_DATE('2026-06-26', 'YYYY-MM-DD') 
      AND I_DATE <= TO_DATE('2026-07-04', 'YYYY-MM-DD')
      AND IN_OUT = -1 AND DOC_TYPE NOT IN (4)
''')
sales = cur.fetchall()
print(f"Sales/Out movements between Jun 26 - Jul 4 for OS32ATVHD: {len(sales)} movements.")
for s in sales:
    print(f"  Date: {s[0]}, Doc: {s[1]}, Qty: {s[2]}, Unit Cost: {s[3]}")

print("\n--- DIMENSION 2: TAX PERIODS & DECLARATIONS ---")
# Check if June tax period is closed in Onyx
try:
    cur.execute('''
        SELECT COUNT(*) FROM IAS20261.GNR_TAX_DECLRTION 
        WHERE TO_CHAR(F_DATE, 'YYYY-MM') <= '2026-06' AND TO_CHAR(T_DATE, 'YYYY-MM') >= '2026-06'
    ''')
    tax_closed = cur.fetchone()[0]
    print(f"Is June Tax Declaration formally closed/generated in Onyx? {'YES' if tax_closed > 0 else 'NO'}")
except Exception as e:
    print("Could not verify tax declaration status.", str(e))


print("\n--- DIMENSION 3: VENDORS & PAYMENTS (Vouchers) ---")
# Did we settle this return?
try:
    cur.execute('''
        SELECT DOC_TYPE, DOC_NO, I_DATE FROM IAS20261.IAS_V_VND_TRNS
        WHERE REF_NO = '900002332'
    ''')
    vnd_trns = cur.fetchall()
    print(f"Vendor Transactions Linked to this Return: {vnd_trns}")
except Exception as e:
    print("Could not check IAS_V_VND_TRNS.", str(e))


print("\n--- DIMENSION 4: GENERAL LEDGER (GLS) ---")
# Check if it hit the final GLS tables
try:
    cur.execute('''
        SELECT JRNAL_NO, JRNAL_DATE, PST_DATE 
        FROM IAS20261.GLS_JRNAL_MST 
        WHERE REF_NO = '900002332'
    ''')
    gls_mst = cur.fetchall()
    print(f"GLS Journal Master entries: {gls_mst}")
except Exception as e:
    print("Could not check GLS_JRNAL_MST.", str(e))

try:
    cur.execute('''
        SELECT JRNAL_NO, ACC_NO, FC_DBT_AMT, FC_CRD_AMT 
        FROM IAS20261.GLS_JRNAL_DTL 
        WHERE REF_NO = '900002332'
    ''')
    gls_dtl = cur.fetchall()
    print(f"GLS Journal Detail lines: {gls_dtl}")
except Exception as e:
    print("Could not check GLS_JRNAL_DTL.", str(e))

cur.close()
conn.close()
