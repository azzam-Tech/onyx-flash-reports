from database import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # Check columns of CUSTOMER_GROUP table
        cur.execute("""
            SELECT COLUMN_NAME, DATA_TYPE 
            FROM ALL_TAB_COLUMNS 
            WHERE TABLE_NAME = 'CUSTOMER_GROUP' AND OWNER = 'IAS20261'
        """)
        cols = cur.fetchall()
        print("CUSTOMER_GROUP columns:", cols)

        # Check sample data from CUSTOMER_GROUP
        cur.execute("""
            SELECT * FROM IAS20261.CUSTOMER_GROUP WHERE ROWNUM <= 5
        """)
        
        # Get column names for the result
        col_names = [desc[0] for desc in cur.description]
        print("CUSTOMER_GROUP columns names from description:", col_names)
        
        rows = cur.fetchall()
        print("CUSTOMER_GROUP data:", rows)
