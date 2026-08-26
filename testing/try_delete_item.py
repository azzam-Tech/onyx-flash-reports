import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def try_delete():
    icode = 'DORWM-13.5'
    print(f"Attempting to delete item {icode} from IAS_ITM_MST using ULT...")
    
    # Using ULT credentials explicitly for this test only
    from database import DB_DSN, InterceptConnection
    import oracledb
    
    test_conn = InterceptConnection(oracledb.connect(user='ULT', password='ULT2017', dsn=DB_DSN))
    
    with test_conn as con:
        with con.cursor() as cur:
            try:
                # Attempt to delete the item directly
                cur.execute("DELETE FROM IAS_ITM_MST WHERE I_CODE = :1", [icode])
                print(f"Rows deleted: {cur.rowcount}")
                print("SUCCESS: Item was deleted successfully from IAS_ITM_MST.")
                
                # Rollback to avoid permanent changes during test
                con.rollback()
                print("ROLLBACK executed. The database was NOT permanently changed.")
            except Exception as e:
                print("\nFAILED: Oracle blocked the deletion.")
                print(f"Error Message:\n{str(e)}")

if __name__ == '__main__':
    try_delete()
