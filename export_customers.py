import sys
import os
import pandas as pd

sys.path.append('privet/onyx_reports')
import database

def export_data():
    conn = database.get_conn()
    
    query = """
    SELECT 
        C.C_CODE AS "كود العميل",
        C.C_A_NAME AS "اسم العميل",
        C.C_TAX_CODE AS "الرقم الضريبي",
        C.C_BOX_CODE AS "الرمز البريدي",
        C.CNTRY_NO AS "رقم الدولة",
        C.CITY_NO AS "رقم المدينة",
        C.DSTRCT_NM AS "الحي",
        C.ADD_NO AS "الرقم الاضافي",
        C.CR_NO AS "رقم السجل التجاري",
        NVL(C.BUILDING_NO, C.BLD_NO) AS "رقم المبنى",
        C.STREET AS "الشارع",
        CI.CITY_A_NAME AS "المدينة",
        C.CSTMR_IDNTFR AS "المعرف"
    FROM IAS20261.CUSTOMER C
    LEFT JOIN IAS20261.CITIES CI ON C.CITY_NO = CI.CITY_NO
    WHERE C.REP_CODE = '153'
    """
    
    df = pd.read_sql(query, conn)
    
    # 1. Export all customers for this rep
    all_file = "العملاء_ديفيد_الهندي_153_محدث.xlsx"
    df.to_excel(all_file, index=False)
    print(f"تم تصدير: {all_file} ({len(df)} عميل)")
    
    # 2. Filter for customers with any missing data in the specified columns
    check_cols = [
        "اسم العميل", "الرقم الضريبي", 
        "رقم الدولة", "رقم المدينة", "الحي", "الرقم الاضافي", 
        "رقم السجل التجاري", "رقم المبنى", "الشارع", "المدينة", "المعرف"
    ]
    
    def has_missing(row):
        for col in check_cols:
            val = row[col]
            if pd.isna(val) or str(val).strip() == '' or str(val).strip() == 'None':
                return True
        return False
        
    missing_df = df[df.apply(has_missing, axis=1)]
    
    missing_file = "العملاء_نواقص_بيانات_153_محدث.xlsx"
    missing_df.to_excel(missing_file, index=False)
    print(f"تم تصدير: {missing_file} ({len(missing_df)} عميل)")

if __name__ == '__main__':
    export_data()
