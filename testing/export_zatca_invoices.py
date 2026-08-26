import os
import sys
import csv

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import get_conn

def export_invoices():
    out_dir = os.path.join(os.path.dirname(__file__), '..', 'Results')
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, 'ZATCA_Invoices_M7_M8.csv')
    
    with get_conn() as con:
        with con.cursor() as cur:
            # Query all invoices for July and August
            query = """
                SELECT 
                    BILL_NO, 
                    TO_CHAR(BILL_DATE, 'YYYY-MM-DD') AS B_DATE,
                    BILL_DOC_TYPE AS DOC_TYPE,
                    BILL_AMT,
                    VAT_AMT,
                    CASE WHEN DOC_HASH IS NOT NULL THEN 'Yes' ELSE 'No' END AS HAS_HASH,
                    CASE WHEN WEB_SRVC_UUID IS NOT NULL THEN 'Yes' ELSE 'No' END AS HAS_UUID,
                    NVL(WEB_SRVC_TRNSFR_DATA_FLG, 0) AS SYNC_FLAG
                FROM IAS_BILL_MST
                WHERE BILL_DATE >= TO_DATE('2026-07-01', 'YYYY-MM-DD')
                  AND BILL_DATE < TO_DATE('2026-09-01', 'YYYY-MM-DD')
                ORDER BY BILL_DATE DESC
            """
            cur.execute(query)
            rows = cur.fetchall()
            
            # Count by SYNC_FLAG to provide a summary
            summary = {}
            for r in rows:
                flag = r[7]
                summary[flag] = summary.get(flag, 0) + 1
            print("--- Summary by WEB_SRVC_TRNSFR_DATA_FLG ---")
            for k, v in summary.items():
                print(f"Flag {k}: {v} invoices")
                
            # Write to CSV
            with open(out_file, 'w', newline='', encoding='utf-8-sig') as f:
                writer = csv.writer(f)
                writer.writerow(['رقم الفاتورة', 'التاريخ', 'نوع الفاتورة', 'الإجمالي', 'الضريبة', 'تحتوي على هاش', 'تحتوي على UUID', 'حالة المزامنة (Onyx)'])
                for r in rows:
                    writer.writerow(r)
                    
            print(f"\nExported {len(rows)} invoices to {out_file}")

if __name__ == '__main__':
    export_invoices()
