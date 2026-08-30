import sys
import json
sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

results = {}
with get_conn() as conn:
    with conn.cursor() as cur:
        # Sum of cash for rep 144
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0))
            FROM IAS_POST_DTL
            WHERE A_CODE LIKE '111%' AND (TO_CHAR(REP_CODE) = '144' OR TO_CHAR(CC_CODE) = '144')
              AND NVL(DOC_POST,0) = 1
        """)
        bal = cur.fetchone()[0]
        results['cash_balance_rep_144'] = bal

with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\rep_cash.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
