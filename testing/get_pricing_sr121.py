import oracledb
import os

# Set Oracle environment
os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")

DB_USER = "RPT_USER"
DB_PASSWORD = "ULT2016"
DB_DSN = "100.100.1.100:1521/ORCL"

def get_pricing_info(item_no):
    print(f"Fetching pricing info for item: {item_no}\n")
    try:
        oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
        conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
        cur = conn.cursor()

        # 1. Master Item metrics (IAS_ITM_MST)
        cur.execute("""
            SELECT PRIMARY_COST, INIT_PRIMARY_COST, VNDR_PRICE, I_NAME
            FROM IAS_ITM_MST
            WHERE I_CODE = :item_no
        """, item_no=item_no)
        res = cur.fetchone()
        if res:
            print(f"--- 1. Master Item metrics (IAS_ITM_MST) ---")
            print(f"Item Name: {res[3]}")
            print(f"PRIMARY_COST (Standard Unit Cost): {res[0]}")
            print(f"INIT_PRIMARY_COST (Initial Opening Cost): {res[1]}")
            print(f"VNDR_PRICE (Default Vendor Price): {res[2]}\n")
        else:
            print("Item not found in IAS_ITM_MST.\n")

        # 2. Sales Price Lists (IAS_ITEM_PRICE)
        cur.execute("""
            SELECT LEV_NO, I_PRICE, ITM_UNT
            FROM IAS_ITEM_PRICE
            WHERE I_CODE = :item_no
            ORDER BY LEV_NO
        """, item_no=item_no)
        prices = cur.fetchall()
        if prices:
            print(f"--- 2. Sales Price Lists (IAS_ITEM_PRICE) ---")
            for p in prices:
                level_name = "سعر الجملة" if p[0] == 1 else "سعر التجزئة" if p[0] == 2 else f"Level {p[0]}"
                print(f"Level {p[0]} ({level_name}): {p[1]} (Unit: {p[2]})")
            print()
        else:
            print("No price lists found in IAS_ITEM_PRICE.\n")

        # 3. Stock Cost / WAC (ITEM_MOVEMENT)
        cur.execute("""
            SELECT STK_COST, I_COST, I_DATE
            FROM ITEM_MOVEMENT
            WHERE I_CODE = :item_no
            ORDER BY I_DATE DESC
            FETCH FIRST 5 ROWS ONLY
        """, item_no=item_no)
        movements = cur.fetchall()
        if movements:
            print(f"--- 3. Recent Stock Costs / WAC (ITEM_MOVEMENT) ---")
            for m in movements:
                print(f"Date: {m[2]}, STK_COST: {m[0]}, I_COST: {m[1]}")
            print()
        else:
            print("No movements found in ITEM_MOVEMENT.\n")

        # 4. Purchase Prices (IAS_PI_BILL_DTL)
        cur.execute("""
            SELECT m.BILL_DATE, d.I_PRICE, d.DIS_AMT, d.I_QTY
            FROM IAS_PI_BILL_DTL d
            JOIN IAS_PI_BILL_MST m ON m.BILL_NO = d.BILL_NO AND m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_SER = d.BILL_SER
            WHERE d.I_CODE = :item_no
            ORDER BY m.BILL_DATE DESC
            FETCH FIRST 5 ROWS ONLY
        """, item_no=item_no)
        purchases = cur.fetchall()
        if purchases:
            print(f"--- 4. Recent Purchase Invoices (IAS_PI_BILL_DTL) ---")
            for p in purchases:
                print(f"Date: {p[0]}, Vendor Price: {p[1]}, Discount: {p[2]}, Qty: {p[3]}")
            print()
        else:
            print("No purchase invoices found.\n")

        # 5. Sales Prices (IAS_BILL_DTL)
        cur.execute("""
            SELECT m.BILL_DATE, d.I_PRICE, d.DIS_AMT, d.STK_COST, d.I_QTY
            FROM IAS_BILL_DTL d
            JOIN IAS_BILL_MST m ON m.BILL_NO = d.BILL_NO AND m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_SER = d.BILL_SER
            WHERE d.I_CODE = :item_no
            ORDER BY m.BILL_DATE DESC
            FETCH FIRST 5 ROWS ONLY
        """, item_no=item_no)
        sales = cur.fetchall()
        if sales:
            print(f"--- 5. Recent Sales Invoices (IAS_BILL_DTL) ---")
            for s in sales:
                net_price = ((s[4] * s[1]) - s[2]) / s[4] if s[4] and s[4] > 0 else s[1]
                print(f"Date: {s[0]}, Qty: {s[4]}, Declared Price: {s[1]}, Discount: {s[2]}, Stock Cost: {s[3]}, Net Price: {net_price:.2f}, With VAT (15%): {net_price * 1.15:.2f}")
            print()
        else:
            print("No sales invoices found.\n")

        cur.close()
        conn.close()

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    get_pricing_info('SR121.')
