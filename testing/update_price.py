import oracledb
import os

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

def update_price():
    try:
        conn = oracledb.connect(user='ULT', password='ULT2017', dsn='100.100.1.100:1521/ORCL')
        cur = conn.cursor()
        
        # Insert a history record first (Best practice)
        cur.execute("""
            INSERT INTO IAS20261.IAS_ITEM_PRICE_HISTORY 
            (I_CODE, LEV_NO, PREV_I_PRICE, I_PRICE, AUD_DATE, AUD_U_ID)
            VALUES ('SR121.', 2, 400, 325, SYSDATE, 999)
        """)
        
        # Update the actual price
        cur.execute("""
            UPDATE IAS20261.IAS_ITEM_PRICE
            SET I_PRICE = 325, UP_DATE = SYSDATE, UP_U_ID = 999
            WHERE I_CODE = 'SR121.' AND LEV_NO = 2
        """)
        
        conn.commit()
        print(f"Success! Price updated to 325 for SR121.")
        
        # Query again to confirm
        cur.execute("SELECT I_PRICE FROM IAS20261.IAS_ITEM_PRICE WHERE I_CODE = 'SR121.' AND LEV_NO = 2")
        print("Confirmed new price:", cur.fetchone()[0])
        
        cur.close()
        conn.close()
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == '__main__':
    update_price()
