from database import get_conn

with get_conn() as con:
    with con.cursor() as cur:
        # Check what tables have C_GROUP_CODE
        cur.execute("""
            SELECT TABLE_NAME 
            FROM ALL_TAB_COLUMNS 
            WHERE COLUMN_NAME = 'C_GROUP_CODE' AND OWNER = 'IAS20261'
        """)
        tables = cur.fetchall()
        print("Tables with C_GROUP_CODE:", tables)
