with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

target = """_lib = os.environ.get("ORA_LIB_DIR", r"C:\\oracle\\instantclient\\instantclient_23_0")
try:
    oracledb.init_oracle_client(lib_dir=_lib) if _lib else oracledb.init_oracle_client()
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)"""

replacement = """try:
    oracledb.init_oracle_client(lib_dir=r"C:\\oracle\\instantclient\\instantclient_23_0")
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)"""

if target in text:
    text = text.replace(target, replacement)
    with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Explicit thick mode path updated!")
else:
    print("Target not found, checking...")
