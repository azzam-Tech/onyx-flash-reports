import re
import os

def find_calculations(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's extract blocks that look like SQL or PL/SQL
    # Words like SELECT, FROM, WHERE, function, return, begin
    blocks = []
    
    # Split by double newlines or similar if possible, or just search for patterns
    # Find all SELECT statements
    selects = re.finditer(r'SELECT\s+.*?(?:FROM|INTO)\s+.*?(?:WHERE|ORDER|GROUP|;|$)', content, re.IGNORECASE | re.DOTALL)
    for m in selects:
        match_str = m.group(0)[:500] # Limit to 500 chars
        blocks.append(f"--- SELECT BLOCK ---\n{match_str}\n")
        
    # Find functions/formulas
    functions = re.finditer(r'function\s+\w+\s*return\s+\w+\s+is.*?end;', content, re.IGNORECASE | re.DOTALL)
    for m in functions:
        match_str = m.group(0)[:500]
        blocks.append(f"--- FUNCTION BLOCK ---\n{match_str}\n")
        
    return blocks

if __name__ == "__main__":
    out = find_calculations(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\rdf_strings.txt")
    if not out:
        print("No SQL or functions found.")
    else:
        for b in out:
            print(b)
