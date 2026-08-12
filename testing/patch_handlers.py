import sys
import os

filepath = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\report_handlers.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Replace in run_cust_aging: if dtype == 5:
content = content.replace('if dtype == 5:', 'if dtype in (5, 15):')

# 2. Replace the SQL for run_cust_aging return links
old_sql_links = '''            # Fetch return links
            sql_links = f"""
                SELECT DISTINCT p.DOC_NO, p.DOC_SER, d.BILL_NO, d.BILL_SER
                FROM IAS20261.IAS_POST_DTL p
                JOIN IAS20261.IAS_RT_BILL_DTL d 
                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER
                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 
                  AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                  AND d.BILL_NO IS NOT NULL
                  {filter_str}
            """'''

new_sql_links = '''            # Fetch return and discount links
            sql_links = f"""
                SELECT DISTINCT p.DOC_NO, p.DOC_SER, d.BILL_NO, d.BILL_SER
                FROM IAS20261.IAS_POST_DTL p
                JOIN IAS20261.IAS_RT_BILL_DTL d 
                    ON p.DOC_NO = d.RT_BILL_NO AND p.DOC_SER = d.RT_BILL_SER
                WHERE p.DOC_TYPE = 5 AND p.CR_AMT > 0 
                  AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                  AND d.BILL_NO IS NOT NULL
                  {filter_str}
                UNION ALL
                SELECT DISTINCT p.DOC_NO, p.DOC_SER, p.REF_NO as BILL_NO, '' as BILL_SER
                FROM IAS20261.IAS_POST_DTL p
                WHERE p.DOC_TYPE = 15 AND p.CR_AMT > 0
                  AND p.DOC_DATE < TO_DATE(:dt, 'YYYY-MM-DD')+1
                  AND p.REF_NO IS NOT NULL
                  {filter_str}
            """'''

if old_sql_links in content:
    content = content.replace(old_sql_links, new_sql_links)
    print('Patched sql_links in run_cust_aging!')
else:
    print('Failed to find old_sql_links')

# 3. Fix the matching logic in run_cust_aging
old_match = '''                for deb in debits:
                    if deb["amt"] > 0 and deb["doc_no"] == b_no and deb["doc_ser"] == b_ser:'''
new_match = '''                for deb in debits:
                    if deb["amt"] > 0 and deb["doc_no"] == b_no and (b_ser == '' or deb["doc_ser"] == b_ser):'''

if old_match in content:
    content = content.replace(old_match, new_match)
    print('Patched loop in run_cust_aging!')
else:
    print('Failed to find old_match loop in run_cust_aging')

# 4. Patch sql_returns in run_perf_aging_fifo AND run_perf_aging_analytical
old_sql_returns = '''        # جلب المردودات وربطها بالفواتير
        sql_returns = """
            SELECT 
                r.DOC_TYPE_REF as bill_type,
                r.DOC_NO_REF as bill_no, 
                r.DOC_SER_REF as bill_ser,
                SUM(r.R_AMT) as ret_amt
            FROM IAS20261.IAS_RT_BILL_DTL r
            WHERE r.DOC_DATE <= TO_DATE(:date_to, 'YYYY-MM-DD')
            GROUP BY r.DOC_TYPE_REF, r.DOC_NO_REF, r.DOC_SER_REF
        """'''

new_sql_returns = '''        # جلب المردودات والخصومات وربطها بالفواتير
        sql_returns = """
            SELECT 
                bill_type, bill_no, bill_ser, SUM(amt) as ret_amt
            FROM (
                SELECT r.DOC_TYPE_REF as bill_type, r.DOC_NO_REF as bill_no, r.DOC_SER_REF as bill_ser, r.R_AMT as amt
                FROM IAS20261.IAS_RT_BILL_DTL r
                WHERE r.DOC_DATE <= TO_DATE(:date_to, 'YYYY-MM-DD')
                UNION ALL
                SELECT d.DOC_TYPE_REF as bill_type, d.DOC_NO_REF as bill_no, d.DOC_SER_REF as bill_ser, NVL(d.ADD_DISC_AMT_MST,0) + NVL(d.ADD_VAT_AMT,0) as amt
                FROM IAS20261.IAS_BILL_MST_ADD_DISC d
                WHERE d.DOC_DATE <= TO_DATE(:date_to, 'YYYY-MM-DD')
            )
            GROUP BY bill_type, bill_no, bill_ser
        """'''

if old_sql_returns in content:
    content = content.replace(old_sql_returns, new_sql_returns)
    print('Patched sql_returns in perf agings!')
else:
    print('Failed to find old_sql_returns')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done patching.")
