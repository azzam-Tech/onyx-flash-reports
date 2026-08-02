import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
import app

args = {
    "date_from": "2026-01-01",
    "date_to": "2026-07-31",
    "grp_by": "rep",
    "inc_rcpt": "1",
    "inc_net": "1",
    "inc_cash": "1",
    "inc_ret": "1"
}

rpt1 = None
rpt2 = None
for tab in app.TABS:
    for r in tab["reports"]:
        if r["id"] == "collection_adopted":
            rpt1 = r
        if r["id"] == "perf_aging_dynamic":
            rpt2 = r

cols1, rows1 = app.run_report(rpt1, args)
cols2, rows2 = app.run_perf_aging_fifo(rpt2, args)

total_col_adopted = sum([float(r[-1].replace(',', '')) for r in rows1 if r[-1]])
print("Collection Adopted Total:", total_col_adopted)

total_perf_aging = sum([float(r[-1].replace(',', '')) for r in rows2 if r[-1]])
print("Perf Aging Dynamic Total:", total_perf_aging)

print("Difference:", total_col_adopted - total_perf_aging)

dict1 = {r[0]: float(r[-1].replace(',', '')) for r in rows1}
dict2 = {r[0]: float(r[-1].replace(',', '')) for r in rows2}

for rep in set(list(dict1.keys()) + list(dict2.keys())):
    v1 = dict1.get(rep, 0.0)
    v2 = dict2.get(rep, 0.0)
    if abs(v1 - v2) > 0.01:
        print(f"Rep {rep}: ColAdopted={v1}, PerfAging={v2}, Diff={v1-v2}")
