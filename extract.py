import re

with open('onyx_files/IAS_item_movement.rdf', 'rb') as f:
    data = f.read().decode('cp1256', errors='ignore')

# Extract SELECT queries
sqls = re.findall(r'SELECT\s+[\s\S]*?(?:FROM)[\s\S]*?(?:WHERE)[\s\S]*?(?:GROUP BY|ORDER BY|;|$)', data, re.IGNORECASE)

print(f"Found {len(sqls)} queries.")
for i, sql in enumerate(sqls):
    if 'ITEM_MOVEMENT' in sql.upper() or 'I_QTY' in sql.upper():
        print(f"\n--- QUERY {i+1} ---")
        print(sql[:2000])
