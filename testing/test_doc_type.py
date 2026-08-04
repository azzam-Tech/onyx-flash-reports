import database
conn = database.get_connection()
cursor = conn.cursor()
try:
    cursor.execute("SELECT * FROM IAS_SYS.IAS_DOCJV_TYPE_SYSTEMS FETCH FIRST 5 ROWS ONLY")
    rows = cursor.fetchall()
    cols = [col[0] for col in cursor.description]
    print(cols)
    for row in rows:
        print(row)
except Exception as e:
    print(e)
