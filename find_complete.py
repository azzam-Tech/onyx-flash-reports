import sys
import os
import pandas as pd

sys.path.append('privet/onyx_reports')
import database

def get_complete_reps():
    conn = database.get_conn()
    
    query = """
    SELECT 
        C.REP_CODE,
        NVL(S.REPRS_A_NAME, 'غير محدد') AS REP_NAME,
        C.C_A_NAME, C.C_TAX_CODE, C.CNTRY_NO, C.CITY_NO, 
        C.DSTRCT_NM, C.ADD_NO, C.CR_NO, 
        NVL(C.BUILDING_NO, C.BLD_NO) AS BUILDING_NO, 
        C.STREET, CI.CITY_A_NAME
    FROM IAS20261.CUSTOMER C
    LEFT JOIN IAS20261.CITIES CI ON C.CITY_NO = CI.CITY_NO
    LEFT JOIN IAS20261.SALES_MAN S ON C.REP_CODE = S.REPRS_CODE
    """
    
    df = pd.read_sql(query, conn)
    
    check_cols = [
        "C_A_NAME", "C_TAX_CODE", "CNTRY_NO", "CITY_NO", 
        "DSTRCT_NM", "ADD_NO", "CR_NO", "BUILDING_NO", "STREET", "CITY_A_NAME"
    ]
    
    def is_missing(row):
        for col in check_cols:
            val = row[col]
            if pd.isna(val) or str(val).strip() == '' or str(val).strip() == 'None':
                return True
        return False
        
    df['has_missing'] = df.apply(is_missing, axis=1)
    
    grouped = df.groupby(['REP_CODE', 'REP_NAME'])
    
    complete_reps = []
    for (rep_code, rep_name), group_df in grouped:
        if not group_df['has_missing'].any():
            complete_reps.append(f"{rep_name} ({rep_code})")
            
    if complete_reps:
        for r in complete_reps:
            print(r)
    else:
        print("NO_COMPLETE_REPS")

if __name__ == '__main__':
    get_complete_reps()
