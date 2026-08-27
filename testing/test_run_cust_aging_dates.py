import os
import sys
from dotenv import load_dotenv

load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\db.env")
sys.path.append(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")

from modules.ar.services import run_cust_aging

rpt = {}
for dt in ['2026-08-26', '2026-08-27', '2026-08-31']:
    args = {
        'rep_code': '144',
        'date_to': dt,
        'vendor_link': '0'
    }
    cols, rows = run_cust_aging(rpt, args)
    total = sum(float(r[-1].replace(',', '')) for r in rows)
    print(f"NO VENDOR ({dt}):", total)
    
    args['vendor_link'] = '1'
    cols, rows = run_cust_aging(rpt, args)
    total = sum(float(r[-1].replace(',', '')) for r in rows)
    print(f"VENDOR LINKED ({dt}):", total)
    print("-" * 30)
