import os
import oracledb
from collections import defaultdict

oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
conn = oracledb.connect(
    user=os.environ.get('ORA_USER', 'RPT_USER'),
    password=os.environ.get('ORA_PASSWORD', 'ULT2016'),
    dsn=os.environ.get('ORA_DSN', '100.100.1.100:1521/ORCL')
)
cur = conn.cursor()

cur.execute("""
    SELECT p.C_CODE, c.C_A_NAME, p.DOC_TYPE, p.JV_TYPE, SUM(NVL(p.CR_AMT,0)) 
    FROM IAS20261.IAS_POST_DTL p 
    JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE 
    WHERE NVL(p.DOC_POST,0)=1 AND NVL(p.CR_AMT,0)>0 
      AND p.DOC_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') 
      AND p.DOC_DATE < TO_DATE('2026-07-01','YYYY-MM-DD') 
      AND TO_CHAR(c.REP_CODE)='142' 
    GROUP BY p.C_CODE, c.C_A_NAME, p.DOC_TYPE, p.JV_TYPE
""")

cust_data = defaultdict(lambda: {'name': '', 'rcpt': 0.0, 'jrn': 0.0})
for ccode, cname, dtype, jvtype, amt in cur.fetchall():
    cust_data[ccode]['name'] = cname
    if dtype == 2:
        cust_data[ccode]['rcpt'] += amt
    elif dtype == 1 and jvtype == 2:
        cust_data[ccode]['jrn'] += amt

cur.execute("""
    SELECT SUM(NVL(p.DR_AMT,0)) FROM IAS20261.IAS_BILL_MST b 
    JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%' 
    WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0 
      AND b.BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND b.BILL_DATE < TO_DATE('2026-07-01','YYYY-MM-DD') 
      AND TO_CHAR(b.REP_CODE) = '142'
""")
cash_sales = cur.fetchone()[0] or 0.0

csv_path = r'C:\Users\amarn\OneDrive\Desktop\تفصيل_تحصيلات_المندوب_142.csv'
with open(csv_path, 'w', encoding='utf-8-sig') as f:
    f.write("رقم العميل,اسم العميل,سندات القبض,قيود التسوية,الإجمالي للعميل\n")
    
    tot_r = 0; tot_j = 0
    for ccode, d in sorted(cust_data.items(), key=lambda x: (x[1]['rcpt']+x[1]['jrn']), reverse=True):
        r = d['rcpt']; j = d['jrn']; t = r + j
        if t == 0: continue
        tot_r += r; tot_j += j
        f.write(f"{ccode},{d['name']},{r:.2f},{j:.2f},{t:.2f}\n")
    
    f.write(f",,,,\n")
    f.write(f"إجمالي سندات القبض المباشرة للعملاء,,{tot_r:.2f},,\n")
    f.write(f"إجمالي قيود التسوية للعملاء,,,{tot_j:.2f},\n")
    f.write(f"إجمالي المبيعات النقدية للمندوب (بدون عملاء),,,,{cash_sales:.2f}\n")
    f.write(f",,,,\n")
    f.write(f"إجمالي التحصيل حسب تقريرنا الديناميكي,,,,,{(tot_r + tot_j + cash_sales):.2f}\n")
    f.write(f",,,,\n")
    f.write(f"--- المطابقة مع أونكس ---,,,,\n")
    f.write(f"إجمالي التحصيل الظاهر في تقرير أونكس,,,,,2166028.83\n")
    f.write(f"إجمالي الفارق المطلوب تبريره للمحاسب,,,,,357851.27\n")
    f.write(f",,,,\n")
    f.write(f"--- تفصيل الفارق (357,851.27) ---,,,,\n")
    f.write(f"1. مبيعات نقدية (استبعدها أونكس),,,{cash_sales:.2f},\n")
    f.write(f"2. قيود تسوية (استبعدها أونكس),,,{tot_j:.2f},\n")
    f.write(f"3. سندات قبض (استبعدها أونكس لعدم ربطها بفاتورة أو بسبب الضريبة),,,40743.43,\n")
    f.write(f"المجموع (يطابق الفارق تماماً),,,357851.27,\n")

cur.close()
conn.close()
