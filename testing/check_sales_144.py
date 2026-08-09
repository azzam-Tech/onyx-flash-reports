import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    if not conn:
        print("Failed to connect to DB")
        return
        
    date = '2026-06-06'
    
    query = f"""
    SELECT 
        SUM(NVL(ip1.I_PRICE,0) * NVL(d.I_QTY,0)) as level1,
        SUM(NVL(ip2.I_PRICE,0) * NVL(d.I_QTY,0)) as level2,
        SUM(NVL(ip3.I_PRICE,0) * NVL(d.I_QTY,0)) as level3,
        SUM(NVL(ip4.I_PRICE,0) * NVL(d.I_QTY,0)) as level4
    FROM IAS20261.IAS_BILL_MST m
    JOIN IAS20261.IAS_BILL_DTL d ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip1 ON d.I_CODE = ip1.I_CODE AND ip1.LEV_NO = 1
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip2 ON d.I_CODE = ip2.I_CODE AND ip2.LEV_NO = 2
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip3 ON d.I_CODE = ip3.I_CODE AND ip3.LEV_NO = 3
    LEFT JOIN IAS20261.IAS_ITEM_PRICE ip4 ON d.I_CODE = ip4.I_CODE AND ip4.LEV_NO = 4
    WHERE m.CC_CODE = 144
      AND m.BILL_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
    """
    
    df = pd.read_sql(query, conn)
    print("=== Sales vs Cost for CC_CODE 144 on 2026-06-06 ===")
    for col in df.columns:
        print(f"{col}: {df[col].iloc[0]:.2f}")

    conn.close()

if __name__ == "__main__":
    main()
