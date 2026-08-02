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

def find_differing_prices():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    sql = """
    WITH item_sell_prices AS (
        SELECT p.I_CODE, 
               MAX(m.I_NAME) as item_name,
               MAX(p.I_PRICE) as price_list_val
        FROM IAS20261.IAS_ITEM_PRICE p
        JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = p.I_CODE
        WHERE p.I_PRICE > 0
        GROUP BY p.I_CODE
    ),
    item_purchase_prices AS (
        SELECT pi.I_CODE,
               AVG(pi.I_PRICE) as avg_purch_price,
               MAX(pi.I_PRICE) as last_purch_price
        FROM IAS20261.IAS_PI_BILL_DTL pi
        WHERE pi.I_PRICE > 0
        GROUP BY pi.I_CODE
    )
    SELECT sp.I_CODE AS icode,
           sp.item_name AS iname,
           sp.price_list_val AS sell_price,
           pp.last_purch_price AS purch_price,
           ABS(sp.price_list_val - pp.last_purch_price) AS price_diff
    FROM item_sell_prices sp
    JOIN item_purchase_prices pp ON pp.I_CODE = sp.I_CODE
    WHERE sp.price_list_val <> pp.last_purch_price
    ORDER BY ABS(sp.price_list_val - pp.last_purch_price) DESC
    FETCH FIRST 5 ROWS ONLY
    """

    cur.execute(sql)
    rows = cur.fetchall()

    print("=== PRODUCTS WITH DIFFERING PRICES IN IAS_ITEM_PRICE vs IAS_PI_BILL_DTL ===")
    for r in rows:
        icode, iname, sell_p, purch_p, diff = r
        print(f"\n📦 كود الصنف: {icode}")
        print(f"   - اسم الصنف: {iname}")
        print(f"   - السعر في قائمة الأسعار (IAS_ITEM_PRICE): {sell_p:,.2f} ريال")
        print(f"   - السعر في فواتير المشتريات (IAS_PI_BILL_DTL): {purch_p:,.2f} ريال")
        print(f"   - الفارق: {diff:,.2f} ريال")

    conn.close()

if __name__ == "__main__":
    find_differing_prices()
