import sys
import os

# Add privet directory to path to import database
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "privet", "onyx_reports"))

from database import get_conn

try:
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
            SELECT p.C_CODE, p.DOC_TYPE, p.DOC_NO, p.DOC_NO_REF, NVL(p.DR_AMT,0), NVL(p.CR_AMT,0)
            FROM IAS20261.IAS_POST_DTL p
            WHERE p.C_CODE = '1735' AND p.DOC_TYPE IN (4, 5)
            ORDER BY p.DOC_DATE DESC
            FETCH FIRST 20 ROWS ONLY
            """
            cur.execute(sql)
            print("C_CODE | DOC_TYPE | DOC_NO | DOC_NO_REF | DR_AMT | CR_AMT")
            for row in cur.fetchall():
                print(row)
except Exception as e:
    print("Error:", e)
