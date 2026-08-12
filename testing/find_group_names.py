import os
import sys
import pandas as pd
import oracledb

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    cursor = conn.cursor()
    
    query = """
    SELECT table_name, column_name
    FROM all_tab_columns
    WHERE owner = 'IAS20261' 
      AND data_type LIKE '%VARCHAR%'
      AND table_name NOT LIKE 'BIN$%'
    """
    
    cursor.execute(query)
    columns = cursor.fetchall()
    
    results = []
    # Search for 'شاشات'
    search_term = 'شاشات'
    
    for table_name, column_name in columns:
        try:
            sql = f"SELECT COUNT(*) FROM IAS20261.{table_name} WHERE {column_name} LIKE '%{search_term}%'"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            if count > 0:
                results.append(f"{table_name}.{column_name}")
        except Exception as e:
            pass
            
    print("Found 'شاشات' in:")
    for res in results:
        print(res)
        
    conn.close()

if __name__ == "__main__":
    main()
