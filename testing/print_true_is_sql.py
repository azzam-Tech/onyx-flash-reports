import sys
import os

sys.path.append(os.path.abspath('privet/onyx_reports'))
from reports_config import TABS

for tab in TABS:
    for rep in tab.get('reports', []):
        if rep.get('id') == 'true_income_statement':
            print("Found true_income_statement")
            if 'sql' in rep:
                print(rep['sql'])
            else:
                print("No SQL attribute directly, might be using a handler")
            if 'handler' in rep:
                print("Handler:", rep['handler'])
