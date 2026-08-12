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
    WHERE table_name IN ('IAS_SUB_GRP_DTL', 'IAS_MAINSUB_GRP_DTL', 'IAS_DETAIL_GROUP')
    AND owner = 'IAS20261'
    """
    
    df = pd.read_sql(query, conn)
    for index, row in df.iterrows():
        if 'NAME' in row['COLUMN_NAME'] or 'CODE' in row['COLUMN_NAME']:
            print(f"{row['TABLE_NAME']}.{row['COLUMN_NAME']}")

    conn.close()

if __name__ == "__main__":
    main()
