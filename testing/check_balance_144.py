import sys
sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT A_CODE, A_NAME, A_NAME_ENG FROM ACCOUNT WHERE A_NAME LIKE '%144%' OR A_NAME LIKE '%محمد سالم%' OR A_CODE LIKE '%144%'")
        accounts = cur.fetchall()
        for acc in accounts:
            print('ACC:', acc)
            
        for acc in accounts:
            acode = acc[0]
            cur.execute("""
                SELECT SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as BALANCE
                FROM IAS_POST_DTL
                WHERE A_CODE = :acode AND NVL(DOC_POST,0) = 1
            """, {'acode': acode})
            bal = cur.fetchone()[0]
            print(f'BALANCE for {acode} ({acc[1]}): {bal}')

        cur.execute("SELECT C_CODE, C_A_NAME FROM CUSTOMER WHERE C_A_NAME LIKE '%144%' OR C_A_NAME LIKE '%محمد سالم%'")
        customers = cur.fetchall()
        for c in customers:
            print('CUSTOMER:', c)
