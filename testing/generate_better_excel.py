import oracledb
import pandas as pd
import os

def main():
    try:
        oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
    except:
        pass

    conn = oracledb.connect(
        user='RPT_USER',
        password='ULT2016',
        dsn='100.100.1.100:1521/ORCL'
    )
    
    # 1. Summary by Customer in CC 101
    sql_summary = """
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
    ORDER BY "الرصيد النهائي" ASC
    """
    df_summary = pd.read_sql(sql_summary, conn)
    
    # 2. Detailed transactions for all customers in CC 101, showing doc types and names
    sql_details = """
    SELECT 
        NVL(c.C_A_NAME, 'عميل غير معروف') as "اسم العميل",
        CASE p.DOC_TYPE
            WHEN 0 THEN 'قيد افتتاحي (0)'
            WHEN 1 THEN 'فاتورة مبيعات نقدية (1)'
            WHEN 2 THEN 'مرتجع نقدي (2)'
            WHEN 3 THEN 'سند صرف/تسوية (3)'
            WHEN 4 THEN 'فاتورة مبيعات آجلة (4)'
            WHEN 5 THEN 'مرتجع مبيعات آجل (5)'
            WHEN 6 THEN 'قيد يومية/تسوية (6)'
            WHEN 11 THEN 'قيد يومية (11)'
            WHEN 12 THEN 'سند قبض (12)'
            WHEN 16 THEN 'إشعار (16)'
            WHEN 34 THEN 'رصيد افتتاحي (34)'
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
      AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
      AND p.CC_CODE = '101'
    ORDER BY p.C_CODE, p.DOC_DATE, p.DOC_NO
    """
    df_details = pd.read_sql(sql_details, conn)
    
    output_file = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\تحليل_سوالب_مركز_101.xlsx'
    
    with pd.ExcelWriter(output_file, engine='openpyxl') as writer:
        df_summary.to_excel(writer, sheet_name='ملخص العملاء (من عليه سوالب)', index=False)
        df_details.to_excel(writer, sheet_name='تفاصيل كل الحركات', index=False)
        
    print(f"Generated Excel report at {output_file}")

if __name__ == '__main__':
    main()
