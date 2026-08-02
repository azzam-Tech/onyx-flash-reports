import os
import oracledb
from collections import defaultdict
from datetime import date, datetime

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

rep_code = '142'
date_from_str = '2026-06-01'
date_to_str = '2026-06-30'
from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

# 1. Fetch ALL transactions for Rep 142
cur.execute("""
    SELECT p.C_CODE, c.C_A_NAME, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND TO_CHAR(c.REP_CODE) = :rep
      AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
""", {"rep": rep_code})

by_c = defaultdict(lambda: {'name': '', 'debits': [], 'credits_hist': 0.0, 'credits_june': 0.0})
for ccode, cname, doc_date, dr, cr, dtype in cur.fetchall():
    d = doc_date.date()
    dr = float(dr)
    cr = float(cr)
    by_c[ccode]['name'] = cname
    
    if dr > 0:
        # We only care about debits BEFORE the end of June
        if d <= to_dt:
            by_c[ccode]['debits'].append((d, dr))
            
    if cr > 0 and dtype == 2: # Onyx standard logic only uses Receipts!
        if from_dt <= d <= to_dt:
            by_c[ccode]['credits_june'] += cr
        elif d < from_dt:
            by_c[ccode]['credits_hist'] += cr

dropped_amounts = {}
total_dropped = 0.0

for ccode, data in by_c.items():
    col = data['credits_june']
    if col == 0: continue
    
    # Calculate pos (Debits in 0-30 bucket) -> between 2026-06-01 and 2026-06-30 approx
    # Actually, Onyx calculates PER_NO from PAID_DATE. Let's assume paid_date = to_dt.
    pos = 0.0
    older_debits = 0.0
    for d, amt in data['debits']:
        age = (to_dt - d).days
        if 0 <= age <= 30:
            pos += amt
        elif age > 30:
            older_debits += amt
            
    # Onyx crlim (remaining unpaid older debt before June)
    # This is roughly: older_debits - credits_hist
    # But wait, credits_hist could pay off pos too if it was paid in advance?
    # Usually crlim is the total remaining balance before the June collections.
    # Total historical balance = (pos + older_debits) - credits_hist
    tot_bal_before_june = max(0.0, (pos + older_debits) - data['credits_hist'])
    crlim = tot_bal_before_june
    
    # If the customer has no new debts in 0-30 days
    if pos <= 0:
        # Onyx drops any collection that exceeds the crlim!
        excess = max(0.0, col - crlim)
        if excess > 0:
            dropped_amounts[ccode] = {'name': data['name'], 'dropped': excess, 'col': col, 'crlim': crlim}
            total_dropped += excess
    else:
        # Even if pos > 0, wait, if pos > 0 it does NOT drop it.
        pass

print(f"Calculated Total Dropped by Onyx: {total_dropped:,.2f}")
for c, info in dropped_amounts.items():
    print(f"Customer {c} ({info['name']}): Dropped {info['dropped']:,.2f} (June Collection: {info['col']}, Remaining Debt: {info['crlim']})")

import csv
csv_path = r'C:\Users\amarn\OneDrive\Desktop\تحليل_المبلغ_المستبعد_40743.csv'
with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['رقم العميل', 'اسم العميل', 'تحصيلات العميل في شهر 6', 'إجمالي ديون العميل القديمة (أونكس)', 'المبلغ المستبعد (الزائد)'])
    for c, info in dropped_amounts.items():
        writer.writerow([c, info['name'], f"{info['col']:.2f}", f"{info['crlim']:.2f}", f"{info['dropped']:.2f}"])
    writer.writerow(['', '', '', 'الإجمالي:', f"{total_dropped:.2f}"])

cur.close()
conn.close()
