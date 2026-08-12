import sys
import os

# Add privet directory to path to import database
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "privet", "onyx_reports"))

from database import get_conn

try:
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
            SELECT p.DOC_TYPE, p.DOC_DATE, p.CR_AMT
            FROM IAS20261.IAS_POST_DTL p
            WHERE p.C_CODE = '1735' AND p.CR_AMT > 0
            ORDER BY p.DOC_DATE DESC
            FETCH FIRST 10 ROWS ONLY
            """
            cur.execute(sql)
            print("DOC_TYPE | DOC_DATE | CR_AMT")
            for row in cur.fetchall():
                print(row)
except Exception as e:
    print("Error:", e)
