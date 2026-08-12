import sys
import os
filepath = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\report_handlers.py'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix in run_cust_aging
old_match = '''                for deb in debits:
                    if deb["amt"] > 0 and deb["doc_no"] == b_no and (not b_ser or deb["doc_ser"] == b_ser):'''
new_match = '''                for deb in debits:
                    if deb["amt"] > 0 and str(deb["doc_no"]) == str(b_no) and (not b_ser or str(deb["doc_ser"]) == str(b_ser)):'''

content = content.replace(old_match, new_match)

# Fix in run_perf_aging_fifo
old_match_perf = '''                for deb in debits:
                    if deb["amt"] > 0 and deb["doc_no"] == b_no and (b_ser == '' or deb["doc_ser"] == b_ser):'''
new_match_perf = '''                for deb in debits:
                    if deb["amt"] > 0 and str(deb["doc_no"]) == str(b_no) and (not b_ser or str(deb["doc_ser"]) == str(b_ser)):'''

content = content.replace(old_match_perf, new_match_perf)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Done fixing str() matching.")
