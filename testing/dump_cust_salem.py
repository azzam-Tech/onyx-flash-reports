import sys
import json
sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

results = {}
with get_conn() as conn:
    with conn.cursor() as cur:
        for ccode in ['1022', '2073']:
            cur.execute("""
                SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
                FROM IAS_POST_DTL
                WHERE C_CODE = :ccode AND NVL(DOC_POST,0) = 1
            """, {'ccode': ccode})
            bal = cur.fetchone()[0]
            if bal is None: bal = 0
            results[f"Customer_{ccode}"] = bal

with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\cust_salem.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
