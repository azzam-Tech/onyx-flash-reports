# -*- coding: utf-8 -*-
from database import get_conn
from . import repository
from report_handlers import run_sql_report
from collections import defaultdict
import datetime

def run_cust_aging(rpt, args):
    from collections import defaultdict
    from datetime import datetime
    from database import get_conn
    rep_code = args.get('rep_code')
    c_code = args.get('c_code')
    cc_code = args.get('cc_code')
    grp_code = args.get('grp_code')
    if cc_code:
        cc_code = cc_code.split(' - ')[0].strip()
    if grp_code:
        grp_code = grp_code.split(' - ')[0].strip()
    if rep_code:
        rep_code = rep_code.split(' - ')[0].strip()
    if c_code:
        c_code = c_code.split(' - ')[0].strip()
    date_to_str = args.get('date_to', '')
    if not date_to_str:
        date_to_str = '2026-07-31'
    to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()
    with get_conn() as con:
        with con.cursor() as cur:
            sql_cust = 'SELECT TO_CHAR(C_CODE), MAX(C_A_NAME), MAX(TO_CHAR(REP_CODE)), MAX(TO_CHAR(C_GROUP_CODE)) FROM CUSTOMER GROUP BY TO_CHAR(C_CODE)'
            cur.execute(sql_cust)
            customers = {}
            for row in cur.fetchall():
                customers[row[0]] = {'name': row[1] or '', 'rep': row[2] or '', 'grp': row[3] or ''}
            binds = {'dt': date_to_str}
            filters = []
            if rep_code:
                filters.append('TO_CHAR(p.REP_CODE) = :rep')
                binds['rep'] = rep_code
            if c_code:
                filters.append('TO_CHAR(p.C_CODE) = :cst')
                binds['cst'] = c_code
            if cc_code:
                filters.append('TO_CHAR(p.CC_CODE) = :cc')
                binds['cc'] = cc_code
            filter_str = ' AND ' + ' AND '.join(filters) if filters else ''
            sql = f"\n                SELECT TO_CHAR(p.C_CODE), p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.DOC_NO, p.DOC_SER\n                FROM IAS_POST_DTL p\n                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))\n                    AND p.C_CODE IS NOT NULL\n                    AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1\n                    {filter_str}\n            "
            cur.execute(sql, binds)
            by_cust = defaultdict(lambda: {'debits': [], 'credits': 0.0, 'returns': []})
            for c_id, ddate, dr, cr, dtype, doc_no, doc_ser in cur.fetchall():
                d = ddate.date() if hasattr(ddate, 'date') else ddate
                dr = float(dr)
                cr = float(cr)
                if cr > 0:
                    if dtype in (5, 15):
                        by_cust[c_id]['returns'].append({'date': d, 'amt': cr, 'doc_no': doc_no, 'doc_ser': doc_ser, 'linked_inv': None})
                    else:
                        by_cust[c_id]['credits'] += cr
                if dr > 0:
                    by_cust[c_id]['debits'].append({'date': d, 'amt': dr, 'type': dtype, 'doc_no': doc_no, 'doc_ser': doc_ser})
            sql_links = f"\n                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(d.BILL_NO) as BILL_NO, TO_CHAR(d.BILL_SER) as BILL_SER\n                FROM IAS_POST_DTL p\n                JOIN IAS_RT_BILL_DTL d \n                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER\n                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 \n                  AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1\n                  AND d.BILL_NO IS NOT NULL\n                  {filter_str}\n                UNION ALL\n                SELECT DISTINCT p.DOC_NO, p.DOC_SER, TO_CHAR(p.DOC_NO_REF) as BILL_NO, '' as BILL_SER\n                FROM IAS_POST_DTL p\n                WHERE p.DOC_TYPE = 15 AND p.CR_AMT > 0\n                  AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1\n                  AND p.DOC_NO_REF IS NOT NULL\n                  {filter_str}\n            "
            cur.execute(sql_links, binds)
            links = {}
            for r_no, r_ser, b_no, b_ser in cur.fetchall():
                links[r_no, r_ser] = (b_no, b_ser)
            for c_id, data in by_cust.items():
                for ret in data['returns']:
                    k = (ret['doc_no'], ret['doc_ser'])
                    if k in links:
                        ret['linked_inv'] = links[k]
            if str(args.get('vendor_link', '0')) == '1':
                cur.execute('SELECT TO_CHAR(C_CODE), TO_CHAR(C_VENDOR) FROM CUSTOMER WHERE C_VENDOR IS NOT NULL')
                cust_vendor_map = {c: v for c, v in cur.fetchall()}
                cur.execute("SELECT TO_CHAR(V_CODE), SUM(NVL(CR_AMT,0) - NVL(DR_AMT,0)) FROM IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND V_CODE IS NOT NULL AND DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1 GROUP BY TO_CHAR(V_CODE)", {'dt': date_to_str})
                vendor_balances = {v: float(bal) for v, bal in cur.fetchall()}
                for c_id, v_id in cust_vendor_map.items():
                    if c_id in by_cust and v_id in vendor_balances and (vendor_balances[v_id] > 0):
                        by_cust[c_id]['credits'] += vendor_balances[v_id]
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
    cols = ['كود العميل', 'اسم العميل', 'المندوب'] + bucket_labels + ['الإجمالي']
    rows = []
    for c_id, data in by_cust.items():
        cust_info = customers.get(c_id, {})
        if rep_code and cust_info.get('rep') != rep_code:
            continue
        if grp_code and cust_info.get('grp') != grp_code:
            continue
        debits = sorted(data['debits'], key=lambda x: x['date'])
        returns = sorted(data['returns'], key=lambda x: x['date'])
        total_credit = data['credits']
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
                total_credit += r_amt
        unmatched_debits = [(d['date'], d['amt']) for d in debits if d['amt'] > 0]
        buckets = [0.0] * num_buckets
        total_unpaid = 0.0
        for ddate, amt in unmatched_debits:
            if total_credit >= amt:
                total_credit -= amt
            else:
                unpaid = amt - total_credit
                total_credit = 0.0
                age = (to_dt - ddate).days
                if age < 0:
                    age = 0
                buckets[bucket_of(age)] += unpaid
                total_unpaid += unpaid
        if round(total_unpaid, 2) > 0:
            nm = customers.get(c_id, {}).get('name', '')
            rp = customers.get(c_id, {}).get('rep', '')
            formatted_b = [f'{x:,.2f}' for x in buckets]
            row = (c_id, nm, rp, *formatted_b, f'{total_unpaid:,.2f}')
            rows.append(row)
    rows.sort(key=lambda r: float(r[-1].replace(',', '')), reverse=True)
    return (cols, rows)


def handle_ar_report(report_id, rpt, args):
    if report_id == 'aging':
        return run_cust_aging(rpt, args)
        
    repo_func_name = f"get_{report_id}_sql"
    if hasattr(repository, repo_func_name):
        rpt['sql'] = getattr(repository, repo_func_name)()
        
    if rpt.get('sql'):
        return run_sql_report(rpt, args)
        
    return [], []
