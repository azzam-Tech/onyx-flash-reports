import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

# Fix 1: collection_adopted
old_calc = """(CASE WHEN :inc_rcpt='1' THEN SUM(rcpt) ELSE 0 END
             + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
             + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
             - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
             - 0) total_inc"""

new_calc = """(SUM(rcpt) + SUM(unposted_rcpt) + SUM(unposted_unknown) + SUM(rcpt_unknown)
             + CASE WHEN :inc_net='1'  THEN SUM(net_jrn) ELSE 0 END
             + CASE WHEN :inc_cash='1' THEN SUM(cash_sales) ELSE 0 END
             - CASE WHEN :inc_ret='1'  THEN SUM(cash_ret) ELSE 0 END
             ) total_inc"""

content = content.replace(old_calc, new_calc)

# Fix 2: perf_aging_dynamic & perf_aging_dynamic_analytical
# They use SQL queries for collections. Let's find them.
import re
def replacer(match):
    return match.group(0).replace("NVL(DOC_POST,0)=1", "NVL(DOC_POST,0) IN (0,1)")

# Search for sql_col inside run_perf_aging_fifo
# And run_perf_aging_analytical
sql_col_pattern = r'sql_col\s*=\s*"""(.*?)"""'
matches = list(re.finditer(sql_col_pattern, content, re.DOTALL))
print("Found sql_col queries:", len(matches))

for match in matches:
    sql_query = match.group(1)
    if "DOC_TYPE=2" in sql_query:
        print("Modifying a sql_col query...")
        new_sql = sql_query.replace("NVL(DOC_POST,0)=1", "NVL(DOC_POST,0) IN (0,1)")
        content = content[:match.start(1)] + new_sql + content[match.end(1):]

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'w', 'utf-8') as f:
    f.write(content)
print("Changes applied!")
