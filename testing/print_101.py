import oracledb
import pandas as pd
oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')

sql = '''
SELECT 
    CASE p.DOC_TYPE
        WHEN 0 THEN 'قيد افتتاحي (0)'
        WHEN 1 THEN 'فاتورة مبيعات نقدية (1)'
        WHEN 2 THEN 'مرتجع نقدي (2)'
        WHEN 3 THEN 'سند صرف (3)'
        WHEN 4 THEN 'فاتورة مبيعات آجلة (4)'
        WHEN 5 THEN 'مرتجع مبيعات آجل (5)'
        WHEN 6 THEN 'تسوية/قيد يومية (6)'
        WHEN 7 THEN 'تسوية (7)'
        WHEN 11 THEN 'قيد يومية (11)'
        WHEN 12 THEN 'سند قبض (12)'
        WHEN 16 THEN 'إشعار (16)'
        WHEN 34 THEN 'رصيد افتتاحي (34)'
        ELSE 'مستند نوع ' || TO_CHAR(p.DOC_TYPE)
    END AS DOC_NAME,
    COUNT(*) as TRN_COUNT,
    SUM(NVL(p.DR_AMT, 0)) as TOTAL_DEBIT,
    SUM(NVL(p.CR_AMT, 0)) as TOTAL_CREDIT,
    SUM(NVL(p.DR_AMT, 0) - NVL(p.CR_AMT, 0)) as TOTAL_BALANCE
FROM IAS20261.IAS_POST_DTL p
WHERE NVL(p.DOC_POST,0)=1 
  AND p.CC_CODE = '101'
  AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
GROUP BY p.DOC_TYPE
ORDER BY TOTAL_BALANCE
'''
df = pd.read_sql(sql, conn)
for _, row in df.iterrows():
    print(f"[{row['DOC_NAME']}]: DR={row['TOTAL_DEBIT']:,.2f} | CR={row['TOTAL_CREDIT']:,.2f} | BAL={row['TOTAL_BALANCE']:,.2f}")

total = df['TOTAL_BALANCE'].sum()
print(f"\\nFINAL BALANCE = {total:,.2f}")
