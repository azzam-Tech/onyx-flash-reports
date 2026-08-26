import sys
import openpyxl
from openpyxl.styles import Font, Alignment
sys.path.append('privet/onyx_reports')
from database import get_conn

def export_invoices():
    conn = get_conn()
    cur = conn.cursor()
    
    # Query to fetch the future invoices
    query = """
    SELECT 
        DOC_TYP_NAME AS "نوع المستند",
        DOC_NO AS "رقم المستند",
        TO_CHAR(DOC_DATE, 'YYYY-MM-DD') AS "تاريخ التوريد/الضريبة",
        DOC_AMT_VAT AS "مبلغ الفاتورة الخاضع",
        VAT_AMT AS "مبلغ الضريبة",
        DOC_AMT_ZERO_VAT AS "المبلغ الصفري",
        DOC_AMT_NO_VAT AS "المبلغ المعفى",
        DOC_AMT_EXPORT_VAT AS "مبلغ الصادرات"
    FROM GNR_TAX_DTL_VW
    WHERE DOC_DATE >= TO_DATE('2026-09-01', 'YYYY-MM-DD')
    ORDER BY DOC_DATE ASC
    """
    
    cur.execute(query)
    rows = cur.fetchall()
    columns = [col[0] for col in cur.description]
    
    # Create workbook and sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Future Invoices"
    ws.sheet_view.rightToLeft = True # Enable RTL for Arabic
    
    # Write Headers
    ws.append(columns)
    
    # Style Headers
    header_font = Font(bold=True)
    for cell in ws[1]:
        cell.font = header_font
        cell.alignment = Alignment(horizontal="center")
    
    # Write Data
    for r in rows:
        ws.append(r)
        
    # Auto-adjust column widths
    for col in ws.columns:
        max_length = 0
        column = col[0].column_letter # Get the column name
        for cell in col:
            try:
                if len(str(cell.value)) > max_length:
                    max_length = len(str(cell.value))
            except:
                pass
        adjusted_width = (max_length + 5)
        ws.column_dimensions[column].width = adjusted_width

    # Save to file
    file_path = "Future_Tax_Invoices.xlsx"
    wb.save(file_path)
    print(f"Exported {len(rows)} invoices to {file_path}")

if __name__ == "__main__":
    try:
        export_invoices()
    except Exception as e:
        import traceback
        traceback.print_exc()
