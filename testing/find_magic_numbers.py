import os
import sys
import pandas as pd
from itertools import combinations

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from database import get_conn

def main():
    conn = get_conn()
    date = '2026-06-06'
    
    # Let's get all sum values for m.CC_CODE = 144
    query = f"""
    SELECT 
        SUM(((NVL(d.I_PRICE_LEV_NO,0))+(NVL(d.OTHR_AMT,0))) * NVL(d.I_QTY,0)) as main_bill_amt,
        SUM(NVL(d.I_PRICE_LEV_NO,0) * NVL(d.I_QTY,0)) as just_lev_no,
        SUM(((NVL(d.I_PRICE,0)-NVL(d.DIS_AMT,0)) +(NVL(d.OTHR_AMT,0))) * NVL(d.I_QTY,0)) as bill_amt
    FROM IAS20261.IAS_BILL_MST m
    JOIN IAS20261.IAS_BILL_DTL d ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
    WHERE m.CC_CODE = 144
      AND m.BILL_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
    """
    
    df = pd.read_sql(query, conn)
    print("=== Raw sums ===")
    for col in df.columns:
        print(f"{col}: {df[col].iloc[0]}")
        
    # Let's see if there is any return on this day for CC 144?
    query_ret = f"""
    SELECT 
        SUM((NVL(d.I_PRICE,0) - NVL(d.DIS_AMT,0)) * NVL(d.I_QTY,0)) as ret_basic,
        SUM(d.VAT_AMT) as ret_vat,
        SUM(m.NET_AMT) as ret_net
    FROM IAS20261.IAS_RT_BILL_MST m
    JOIN IAS20261.IAS_RT_BILL_DTL d ON m.RT_BILL_DOC_TYPE = d.RT_BILL_DOC_TYPE AND m.RT_BILL_NO = d.RT_BILL_NO AND m.RT_BILL_SER = d.RT_BILL_SER
    WHERE m.CC_CODE = 144
      AND m.RT_BILL_DATE = TO_DATE('{date}', 'YYYY-MM-DD')
    """
    df_ret = pd.read_sql(query_ret, conn)
    print("\n=== Return sums ===")
    for col in df_ret.columns:
        print(f"{col}: {df_ret[col].iloc[0]}")

    conn.close()

if __name__ == "__main__":
    main()
