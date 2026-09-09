import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'zatca_printer')))
from app.database import get_conn
import oracledb

conn = get_conn(readonly=True)
cur = conn.cursor()
p_lng_no = 1
msg_id = 3331
res = cur.callfunc("Ias_Gen_Pkg.Get_Msg", oracledb.DB_TYPE_VARCHAR, [p_lng_no, msg_id])
print(f"Message 3331: {res}")
conn.close()
