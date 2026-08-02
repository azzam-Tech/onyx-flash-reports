app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update DFROM and DTO defaults to month 7 (July 2026)
content = content.replace('DFROM = {"name":"date_from","label":"من تاريخ","type":"date","default":"2026-01-01"}',
                          'DFROM = {"name":"date_from","label":"من تاريخ","type":"date","default":"2026-07-01"}')
content = content.replace('DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-10"}',
                          'DTO   = {"name":"date_to","label":"إلى تاريخ","type":"date","default":"2026-07-31"}')

# Update as_of defaults from 2026-07-10 to 2026-07-31
content = content.replace('"default":"2026-07-10"', '"default":"2026-07-31"')

# Update overview dashboard default dates to month 7
content = content.replace('"default":"2026-01-01"', '"default":"2026-07-01"')

# Update run_sql_report fallback dates
content = content.replace('val = val or ("2026-01-01" if "from" in pname else "2026-12-31")',
                          'val = val or ("2026-07-01" if "from" in pname else "2026-07-31")')

# Update run_perf_aging_fifo default dates
content = content.replace('if not date_from_str: date_from_str = "2026-06-01"', 'if not date_from_str: date_from_str = "2026-07-01"')
content = content.replace('if not date_to_str: date_to_str = "2026-06-30"', 'if not date_to_str: date_to_str = "2026-07-31"')

# 2. Optimize run_perf_aging_fifo SQL query with C_CODE IS NOT NULL and rep_code filter
old_fifo_sql = """            # Fetch relevant debits and credits from IAS_POST_DTL
            sql = \"\"\"
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
            \"\"\"
            cur.execute(sql)"""

new_fifo_sql = """            # Fetch relevant debits and credits from IAS_POST_DTL
            rep_filter = " AND (TO_CHAR(p.REP_CODE) = :rep_code OR TO_CHAR(p.CC_CODE) = :rep_code)" if rep_code else ""
            binds_fifo = {}
            if rep_code: binds_fifo["rep_code"] = rep_code
            sql = f\"\"\"
                SELECT p.C_CODE, p.DOC_DATE, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0), p.DOC_TYPE, p.JV_TYPE, p.A_CODE
                FROM IAS20261.IAS_POST_DTL p
                WHERE (NVL(p.DOC_POST,0)=1 OR (NVL(p.DOC_POST,0)=0 AND p.DOC_TYPE=2))
                    AND (NVL(p.DR_AMT,0) > 0 OR NVL(p.CR_AMT,0) > 0)
                    AND p.C_CODE IS NOT NULL
                    {rep_filter}
            \"\"\"
            cur.execute(sql, binds_fifo)"""

if old_fifo_sql in content:
    content = content.replace(old_fifo_sql, new_fifo_sql)
    print("Optimized run_perf_aging_fifo SQL query!")

with open(app_path, "w", encoding="utf-8") as f:
    f.write(content)

print("UPDATED DEFAULTS AND SPEEDUP IN APP.PY SUCCESSFULLY!")
