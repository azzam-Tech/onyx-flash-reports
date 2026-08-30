import sys
import json
sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

results = {}
with get_conn() as conn:
    with conn.cursor() as cur:
        # Search for any account related to محمد سالم or 144
        cur.execute("SELECT A_CODE, A_NAME, A_NAME_ENG FROM ACCOUNT WHERE (A_NAME LIKE '%محمد سالم%' OR A_CODE LIKE '%144%')")
        accounts = cur.fetchall()
            
        for acc in accounts:
            acode = acc[0]
            cur.execute("""
                SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
                FROM IAS_POST_DTL
                WHERE A_CODE = :acode AND NVL(DOC_POST,0) = 1
            """, {'acode': acode})
            bal = cur.fetchone()[0]
            results[acode] = {
                'name': acc[1],
                'balance': bal
            }

with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\balance_results2.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
