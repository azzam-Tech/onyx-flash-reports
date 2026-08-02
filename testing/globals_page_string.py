GLOBALS_PAGE = """<!doctype html><html lang="ar" dir="rtl"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1"><title>المتغيرات العامة</title>""" + STYLE + """
<style>
.tgt-table { width:100%; border-collapse:collapse; font-size:13px; }
.tgt-table th, .tgt-table td { border:1px solid #e2e8f0; padding:6px; text-align:center; }
.tgt-table th { background:#f8fafc; font-weight:700; color:#475569; position:sticky; top:0; }
.tgt-input { width:100%; min-width:70px; padding:4px; border:1px solid #cbd5e1; border-radius:4px; text-align:center; }
</style>
</head><body>
<div class="app"><div class="main">
 <div class="wrap">
   <a class="back" href="/" style="color:#4f46e5;font-weight:700;display:inline-block;margin-bottom:16px">&#8594; العودة للرئيسية</a>
   <div class="rhead">
     <h1>المتغيرات العامة (التارجت)</h1>
     {% if saved %}<div style="color:#10b981;font-weight:bold;margin-top:10px">تم الحفظ بنجاح!</div>{% endif %}
   </div>
   <form method="post" action="/globals">
     <div style="overflow-x:auto; max-height: 70vh; margin-bottom: 20px; border-radius: 8px; border: 1px solid #e2e8f0">
       <table class="tgt-table">
         <thead>
           <tr>
             <th style="min-width:150px">اسم المندوب</th>
             {% for m in range(1, 13) %}
             <th>شهر {{m}}</th>
             {% endfor %}
           </tr>
         </thead>
         <tbody>
           {% for rep in reps %}
           <tr>
             <td style="text-align:right">{{ rep.name }}</td>
             {% for m in range(1, 13) %}
             <td>
               <input type="number" class="tgt-input" 
                      name="target_{{rep.code}}_{{m}}" 
                      value="{{ targets.get(rep.code|string, {}).get(m|string, 1000000) }}">
             </td>
             {% endfor %}
           </tr>
           {% endfor %}
         </tbody>
       </table>
     </div>
     <button type="submit" style="background:#4f46e5;color:#fff;border:0;padding:12px 24px;border-radius:9px;font-weight:700;font-size:15px;cursor:pointer">حفظ المتغيرات</button>
   </form>
 </div>
</div></div></body></html>"""
