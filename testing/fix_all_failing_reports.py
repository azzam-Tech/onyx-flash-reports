with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

# 1. Fix stray comma in by_salesman
old_by_salesman_err = "       ),\n         UNION ALL"
new_by_salesman_fix = "       )\n         UNION ALL"

if old_by_salesman_err in content:
    content = content.replace(old_by_salesman_err, new_by_salesman_fix)
    print("Fixed stray comma in by_salesman SQL query!")

# 2. Add "fn":"run_perf_aging_fifo" to perf_aging_dynamic_analytical and perf_aging_dynamic
old_dyn_ana = '{"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT]'
new_dyn_ana = '{"id":"perf_aging_dynamic_analytical","title":"أعمار التحصيل الصافي (تحليلي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT]'

if old_dyn_ana in content:
    content = content.replace(old_dyn_ana, new_dyn_ana)
    print("Added fn: run_perf_aging_fifo to perf_aging_dynamic_analytical!")

old_dyn = '{"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT]'
new_dyn = '{"id":"perf_aging_dynamic","title":"أعمار التحصيل الصافي (ديناميكي)","fn":"run_perf_aging_fifo","params":[DFROM,DTO,REP,AGETR,INCR,INCN,INCC,INCRT]'

if old_dyn in content:
    content = content.replace(old_dyn, new_dyn)
    print("Added fn: run_perf_aging_fifo to perf_aging_dynamic!")

with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Finished fixing failing reports in app.py!")
