import sys
import os
sys.path.append(os.path.join(os.path.dirname('C:/Users/amarn/OneDrive/Desktop/dbOnyxOnAntigravity/'), 'privet', 'onyx_reports'))
from report_handlers import run_cust_aging

args = {'grp_code': '141', 'date_to': '2026-06-30', 'aging_ranges': '30, 60, 90, 120', 'vendor_link': '0'}

filepath = os.path.join(os.path.dirname('C:/Users/amarn/OneDrive/Desktop/dbOnyxOnAntigravity/'), 'privet', 'onyx_reports', 'report_handlers.py')
with open(filepath, 'r', encoding='utf-8') as f:
    code = f.read()

new_code = code.replace(
    '        for ret in returns:',
    '        if c_id == "1035":\n            print("DOC NOS:", [r["doc_no"] for r in returns])\n            print("LINKED INVS:", [r["linked_inv"] for r in returns])\n        for ret in returns:'
)

exec(new_code, globals())
cols, rows = run_cust_aging({'id': 'aging'}, args)
