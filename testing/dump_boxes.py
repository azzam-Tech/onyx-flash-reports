import sys
import json
sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

results = {}
with get_conn() as conn:
    with conn.cursor() as cur:
        # Check BOXES table
        try:
            cur.execute("SELECT BOX_NO, BOX_NAME, BOX_A_NAME FROM BOXES WHERE BOX_NO LIKE '%144%' OR BOX_A_NAME LIKE '%144%'")
            boxes = cur.fetchall()
            for b in boxes:
                print('BOX:', b)
        except Exception as e:
            print("No BOXES table or diff columns:", e)

        try:
            cur.execute("SELECT B_CODE, B_NAME FROM BOXES")
            boxes = cur.fetchall()
            for b in boxes:
                if '144' in str(b) or 'محمد' in str(b):
                    print('BOX (B_CODE):', b)
        except Exception as e:
            print("Error query BOXES B_CODE:", e)

        try:
            # Maybe there is an account starting with 111 (cash) and the name has محمد سالم?
            cur.execute("SELECT A_CODE, A_NAME FROM ACCOUNT WHERE A_CODE LIKE '111%' AND (A_NAME LIKE '%144%' OR A_NAME LIKE '%سالم%')")
            accs = cur.fetchall()
            for a in accs:
                print('CASH_ACC:', a)
        except Exception as e:
            print("Error cash acc:", e)

