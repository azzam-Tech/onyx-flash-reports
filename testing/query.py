import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))
from dotenv import load_dotenv
load_dotenv(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer', '.env')))
from app.database import get_conn
import oracledb

try:
    conn = get_conn(readonly=True)
    cur = conn.cursor()
    print("--- Check Foreign Keys referencing IAS_BILL_MST ---")
    sql = """
    SELECT a.table_name, a.column_name
      FROM all_cons_columns a
      JOIN all_constraints c ON a.owner = c.owner AND a.constraint_name = c.constraint_name
      JOIN all_constraints c_pk ON c.r_owner = c_pk.owner AND c.r_constraint_name = c_pk.constraint_name
     WHERE c.constraint_type = 'R'
       AND c_pk.table_name = 'IAS_BILL_MST'
       AND c.owner = 'IAS20261'
    """
    cur.execute(sql)
    rows = cur.fetchall()
    print(f"Found {len(rows)} foreign key columns referencing IAS_BILL_MST:")
    for r in rows:
        print(f"Table: {r[0]}, Column: {r[1]}")
except Exception as e:
    print(e)
finally:
    if 'conn' in locals():
        conn.close()
