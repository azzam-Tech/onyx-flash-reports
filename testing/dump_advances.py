import sys
import json
sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

results = {}
with get_conn() as conn:
    with conn.cursor() as cur:
        # Check all accounts that start with 114
        cur.execute("SELECT A_CODE, A_NAME, A_NAME_ENG FROM ACCOUNT WHERE A_CODE LIKE '114%'")
        accs = cur.fetchall()
        for a in accs:
            results[a[0]] = a[1]

with open(r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\advances_accounts.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=4)
