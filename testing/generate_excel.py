import os
import sys
import csv

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
    
    # 1. Find the top product by quantity for Salesman 144 in June 2026
    sql_top = """
    SELECT im.I_CODE, MAX(it.I_NAME) as I_NAME, SUM(im.I_QTY) as total_qty
    FROM IAS20261.ITEM_MOVEMENT im
    JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
    JOIN IAS20261.IAS_BILL_MST m 
        ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
       AND m.BILL_NO = im.DOC_NO 
       AND m.BILL_SER = im.DOC_SER
    WHERE m.REP_CODE = 144
      AND im.DOC_TYPE = 1 
      AND m.BILL_DATE BETWEEN TO_DATE('2026-06-01', 'YYYY-MM-DD') AND TO_DATE('2026-06-30', 'YYYY-MM-DD')
    GROUP BY im.I_CODE
    ORDER BY total_qty DESC
    FETCH FIRST 1 ROWS ONLY
    """
    cur.execute(sql_top)
    top_row = cur.fetchone()
    if not top_row:
        print("No sales found for this salesman in June 2026.")
        return
        
    top_icode, top_iname, top_qty = top_row
    print(f"Top Product: {top_icode} - {top_iname} (Qty: {top_qty})")

    # 2. Get details for this product
    sql_details = """
    SELECT 
        TO_CHAR(m.BILL_DATE, 'YYYY-MM-DD') as "تاريخ الفاتورة",
        im.DOC_NO as "رقم الفاتورة",
        im.I_QTY as "الكمية المباعة",
        NVL(d.I_PRICE, 0) as "سعر البيع للوحدة",
        (im.I_QTY * NVL(d.I_PRICE, 0)) as "إجمالي البيع",
        
        NVL(im.I_COST, 0) as "تكلفة فعلية للوحدة",
        (im.I_QTY * NVL(im.I_COST, 0)) as "إجمالي تكلفة فعلية",
        (im.I_QTY * NVL(d.I_PRICE, 0)) - (im.I_QTY * NVL(im.I_COST, 0)) as "الربح الفعلي",
        
        NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0)) as "تكلفة معيارية للوحدة",
        (im.I_QTY * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as "إجمالي تكلفة معيارية",
        (im.I_QTY * NVL(d.I_PRICE, 0)) - (im.I_QTY * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as "الربح المعياري"
        
    FROM IAS20261.ITEM_MOVEMENT im
    JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
    JOIN IAS20261.IAS_BILL_MST m 
        ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
       AND m.BILL_NO = im.DOC_NO 
       AND m.BILL_SER = im.DOC_SER
    JOIN IAS20261.IAS_BILL_DTL d
        ON d.BILL_DOC_TYPE = m.BILL_DOC_TYPE
       AND d.BILL_NO = m.BILL_NO
       AND d.BILL_SER = m.BILL_SER
       AND d.I_CODE = im.I_CODE
    WHERE m.REP_CODE = 144
      AND im.DOC_TYPE = 1 
      AND im.I_CODE = :1
      AND m.BILL_DATE BETWEEN TO_DATE('2026-06-01', 'YYYY-MM-DD') AND TO_DATE('2026-06-30', 'YYYY-MM-DD')
    ORDER BY m.BILL_DATE, im.DOC_NO
    """
    cur.execute(sql_details, [top_icode])
    columns = [col[0] for col in cur.description]
    rows = cur.fetchall()

    filename = "Top_Product_Sales_144.csv"
    with open(filename, 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.writer(f)
        writer.writerow(columns)
        for r in rows:
            writer.writerow(r)
            
    print(f"Report saved successfully to {filename}")

if __name__ == '__main__':
    main()
