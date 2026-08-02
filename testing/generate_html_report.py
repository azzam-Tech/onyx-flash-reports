import oracledb
import pandas as pd

def main():
    try:
        oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
    except:
        pass
    conn = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')
    
    sql_summary = '''
    SELECT 
        c.C_CODE as "رقم العميل",
        NVL(c.C_A_NAME, 'عميل غير معروف') as "اسم العميل",
        SUM(NVL(p.DR_AMT, 0)) as "إجمالي مدين (عليه)",
        SUM(NVL(p.CR_AMT, 0)) as "إجمالي دائن (له)",
        SUM(NVL(p.DR_AMT, 0) - NVL(p.CR_AMT, 0)) as "الرصيد النهائي"
    FROM IAS20261.IAS_POST_DTL p
    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 
      AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
      AND p.CC_CODE = '101'
    GROUP BY c.C_CODE, c.C_A_NAME
    HAVING SUM(NVL(p.DR_AMT, 0) - NVL(p.CR_AMT, 0)) < 0
    ORDER BY "الرصيد النهائي" ASC
    '''
    df_summary = pd.read_sql(sql_summary, conn)
    
    sql_details = '''
    SELECT 
        NVL(c.C_A_NAME, 'عميل غير معروف') as "اسم العميل",
        CASE p.DOC_TYPE
            WHEN 0 THEN 'قيد افتتاحي'
            WHEN 1 THEN 'فاتورة مبيعات نقدية'
            WHEN 2 THEN 'مرتجع نقدي'
            WHEN 3 THEN 'سند صرف/تسوية'
            WHEN 4 THEN 'فاتورة مبيعات آجلة'
            WHEN 5 THEN 'مرتجع مبيعات آجل'
            WHEN 6 THEN 'قيد يومية/تسوية'
            WHEN 11 THEN 'قيد يومية'
            WHEN 12 THEN 'سند قبض'
            WHEN 16 THEN 'إشعار'
            WHEN 34 THEN 'رصيد افتتاحي'
            ELSE 'مستند نوع ' || TO_CHAR(p.DOC_TYPE)
        END AS "نوع المستند",
        p.DOC_NO as "رقم المستند",
        TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') as "التاريخ",
        NVL(p.DR_AMT, 0) as "مدين (عليه)",
        NVL(p.CR_AMT, 0) as "دائن (له)",
        p.DOC_DESC as "البيان"
    FROM IAS20261.IAS_POST_DTL p
    LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
    WHERE NVL(p.DOC_POST,0)=1 
      AND p.CC_CODE = '101'
      AND c.C_CODE IN (
          SELECT p2.C_CODE FROM IAS20261.IAS_POST_DTL p2 
          WHERE p2.CC_CODE='101' GROUP BY p2.C_CODE 
          HAVING SUM(NVL(p2.DR_AMT, 0) - NVL(p2.CR_AMT, 0)) < 0
      )
    ORDER BY c.C_CODE, p.DOC_DATE, p.DOC_NO
    '''
    df_details = pd.read_sql(sql_details, conn)
    
    html = '<html><head><meta charset="utf-8"><style>body{direction:rtl;font-family:Arial,sans-serif;padding:20px;background:#f5f5f5;} table{border-collapse:collapse;width:100%;margin-bottom:30px;background:white;box-shadow:0 1px 3px rgba(0,0,0,0.2);} th,td{border:1px solid #ddd;padding:12px;text-align:right;} th{background-color:#4CAF50;color:white;} tr:nth-child(even){background-color:#f9f9f9;} h2{color:#333;border-bottom:2px solid #4CAF50;padding-bottom:10px;}</style></head><body>'
    html += '<h2>1. ملخص العملاء الذين رصيدهم النهائي سالب (مركز 101)</h2>'
    html += '<p>هذا الجدول يوضح لك من هم العملاء بالتحديد الذين جعلوا رصيد المركز 101 بالسالب</p>'
    html += df_summary.to_html(index=False, classes='table')
    
    html += '<h2>2. تفاصيل كل حركات هؤلاء العملاء (لمعرفة سبب السالب بالتفصيل)</h2>'
    html += '<p>هذا الجدول يعرض كل فاتورة وقيد وسند قبض لكل عميل ظهر في الجدول الأول لمعرفة الحركة الدقيقة التي سببت السالب.</p>'
    html += df_details.to_html(index=False, classes='table')
    html += '</body></html>'
    
    output_path = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\تحليل_سوالب_مركز_101.html'
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(html)
        
    print(f'Generated HTML file successfully at {output_path}')

if __name__ == '__main__':
    main()
