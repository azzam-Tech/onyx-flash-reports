app_path = r"c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py"

with open(app_path, "r", encoding="utf-8") as f:
    content = f.read()

target = '{"id":"true_income_statement","title":"قائمة الدخل الحقيقية (تكاليف ومصاريف أونكس الحقيقية)","fn":"run_true_income_statement","params":[DFROM,DTO],"sql":""},\n  ]\n,'
replacement = '{"id":"true_income_statement","title":"قائمة الدخل الحقيقية (تكاليف ومصاريف أونكس الحقيقية)","fn":"run_true_income_statement","params":[DFROM,DTO],"sql":""}\n  ]},'

if target in content:
    content = content.replace(target, replacement)
    with open(app_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("REPLACED PROF CLOSING BRACKET SUCCESSFULLY!")
else:
    print("TARGET NOT FOUND IN CONTENT!")
