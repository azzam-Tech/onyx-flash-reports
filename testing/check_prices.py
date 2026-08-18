import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def explore_pricing():
    with get_conn() as con:
        with con.cursor() as cur:
            cur.execute("SELECT LEV_NO, LEV_A_NAME FROM IAS_PRICING_LEVELS")
            print("Pricing Levels (IAS_PRICING_LEVELS):")
            for r in cur.fetchall():
                print(f"{r[0]}: {r[1]}")

            cur.execute("SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME = 'IAS_ITEM_PRICE'")
            print("\nColumns in IAS_ITEM_PRICE:")
            for r in cur.fetchall():
                print(r[0])
                
            print("\nSample Item Prices:")
            cur.execute("SELECT I_CODE, UNIT_NO, PRICE_LEV_NO, PRICE FROM IAS_ITEM_PRICE WHERE ROWNUM <= 10")
            for r in cur.fetchall():
                print(r)

if __name__ == '__main__':
    explore_pricing()
