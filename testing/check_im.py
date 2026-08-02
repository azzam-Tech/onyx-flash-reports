import os
import sys
sys.path.append(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports")
from app import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # Let's check distinct DOC_TYPE and IN_OUT for ITEM_MOVEMENT where it links to sales returns
        cur.execute("""
            SELECT DISTINCT im.DOC_TYPE, im.BILL_DOC_TYPE, im.IN_OUT
            FROM IAS20261.ITEM_MOVEMENT im
            JOIN IAS20261.IAS_RT_BILL_MST r
              ON r.RT_BILL_NO = im.DOC_NO 
             AND r.RT_BILL_SER = im.DOC_SER
            WHERE ROWNUM <= 100
        """)
        for row in cur.fetchall():
            print(f"Returns -> DOC_TYPE: {row[0]}, BILL_DOC_TYPE: {row[1]}, IN_OUT: {row[2]}")
            
        cur.execute("""
            SELECT DISTINCT im.DOC_TYPE, im.BILL_DOC_TYPE, im.IN_OUT
            FROM IAS20261.ITEM_MOVEMENT im
            JOIN IAS20261.IAS_BILL_MST b
              ON b.BILL_NO = im.DOC_NO 
             AND b.BILL_SER = im.DOC_SER
            WHERE ROWNUM <= 100
        """)
        for row in cur.fetchall():
            print(f"Sales -> DOC_TYPE: {row[0]}, BILL_DOC_TYPE: {row[1]}, IN_OUT: {row[2]}")
