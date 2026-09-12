from database import get_conn
import sys

with get_conn() as con:
    with con.cursor() as cur:
        query = """
            SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)), 0) 
            FROM IAS20261.IAS_POST_DTL 
            WHERE AC_CODE_DTL = '1381' AND NVL(DOC_POST,0) = 1
        """
        cur.execute(query)
        result = cur.fetchone()[0]
        print(f"Net Balance using AC_CODE_DTL: {result}")
        
        query2 = """
            SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)), 0) 
            FROM IAS20261.IAS_POST_DTL 
            WHERE C_CODE = '1381' AND NVL(DOC_POST,0) = 1
        """
        cur.execute(query2)
        result2 = cur.fetchone()[0]
        print(f"Net Balance using C_CODE: {result2}")
