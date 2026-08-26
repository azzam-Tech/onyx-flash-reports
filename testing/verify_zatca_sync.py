import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def verify_zatca_sync():
    with get_conn() as con:
        with con.cursor() as cur:
            # 1. Get columns of GNR_E_INVC_SQ_MST
            try:
                cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'GNR_E_INVC_SQ_MST'")
                sq_mst_cols = [c[0] for c in cur.fetchall()]
                print("Columns in GNR_E_INVC_SQ_MST:", sq_mst_cols)
                
                # Check what rows exist in GNR_E_INVC_SQ_MST to understand how invoice numbers are stored
                cur.execute("SELECT * FROM GNR_E_INVC_SQ_MST FETCH FIRST 5 ROWS ONLY")
                rows = cur.fetchall()
                print("\nSample rows in GNR_E_INVC_SQ_MST:")
                for r in rows:
                    print(r)
            except Exception as e:
                print(f"Error checking GNR_E_INVC_SQ_MST: {e}")
                
            # 2. Search for 26314600409 in any ZATCA or SYNC related table that we can find
            try:
                cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%ZATCA%' OR table_name LIKE '%SYNC%' OR table_name LIKE '%INV%'")
                tables = cur.fetchall()
                print("\nSearching for 26314600409 in all sync/inv tables...")
                for t in tables:
                    tname = t[0]
                    # Get columns of the table
                    cur.execute(f"SELECT column_name FROM all_tab_columns WHERE table_name = '{tname}'")
                    cols = [c[0] for c in cur.fetchall()]
                    
                    # Search across any column that might hold the invoice number
                    for col in cols:
                        if 'DOC' in col or 'BILL' in col or 'NO' in col or 'ID' in col or 'REF' in col:
                            try:
                                cur.execute(f"SELECT * FROM {tname} WHERE {col} = '26314600409'")
                                res = cur.fetchall()
                                if res:
                                    print(f"Found in {tname}.{col}:")
                                    # Print columns and values matched nicely
                                    for row in res:
                                        print(dict(zip(cols, row)))
                            except:
                                pass
            except Exception as e:
                print(f"Error searching tables: {e}")

if __name__ == '__main__':
    verify_zatca_sync()
