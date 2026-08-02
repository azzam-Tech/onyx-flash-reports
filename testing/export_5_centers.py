import oracledb
import pandas as pd
import os

def main():
    try:
        oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
    except Exception as e:
        print("Oracle init warning:", e)

    conn = oracledb.connect(
        user='RPT_USER',
        password='ULT2016',
        dsn='100.100.1.100:1521/ORCL'
    )
    
    centers = ['100', '101', '103', '123', '175']
    output_dir = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity'
    
    for cc in centers:
        print(f"Fetching data for CC {cc}...")
        
        # Detailed analytic statement query for the center
        # Including all operations for the year (2026 since we use IAS20261)
        sql = f"""
        SELECT 
            TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') as "التاريخ",
            p.DOC_NO as "رقم المستند",
            CASE p.DOC_TYPE
                WHEN 0 THEN 'قيد افتتاحي'
                WHEN 1 THEN 'فاتورة مبيعات نقدية'
                WHEN 2 THEN 'مرتجع نقدي'
                WHEN 3 THEN 'سند صرف'
                WHEN 4 THEN 'فاتورة مبيعات آجلة'
                WHEN 5 THEN 'مرتجع مبيعات آجل'
                WHEN 6 THEN 'تسوية/قيد يومية'
                WHEN 11 THEN 'قيد يومية'
                WHEN 12 THEN 'سند قبض'
                WHEN 16 THEN 'إشعار'
                WHEN 34 THEN 'رصيد افتتاحي'
                ELSE TO_CHAR(p.DOC_TYPE)
            END AS "نوع المستند",
            NVL(c.C_A_NAME, 'غير محدد') as "اسم العميل",
            NVL(c.C_CODE, p.C_V_CODE) as "رقم العميل/الحساب",
            NVL(p.DR_AMT, 0) as "مدين",
            NVL(p.CR_AMT, 0) as "دائن",
            p.DOC_DESC as "البيان المحاسبي"
        FROM IAS20261.IAS_POST_DTL p
        LEFT JOIN IAS20261.CUSTOMER c ON c.C_CODE = p.C_CODE
        WHERE NVL(p.DOC_POST,0)=1 
          AND p.CC_CODE = '{cc}'
        ORDER BY p.DOC_DATE, p.DOC_NO
        """
        
        df = pd.read_sql(sql, conn)
        
        # Add running balance per customer, or just overall balance?
        # A simple analytic statement usually has running balance, but since it includes many customers, 
        # it's best to sort by Customer then Date to show individual customer accounts clearly.
        df.sort_values(by=["رقم العميل/الحساب", "التاريخ", "رقم المستند"], inplace=True)
        
        # Calculate running balance per customer
        df['الرصيد'] = df.groupby('رقم العميل/الحساب')['مدين'].cumsum() - df.groupby('رقم العميل/الحساب')['دائن'].cumsum()
        
        # Reorder columns to put Balance after Credit
        cols = ["التاريخ", "رقم المستند", "نوع المستند", "رقم العميل/الحساب", "اسم العميل", "البيان المحاسبي", "مدين", "دائن", "الرصيد"]
        df = df[cols]
        
        output_file = os.path.join(output_dir, f'كشف_تحليلي_مركز_{cc}.xlsx')
        try:
            # We will use xlsxwriter which is usually installed with pandas in these envs, or openpyxl
            df.to_excel(output_file, index=False, engine='openpyxl')
        except ImportError:
            # Fallback to CSV with UTF-8-SIG for Arabic if excel fails
            output_file = os.path.join(output_dir, f'كشف_تحليلي_مركز_{cc}.csv')
            df.to_csv(output_file, index=False, encoding='utf-8-sig')
            
        print(f"Generated {output_file}")

if __name__ == '__main__':
    main()
