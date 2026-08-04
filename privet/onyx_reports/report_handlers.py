from database import get_conn
from config import get_target_amount

def run_perf_aging_fifo(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    
    is_dynamic = (rpt.get("id") == "perf_aging_dynamic")
    
    rep_code = args.get("rep_code")
    if is_dynamic:
        inc_rcpt = str(args.get("inc_rcpt", "1")) == "1"
        inc_net  = str(args.get("inc_net", "1")) == "1"
        inc_cash = str(args.get("inc_cash", "1")) == "1"
        inc_ret  = str(args.get("inc_ret", "1")) == "1"
        inc_ext  = False
    else:
        inc_rcpt = True
        inc_net  = False
        inc_cash = False
        inc_ret  = False
        inc_ext  = False
    if rep_code:
        rep_code = rep_code.split(" - ")[0].strip()
    
    date_from_str = args.get("date_from", "")
    date_to_str = args.get("date_to", "")
    if not date_from_str: date_from_str = "2026-07-01"
    if not date_to_str: date_to_str = "2026-07-31"
    
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT C_CODE, REP_CODE FROM IAS20261.CUSTOMER")
            cust_rep = {str(c): str(r) for c, r in cur.fetchall()}
                
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
            rep_filter = " AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)" if rep_code else ""
            binds_fifo = {}
            if rep_code: binds_fifo["rep_code"] = rep_code
            sql = f"""
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
                    AND p.C_CODE IS NOT NULL
                    {rep_filter}
            """
            cur.execute(sql, binds_fifo)
            byc = defaultdict(lambda: {"debits": [], "credits": []})
            
            for ccode, ddate, dr, cr, dtype, jvtype, acode in cur.fetchall():
                if ccode is None: continue
                d = ddate.date() if hasattr(ddate, "date") else ddate
                dr = float(dr)
                cr = float(cr)
                
                valid_cr = 0.0
                if cr > 0:
                    if not is_dynamic:
                        valid_cr = cr
                    else:
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

    aging_ranges_str = args.get("aging_ranges", "2,30,60,90,120")
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(",") if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]

    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append("0")
        elif prev == 0:
            bucket_labels.append(f"0-{lim}")
        else:
            bucket_labels.append(f"{prev+1}-{lim}")
        prev = lim
    bucket_labels.append(f"أكثر من {limits[-1]}")

    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)

    rep_results = defaultdict(lambda: {"cust_count": set(), "b": [0.0]*num_buckets, "total": 0.0})

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
            
            rep_results[r_code]["cust_count"].add(ccode)
            rep_results[r_code]["total"] += cr
            
            for (lo, hi, idate) in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0: continue
                    
                    if is_negative: amt = -amt
                    
                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days
                    
                    rep_results[r_code]["b"][bucket_of(age)] += amt

    # Add cash sales
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code: continue
            if c_sales > 0:
                rep_results[r_code]["total"] += c_sales
                rep_results[r_code]["b"][0] += c_sales

    # Subtract cash returns without C_CODE
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and r_code != 'UNKNOWN': continue
            if c_ret > 0:
                rep_results[r_code]["total"] -= c_ret
                rep_results[r_code]["b"][0] -= c_ret

    cols = ["كود المندوب", "اسم المندوب", "عدد العملاء"] + bucket_labels + ["المبلغ المحصل"]
    rows = []
    
    for r_code, data in rep_results.items():
        # Avoid showing empty rows if net collection is 0 and buckets are 0
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        formatted_b = [f"{x:,.2f}" for x in data["b"]]
        row = (
            r_code,
            rep_name.get(r_code, r_code),
            len(data["cust_count"]),
        ) + tuple(formatted_b) + (f"{data['total']:,.2f}",)
        rows.append(row)
        
    tot_idx = len(cols) - 1
    rows.sort(key=lambda x: float(str(x[tot_idx]).replace(',','')), reverse=True)
    return cols, rows

MAIN_WAREHOUSES_CODES = ["105", "103", "121", "122", "118", "108", "119"]

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
    else:
        return ["تنبيه"], [("الرجاء اختيار المندوب أولاً من القائمة المنسدلة لعرض التقرير التحليلي.", "", "", "", "", "", "", "")]
    
    date_from_str = args.get("date_from", "")
    date_to_str = args.get("date_to", "")
    if not date_from_str: date_from_str = "2026-07-01"
    if not date_to_str: date_to_str = "2026-07-31"
    
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
            rep_filter = " AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)" if rep_code else ""
            binds_fifo = {}
            if rep_code: binds_fifo["rep_code"] = rep_code
            sql = f"""
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
                    AND p.C_CODE IS NOT NULL
                    {rep_filter}
            """
            cur.execute(sql, binds_fifo)
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

    aging_ranges_str = args.get("aging_ranges", "2,30,60,90,120")
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(",") if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]

    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append("0")
        elif prev == 0:
            bucket_labels.append(f"0-{lim}")
        else:
            bucket_labels.append(f"{prev+1}-{lim}")
        prev = lim
    bucket_labels.append(f"أكثر من {limits[-1]}")

    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)

    cust_results = defaultdict(lambda: {"b": [0.0]*num_buckets, "total": 0.0})

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

    cols = ["رقم العميل", "اسم العميل"] + bucket_labels + ["إجمالي التحصيل"]
    rows = []
    
    for ccode, data in cust_results.items():
        if round(data["total"], 2) == 0 and sum(abs(x) for x in data["b"]) < 0.01: continue
        
        if str(ccode).startswith("CASH_SALES_"):
            c_name = "مبيعات نقدية (للمندوب)"
            disp_code = "-"
        else:
            c_name = cust_names.get(str(ccode), str(ccode))
            disp_code = str(ccode)
            
        formatted_b = [f"{x:,.2f}" for x in data["b"]]
        row = (
            disp_code,
            c_name,
        ) + tuple(formatted_b) + (f"{data['total']:,.2f}",)
        rows.append(row)
        
    tot_idx = len(cols) - 1
    rows.sort(key=lambda x: float(str(x[tot_idx]).replace(',','')), reverse=True)
    return cols, rows


def run_main_wh_movement(rpt, args):
    from collections import defaultdict
    date_from_str = args.get("date_from", "2026-01-01")
    date_to_str = args.get("date_to", "2026-12-31")
    i_code_str = args.get("i_code", "").split(" - ")[0].strip()
    
    print(f"[DEBUG WH] date_from: {date_from_str}, date_to: {date_to_str}, i_code: {i_code_str}")
    
    wh_mapping = {
        "105": "مخزن عيضة",
        "103": "مخزن حسام",
        "121": "مخزن المنصورية",
        "122": "مخزن الدمام",
        "118": "مخزن تبوك",
        "108": "مخزن الجنوب",
        "119": "مخزن جده"
    }
    
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                codes_str = ",".join(MAIN_WAREHOUSES_CODES)
                cur.execute(f"SELECT W_CODE, W_NAME FROM IAS20261.WAREHOUSE_DETAILS WHERE W_CODE IN ({codes_str})")
                for w_code, w_name in cur.fetchall():
                    wh_mapping[str(w_code)] = w_name
    except Exception as e:
        print("Error fetching warehouse names dynamically:", e)

    wh_codes = MAIN_WAREHOUSES_CODES
    
    item_filter = ""
    if i_code_str:
        item_filter = " AND dt.I_CODE = :icode "
    
    sql = f"""
        SELECT
            dt.I_CODE,
            MAX(m.I_NAME),
            dt.W_CODE,
            SUM(NVL(dt.I_QTY, 0)) AS net_qty
        FROM IAS20261.ITEM_MOVEMENT dt
        LEFT JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = dt.I_CODE
        WHERE dt.I_DATE >= TO_DATE(:df, 'YYYY-MM-DD')
          AND dt.I_DATE < TO_DATE(:dt, 'YYYY-MM-DD') + 1
          AND dt.W_CODE IN (105, 103, 121, 122, 118, 108, 119)
          AND dt.IN_OUT = -1
          {item_filter}
        GROUP BY dt.I_CODE, dt.W_CODE
        HAVING SUM(NVL(dt.I_QTY, 0)) > 0
    """
    
    params = {"df": date_from_str, "dt": date_to_str}
    if i_code_str:
        params["icode"] = i_code_str
    
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, params)
            results = cur.fetchall()
            print(f"[DEBUG WH] Query returned {len(results)} raw grouped rows.")
            
    items = defaultdict(lambda: {"name": "", "total": 0, "wh": defaultdict(float)})
    for i_code, i_name, w_code, net_qty in results:
        code_str = str(w_code)
        items[str(i_code)]["name"] = str(i_name)
        items[str(i_code)]["total"] += float(net_qty)
        items[str(i_code)]["wh"][code_str] += float(net_qty)
        
    cols = ["كود الصنف", "اسم الصنف", "الإجمالي"] + [wh_mapping[c] for c in wh_codes]
    rows = []
    for code, data in items.items():
        row = [code, data["name"], f"{data['total']:,.2f}"]
        for w_code in wh_codes:
            row.append(f"{data['wh'][w_code]:,.2f}")
        rows.append(tuple(row))
        
    rows.sort(key=lambda x: float(x[2].replace(',', '')), reverse=True)
    return cols, rows

