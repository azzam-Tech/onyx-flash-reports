import sys
sys.path.append(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer")

from dotenv import load_dotenv
load_dotenv(r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\.env")

from app.database import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        cur.execute("SELECT VST_NO, C_CODE, REP_CODE, VST_STS, VST_CNCL_RSN, VST_DATE FROM IAS20261.DTS_CST_VST_MST WHERE C_CODE='1545' ORDER BY VST_NO DESC FETCH FIRST 5 ROWS ONLY")
        rows = cur.fetchall()
        print("Recent Visits for Customer 1545:")
        for r in rows:
            print(r)
