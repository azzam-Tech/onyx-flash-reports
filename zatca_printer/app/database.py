import os
import oracledb

# We rely on load_dotenv() from run.py to load the .env file.

DB_USER     = os.environ.get("ORA_USER")
DB_PASSWORD = os.environ.get("ORA_PASSWORD")
DB_DSN      = os.environ.get("ORA_DSN")
_lib        = os.environ.get("ORA_LIB_DIR")

try:
    if _lib:
        oracledb.init_oracle_client(lib_dir=_lib)
    else:
        try:
            # 1. التجربة الأولى: مسار الأوراكل الثابت في جهازك الحالي
            oracledb.init_oracle_client(lib_dir=r"C:\oracle\instantclient\instantclient_23_0")
        except Exception:
            # 2. التجربة الثانية: الاعتماد على بيئة الويندوز (هذا ما يعمل في الجهاز الآخر!)
            oracledb.init_oracle_client()
    print("Thick mode ON")
except Exception as e:
    print("thick warn:", e)


class InterceptCursor:
    def __init__(self, cur):
        self._cur = cur

    def execute(self, statement, parameters=None, **keyword_parameters):
        if parameters is not None:
            return self._cur.execute(statement, parameters, **keyword_parameters)
        return self._cur.execute(statement, **keyword_parameters)

    def __getattr__(self, name):
        return getattr(self._cur, name)

    def __iter__(self):
        return iter(self._cur)


    def __enter__(self):
        self._cur.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._cur.__exit__(exc_type, exc_val, exc_tb)

class InterceptConnection:

    def __init__(self, conn):
        self._conn = conn

    def cursor(self):
        cur = self._conn.cursor()
        import sys
        target_schema = os.environ.get("DEFAULT_SCHEMA", "IAS20261")
        if 'flask' in sys.modules:
            try:
                from flask import g
                target_year = getattr(g, 'target_year', None)
                if target_year and str(target_year).isdigit() and len(str(target_year)) == 4:
                    target_schema = f"IAS{target_year}1"
            except Exception:
                pass
        
        current_conn_schema = getattr(self._conn, '_current_schema', None)
        if current_conn_schema != target_schema:
            try:
                cur.execute(f"ALTER SESSION SET CURRENT_SCHEMA = {target_schema}")
                self._conn._current_schema = target_schema
            except Exception as e:
                print("Alter session warning:", e)
            
        return InterceptCursor(cur)

    def __getattr__(self, name):
        return getattr(self._conn, name)

    def __enter__(self):
        self._conn.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._conn.__exit__(exc_type, exc_val, exc_tb)

def get_conn(readonly=True):
    """
    Unified database connection.
    - readonly=True (default): uses ORA_USER (e.g. RPT_USER) for safe reporting.
    - readonly=False: uses ORA_WRITE_USER (e.g. ULT) for authorized INSERT/UPDATE operations.
    """
    if readonly:
        user = DB_USER
        password = DB_PASSWORD
    else:
        user = os.environ.get("ORA_WRITE_USER")
        password = os.environ.get("ORA_WRITE_PASSWORD")
        if not user or not password:
            raise ValueError("ORA_WRITE_USER and ORA_WRITE_PASSWORD must be defined in the .env file for write operations.")
        
    return InterceptConnection(oracledb.connect(user=user, password=password, dsn=DB_DSN))

_pool = None

def get_pooled_conn():
    global _pool
    if _pool is None:
        _pool = oracledb.create_pool(
            user=DB_USER, 
            password=DB_PASSWORD, 
            dsn=DB_DSN, 
            min=2, 
            max=20, 
            increment=2
        )
    return InterceptConnection(_pool.acquire())

