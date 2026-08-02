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

def get_all_prices_for_item():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    icode = "HIKT-100S4KWQ3"
    print(f"=== ALL RECORDED PRICES & COSTS FOR ITEM: '{icode}' ===")

    # 1. Master Item (IAS_ITM_MST)
    cur.execute("""
      SELECT I_CODE, I_NAME, PRIMARY_COST, INIT_PRIMARY_COST, VNDR_PRICE
      FROM IAS20261.IAS_ITM_MST WHERE I_CODE = :icode
    """, {"icode": icode})
    r1 = cur.fetchone()
    print("\n1️⃣  جدول الصنف الرئيسي (IAS_ITM_MST):")
    print(f"   - كود الصنف: {r1[0]}")
    print(f"   - اسم الصنف: {r1[1]}")
    print(f"   - التكلفة المعيارية الحالية (PRIMARY_COST): {r1[2]} ريال")
    print(f"   - التكلفة الافتتاحية المبدئية (INIT_PRIMARY_COST): {r1[3]} ريال")
    print(f"   - سعر الشراء المعتمد للمورد (VNDR_PRICE): {r1[4]} ريال")

    # 2. Price List Levels (IAS_ITEM_PRICE)
    print("\n2️⃣  قوائم أسعار البيع المعتمدة (IAS_ITEM_PRICE):")
    cur.execute("""
      SELECT LEV_NO, ITM_UNT, I_PRICE, TO_CHAR(AD_DATE,'YYYY-MM-DD HH24:MI'), TO_CHAR(UP_DATE,'YYYY-MM-DD HH24:MI')
      FROM IAS20261.IAS_ITEM_PRICE WHERE I_CODE = :icode
    """, {"icode": icode})
    rows2 = cur.fetchall()
    if rows2:
        for r in rows2:
            print(f"   - مستوى تسعير #{r[0]} ({r[1]}): سعر البيع = {r[2]} ريال (تاريخ الإضافة: {r[3]} | آخر تحديث: {r[4]})")
    else:
        print("   - لا توجد سجلاّت مخصصة في IAS_ITEM_PRICE.")

    # 3. Price History (IAS_ITEM_PRICE_HISTORY)
    print("\n3️⃣  سجل تاريخ تغير أسعار الصنف (IAS_ITEM_PRICE_HISTORY):")
    try:
        cur.execute("""
          SELECT LEV_NO, I_PRICE, PREV_I_PRICE, TO_CHAR(AUD_DATE,'YYYY-MM-DD HH24:MI'), AUD_U_ID
          FROM IAS20261.IAS_ITEM_PRICE_HISTORY WHERE I_CODE = :icode
          ORDER BY AUD_DATE ASC
        """, {"icode": icode})
        rows3 = cur.fetchall()
        if rows3:
            for r in rows3:
                print(f"   - بتاريخ {r[3]} (مستخدم #{r[4]}): مستوى #{r[0]} تغير من {r[2]} ريال ⬅️ إلى {r[1]} ريال")
        else:
            print("   - لم يُسجل تغير تاريخي في السعر لهذا الصنف.")
    except Exception as e:
        print("   Query history error:", e)

    # 4. Purchase Bills from Suppliers (IAS_PI_BILL_DTL)
    print("\n4️⃣  فواتير المشتريات التوريدية من الموردين (IAS_PI_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             b.V_NAME, d.I_QTY, d.I_PRICE
      FROM IAS20261.IAS_PI_BILL_DTL d
      JOIN IAS20261.IAS_PI_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      WHERE d.I_CODE = :icode
      ORDER BY b.BILL_DATE DESC
    """, {"icode": icode})
    rows4 = cur.fetchall()
    if rows4:
        for r in rows4:
            print(f"   - فاتورة شراء #{r[0]} بتاريخ {r[1]} (المورد: {r[2]}):")
            print(f"     * كمية الشراء: {r[3]} قطعة")
            print(f"     * سعر التوريد للقطعة: {r[4]} ريال")
    else:
        print("   - لا توجد فواتير مشتريات مسجلة لهذا الصنف.")

    # 5. Sales Invoices to Customers (IAS_BILL_DTL)
    print("\n5️⃣  أسعار فواتير المبيعات الفعلية للعملاء (IAS_BILL_DTL):")
    cur.execute("""
      SELECT b.BILL_NO, TO_CHAR(b.BILL_DATE,'YYYY-MM-DD'),
             c.C_A_NAME, d.I_QTY, d.I_PRICE, d.DIS_AMT, d.STK_COST,
             (d.I_QTY * d.I_PRICE - d.DIS_AMT) / d.I_QTY as net_unit_price,
             ((d.I_QTY * d.I_PRICE - d.DIS_AMT) * 1.15) / d.I_QTY as net_unit_with_vat
      FROM IAS20261.IAS_BILL_DTL d
      JOIN IAS20261.IAS_BILL_MST b ON b.BILL_DOC_TYPE=d.BILL_DOC_TYPE AND b.BILL_NO=d.BILL_NO AND b.BILL_SER=d.BILL_SER
      LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = b.C_CODE
      WHERE d.I_CODE = :icode AND d.I_QTY > 0
      ORDER BY b.BILL_DATE DESC
    """, {"icode": icode})
    rows5 = cur.fetchall()
    if rows5:
        print(f"   إجمالي فواتير المبيعات لهذا الصنف: {len(rows5)} فاتورة:")
        for r in rows5:
            print(f"   - فاتورة مبيعات #{r[0]} بتاريخ {r[1]} (العميل: {r[2]}):")
            print(f"     * الكمية المباعة: {r[3]} قطعة")
            print(f"     * السعر الخام المعلن: {r[4]} ريال")
            print(f"     * خصم السطر: {r[5]} ريال")
            print(f"     * الصافي (بدون ضريبة): {r[7]:,.2f} ريال")
            print(f"     * الصافي (شامل 15% ضريبة): {r[8]:,.2f} ريال")
            print(f"     * التكلفة المخزنية المحسوبة (STK_COST): {r[6]} ريال")
    else:
        print("   - لا توجد فواتير مبيعات مسجلة لهذا الصنف حتى الآن.")

    # 6. Central Movement Cost (ITEM_MOVEMENT)
    print("\n6️⃣  حركة وتكلفة المخزون المرجحة (ITEM_MOVEMENT):")
    cur.execute("""
      SELECT m.DOC_NO, m.DOC_TYPE, TO_CHAR(m.DOC_DATE,'YYYY-MM-DD'),
             m.I_QTY, m.STK_COST
      FROM IAS20261.ITEM_MOVEMENT m
      WHERE m.I_CODE = :icode AND ROWNUM <= 5
      ORDER BY m.DOC_DATE DESC
    """, {"icode": icode})
    rows6 = cur.fetchall()
    if rows6:
        for r in rows6:
            print(f"   - مستند حركة #{r[0]} (نوع {r[1]} بتاريخ {r[2]}): كمية {r[3]} | متوسط تكلفة المخزون وقت الحركة = {r[4]} ريال")

    conn.close()

if __name__ == "__main__":
    get_all_prices_for_item()
