import re

def main():
    file_path = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # We want to extract the dictionary definitions for these reports:
    # 1. debt_movement_summary
    # 2. statement_analytic
    # 3. perf_aging_dynamic_analytical
    # 4. perf_aging_dynamic
    # 5. true_income_statement
    
    reports_to_find = [
        "debt_movement_summary",
        "statement_analytic",
        "perf_aging_dynamic_analytical",
        "perf_aging_dynamic",
        "true_income_statement"
    ]
    
    extracted = []
    
    for rid in reports_to_find:
        # Regex to match {"id":"<rid>", ... }
        # Since SQL queries contain """, we must match until the closing }, 
        # But report dicts can be complex.
        # Let's find the exact string '{"id":"' + rid + '"'
        start_idx = content.find('{"id":"' + rid + '"')
        if start_idx == -1:
            start_idx = content.find("{'id':'" + rid + "'")
        
        if start_idx != -1:
            # find the end of the dictionary. It ends with '}' that matches the opening '{'
            brace_count = 0
            in_string = False
            str_char = ''
            in_triple_string = False
            triple_char = ''
            
            end_idx = -1
            i = start_idx
            while i < len(content):
                c = content[i]
                
                if in_triple_string:
                    if content[i:i+3] == triple_char:
                        in_triple_string = False
                        i += 2
                elif in_string:
                    if c == '\\':
                        i += 1
                    elif c == str_char:
                        in_string = False
                else:
                    if content[i:i+3] in ['"""', "'''"]:
                        in_triple_string = True
                        triple_char = content[i:i+3]
                        i += 2
                    elif c in ['"', "'"]:
                        in_string = True
                        str_char = c
                    elif c == '{':
                        brace_count += 1
                    elif c == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            end_idx = i
                            break
                i += 1
                
            if end_idx != -1:
                rep_dict_str = content[start_idx:end_idx+1]
                extracted.append(rep_dict_str)
                print(f"Found {rid}")
            else:
                print(f"Could not find end of {rid}")
        else:
            print(f"Could not find {rid}")
            
    # Now construct the new tab
    new_tab = f'''
 {{"id":"summary","title":"ملخص التقارير","icon":"M13 3h8v8h-8zM3 13h8v8H3zM13 13h8v8h-8zM3 3h8v8H3z","reports":[
   {', '.join(extracted)}
 ]}},'''

    # Insert it after TABS = [
    tabs_idx = content.find("TABS = [")
    if tabs_idx != -1:
        insert_idx = content.find("[", tabs_idx) + 1
        new_content = content[:insert_idx] + "\n" + new_tab + content[insert_idx:]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully added summary tab to app.py")
    else:
        print("Could not find TABS = [")

if __name__ == '__main__':
    main()
