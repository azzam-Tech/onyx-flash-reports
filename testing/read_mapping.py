import openpyxl

try:
    wb = openpyxl.load_workbook('Results/Province_Mapping_Template.xlsx')
    ws = wb['خريطة دمج المحافظات']
    
    print("Mapping provided by user:")
    for row in ws.iter_rows(min_row=2, values_only=True):
        wrong_id, wrong_name, correct_id = row
        if correct_id is not None and str(correct_id).strip() != '':
            print(f"Wrong: {wrong_id} ({wrong_name}) -> Correct: {correct_id}")
            
except Exception as e:
    print(f"Error: {e}")
