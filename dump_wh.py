import sys
sys.path.append('privet/onyx_reports')
import database
import json

query = """
SELECT W_CODE, W_NAME 
FROM IAS20261.WAREHOUSE_DETAILS 
"""
mapping = {}
with database.get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute(query)
        for row in cur.fetchall():
            mapping[str(row[0])] = row[1]

with open('wh_dump.json', 'w', encoding='utf-8') as f:
    json.dump(mapping, f, ensure_ascii=False, indent=2)

print("Dumped to wh_dump.json")
