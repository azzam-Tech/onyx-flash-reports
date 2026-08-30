import os
import sys
from dotenv import load_dotenv
import oracledb

sys.path.append(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer')
from database import get_conn

with get_conn() as conn:
    with conn.cursor() as cur:
        # Get August movement (all docs)
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)), SUM(NVL(CR_AMT,0))
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144'
              AND EXTRACT(MONTH FROM DOC_DATE) = 8
        """)
        dr_aug, cr_aug = cur.fetchone()
        
        cur.execute("""
            SELECT SUM(NVL(DR_AMT,0)), SUM(NVL(CR_AMT,0))
            FROM IAS_POST_DTL
            WHERE A_CODE = '111010101' AND AC_CODE_DTL = '144'
              AND EXTRACT(MONTH FROM DOC_DATE) = 8
              AND NVL(DOC_POST,0) = 0
        """)
        dr_aug_unp, cr_aug_unp = cur.fetchone()

        print(f"August ALL - DR: {dr_aug}, CR: {cr_aug}, Net: {(dr_aug or 0) - (cr_aug or 0)}")
        print(f"August UNPOSTED - DR: {dr_aug_unp}, CR: {cr_aug_unp}")
