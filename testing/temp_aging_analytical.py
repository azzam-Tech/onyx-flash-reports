def run_perf_aging_analytical(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    
    rep_code = args.get("rep_code")
    
    inc_rcpt = str(args.get("inc_rcpt", "1")) == "1"
    inc_net  = str(args.get("inc_net", "1")) == "1"
    inc_cash = str(args.get("inc_cash", "1")) == "1"
    inc_ret  = str(args.get("inc_ret", "1")) == "1"
    inc_ext  = False
    
    if rep_code:
        rep_code = rep_code.split(" - ")[0].strip()
    
    date_from_str = args.get("date_from", "")
    date_to_str = args.get("date_to", "")
    if not date_from_str: date_from_str = "2026-06-01"
    if not date_to_str: date_to_str = "2026-06-30"
    
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT C_CODE, REP_CODE, C_A_NAME FROM IAS20261.CUSTOMER")
            cust_rep = {}
            cust_names = {}
            for c, r, n in cur.fetchall():
                cust_rep[str(c)] = str(r)
                cust_names[str(c)] = str(n)
                
            cur.execute("SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN")
            rep_name = {str(c): n for c, n in cur.fetchall()}

            # Get Cash Sales for the period (no C_CODE needed)
            sql_cash = """
                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))
                FROM IAS20261.IAS_BILL_MST b
                JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(b.REP_CODE)
            """
            cur.execute(sql_cash, {"df": date_from_str, "dt": date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}

            # Get Cash Returns without C_CODE
            sql_ret_null = """
                SELECT NVL(TO_CHAR(REP_CODE), 'UNKNOWN'), SUM(NVL(CR_AMT,0))
                FROM IAS20261.IAS_POST_DTL
                WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0
                  AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
                GROUP BY TO_CHAR(REP_CODE)
            """
            cur.execute(sql_ret_null, {"df": date_from_str, "dt": date_to_str})
            cash_ret_null_by_rep = {r: float(amt) for r, amt in cur.fetchall()}

            # Fetch relevant debits and credits from IAS_POST_DTL
            sql = """
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE NVL(p.DOC_POST,0)=1
                  AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
            """
            cur.execute(sql)
            byc = defaultdict(lambda: {"debits": [], "credits": []})
            
            for ccode, ddate, dr, cr, dtype, jvtype, acode in cur.fetchall():
                if ccode is None: continue
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                
                valid_cr = 0.0
                if cr > 0:
                    if dtype == 2 and inc_rcpt:  # rcpt
                        valid_cr = cr
                    elif dtype == 1 and jvtype == 2 and inc_net:  # net_jrn
                        valid_cr = cr
                    elif dtype == 5 and acode and str(acode).startswith('111') and inc_ret:  # cash_ret
                        valid_cr = -cr
                    elif dtype == 15 and inc_ext:  # ext_notice
                        valid_cr = -cr
                
                if dr > 0:
                    byc[str(ccode)]["debits"].append((d, dr))
                if valid_cr != 0:
                    byc[str(ccode)]["credits"].append((d, valid_cr))

    def bucket_of(age):
        if age <= 30:  return 0
        if age <= 60:  return 1
        if age <= 90:  return 2
        if age <= 120: return 3
        return 4

    cust_results = defaultdict(lambda: {"b": [0.0]*5, "total": 0.0})

    for ccode, evs in byc.items():
        r_code = cust_rep.get(ccode)
        if not r_code: continue
        if rep_code and r_code != rep_code: continue

        debits  = sorted(evs["debits"], key=lambda x: x[0])
        credits = sorted(evs["credits"], key=lambda x: x[0])
        
        dcum = 0.0; dint = []
        for (d, dr) in debits:
            lo = dcum; dcum += dr; dint.append((lo, dcum, d))
        ddates = [x[0] for x in debits]
        
        ccum = 0.0
        for (d, cr) in credits:
            clo = ccum; ccum += cr; chi = ccum
            if not (from_dt <= d <= to_dt):
                continue
            
            # Handle negative credits (deductions)
            lo_cr, hi_cr = min(clo, chi), max(clo, chi)
            is_negative = (cr < 0)
            
            cust_results[ccode]["total"] += cr
            
            for (lo, hi, idate) in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0: continue
                    
                    if is_negative: amt = -amt
                    
                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days
                    
                    cust_results[ccode]["b"][bucket_of(age)] += amt

    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                cust_results["CASH_SALES_" + str(r_code)]["total"] += c_sales
                cust_results["CASH_SALES_" + str(r_code)]["b"][0] += c_sales

    # Subtract cash returns without C_CODE
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and r_code != 'UNKNOWN': continue
            if c_ret > 0:
                cust_results["CASH_SALES_" + str(r_code)]["total"] -= c_ret
                cust_results["CASH_SALES_" + str(r_code)]["b"][0] -= c_ret

    cols = ["رقم العميل", "اسم العميل", "0-30", "31-60", "61-90", "91-120", "أكثر من 120", "إجمالي التحصيل"]
    rows = []
    
    for ccode, data in cust_results.items():
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        
        if str(ccode).startswith("CASH_SALES_"):
            c_name = "مبيعات نقدية (للمندوب)"
            disp_code = "-"
        else:
            c_name = cust_names.get(str(ccode), str(ccode))
            disp_code = str(ccode)
            
        row = (
            disp_code,
            c_name,
            f"{data['b'][0]:,.2f}",
            f"{data['b'][1]:,.2f}",
            f"{data['b'][2]:,.2f}",
            f"{data['b'][3]:,.2f}",
            f"{data['b'][4]:,.2f}",
            f"{data['total']:,.2f}"
        )
        rows.append(row)
        
    rows.sort(key=lambda x: float(x[7].replace(',','')), reverse=True)
    return cols, rows
