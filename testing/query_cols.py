import oracledb
oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect('ULT/ULT2017@100.100.1.100:1521/ORCL')
cur = con.cursor()
tables = ['DTS_CST_VST_MST', 'DTS_CST_VST_DTL', 'DTS_VST_FAIL_REASON', 'DTS_VST_RSLT_TYPS']
for t in tables:
    print(f"\n--- {t} ---")
    cur.execute(f"SELECT COLUMN_NAME, DATA_TYPE FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='{t}' ORDER BY COLUMN_ID")
    for row in cur.fetchall():
        print(f"{row[0]} ({row[1]})")
con.close()
