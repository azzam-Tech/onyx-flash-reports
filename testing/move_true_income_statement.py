with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Find true_income_statement definition block
target = '{"id":"true_income_statement","title":"قائمة الدخل (الحقيقية)"'
start_pos = content.find(target)
end_pos = content.find('{"id":"dts","title":"التوزيع والمناديب"')

if start_pos == -1 or end_pos == -1:
    print(f"Error finding true_income_statement block: start={start_pos}, end={end_pos}")
    sys.exit(1)

# Extract true_income_statement block (from start_pos up to ending `"""},\n`)
block_end_marker = '"""},\n'
block_end = content.find(block_end_marker, start_pos)
if block_end == -1 or block_end >= end_pos:
    block_end = content.find('"""}', start_pos)
    block_len = len('"""}')
else:
    block_len = len(block_end_marker)

true_inc_block = content[start_pos:block_end + block_len].strip()
if true_inc_block.endswith(','):
    true_inc_block = true_inc_block[:-1].strip()

print("Extracted true_income_statement block successfully!")

# Remove true_income_statement from ar tab
# In ar tab, previous item was aging_dormant or statement
# Let's clean up content around start_pos
ar_cleaned = content[:start_pos].rstrip()
if ar_cleaned.endswith(','):
    ar_cleaned = ar_cleaned[:-1]

after_ar_cleaned = content[block_end + block_len:]

content_without_true_inc = ar_cleaned + "\n" + after_ar_cleaned

# 2. Add true_income_statement to prof tab
prof_marker = '{"id":"prof","title":"الربحية","icon":"M3 3v18h18M7 14l3-4 3 3 5-6","reports":['
prof_pos = content_without_true_inc.find(prof_marker)

if prof_pos == -1:
    print("Error finding prof tab marker!")
    sys.exit(1)

insert_pos = prof_pos + len(prof_marker)

new_content = content_without_true_inc[:insert_pos] + "\n    " + true_inc_block + ",\n" + content_without_true_inc[insert_pos:]

with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
    f.write(new_content)

print("Successfully moved true_income_statement to prof tab in app.py!")