def add_total_row(cols, rows, rpt_id=""):
    if not rows:
        return cols, rows
        
    totals = [0.0] * len(cols)
    is_numeric = [False] * len(cols)
    has_values = [False] * len(cols)
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        
        if any(x in col_name for x in ['كود', 'تاريخ', 'هاتف', 'code', 'no', 'date', 'phone', 'عنوان', 'ملاحظات', 'بيان', 'مستند', 'رمز', 'نسبة', 'اسم', 'حساب', 'رقم']):
            continue
        if col_name in ('الرصيد', 'balance'):
            continue
            
        for row in rows:
            val = row[col_idx]
            if val is None or val == "": 
                continue
            if isinstance(val, (int, float)):
                is_numeric[col_idx] = True
                break
            if isinstance(val, str):
                try:
                    float(val.replace(',', ''))
                    is_numeric[col_idx] = True
                    break
                except ValueError:
                    pass
                    
    for row in rows:
        if row and len(row) > 1 and str(row[1]).strip() == "رصيد افتتاحي":
            continue
        if row and len(row) > 3 and str(row[3]).strip() in ("رصيد افتتاحي", "الرصيد الإفتتاحي"):
            continue
        for col_idx in range(len(cols)):
            if is_numeric[col_idx]:
                val = row[col_idx]
                if val is not None and val != "":
                    if isinstance(val, str):
                        try:
                            totals[col_idx] += float(val.replace(',', ''))
                            has_values[col_idx] = True
                        except ValueError:
                            pass
                    else:
                        totals[col_idx] += float(val)
                        has_values[col_idx] = True
                        
    total_row = []
    has_total_label = False
    
    for col_idx in range(len(cols)):
        col_name = str(cols[col_idx]).lower().strip()
        if col_name == 'الرصيد' or col_name == 'balance':
            total_row.append(str(rows[-1][col_idx]) if rows else "")
        elif is_numeric[col_idx]:
            val = totals[col_idx]
            if not has_values[col_idx] or val == 0:
                total_row.append("")
            else:
                total_row.append(f"{val:,.2f}")
        else:
            if not has_total_label:
                total_row.append("الإجمالي")
                has_total_label = True
            else:
                total_row.append("")
                
    if rpt_id == "debt_movement_summary" and len(cols) >= 11:
        try:
            t_open = totals[2] if is_numeric[2] else 0.0
            t_sales_vat = totals[3] if is_numeric[3] else 0.0
            t_col = totals[4] if is_numeric[4] else 0.0
            t_sales_no_vat = totals[8] if is_numeric[8] else 0.0
            t_target = totals[9] if is_numeric[9] else 0.0
            
            if t_target > 0:
                total_row[10] = f"{t_target - t_sales_no_vat:,.2f}"
            
            t_due = t_open + t_sales_vat
            if t_due > 0:
                total_row[6] = f"{(t_col / t_due) * 100:,.2f}%"
        except Exception:
            pass

    summary_rows = [tuple(total_row)]
    
    # Net Profit summary rows for true_income_statement
    if rpt_id == "true_income_statement" and len(cols) == 8:
        mv_dr = totals[4] if is_numeric[4] else 0.0
        mv_cr = totals[5] if is_numeric[5] else 0.0
        period_net = mv_cr - mv_dr
        
        bal_dr = totals[6] if is_numeric[6] else 0.0
        bal_cr = totals[7] if is_numeric[7] else 0.0
        final_net = bal_cr - bal_dr
        
        p_row = ["", "رصيد الفترة صافي الربح", "", "", "", "", "", ""]
        if period_net >= 0:
            p_row[5] = f"{period_net:,.2f}"
        else:
            p_row[4] = f"{abs(period_net):,.2f}"
        summary_rows.append(tuple(p_row))
        
        f_row = ["", "الرصيد النهائي صافي الربح", "", "", "", "", "", ""]
        if final_net >= 0:
            f_row[7] = f"{final_net:,.2f}"
        else:
            f_row[6] = f"{abs(final_net):,.2f}"
        summary_rows.append(tuple(f_row))
                
    return cols, summary_rows + rows

def get_date_range(year_str, period_type, period_val):
    try:
        yr = int(year_str)
    except:
        yr = datetime.now().year
        
    date_from = f"{yr}-01-01"
    date_to = f"{yr}-12-31"
    
    if period_type == "monthly" and period_val and period_val != "all":
        try:
            m = int(period_val)
            import calendar
            last_day = calendar.monthrange(yr, m)[1]
            date_from = f"{yr}-{m:02d}-01"
            date_to = f"{yr}-{m:02d}-{last_day:02d}"
        except:
            pass
    elif period_type == "quarterly" and period_val and period_val != "all":
        q_map = {
            "q1": (1, 3, 31), "1": (1, 3, 31),
            "q2": (4, 6, 30), "2": (4, 6, 30),
            "q3": (7, 9, 30), "3": (7, 9, 30),
            "q4": (10, 12, 31), "4": (10, 12, 31),
        }
        if period_val in q_map:
            sm, em, ed = q_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
    elif period_type == "semi_annual" and period_val and period_val != "all":
        h_map = {
            "h1": (1, 6, 30), "1": (1, 6, 30),
            "h2": (7, 12, 31), "2": (7, 12, 31),
        }
        if period_val in h_map:
            sm, em, ed = h_map[period_val]
            date_from = f"{yr}-{sm:02d}-01"
            date_to = f"{yr}-{em:02d}-{ed:02d}"
            
    return date_from, date_to

