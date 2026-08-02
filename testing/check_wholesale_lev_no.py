import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # Check all LEV_NO values and sample item prices
        cur.execute("""
            SELECT LEV_NO, I_CODE, ITM_UNT, I_PRICE
            FROM IAS20261.IAS_ITEM_PRICE
            WHERE I_CODE LIKE '%HIKT-100S4KWQ3%' OR I_CODE = 'HIKT-100S4KWQ3'
            ORDER BY LEV_NO
        """)
        rows = cur.fetchall()
        print("--- HIKT-100S4KWQ3 IN IAS_ITEM_PRICE ---")
        for r in rows:
            print(f"LEV_NO: {r[0]}, Item: {r[1]}, Unit: {r[2]}, Price: {r[3]}")

        # Check overall LEV_NO counts in IAS_ITEM_PRICE
        cur.execute("""
            SELECT LEV_NO, COUNT(*) cnt, AVG(I_PRICE) avg_p, MIN(I_PRICE) min_p, MAX(I_PRICE) max_p
            FROM IAS20261.IAS_ITEM_PRICE
            WHERE I_PRICE IS NOT NULL AND I_PRICE > 0
            GROUP BY LEV_NO
            ORDER BY LEV_NO
        """)
        print("\n--- ALL LEV_NO SUMMARY IN IAS_ITEM_PRICE ---")
        for r in cur.fetchall():
            print(f"LEV_NO: {r[0]}, Count: {r[1]}, Avg Price: {r[2]:,.2f}, Min: {r[3]:,.2f}, Max: {r[4]:,.2f}")
