import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def check_sync():
    with get_conn() as con:
        with con.cursor() as cur:
            try:
                # Check GNR_EXTRNL_DOC_SYNC
                cur.execute("SELECT DOC_TYPE, DOC_NO, SYNC_FLG, SYNC_RSLT, SYNC_DATE FROM GNR_EXTRNL_DOC_SYNC WHERE DOC_NO = '26314600409'")
                res = cur.fetchall()
                if res:
                    print("--- GNR_EXTRNL_DOC_SYNC ---")
                    for r in res:
                        print(f"Doc Type: {r[0]}, Doc No: {r[1]}, Sync Flg: {r[2]}, Sync Rslt: {r[3]}, Date: {r[4]}")
                else:
                    print("Not found in GNR_EXTRNL_DOC_SYNC")
                    
                # Check GNR_E_INVC_SQ_MST
                cur.execute("SELECT DOC_TYP, DOC_NO, E_INV_SYNC_STS, HASH_VAL FROM GNR_E_INVC_SQ_MST WHERE DOC_NO = '26314600409'")
                res = cur.fetchall()
                if res:
                    print("--- GNR_E_INVC_SQ_MST ---")
                    for r in res:
                        print(f"Doc Type: {r[0]}, Doc No: {r[1]}, Sync Status: {r[2]}, Hash: {r[3]}")
                else:
                    print("Not found in GNR_E_INVC_SQ_MST")
                    
                # Check IAS_SMAN_DOC_SYNC_DTS
                cur.execute("SELECT DOC_TYPE, REP_CODE, SYNC_METHOD FROM IAS_SMAN_DOC_SYNC_DTS WHERE DOC_TYPE = '1'") # Can't filter by doc_no directly without knowing columns
                
            except Exception as e:
                print(e)

if __name__ == '__main__':
    check_sync()