def run_sales_collection_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ""
    rep_filter = ""
    
    if grp_by == "rep":
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_col = "TO_CHAR(REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(b.C_CODE)"
        grp_col = "TO_CHAR(C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
        rep_filter = "AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)"
    elif grp_by == "customer":
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(b.C_CODE)"
        grp_col = "TO_CHAR(C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
        rep_filter = "AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "NVL(ns.grp_code, cs.grp_code)"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
    else: # default cc
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_col = "TO_CHAR(CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = NVL(ns.grp_code, cs.grp_code)"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f"""
    WITH sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as sales
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0)) - SUM(NVL(DISC_AMT_MST,0)) as returns
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, ROUND(SUM(NVL(CR_AMT,0)) / 1.15, 2) as ext_disc
        FROM IAS20261.IAS_POST_DTL
        WHERE DOC_TYPE = 15 AND NVL(CR_AMT,0) > 0 AND NVL(DOC_POST,0) = 1
          AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales, 0)) - SUM(NVL(r.returns, 0)) - SUM(NVL(d.ext_disc, 0)) AS net_sales
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      -- Posted receipts with customer
      SELECT {grp_col} as grp_code, CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Unposted receipts with customer
      SELECT {grp_col}, 0, 0, 0, 0, CR_AMT
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Network journals with customer
      SELECT {grp_col}, 0, CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND NVL(CR_AMT,0)>0 AND C_CODE IS NOT NULL
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Cash Sales (posted DOC_TYPE=4)
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      -- Cash Returns (posted DOC_TYPE=5)
      SELECT {grp_col}, 0, 0, 0, CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL
      WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND NVL(CR_AMT,0)>0
        AND DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    )
    SELECT NVL(ns.grp_code, cs.grp_code) AS item_code,
           {name_expr} AS item_name,
           NVL(SUM(ns.net_sales), 0) AS net_sales,
           NVL(SUM(cs.total_collection), 0) AS total_col
    FROM net_sales_summary ns
    FULL OUTER JOIN col_summary cs ON ns.grp_code = cs.grp_code
    {join_table}
    WHERE NVL(ns.grp_code, cs.grp_code) IS NOT NULL
    GROUP BY NVL(ns.grp_code, cs.grp_code)
    HAVING NVL(SUM(ns.net_sales), 0) <> 0 OR NVL(SUM(cs.total_collection), 0) <> 0
    ORDER BY NVL(ns.grp_code, cs.grp_code)
    """
    
    cols = [code_label, name_label, "صافي المبيعات", "المبيعات شامل الضريبة", "إجمالي التحصيل", "الفرق (المبيعات - التحصيل)", "نسبة التحصيل", "الهدف"]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            params = {"date_from": date_from, "date_to": date_to}
            if ":rep_code" in sql: params["rep_code"] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, ns, col in cur.fetchall():
                ns_val = float(ns or 0.0)
                ns_vat_val = ns_val * 1.15
                col_val = float(col or 0.0)
                diff = ns_val - col_val
                ratio_str = f"{(col_val / ns_val * 100):.1f}%" if ns_val > 0 else "0.0%"
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ns_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff:,.2f}",
                    ratio_str,
                    target_str
                ))
                
    return cols, rows

