from database import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # Check columns of CUSTOMER table
        cur.execute("""
            SELECT COLUMN_NAME, DATA_TYPE 
            FROM ALL_TAB_COLUMNS 
            WHERE TABLE_NAME = 'CUSTOMER' AND OWNER = 'IAS20261'
            AND (COLUMN_NAME LIKE '%GRP%' OR COLUMN_NAME LIKE '%GROUP%' OR COLUMN_NAME LIKE '%G_CODE%')
        """)
        cols = cur.fetchall()
        print("CUSTOMER table group columns:", cols)

        # Look for tables related to Customer Groups
        cur.execute("""
            SELECT TABLE_NAME 
            FROM ALL_TABLES 
            WHERE OWNER = 'IAS20261' 
            AND (TABLE_NAME LIKE '%CUST%GRP%' OR TABLE_NAME LIKE '%CG_%' OR TABLE_NAME LIKE '%C_GRP%')
        """)
        tables = cur.fetchall()
        print("Possible Group Tables:", tables)
