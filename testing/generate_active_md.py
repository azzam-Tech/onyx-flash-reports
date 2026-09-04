import json
import os

def main():
    json_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\fake_customers_active_only.json'
    md_path = r'c:\Users\amarn\.gemini\antigravity-ide\brain\4fb2f17e-6238-41c0-acb1-78bf3adf7214\fake_data_active_customers.md'
    
    with open(json_path, 'r', encoding='utf-8') as f:
        fake_customers = json.load(f)
        
    md_content = "# تقرير العملاء النشطين ذوي البيانات الوهمية (باستثناء الشخصي)\n\n"
    md_content += "> [!WARNING]\n"
    md_content += "> هؤلاء العملاء **نشطون حالياً** (غير موقوفين) ولديهم تلاعب في البيانات رغم أنهم مصنفون كشركات أو أعمال وليسوا أفراداً.\n\n"
    md_content += f"**إجمالي العملاء المتلاعبين النشطين:** {len(fake_customers)}\n\n"
    
    if fake_customers:
        md_content += "| رقم العميل | اسم العميل | الحقول الناقصة أو الوهمية |\n"
        md_content += "|---|---|---|\n"
        for c in fake_customers[:100]: 
            md_content += f"| {c['code']} | {c['name']} | {c['issues']} |\n"
        
        if len(fake_customers) > 100:
            md_content += f"\n*(تم عرض أول 100 عميل فقط من أصل {len(fake_customers)})*\n"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
        
    print("Markdown created successfully.")

if __name__ == "__main__":
    main()
