import sys

db_path = 'privet/onyx_reports/database.py'
with open(db_path, 'r', encoding='utf-8') as f:
    c = f.read()

fix_methods = """
    def __enter__(self):
        self._cur.__enter__()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return self._cur.__exit__(exc_type, exc_val, exc_tb)

class InterceptConnection:
"""

c = c.replace("class InterceptConnection:", fix_methods)

with open(db_path, 'w', encoding='utf-8') as f:
    f.write(c)

print("Added context manager methods to InterceptCursor")
