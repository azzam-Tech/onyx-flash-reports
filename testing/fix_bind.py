import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    lines = f.readlines()

new_lines = []
for line in lines:
    if "(SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown) + SUM(rcpt_unknown)" in line:
        new_lines.append(line.replace("(SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown) + SUM(rcpt_unknown)", "(CASE WHEN :inc_rcpt='1' THEN (SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown) + SUM(rcpt_unknown)) ELSE 0 END"))
    else:
        new_lines.append(line)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'w', 'utf-8') as f:
    f.writelines(new_lines)
