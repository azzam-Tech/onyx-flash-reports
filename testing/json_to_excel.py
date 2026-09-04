import json
import csv
import os

def main():
    json_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\fake_customers_active_only.json'
    csv_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\Active_Fake_Customers.csv'
    
    with open(json_path, 'r', encoding='utf-8') as f:
        fake_customers = json.load(f)
        
    # Write to CSV with utf-8-sig to ensure Excel opens Arabic correctly
    with open(csv_path, 'w', encoding='utf-8-sig', newline='') as f:
        writer = csv.writer(f)
        
        # Write header
        writer.writerow(['رقم العميل', 'اسم العميل', 'الحقول الناقصة أو الوهمية'])
        
        # Write data
        for c in fake_customers:
            writer.writerow([c['code'], c['name'], c['issues']])
            
    print(f"Excel (CSV) file created successfully at: {csv_path}")

if __name__ == "__main__":
    main()
