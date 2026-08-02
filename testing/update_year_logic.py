import re
import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "r", "utf-8") as f:
    content = f.read()

replacement = """
        # Inject dynamic dates if this report uses dynamic period params
        target_year = "2026" # fallback
        if "p_year" in binds and "p_type" in binds:
            target_year = str(binds["p_year"])
            d_from, d_to = calculate_dates(binds["p_year"], binds["p_type"], binds.get("p_val", 1))
            binds["date_from"] = d_from
            binds["date_to"] = d_to
        elif "date_from" in binds and binds["date_from"]:
            target_year = str(binds["date_from"])[:4]
            
        # Oracle throws ORA-01036 if we pass bind variables that aren't in the query.
        import re
        sql = rpt["sql"]
        
        # Dynamic Year Routing: Onyx stores data in schema per year, e.g. IAS20251 for 2025
        # So we dynamically replace the hardcoded IAS20261 with IAS[year]1
        if target_year.isdigit() and len(target_year) == 4:
            sql = sql.replace('IAS20261', f'IAS{target_year}1')
            
        used_binds = set(re.findall(r':([a-zA-Z0-9_]+)', sql))
"""

content = re.sub(
    r'# Inject dynamic dates if this report uses dynamic period params.*?used_binds = set\(re.findall\(r\':\(\[a-zA-Z0-9_\]\+\)\', sql\)\)',
    replacement.strip(),
    content,
    flags=re.DOTALL
)

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", "w", "utf-8") as f:
    f.write(content)
print("SUCCESS")
