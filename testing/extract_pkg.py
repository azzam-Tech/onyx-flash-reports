import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", "privet", "onyx_reports"))
from database import get_conn
import pandas as pd

def extract_pkg_source():
    with get_conn() as con:
        sql = """
            SELECT text
            FROM all_source
            WHERE owner = 'IAS20261' 
              AND name = 'IAS_DSTR_CST_DR_PKG'
            ORDER BY type, line
        """
        df = pd.read_sql(sql, con)
        if df.empty:
            print("Package IAS_DSTR_CST_DR_PKG not found.")
            sql = """
                SELECT text
                FROM all_source
                WHERE owner = 'IAS20261' 
                  AND UPPER(name) LIKE '%IAS_DSTR_CST%'
                ORDER BY name, type, line
            """
            df = pd.read_sql(sql, con)
            
        if not df.empty:
            with open("pkg_source.txt", "w", encoding="utf-8") as f:
                for text in df['TEXT'] if 'TEXT' in df.columns else df['text']:
                    f.write(text)
            print("Source saved to pkg_source.txt")
        else:
            print("No matching package found.")

if __name__ == "__main__":
    extract_pkg_source()
