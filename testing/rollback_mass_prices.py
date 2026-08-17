import oracledb
import os

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

old_prices = {
    'SR121': 255,
    'SR121.': 262,
    'SRTM218DFW': 499,
    'SRTM274DFS': 600,
    'SRTM274DFW': 595,
    'SRRF-286NFS': 749,
    'SRTM386NFW': 750,
    'SRRF-300NF': 825,
    'SRRF-420NFS': 970,
    'SRTM-465NFS': 1000,
    'SRTM604NF': 990,
    'SRRF-465NFS': 1000,
    'SRRF-515NF': 1155,
    'SRRF-525NF': 1250,
    'SRRF-538NFS': 1230,
    'SRTM-545NFS': 1238,
    'SRTM754NFS': 1270,
    'SRTM-605NFS': 1410,
    'SRRF-612NFS': 1410,
    'SRTM-650NFS': 1410
}

def rollback_wholesale_prices():
    try:
        conn = oracledb.connect(user='ULT', password='ULT2017', dsn='100.100.1.100:1521/ORCL')
        cur = conn.cursor()
        
        updated_count = 0
        
        for code, old_price in old_prices.items():
            
            # Get current price
            cur.execute("SELECT I_PRICE FROM IAS_ITEM_PRICE WHERE I_CODE = :1 AND LEV_NO = 1", (code,))
            res = cur.fetchone()
            
            if not res:
                print(f"Not found: {code}")
                continue
                
            current_price = res[0]
            
            if current_price == old_price:
                continue
                
            # Insert History again to log the rollback
            cur.execute("""
                INSERT INTO IAS_ITEM_PRICE_HISTORY 
                (I_CODE, LEV_NO, PREV_I_PRICE, I_PRICE, AUD_DATE, AUD_U_ID)
                VALUES (:1, 1, :2, :3, SYSDATE, 999)
            """, (code, current_price, old_price))
            
            # Update Price back to original
            cur.execute("""
                UPDATE IAS_ITEM_PRICE
                SET I_PRICE = :1, UP_DATE = SYSDATE, UP_U_ID = 999
                WHERE I_CODE = :2 AND LEV_NO = 1
            """, (old_price, code))
            
            updated_count += 1
            print(f"Rolled back {code} from {current_price} to {old_price}")
            
        conn.commit()
        cur.close()
        conn.close()
        
        print(f"\nSuccessfully rolled back {updated_count} items to their original prices.")
            
    except Exception as e:
        print(f"Failed: {e}")

if __name__ == '__main__':
    rollback_wholesale_prices()
