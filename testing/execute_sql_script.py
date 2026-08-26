import os
import sys

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'privet', 'onyx_reports'))
from database import DB_DSN, InterceptConnection
import oracledb

def execute_script():
    sql_path = os.path.join(os.path.dirname(__file__), '..', 'migration_plan', 'update_group_005_final.sql')
    
    with open(sql_path, 'r', encoding='utf-8') as f:
        sql_content = f.read()
        
    statements = [s.strip() for s in sql_content.split(';') if s.strip()]
    
    print("Connecting to DB as ULT...")
    conn = InterceptConnection(oracledb.connect(user='ULT', password='ULT2017', dsn=DB_DSN))
    
    with conn as con:
        with con.cursor() as cur:
            updates = 0
            for stmt in statements:
                # ignore comments and commit
                if stmt.startswith('--'):
                    # if there are multiple lines of comments, filter them out
                    lines = [l for l in stmt.split('\n') if not l.strip().startswith('--')]
                    stmt = '\n'.join(lines).strip()
                    if not stmt:
                        continue
                        
                if stmt.upper() == 'COMMIT':
                    con.commit()
                    print("COMMIT executed.")
                    continue
                    
                if stmt.upper().startswith("UPDATE"):
                    try:
                        cur.execute(stmt)
                        updates += cur.rowcount
                    except Exception as e:
                        print(f"Error executing statement: {stmt}\nError: {e}")
            
            print(f"Total rows updated/deactivated successfully: {updates}")

if __name__ == '__main__':
    execute_script()
