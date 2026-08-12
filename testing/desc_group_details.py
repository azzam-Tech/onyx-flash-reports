import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT column_name, data_type
    FROM all_tab_columns
    WHERE table_name = 'GROUP_DETAILS'
    """
    
    df = pd.read_sql(query, conn)
    for index, row in df.iterrows():
        print(f"{row['COLUMN_NAME']}: {row['DATA_TYPE']}")
        
    conn.close()

if __name__ == "__main__":
    main()
