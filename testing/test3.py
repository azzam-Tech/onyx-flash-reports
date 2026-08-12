import sys
with open('privet/onyx_reports/reports_config.py', 'r', encoding='utf-8') as f:
    c = f.read()

idx2 = c.find('"smart_replenishment"')
print('--- smart_replenishment ---')
print(c[idx2:idx2+1000])

idx3 = c.find('"dead_stock_value"')
print('--- dead_stock_value ---')
print(c[idx3:idx3+1000])
