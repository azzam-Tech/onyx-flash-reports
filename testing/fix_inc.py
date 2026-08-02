import re

with open('testing/app_rebuild4.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = 'INCR  = {"name":"inc_rcpt","label":" ","type":"select","default":"1","options":[["1",""],["0",""]]}'

replacement = """INCR  = {"name":"inc_rcpt","label":" ","type":"select","default":"1","options":[["1",""],["0",""]]}
INCN  = {"name":"inc_net","label":"  ","type":"select","default":"1","options":[["1",""],["0",""]]}
INCC  = {"name":"inc_cash","label":" ","type":"select","default":"1","options":[["1",""],["0",""]]}
INCRT = {"name":"inc_ret","label":"  ()","type":"select","default":"1","options":[["1",""],["0",""]]}
INCEX = {"name":"inc_ext","label":"   ()","type":"select","default":"0","hidden":True,"options":[["1",""],["0",""]]}"""

if target in text and "INCN" not in text:
    text = text.replace(target, replacement)
    with open('testing/app_rebuild4.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed in app_rebuild4.py")
else:
    print("Target not found or already fixed.")
