import re

file_path = r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\app\templates\invoice.html'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Fix .panel
old_panel = """        .panel {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
            border: 1px solid var(--border);
        }"""
new_panel = """        .panel {
            background: var(--card-bg);
            border-radius: 16px;
            padding: 1.5rem;
            box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
            border: 1px solid var(--border);
            min-width: 0; /* Fix grid overflow */
            overflow: hidden;
        }"""
content = content.replace(old_panel, new_panel)

# Fix .cart-table-wrapper
old_wrapper = """        .cart-table-wrapper {
            overflow-x: auto;
            margin-bottom: 1.5rem;
        }"""
new_wrapper = """        .cart-table-wrapper {
            overflow-x: auto;
            margin-bottom: 1.5rem;
            width: 100%;
            -webkit-overflow-scrolling: touch; /* Smooth scroll on mobile */
        }"""
content = content.replace(old_wrapper, new_wrapper)

# Fix .modal-overlay
old_modal = """        .modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(4px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 50;
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }"""
new_modal = """        .modal-overlay {
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            width: 100%; height: 100%;
            background: rgba(15, 23, 42, 0.6);
            backdrop-filter: blur(4px);
            display: flex;
            justify-content: center;
            align-items: center;
            z-index: 9999; /* ensure top */
            opacity: 0;
            visibility: hidden;
            transition: all 0.3s ease;
        }"""
content = content.replace(old_modal, new_modal)


# Also ensure main-container has min-width: 0 on children if needed, but the panel fix should be enough.

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("CSS patched")
