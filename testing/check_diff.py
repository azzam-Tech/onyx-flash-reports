import os
import sys

os.environ["NLS_LANG"] = ".AL32UTF8"
sys.stdout.reconfigure(encoding='utf-8')

import oracledb

_lib = r"C:\oracle\instantclient\instantclient_23_0"
try:
    oracledb.init_oracle_client(lib_dir=_lib)
except Exception:
    pass

DB_USER     = os.environ.get("ORA_USER",     "RPT_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD", "ULT2016")
DB_DSN      = os.environ.get("ORA_DSN",      "100.100.1.100:1521/ORCL")

def main():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()
    
    sql = """
    SELECT 
        im.DOC_NO,
        im.I_CODE,
        it.I_NAME,
        im.I_QTY,
        NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) as app_py_unit_cost,
        NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) * NVL(im.I_QTY,0) as app_py_total_cost,
        NVL(im.I_COST, 0) as doc_unit_cost,
        NVL(im.I_COST, 0) * NVL(im.I_QTY,0) as doc_total_cost
    FROM IAS20261.ITEM_MOVEMENT im
    JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
    JOIN IAS20261.IAS_BILL_MST m 
        ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
       AND m.BILL_NO = im.DOC_NO 
       AND m.BILL_SER = im.DOC_SER
    WHERE m.REP_CODE = 144
      AND im.DOC_TYPE = 1 
      AND m.BILL_DATE BETWEEN TO_DATE('2026-06-01', 'YYYY-MM-DD') AND TO_DATE('2026-06-30', 'YYYY-MM-DD')
      AND NVL(im.I_QTY,0) > 0
    """
    cur.execute(sql)
    rows = cur.fetchall()
    
    total_app = 0
    total_doc = 0
    diff_count = 0
    
    print(f"{'DOC_NO':<10} | {'I_CODE':<15} | {'QTY':<8} | {'APP_UCOST':<10} | {'DOC_UCOST':<10} | {'APP_TOT':<10} | {'DOC_TOT':<10} | {'DIFF':<10}")
    print("-" * 100)
    
    for r in rows:
        doc_no, icode, iname, qty, app_ucost, app_tot, doc_ucost, doc_tot = r
        total_app += app_tot
        total_doc += doc_tot
        
        diff = app_tot - doc_tot
        if abs(diff) > 0.01:
            diff_count += 1
            print(f"{doc_no:<10} | {icode:<15} | {qty:<8} | {app_ucost:<10.2f} | {doc_ucost:<10.2f} | {app_tot:<10.2f} | {doc_tot:<10.2f} | {diff:<10.2f}")
            
    print("-" * 100)
    print(f"Total APP (app.py) : {total_app:,.2f}")
    print(f"Total DOC (Invoice): {total_doc:,.2f}")
    print(f"Difference         : {total_app - total_doc:,.2f}")
    print(f"Number of mismatches: {diff_count}")

if __name__ == '__main__':
    main()
