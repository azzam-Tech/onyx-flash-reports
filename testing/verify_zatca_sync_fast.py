import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def verify():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                # 1. Get columns of GNR_E_INVC_SQ_MST
                cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'GNR_E_INVC_SQ_MST'")
                sq_mst_cols = [c[0] for c in cur.fetchall()]
                print("Columns in GNR_E_INVC_SQ_MST:", sq_mst_cols)
                
                # Check what rows exist in GNR_E_INVC_SQ_MST for 26314600409 using the right column
                for col in sq_mst_cols:
                    if 'DOC' in col or 'NO' in col or 'REF' in col or 'ID' in col:
                        try:
                            cur.execute(f"SELECT * FROM GNR_E_INVC_SQ_MST WHERE {col} = '26314600409'")
                            res = cur.fetchall()
                            if res:
                                print(f"\nFound in GNR_E_INVC_SQ_MST via {col}:")
                                for row in res:
                                    print(dict(zip(sq_mst_cols, row)))
                        except:
                            pass
                            
                # Also check IAS_BILL_MST ZATCA_STS if it exists
                cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_BILL_MST'")
                mst_cols = [c[0] for c in cur.fetchall()]
                for col in mst_cols:
                    if 'ZATCA' in col:
                        cur.execute(f"SELECT {col} FROM IAS_BILL_MST WHERE BILL_NO = '26314600409'")
                        print(f"IAS_BILL_MST.{col}:", cur.fetchone()[0])
            except Exception as e:
                print(f"Error: {e}")

if __name__ == '__main__':
    verify()
