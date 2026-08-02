import sys
sys.path.insert(0, r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

# 1. Check PRICE_LEVEL / PRC_LEVEL names or tables in Onyx DB
with get_conn() as con:
    with con.cursor() as cur:
        # Check price levels in IAS_ITEM_PRICE
        cur.execute("""
            SELECT p.PRC_LEVEL, COUNT(*) cnt, MIN(p.I_PRICE) min_p, MAX(p.I_PRICE) max_p
            FROM IAS20261.IAS_ITEM_PRICE p
            GROUP BY p.PRC_LEVEL
            ORDER BY p.PRC_LEVEL
        """)
        print("--- IAS_ITEM_PRICE LEVELS ---")
        for row in cur.fetchall():
            print(row)

        # Check price level lookup table if exists
        try:
            cur.execute("SELECT * FROM IAS20261.IAS_PRC_LEVEL")
            print("--- IAS_PRC_LEVEL TABLE ---")
            for row in cur.fetchall():
                print(row)
        except Exception as e:
            print("IAS_PRC_LEVEL table error:", e)

        # Check item price for sample item HIKT-100S4KWQ3
        cur.execute("""
            SELECT p.I_CODE, p.PRC_LEVEL, p.I_PRICE, p.UNIT_CODE
            FROM IAS20261.IAS_ITEM_PRICE p
            WHERE p.I_CODE LIKE '%HIKT-100S4KWQ3%' OR p.I_CODE = 'HIKT-100S4KWQ3'
        """)
        print("--- HIKT-100S4KWQ3 PRICES ---")
        for row in cur.fetchall():
            print(row)
