from database import get_conn
import sys

with get_conn() as con:
    with con.cursor() as cur:
        # Check if C_V_CODE or V_C_CODE works
        query = """
            SELECT NVL(SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0)), 0) 
            FROM IAS20261.IAS_POST_DTL 
            WHERE (AC_CODE_DTL = '1381' OR C_V_CODE = '1381' OR V_C_CODE = '1381') AND NVL(DOC_POST,0) = 1
        """
        cur.execute(query)
        result = cur.fetchone()[0]
        print(f"Net Balance using OR logic: {result}")
        
        # Check what V_CODE or C_CODE gives with C_V_CODE
        query2 = """
            SELECT C_V_CODE, V_C_CODE, AC_CODE_DTL, C_CODE, V_CODE, SUM(NVL(DR_AMT,0) - NVL(CR_AMT,0))
            FROM IAS20261.IAS_POST_DTL 
            WHERE (AC_CODE_DTL = '1381' OR C_V_CODE = '1381' OR V_C_CODE = '1381' OR C_CODE = '1381' OR V_CODE = '1381')
            GROUP BY C_V_CODE, V_C_CODE, AC_CODE_DTL, C_CODE, V_CODE
        """
        cur.execute(query2)
        for row in cur.fetchall():
            print(row)
