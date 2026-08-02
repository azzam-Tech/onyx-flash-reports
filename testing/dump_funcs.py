import codecs

with codecs.open(r"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\privet\onyx_reports\app.py", 'r', 'utf-8') as f:
    content = f.read()

# I need to modify the queries for `collect` or `rcpt` in `run_perf_aging_fifo` and `run_perf_aging_analytical`.
# Let's dump these two functions to a clean text file so I can read them and know exactly what to replace.
import ast
tree = ast.parse(content)
for node in tree.body:
    if isinstance(node, ast.FunctionDef) and node.name in ['run_perf_aging_fifo', 'run_perf_aging_analytical']:
        with codecs.open(rf"C:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\testing\{node.name}.py", 'w', 'utf-8') as out:
            out.write(ast.get_source_segment(content, node))
