import oracledb
import pandas as pd

def main():
    try:
        oracledb.init_oracle_client(lib_dir=r'C:\oracle\instantclient\instantclient_23_0')
    except:
        pass
    conn = oracledb.connect(user='RPT_USER', password='ULT2016', dsn='100.100.1.100:1521/ORCL')
    sql = "SELECT COLUMN_NAME FROM ALL_TAB_COLUMNS WHERE TABLE_NAME='IAS_POST_DTL' AND OWNER='IAS20261'"
    df = pd.read_sql(sql, conn)
    print(df['COLUMN_NAME'].tolist()[:50])

if __name__ == '__main__':
    main()
