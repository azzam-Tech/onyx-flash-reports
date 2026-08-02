import os
import oracledb
import csv

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

# 1. Get ALL Receipts for Rep 142 from our logic (IAS_POST_DTL)
cur.execute("""
    SELECT p.C_CODE, c.C_A_NAME, p.DOC_NO, SUM(NVL(p.CR_AMT,0))
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0
      AND p.DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD')
      AND p.DOC_DATE < TO_DATE('2026-07-01','YYYY-MM-DD')
      AND TO_CHAR(c.REP_CODE)='142'
    GROUP BY p.C_CODE, c.C_A_NAME, p.DOC_NO
""")
our_receipts = {}
for ccode, cname, doc_no, amt in cur.fetchall():
    our_receipts[str(doc_no)] = {'ccode': ccode, 'name': cname, 'amt': amt}

# 2. Get Onyx's Collections for Rep 142 from IAS_CRLIMIT_TMP
cur.execute("""
    SELECT DOC_NO_REF, SUM(NVL(DR_AMT,0))
    FROM IAS20261.IAS_CRLIMIT_TMP
    WHERE DOC_TYPE_REF=2
      AND PAID_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD')
      AND PAID_DATE < TO_DATE('2026-07-01','YYYY-MM-DD')
      AND TO_CHAR(REP_CODE)='142'
    GROUP BY DOC_NO_REF
""")
onyx_receipts = {}
for doc_no_ref, amt in cur.fetchall():
    onyx_receipts[str(doc_no_ref)] = amt

# 3. Find the differences
missing_in_onyx = []
total_missing = 0.0

for doc_no, info in our_receipts.items():
    our_amt = info['amt']
    onyx_amt = onyx_receipts.get(doc_no, 0.0)
    diff = our_amt - onyx_amt
    
    # We only care if Onyx excluded or reduced it (diff > 0.01)
    if diff > 0.01:
        missing_in_onyx.append({
            'doc_no': doc_no,
            'ccode': info['ccode'],
            'name': info['name'],
            'our_amt': our_amt,
            'onyx_amt': onyx_amt,
            'diff': diff
        })
        total_missing += diff

# Check what we found
print(f"Total Missing in Onyx (should be ~40,743.43): {total_missing}")

# Write to CSV
csv_path = r'C:\Users\amarn\OneDrive\Desktop\تفصيل_مبلغ_40743_المستبعد.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["رقم السند", "رقم العميل", "اسم العميل", "مبلغ السند الفعلي", "المبلغ المعتمد في أونكس", "الفرق (المستبعد)"])
    
    for row in missing_in_onyx:
        writer.writerow([row['doc_no'], row['ccode'], row['name'], f"{row['our_amt']:.2f}", f"{row['onyx_amt']:.2f}", f"{row['diff']:.2f}"])
        
    writer.writerow([])
    writer.writerow(["", "", "", "", "الإجمالي المستبعد:", f"{total_missing:.2f}"])

cur.close()
conn.close()
