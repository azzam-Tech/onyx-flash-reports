import codecs
with codecs.open("testing/app_rebuild4.py", "r", "utf-8") as f:
    text = f.read()

missing = """
INCN  = {"name":"inc_net","label":"صافي القيود","type":"select","default":"1","options":[["1","نعم"],["0","لا"]]}
INCC  = {"name":"inc_cash","label":"مبيعات نقدية","type":"select","default":"1","options":[["1","نعم"],["0","لا"]]}
INCRT = {"name":"inc_ret","label":"مردود مبيعات (-)","type":"select","default":"1","options":[["1","نعم"],["0","لا"]]}
INCEX = {"name":"inc_ext","label":"إشعارات خصم (-)","type":"select","default":"0","hidden":True,"options":[["1","نعم"],["0","لا"]]}
"""

if "INCRT =" not in text:
    text = text.replace("TABS = [", missing + "\nTABS = [")
    with codecs.open("testing/app_rebuild4.py", "w", "utf-8") as f:
        f.write(text)
    print("Fixed!")
else:
    print("Already fixed")
