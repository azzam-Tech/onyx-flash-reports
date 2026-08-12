import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT table_name, column_name
    FROM all_tab_columns
    WHERE owner = 'IAS20261' 
      AND (table_name LIKE '%GRP%' OR table_name LIKE '%GROUP%')
      AND column_name LIKE '%ACC%'
    """
    
    df = pd.read_sql(query, conn)
    for index, row in df.iterrows():
        print(f"{row['TABLE_NAME']}.{row['COLUMN_NAME']}")
        
    conn.close()

if __name__ == "__main__":
    main()
