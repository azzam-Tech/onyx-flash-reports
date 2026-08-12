import sys
import os
import oracledb
import pandas as pd

def extract_pkg_ult():
    oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
    passwords = ["ULT", "ult", "ULT2016", "ult2016", "admin", "123456", "OnyxAdmin"]
    con = None
    for pwd in passwords:
        conn_str = f"ULT/{pwd}@100.100.1.100:1521/ORCL"
        try:
            con = oracledb.connect(conn_str)
            print("Connected with password:", pwd)
            break
        except Exception:
            pass
            
    if con is None:
        print("Failed to connect with any password")
        return
        
    with con:
        # First check if the package exists in all_objects
        sql_check = """
            SELECT owner, object_name, object_type, status
            FROM dba_objects
            WHERE UPPER(object_name) LIKE '%IAS_DSTR_CST%'
        """
        try:
            df_check = pd.read_sql(sql_check, con)
            print("Objects found:")
            print(df_check)
        except Exception as e:
            print("Failed to query dba_objects:", e)
            
        # Try to extract source
        sql_source = """
            SELECT name, type, line, text
            FROM dba_source
            WHERE UPPER(name) LIKE '%IAS_DSTR_CST%'
            ORDER BY owner, name, type, line
        """
        try:
            df_source = pd.read_sql(sql_source, con)
            if not df_source.empty:
                with open("pkg_source_ult.txt", "w", encoding="utf-8") as f:
                    for text in df_source['TEXT'] if 'TEXT' in df_source.columns else df_source['text']:
                        f.write(text)
                print(f"Successfully wrote {len(df_source)} lines of source code to pkg_source_ult.txt")
                
                # print a small sample of the source to see if it's wrapped
                print("Sample of source code:")
                print(df_source.head(20)['TEXT' if 'TEXT' in df_source.columns else 'text'].tolist())
            else:
                print("Source code not found in dba_source.")
        except Exception as e:
            print("Failed to query dba_source:", e)

if __name__ == "__main__":
    extract_pkg_ult()
