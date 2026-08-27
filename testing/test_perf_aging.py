import os
import sys
from dotenv import load_dotenv

load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\db.env")
sys.path.append(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")

from modules.fin.services import run_perf_aging_fifo

rpt = {'id': 'perf_aging_fifo'}
args = {
    'rep_code': '144',
    'date_to': '2026-08-31',
    'vendor_link': '0'
}

cols, rows = run_perf_aging_fifo(rpt, args)
total = sum(float(r[-1].replace(',', '')) for r in rows)
print("PERF AGING (NO VENDOR):", total)
