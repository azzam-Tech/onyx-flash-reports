import oracledb

try:
    oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
except Exception as e:
    pass

conn = oracledb.connect('RPT_USER/ULT2016@100.100.1.100:1521/ORCL')
cur = conn.cursor()

sql_trans = """
         SELECT p.DOC_DATE, p.DOC_NO, p.REF_NO, NVL(p.DR_AMT,0) dr, NVL(p.CR_AMT,0) cr
         FROM IAS20261.IAS_POST_DTL p
         WHERE (p.AC_CODE_DTL = '1381' OR p.C_V_CODE = '1381' OR p.V_C_CODE = '1381')
           AND NVL(p.DOC_POST,0)=1
           AND NVL(p.DOC_TYPE,0) <> 0
           AND p.DOC_DATE >= TO_DATE('2026-01-01','YYYY-MM-DD')
           AND p.DOC_DATE < TO_DATE('2026-02-01','YYYY-MM-DD')
         ORDER BY p.DOC_DATE, p.DOC_NO
"""
cur.execute(sql_trans)
for r in cur.fetchall():
    print(r)
