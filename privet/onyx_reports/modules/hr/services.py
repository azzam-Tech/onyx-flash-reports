# -*- coding: utf-8 -*-
from database import get_conn
from . import repository
from report_handlers import run_sql_report

def handle_hr_report(report_id, rpt, args):
    repo_func_name = f"get_{report_id}_sql"
    if hasattr(repository, repo_func_name):
        rpt['sql'] = getattr(repository, repo_func_name)()
        
    if rpt.get('sql'):
        return run_sql_report(rpt, args)
        
    return [], []
