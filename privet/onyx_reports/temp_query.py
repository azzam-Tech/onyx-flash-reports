from database import get_conn
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

conn = get_conn()
sql = "SELECT * FROM IAS20261.CUSTOMER_GROUP WHERE ROWNUM = 1"
df = pd.read_sql(sql, conn)
print(df.columns.tolist())
