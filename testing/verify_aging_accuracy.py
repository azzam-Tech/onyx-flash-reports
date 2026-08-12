import sys, os
sys.path.append(os.path.abspath('privet/onyx_reports'))
import report_handlers
from database import get_conn
import pandas as pd

try:
    print("Checking 5 random customers for accuracy...")
    args = {
        "date_to": "2026-08-31",
        "aging_ranges": "2,30,60,90,120"
    }
    rpt = {"id": "aging"}
    
    cols, rows = report_handlers.run_cust_aging(rpt, args)
    
    aging_totals = {}
    for r in rows:
        c_code = r[0]
        tot = float(r[-1].replace(',', ''))
        aging_totals[c_code] = tot
        
    if not aging_totals:
        print("No customers with debt.")
        sys.exit(0)
        
    top_5 = list(aging_totals.keys())[:5]
    
    with get_conn() as con:
        placeholders = ','.join([f"'{c}'" for c in top_5])
        sql = f"""
            SELECT TO_CHAR(C_CODE) as c_code, 
                   SUM(NVL(DR_AMT,0)) as dr, 
                   SUM(NVL(CR_AMT,0)) as cr,
                   SUM(NVL(DR_AMT,0)) - SUM(NVL(CR_AMT,0)) as actual_bal
            FROM IAS20261.IAS_POST_DTL
            WHERE (NVL(DOC_POST,0)=1 OR (NVL(DOC_POST,0)=0 AND DOC_TYPE=2))
              AND DOC_DATE < TO_DATE('2026-08-31', 'YYYY-MM-DD')+1
              AND TO_CHAR(C_CODE) IN ({placeholders})
            GROUP BY TO_CHAR(C_CODE)
        """
        df = pd.read_sql(sql, con)
        
    print("\\n--- Matches ---")
    for _, row in df.iterrows():
        c_code = row['C_CODE']
        actual_bal = round(row['ACTUAL_BAL'], 2)
        aging_bal = round(aging_totals.get(c_code, 0.0), 2)
        
        status = "MATCH" if actual_bal == aging_bal else "MISMATCH"
        print(f"Cust: {c_code} | DB: {actual_bal} | Aging: {aging_bal} | Status: {status}")

except Exception as e:
    import traceback
    traceback.print_exc()
