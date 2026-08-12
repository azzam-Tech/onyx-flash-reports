import sys
import os
from collections import defaultdict
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "privet", "onyx_reports"))
from database import get_conn

def test_lifo_aging():
    date_to_str = "2026-06-30"
    
    with get_conn() as con:
        with con.cursor() as cur:
            sql = f"""
                SELECT TO_CHAR(p.C_CODE), p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE
                FROM IAS20261.IAS_POST_DTL p
                JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND p.C_CODE IS NOT NULL
                    AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                    AND TO_CHAR(c.C_GROUP_CODE) = '141'
            """
            cur.execute(sql, {"dt": date_to_str})
            
            by_cust = defaultdict(lambda: {"debits": [], "credits": 0.0, "credit_returns": []})
            
            for c_id, ddate, dr, cr, dtype in cur.fetchall():
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                if cr > 0:
                    if dtype == 5:
                        by_cust[c_id]["credit_returns"].append((d, cr))
                    else:
                        by_cust[c_id]["credits"] += cr
                if dr > 0:
                    by_cust[c_id]["debits"].append([d, dr, dtype]) # mutable list

    limits = [30, 60, 90, 120]
    num_buckets = 5
    
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()
    
    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)

    total_b = [0.0]*5
    total_balance = 0.0

    for ccode, data in by_cust.items():
        debits = sorted(data["debits"], key=lambda x: x[0])
        credit_returns = sorted(data["credit_returns"], key=lambda x: x[0])
        total_credit = data["credits"]
        
        # LIFO Matching for Returns!
        for r_date, r_amt in credit_returns:
            remaining_return = r_amt
            # Search backwards (LIFO) for any invoice before or on the return date
            for i in range(len(debits)-1, -1, -1):
                d_date, d_amt, d_type = debits[i]
                if d_amt > 0 and d_date <= r_date:
                    if remaining_return >= d_amt:
                        remaining_return -= d_amt
                        debits[i][1] = 0.0 # fully canceled
                    else:
                        debits[i][1] -= remaining_return
                        remaining_return = 0.0
                        break
            if remaining_return > 0:
                total_credit += remaining_return # If any return left, add to general credits
                
        # Filter out 0 amount debits
        unmatched_debits = [(d[0], d[1]) for d in debits if d[1] > 0]
        
        buckets = [0.0] * num_buckets
        
        for ddate, amt in unmatched_debits:
            if total_credit >= amt:
                total_credit -= amt
            else:
                unpaid = amt - total_credit
                total_credit = 0.0
                age = (to_dt - ddate).days
                if age < 0: age = 0
                buckets[bucket_of(age)] += unpaid
                
        # Handle overpayment
        if total_credit > 0:
            buckets[0] -= total_credit

        for i in range(5):
            total_b[i] += buckets[i]
        total_balance += sum(buckets)

    print(f"Total Balance: {total_balance:,.2f}")
    print(f"0-30: {total_b[0]:,.2f}")
    print(f"31-60: {total_b[1]:,.2f}")
    print(f"61-90: {total_b[2]:,.2f}")
    print(f"91-120: {total_b[3]:,.2f}")
    print(f">120: {total_b[4]:,.2f}")

if __name__ == "__main__":
    test_lifo_aging()
