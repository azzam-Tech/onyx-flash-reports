import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def check_table(conn, table_name, name_col, code_col):
    try:
        query = f"SELECT {code_col}, {name_col} FROM IAS20261.{table_name} WHERE ROWNUM <= 10"
        df = pd.read_sql(query, conn)
        print(f"\n--- {table_name} ---")
        for index, row in df.iterrows():
            print(f"{row[code_col]} - {row[name_col]}")
        
        # Get count
        cnt = pd.read_sql(f"SELECT COUNT(*) as c FROM IAS20261.{table_name}", conn)
        print(f"Total Rows: {cnt['C'].iloc[0]}")
    except Exception as e:
        print(f"Error checking {table_name}: {e}")

def main():
    conn = get_conn()
    
    check_table(conn, 'IAS_SUB_GRP_DTL', 'SUB_G_A_NAME', 'SUBG_CODE')
    check_table(conn, 'IAS_MAINSUB_GRP_DTL', 'MNG_A_NAME', 'MNG_CODE')
    check_table(conn, 'IAS_DETAIL_GROUP', 'DTL_A_NAME', 'DTL_G_CODE')

    conn.close()

if __name__ == "__main__":
    main()
