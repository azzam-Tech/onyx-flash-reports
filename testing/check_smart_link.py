import sys
import os
from collections import defaultdict
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "privet", "onyx_reports"))
from database import get_conn

def test_smart_link_aging():
    date_to_str = "2026-06-30"
    
    with get_conn() as con:
        with con.cursor() as cur:
            # Query debits and normal credits
            sql = f"""
                SELECT TO_CHAR(p.C_CODE), p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.DOC_NO, p.DOC_SER
                FROM IAS20261.IAS_POST_DTL p
                JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND p.C_CODE IS NOT NULL
                    AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                    AND TO_CHAR(c.C_GROUP_CODE) = '141'
            """
            cur.execute(sql, {"dt": date_to_str})
            
            by_cust = defaultdict(lambda: {"debits": [], "credits": 0.0, "returns": []})
            
            for c_id, ddate, dr, cr, dtype, doc_no, doc_ser in cur.fetchall():
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                if cr > 0:
                    if dtype == 5:
                        by_cust[c_id]["returns"].append({"date": d, "amt": cr, "doc_no": doc_no, "doc_ser": doc_ser, "linked_inv": None})
                    else:
                        by_cust[c_id]["credits"] += cr
                if dr > 0:
                    # store doc_no, doc_ser to link
                    by_cust[c_id]["debits"].append({"date": d, "amt": dr, "type": dtype, "doc_no": doc_no, "doc_ser": doc_ser})

            # Now, fetch the links for returns
            sql_links = f"""
                SELECT DISTINCT p.DOC_NO as RET_NO, p.DOC_SER as RET_SER, d.BILL_NO, d.BILL_SER
                FROM IAS20261.IAS_POST_DTL p
                JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
                JOIN IAS20261.IAS_RT_BILL_DTL d 
                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER
                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 
                  AND TO_CHAR(c.C_GROUP_CODE) = '141'
                  AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                  AND d.BILL_NO IS NOT NULL
            """
            cur.execute(sql_links, {"dt": date_to_str})
            links = {}
            for r_no, r_ser, b_no, b_ser in cur.fetchall():
                links[(r_no, r_ser)] = (b_no, b_ser)
                
            # Apply links to returns
            for c_id, data in by_cust.items():
                for ret in data["returns"]:
                    k = (ret["doc_no"], ret["doc_ser"])
                    if k in links:
                        ret["linked_inv"] = links[k]

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
        debits = sorted(data["debits"], key=lambda x: x["date"])
        returns = sorted(data["returns"], key=lambda x: x["date"])
        total_credit = data["credits"]
        
        # Exact Link Matching for Returns!
        for ret in returns:
            r_amt = ret["amt"]
            linked_inv = ret["linked_inv"]
            matched = False
            if linked_inv:
                b_no, b_ser = linked_inv
                # Find the invoice
                for deb in debits:
                    if deb["amt"] > 0 and deb["doc_no"] == b_no and deb["doc_ser"] == b_ser:
                        # Apply return to this invoice
                        if r_amt >= deb["amt"]:
                            r_amt -= deb["amt"]
                            deb["amt"] = 0.0
                        else:
                            deb["amt"] -= r_amt
                            r_amt = 0.0
                            matched = True
                            break
                        if r_amt <= 0:
                            matched = True
                            break
                            
            if r_amt > 0:
                # If no link, or return amount exceeded invoice amount, add to general credits
                total_credit += r_amt
                
        # Filter out 0 amount debits
        unmatched_debits = [(d["date"], d["amt"]) for d in debits if d["amt"] > 0]
        
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
    test_smart_link_aging()
