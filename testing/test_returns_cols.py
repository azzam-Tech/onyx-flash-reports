import sys
import os

# Add privet directory to path to import database
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "privet", "onyx_reports"))

from database import get_conn

try:
    with get_conn() as con:
        with con.cursor() as cur:
            sql = """
            SELECT *
            FROM IAS20261.IAS_POST_DTL
            WHERE C_CODE = '1735' AND DOC_NO = '2621130228'
            """
            cur.execute(sql)
            columns = [col[0] for col in cur.description]
            print("Columns:", columns)
            for row in cur.fetchall():
                print(dict(zip(columns, row)))
except Exception as e:
    print("Error:", e)
