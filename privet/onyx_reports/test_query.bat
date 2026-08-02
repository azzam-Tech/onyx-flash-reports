@echo off
set ORA_LIB_DIR=C:\oracle64\instantclient_19_23
set TNS_ADMIN=C:\oracle64\instantclient_19_23
set PATH=%ORA_LIB_DIR%;%PATH%
py -c "import sys, os; from unittest.mock import MagicMock; sys.modules['flask'] = MagicMock(); sys.path.append(os.path.join(os.getcwd(), 'privet', 'onyx_reports')); from app import get_conn; conn = get_conn(); cursor = conn.cursor(); cursor.execute('''SELECT p.DOC_TYPE, p.JV_TYPE, COUNT(*) AS CNT, SUM(p.DR_AMT) AS TOT_DR FROM IAS20261.IAS_BILL_MST b JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER WHERE b.BILL_DOC_TYPE = 1 AND b.REP_CODE = 146 AND NVL(p.DOC_POST,0) = 1 AND NVL(p.DR_AMT,0) > 0 AND b.BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND b.BILL_DATE < TO_DATE('2026-07-01','YYYY-MM-DD') GROUP BY p.DOC_TYPE, p.JV_TYPE'''); print(cursor.fetchall())"
