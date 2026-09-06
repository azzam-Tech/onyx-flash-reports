import re
with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\app\templates\item_prices.html', 'r', encoding='utf-8') as f:
    content = f.read()

main_start = content.find('<!-- Search & Filter Bar -->')
footer_start = content.find('<!-- Footer -->')
scripts_start = content.find('<script>')
scripts_end = content.find('</body>')

main_html = content[main_start:footer_start]

# We need to drop the tailwind config from scripts because it's already in base.html
scripts_part = content[scripts_start:scripts_end]
scripts_part = re.sub(r'<script>\s*tailwind\.config\s*=\s*{.*?}\s*</script>', '', scripts_part, flags=re.DOTALL)

new_content = """{% extends "base.html" %}
{% block title %}{{ t('prices_title') }}{% endblock %}

{% block extra_css %}
<style>
    .table-container::-webkit-scrollbar { height: 8px; width: 8px; }
    .table-container::-webkit-scrollbar-track { background: #f1f5f9; border-radius: 4px; }
    .table-container::-webkit-scrollbar-thumb { background: #cbd5e1; border-radius: 4px; }
    .table-container::-webkit-scrollbar-thumb:hover { background: #94a3b8; }
</style>
{% endblock %}

{% block content %}
<div class="mb-6 flex justify-between items-center">
    <div>
        <h1 class="text-2xl font-bold text-gray-900">{{ t('prices_title') }}</h1>
        <p class="text-gray-500 mt-1">{{ t('salesman_label') }} {{ current_user.name }}</p>
    </div>
</div>

""" + main_html + """
{% endblock %}

{% block scripts %}
""" + scripts_part + """
{% endblock %}
"""

with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\zatca_printer\app\templates\item_prices.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
print('Updated item_prices.html')
