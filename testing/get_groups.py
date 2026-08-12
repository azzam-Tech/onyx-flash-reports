import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT G_CODE, G_A_NAME 
    FROM IAS20261.GROUP_DETAILS
    """
    
    df = pd.read_sql(query, conn)
    for index, row in df.iterrows():
        print(f"Group: {row['G_CODE']} - {row['G_A_NAME']}")

    conn.close()

if __name__ == "__main__":
    main()
