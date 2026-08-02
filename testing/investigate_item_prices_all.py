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

def test_all_prices():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sample_icode = "OS32ATVHD"
    print(f"=== FULL PRICE & COST INVESTIGATION FOR ITEM: '{sample_icode}' ===")

    # 1. Master Item Table (IAS_ITM_MST)
    print("\n📌 1. MASTER ITEM TABLE (IAS20261.IAS_ITM_MST):")
    cur.execute("""
      SELECT I_CODE, I_NAME, PRIMARY_COST, INIT_PRIMARY_COST, VNDR_PRICE
      FROM IAS20261.IAS_ITM_MST WHERE I_CODE = :icode
    """, {"icode": sample_icode})
    r1 = cur.fetchone()
    print(f"   Code: {r1[0]} | Name: {r1[1]}")
    print(f"   - PRIMARY_COST (التكلفة الأولية/المخزنية المعيارية): {r1[2]}")
    print(f"   - INIT_PRIMARY_COST (التكلفة الافتتاحية المبدئية): {r1[3]}")
    print(f"   - VNDR_PRICE (سعر الشراء من المورد / سعر المورد): {r1[4]}")

    # 2. Units & Unit Prices (IAS_ITEM_UNITS / IAS_ITM_UNIT_PRICE / IAS_ITM_PRICELIST)
    print("\n📌 2. UNITS & PRICELISTS (IAS20261.IAS_ITEM_UNITS):")
    try:
        cur.execute("""
          SELECT UNIT_CODE, WHOLESALE_PRICE, RETAIL_PRICE, MIN_RETAIL_PRICE, PURCH_PRICE
          FROM IAS20261.IAS_ITEM_UNITS WHERE I_CODE = :icode
        """, {"icode": sample_icode})
        for r in cur.fetchall():
            print(f"   Unit '{r[0]}': WHOLESALE_PRICE={r[1]}, RETAIL_PRICE={r[2]}, MIN_RETAIL={r[3]}, PURCH_PRICE={r[4]}")
    except Exception as e:
        print("   Query IAS_ITEM_UNITS error:", e)

    # Search all tables with 'PRICE' or 'PRC' or 'COST' or 'UNIT'
    cur.execute("""
      SELECT table_name FROM all_tables 
      WHERE owner='IAS20261' 
        AND (table_name LIKE '%PRICE%' OR table_name LIKE '%PRC%' OR table_name LIKE '%UNITS%' OR table_name LIKE '%ITEM%')
      ORDER BY table_name
    """)
    itm_tables = [r[0] for r in cur.fetchall()]
    print("\nAll Item/Price/Unit tables in DB:", itm_tables)

    for tbl in itm_tables:
        try:
            cur.execute(f"SELECT column_name FROM all_tab_columns WHERE owner='IAS20261' AND table_name='{tbl}' AND column_name='I_CODE'")
            if cur.fetchone():
                cur.execute(f"SELECT * FROM IAS20261.{tbl} WHERE I_CODE = :icode AND ROWNUM <= 2", {"icode": sample_icode})
                cols = [d[0] for d in cur.description]
                rows = cur.fetchall()
                if rows:
                    print(f"\n📍 Found data for {sample_icode} in table 'IAS20261.{tbl}':")
                    for r in rows:
                        p_vals = {c: val for c, val in zip(cols, r) if val is not None and any(k in c.upper() for k in ['PRICE', 'COST', 'PRC', 'AMT', 'UNIT', 'VAL', 'DISC', 'RATE', 'PUR'])}
                        print("   Prices/Costs:", p_vals)
        except Exception:
            pass

    # 3. Actual Sales Invoices (IAS_BILL_DTL)
    print("\n📌 3. ACTUAL SALES INVOICES (IAS20261.IAS_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             d.I_PRICE as gross_price,
             d.DIS_AMT as line_disc,
             d.I_QTY as qty,
             ROUND((d.I_QTY * d.I_PRICE - d.DIS_AMT) / d.I_QTY, 2) as net_unit_price,
             NVL(d.TAX_VAL,0) / d.I_QTY as vat_per_unit,
             ROUND((d.I_QTY * d.I_PRICE - d.DIS_AMT + NVL(d.TAX_VAL,0)) / d.I_QTY, 2) as unit_price_with_vat,
             d.STK_COST as stock_cost_at_sale
      FROM IAS20261.IAS_BILL_DTL d
      JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode AND d.I_QTY > 0 AND ROWNUM <= 5
      ORDER BY b.BILL_DATE DESC
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        print(f"   Bill #{r[0]} ({r[1]}): Qty={r[4]} | Gross Unit Price={r[2]} | Line Disc={r[3]} | Net Unit (excl VAT)={r[5]} | Unit (WITH 15% VAT)={r[7]} | Stock Cost={r[8]}")

    # 4. Purchase Invoices (IAS_PI_BILL_DTL)
    print("\n📌 4. PURCHASE INVOICES FROM SUPPLIERS (IAS20261.IAS_PI_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             d.I_PRICE as purchase_price,
             d.DISC_AMT as purchase_disc,
             d.I_QTY as qty
      FROM IAS20261.IAS_PI_BILL_DTL d
      JOIN IAS20261.IAS_PI_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode AND ROWNUM <= 5
      ORDER BY b.BILL_DATE DESC
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        print(f"   Purchase Bill #{r[0]} ({r[1]}): Qty={r[4]} | Purchase Unit Price={r[2]} | Purch Disc={r[3]}")

    conn.close()

if __name__ == "__main__":
    test_all_prices()
