import oracledb
import os

os.environ["PATH"] = r"C:\oracle\instantclient\instantclient_23_0;" + os.environ.get("PATH", "")
oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")

def check_conn(u, p):
    try:
        conn = oracledb.connect(user=u, password=p, dsn='100.100.1.100:1521/ORCL')
        print(f"SUCCESS: user={u}, pass={p}")
        conn.close()
        return True
    except Exception as e:
        # print(f"FAIL: user={u}, pass={p} - {e}")
        return False

combos = [
    ('ULT', 'ULT2016'),
    ('ult', 'ULT2016'),
    ('ULT', 'ult2016'),
    ('ult', 'ult2016'),
    ('IAS20261', 'ULT2016'),
    ('IAS20261', 'ult2016'),
    ('ULT', '123456'),
    ('SYS', 'SYS'),
    ('SYSTEM', 'ULT2016')
]

for u, p in combos:
    if check_conn(u, p):
        break
