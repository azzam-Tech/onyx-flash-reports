import os
import oracledb
from dotenv import load_dotenv

load_dotenv('db.env')

lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception as e:
    pass

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def analyze_stagnant_items():
    with get_conn() as con:
        with con.cursor() as cur:
            # Check what DOC_TYPEs exist in ITEM_MOVEMENT
            doc_types_sql = """
                SELECT DOC_TYPE, COUNT(*), SUM(I_QTY * IN_OUT) 
                FROM IAS20261.ITEM_MOVEMENT 
                GROUP BY DOC_TYPE
                ORDER BY DOC_TYPE
            """
            cur.execute(doc_types_sql)
            print("--- ITEM_MOVEMENT DOC_TYPES ---")
            for row in cur.fetchall():
                print(row)

            # Check stagnant items based on DOC_TYPE = 0 (Opening Balance)
            stagnant_sql = """
                WITH item_stats AS (
                    SELECT 
                        I_CODE,
                        SUM(CASE WHEN DOC_TYPE = 0 THEN NVL(IN_OUT, 1) * NVL(I_QTY, 0) ELSE 0 END) as opening_qty,
                        SUM(CASE WHEN DOC_TYPE <> 0 THEN 1 ELSE 0 END) as other_movements_count,
                        SUM(NVL(IN_OUT, 1) * NVL(I_QTY, 0)) as current_qty
                    FROM IAS20261.ITEM_MOVEMENT
                    GROUP BY I_CODE
                )
                SELECT 
                    m.I_CODE, 
                    m.I_NAME, 
                    s.opening_qty, 
                    s.current_qty,
                    s.other_movements_count
                FROM item_stats s
                JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = s.I_CODE
                WHERE s.current_qty > 0 AND s.other_movements_count = 0
                ORDER BY s.current_qty DESC
            """
            cur.execute(stagnant_sql)
            rows = cur.fetchall()
            print("\n--- Stagnant Items (Stock > 0, No movements other than DOC_TYPE 0) ---")
            print(f"Total stagnant items: {len(rows)}")
            
            # Print top 20 items and also compute their purchase values
            print(f"{'I_CODE':<15} | {'QTY':<8} | {'I_NAME'}")
            print("-" * 60)
            
            total_stagnant_qty = 0
            stagnant_icodes = []
            for idx, row in enumerate(rows):
                total_stagnant_qty += row[3]
                stagnant_icodes.append(row[0])
                if idx < 20:
                    print(f"{row[0]:<15} | {row[3]:<8} | {row[1]}")
            
            print(f"Total Stagnant Qty: {total_stagnant_qty}")
            
            # Phase 2: Total purchase value for these stagnant items
            # Assuming IAS_ITM_O_BAL or IAS_ITEM_PRICE holds the cost, or we use standard cost from IAS_ITM_MST
            # But user said "من فواتير الشراء" (from purchase invoices). Purchase invoices are IAS_PR_BILL_MST and IAS_PR_BILL_DTL
            # Let's find the total purchase amount for these items.
            
            if not stagnant_icodes:
                return

            print("\nCalculating total value of stagnant items based on PRIMARY_COST (from IAS_ITM_MST) and I_COST (from ITEM_MOVEMENT)...")
            
            purchase_value_sql = """
                WITH item_stats AS (
                    SELECT 
                        I_CODE,
                        SUM(CASE WHEN DOC_TYPE = 0 THEN NVL(IN_OUT, 1) * NVL(I_QTY, 0) ELSE 0 END) as opening_qty,
                        SUM(CASE WHEN DOC_TYPE <> 0 THEN 1 ELSE 0 END) as other_movements_count,
                        SUM(NVL(IN_OUT, 1) * NVL(I_QTY, 0)) as current_qty,
                        MAX(CASE WHEN DOC_TYPE = 0 THEN NVL(I_COST, 0) ELSE 0 END) as opening_i_cost
                    FROM IAS20261.ITEM_MOVEMENT
                    GROUP BY I_CODE
                ),
                stagnant_items AS (
                    SELECT s.I_CODE, s.current_qty, s.opening_i_cost
                    FROM item_stats s
                    WHERE s.current_qty > 0 AND s.other_movements_count = 0
                )
                SELECT 
                    SUM(si.current_qty * NVL(si.opening_i_cost, 0)) as total_inventory_value_icost,
                    SUM(si.current_qty * NVL(m.PRIMARY_COST, 0)) as total_inventory_value_primary
                FROM stagnant_items si
                JOIN IAS20261.IAS_ITM_MST m ON si.I_CODE = m.I_CODE
            """
            cur.execute(purchase_value_sql)
            val_row = cur.fetchone()
            print(f"Total Value of Stagnant Inventory (Current Qty * Opening I_COST from ITEM_MOVEMENT): {val_row[0]:,.2f}")
            print(f"Total Value of Stagnant Inventory (Current Qty * PRIMARY_COST from IAS_ITM_MST): {val_row[1]:,.2f}")

if __name__ == "__main__":
    analyze_stagnant_items()
