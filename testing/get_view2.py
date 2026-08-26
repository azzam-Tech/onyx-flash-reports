import sys
sys.path.append('privet/onyx_reports')
from database import get_conn
conn = get_conn()
cur = conn.cursor()
cur.execute("SELECT TEXT FROM ALL_VIEWS WHERE VIEW_NAME = 'GNR_TAX_SUM_VW'")
row = cur.fetchone()
if row and row[0]:
    try:
        print(row[0].read())
    except AttributeError:
        print(row[0])
