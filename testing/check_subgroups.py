import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT 
        COUNT(DISTINCT SUB_FOOD_GRP_NO) as cnt_sub,
        COUNT(DISTINCT FOOD_GRP_NO) as cnt_food,
        COUNT(DISTINCT GRP_CLASS_CODE) as cnt_class,
        MAX(SUB_FOOD_GRP_NO) as mx_sub,
        MAX(FOOD_GRP_NO) as mx_food,
        MAX(GRP_CLASS_CODE) as mx_class
    FROM IAS20261.IAS_ITM_MST
    """
    
    df = pd.read_sql(query, conn)
    print(df.iloc[0])
    
    conn.close()

if __name__ == "__main__":
    main()
