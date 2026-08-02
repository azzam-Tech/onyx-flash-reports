import os
import oracledb
from itertools import combinations

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

cur.execute("""
    SELECT p.C_CODE, p.DOC_TYPE, p.JV_TYPE, SUM(NVL(p.CR_AMT,0)) as amt
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND NVL(p.CR_AMT,0) > 0
      AND p.DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(c.REP_CODE) = :rep
    GROUP BY p.C_CODE, p.DOC_TYPE, p.JV_TYPE
""", {"df": date_from, "dt": date_to, "rep": rep_code})

records = cur.fetchall()
cust_totals = {}
doc_totals = {}

for c_code, dtype, jvtype, amt in records:
    # Mimic our logic: Receipts + Net Journals - Credit Returns
    if dtype == 2:
        cust_totals[c_code] = cust_totals.get(c_code, 0) + amt
        doc_totals[f"{c_code}_{dtype}_{jvtype}"] = amt
    elif dtype == 1 and jvtype == 2:
        cust_totals[c_code] = cust_totals.get(c_code, 0) + amt
        doc_totals[f"{c_code}_{dtype}_{jvtype}"] = amt
    elif dtype == 5:
        cust_totals[c_code] = cust_totals.get(c_code, 0) - amt
        doc_totals[f"{c_code}_{dtype}_{jvtype}"] = -amt

# Add cash sales
cur.execute("""
    SELECT SUM(NVL(p.DR_AMT,0)) as amt
    FROM IAS20261.IAS_BILL_MST b
    JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
    WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
      AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(b.REP_CODE) = :rep
""", {"df": date_from, "dt": date_to, "rep": rep_code})
cash_sales = cur.fetchone()[0] or 0.0

print(f"Total Cash Sales: {cash_sales:,.2f}")

# Target Difference:
target = 357851.27

# Search for any combination of values in doc_totals or cash_sales that sum to ~target
vals = [("CASH_SALES", cash_sales)] + [(k, v) for k, v in doc_totals.items() if v != 0]

print("\nLooking for subset sum matching 357,851.27...")
found = False
for r in range(1, 4):
    for combo in combinations(vals, r):
        s = sum([x[1] for x in combo])
        if abs(s - target) < 0.1:
            print("FOUND COMBINATION:", [x[0] for x in combo], "Sum:", s)
            found = True

if not found:
    print("Could not find exact combination for 357,851.27")
    
    # What if it's 40,743.43 ?
    target2 = 40743.43
    print("\nLooking for subset sum matching 40,743.43...")
    for r in range(1, 4):
        for combo in combinations(vals, r):
            s = sum([x[1] for x in combo])
            if abs(s - target2) < 0.1:
                print("FOUND COMBINATION:", [x[0] for x in combo], "Sum:", s)

cur.close()
conn.close()
