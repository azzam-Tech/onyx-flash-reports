import re
import pandas as pd
from database import get_conn

with open('reports_config.py', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'\"id\":\s*\"true_income_statement\".*?\"sql\":\s*\"\"\"(.*?)\"\"\"', text, re.DOTALL)
if m:
    sql = m.group(1)
    
    # replace parameters
    sql = sql.replace(':rep_code', "'144'")
    sql = sql.replace(':date_from', "'2026-06-01'")
    sql = sql.replace(':date_to', "'2026-06-30'")
    
    with get_conn() as con:
        df = pd.read_sql(sql, con)
        pd.set_option('display.max_columns', None)
        pd.set_option('display.width', 1000)
        print(df)
else:
    print("SQL not found")
