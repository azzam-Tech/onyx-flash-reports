# -*- coding: utf-8 -*-
from database import get_conn
from . import repository
from report_handlers import run_sql_report, get_date_range
from collections import defaultdict
import datetime

def run_perf_aging_fifo(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    is_dynamic = rpt.get('id') == 'perf_aging_dynamic'
    rep_code = args.get('rep_code')
    cc_code = args.get('cc_code')
    grp_code = args.get('grp_code')
    if cc_code:
        cc_code = cc_code.split(' - ')[0].strip()
    if grp_code:
        grp_code = grp_code.split(' - ')[0].strip()
    if is_dynamic:
        inc_rcpt = str(args.get('inc_rcpt', '1')) == '1'
        inc_net = str(args.get('inc_net', '1')) == '1'
        inc_cash = str(args.get('inc_cash', '1')) == '1'
        inc_ret = str(args.get('inc_ret', '1')) == '1'
        inc_ext = False
    else:
        inc_rcpt = True
        inc_net = False
        inc_cash = False
        inc_ret = False
        inc_ext = False
    if rep_code:
        rep_code = rep_code.split(' - ')[0].strip()
    date_from_str = args.get('date_from', '')
    date_to_str = args.get('date_to', '')
    if not date_from_str:
        now = datetime.now()
        date_from_str = f"{now.year}-{now.month:02d}-01"
    if not date_to_str:
        import calendar
        now = datetime.now()
        last_day = calendar.monthrange(now.year, now.month)[1]
        date_to_str = f"{now.year}-{now.month:02d}-{last_day:02d}"
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute('SELECT C_CODE, REP_CODE, C_GROUP_CODE FROM CUSTOMER')
            res_cust = cur.fetchall()
            cust_rep = {str(c): str(r) if r else '' for c, r, g in res_cust}
            cust_grp = {str(c): str(g) if g else '' for c, r, g in res_cust}
            cur.execute('SELECT REPRS_CODE, REPRS_A_NAME FROM SALES_MAN')
            rep_name = {str(c): n for c, n in cur.fetchall()}
            sql_cash = "\n                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))\n                FROM IAS_BILL_MST b\n                JOIN IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'\n                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0\n                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1\n                GROUP BY TO_CHAR(b.REP_CODE)\n            "
            cur.execute(sql_cash, {'df': date_from_str, 'dt': date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}
            sql_ret_null = "\n                SELECT NVL(TO_CHAR(REP_CODE), 'UNKNOWN'), SUM(NVL(CR_AMT,0))\n                FROM IAS_POST_DTL\n                WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0\n                  AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1\n                GROUP BY TO_CHAR(REP_CODE)\n            "
            cur.execute(sql_ret_null, {'df': date_from_str, 'dt': date_to_str})
            cash_ret_null_by_rep = {r: float(amt) for r, amt in cur.fetchall()}
            rep_filter = ' AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)' if rep_code else ''
            binds_fifo = {}
            if rep_code:
                binds_fifo['rep_code'] = rep_code
            sql = f'\n                SELECT TO_CHAR(p.C_CODE), p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE, p.DOC_NO, p.DOC_SER\n                FROM IAS_POST_DTL p\n                WHERE (1=1)\n                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)\n                    AND p.C_CODE IS NOT NULL\n                    {rep_filter}\n            '
            cur.execute(sql, binds_fifo)
            byc = defaultdict(lambda: {'debits': [], 'credits': [], 'returns': []})
            for ccode, ddate, dr, cr, dtype, jvtype, acode, doc_no, doc_ser in cur.fetchall():
                if ccode is None:
                    continue
                d = ddate.date() if hasattr(ddate, 'date') else ddate
                dr = float(dr)
                cr = float(cr)
                if cr > 0:
                    if dtype in (5, 15):
                        byc[str(ccode)]['returns'].append({'date': d, 'amt': cr, 'doc_no': doc_no, 'doc_ser': doc_ser, 'linked_inv': None, 'dtype': dtype, 'jvtype': jvtype, 'acode': acode})
                    else:
                        if not is_dynamic:
                            valid_cr = cr
                        elif dtype == 2 and inc_rcpt:
                            valid_cr = cr
                        elif dtype == 1 and jvtype == 2 and inc_net:
                            valid_cr = cr
                        elif dtype == 15 and inc_ext:
                            valid_cr = -cr
                        if valid_cr != 0:
                            byc[str(ccode)]['credits'].append((d, valid_cr))
                if dr > 0:
                    byc[str(ccode)]['debits'].append({'date': d, 'amt': dr, 'doc_no': doc_no, 'doc_ser': doc_ser})
            sql_links = f"\n                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(d.BILL_NO) as BILL_NO, TO_CHAR(d.BILL_SER) as BILL_SER\n                FROM IAS_POST_DTL p\n                JOIN IAS_RT_BILL_DTL d \n                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER\n                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 \n                  AND p.C_CODE IS NOT NULL\n                  AND d.BILL_NO IS NOT NULL\n                  {rep_filter}\n                UNION ALL\n                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(p.DOC_NO_REF) as BILL_NO, '' as BILL_SER\n                FROM IAS_POST_DTL p\n                WHERE p.DOC_TYPE = 15 AND p.CR_AMT > 0\n                  AND p.C_CODE IS NOT NULL\n                  AND p.DOC_NO_REF IS NOT NULL\n                  {rep_filter}\n            "
            cur.execute(sql_links, binds_fifo)
            links = {}
            for r_no, r_ser, b_no, b_ser in cur.fetchall():
                links[r_no, r_ser] = (b_no, b_ser)
            for c_id, data in byc.items():
                for ret in data['returns']:
                    k = (ret['doc_no'], ret['doc_ser'])
                    if k in links:
                        ret['linked_inv'] = links[k]
    aging_ranges_str = args.get('aging_ranges', '2,30,60,90,120')
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(',') if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]
    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append('0')
        elif prev == 0:
            bucket_labels.append(f'0-{lim}')
        else:
            bucket_labels.append(f'{prev + 1}-{lim}')
        prev = lim
    bucket_labels.append(f'أكثر من {limits[-1]}')
    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)
    rep_results = defaultdict(lambda: {'cust_count': set(), 'b': [0.0] * num_buckets, 'total': 0.0})
    for ccode, evs in byc.items():
        r_code = cust_rep.get(ccode)
        if not r_code:
            continue
        if rep_code and r_code != rep_code:
            continue
        debits = sorted(evs['debits'], key=lambda x: x['date'])
        credits = sorted(evs['credits'], key=lambda x: x[0])
        returns = sorted(evs['returns'], key=lambda x: x['date'])
        for ret in returns:
            r_amt = ret['amt']
            linked_inv = ret['linked_inv']
            if linked_inv:
                b_no, b_ser = linked_inv
                for deb in debits:
                    if deb['amt'] > 0 and str(deb['doc_no']) == str(b_no) and (not b_ser or str(deb['doc_ser']) == str(b_ser)):
                        if r_amt >= deb['amt']:
                            r_amt -= deb['amt']
                            deb['amt'] = 0.0
                        else:
                            deb['amt'] -= r_amt
                            r_amt = 0.0
                            break
                        if r_amt <= 0:
                            break
            if r_amt > 0:
                valid_cr = 0.0
                if not is_dynamic:
                    valid_cr = r_amt
                elif ret['dtype'] == 5 and ret['acode'] and str(ret['acode']).startswith('111') and inc_ret:
                    valid_cr = -r_amt
                if valid_cr != 0:
                    credits.append((ret['date'], valid_cr))
        credits.sort(key=lambda x: x[0])
        dcum = 0.0
        dint = []
        for deb in debits:
            if deb['amt'] > 0:
                lo = dcum
                dcum += deb['amt']
                dint.append((lo, dcum, deb['date']))
        ddates = [deb['date'] for deb in debits if deb['amt'] > 0]
        ccum = 0.0
        for d, cr in credits:
            clo = ccum
            ccum += cr
            chi = ccum
            if not from_dt <= d <= to_dt:
                continue
            lo_cr, hi_cr = (min(clo, chi), max(clo, chi))
            is_negative = cr < 0
            rep_results[r_code]['cust_count'].add(ccode)
            rep_results[r_code]['total'] += cr
            for lo, hi, idate in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0:
                        continue
                    if is_negative:
                        amt = -amt
                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days
                    rep_results[r_code]['b'][bucket_of(age)] += amt
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code:
                continue
            if c_sales > 0:
                rep_results[r_code]['total'] += c_sales
                rep_results[r_code]['b'][0] += c_sales
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and (r_code != 'UNKNOWN'):
                continue
            if c_ret > 0:
                rep_results[r_code]['total'] -= c_ret
                rep_results[r_code]['b'][0] -= c_ret
    cols = ['كود المندوب', 'اسم المندوب', 'عدد العملاء'] + bucket_labels + ['المبلغ المحصل']
    rows = []
    for r_code, data in rep_results.items():
        if round(data['total'], 2) == 0 and sum((abs(x) for x in data['b'])) < 0.01:
            continue
        formatted_b = [f'{x:,.2f}' for x in data['b']]
        row = (r_code, rep_name.get(r_code, r_code), len(data['cust_count'])) + tuple(formatted_b) + (f"{data['total']:,.2f}",)
        rows.append(row)
    tot_idx = len(cols) - 1
    rows.sort(key=lambda x: float(str(x[tot_idx]).replace(',', '')), reverse=True)
    return (cols, rows)

