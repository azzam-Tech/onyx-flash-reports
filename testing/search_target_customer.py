import os
import oracledb
from dotenv import load_dotenv

load_dotenv('db.env')
lib_dir = os.getenv("ORA_LIB_DIR", r"C:\oracle\instantclient\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=lib_dir)
except Exception:
    pass

def get_conn():
    return oracledb.connect(
        user=os.getenv("DB_USER", "RPT_USER"),
        password=os.getenv("DB_PASS", "ULT2016"),
        dsn=os.getenv("ORA_DSN", "100.100.1.100:1521/ORCL")
    )

def main():
    with get_conn() as con:
        with con.cursor() as cur:
            # Find all tables with 'CUST' in their name
            cur.execute("""
                SELECT TABLE_NAME 
                FROM ALL_TABLES 
                WHERE OWNER = 'IAS20261' AND TABLE_NAME LIKE '%CUST%'
            """)
            tables = [t[0] for t in cur.fetchall()]
            
            print(f"Searching for '7897911' or 'عزام بشار' in {len(tables)} tables...")
            
            for t in tables:
                try:
                    # Get varchar/char columns
                    cur.execute(f"""
                        SELECT COLUMN_NAME 
                        FROM ALL_TAB_COLUMNS 
                        WHERE OWNER = 'IAS20261' AND TABLE_NAME = '{t}' 
                          AND DATA_TYPE LIKE '%CHAR%'
                    """)
                    cols = [c[0] for c in cur.fetchall()]
                    
                    if not cols:
                        continue
                        
                    # Build search query
                    where_clauses = [f"{c} LIKE '%7897911%' OR {c} LIKE '%عزام بشار%'" for c in cols]
                    query = f"SELECT * FROM IAS20261.{t} WHERE " + " OR ".join(where_clauses)
                    
                    cur.execute(query)
                    rows = cur.fetchall()
                    if rows:
                        print(f"\n>>> FOUND IN TABLE: {t}")
                        col_names = [col[0] for col in cur.description]
                        for r in rows:
                            row_dict = dict(zip(col_names, r))
                            print("Match:")
                            for k, v in row_dict.items():
                                if v is not None:
                                    print(f"  {k}: {v}")
                except Exception as e:
                    pass

if __name__ == "__main__":
    main()
