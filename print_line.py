import sys

with open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\reports_config.py", "r", encoding="utf-8") as file:
    for i, line in enumerate(file):
        if "مورد" in line:
            print(f"Line {i+1}: {line.strip()}")
