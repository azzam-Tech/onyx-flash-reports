import json
import os

def main():
    json_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\fake_customers_data.json'
    md_path = r'c:\Users\amarn\.gemini\antigravity-ide\brain\4fb2f17e-6238-41c0-acb1-78bf3adf7214\fake_data_customers.md'
    
    with open(json_path, 'r', encoding='utf-8') as f:
        fake_customers = json.load(f)
        
    # Generate markdown report
    md_content = "# تقرير العملاء ذوي البيانات الناقصة أو الوهمية (حقول هيئة الزكاة)\n\n"
    md_content += f"**إجمالي العملاء المخالفين:** {len(fake_customers)}\n\n"
    
    if fake_customers:
        md_content += "| رقم العميل | اسم العميل | الحقول الناقصة أو الوهمية |\n"
        md_content += "|---|---|---|\n"
        for c in fake_customers[:100]: # limit to 100
            md_content += f"| {c['code']} | {c['name']} | {c['issues']} |\n"
        
        if len(fake_customers) > 100:
            md_content += f"\n*(تم عرض أول 100 عميل فقط من أصل {len(fake_customers)})*\n"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print("Markdown created successfully.")

if __name__ == "__main__":
    main()
