import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
with oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL') as con:
    cur = con.cursor()
    
    d1 = '2026-01-01'
    d2 = '2026-06-30'
    cond = f"DOC_DATE >= TO_DATE('{d1}', 'YYYY-MM-DD') AND DOC_DATE < TO_DATE('{d2}', 'YYYY-MM-DD')+1"
    
    cur.execute(f"SELECT SUM(CR_AMT) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND {cond}")
    rcpt = cur.fetchone()[0] or 0
    print('1. rcpt:', rcpt)
    
    cur.execute(f"SELECT SUM(CR_AMT) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND C_CODE IS NOT NULL AND {cond}")
    unposted_rcpt = cur.fetchone()[0] or 0
    print('2. unposted_rcpt:', unposted_rcpt)
    
    cur.execute(f"SELECT SUM(CR_AMT) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=0 AND DOC_TYPE=2 AND C_CODE IS NULL AND {cond}")
    unposted_unknown = cur.fetchone()[0] or 0
    print('3. unposted_unknown:', unposted_unknown)
    
    cur.execute(f"SELECT SUM(CR_AMT) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=1 AND JV_TYPE=2 AND C_CODE IS NOT NULL AND {cond}")
    net_jrn = cur.fetchone()[0] or 0
    print('4. net_jrn:', net_jrn)
    
    cur.execute(f"SELECT SUM(NVL(p.DR_AMT,0)) FROM IAS20261.IAS_BILL_MST b JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%' WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0 AND b.BILL_DATE >= TO_DATE('{d1}', 'YYYY-MM-DD') AND b.BILL_DATE < TO_DATE('{d2}', 'YYYY-MM-DD')+1")
    cash_sales = cur.fetchone()[0] or 0
    print('5. cash_sales:', cash_sales)
    
    cur.execute(f"SELECT SUM(CR_AMT) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=5 AND TO_CHAR(A_CODE) LIKE '111%' AND {cond}")
    cash_ret = cur.fetchone()[0] or 0
    print('6. cash_ret:', cash_ret)
    
    cur.execute(f"SELECT SUM(CR_AMT) FROM IAS20261.IAS_POST_DTL WHERE NVL(DOC_POST,0)=1 AND DOC_TYPE=2 AND C_CODE IS NULL AND {cond}")
    rcpt_unknown = cur.fetchone()[0] or 0
    print('7. rcpt_unknown:', rcpt_unknown)
    
    print('TOTAL:', rcpt + unposted_rcpt + unposted_unknown + net_jrn + cash_sales - cash_ret + rcpt_unknown)
