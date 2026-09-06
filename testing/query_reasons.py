import oracledb
oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect('ULT/ULT2017@100.100.1.100:1521/ORCL')
cur = con.cursor()

print("--- DTS_VST_FAIL_REASON ---")
cur.execute("SELECT RESON_TYP, RESON_L_DSC FROM IAS20261.DTS_VST_FAIL_REASON")
for row in cur.fetchall(): print(row)

print("\n--- DTS_VST_RSLT_TYPS ---")
cur.execute("SELECT VST_RSLT_TYP, VST_RSLT_L_DSC FROM IAS20261.DTS_VST_RSLT_TYPS")
for row in cur.fetchall(): print(row)

con.close()
