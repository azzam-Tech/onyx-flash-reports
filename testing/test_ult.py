import oracledb

def check_constraint():
    try:
        connection = oracledb.connect(user="RPT_USER", password="ULT2016", dsn="100.100.1.100:1521/ORCL")
        cursor = connection.cursor()
        
        print("Checking VST_RSLT_TYP distribution...")
        cursor.execute("SELECT VST_RSLT_TYP, COUNT(*) FROM IAS20261.DTS_CST_VST_MST GROUP BY VST_RSLT_TYP")
        for row in cursor.fetchall():
            print(f"VST_RSLT_TYP: {row[0]}, Count: {row[1]}")
            
        print("\nChecking VST_CNCL_RSN (Cancel Reasons) distribution...")
        cursor.execute("SELECT COUNT(*) FROM IAS20261.DTS_CST_VST_MST WHERE VST_CNCL_RSN IS NOT NULL")
        cnt = cursor.fetchone()[0]
        print(f"Records with VST_CNCL_RSN: {cnt}")
        
        if cnt > 0:
            cursor.execute("SELECT VST_NO, VST_CNCL_RSN FROM IAS20261.DTS_CST_VST_MST WHERE VST_CNCL_RSN IS NOT NULL FETCH FIRST 5 ROWS ONLY")
            for row in cursor.fetchall():
                print(row)
                
        print("\nChecking if there is any other table for visit details...")
        cursor.execute("SELECT table_name FROM all_tables WHERE table_name LIKE 'DTS_CST_VST%' AND owner = 'IAS20261'")
        for row in cursor.fetchall():
            print(row[0])
            
        connection.close()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
    check_constraint()
