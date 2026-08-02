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

def test_targeted_prices():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sample_icode = "OS32ATVHD"
    print(f"=== TARGETED PRICE INVESTIGATION FOR ITEM: '{sample_icode}' ===")

    # 1. Master Item Table (IAS_ITM_MST)
    print("\n📌 1. MASTER ITEM TABLE (IAS20261.IAS_ITM_MST):")
    cur.execute("""
      SELECT * FROM IAS20261.IAS_ITM_MST WHERE I_CODE = :icode
    """, {"icode": sample_icode})
    cols1 = [d[0] for d in cur.description]
    row1 = cur.fetchone()
    for c, v in zip(cols1, row1):
        if any(k in c.upper() for k in ['PRICE', 'COST', 'PRC', 'AMT', 'RATE', 'SAL', 'PUR', 'DISC', 'MIN', 'MAX', 'VAL']):
            print(f"   - {c}: {v}")

    # 2. Item Units Table (IAS_ITM_UNIT)
    print("\n📌 2. ITEM UNITS TABLE (IAS20261.IAS_ITM_UNIT):")
    cur.execute("""
      SELECT * FROM IAS20261.IAS_ITM_UNIT WHERE I_CODE = :icode
    """, {"icode": sample_icode})
    cols2 = [d[0] for d in cur.description]
    rows2 = cur.fetchall()
    for r in rows2:
        print("   Unit record:")
        for c, v in zip(cols2, r):
            if any(k in c.upper() for k in ['PRICE', 'COST', 'PRC', 'AMT', 'RATE', 'SAL', 'PUR', 'DISC', 'MIN', 'MAX', 'VAL', 'UNIT']):
                print(f"     - {c}: {v}")

    # 3. Price List Details
    print("\n📌 3. PRICE LIST TABLES IN SYSTEM:")
    cur.execute("""
      SELECT table_name FROM all_tables WHERE owner='IAS20261' AND (table_name LIKE '%PRICE%' OR table_name LIKE '%PRC%')
    """)
    prc_tables = [r[0] for r in cur.fetchall()]
    print("   Price List tables found:", prc_tables)

    for pt in prc_tables:
        try:
            cur.execute(f"SELECT * FROM IAS20261.{pt} WHERE ROWNUM <= 2")
            p_cols = [d[0] for d in cur.description]
            p_rows = cur.fetchall()
            print(f"   Table '{pt}' sample rows: {len(p_rows)}")
            for pr in p_rows:
                print("    ", dict(zip(p_cols[:10], pr[:10])))
        except Exception as e:
            print(f"   Table '{pt}' query error: {e}")

    # 4. Actual Sales Invoice Detail (IAS_BILL_DTL)
    print("\n📌 4. ACTUAL SALES INVOICES (IAS20261.IAS_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             d.I_PRICE, d.DIS_AMT, d.I_QTY, d.TAX_VAL, d.STK_COST
      FROM IAS20261.IAS_BILL_DTL d
      JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode AND d.I_QTY > 0 AND ROWNUM <= 3
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        bill_no, bill_date, price, line_disc, qty, tax_val, stk_cost = r
        net_unit = (qty * price - line_disc) / qty
        net_unit_vat = (qty * price - line_disc + NVL(tax_val,0)) / qty
        print(f"   Bill #{bill_no} ({bill_date}): Qty={qty} | Gross Price={price} | Line Disc={line_disc} | Net Unit (excl. VAT)={net_unit:.2f} | Net Unit (WITH VAT)={net_unit_vat:.2f} | Stock Cost={stk_cost}")

    # 5. Purchase Invoices (IAS_PI_BILL_DTL)
    print("\n📌 5. PURCHASE INVOICES FROM SUPPLIERS (IAS20261.IAS_PI_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             d.I_PRICE, d.DISC_AMT, d.I_QTY
      FROM IAS20261.IAS_PI_BILL_DTL d
      JOIN IAS20261.IAS_PI_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode AND ROWNUM <= 3
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        bill_no, bill_date, price, disc, qty = r
        print(f"   Purch Bill #{bill_no} ({bill_date}): Qty={qty} | Purch Unit Price={price} | Disc={disc}")

    conn.close()

if __name__ == "__main__":
    test_targeted_prices()
