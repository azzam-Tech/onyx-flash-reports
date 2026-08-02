import oracledb
import os
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
    
    # We want to check the GL_BASE for cost center 101 and account type = Customers (usually ACC_TYPE=3 or we just check all transactions for this CC)
    # Actually, in Onyx, customer accounts are usually linked to Cost Centers in IAS_BILL_MST or GL_BASE.
    # Let's query the summary of all GL transactions for Cost Center 101.
    sql = """
    SELECT DOC_TYPE, DOC_NO, DOC_DATE, DEBIT, CREDIT, NARRATION 
    FROM GL_BASE 
    WHERE CC_CODE = '101' 
    -- AND ACC_NO LIKE '121%' -- assuming 121 is customers
    ORDER BY DOC_DATE DESC
    FETCH FIRST 50 ROWS ONLY
    """
    
    df = pd.read_sql(sql, conn)
    print("Recent GL_BASE transactions for CC 101:")
    print(df)
    
    # Also let's check the total debit/credit for CC 101
    sql2 = """
    SELECT SUM(DEBIT) as total_debit, SUM(CREDIT) as total_credit, SUM(DEBIT - CREDIT) as balance
    FROM GL_BASE
    WHERE CC_CODE = '101'
    """
    df2 = pd.read_sql(sql2, conn)
    print("\nTotal Balance for CC 101 in GL_BASE:")
    print(df2)

if __name__ == '__main__':
    main()
