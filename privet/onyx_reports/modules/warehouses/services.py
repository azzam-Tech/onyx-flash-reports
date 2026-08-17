# -*- coding: utf-8 -*-
from collections import defaultdict
from .repository import get_main_wh_movement_data, get_warehouse_names, MAIN_WAREHOUSES_CODES
from report_handlers import run_sql_report

def process_main_wh_movement(rpt, args):
    date_from_str = args.get('date_from', '2026-01-01')
    date_to_str = args.get('date_to', '2026-12-31')
    i_code_str = args.get('i_code', '').split(' - ')[0].strip()
    
    print(f'[DEBUG WH] date_from: {date_from_str}, date_to: {date_to_str}, i_code: {i_code_str}')
    
    wh_mapping = get_warehouse_names()
    results = get_main_wh_movement_data(date_from_str, date_to_str, i_code_str)
    
    print(f'[DEBUG WH] Query returned {len(results)} raw grouped rows.')
    
    items = defaultdict(lambda: {'name': '', 'total': 0.0, 'wh': defaultdict(float)})
    for i_code, i_name, w_code, net_qty in results:
        code_str = str(w_code)
        items[str(i_code)]['name'] = str(i_name)
        items[str(i_code)]['total'] += float(net_qty)
        items[str(i_code)]['wh'][code_str] += float(net_qty)
        
    cols = ['رقم الصنف', 'اسم الصنف', 'الإجمالي'] + [wh_mapping.get(c, c) for c in MAIN_WAREHOUSES_CODES]
    rows = []
    
    for code, data in items.items():
        row = [code, data['name'], f"{data['total']:,.2f}"]
        for w_code in MAIN_WAREHOUSES_CODES:
            row.append(f"{data['wh'][w_code]:,.2f}")
        rows.append(tuple(row))
        
    # Sort by total descending
    rows.sort(key=lambda x: float(x[2].replace(',', '')), reverse=True)
    
    return cols, rows

from . import repository

def handle_warehouse_report(report_id, rpt, args):
    if report_id == 'main_wh_movement':
        return process_main_wh_movement(rpt, args)
    
    # Override SQL from our new repository
    repo_func_name = f"get_{report_id}_sql"
    if hasattr(repository, repo_func_name):
        rpt['sql'] = getattr(repository, repo_func_name)()
    
    if rpt.get('sql'):
        return run_sql_report(rpt, args)
        
    return [], []
