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

with open(r'C:\Users\amarn\.gemini\antigravity-ide\brain\829eac90-8e42-445a-b229-8b86a005b556\rep_142_report.md', 'w', encoding='utf-8') as f:
    f.write("# تقرير تفصيلي للتحصيلات: المندوب 142 (شهر 6 - 2026)\n\n")
    f.write("هذا التقرير يوضح مصادر التحصيلات (سندات القبض + قيود التسوية) لكل عميل تابع للمندوب 142 في شهر 6، بالإضافة إلى المبيعات النقدية للمندوب، للوصول إلى الإجمالي المحصل (2,523,880.10) كما يظهر في نظام التحصيل الديناميكي.\n\n")
    
    f.write("## 1. المبيعات النقدية (بدون عملاء)\n")
    
    cur.execute("""
        SELECT SUM(NVL(p.DR_AMT,0)) FROM IAS20261.IAS_BILL_MST b 
        JOIN IAS20261.IAS_POST_DTL p ON p.DOC_NO = b.BILL_NO AND p.DOC_SER = b.BILL_SER AND p.DOC_TYPE = 4 AND TO_CHAR(p.A_CODE) LIKE '111%' 
        WHERE b.BILL_DOC_TYPE=1 AND NVL(p.DOC_POST,0)=1 AND p.DR_AMT > 0 
          AND b.BILL_DATE >= TO_DATE('2026-06-01','YYYY-MM-DD') AND b.BILL_DATE < TO_DATE('2026-07-01','YYYY-MM-DD') 
          AND TO_CHAR(b.REP_CODE) = '142'
    """)
    cash_sales = cur.fetchone()[0] or 0.0
    f.write(f"- إجمالي المبيعات النقدية المباشرة للمندوب: **{cash_sales:,.2f}** ريال.\n\n")
    
    f.write("## 2. تفصيل تحصيلات العملاء الآجلين (سندات وقيود)\n")
    f.write("| رقم العميل | اسم العميل | سندات القبض | قيود التسوية | إجمالي تحصيل العميل |\n")
    f.write("|---|---|---|---|---|\n")
    
    tot_r = 0; tot_j = 0
    for ccode, d in sorted(cust_data.items(), key=lambda x: (x[1]['rcpt']+x[1]['jrn']), reverse=True):
        r = d['rcpt']; j = d['jrn']; t = r + j
        if t == 0: continue
        tot_r += r; tot_j += j
        f.write(f"| {ccode} | {d['name']} | {r:,.2f} | {j:,.2f} | {t:,.2f} |\n")
    
    f.write(f"| **الإجمالي** | | **{tot_r:,.2f}** | **{tot_j:,.2f}** | **{tot_r+tot_j:,.2f}** |\n\n")
    
    f.write("## الخلاصة والمطابقة النهائية\n")
    f.write(f"- **إجمالي مبيعات نقدية:** {cash_sales:,.2f}\n")
    f.write(f"- **إجمالي سندات قبض العملاء:** {tot_r:,.2f}\n")
    f.write(f"- **إجمالي تسويات العملاء:** {tot_j:,.2f}\n")
    f.write(f"- **المجموع الكلي (Total Dynamic Collections):** **{(cash_sales + tot_r + tot_j):,.2f}**\n\n")
    
    f.write("> **ملاحظة للمحاسب:** تقرير أونكس لأعمار التحصيل (2,166,028.83) لا يتضمن المبيعات النقدية (238,921.84) ولا قيود التسوية الدائنة (78,186.00). بالإضافة إلى وجود فروقات في طريقة توزيع التحصيل على أعمار الفواتير نتيجة استبعاد القيود، مما يُظهر مبالغ أكبر في الفئات المتأخرة في أونكس مقارنة بتقريرنا الذي يقوم بالتسوية التلقائية فورياً.")

cur.close()
conn.close()
