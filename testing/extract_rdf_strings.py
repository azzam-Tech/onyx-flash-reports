import string
import re
import os

def extract_strings(filename, min_length=4):
    with open(filename, errors="ignore", encoding="latin1") as f:
        content = f.read()
    
    # Extract sequences of printable characters
    pattern = f"[{string.printable}]{{{min_length},}}"
    strings = re.findall(pattern, content)
    
    # Also extract sequences of arabic characters just in case
    # Arabic range: \u0600-\u06FF
    arabic_pattern = f"[\u0600-\u06FF\s]{{{min_length},}}"
    arabic_strings = re.findall(arabic_pattern, content)
    
    return strings + arabic_strings

def main():
    rdf_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\onyx_files\Ias_Sales_NeT_Othrs_Sum2.rdf"
    out_path = r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\rdf_strings.txt"
    
    if not os.path.exists(rdf_path):
        print("File not found:", rdf_path)
        return
        
    all_strings = extract_strings(rdf_path, min_length=10)
    
    with open(out_path, "w", encoding="utf-8") as f:
        for s in all_strings:
            f.write(s + "\n")
            
    print(f"Extracted {len(all_strings)} strings to {out_path}")

if __name__ == "__main__":
    main()
