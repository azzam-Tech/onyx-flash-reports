import os
import sys
import pandas as pd
import oracledb

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    cursor = conn.cursor()
    
    # Get all tables and varchar columns
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
    for table_name, column_name in columns:
        try:
            sql = f"SELECT COUNT(*) FROM IAS20261.{table_name} WHERE {column_name} = '112010131'"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            if count > 0:
                results.append(f"{table_name}.{column_name}")
        except oracledb.DatabaseError as e:
            pass # Ignore errors like missing privileges or locked tables
            
    for res in results:
        print(f"Found in: {res}")
        
    conn.close()

if __name__ == "__main__":
    main()
