import sys
import os
import json

sys.path.append(os.path.abspath('privet/onyx_reports'))
from reports_config import TABS

for tab in TABS:
    print(f"Tab ID: {tab.get('id')}")
    for rep in tab.get('reports', []):
        print(f"  Report ID: {rep.get('id')}")
