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

def main():
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
                WITH item_stats AS (
                    SELECT 
                        I_CODE,
                        SUM(CASE WHEN DOC_TYPE <> 0 THEN I_QTY ELSE 0 END) as total_movement_qty,
                        SUM(NVL(IN_OUT, 1) * NVL(I_QTY, 0)) as current_qty,
                        MAX(STK_COST) as max_stk_cost,
                        MAX(I_COST) as max_i_cost
                    FROM IAS20261.ITEM_MOVEMENT
                    GROUP BY I_CODE
                )
                SELECT 
                    s.I_CODE, 
                    m.I_NAME, 
                    s.total_movement_qty, 
                    s.current_qty,
                    s.max_stk_cost,
                    s.max_i_cost,
                    NVL(m.PRIMARY_COST, 0) as primary_cost
                FROM item_stats s
                JOIN IAS20261.IAS_ITM_MST m ON m.I_CODE = s.I_CODE
                WHERE s.current_qty > 0
                ORDER BY s.total_movement_qty ASC, s.current_qty DESC
            """
            cur.execute(sql)
            rows = cur.fetchall()
            
            cumulative_cost = 0.0
            selected_items = []
            
            for row in rows:
                icode = row[0]
                iname = row[1]
                movement_qty = row[2]
                current_qty = row[3]
                
                # Determine best unit cost
                cost1 = row[4] if row[4] else 0  # max_stk_cost
                cost2 = row[5] if row[5] else 0  # max_i_cost
                cost3 = row[6] if row[6] else 0  # primary_cost
                
                unit_cost = cost1 if cost1 > 0 else (cost2 if cost2 > 0 else cost3)
                
                # If no reliable cost is found, fallback to 0
                item_total_cost = current_qty * unit_cost
                
                if item_total_cost > 0:
                    selected_items.append({
                        "icode": icode,
                        "iname": iname.strip(),
                        "movement_qty": movement_qty,
                        "current_qty": current_qty,
                        "unit_cost": unit_cost,
                        "total_cost": item_total_cost
                    })
                    cumulative_cost += item_total_cost
                    
                    if cumulative_cost >= 5000000:
                        break
            
            # Generate markdown report
            import json
            artifact_dir = os.path.dirname(__file__)
            report_path = os.path.join(artifact_dir, "least_movement_5m.md")
            
            report = "# الأصناف الأقل حركة حتى إجمالي تكلفة 5 مليون ريال\n\n"
            report += f"- **إجمالي التكلفة التراكمية:** `{cumulative_cost:,.2f}` ريال\n"
            report += f"- **عدد الأصناف:** `{len(selected_items)}` صنفاً\n\n"
            report += "| كود الصنف | اسم الصنف | كمية الحركة (2026) | الرصيد الحالي | تكلفة الوحدة | إجمالي التكلفة التراكمي للسطر |\n"
            report += "|---|---|---|---|---|---|\n"
            
            running_total = 0
            for item in selected_items:
                running_total += item['total_cost']
                report += f"| `{item['icode']}` | {item['iname']} | {item['movement_qty']} | {item['current_qty']} | {item['unit_cost']:,.2f} | **{running_total:,.2f}** |\n"
            
            with open(report_path, "w", encoding="utf-8") as f:
                f.write(report)
            
            print(f"SUCCESS: Accumulated cost: {cumulative_cost:,.2f}. Items count: {len(selected_items)}. Report saved to {report_path}")

if __name__ == "__main__":
    main()
