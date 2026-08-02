import sys, os
from unittest.mock import MagicMock
sys.modules['flask'] = MagicMock()
sys.path.append(os.path.join(os.getcwd(), 'privet', 'onyx_reports'))
from app import get_conn

try:
    conn = get_conn()
    cursor = conn.cursor()
    cursor.execute('''SELECT SUM(p.DR_AMT) FROM IAS20261.IAS_BILL_MST b JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 1 AND TO_CHAR(p.A_CODE) LIKE '111%' WHERE b.BILL_DOC_TYPE = 1 AND b.REP_CODE = 146 AND NVL(p.DOC_POST,0) = 1 AND NVL(p.DR_AMT,0) > 0 AND b.BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND b.BILL_DATE < TO_DATE('2026-07-01','YYYY-MM-DD')''')
    print('CASH_BOX_AMOUNT:', cursor.fetchone()[0])
except Exception as e:
    print('Error:', e)
