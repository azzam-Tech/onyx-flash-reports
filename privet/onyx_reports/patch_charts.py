# -*- coding: utf-8 -*-
import re

with open('app.py', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove duplicated dashboard icon
old_dash_link = '''<a href="/dashboard" class="{{ 'on' if request.path == '/dashboard' else '' }}"><svg viewBox="0 0 24 24"><path d="M3 13h8V3H3zM13 21h8V3h-8zM3 21h8v-6H3z"/></svg><span>لوحة القيادة</span></a>'''
if old_dash_link in text:
    text = text.replace(old_dash_link, '')

# 2. Upgrade the charts to look premium
old_script = '''     <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ if(!window.Chart) return; Chart.defaults.font.family="Tahoma";
       new Chart(document.getElementById("c1"),{type:"bar",data:{labels:D.months,datasets:[{label:"مبيعات",data:D.msales,backgroundColor:"#3b82f6",borderRadius:6},{label:"تحصيل",data:D.mcollect,backgroundColor:"#22c55e",borderRadius:6}]}});
       new Chart(document.getElementById("c2"),{type:"bar",data:{labels:D.rep_labels,datasets:[{data:D.rep_vals,backgroundColor:"#14867a",borderRadius:6}]},options:{indexAxis:"y",plugins:{legend:{display:false}}}});
       new Chart(document.getElementById("c3"),{type:"bar",data:{labels:D.itm_labels,datasets:[{data:D.itm_vals,backgroundColor:"#f97316",borderRadius:6}]},options:{indexAxis:"y",plugins:{legend:{display:false}}}});
       new Chart(document.getElementById("c4"),{type:"line",data:{labels:D.months,datasets:[{data:D.mpurch,borderColor:"#f97316",backgroundColor:"rgba(249,115,22,.12)",fill:true,tension:.35}]},options:{plugins:{legend:{display:false}}}});
     });
     </script>'''

new_script = '''     <script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
     <script>
     var D={{ dash|tojson }};
     window.addEventListener("load",function(){ 
       if(!window.Chart) return; 
       Chart.defaults.font.family = "'Cairo', 'Inter', sans-serif";
       Chart.defaults.color = "#64748b";
       
       const commonOptions = {
         responsive: true,
         maintainAspectRatio: false,
         plugins: {
           legend: { display: false },
           tooltip: {
             backgroundColor: '#1e293b',
             padding: 14,
             titleFont: { size: 14, family: "'Cairo', sans-serif", weight: 'bold' },
             bodyFont: { size: 14, family: "'Cairo', sans-serif" },
             cornerRadius: 10,
             displayColors: true,
             boxPadding: 6
           }
         },
         scales: {
           x: { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' } } },
           y: { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } }
         }
       };

       const horizontalOptions = JSON.parse(JSON.stringify(commonOptions));
       horizontalOptions.indexAxis = "y";
       horizontalOptions.scales.x = { grid: { color: '#f1f5f9', borderDash: [6, 4] }, border: { display: false }, ticks: { font: { weight: '600' } } };
       horizontalOptions.scales.y = { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600' }, padding: 10 } };
       
       // C1: Bar Chart (Sales & Collection)
       new Chart(document.getElementById("c1"),{
         type:"bar",
         data:{
           labels:D.months,
           datasets:[
             {label:"مبيعات", data:D.msales, backgroundColor:"#4f46e5", borderRadius:8, maxBarThickness: 32, borderSkipped: false},
             {label:"تحصيل", data:D.mcollect, backgroundColor:"#38bdf8", borderRadius:8, maxBarThickness: 32, borderSkipped: false}
           ]
         },
         options: {
           ...commonOptions,
           plugins: {
             ...commonOptions.plugins,
             legend: { display: true, position: 'top', align: 'end', labels: { usePointStyle: true, boxWidth: 10, padding: 20, font: { family: "'Cairo'", size: 13, weight: 'bold' } } }
           }
         }
       });

       // C2: Horizontal Bar (Salesmen)
       new Chart(document.getElementById("c2"),{
         type:"bar",
         data:{
           labels:D.rep_labels,
           datasets:[{label: "مبيعات", data:D.rep_vals, backgroundColor:"#8b5cf6", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C3: Horizontal Bar (Items)
       new Chart(document.getElementById("c3"),{
         type:"bar",
         data:{
           labels:D.itm_labels,
           datasets:[{label: "مبيعات", data:D.itm_vals, backgroundColor:"#10b981", borderRadius:8, maxBarThickness: 24, borderSkipped: false}]
         },
         options: horizontalOptions
       });

       // C4: Line Chart (Purchases)
       const ctx4 = document.getElementById("c4").getContext('2d');
       const grad4 = ctx4.createLinearGradient(0, 0, 0, 300);
       grad4.addColorStop(0, 'rgba(249, 115, 22, 0.4)');
       grad4.addColorStop(1, 'rgba(249, 115, 22, 0.0)');
       
       new Chart(ctx4,{
         type:"line",
         data:{
           labels:D.months,
           datasets:[{
             label: "مشتريات",
             data:D.mpurch,
             borderColor:"#f97316",
             borderWidth: 3,
             backgroundColor: grad4,
             fill:true,
             tension:0.4,
             pointRadius: 0,
             pointHoverRadius: 6,
             pointBackgroundColor: "#fff",
             pointBorderColor: "#f97316",
             pointBorderWidth: 2
           }]
         },
         options: {
           ...commonOptions,
           interaction: { mode: 'index', intersect: false }
         }
       });
     });
     </script>'''

if old_script in text:
    text = text.replace(old_script, new_script)
else:
    # Use regex if spacing differs
    text = re.sub(r'<script src="https://cdnjs\.cloudflare\.com.*?</script>', new_script, text, flags=re.DOTALL)

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(text)

print("Charts patched and duplicate icon removed!")
