import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    # Check if IAS_GRP_ITM_LVL has a tree structure
    query_groups = """
    SELECT GRP_CODE, GRP_CODE_PARENT, GRP_F_NAME 
    FROM IAS20261.IAS_GRP_ITM_LVL
    WHERE ROWNUM <= 10
    """
    
    try:
        df_groups = pd.read_sql(query_groups, conn)
        print("--- Group Tree Structure Samples ---")
        for index, row in df_groups.iterrows():
            parent = row['GRP_CODE_PARENT']
            print(f"Group: {row['GRP_CODE']} - {row['GRP_F_NAME']} | Parent: {parent if pd.notna(parent) else 'None'}")
            
        # Check total groups and those with parents
        query_stats = """
        SELECT 
            COUNT(*) as total_groups,
            SUM(CASE WHEN GRP_CODE_PARENT IS NOT NULL THEN 1 ELSE 0 END) as groups_with_parents
        FROM IAS20261.IAS_GRP_ITM_LVL
        """
        df_stats = pd.read_sql(query_stats, conn)
        print("\n--- Group Stats ---")
        print(f"Total Groups: {df_stats['TOTAL_GROUPS'].iloc[0]}")
        print(f"Groups with Parents: {df_stats['GROUPS_WITH_PARENTS'].iloc[0]}")
        
    except Exception as e:
        print(f"Error querying groups: {e}")
        
    # Check if items are linked to groups
    query_items = """
    SELECT COUNT(*) as total_items,
           SUM(CASE WHEN GRP_CODE IS NOT NULL THEN 1 ELSE 0 END) as items_with_group
    FROM IAS20261.IAS_ITM_MST
    """
    try:
        df_items = pd.read_sql(query_items, conn)
        print("\n--- Item Stats ---")
        print(f"Total Items: {df_items['TOTAL_ITEMS'].iloc[0]}")
        print(f"Items linked to a group: {df_items['ITEMS_WITH_GROUP'].iloc[0]}")
    except Exception as e:
        print(f"Error querying items: {e}")

    conn.close()

if __name__ == "__main__":
    main()
