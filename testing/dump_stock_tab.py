import sys
import os
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from reports_config import TABS

for tab in TABS:
    if tab.get('id') == 'stock':
        print(json.dumps(tab.get('reports', []), ensure_ascii=False, indent=2))
