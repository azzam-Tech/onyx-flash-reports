import os
import sys
import pandas as pd
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT G_CODE, G_A_NAME 
    FROM IAS20261.GROUP_DETAILS
    """
    
    df = pd.read_sql(query, conn)
    records = df.to_dict('records')
    
    with open('testing/group_details_dump.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=4)

    conn.close()

if __name__ == "__main__":
    main()
