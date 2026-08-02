import os
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

date_from = '2026-06-01'
date_to = '2026-06-30'
rep_code = '142'

print(f"--- Analyzing Rep {rep_code} for {date_from} to {date_to} ---")

# 1. Cash Sales
sql_cash = """
    SELECT SUM(NVL(p.DR_AMT,0))
    FROM IAS20261.IAS_BILL_MST b
    JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
    WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
      AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(b.REP_CODE) = :rep
"""
cur.execute(sql_cash, {"df": date_from, "dt": date_to, "rep": rep_code})
cash_sales = cur.fetchone()[0] or 0.0
print(f"Cash Sales: {cash_sales:,.2f}")

# 2. Cash Returns
sql_cash_ret = """
    SELECT SUM(NVL(CR_AMT,0))
    FROM IAS20261.IAS_POST_DTL
    WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND A_CODE LIKE '111%' AND C_CODE IS NULL AND NVL(CR_AMT,0)>0
      AND DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(REP_CODE) = :rep
"""
cur.execute(sql_cash_ret, {"df": date_from, "dt": date_to, "rep": rep_code})
cash_ret = cur.fetchone()[0] or 0.0
print(f"Cash Returns: {cash_ret:,.2f}")

# 3. Credits for Rep's Customers
sql_credits = """
    SELECT p.DOC_TYPE, p.JV_TYPE, SUM(NVL(p.CR_AMT,0))
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND NVL(p.CR_AMT,0) > 0
      AND p.DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(c.REP_CODE) = :rep
    GROUP BY p.DOC_TYPE, p.JV_TYPE
"""
cur.execute(sql_credits, {"df": date_from, "dt": date_to, "rep": rep_code})
credits_by_type = cur.fetchall()

rcpt = 0.0
net_jrn = 0.0
credit_ret = 0.0
ext_notice = 0.0
other = 0.0

print("\nCredits on Customers (by DOC_TYPE, JV_TYPE):")
for dtype, jvtype, amt in credits_by_type:
    print(f"  DOC_TYPE={dtype}, JV_TYPE={jvtype} : {amt:,.2f}")
    if dtype == 2:
        rcpt += amt
    elif dtype == 1 and jvtype == 2:
        net_jrn += amt
    elif dtype == 5:
        credit_ret += amt
    elif dtype == 15:
        ext_notice += amt
    else:
        other += amt

print(f"\nBreakdown Summary:")
print(f"  Receipts (DOC_TYPE 2): {rcpt:,.2f}")
print(f"  Net Journals (DOC_TYPE 1, JV 2): {net_jrn:,.2f}")
print(f"  Credit Returns (DOC_TYPE 5): {-credit_ret:,.2f}")
print(f"  External Notices (DOC_TYPE 15): {-ext_notice:,.2f}")
print(f"  Other Credits: {other:,.2f}")

total_our_script = rcpt + net_jrn - credit_ret + cash_sales - cash_ret
print(f"\nTotal calculated by OUR logic (Receipts + Net Journals - Credit Returns + Cash Sales - Cash Returns):")
print(f"  = {rcpt:,.2f} + {net_jrn:,.2f} - {credit_ret:,.2f} + {cash_sales:,.2f} - {cash_ret:,.2f}")
print(f"  = {total_our_script:,.2f}")

onyx_total = 2166028.83
diff = total_our_script - onyx_total
print(f"\nDifference with Onyx ({onyx_total:,.2f}): {diff:,.2f}")

cur.close()
conn.close()
