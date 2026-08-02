import sys
import re

app_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'

with open(app_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace d["sales"]
old_sales = 'd["sales"]=sc("SELECT NVL(SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),0)'
new_sales = 'd["sales"]=sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0)'
content = content.replace(old_sales, new_sales)

# Replace d["purch"]
old_purch = 'd["purch"]=sc("SELECT NVL(SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)),0) FROM IAS20261.IAS_PI_BILL_MST'
new_purch = 'd["purch"]=sc("SELECT NVL(SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_PI_BILL_MST'
content = content.replace(old_purch, new_purch)

# Replace d["gross"]
old_gross = 'd["gross"]=sc("SELECT NVL(SUM(NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)),0)'
new_gross = 'd["gross"]=sc("SELECT NVL(SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))-NVL(x.I_QTY,0)*NVL(x.STK_COST,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)),0)'
content = content.replace(old_gross, new_gross)

# Replace ov
old_ov = 'ov=sc("SELECT NVL(SUM(NVL(VAT_AMT,0)),0) FROM IAS20261.IAS_BILL_MST'
new_ov = 'ov=sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_BILL_MST'
content = content.replace(old_ov, new_ov)

# Replace iv
old_iv = 'iv=sc("SELECT NVL(SUM(NVL(VAT_AMT,0)),0) FROM IAS20261.IAS_PI_BILL_MST'
new_iv = 'iv=sc("SELECT NVL(SUM(NVL(VAT_AMT,0) * DECODE(BILL_DOC_TYPE, 3, -1, 1)),0) FROM IAS20261.IAS_PI_BILL_MST'
content = content.replace(old_iv, new_iv)

# Replace msales
old_msales = 'SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) FROM IAS20261.IAS_BILL_MST'
new_msales = 'SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_BILL_MST'
content = content.replace(old_msales, new_msales)

# Replace mpurch
old_mpurch = 'SUM(NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) FROM IAS20261.IAS_PI_BILL_MST'
new_mpurch = 'SUM((NVL(BILL_AMT,0)-(NVL(DISC_AMT,0)-NVL(ADD_DISC_AMT_MST,0))+NVL(VAT_AMT,0)+NVL(OTHR_AMT,0)) * DECODE(BILL_DOC_TYPE, 3, -1, 1)) FROM IAS20261.IAS_PI_BILL_MST'
content = content.replace(old_mpurch, new_mpurch)

# Replace rep_labels
old_rep = 'SUM(NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) v FROM IAS20261.IAS_BILL_MST m'
new_rep = 'SUM((NVL(m.BILL_AMT,0)-(NVL(m.DISC_AMT,0)-NVL(m.ADD_DISC_AMT_MST,0))+NVL(m.VAT_AMT,0)+NVL(m.OTHR_AMT,0)) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) v FROM IAS20261.IAS_BILL_MST m'
content = content.replace(old_rep, new_rep)

# Replace itm_labels
old_itm = 'SUM(NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) v FROM IAS20261.IAS_BILL_DTL x'
new_itm = 'SUM((NVL(x.I_QTY,0)*(NVL(x.I_PRICE,0)-NVL(x.DIS_AMT,0)+NVL(x.OTHR_AMT,0))) * DECODE(m.BILL_DOC_TYPE, 3, -1, 1)) v FROM IAS20261.IAS_BILL_DTL x'
content = content.replace(old_itm, new_itm)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(content)

print("Dashboard queries successfully updated for accurate Return handling.")
