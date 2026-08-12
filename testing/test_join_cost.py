import os
import sys
import pandas as pd

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    
    query = """
    SELECT 
        SUM(NVL(im.I_QTY,0) * NVL(d.I_PRICE_LEV_NO, 0)) as cost_from_dtl,
        SUM(NVL(im.I_QTY,0) * NVL(im.I_COST, 0)) as cost_from_im
    FROM IAS20261.ITEM_MOVEMENT im
    JOIN IAS20261.IAS_BILL_MST m 
        ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
        AND m.BILL_NO = im.DOC_NO 
        AND m.BILL_SER = im.DOC_SER
    LEFT JOIN IAS20261.IAS_BILL_DTL d
        ON d.BILL_DOC_TYPE = im.BILL_DOC_TYPE
        AND d.BILL_NO = im.DOC_NO
        AND d.BILL_SER = im.DOC_SER
        AND d.I_CODE = im.I_CODE
    WHERE m.CC_CODE = 144
        AND im.DOC_TYPE = 1 
        AND m.BILL_DATE = TO_DATE('2026-06-06', 'YYYY-MM-DD')
        AND NVL(im.I_QTY,0) > 0
    """
    
    df = pd.read_sql(query, conn)
    for col in df.columns:
        print(f"{col}: {df[col].iloc[0]}")
        
    conn.close()

if __name__ == "__main__":
    main()
