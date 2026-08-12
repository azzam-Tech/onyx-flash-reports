import sys

db_code = """
class InterceptCursor:
    def __init__(self, cur):
        self._cur = cur

    def execute(self, statement, parameters=None, **keyword_parameters):
        import sys
        if 'flask' in sys.modules:
            try:
                from flask import g
                target_year = getattr(g, 'target_year', None)
                if target_year and str(target_year).isdigit() and len(str(target_year)) == 4:
                    statement = statement.replace("IAS20261", f"IAS{target_year}1")
                    statement = statement.replace("ias20261", f"ias{target_year}1")
            except Exception:
                pass
        if parameters is not None:
            return self._cur.execute(statement, parameters, **keyword_parameters)
        return self._cur.execute(statement, **keyword_parameters)

    def __getattr__(self, name):
        return getattr(self._cur, name)

    def __iter__(self):
        return iter(self._cur)

class InterceptConnection:
    def __init__(self, conn):
        self._conn = conn

    def cursor(self):
        return InterceptCursor(self._conn.cursor())

    def __getattr__(self, name):
        return getattr(self._conn, name)

    def __enter__(self):
        self._conn.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._conn.__exit__(exc_type, exc_val, exc_tb)

def get_conn():
    return InterceptConnection(oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN))
"""

db_path = 'privet/onyx_reports/database.py'
with open(db_path, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace("""def get_conn():
    return oracledb.connect(user=DB_USER, password=DB_PASSWORD, dsn=DB_DSN)""", db_code)

with open(db_path, 'w', encoding='utf-8') as f:
    f.write(c)

app_code = """
@app.before_request
def set_target_year():
    from flask import request, g
    year_val = request.args.get('year_val')
    date_to = request.args.get('date_to')
    date_from = request.args.get('date_from')
    
    target_year = "2026"
    if year_val and len(year_val) == 4:
        target_year = year_val
    elif date_from and len(date_from) >= 4:
        target_year = date_from[:4]
    elif date_to and len(date_to) >= 4:
        target_year = date_to[:4]
        
    g.target_year = target_year
"""

app_path = 'privet/onyx_reports/app.py'
with open(app_path, 'r', encoding='utf-8') as f:
    c_app = f.read()

c_app = c_app.replace("app = Flask(__name__)\n", "app = Flask(__name__)\n" + app_code)

with open(app_path, 'w', encoding='utf-8') as f:
    f.write(c_app)

print("Patch applied to database.py and app.py!")
