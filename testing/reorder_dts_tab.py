app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# Find tab=dts section
dts_idx = content.find('{"id":"dts"')
if dts_idx == -1:
    print("ERROR: tab=dts not found!")
    sys.exit(1)

# Move collection_adopted report to be first in dts reports array
# Locate collection_adopted block
ca_idx = content.find('{"id":"collection_adopted"', dts_idx)
if ca_idx == -1:
    print("ERROR: collection_adopted report not found in tab=dts!")
    sys.exit(1)

# We find the reports array start after dts_idx
rep_array_start = content.find('"reports":[', dts_idx) + len('"reports":[')

# Find the full block of collection_adopted report
ca_end = content.find('SELECT * FROM (\n        SELECT grp_code', ca_idx)
ca_end = content.find(') WHERE ROWNUM <= 300"""}', ca_idx) + len(') WHERE ROWNUM <= 300"""}')

ca_block = content[ca_idx:ca_end]

# Remove ca_block and leading/trailing comma from its current position
content_without_ca = content[:ca_idx].rstrip(', \n\r') + content[ca_end:]

# Re-insert ca_block right at the beginning of "reports":[" in dts
rep_array_start_new = content_without_ca.find('"reports":[', dts_idx) + len('"reports":[')
content_reordered = content_without_ca[:rep_array_start_new] + "\n        " + ca_block + ",\n        " + content_without_ca[rep_array_start_new:]

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content_reordered)

print("REORDERED TAB=DTS REPORTS SUCCESSFULLY!")
