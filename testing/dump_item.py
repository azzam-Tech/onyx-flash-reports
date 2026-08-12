import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT *
    FROM IAS20261.IAS_ITM_MST
    WHERE I_CODE = 'HOMAR-18S-HC'
    """
    
    df = pd.read_sql(query, conn)
    if not df.empty:
        for col in df.columns:
            val = df.iloc[0][col]
            if pd.notna(val) and val != '':
                print(f"{col}: {val}")
    else:
        print("Item not found!")
    
    conn.close()

if __name__ == "__main__":
    main()
