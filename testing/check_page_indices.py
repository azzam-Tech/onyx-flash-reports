with open(r'testing\app_rebuild4.py', 'r', encoding='utf-8') as f:
    text = f.read()

idx_tp = text.find('TARGETS_PAGE')
idx_p = text.find('PAGE =')
print("TARGETS_PAGE at:", idx_tp)
print("PAGE at:", idx_p)
