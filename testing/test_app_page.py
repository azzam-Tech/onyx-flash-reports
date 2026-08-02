import urllib.request

try:
    resp = urllib.request.urlopen("http://127.0.0.1:5000/?tab=sales&report=debt_movement_summary&grp_by=customer")
    html = resp.read().decode('utf-8')
    if "خطأ:" in html:
        print("ERROR IN PAGE:", html[:300])
    else:
        print("SUCCESS! Debt movement summary page loaded properly.")
except Exception as e:
    print("FAILED TO FETCH PAGE:", e)
