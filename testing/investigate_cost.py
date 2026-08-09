import os
import sys
import pandas as pd

# Add privet/onyx_reports to path to import database
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    if not conn:
        print("Failed to connect to DB")
        return
    
    rep_code = 144
    date = '2026-06-06'
    
    # Query 1: Find the journal entries for cost of sales (A_CODE = '311010001') for this delegate on this day
    query1 = f"""
    SELECT p.DOC_TYPE, p.DOC_NO, p.DOC_DATE, p.CR_AMT, p.DB_AMT, p.A_CODE, p.REP_CODE, p.REMARK
    FROM IAS_POST_DTL p
    WHERE p.REP_CODE = {rep_code}
      AND p.DOC_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
      AND p.A_CODE = '311010001'
    """
    
    df1 = pd.read_sql(query1, conn)
    print("=== Journal Entries for Cost of Sales ===")
    print(df1)
    
    if not df1.empty:
        # Get the unique document types and numbers
        doc_types = tuple(df1['DOC_TYPE'].unique())
        if len(doc_types) == 1:
            doc_types_str = f"({doc_types[0]})"
        else:
            doc_types_str = str(doc_types)
            
        doc_nos = tuple(df1['DOC_NO'].unique())
        if len(doc_nos) == 1:
            doc_nos_str = f"({doc_nos[0]})"
        else:
            doc_nos_str = str(doc_nos)
            
        print(f"\nDocument Types: {doc_types_str}")
        print(f"Document Nos: {doc_nos_str}")
        
        # Depending on DOC_TYPE, fetch the details.
        # DOC_TYPE 1 = Sales Invoice (IAS_BILL_MST)
        # We need to get the item details and their costs.
        # Onyx usually stores cost in IAS_BILL_DTL ? Let's check columns of IAS_BILL_DTL
        query2 = f"""
        SELECT m.BILL_DOC_TYPE, m.BILL_NO, m.BILL_DATE, m.REP_CODE, d.I_CODE, i.I_NAME, d.I_QTY, d.I_PRICE, d.I_COST
        FROM IAS_BILL_MST m
        JOIN IAS_BILL_DTL d ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
        LEFT JOIN IAS_ITM_MST i ON d.I_CODE = i.I_CODE
        WHERE m.REP_CODE = {rep_code}
          AND m.BILL_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
          AND m.BILL_DOC_TYPE IN {doc_types_str}
          AND m.BILL_NO IN {doc_nos_str}
        """
        
        try:
            df2 = pd.read_sql(query2, conn)
            print("\n=== Invoice Details (IAS_BILL_DTL) ===")
            print(df2)
            
            # Save to Excel
            excel_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f'cost_details_rep_{rep_code}_{date}.xlsx'))
            df2.to_excel(excel_path, index=False)
            print(f"\nSaved details to {excel_path}")
            
        except Exception as e:
            print(f"Error querying details: {e}")
            
            # Let's see what columns are in IAS_BILL_DTL
            cols_query = "SELECT column_name FROM all_tab_columns WHERE table_name = 'IAS_BILL_DTL'"
            df_cols = pd.read_sql(cols_query, conn)
            print("\nColumns in IAS_BILL_DTL:")
            print(df_cols['COLUMN_NAME'].tolist())
            
    conn.close()

if __name__ == "__main__":
    main()
