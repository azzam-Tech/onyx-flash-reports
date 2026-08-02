import oracledb
import pandas as pd

def main():
    try:
        oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
    except Exception as e:
        pass

    conn = oracledb.connect(
        user='RPT_USER',
        password='ULT2016',
        dsn='100.100.1.100:1521/ORCL'
    )
    
    # Query all transactions for Cost Center 101 (الرئيسي) from IAS_POST_DTL
    sql = """
    SELECT 
        p.DOC_TYPE,
        CASE p.DOC_TYPE
            WHEN 0 THEN 'قيد افتتاحي'
            WHEN 1 THEN 'فاتورة مبيعات نقدية'
            WHEN 2 THEN 'مرتجع مبيعات نقدي'
            WHEN 4 THEN 'فاتورة مبيعات آجلة'
            WHEN 5 THEN 'مرتجع مبيعات آجل'
            WHEN 11 THEN 'قيد يومية'
            WHEN 12 THEN 'سند قبض'
            WHEN 13 THEN 'سند صرف'
            WHEN 34 THEN 'رصيد افتتاحي'
            ELSE 'أخرى (' || TO_CHAR(p.DOC_TYPE) || ')'
        END AS doc_type_name,
        p.DOC_NO,
        TO_CHAR(p.DOC_DATE, 'YYYY-MM-DD') as doc_date,
        p.C_CODE,
        NVL(p.DR_AMT, 0) as debit,
        NVL(p.CR_AMT, 0) as credit,
        NVL(p.DR_AMT, 0) - NVL(p.CR_AMT, 0) as balance,
        p.DOC_NO as doc_no_dup
    FROM IAS20261.IAS_POST_DTL p
    WHERE NVL(p.DOC_POST,0)=1 
      AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
      AND p.CC_CODE = '101'
    ORDER BY p.DOC_DATE, p.DOC_NO
    """
    
    df = pd.read_sql(sql, conn)
    
    # Filter to only show the most significant transactions (e.g. credit > 0)
    # or just export everything to an Excel file so the user can filter.
    output_file = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\CostCenter_101_Details.csv'
    # Save as CSV with utf-8-sig for Arabic support in Excel
    df.to_csv(output_file, index=False, encoding='utf-8-sig')
    
    print(f"Exported detailed transactions for CC 101 to {output_file}")
    
    # Let's also print a summary of balances by DOC_TYPE
    summary_sql = """
    SELECT 
        p.DOC_TYPE,
        COUNT(*) as trn_count,
        SUM(NVL(p.DR_AMT, 0)) as total_debit,
        SUM(NVL(p.CR_AMT, 0)) as total_credit,
        SUM(NVL(p.DR_AMT, 0) - NVL(p.CR_AMT, 0)) as total_balance
    FROM IAS20261.IAS_POST_DTL p
    WHERE NVL(p.DOC_POST,0)=1 
      AND (p.C_CODE IS NOT NULL OR p.C_V_CODE IS NOT NULL)
      AND p.CC_CODE = '101'
    GROUP BY p.DOC_TYPE
    ORDER BY total_balance
    """
    summary_df = pd.read_sql(summary_sql, conn)
    print("\nSummary by Document Type for CC 101:")
    print(summary_df)

if __name__ == '__main__':
    main()
