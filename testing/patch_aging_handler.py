import os

handler_code = """
def run_cust_aging(rpt, args):
    from collections import defaultdict
    from datetime import datetime
    from database import get_conn
    
    rep_code = args.get("rep_code")
    c_code = args.get("c_code")
    if rep_code: rep_code = rep_code.split(" - ")[0].strip()
    if c_code: c_code = c_code.split(" - ")[0].strip()
    
    date_to_str = args.get("date_to", "")
    if not date_to_str: date_to_str = "2026-07-31"
    
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

    with get_conn() as con:
        with con.cursor() as cur:
            # 1. Fetch customers
            sql_cust = "SELECT TO_CHAR(C_CODE), MAX(C_A_NAME), MAX(TO_CHAR(REP_CODE)) FROM IAS20261.CUSTOMER GROUP BY TO_CHAR(C_CODE)"
            cur.execute(sql_cust)
            customers = {}
            for row in cur.fetchall():
                customers[row[0]] = {"name": row[1] or "", "rep": row[2] or ""}
                
            # 2. Fetch debts and payments
            binds = {"dt": date_to_str}
            filters = []
            if rep_code: 
                filters.append("TO_CHAR(p.REP_CODE) = :rep")
                binds["rep"] = rep_code
            if c_code:
                filters.append("TO_CHAR(p.C_CODE) = :cst")
                binds["cst"] = c_code
                
            filter_str = " AND " + " AND ".join(filters) if filters else ""
            
            sql = f\"\"\"
                SELECT TO_CHAR(p.C_CODE), p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0)
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND p.C_CODE IS NOT NULL
                    AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                    {filter_str}
            \"\"\"
            cur.execute(sql, binds)
            
            by_cust = defaultdict(lambda: {"debits": [], "credits": 0.0})
            
            for c_id, ddate, dr, cr in cur.fetchall():
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                if cr > 0:
                    by_cust[c_id]["credits"] += cr
                if dr > 0:
                    by_cust[c_id]["debits"].append((d, dr))
                    
    # 3. Dynamic Buckets
    aging_ranges_str = args.get("aging_ranges", "2,30,60,90,120")
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(",") if x.strip().isdigit()])
        if not limits: limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]

    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0: bucket_labels.append("0")
        elif prev == 0: bucket_labels.append(f"0-{lim}")
        else: bucket_labels.append(f"{prev+1}-{lim}")
        prev = lim
    bucket_labels.append(f"أكثر من {limits[-1]}")
    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim: return idx
        return len(limits)

    cols = ["كود العميل", "اسم العميل", "المندوب"] + bucket_labels + ["الإجمالي"]
    rows = []
    
    # 4. Apply FIFO
    for c_id, data in by_cust.items():
        if rep_code and customers.get(c_id, {}).get("rep") != rep_code: continue
        
        debits = sorted(data["debits"], key=lambda x: x[0])
        total_credit = data["credits"]
        
        buckets = [0.0] * num_buckets
        total_unpaid = 0.0
        
        for ddate, amt in debits:
            if total_credit >= amt:
                total_credit -= amt
            else:
                unpaid = amt - total_credit
                total_credit = 0.0
                
                # calc age
                age = (to_dt - ddate).days
                if age < 0: age = 0
                
                buckets[bucket_of(age)] += unpaid
                total_unpaid += unpaid
                
        if round(total_unpaid, 2) > 0:
            nm = customers.get(c_id, {}).get("name", "")
            rp = customers.get(c_id, {}).get("rep", "")
            
            formatted_b = [f"{x:,.2f}" for x in buckets]
            row = (
                c_id,
                nm,
                rp,
                *formatted_b,
                f"{total_unpaid:,.2f}"
            )
            rows.append(row)
            
    # Sort by total unpaid descending
    rows.sort(key=lambda r: float(r[-1].replace(',', '')), reverse=True)
            
    return {"cols": cols, "rows": rows}
"""

file_path = 'privet/onyx_reports/report_handlers.py'
with open(file_path, 'a', encoding='utf-8') as f:
    f.write("\n" + handler_code + "\n")
print("Added run_cust_aging to report_handlers.py")
