import re

with open('privet/onyx_reports/routes/dashboard.py', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Remove sales, sales_ret, collect from sqls
content = re.sub(r'^\s*"sales":\s*".*?",\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*"sales_ret":\s*".*?",\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*"collect":\s*".*?",\n', '', content, flags=re.MULTILINE)

# 2. Remove ms, ms_ret, mc from sqls
content = re.sub(r'^\s*"ms":\s*".*?",\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*"ms_ret":\s*".*?",\n', '', content, flags=re.MULTILINE)
content = re.sub(r'^\s*"mc":\s*".*?",\n', '', content, flags=re.MULTILINE)

# 3. Update the keys in the if statement
content = content.replace(
    'if key in ["sales", "sales_ret", "collect", "purch", "gross", "gross_ret", "netprofit", "invval", "ov", "ov_ret", "iv"]:',
    'if key in ["purch", "gross", "gross_ret", "netprofit", "invval", "ov", "ov_ret", "iv"]:'
)

content = content.replace(
    'results[key] = (0.0 if key not in ["ms", "ms_ret", "mc", "mp", "rs", "rs_ret", "its", "its_ret"] else {})',
    'results[key] = (0.0 if key not in ["mp", "rs", "rs_ret", "its", "its_ret"] else {})'
)

# 4. Replace the logic block for sales and ms/mc calculations
old_logic = """
        sales = results["sales"]; sales_ret = results["sales_ret"]
        d["sales"] = round(sales - sales_ret, 2)
        d["collect"] = results["collect"]
        d["purch"] = results["purch"]
        d["gross"] = round(results["gross"] - results["gross_ret"], 2)
        d["netprofit"] = results["netprofit"]
        d["recv"] = results["recv"]
        d["invval"] = results["invval"]
        d["vat"] = round((results["ov"] - results["ov_ret"]) - results["iv"], 2)
        
        ms = results["ms"]; ms_ret = results["ms_ret"]
        mc = results["mc"]; mp = results["mp"]
        
        months=sorted(set(list(ms)+list(ms_ret)+list(mc)+list(mp)))
        d["months"]=months
        d["msales"]=[round(ms.get(x,0) - ms_ret.get(x,0), 2) for x in months]
        d["mcollect"]=[mc.get(x,0) for x in months]
        d["mpurch"]=[mp.get(x,0) for x in months]
"""

new_logic = """
        try:
            from modules.sales.services import run_debt_movement_summary
            args = {
                'date_from': f,
                'date_to': t,
                'grp_by': 'period',
                'period_type': 'monthly',
                'period_val': 'all'
            }
            # row: [period, desc, open_bal, net_sales_vat, collect, diff, ratio, close_bal, ...]
            _, rows = run_debt_movement_summary({}, args)
            
            d["sales"] = round(sum(float(str(r[3]).replace(',','')) for r in rows), 2)
            d["collect"] = round(sum(float(str(r[4]).replace(',','')) for r in rows), 2)
            
            ms_dict = {str(r[0]): float(str(r[3]).replace(',','')) for r in rows}
            mc_dict = {str(r[0]): float(str(r[4]).replace(',','')) for r in rows}
        except Exception as e:
            import logging
            logging.getLogger(__name__).error("debt_movement_summary Exception:", exc_info=True)
            d["sales"] = 0.0
            d["collect"] = 0.0
            ms_dict = {}
            mc_dict = {}

        d["purch"] = results["purch"]
        d["gross"] = round(results["gross"] - results["gross_ret"], 2)
        d["netprofit"] = results["netprofit"]
        d["recv"] = results.get("recv", 0.0)
        d["invval"] = results["invval"]
        d["vat"] = round((results["ov"] - results["ov_ret"]) - results["iv"], 2)
        
        mp = results.get("mp", {})
        months = sorted(set(list(ms_dict.keys()) + list(mc_dict.keys()) + list(mp.keys())))
        d["months"] = months
        d["msales"] = [ms_dict.get(x, 0.0) for x in months]
        d["mcollect"] = [mc_dict.get(x, 0.0) for x in months]
        d["mpurch"] = [mp.get(x, 0.0) for x in months]
"""

content = content.replace(old_logic.strip(), new_logic.strip())

with open('privet/onyx_reports/routes/dashboard.py', 'w', encoding='utf-8') as file:
    file.write(content)

print("Patch script executed successfully.")
