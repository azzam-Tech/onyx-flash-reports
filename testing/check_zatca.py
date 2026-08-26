import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_zatca_fields():
    with get_conn() as con:
        with con.cursor() as cur:
            # 1. Check IAS_BILL_MST columns
            cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_BILL_MST' AND (column_name LIKE '%ZATCA%' OR column_name LIKE '%HASH%' OR column_name LIKE '%QR%' OR column_name LIKE '%UUID%')")
            cols = cur.fetchall()
            print("--- ZATCA/Hash related columns in IAS_BILL_MST ---")
            for c in cols:
                print(c[0])
            
            # If there's an obvious column, we query it. Let's try to query PIH, HASH, QR if we can guess them.
            # But let's check another table that Onyx uses for ZATCA: maybe E_INV_MST or something similar
            cur.execute("SELECT table_name FROM all_tables WHERE table_name LIKE '%ZATCA%' OR table_name LIKE '%E_INV%' OR table_name LIKE '%EINV%'")
            tables = cur.fetchall()
            print("\n--- ZATCA/E_INV related tables ---")
            for t in tables:
                print(t[0])
                
            # If there are tables like GNR_EXTRNL_DOC_SYNC, let's check its columns
            cur.execute("SELECT column_name FROM all_tab_columns WHERE table_name = 'GNR_EXTRNL_DOC_SYNC' AND (column_name LIKE '%HASH%' OR column_name LIKE '%QR%' OR column_name LIKE '%STS%' OR column_name LIKE '%STATUS%')")
            gnr_cols = cur.fetchall()
            print("\n--- ZATCA/Hash related columns in GNR_EXTRNL_DOC_SYNC ---")
            for c in gnr_cols:
                print(c[0])

if __name__ == '__main__':
    check_zatca_fields()
