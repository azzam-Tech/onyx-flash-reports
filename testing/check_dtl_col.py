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
    print("Columns in IAS_ITM_MST matching DET or DTL:")
    for c in df['COLUMN_NAME']:
        if 'DET' in c or 'DTL' in c:
            print(c)
            
    conn.close()

if __name__ == "__main__":
    main()
