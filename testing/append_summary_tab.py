import re

def main():
    file_path = r'C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Extract collection_adopted dictionary
    rid = "collection_adopted"
    start_idx = content.find('{"id":"' + rid + '"')
    if start_idx == -1:
        start_idx = content.find("{'id':'" + rid + "'")
        
    if start_idx == -1:
        print("Could not find collection_adopted")
        return
        
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
        
    if end_idx == -1:
        print("Could not parse collection_adopted")
        return
        
    rep_dict_str = content[start_idx:end_idx+1]
    print("Found collection_adopted")

    # 2. Find the summary tab and insert this report at the end of its reports list
    summary_start_idx = content.find('{"id":"summary"')
    if summary_start_idx == -1:
        print("Could not find summary tab")
        return
        
    # Find the reports list inside the summary tab
    reports_list_idx = content.find('"reports":[', summary_start_idx)
    if reports_list_idx == -1:
        print("Could not find reports list in summary tab")
        return
        
    # We want to insert rep_dict_str just before the closing ] of the summary tab's reports list.
    # We can parse to find the end of the summary tab's reports array.
    reports_start_bracket_idx = content.find('[', reports_list_idx)
    
    bracket_count = 0
    in_string = False
    str_char = ''
    in_triple_string = False
    triple_char = ''
    
    list_end_idx = -1
    i = reports_start_bracket_idx
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
            elif c == '[':
                bracket_count += 1
            elif c == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    list_end_idx = i
                    break
        i += 1
        
    if list_end_idx == -1:
        print("Could not find end of reports list for summary tab")
        return
        
    # Check if the list is empty (only whitespace before ])
    list_contents = content[reports_start_bracket_idx+1:list_end_idx]
    if list_contents.strip():
        # Not empty, so we prepend a comma
        insertion = ",\n   " + rep_dict_str
    else:
        insertion = "\n   " + rep_dict_str
        
    new_content = content[:list_end_idx] + insertion + content[list_end_idx:]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print("Successfully added collection_adopted to summary tab")

if __name__ == '__main__':
    main()
