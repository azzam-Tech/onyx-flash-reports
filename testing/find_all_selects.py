import re

def main():
    with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\rdf_strings.txt", 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find all SELECT ... FROM blocks, no matter how they are formatted
    matches = re.finditer(r'SELECT\s+.*?\s+FROM\s+.*?(?:\n\n|;|$)', content, re.IGNORECASE | re.DOTALL)
    
    count = 0
    for m in matches:
        count += 1
        text = m.group(0).strip()
        if len(text) > 2000:
            text = text[:2000] + " ... [TRUNCATED]"
        print(f"--- MATCH {count} ---")
        print(text)
        print("---------------------\n")
        
    print(f"Total selects found: {count}")

if __name__ == "__main__":
    main()