def run_debt_movement_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    rep_code = args.get("rep_code", "")
    if not rep_code:
        rep_code = None
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ""
    rep_filter = ""
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_col_debt = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_col = "TO_CHAR(p.C_CODE)"
        grp_col_debt = "TO_CHAR(NVL(p.C_CODE, p.C_V_CODE))"
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(p.C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
        rep_filter = "AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(p.DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(p.DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
        grp_col_debt = grp_col
    else: # default cc
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_col_debt = grp_col
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"

    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col_debt}
    ),
    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
          AND (p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1)
        GROUP BY {grp_col_debt}
    ),
    sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,
               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    ),
    all_codes AS (
      SELECT grp_code FROM open_debt
      UNION
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
      UNION
      SELECT grp_code FROM close_debt
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col,
           NVL(SUM(cd.close_bal), 0) as close_bal
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    LEFT JOIN close_debt cd ON cd.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
      {rep_filter}
      GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    """

    cols = [
        code_label,
        name_label,
        "المديونية الافتتاحية",
        "صافي المبيعات شامل الضريبة",
        "إجمالي التحصيل",
        "الفرق (المبيعات - التحصيل)",
        "نسبة التحصيل",
        "المديونية النهائية",
        "إجمالي المبيعات بدون الضريبة",
        "الهدف",
        "الفرق (الهدف - المبيعات)"
    ]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            params = {"date_from": date_from, "date_to": date_to}
            if ":rep_code" in sql: params["rep_code"] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, open_b, ns_vat, ns_no_vat, col, close_b in cur.fetchall():
                ob_val = float(open_b or 0.0)
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                closing_val = float(close_b or 0.0)
                
                total_due = ob_val + ns_vat_val
                if total_due > 0:
                    col_ratio = (col_val / total_due) * 100
                else:
                    col_ratio = 0.0
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                diff_sales_col = ns_vat_val - col_val
                diff_target_sales = target_val - ns_no_vat_val if target_val > 0 else 0.0
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{diff_sales_col:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    target_str,
                    f"{diff_target_sales:,.2f}" if target_val > 0 else ""
                ))
                
    return cols, rows

def run_net_debt_movement_summary(rpt, args):
    year_val = args.get("year_val", "2026")
    period_type = args.get("period_type", "monthly")
    period_val = args.get("period_val", "all")
    grp_by = args.get("grp_by", "cc")
    rep_code = args.get("rep_code", "")
    if not rep_code:
        rep_code = None
    exclude_suppliers = args.get("exclude_suppliers", "1")
    
    date_from, date_to = get_date_range(year_val, period_type, period_val)
    rep_filter = ""
    rep_filter = ""
    
    if grp_by == "rep":
        grp_col = "TO_CHAR(p.REP_CODE)"
        grp_col_debt = "TO_CHAR(p.REP_CODE)"
        grp_sales = "TO_CHAR(REP_CODE)"
        grp_sales_b = "TO_CHAR(b.REP_CODE)"
        grp_ret = "TO_CHAR(REP_CODE)"
        join_table = "LEFT JOIN IAS20261.SALES_MAN sm ON TO_CHAR(sm.REPRS_CODE) = ac.grp_code"
        name_expr = "MAX(sm.REPRS_A_NAME)"
        code_label = "كود المندوب"
        name_label = "اسم المندوب"
    elif grp_by == "customer":
        grp_col = "TO_CHAR(p.C_CODE)"
        grp_col_debt = "TO_CHAR(NVL(p.C_CODE, p.C_V_CODE))"
        grp_sales = "TO_CHAR(C_CODE)"
        grp_sales_b = "TO_CHAR(p.C_CODE)"
        grp_ret = "TO_CHAR(C_CODE)"
        join_table = "LEFT JOIN IAS20261.CUSTOMER c ON TO_CHAR(c.C_CODE) = ac.grp_code"
        name_expr = "MAX(c.C_A_NAME)"
        code_label = "كود العميل"
        name_label = "اسم العميل"
        rep_filter = "AND (:rep_code IS NULL OR TO_CHAR(c.REP_CODE) = :rep_code)"
    elif grp_by == "period":
        if period_type == "quarterly":
            grp_sales = "'Q' || TO_CHAR(BILL_DATE, 'Q')"
            grp_sales_b = "'Q' || TO_CHAR(b.BILL_DATE, 'Q')"
            grp_col = "'Q' || TO_CHAR(p.DOC_DATE, 'Q')"
            grp_ret = "'Q' || TO_CHAR(RT_BILL_DATE, 'Q')"
        elif period_type == "semi_annual":
            grp_sales = "CASE WHEN TO_CHAR(BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_sales_b = "CASE WHEN TO_CHAR(b.BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_col = "CASE WHEN TO_CHAR(p.DOC_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
            grp_ret = "CASE WHEN TO_CHAR(RT_BILL_DATE, 'MM') <= '06' THEN 'النصف الأول (H1)' ELSE 'النصف الثاني (H2)' END"
        else: # monthly or annual
            grp_sales = "TO_CHAR(BILL_DATE, 'YYYY-MM')"
            grp_sales_b = "TO_CHAR(b.BILL_DATE, 'YYYY-MM')"
            grp_col = "TO_CHAR(p.DOC_DATE, 'YYYY-MM')"
            grp_ret = "TO_CHAR(RT_BILL_DATE, 'YYYY-MM')"
        join_table = ""
        name_expr = "ac.grp_code"
        code_label = "الفترة الزمنية"
        name_label = "البيان"
        grp_col_debt = grp_col
    else: # default cc
        grp_col = "TO_CHAR(p.CC_CODE)"
        grp_col_debt = grp_col
        grp_sales = "TO_CHAR(CC_CODE)"
        grp_sales_b = "TO_CHAR(b.CC_CODE)"
        grp_ret = "TO_CHAR(CC_CODE)"
        join_table = "LEFT JOIN IAS20261.COST_CENTERS cc ON TO_CHAR(cc.CC_CODE) = ac.grp_code"
        name_expr = "MAX(cc.CC_A_NAME)"
        code_label = "رمز مركز التكلفة"
        name_label = "اسم مركز التكلفة"


    supplier_filter = "AND p.C_CODE IS NOT NULL AND TO_CHAR(p.A_CODE) LIKE '121%'" if exclude_suppliers == "1" else "AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)"
    
    sql = f"""
    WITH open_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as open_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 {supplier_filter}

          AND (p.DOC_DATE < TO_DATE(:date_from, 'YYYY-MM-DD') OR NVL(p.DOC_TYPE,0) = 0)
        GROUP BY {grp_col_debt}
    ),
    close_debt AS (
        SELECT {grp_col_debt} as grp_code,
               SUM(NVL(p.DR_AMT,0) - NVL(p.CR_AMT,0)) as close_bal
        FROM IAS20261.IAS_POST_DTL p
        WHERE NVL(p.DOC_POST,0)=1 {supplier_filter}
          AND (p.DOC_DATE < TO_DATE(:date_to, 'YYYY-MM-DD')+1)
        GROUP BY {grp_col_debt}
    ),
    sales_base AS (
        SELECT {grp_sales} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as sales_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as sales_no_vat
        FROM IAS20261.IAS_BILL_MST
        WHERE BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_sales}
    ),
    returns_base AS (
        SELECT {grp_ret} as grp_code,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0) + NVL(VAT_AMT,0)) as returns_with_vat,
               SUM(NVL(BILL_AMT,0) - NVL(DISC_AMT_MST,0)) as returns_no_vat
        FROM IAS20261.IAS_RT_BILL_MST
        WHERE RT_BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND RT_BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
          AND RT_BILL_DOC_TYPE IN (1,2,3,4,5,6,7,8)
        GROUP BY {grp_ret}
    ),
    ext_disc_base AS (
        SELECT {grp_col} as grp_code, SUM(NVL(p.CR_AMT,0)) as ext_disc_with_vat
        FROM IAS20261.IAS_POST_DTL p
        WHERE p.DOC_TYPE = 15 AND NVL(p.CR_AMT,0) > 0 AND NVL(p.DOC_POST,0) = 1
          AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') 
          AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
        GROUP BY {grp_col}
    ),
    net_sales_summary AS (
        SELECT NVL(NVL(s.grp_code, r.grp_code), d.grp_code) AS grp_code,
               SUM(NVL(s.sales_with_vat, 0)) - SUM(NVL(r.returns_with_vat, 0)) - SUM(NVL(d.ext_disc_with_vat, 0)) AS net_sales_vat,
               SUM(NVL(s.sales_no_vat, 0)) - SUM(NVL(r.returns_no_vat, 0)) - SUM(ROUND(NVL(d.ext_disc_with_vat, 0)/1.15, 2)) AS net_sales_no_vat
        FROM sales_base s
        FULL OUTER JOIN returns_base r ON s.grp_code = r.grp_code
        FULL OUTER JOIN ext_disc_base d ON NVL(s.grp_code, r.grp_code) = d.grp_code
        GROUP BY NVL(NVL(s.grp_code, r.grp_code), d.grp_code)
    ),
    col_trans AS (
      SELECT {grp_col} as grp_code, p.CR_AMT as rcpt, 0 as net_jrn, 0 as cash_sales, 0 as cash_ret, 0 as unposted_rcpt
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, 0, p.CR_AMT
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, p.CR_AMT, 0, 0, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=1 AND p.JV_TYPE=2 AND NVL(p.CR_AMT,0)>0 AND p.C_CODE IS NOT NULL
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_sales_b}, 0, 0, NVL(p.DR_AMT,0), 0, 0
      FROM IAS20261.IAS_BILL_MST b
      JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
      WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
        AND b.BILL_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
      UNION ALL
      SELECT {grp_col}, 0, 0, 0, p.CR_AMT, 0
      FROM IAS20261.IAS_POST_DTL p
      WHERE NVL(p.DOC_POST,0)=1 AND p.DOC_TYPE=5 AND p.A_CODE LIKE '111%' AND NVL(p.CR_AMT,0)>0
        AND p.DOC_DATE >= TO_DATE(:date_from,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:date_to,'YYYY-MM-DD')+1
    ),
    col_summary AS (
      SELECT grp_code,
             SUM(rcpt + unposted_rcpt + net_jrn + cash_sales - cash_ret) as total_collection
      FROM col_trans
      GROUP BY grp_code
    ),
    all_codes AS (
      SELECT grp_code FROM open_debt
      UNION
      SELECT grp_code FROM net_sales_summary
      UNION
      SELECT grp_code FROM col_summary
      UNION
      SELECT grp_code FROM close_debt
    )
    SELECT ac.grp_code,
           {name_expr} as grp_name,
           NVL(SUM(o.open_bal), 0) as open_bal,
           NVL(SUM(ns.net_sales_vat), 0) as net_sales_vat,
           NVL(SUM(ns.net_sales_no_vat), 0) as net_sales_no_vat,
           NVL(SUM(cs.total_collection), 0) as total_col,
           NVL(SUM(cd.close_bal), 0) as close_bal
    FROM all_codes ac
    LEFT JOIN open_debt o ON o.grp_code = ac.grp_code
    LEFT JOIN net_sales_summary ns ON ns.grp_code = ac.grp_code
    LEFT JOIN col_summary cs ON cs.grp_code = ac.grp_code
    LEFT JOIN close_debt cd ON cd.grp_code = ac.grp_code
    {join_table}
    WHERE ac.grp_code IS NOT NULL
      {rep_filter}
      GROUP BY ac.grp_code
    ORDER BY ac.grp_code
    """

    cols = [
        code_label,
        name_label,
        "المديونية الافتتاحية",
        "صافي المبيعات شامل الضريبة",
        "إجمالي التحصيل",
        "نسبة التحصيل",
        "المديونية النهائية",
        "إجمالي المبيعات بدون الضريبة",
        "الهدف"
    ]
    rows = []
    
    with get_conn() as con:
        with con.cursor() as cur:
            params = {"date_from": date_from, "date_to": date_to}
            if ":rep_code" in sql: params["rep_code"] = rep_code
            cur.execute(sql, params)
            for c_code, c_name, open_b, ns_vat, ns_no_vat, col, close_b in cur.fetchall():
                ob_val = float(open_b or 0.0)
                ns_vat_val = float(ns_vat or 0.0)
                ns_no_vat_val = float(ns_no_vat or 0.0)
                col_val = float(col or 0.0)
                closing_val = float(close_b or 0.0)
                
                total_due = ob_val + ns_vat_val
                if total_due > 0:
                    col_ratio = (col_val / total_due) * 100
                else:
                    col_ratio = 0.0
                
                target_val = get_target_amount(year_val, period_type, period_val, grp_by, c_code)
                target_str = f"{target_val:,.2f}" if target_val > 0 else ""
                
                rows.append((
                    c_code,
                    c_name or str(c_code),
                    f"{ob_val:,.2f}",
                    f"{ns_vat_val:,.2f}",
                    f"{col_val:,.2f}",
                    f"{col_ratio:,.2f}%",
                    f"{closing_val:,.2f}",
                    f"{ns_no_vat_val:,.2f}",
                    target_str
                ))
                
    return cols, rows


def run_sql_report(rpt, args):
    sql = rpt["sql"]
    binds = {}
    for p in rpt["params"]:
        pname = p["name"]
        raw = args.get(pname, p.get("default", ""))
        val = str(raw).split(" - ")[0].strip() if raw else ""
        if p.get("type") in ("date", "month"):
            if not val:
                if callable(p.get("get_default")):
                    val = p["get_default"]()
                elif p.get("default"):
                    val = p["default"]
                else:
                    val = get_default_date_from() if "from" in pname else get_default_date_to()
        binds[pname] = val
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute(sql, binds)
            cols = [d[0] for d in cur.description] if cur.description else []
            rows = cur.fetchall()
            sort_col = args.get("sort_col")
            sort_dir = args.get("sort_dir", "desc")
            if sort_col and sort_col in cols and rows:
                col_idx = cols.index(sort_col)
                def parse_sort_val(r):
                    v = r[col_idx]
                    if v is None: return float('-inf') if sort_dir == 'asc' else float('inf')
                    if isinstance(v, (int, float)): return v
                    if isinstance(v, str):
                        try: return float(v.replace(',', ''))
                        except: return v
                    return str(v)
                rows.sort(key=parse_sort_val, reverse=(sort_dir == 'desc'))
            return cols, rows

def run_report(rpt, args):
    if "fn" in rpt:
        func = globals().get(rpt["fn"])
        if func:
            cols, rows = func(rpt, args)
            return add_total_row(cols, rows, rpt.get('id', ''))
    if not rpt.get("sql"):
        return [], []
    cols, rows = run_sql_report(rpt, args)
    return add_total_row(cols, rows, rpt.get('id', ''))

def jv_options():
    global _JV_CACHE
    if _JV_CACHE is not None:
        return _JV_CACHE
    opts = [["","الكل"]]
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute("""SELECT p.JV_TYPE, MAX(j.JV_NAME) nm
                    FROM IAS20261.IAS_POST_DTL p
                    LEFT JOIN IAS20261.JV_TYPES j ON j.JV_TYPE=p.JV_TYPE
                    WHERE p.C_CODE IS NOT NULL AND NVL(p.DOC_POST,0)=1
                    GROUP BY p.JV_TYPE ORDER BY COUNT(*) DESC""")
                for t, nm in cur.fetchall():
                    if t is None: continue
                    code = str(int(t))
                    label = nm or ("بدون نوع" if int(t)==0 else "نوع "+code)
                    opts.append([code, label])
        _JV_CACHE = opts
        return _JV_CACHE
    except Exception:
        return [["","الكل"],["1","قيد يومية"],["2","قيود الشبكة"],["4","قيود دائنون"],["9","قيد ضريبي"],["11","رصيد افتتاحي للعملاء"],["0","بدون نوع"]]

_LK_CACHE = {}
def lookups(name):
    if name in _LK_CACHE:
        return _LK_CACHE[name]
    q = {
      "rep_code": "SELECT REPRS_CODE, REPRS_A_NAME FROM IAS20261.SALES_MAN WHERE REPRS_CODE IS NOT NULL ORDER BY REPRS_A_NAME",
      "c_code":   "SELECT C_CODE, C_A_NAME FROM IAS20261.CUSTOMER WHERE NVL(INACTIVE,0)=0 AND C_CODE IS NOT NULL ORDER BY C_A_NAME",
      "v_code":   "SELECT V_CODE, MAX(V_NAME) FROM IAS20261.IAS_PI_BILL_MST WHERE V_CODE IS NOT NULL GROUP BY V_CODE ORDER BY MAX(V_NAME)",
      "i_code":   "SELECT I_CODE, I_NAME FROM IAS20261.IAS_ITM_MST WHERE I_CODE IS NOT NULL ORDER BY I_NAME",
      "a_code":   "SELECT A_CODE, A_NAME FROM IAS20261.ACCOUNT WHERE A_CODE IS NOT NULL ORDER BY A_CODE",
    }.get(name)
    if not q:
        return []
    out = []
    try:
        with get_conn() as con:
            with con.cursor() as cur:
                cur.execute(q)
                for code, nm in cur.fetchall():
                    if code is None:
                        continue
                    out.append(("%s - %s" % (str(code).strip(), (nm or "").strip())).strip(" -"))
        _LK_CACHE[name] = out
        return out
    except Exception:
        return []

STYLE = """<style>

