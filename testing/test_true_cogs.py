import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        query = """
        SELECT SUM(NVL(im.I_QTY,0) * NVL(it.PRIMARY_COST,0))
        FROM IAS20261.ITEM_MOVEMENT im
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = im.I_CODE
        JOIN IAS20261.IAS_BILL_MST m 
          ON m.BILL_DOC_TYPE = im.BILL_DOC_TYPE 
         AND m.BILL_NO = im.DOC_NO 
         AND m.BILL_SER = im.DOC_SER
        WHERE im.DOC_TYPE = 1 
          AND NVL(im.I_QTY,0) > 0
          AND m.BILL_DATE >= TO_DATE('2026-01-01', 'YYYY-MM-DD')
          AND m.BILL_DATE <= TO_DATE('2026-06-30', 'YYYY-MM-DD')
        """
        cur.execute(query)
        print(f"Total True COGS using PRIMARY_COST: {cur.fetchone()[0]}")
