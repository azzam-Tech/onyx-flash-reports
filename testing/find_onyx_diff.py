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

# We want to know exactly what Onyx includes in its 2,166,028.83 total
# Onyx is an Aging Report, which means it probably calculates "Collections" or "Net Paid" for the period.
# Our total is 2,523,880.10

cur.execute("""
    SELECT p.DOC_TYPE, p.JV_TYPE, SUM(NVL(p.CR_AMT,0)) as amt
    FROM IAS20261.IAS_POST_DTL p
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 AND NVL(p.CR_AMT,0) > 0
      AND p.DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND p.DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(c.REP_CODE) = :rep
    GROUP BY p.DOC_TYPE, p.JV_TYPE
""", {"df": date_from, "dt": date_to, "rep": rep_code})
cust_credits = cur.fetchall()

cur.execute("""
    SELECT SUM(NVL(p.DR_AMT,0)) as amt
    FROM IAS20261.IAS_BILL_MST b
    JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%'
    WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0
      AND b.BILL_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND TO_CHAR(b.REP_CODE) = :rep
""", {"df": date_from, "dt": date_to, "rep": rep_code})
cash_sales = cur.fetchone()[0] or 0.0

print("Components:")
components = {}
for dtype, jvtype, amt in cust_credits:
    components[f"CR_DOC_{dtype}_JV_{jvtype}"] = amt
components["CASH_SALES"] = cash_sales

for k, v in components.items():
    print(f"{k}: {v:,.2f}")

# Onyx Total
onyx_total = 2166028.83
diff = 2523880.10 - onyx_total
print(f"\nDifference to find: {diff:,.2f}")

# Wait, Onyx might subtract discounts? 
# DOC_TYPE=2, JV_TYPE=2 is 1,676,258.01. What if this includes a massive discount?
# In Onyx, Receipt Vouchers (DOC_TYPE=2) can have discounts (DIS_AMT). If we sum CR_AMT in IAS_POST_DTL, it includes the full credit to the customer (Cash + Discount).
# Does Onyx's aging report consider the "Discount" as a Collection?
# Let's check how much discount there is in DOC_TYPE=2 for these customers.
cur.execute("""
    SELECT SUM(NVL(DIS_AMT,0))
    FROM IAS20261.IAS_RCPT_MST r
    WHERE r.DOC_DATE >= TO_DATE(:df,'YYYY-MM-DD') AND r.DOC_DATE < TO_DATE(:dt,'YYYY-MM-DD')+1
      AND r.C_CODE IN (SELECT C_CODE FROM IAS20261.CUSTOMER WHERE REP_CODE = :rep)
      AND NVL(r.DOC_POST,0)=1
""", {"df": date_from, "dt": date_to, "rep": rep_code})
rcpt_discounts = cur.fetchone()[0] or 0.0
print(f"\nDiscounts inside Receipts (DOC_TYPE 2): {rcpt_discounts:,.2f}")

# Let's check if the difference (357,851.27) is Cash Sales (238,921.84) + Discounts (???) + something else.
# Or maybe Onyx doesn't include JV_TYPE=2 ?
# Net Journals (CR_DOC_1_JV_2) = 78,186.00
print(f"Cash Sales + Net Journals = {cash_sales + components.get('CR_DOC_1_JV_2', 0):,.2f}")
print(f"Cash Sales + Net Journals + Discounts = {cash_sales + components.get('CR_DOC_1_JV_2', 0) + rcpt_discounts:,.2f}")

cur.close()
conn.close()
