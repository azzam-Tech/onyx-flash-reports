import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../privet/onyx_reports')))
from reports_config import TABS

for tab in TABS:
    print(f"Tab ID: {tab.get('id')}, Title: {tab.get('title')}")
