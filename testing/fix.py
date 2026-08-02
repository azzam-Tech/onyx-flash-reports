import codecs
import re

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

# Fix 1: collection_adopted
# Find: (CASE WHEN :inc_rcpt='1' THEN SUM(rcpt) ELSE 0 END ... - 0) total_inc
pattern1 = re.compile(r'\(CASE WHEN :inc_rcpt=\'1\' THEN SUM\(rcpt\) ELSE 0 END\s*\+\s*CASE WHEN :inc_net=\'1\'\s*THEN SUM\(net_jrn\) ELSE 0 END\s*\+\s*CASE WHEN :inc_cash=\'1\' THEN SUM\(cash_sales\) ELSE 0 END\s*-\s*CASE WHEN :inc_ret=\'1\'\s*THEN SUM\(cash_ret\) ELSE 0 END\s*-\s*0\)\s*total_inc')
if pattern1.search(content):
    content = pattern1.sub(r'(SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown) + SUM(rcpt_unknown)\n             + CASE WHEN :inc_net=\'1\'  THEN SUM(net_jrn) ELSE 0 END\n             + CASE WHEN :inc_cash=\'1\' THEN SUM(cash_sales) ELSE 0 END\n             - CASE WHEN :inc_ret=\'1\'  THEN SUM(cash_ret) ELSE 0 END\n             ) total_inc', content)
    print("Fixed collection_adopted calculation.")
else:
    print("pattern1 not found")

# Fix 2: perf_aging
pattern2 = re.compile(r'WHERE NVL\(p\.DOC_POST,0\)=1\s+AND \(NVL\(p\.DR_AMT,0\) > 0 OR NVL\(p\.CR_AMT,0\) > 0\)')
if pattern2.search(content):
    content = pattern2.sub(r'WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))\n                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)', content)
    print("Fixed perf_aging where clauses.")
else:
    print("pattern2 not found")

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'w', 'utf-8') as f:
    f.write(content)
