import os
import oracledb
import itertools

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

date_from = '2026-06-01'
date_to = '2026-06-30'
rep_code = '142'

# 1. Get all base values
cur.execute("""
    SELECT 
        SUM(CASE WHEN p.DOC_TYPE=2 THEN p.CR_AMT ELSE 0 END) as rcpt_cr,
        SUM(CASE WHEN p.DOC_TYPE=1 AND p.JV_TYPE=2 THEN p.CR_AMT ELSE 0 END) as net_jrn_cr,
        SUM(CASE WHEN p.DOC_TYPE=1 AND p.JV_TYPE=1 THEN p.CR_AMT ELSE 0 END) as std_jrn_cr,
        SUM(CASE WHEN p.DOC_TYPE=5 THEN p.CR_AMT ELSE 0 END) as ret_cr,
        SUM(CASE WHEN p.DOC_TYPE=15 THEN p.CR_AMT ELSE 0 END) as ext_cr
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND NVL(p.CR_AMT,0) > 0
      AND p.DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(c.REP_CODE) = :rep
""", {"df": date_from, "dt": date_to, "rep": rep_code})
rcpt_cr, net_jrn_cr, std_jrn_cr, ret_cr, ext_cr = cur.fetchone()
rcpt_cr = rcpt_cr or 0
net_jrn_cr = net_jrn_cr or 0
std_jrn_cr = std_jrn_cr or 0
ret_cr = ret_cr or 0
ext_cr = ext_cr or 0

cur.execute("""
    SELECT SUM(NVL(p.DR_AMT,0))
    FROM IAS20261.IAS_BILL_MST b
    JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
    WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
      AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(b.REP_CODE) = :rep
""", {"df": date_from, "dt": date_to, "rep": rep_code})
cash_sales = cur.fetchone()[0] or 0

cur.execute("""
    SELECT SUM(NVL(CR_AMT,0))
    FROM IAS20261.IAS_POST_DTL
    WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0
      AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(REP_CODE) = :rep
""", {"df": date_from, "dt": date_to, "rep": rep_code})
cash_ret = cur.fetchone()[0] or 0

# Let's get TAX amounts from Tax table for these customers/receipts?
# Onyx might be separating VAT out of collections.
cur.execute("""
    SELECT SUM(NVL(TAX_AMT,0))
    FROM IAS20261.GNR_TAX_ITM_MOVMNT t
    WHERE t.DOC_TYPE=2 AND t.DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND t.DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND t.C_CODE IN (SELECT C_CODE FROM IAS20261.CUSTOMER WHERE REP_CODE=:rep)
""", {"df": date_from, "dt": date_to, "rep": rep_code})
rcpt_tax = cur.fetchone()[0] or 0

# Try all combinations of adding/subtracting these components
components = {
    'Receipts (DOC 2)': rcpt_cr,
    'Net Journals (DOC 1 JV 2)': net_jrn_cr,
    'Std Journals (DOC 1 JV 1)': std_jrn_cr,
    'Return Invoices (DOC 5)': -ret_cr,
    'Cash Sales': cash_sales,
    'Cash Returns': -cash_ret,
    'Receipt Tax': -rcpt_tax
}

print("Available Components:")
for k, v in components.items():
    print(f"  {k}: {v:,.2f}")

target = 2166028.83
print(f"\nTarget Onyx Total: {target:,.2f}")

found_combos = []
keys = list(components.keys())
for r in range(1, len(keys)+1):
    for combo in itertools.combinations(keys, r):
        s = sum([components[k] for k in combo])
        if abs(s - target) < 1.0:
            found_combos.append((combo, s))

if found_combos:
    print("\nFound exact matches!")
    for c, s in found_combos:
        print(f"  {c} -> {s:,.2f}")
else:
    print("\nNo exact matches found using broad components.")

cur.close()
conn.close()
