import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

# First we find where {"id":"true_income_statement" starts
start_idx = content.find('{"id":"true_income_statement"')
if start_idx == -1:
    print("Not found")
    import sys
    sys.exit(1)

# we find the next line that starts with something like `     {"id":` or `   ]`
end_idx = content.find('{"id":"dormant"', start_idx) # Let's find a known anchor if any, wait, it's the last item in TABS
if end_idx == -1:
    # it might be the end of the list
    end_idx = content.find(']', start_idx)

# Let's just find the exact string that is duplicated
bad_string_start = content.find('"""}, 1, 5) as acc_code,')
if bad_string_start != -1:
    bad_string_end = content.find('    ] # End of ar tab', bad_string_start)
    if bad_string_end == -1:
        bad_string_end = content.find(']', bad_string_start)
    
    # We remove from bad_string_start up to bad_string_end
    content = content[:bad_string_start + 5] + "\n" + content[bad_string_end:]

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'w', 'utf-8') as f:
    f.write(content)
print("Fixed syntax error")
