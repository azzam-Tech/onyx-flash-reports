import os
import oracledb
from datetime import datetime
from collections import defaultdict

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

date_from_str = '2026-06-01'
date_to_str = '2026-06-30'
target_rep = '142'

from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

def bucket_of(age):
    if age <= 30:  return 0
    if age <= 60:  return 1
    if age <= 90:  return 2
    if age <= 120: return 3
    return 4

# Fetch Debits WITH their original Invoice Rep Code!
# We join with IAS_BILL_MST to get the true REP_CODE of the invoice.
# But for opening balances or journals, we might use the customer's rep.
cur.execute("""
    SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, 
           NVL(TO_CHAR(b.REP_CODE), TO_CHAR(c.REP_CODE)) as inv_rep
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    LEFT JOIN IAS20261.IAS_BILL_MST b ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4
    WHERE NVL(p.DOC_POST,0)=1 AND TO_CHAR(c.REP_CODE) = :rep
      AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
""", {"rep": target_rep})

byc = defaultdict(lambda: {"debits": [], "credits": []})
for ccode, ddate, dr, cr, dtype, inv_rep in cur.fetchall():
    d = ddate.date()
    dr = float(dr)
    cr = float(cr)
    
    if cr > 0 and dtype == 2:  # Only receipts
        byc[str(ccode)]["credits"].append((d, cr))
    
    if dr > 0:
        byc[str(ccode)]["debits"].append((d, dr, inv_rep))

total_for_142 = 0.0
total_for_others = 0.0
other_reps = defaultdict(float)

for ccode, evs in byc.items():
    debits  = sorted(evs["debits"], key=lambda x: x[0])
    credits = sorted(evs["credits"], key=lambda x: x[0])
    
    dcum = 0.0; dint = []
    for (d, dr, inv_rep) in debits:
        lo = dcum; dcum += dr; dint.append((lo, dcum, d, inv_rep))
        
    ccum = 0.0
    for (d, cr) in credits:
        clo = ccum; ccum += cr; chi = ccum
        if not (from_dt <= d <= to_dt):
            continue
        
        hi_cr = max(clo, chi)
        lo_cr = min(clo, chi)
        
        for (lo, hi, idate, inv_rep) in dint:
            if lo < hi_cr and hi > lo_cr:
                amt = min(hi_cr, hi) - max(lo_cr, lo)
                if amt <= 0: continue
                
                if inv_rep == target_rep:
                    total_for_142 += amt
                else:
                    total_for_others += amt
                    other_reps[inv_rep] += amt

print(f"Receipts paying off {target_rep}'s invoices: {total_for_142:,.2f}")
print(f"Receipts paying off OTHER Reps invoices: {total_for_others:,.2f}")
for r, amt in other_reps.items():
    print(f"  Rep {r}: {amt:,.2f}")

cur.close()
conn.close()
