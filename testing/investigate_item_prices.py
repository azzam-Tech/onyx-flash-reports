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

def investigate_item_prices():
    conn = oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)
    cur = conn.cursor()

    # 1. Select a top selling item code
    cur.execute("""
      SELECT dt.I_CODE, MAX(m.I_NAME), SUM(NVL(dt.I_QTY,0)) as total_qty
      FROM IAS20261.IAS_BILL_DTL dt
      JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = dt.I_CODE
      GROUP BY dt.I_CODE
      ORDER BY SUM(NVL(dt.I_QTY,0)) DESC
      FETCH FIRST 1 ROWS ONLY
    """)
    row = cur.fetchone()
    sample_icode = row[0]
    sample_iname = row[1]
    print(f"=== SAMPLE ITEM SELECTED: Code='{sample_icode}' | Name='{sample_iname}' ===")

    # 2. Inspect IAS_ITM_MST price/cost columns
    print("\n--- 1. MASTER ITEM TABLE (IAS_ITM_MST) ---")
    cur.execute("""
      SELECT * FROM IAS20261.IAS_ITM_MST WHERE I_CODE = :icode
    """, {"icode": sample_icode})
    col_names = [d[0] for d in cur.description]
    master_row = cur.fetchone()
    
    price_cost_fields = {}
    for col, val in zip(col_names, master_row):
        if any(keyword in col.upper() for keyword in ['PRICE', 'COST', 'PRC', 'AMT', 'RATE', 'SAL', 'PUR', 'DISC', 'MIN', 'MAX', 'VAL']):
            if val is not None and str(val).strip() != '':
                price_cost_fields[col] = val

    print(f"Master Item fields for {sample_icode}:")
    for k, v in price_cost_fields.items():
        print(f"  - {k}: {v}")

    # 3. Search all tables in IAS20261 schema containing I_CODE column and check price/cost columns
    print("\n--- 2. SEARCHING ALL TABLES IN DATABASE WITH I_CODE ---")
    cur.execute("""
      SELECT table_name 
      FROM all_tab_columns 
      WHERE owner = 'IAS20261' AND column_name = 'I_CODE'
      ORDER BY table_name
    """)
    tables = [r[0] for r in cur.fetchall()]
    print(f"Found {len(tables)} tables containing 'I_CODE':", tables)

    for tbl in tables:
        try:
            # Check price/cost columns in this table
            cur.execute(f"SELECT column_name FROM all_tab_columns WHERE owner = 'IAS20261' AND table_name = '{tbl}'")
            cols = [r[0] for r in cur.fetchall()]
            p_cols = [c for c in cols if any(k in c.upper() for k in ['PRICE', 'COST', 'PRC', 'AMT', 'PRICE1', 'SELL', 'VAL', 'PURCHASE'])]
            
            if p_cols:
                query_cols = ", ".join(p_cols[:10])
                cur.execute(f"SELECT {query_cols} FROM IAS20261.{tbl} WHERE I_CODE = :icode AND ROWNUM <= 3", {"icode": sample_icode})
                res = cur.fetchall()
                if res:
                    print(f"\n📍 Table '{tbl}' has price/cost columns: {p_cols}")
                    for r in res:
                        row_str = ", ".join([f"{col}={val}" for col, val in zip(p_cols[:10], r) if val is not None])
                        print(f"   Row: {row_str}")
        except Exception as e:
            # Table might not be accessible or empty
            pass

    conn.close()

if __name__ == "__main__":
    investigate_item_prices()
