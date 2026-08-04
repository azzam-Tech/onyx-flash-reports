import sys
import os
import pandas as pd

sys.path.append('privet/onyx_reports')
import database

def export_data():
    conn = database.get_conn()
    
    # Query all customers with their Sales Representative name
    query = """
    SELECT 
        C.REP_CODE AS "المندوب",
        NVL(S.REPRS_A_NAME, 'غير محدد') AS "اسم المندوب",
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
    LEFT JOIN IAS20261.SALES_MAN S ON C.REP_CODE = S.REPRS_CODE
    """
    
    df = pd.read_sql(query, conn)
    
    # Fields that must not be empty (Excluding "المعرف")
    check_cols = [
        "اسم العميل", "الرقم الضريبي", 
        "رقم الدولة", "رقم المدينة", "الحي", "الرقم الاضافي", 
        "رقم السجل التجاري", "رقم المبنى", "الشارع", "المدينة"
    ]
    
    def has_missing(row):
        for col in check_cols:
            val = row[col]
            if pd.isna(val) or str(val).strip() == '' or str(val).strip() == 'None':
                return True
        return False
        
    # Get only missing customers
    missing_df = df[df.apply(has_missing, axis=1)]
    
    # Create folder
    output_dir = "نواقص_العملاء_بدون_شرط_المعرف"
    os.makedirs(output_dir, exist_ok=True)
    
    # Group by representative and save a file for each
    grouped = missing_df.groupby("المندوب")
    
    count_files = 0
    for rep_code, group_df in grouped:
        if pd.isna(rep_code) or str(rep_code).strip() == '':
            rep_code = "بدون_مندوب"
        
        rep_name = group_df.iloc[0]["اسم المندوب"]
        
        # Clean rep_name for valid filename
        safe_rep_name = "".join(c for c in str(rep_name) if c.isalnum() or c in (' ', '_', '-')).strip()
        safe_rep_code = "".join(c for c in str(rep_code) if c.isalnum() or c in (' ', '_', '-')).strip()
        
        file_name = f"نواقص_المندوب_{safe_rep_code}_{safe_rep_name}.xlsx"
        file_path = os.path.join(output_dir, file_name)
        
        group_df.to_excel(file_path, index=False)
        count_files += 1

    print(f"تم إنشاء {count_files} ملف إكسل داخل مجلد: {output_dir}")

if __name__ == '__main__':
    export_data()
