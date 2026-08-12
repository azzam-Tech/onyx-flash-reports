import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT column_name
    FROM all_tab_columns
    WHERE table_name = 'IAS_ITM_MST'
      AND owner = 'IAS20261'
    """
    
    df = pd.read_sql(query, conn)
    print("Columns in IAS_ITM_MST:")
    for c in df['COLUMN_NAME']:
        if 'GRP' in c or 'GROUP' in c or 'LVL' in c or 'PRNT' in c or 'TREE' in c:
            print(c)
            
    # Check GROUP_DETAILS table
    print("\nCheck GROUP_DETAILS row count:")
    q2 = "SELECT COUNT(*) FROM IAS20261.GROUP_DETAILS"
    df2 = pd.read_sql(q2, conn)
    print(df2.iloc[0,0])

    conn.close()

if __name__ == "__main__":
    main()