def run_perf_aging_analytical(rpt, args):
    import bisect
    from collections import defaultdict
    from datetime import datetime
    rep_code = args.get('rep_code')
    inc_rcpt = str(args.get('inc_rcpt', '1')) == '1'
    inc_net = str(args.get('inc_net', '1')) == '1'
    inc_cash = str(args.get('inc_cash', '1')) == '1'
    inc_ret = str(args.get('inc_ret', '1')) == '1'
    inc_ext = False
    if rep_code:
        rep_code = rep_code.split(' - ')[0].strip()
    else:
        return (['تنبيه'], [('الرجاء اختيار المندوب أولاً من القائمة المنسدلة لعرض التقرير التحليلي.', '', '', '', '', '', '', '')])
    date_from_str = args.get('date_from', '')
    date_to_str = args.get('date_to', '')
    if not date_from_str:
        now = datetime.now()
        date_from_str = f"{now.year}-{now.month:02d}-01"
    if not date_to_str:
        import calendar
        now = datetime.now()
        last_day = calendar.monthrange(now.year, now.month)[1]
        date_to_str = f"{now.year}-{now.month:02d}-{last_day:02d}"
    from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute('SELECT C_CODE, REP_CODE, C_A_NAME, C_GROUP_CODE FROM CUSTOMER')
            cust_rep = {}
            cust_names = {}
            cust_grp = {}
            for c, r, n, g in cur.fetchall():
                cust_rep[str(c)] = str(r)
                cust_names[str(c)] = str(n)
                cust_grp[str(c)] = str(g) if g else ''
            cur.execute('SELECT REPRS_CODE, REPRS_A_NAME FROM SALES_MAN')
            rep_name = {str(c): n for c, n in cur.fetchall()}
            sql_cash = "\n                SELECT TO_CHAR(b.REP_CODE), SUM(NVL(p.DR_AMT,0))\n                FROM IAS_BILL_MST b\n                JOIN IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'\n                WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0\n                  AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1\n                GROUP BY TO_CHAR(b.REP_CODE)\n            "
            cur.execute(sql_cash, {'df': date_from_str, 'dt': date_to_str})
            cash_sales_by_rep = {r: float(amt) for r, amt in cur.fetchall() if r}
            sql_ret_null = "\n                SELECT NVL(TO_CHAR(REP_CODE), 'UNKNOWN'), SUM(NVL(CR_AMT,0))\n                FROM IAS_POST_DTL\n                WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0\n                  AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1\n                GROUP BY TO_CHAR(REP_CODE)\n            "
            cur.execute(sql_ret_null, {'df': date_from_str, 'dt': date_to_str})
            cash_ret_null_by_rep = {r: float(amt) for r, amt in cur.fetchall()}
            rep_filter = ' AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)' if rep_code else ''
            binds_fifo = {}
            if rep_code:
                binds_fifo['rep_code'] = rep_code
            sql = f'\n                SELECT TO_CHAR(p.C_CODE), p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE, p.DOC_NO, p.DOC_SER\n                FROM IAS_POST_DTL p\n                WHERE (1=1)\n                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)\n                    AND p.C_CODE IS NOT NULL\n                    {rep_filter}\n            '
            cur.execute(sql, binds_fifo)
            byc = defaultdict(lambda: {'debits': [], 'credits': [], 'returns': []})
            for ccode, ddate, dr, cr, dtype, jvtype, acode, doc_no, doc_ser in cur.fetchall():
                if ccode is None:
                    continue
                d = ddate.date() if hasattr(ddate, 'date') else ddate
                dr = float(dr)
                cr = float(cr)
                if cr > 0:
                    if dtype in (5, 15):
                        byc[str(ccode)]['returns'].append({'date': d, 'amt': cr, 'doc_no': doc_no, 'doc_ser': doc_ser, 'linked_inv': None, 'dtype': dtype, 'jvtype': jvtype, 'acode': acode})
                    else:
                        if dtype == 2 and inc_rcpt:
                            valid_cr = cr
                        elif dtype == 1 and jvtype == 2 and inc_net:
                            valid_cr = cr
                        elif dtype == 15 and inc_ext:
                            valid_cr = -cr
                        if valid_cr != 0:
                            byc[str(ccode)]['credits'].append((d, valid_cr))
                if dr > 0:
                    byc[str(ccode)]['debits'].append({'date': d, 'amt': dr, 'doc_no': doc_no, 'doc_ser': doc_ser})
            sql_links = f"\n                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(d.BILL_NO) as BILL_NO, TO_CHAR(d.BILL_SER) as BILL_SER\n                FROM IAS_POST_DTL p\n                JOIN IAS_RT_BILL_DTL d \n                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER\n                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 \n                  AND p.C_CODE IS NOT NULL\n                  AND d.BILL_NO IS NOT NULL\n                  {rep_filter}\n                UNION ALL\n                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(p.DOC_NO_REF) as BILL_NO, '' as BILL_SER\n                FROM IAS_POST_DTL p\n                WHERE p.DOC_TYPE = 15 AND p.CR_AMT > 0\n                  AND p.C_CODE IS NOT NULL\n                  AND p.DOC_NO_REF IS NOT NULL\n                  {rep_filter}\n            "
            cur.execute(sql_links, binds_fifo)
            links = {}
            for r_no, r_ser, b_no, b_ser in cur.fetchall():
                links[r_no, r_ser] = (b_no, b_ser)
            for c_id, data in byc.items():
                for ret in data['returns']:
                    k = (ret['doc_no'], ret['doc_ser'])
                    if k in links:
                        ret['linked_inv'] = links[k]
    aging_ranges_str = args.get('aging_ranges', '2,30,60,90,120')
    try:
        limits = sorted([int(x.strip()) for x in aging_ranges_str.split(',') if x.strip().isdigit()])
        if not limits:
            limits = [2, 30, 60, 90, 120]
    except Exception:
        limits = [2, 30, 60, 90, 120]
    bucket_labels = []
    prev = 0
    for lim in limits:
        if prev == 0 and lim == 0:
            bucket_labels.append('0')
        elif prev == 0:
            bucket_labels.append(f'0-{lim}')
        else:
            bucket_labels.append(f'{prev + 1}-{lim}')
        prev = lim
    bucket_labels.append(f'أكثر من {limits[-1]}')
    num_buckets = len(bucket_labels)

    def bucket_of(age):
        for idx, lim in enumerate(limits):
            if age <= lim:
                return idx
        return len(limits)
    cust_results = defaultdict(lambda: {'b': [0.0] * num_buckets, 'total': 0.0})
    for ccode, evs in byc.items():
        r_code = cust_rep.get(ccode)
        if not r_code:
            continue
        if rep_code and r_code != rep_code:
            continue
        debits = sorted(evs['debits'], key=lambda x: x['date'])
        credits = sorted(evs['credits'], key=lambda x: x[0])
        returns = sorted(evs['returns'], key=lambda x: x['date'])
        for ret in returns:
            r_amt = ret['amt']
            linked_inv = ret['linked_inv']
            if linked_inv:
                b_no, b_ser = linked_inv
                for deb in debits:
                    if deb['amt'] > 0 and str(deb['doc_no']) == str(b_no) and (not b_ser or str(deb['doc_ser']) == str(b_ser)):
                        if r_amt >= deb['amt']:
                            r_amt -= deb['amt']
                            deb['amt'] = 0.0
                        else:
                            deb['amt'] -= r_amt
                            r_amt = 0.0
                            break
                        if r_amt <= 0:
                            break
            if r_amt > 0:
                valid_cr = 0.0
                if ret['dtype'] == 5 and ret['acode'] and str(ret['acode']).startswith('111') and inc_ret:
                    valid_cr = -r_amt
                if valid_cr != 0:
                    credits.append((ret['date'], valid_cr))
        credits.sort(key=lambda x: x[0])
        dcum = 0.0
        dint = []
        for deb in debits:
            if deb['amt'] > 0:
                lo = dcum
                dcum += deb['amt']
                dint.append((lo, dcum, deb['date']))
        ddates = [deb['date'] for deb in debits if deb['amt'] > 0]
        ccum = 0.0
        for d, cr in credits:
            clo = ccum
            ccum += cr
            chi = ccum
            if not from_dt <= d <= to_dt:
                continue
            lo_cr, hi_cr = (min(clo, chi), max(clo, chi))
            is_negative = cr < 0
            cust_results[ccode]['total'] += cr
            for lo, hi, idate in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0:
                        continue
                    if is_negative:
                        amt = -amt
                    if idate > d:
                        age = 0
                    else:
                        age = (d - idate).days
                    cust_results[ccode]['b'][bucket_of(age)] += amt
    if inc_cash:
        for r_code, c_sales in cash_sales_by_rep.items():
            if rep_code and r_code != rep_code:
                continue
            if c_sales > 0:
                cust_results['CASH_SALES_' + str(r_code)]['total'] += c_sales
                cust_results['CASH_SALES_' + str(r_code)]['b'][0] += c_sales
    if inc_ret:
        for r_code, c_ret in cash_ret_null_by_rep.items():
            if rep_code and r_code != rep_code and (r_code != 'UNKNOWN'):
                continue
            if c_ret > 0:
                cust_results['CASH_SALES_' + str(r_code)]['total'] -= c_ret
                cust_results['CASH_SALES_' + str(r_code)]['b'][0] -= c_ret
    cols = ['رقم العميل', 'اسم العميل'] + bucket_labels + ['إجمالي التحصيل']
    rows = []
    for ccode, data in cust_results.items():
        if round(data['total'], 2) == 0 and sum((abs(x) for x in data['b'])) < 0.01:
            continue
        if str(ccode).startswith('CASH_SALES_'):
            c_name = 'مبيعات نقدية (للمندوب)'
            disp_code = '-'
        else:
            c_name = cust_names.get(str(ccode), str(ccode))
            disp_code = str(ccode)
        formatted_b = [f'{x:,.2f}' for x in data['b']]
        row = (disp_code, c_name) + tuple(formatted_b) + (f"{data['total']:,.2f}",)
        rows.append(row)
    tot_idx = len(cols) - 1
    rows.sort(key=lambda x: float(str(x[tot_idx]).replace(',', '')), reverse=True)
    return (cols, rows)


def handle_fin_report(report_id, rpt, args):
    if report_id == 'perf_aging_dynamic':
        return run_perf_aging_fifo(rpt, args)
    if report_id == 'perf_aging_dynamic_analytical':
        return run_perf_aging_analytical(rpt, args)
        
    repo_func_name = f"get_{report_id}_sql"
    if hasattr(repository, repo_func_name):
        rpt['sql'] = getattr(repository, repo_func_name)()
        
    if rpt.get('sql'):
        return run_sql_report(rpt, args)
        
    return [], []