/* Hide scrollbars completely while keeping scroll functionality */
::-webkit-scrollbar { display: none; }
* { -ms-overflow-style: none; scrollbar-width: none; }
.quick-dates { display: flex; gap: 12px; flex-wrap: wrap; margin-top: -12px; margin-bottom: -8px; align-items: center; justify-content: center; }
.quick-dates .btn-sm { background: #ffffff; border: 2px solid #e2e8f0; color: var(--ink-dark); padding: 10px 20px; border-radius: 14px; font-size: 14px; font-weight: 700; cursor: pointer; transition: all 0.25s ease; box-shadow: 0 2px 4px rgba(0,0,0,0.02); }
.quick-dates .btn-sm:hover { border-color: var(--primary); color: var(--primary); transform: translateY(-3px); box-shadow: 0 10px 15px -3px rgba(79, 70, 229, 0.15), 0 4px 6px -2px rgba(79, 70, 229, 0.05); background: #fefeff; }
.quick-dates .btn-sm:active, .quick-dates .btn-sm.active { background: var(--primary); border-color: var(--primary); color: #ffffff; transform: translateY(-1px); box-shadow: 0 6px 12px -2px rgba(79, 70, 229, 0.4); }
@import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;500;600;700;800&family=Inter:wght@400;500;600;700;800&display=swap');
:root {
  --bg: #f4f5f8;
  --sb-bg: #ffffff;
  --card-bg: #ffffff;
  --primary: #4f46e5;
  --primary-hover: #4338ca;
  --ink: #64748b;
  --ink-dark: #1e293b;
  --line: #f1f5f9;
  --sh: 0 10px 40px rgba(0,0,0,0.04);
}
body { background: var(--bg); color: var(--ink); font-family: 'Cairo', 'Inter', sans-serif; direction: rtl; margin:0; padding:0; box-sizing:border-box; }
* { box-sizing: border-box; margin:0; padding:0; }
a { text-decoration: none; }
.card { background: var(--card-bg); border-radius: 20px; padding: 24px; box-shadow: var(--sh); }
.app { display: flex; min-height: 100vh; padding: 20px; gap: 24px; }
.sb { width: 260px; background: var(--sb-bg); border-radius: 24px; display: flex; flex-direction: column; padding: 30px 20px; flex-shrink: 0; box-shadow: var(--sh); position: sticky; top: 20px; max-height: calc(100vh - 40px); overflow-y: auto; }
.brand { display: flex; align-items: center; gap: 12px; font-size: 24px; font-weight: 800; color: var(--ink-dark); margin-bottom: 40px; }
.brand svg { width: 32px; height: 32px; fill: var(--primary); }
.menu-lbl { font-size: 11px; font-weight: 700; color: #94a3b8; margin: 20px 10px 10px; letter-spacing: 1px; }
.sb a { display: flex; align-items: center; gap: 14px; padding: 14px 20px; border-radius: 16px; color: var(--ink); font-weight: 600; font-size: 15px; margin-bottom: 8px; transition: all 0.3s; }
.sb a:hover { background: #f8fafc; color: var(--ink-dark); }
.sb a.on { background: var(--primary); color: #fff; box-shadow: 0 10px 20px rgba(79, 70, 229, 0.25); }
.sb svg { width: 22px; height: 22px; stroke: currentColor; fill: none; stroke-width: 2; }
.sb a.on svg { stroke: #fff; }

.main { flex: 1; min-width: 0; display: flex; flex-direction: column; }
.top { display: flex; align-items: center; padding: 10px 0 30px; gap: 15px; }
.logo { display:none; }
.ttl { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.wrap { display: flex; flex-direction: column; gap: 24px; }

.pills { display: flex; gap: 12px; flex-wrap: wrap; }
.pill { background: var(--card-bg); border-radius: 12px; padding: 12px 24px; font-size: 14px; font-weight: 600; color: var(--ink); box-shadow: var(--sh); transition: 0.3s; }
.pill:hover { transform: translateY(-2px); color: var(--primary); }
.pill.on { background: var(--primary); color: #fff; box-shadow: 0 10px 20px rgba(79, 70, 229, 0.25); }

.filters { background: var(--card-bg); border-radius: 20px; padding: 24px; display: grid; grid-template-columns: repeat(auto-fit, minmax(180px, 1fr)); gap: 20px; align-items: end; box-shadow: var(--sh); margin-bottom: 0; }
.filters label { display: block; font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 8px; }
.filters input, .filters select { width: 100%; padding: 12px 16px; border: 1px solid var(--line); border-radius: 12px; font-family: inherit; font-size: 14px; font-weight: 500; color: var(--ink-dark); background: #f8fafc; outline: none; transition: 0.3s; }
.filters input:focus, .filters select:focus { border-color: var(--primary); background: #fff; box-shadow: 0 0 0 4px rgba(79, 70, 229, 0.1); }
.filters .btn { background: var(--primary); color: #fff; border: 0; padding: 14px 24px; border-radius: 12px; font-weight: 600; font-size: 14px; cursor: pointer; transition: 0.3s; height: 46px; }
.filters .btn:hover { background: var(--primary-hover); transform: translateY(-2px); box-shadow: 0 10px 20px rgba(79, 70, 229, 0.2); }

.tw { overflow-x: auto; background: var(--card-bg); border-radius: 20px; box-shadow: var(--sh); padding: 10px; }
table { border-collapse: collapse; width: 100%;  }
thead th { position: sticky; top: 0; z-index: 10; background: #ffffff; white-space: nowrap; color: var(--ink); padding: 8px 12px; text-align: right; font-size: 13px; font-weight: 600; border-bottom: 2px solid var(--line);  }
tbody td { white-space: nowrap; padding: 6px 12px; border-bottom: 1px solid var(--line); font-size: 13px; font-weight: 500; color: var(--ink-dark);  transition: 0.2s; }
tbody tr:hover td { background: #f8fafc; }
tr.tot-row td { position: sticky; top: 35px; z-index: 9; background: #e2e8f0 !important; color: #0f172a !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #cbd5e1 !important; }
tr.prof-row1 td { background: #dcfce7 !important; color: #15803d !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 1.5px solid #bbf7d0 !important; }
tr.prof-row2 td { background: #dbeafe !important; color: #1e40af !important; font-weight: 800 !important; font-size: 14px !important; border-bottom: 2px solid #93c5fd !important; }

.rhead { display: flex; align-items: center; gap: 16px; margin-bottom: 10px; }
.rhead h1 { margin: 0; flex: 1; font-size: 20px; color: var(--ink-dark); font-weight: 800; border:0; padding:0; }
.rhead h1::before { display: none; }
.cnt { color: var(--ink); font-size: 13px; font-weight: 600; margin-bottom: 10px; }
.exps { display: flex; gap: 10px; }
.exp { border: 0; border-radius: 10px; padding: 10px 20px; font-weight: 600; font-size: 13px; color: #fff; cursor: pointer; transition: 0.3s; }
.exp:hover { transform: translateY(-2px); box-shadow: 0 5px 15px rgba(0,0,0,0.1); }
.exp.xl { background: #10b981; } .exp.pf { background: #ef4444; }
.err { background: #fef2f2; color: #b91c1c; padding: 16px; border-radius: 12px; font-weight: 600; }

.gdwrap { display: flex; flex-direction: column; gap: 24px; }
.gkpis { display: grid; grid-template-columns: repeat(4, 1fr); gap: 24px; }
.gk { background: var(--card-bg); border-radius: 24px; padding: 24px; display: flex; flex-direction: column; gap: 16px; box-shadow: var(--sh); position: relative; overflow: hidden; }
.gk:nth-child(1) { background: var(--primary); color: #fff; }
.gk:nth-child(1) .gl { color: rgba(255,255,255,0.8); }
.gk:nth-child(1) .gv { color: #fff; }
.gk .gic { width: 48px; height: 48px; border-radius: 16px; display: flex; align-items: center; justify-content: center; font-size: 20px; }
.gk:nth-child(1) .gic { background: rgba(255,255,255,0.2); }
.gk:nth-child(2) .gic { background: #dcfce7; color: #16a34a; }
.gk:nth-child(3) .gic { background: #ffedd5; color: #f97316; }
.gk:nth-child(4) .gic { background: #e0e7ff; color: #4f46e5; }
.gk:nth-child(5) .gic { background: #d1fae5; color: #059669; }
.gk:nth-child(6) .gic { background: #fee2e2; color: #dc2626; }
.gk:nth-child(7) .gic { background: #e0f2fe; color: #0284c7; }
.gk:nth-child(8) .gic { background: #fef3c7; color: #d97706; }
.gk .gl { font-size: 13px; font-weight: 600; color: var(--ink); margin-bottom: 4px; }
.gk .gv { font-size: 26px; font-weight: 800; color: var(--ink-dark); }
.gcharts { display: grid; grid-template-columns: 1fr 1fr; gap: 24px; }
.gc { background: var(--card-bg); border-radius: 24px; padding: 24px; box-shadow: var(--sh); }
.gc h3 { font-size: 16px; font-weight: 700; margin: 0 0 20px; color: var(--ink-dark); }
.app-logo { color:#4f46e5; font-weight:900; font-size:26px; letter-spacing:-1px; }
.mobile-dropdown { display: none; }
.mobile-dropdown select { width: 100%; padding: 12px 16px; border: 2px solid var(--primary); border-radius: 12px; font-family: inherit; font-size: 15px; font-weight: 700; color: var(--primary); background: #f8fafc; outline: none; text-align: center; cursor: pointer; margin-bottom: 15px; box-shadow: var(--sh); }

@media(max-width:900px){
  .app { flex-direction:column; padding:10px; }
  .sb { width:100%; flex-direction:row; padding:10px; overflow-x:auto; border-radius:16px; gap:8px; align-items:flex-start; -webkit-overflow-scrolling: touch; }
  .brand { margin:0; padding-right:10px; align-self: center; }
  .brand span { display:none; }
  .menu-lbl { display:none; }
  .sb a { margin:0; padding:8px 10px; flex-shrink: 0; flex-direction: column; justify-content: center; gap: 5px; min-width: 65px; text-align: center; }
  .sb a span { display: block; font-size: 11px;  line-height: 1.2; }
  
  .top { flex-direction: column; align-items: center; gap: 8px; padding-bottom: 15px; text-align: center; }
  .app-logo { font-size: 20px; }
  .ttl { font-size: 18px; }
  
  .pills { display: none; }
  .mobile-dropdown { display: block; }
  
  .rhead { flex-direction: column; align-items: center; gap: 12px; text-align: center; }
  .exps { width: 100%; justify-content: center; gap: 15px; }
  .exp { flex: 1; text-align: center; padding: 12px; font-size: 14px; }
  
  .filters { grid-template-columns: 1fr; gap: 15px; padding: 16px; }
  .filters .btn { height: 50px; font-size: 15px; }
  
  .gkpis { grid-template-columns: repeat(2,1fr); gap: 15px; }
  .gk { padding: 16px; }
  .gk .gv { font-size: 20px; }
  .gcharts { grid-template-columns: 1fr; }
}

</style>"""

LOGO = '<div class="app-logo">تقارير الأونكس الحديثة</div>'

PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>تقارير SREEN</title>""" + STYLE + """</head><body>
<div class="app">
 <aside class="sb">
   <div class="brand"><svg viewBox="0 0 24 24"><rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><rect x="14" y="14" width="7" height="7" rx="1"/></svg><span>Onyx Deck</span></div>
   <div class="menu-lbl">القائمة الرئيسية</div>
   
   {% for t in tabs %}{% if t.id not in hidden_tabs %}
     <a class="{{ 'on' if t.id==cur_tab else '' }}" href="/?tab={{t.id}}">
       <svg viewBox="0 0 24 24"><path d="{{t.icon}}"/></svg><span>{{ t.title }}</span></a>
   {% endif %}{% endfor %}
   <div class="menu-lbl" style="margin-top:auto">أدوات</div>
   <a href="/globals"><svg viewBox="0 0 24 24"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg><span>المتغيرات العامة</span></a>
   <a href="/settings"><svg viewBox="0 0 24 24"><path d="M4 6h9M4 12h5M4 18h7"/><circle cx="17" cy="6" r="2.3"/><circle cx="13" cy="12" r="2.3"/><circle cx="15" cy="18" r="2.3"/></svg><span>الإعدادات</span></a>
 </aside>
 <div class="main">
   <div class="wrap">
     {% if dash %}
     <div class="rhead"><h1>لوحة القيادة</h1></div>
     <form class="filters" method="get" action="/">
       <input type="hidden" name="tab" value="{{cur_tab}}"><input type="hidden" name="report" value="overview">
       <div><label>من تاريخ</label><input type="date" name="date_from" value="{{ binds.get('date_from') or '2026-01-01' }}"></div>
       <div><label>إلى تاريخ</label><input type="date" name="date_to" value="{{ binds.get('date_to') or '2026-12-31' }}"></div>
       <div><button class="btn" type="submit">تحديث</button></div>
     </form>
     {% if error %}<div class="err">خطأ: {{error}}</div>{% else %}
     <div class="gdwrap">
       <div class="gkpis">
         <div class="gk"><div class="gic" style="background:#dbeafe">💵</div><div><div class="gl">إجمالي المبيعات</div><div class="gv">{{ "{:,.0f}".format(dash.sales) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#dcfce7">💰</div><div><div class="gl">إجمالي التحصيل</div><div class="gv">{{ "{:,.0f}".format(dash.collect) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#ffedd5">🛒</div><div><div class="gl">إجمالي المشتريات</div><div class="gv">{{ "{:,.0f}".format(dash.purch) }}</div></div></div>
         {% if not hide_profit %}<div class="gk"><div class="gic" style="background:#ede9fe">📈</div><div><div class="gl">مجمل الربح</div><div class="gv">{{ "{:,.0f}".format(dash.gross) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#d1fae5">✅</div><div><div class="gl">صافي الربح</div><div class="gv">{{ "{:,.0f}".format(dash.netprofit) }}</div></div></div>{% endif %}
         <div class="gk"><div class="gic" style="background:#fee2e2">🧾</div><div><div class="gl">الذمم المدينة</div><div class="gv">{{ "{:,.0f}".format(dash.recv) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#e0f2fe">📦</div><div><div class="gl">قيمة المخزون</div><div class="gv">{{ "{:,.0f}".format(dash.invval) }}</div></div></div>
         <div class="gk"><div class="gic" style="background:#fef3c7">🏛️</div><div><div class="gl">صافي الضريبة</div><div class="gv">{{ "{:,.0f}".format(dash.vat) }}</div></div></div>
       </div>
       <div class="gcharts" style="grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));">
          <div class="gc" style="grid-column: 1 / -1;"><h3>المبيعات والتحصيل شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c1"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 مناديب</h3><div style="position:relative;height:250px;width:100%"><canvas id="c2"></canvas></div></div>
          <div class="gc"><h3>أفضل 5 أصناف</h3><div style="position:relative;height:250px;width:100%"><canvas id="c3"></canvas></div></div>
          <div class="gc" style="grid-column: 1 / -1;"><h3>المشتريات شهرياً</h3><div style="position:relative;height:280px;width:100%"><canvas id="c4"></canvas></div></div>
        </div>
     </div>
          <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: { backgroundColor: '#1e293b', padding: 14, titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' }, bodyFont: { size: 14, family: "'Cairo', sans-serif" }, cornerRadius: 10, displayColors: true, boxPadding: 6 }
         }
       };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32}
           ]
         },
         options: {
           ...commonOptions,
           plugins: { ...commonOptions.plugins, legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, font: { family: "'Cairo'", size: 13, weight: 'bold' } } } },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });

       // C2: Doughnut (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"doughnut",
         data:{
           labels:D.rep_labels.slice(0,5),
           datasets:[{data:D.rep_vals.slice(0,5), backgroundColor:["#4f46e5", "#38bdf8", "#10b981", "#f59e0b", "#8b5cf6"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C3: Doughnut (Items)
       new Chart(document.getElementById("c3"),{
         type:"doughnut",
         data:{
           labels:D.itm_labels.slice(0,5),
           datasets:[{data:D.itm_vals.slice(0,5), backgroundColor:["#f43f5e", "#d946ef", "#0ea5e9", "#14b8a6", "#eab308"], borderWidth: 0, hoverOffset: 4}]
         },
         options: {
           responsive: true, maintainAspectRatio: false, cutout: '75%',
           plugins: { legend: { display: true, position: 'bottom', labels: { usePointStyle: true, boxWidth: 8, font: { size: 11 } } } }
         }
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(16, 185, 129, 0.4)');
       grad4.addColorStop(1, 'rgba(16, 185, 129, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات", data:D.mpurch, borderColor:"#10b981", borderWidth: 3, backgroundColor: grad4, fill:true, tension:0.4, pointRadius: 0, pointHoverRadius: 6, pointBackgroundColor: "#fff", pointBorderColor: "#10b981", pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false },
           scales: {
             x: { grid: { display: false }, border: { display: false } },
             y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false } }
           }
         }
       });
     });
     </script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: {
             backgroundColor: '#1e293b',
             padding: 14,
             titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' },
             bodyFont: { size: 14, family: "'Cairo', sans-serif" },
             cornerRadius: 10,
             displayColors: true,
             boxPadding: 6
           }
         },
         scales: {
           x: { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' } } },
           y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } }
         }
       };

       const horizontalOptions = JSON.parse(JSON.stringify(commonOptions));
       horizontalOptions.indexAxis = "y";
       horizontalOptions.scales.x = { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' } } };
       horizontalOptions.scales.y = { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32, borderSkipped: false},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32, borderSkipped: false}
           ]
         },
         options: {
           ...commonOptions,
           plugins: {
             ...commonOptions.plugins,
             legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, padding: 20, font: { family: "'Cairo'", size: 13, weight: 'bold' } } }
           }
         }
       });

       // C2: Horizontal Bar (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"bar",
         data:{
           labels:D.rep_labels,
           datasets:[{label: "مبيعات", data:D.rep_vals, backgroundColor:"#8b5cf6", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C3: Horizontal Bar (Items)
       new Chart(document.getElementById("c3"),{
         type:"bar",
         data:{
           labels:D.itm_labels,
           datasets:[{label: "مبيعات", data:D.itm_vals, backgroundColor:"#10b981", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(249, 115, 22, 0.4)');
       grad4.addColorStop(1, 'rgba(249, 115, 22, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات",
             data:D.mpurch,
             borderColor:"#f97316",
             borderWidth: 3,
             backgroundColor: grad4,
             fill:true,
             tension:0.4,
             pointRadius: 0,
             pointHoverRadius: 6,
             pointBackgroundColor: "#fff",
             pointBorderColor: "#f97316",
             pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false }
         }
       });
     });
     </script>
     {% endif %}
     {% else %}
     <div class="pills">
       {% for r in tab.reports %}{% if (cur_tab ~ '/' ~ r.id) not in hidden_reports %}
         <a class="pill {{ 'on' if r.id==rpt.id else '' }}" href="/?tab={{cur_tab}}&report={{r.id}}">{{ r.title }}</a>
       {% endif %}{% endfor %}
     </div>
     <div class="mobile-dropdown">
       <select onchange="window.location.href=this.value">
         {% for r in tab.reports %}{% if (cur_tab ~ '/' ~ r.id) not in hidden_reports %}
           <option value="/?tab={{cur_tab}}&report={{r.id}}" {{ 'selected' if r.id==rpt.id else '' }}>{{ r.title }}</option>
         {% endif %}{% endfor %}
       </select>
     </div>
     <div class="rhead">
  <h1>{{ rpt.title }}</h1>
  <div class="exps">
    <a class="exp xl" href="/export?{{qs}}&format=xlsx">Excel</a>
    {% if rpt.id == 'collection_adopted' %}
      <select id="pdfModel" style="padding:4px 8px; border:1px solid #cbd5e1; border-radius:4px; margin-left:4px; font-family:inherit; font-size:13px;">
        <option value="1">PDF (النموذج الافتراضي)</option>
        <option value="2">PDF (نموذج 2)</option>
      </select>
      <button class="exp pf" style="border:none; cursor:pointer;" onclick="window.open('/print?{{qs|safe}}&model=' + document.getElementById('pdfModel').value, '_blank')">طباعة</button>
    {% else %}
      <a class="exp pf" href="/print?{{qs}}" target="_blank">PDF</a>
    {% endif %}
  </div>
</div>
     {% if rpt.params %}
     <form class="filters" method="get" action="/">
       <input type="hidden" name="tab" value="{{cur_tab}}"><input type="hidden" name="report" value="{{rpt.id}}">

       {% for p in rpt.params %}
         <div><label>{{p.label}}</label>
         {% if p.type=='select' %}
           <select name="{{p.name}}">{% for o in p.options %}<option value="{{o[0]}}" {{'selected' if binds.get(p.name)==o[0] else ''}}>{{o[1]}}</option>{% endfor %}</select>
         {% elif p.get('_list') %}
           <input type="text" name="{{p.name}}" list="dl_{{p.name}}" autocomplete="off" placeholder="ابحث بالكود أو الاسم" value="{{ binds.get(p.name) if binds.get(p.name) is not none else '' }}">
           <datalist id="dl_{{p.name}}">{% for o in p.get('_list') %}<option value="{{o}}"></option>{% endfor %}</datalist>
         {% else %}
           <input type="{{p.type}}" name="{{p.name}}" value="{{ binds.get(p.name) if binds.get(p.name) is not none else '' }}">
         {% endif %}
         </div>
       {% endfor %}
       <div><button class="btn" type="submit">عرض التقرير</button></div>
     </form>
      <script>
         document.addEventListener("DOMContentLoaded", function() {
             const pt = document.querySelector('select[name="period_type"]');
             const pv = document.querySelector('select[name="period_val"]');
             if(pt && pv) {
                 const allOpts = Array.from(pv.options).map(o => ({val: o.value, text: o.text}));
                 function updatePV() {
                     const t = pt.value;
                     const curVal = pv.value;
                     pv.innerHTML = '';
                     allOpts.forEach(o => {
                         let show = false;
                         let txt = o.text;
                         if(o.val === 'all') {
                             show = true;
                         } else {
                             const valNum = parseInt(o.val);
                             const parts = txt.split(' / ');
                             if (t === 'monthly' && valNum >= 1 && valNum <= 12) {
                                 show = true;
                                 txt = parts[0];
                             } else if (t === 'quarterly' && valNum >= 1 && valNum <= 4) {
                                 show = true;
                                 txt = parts[1] || txt;
                             } else if (t === 'semi_annual' && valNum >= 1 && valNum <= 2) {
                                 show = true;
                                 txt = parts[2] || txt;
                             }
                         }
                         if(show) {
                             const opt = document.createElement('option');
                             opt.value = o.val;
                             opt.text = txt;
                             pv.appendChild(opt);
                         }
                     });
                     if(!Array.from(pv.options).find(o => o.value === curVal)) {
                         pv.value = 'all';
                     } else {
                         pv.value = curVal;
                     }
                 }
                 pt.addEventListener('change', updatePV);
                 updatePV();
             }
         });
      </script>
     {% endif %}
     {% if rpt.params and 'date_from' in rpt.params|map(attribute='name') %}
     <div class="quick-dates">
         <button type="button" class="btn-sm" onclick="setDates('today', this)">اليوم</button>
         <button type="button" class="btn-sm" onclick="setDates('this_week', this)">هذا الأسبوع</button>
         <button type="button" class="btn-sm" onclick="setDates('this_month', this)">هذا الشهر</button>
         <button type="button" class="btn-sm" onclick="setDates('last_month', this)">الشهر السابق</button>
         <button type="button" class="btn-sm" onclick="setDates('this_year', this)">هذه السنة</button>
         <button type="button" class="btn-sm" onclick="setDates('last_year', this)">السنة السابقة</button>
     </div>
     <script>
         function setDates(range, btn) {
             document.querySelectorAll('.quick-dates .btn-sm').forEach(b => b.classList.remove('active'));
             if(btn) btn.classList.add('active');
             
             const dFrom = document.querySelector('input[name="date_from"]');
             const dTo = document.querySelector('input[name="date_to"]');
             if(!dFrom || !dTo) return;
             
             const today = new Date();
             let from = new Date();
             let to = new Date();

             if(range === 'today') {
                 // keep today
             } else if (range === 'this_week') {
                 const day = today.getDay();
                 from.setDate(today.getDate() - day);
             } else if (range === 'this_month') {
                 from = new Date(today.getFullYear(), today.getMonth(), 1);
                 to = new Date(today.getFullYear(), today.getMonth() + 1, 0);
             } else if (range === 'last_month') {
                 from = new Date(today.getFullYear(), today.getMonth() - 1, 1);
                 to = new Date(today.getFullYear(), today.getMonth(), 0);
             } else if (range === 'this_year') {
                 from = new Date(today.getFullYear(), 0, 1);
                 to = new Date(today.getFullYear(), 11, 31);
             } else if (range === 'last_year') {
                 from = new Date(today.getFullYear() - 1, 0, 1);
                 to = new Date(today.getFullYear() - 1, 11, 31);
             }

             const fmt = d => {
                 const m = String(d.getMonth() + 1).padStart(2, '0');
                 const day = String(d.getDate()).padStart(2, '0');
                 return `${d.getFullYear()}-${m}-${day}`;
             };
             
             dFrom.value = fmt(from);
             dTo.value = fmt(to);
             
             const form = dFrom.closest('form');
             if(form) form.submit();
         }
     </script>
     {% endif %}
     
     {% if error %}<div class="err">خطأ: {{error}}</div>
     {% else %}
       <div class="tw"><table><thead><tr>{% for c in cols %}<th onclick="sortTable({{loop.index0}})" style="cursor:pointer" title="اضغط للترتيب">{{c}} <span style="font-size:10px; opacity:0.5; margin-right:4px">↕</span></th>{% endfor %}</tr></thead>
       <tbody>{% for row in rows %}{% set r0 = (row[0]|string).strip() %}{% set r1 = (row[1]|string).strip() %}{% set cls = '' %}{% if r0=='الإجمالي' or r1=='الإجمالي' %}{% set cls = 'tot-row' %}{% elif 'رصيد الفترة صافي' in r1 %}{% set cls = 'prof-row1' %}{% elif 'الرصيد النهائي صافي' in r1 %}{% set cls = 'prof-row2' %}{% endif %}<tr class="{{ cls }}">{% for cell in row %}<td>{{ '' if cell is none else cell }}</td>{% endfor %}</tr>{% endfor %}</tbody></table></div>
     {% endif %}
     {% endif %}
   </div>
 </div>
 <script>
 document.addEventListener('DOMContentLoaded', function() {
   var activeTab = document.querySelector('.sb a.on');
   if (activeTab) { activeTab.scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'center' }); }
   var activePill = document.querySelector('.pills a.on');
   if (activePill) { activePill.scrollIntoView({ behavior: 'auto', block: 'nearest', inline: 'center' }); }
 });

    function sortTable(colIndex) {
      const tbody = document.querySelector('tbody');
      if (!tbody) return;
      
      const rows = Array.from(tbody.querySelectorAll('tr'));
      if (rows.length <= 1) return; 
      
      const totalRow = rows.shift(); 
      
      let dir = tbody.getAttribute('data-sort-dir') === 'asc' ? 'desc' : 'asc';
      tbody.setAttribute('data-sort-dir', dir);
      
      rows.sort((a, b) => {
        let valA = a.children[colIndex].textContent.trim();
        let valB = b.children[colIndex].textContent.trim();
        
        let numA = parseFloat(valA.replace(/,/g, ''));
        let numB = parseFloat(valB.replace(/,/g, ''));
        
        let isNumA = !isNaN(numA) && valA !== '';
        let isNumB = !isNaN(numB) && valB !== '';
        
        let cmp = 0;
        if (isNumA && isNumB) {
          cmp = numA - numB;
        } else {
          cmp = valA.localeCompare(valB, 'ar');
        }
        
        return dir === 'asc' ? cmp : -cmp;
      });
      
      tbody.innerHTML = '';
      tbody.appendChild(totalRow);
      rows.forEach(r => tbody.appendChild(r));
      
      // Update PDF and Excel export links
      let exps = document.querySelectorAll('.exp');
      let colName = document.querySelectorAll('thead th')[colIndex].textContent.replace(' ↕', '').trim();
      exps.forEach(a => {
        let url = new URL(a.href, window.location.origin);
        url.searchParams.set('sort_col', colName);
        url.searchParams.set('sort_dir', dir);
        a.href = url.pathname + url.search;
      });
    }
 </script>
</body></html>"""

