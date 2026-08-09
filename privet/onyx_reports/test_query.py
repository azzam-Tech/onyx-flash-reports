import reports_config
from database import get_conn
import pandas as pd

try:
    sql = None
    for tab in reports_config.TABS:
        if 'reports' in tab:
            for r in tab['reports']:
                if r['id'] == 'stock_bal':
                    sql = r['sql']
    
    with get_conn() as con:
        sql_test = sql.replace(':as_of', "'2026-07-31'").replace(':w_code', 'NULL').replace(':i_code', 'NULL')
        df = pd.read_sql(sql_test, con)
        print('Query successful! Columns:', list(df.columns))
except Exception as e:
    print('Error:', e)
