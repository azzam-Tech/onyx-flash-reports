import os
os.environ['NLS_LANG'] = 'AMERICAN_AMERICA.AR8MSWIN1256'
import oracledb

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
con = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')

cur = con.cursor()
query = """
    SELECT 
        m.BILL_NO, 
        TO_CHAR(m.BILL_DATE, 'DD/MM/YYYY'), 
        TO_CHAR(m.AD_DATE, 'HH:MI:SS AM'),
        m.BILL_AMT,
        NVL(m.VAT_AMT, 0) as VAT_AMT,
        NVL(m.C_NAME, NVL(c.C_A_NAME, cash_c.CUST_L_NM)) as C_NAME,
        m.BILL_DATE,
        m.BILL_DOC_TYPE,
        NVL(c.BUILDING_NO, cash_c.BUILDING_NO),
        NVL(c.STREET, cash_c.STREET),
        NVL(c.DSTRCT_NM, cash_c.DSTRCT_NM),
        NVL(c.C_BOX_CODE, cash_c.PBOX),
        NVL(c.ADD_NO, cash_c.ADD_NO),
        NVL(c.C_TAX_CODE, cash_c.C_TAX_CODE),
        NVL(c.CR_NO, cash_c.CR_NO),
        NVL(c.CSTMR_IDNTFR, cash_c.CSTMR_IDNTFR),
        m.TAX_BILL_TYP,
        TO_CHAR(m.AD_DATE, 'HH24:MI:SS'),
        ci.CITY_A_NAME,
        co.CNTRY_A_NAME
    FROM IAS20261.IAS_BILL_MST m
    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = m.C_CODE
    LEFT JOIN IAS20261.IAS_CASH_CUSTMR cash_c ON m.C_CODE_CSH = cash_c.CUST_CODE
    LEFT JOIN IAS20261.CITIES ci ON NVL(c.CITY_NO, cash_c.CITY_NO) = ci.CITY_NO AND NVL(c.CNTRY_NO, cash_c.CNTRY_NO) = ci.CNTRY_NO AND NVL(c.PROV_NO, cash_c.PROV_NO) = ci.PROV_NO
    LEFT JOIN IAS20261.CNTRY co ON NVL(c.CNTRY_NO, cash_c.CNTRY_NO) = co.CNTRY_NO
    WHERE m.BILL_NO = :1
"""
try:
    cur.execute(query, ['2616800625'])
    row = cur.fetchone()
    print("Success:", row is not None)
    if row:
        print("Name:", row[5])
        print("Building:", row[8])
        print("Street:", row[9])
        print("VAT:", row[13])
except Exception as e:
    print(str(e))
