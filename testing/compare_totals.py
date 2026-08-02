import urllib.request
import re

html1 = urllib.request.urlopen("http://127.0.0.1:5000/?tab=dts&report=perf_aging_dynamic&date_from=2026-01-01&date_to=2026-07-23&inc_rcpt=1&inc_net=1&inc_cash=1&inc_ret=1").read().decode('utf-8')
html2 = urllib.request.urlopen("http://127.0.0.1:5000/?tab=dts&report=collection_adopted&date_from=2026-01-01&date_to=2026-07-23&inc_rcpt=1&inc_net=1&inc_cash=1&inc_ret=1&grp_by=rep").read().decode('utf-8')

def extract_totals(html):
    matches = re.findall(r'<tr>(.*?)</tr>', html, flags=re.DOTALL)
    totals = {}
    for m in matches:
        if '<th>' in m: continue
        tds = re.findall(r'<td.*?>(.*?)</td>', m, flags=re.DOTALL)
        if len(tds) >= 9:
            rep = tds[0].strip()
            # remove html tags from tds
            tot = re.sub(r'<.*?>', '', tds[-1]).strip().replace(',', '')
            if 'الإجمالي' in rep: continue
            try:
                totals[rep] = float(tot)
            except:
                pass
    return totals

tot1 = extract_totals(html1)
tot2 = extract_totals(html2)

print(f"{'Rep':<5} | {'Perf Aging':<15} | {'Col Adopted':<15} | {'Diff':<15}")
print("-" * 55)
all_reps = set(list(tot1.keys()) + list(tot2.keys()))
for rep in sorted(all_reps):
    t1 = tot1.get(rep, 0.0)
    t2 = tot2.get(rep, 0.0)
    if abs(t1 - t2) > 0.01:
        print(f"{rep:<5} | {t1:<15.2f} | {t2:<15.2f} | {t1-t2:<15.2f}")
