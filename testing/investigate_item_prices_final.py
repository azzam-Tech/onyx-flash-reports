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

def test_final_prices():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sample_icode = "OS32ATVHD"
    print(f"=== COMPREHENSIVE PRICE & COST COMPARISON FOR ITEM: '{sample_icode}' ===")

    # 1. Master Item & Price Levels
    cur.execute("""
      SELECT I_CODE, I_NAME, PRIMARY_COST, INIT_PRIMARY_COST, VNDR_PRICE
      FROM IAS20261.IAS_ITM_MST WHERE I_CODE = :icode
    """, {"icode": sample_icode})
    r_mst = cur.fetchone()
    print("\n1️⃣  جدول الصنف الرئيسي (IAS_ITM_MST):")
    print(f"   - كود الصنف: {r_mst[0]}")
    print(f"   - اسم الصنف: {r_mst[1]}")
    print(f"   - PRIMARY_COST (التكلفة المعيارية الحالية): {r_mst[2]} ريال")
    print(f"   - INIT_PRIMARY_COST (التكلفة الافتتاحية المبدئية): {r_mst[3]} ريال")
    print(f"   - VNDR_PRICE (سعر الشراء المعتمد من المورد): {r_mst[4]} ريال")

    # 2. Price Levels (IAS_ITEM_PRICE)
    print("\n2️⃣  جدول قوائم الأسعار ومستويات البيع (IAS_ITEM_PRICE):")
    cur.execute("""
      SELECT * FROM IAS20261.IAS_ITEM_PRICE WHERE I_CODE = :icode
    """, {"icode": sample_icode})
    cols_p = [d[0] for d in cur.description]
    for r in cur.fetchall():
        row_dict = dict(zip(cols_p, r))
        print(f"   - {row_dict}")

    # 3. Item Price History (IAS_ITEM_PRICE_HISTORY)
    print("\n3️⃣  سجل تاريخ تغير أسعار الصنف (IAS_ITEM_PRICE_HISTORY):")
    cur.execute("""
      SELECT TO_CHAR(A_DATE,'YYYY-MM-DD'), I_PRICE, PREV_I_PRICE
      FROM IAS20261.IAS_ITEM_PRICE_HISTORY WHERE I_CODE = :icode AND ROWNUM <= 5
      ORDER BY A_DATE DESC
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        print(f"   - بتاريخ {r[0]}: تغير السعر من {r[2]} ريال ⬅️ إلى {r[1]} ريال")

    # 4. Actual Sales Bills (IAS_BILL_DTL)
    print("\n4️⃣  فواتير المبيعات الفعلية للعملاء (IAS_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             d.I_PRICE, d.DIS_AMT, d.I_QTY, d.STK_COST,
             (d.I_QTY * d.I_PRICE - d.DIS_AMT) / d.I_QTY as net_unit_no_vat,
             ((d.I_QTY * d.I_PRICE - d.DIS_AMT) * 1.15) / d.I_QTY as net_unit_with_vat
      FROM IAS20261.IAS_BILL_DTL d
      JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode AND d.I_QTY > 0 AND ROWNUM <= 5
      ORDER BY b.BILL_DATE DESC
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        bill_no, date, price, line_disc, qty, stk_cost, net_no_vat, net_vat = r
        print(f"   - فاتورة مبيعات #{bill_no} بتاريخ {date}:")
        print(f"     * كمية: {qty} | سعر الوحدة الخام قبل الخصم = {price} ريال")
        print(f"     * خصم السطر = {line_disc} ريال")
        print(f"     * صافي سعر الوحدة (بدون ضريبة) = {net_no_vat:.2f} ريال")
        print(f"     * صافي سعر الوحدة (شامل 15% ضريبة) = {net_vat:.2f} ريال")
        print(f"     * تكلفة مخزون الصنف وقت البيع (STK_COST) = {stk_cost} ريال")

    # 5. Purchase Bills (IAS_PI_BILL_DTL)
    print("\n5️⃣  فواتير المشتريات من الموردين (IAS_PI_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             d.I_PRICE, d.DISC_AMT, d.I_QTY
      FROM IAS20261.IAS_PI_BILL_DTL d
      JOIN IAS20261.IAS_PI_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode AND ROWNUM <= 5
      ORDER BY b.BILL_DATE DESC
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        bill_no, date, price, disc, qty = r
        print(f"   - فاتورة شراء #{bill_no} بتاريخ {date}: كمية {qty} بسعر شراء {price} ريال للوحدة (خصم {disc} ريال)")

    # 6. Inventory Weighted Average Movement Cost (ITEM_MOVEMENT)
    print("\n6️⃣  حركة وتكلفة المخزون المرجحة (ITEM_MOVEMENT):")
    cur.execute("""
      SELECT m.DOC_NO, m.DOC_TYPE, TO_CHAR(m.DOC_DATE,'YYYY-MM-DD'),
             m.I_QTY, m.STK_COST, m.I_COST
      FROM IAS20261.ITEM_MOVEMENT m
      WHERE m.I_CODE = :icode AND ROWNUM <= 5
      ORDER BY m.DOC_DATE DESC
    """, {"icode": sample_icode})
    for r in cur.fetchall():
        print(f"   - مستند حركة #{r[0]} (نوع {r[1]} - {r[2]}): كمية {r[3]} | متوسط تكلفة المخزون المرجح (STK_COST) = {r[4]} ريال")

    conn.close()

if __name__ == "__main__":
    test_final_prices()
