import pandas as pd
from database import get_conn

with get_conn() as con:
    sql = '''
        SELECT p.flow_id, p.page_id, p.plug_name, p.plug_source 
        FROM APEX_220100.WWV_FLOW_PAGE_PLUGS p
        WHERE LOWER(p.plug_source) LIKE '%ias_bill_mst%' 
           OR LOWER(p.plug_source) LIKE '%item_movement%'
    '''
    df = pd.read_sql(sql, con)
    for index, row in df.iterrows():
        print(f"APP: {row['FLOW_ID']} PAGE: {row['PAGE_ID']} PLUG: {row['PLUG_NAME']}")
        print(row['PLUG_SOURCE'][:1500])
        print('------------------')
