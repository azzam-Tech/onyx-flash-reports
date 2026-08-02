import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

# Fix the column "إشعار خصم مستقل (-)" to show 0 if not included
old_sql_column = "TO_CHAR(SUM(NVL(d.ext_disc, 0)),'FM999,999,999,990.00') AS \"إشعار خصم مستقل (-)\","
new_sql_column = "TO_CHAR(CASE WHEN :inc_ext = '1' THEN SUM(NVL(d.ext_disc, 0)) ELSE 0 END,'FM999,999,999,990.00') AS \"إشعار خصم مستقل (-)\","

if old_sql_column in content:
    content = content.replace(old_sql_column, new_sql_column)
    print("Fixed ext_disc column display")
else:
    print("Could not find old_sql_column")

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
