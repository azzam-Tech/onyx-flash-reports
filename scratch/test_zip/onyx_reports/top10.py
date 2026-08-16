import pandas as pd
from database import get_conn

with get_conn() as con:
    sql = '''
        SELECT 
            it.I_NAME as "المنتج", 
            SUM(NVL(d.I_QTY,0)) as "الكمية المباعة"
        FROM IAS20261.IAS_BILL_DTL d
        JOIN IAS20261.IAS_BILL_MST m ON m.BILL_DOC_TYPE = d.BILL_DOC_TYPE AND m.BILL_NO = d.BILL_NO AND m.BILL_SER = d.BILL_SER
        JOIN IAS20261.IAS_ITM_MST it ON it.I_CODE = d.I_CODE
        WHERE EXTRACT(MONTH FROM m.BILL_DATE) = 6
        GROUP BY it.I_NAME
        ORDER BY SUM(NVL(d.I_QTY,0)) DESC
        FETCH FIRST 10 ROWS ONLY
    '''
    df = pd.read_sql(sql, con)
    print(df.to_string(index=False))
