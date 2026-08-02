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
rep_code = '142'

from_dt = datetime.strptime(date_from_str, '%Y-%m-%d').date()
to_dt = datetime.strptime(date_to_str, '%Y-%m-%d').date()

def bucket_of(age):
    if age <= 30:  return 0
    if age <= 60:  return 1
    if age <= 90:  return 2
    if age <= 120: return 3
    return 4

def simulate(inc_cash, inc_net, inc_ret, inc_ext):
    cur.execute("""
        SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
        FROM IAS20261.IAS_POST_DTL p
        JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
        WHERE NVL(p.DOC_POST,0)=1 AND TO_CHAR(c.REP_CODE) = :rep
          AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
    """, {"rep": rep_code})
    
    byc = defaultdict(lambda: {"debits": [], "credits": []})
    for ccode, ddate, dr, cr, dtype, jvtype, acode in cur.fetchall():
        d = ddate.date()
        dr = float(dr)
        cr = float(cr)
        
        valid_cr = 0.0
        if cr > 0:
            if dtype == 2:  # rcpt
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
            
    b = [0.0]*5
    total = 0.0
    
    for ccode, evs in byc.items():
        debits  = sorted(evs["debits"], key=lambda x: x[0])
        credits = sorted(evs["credits"], key=lambda x: x[0])
        
        dcum = 0.0; dint = []
        for (d, dr) in debits:
            lo = dcum; dcum += dr; dint.append((lo, dcum, d))
            
        ccum = 0.0
        for (d, cr) in credits:
            clo = ccum; ccum += cr; chi = ccum
            if not (from_dt <= d <= to_dt):
                continue
            
            hi_cr = max(clo, chi)
            lo_cr = min(clo, chi)
            is_negative = (cr < 0)
            
            total += cr
            for (lo, hi, idate) in dint:
                if lo < hi_cr and hi > lo_cr:
                    amt = min(hi_cr, hi) - max(lo_cr, lo)
                    if amt <= 0: continue
                    if is_negative: amt = -amt
                    
                    if idate > d: age = 0
                    else: age = (d - idate).days
                    b[bucket_of(age)] += amt

    if inc_cash:
        cur.execute("""
            SELECT SUM(NVL(p.DR_AMT,0))
            FROM IAS20261.IAS_BILL_MST b
            JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
            WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
              AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
              AND TO_CHAR(b.REP_CODE) = :rep
        """, {"df": date_from_str, "dt": date_to_str, "rep": rep_code})
        c_sales = cur.fetchone()[0] or 0.0
        total += c_sales
        b[0] += c_sales

    print(f"\nSimulation (inc_cash={inc_cash}, inc_net={inc_net}, inc_ret={inc_ret}):")
    print(f"Total: {total:,.2f}")
    print(f"0-30:  {b[0]:,.2f}")
    print(f"31-60: {b[1]:,.2f}")
    print(f"61-90: {b[2]:,.2f}")
    print(f"91-120: {b[3]:,.2f}")
    print(f">120:  {b[4]:,.2f}")

simulate(inc_cash=True, inc_net=True, inc_ret=True, inc_ext=False)
simulate(inc_cash=False, inc_net=False, inc_ret=False, inc_ext=False)
simulate(inc_cash=False, inc_net=True, inc_ret=False, inc_ext=False)

cur.close()
conn.close()
