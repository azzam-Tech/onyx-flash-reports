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
        
    rep_code = 144
    
    query = f"""
        SELECT 
            SUM(NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as mv_dr
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
        JOIN IAS20261.IAS_BILL_MST m 
          ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND m.BILL_NO = im.DOC_NO 
         AND m.BILL_SER = im.DOC_SER
        WHERE m.REP_CODE = {rep_code}
          AND im.DOC_TYPE = 1 
          AND NVL(im.I_QTY,0) > 0
          AND m.BILL_DATE >= TO_DATE('2026-06-04', 'YYYY-MM-DD') 
          AND m.BILL_DATE < TO_DATE('2026-06-05', 'YYYY-MM-DD')+1
    """
    
    df = pd.read_sql(query, conn)
    print("Cost of Sales for 2026-06-04 to 2026-06-05:", df['MV_DR'][0])
    
    query2 = f"""
        SELECT m.BILL_DATE,
            SUM(NVL(im.I_QTY,0) * NVL(ip.I_PRICE, NVL(it.PRIMARY_COST,0))) as daily_cost
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        LEFT JOIN IAS20261.IAS_ITEM_PRICE ip ON ip.I_CODE = im.I_CODE AND ip.LEV_NO = 1
        JOIN IAS20261.IAS_BILL_MST m 
          ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND m.BILL_NO = im.DOC_NO 
         AND m.BILL_SER = im.DOC_SER
        WHERE m.REP_CODE = {rep_code}
          AND im.DOC_TYPE = 1 
          AND NVL(im.I_QTY,0) > 0
          AND m.BILL_DATE BETWEEN TO_DATE('2026-06-01', 'YYYY-MM-DD') AND TO_DATE('2026-06-10', 'YYYY-MM-DD')
        GROUP BY m.BILL_DATE
        ORDER BY m.BILL_DATE
    """
    df2 = pd.read_sql(query2, conn)
    print("\nDaily Cost in early June:")
    print(df2)
    
    conn.close()

if __name__ == "__main__":
    main()
