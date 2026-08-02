import os

text = """
### تحديثات 30 يوليو 2026 (معادلات الداشبورد المتقدمة)
- **مردودات المبيعات:** لا تحفظ في جدول الفواتير الرئيسي، بل لها جدول مستقل تماماً `IAS_RT_BILL_MST` وتفاصيل في `IAS_RT_BILL_DTL`. للحصول على الصافي يجب دائماً طرحها من المبيعات.
- **الخصومات الإضافية:** لمعرفة الخصم الدقيق بما فيه `ADD_DISC_AMT_DTL` يجب حساب: `BILL_AMT - DISC_AMT + ADD_DISC_AMT_MST`.
- **إشعار الخصم المستقل:** يسجل في `IAS_POST_DTL` تحت `DOC_TYPE=15`.
- **التحصيل الشامل (Collection):** لا يقتصر على سندات القبض (`DOC_TYPE=2`) بل يشمل أيضاً: المبيعات النقدية (`DOC_TYPE=4` بحسابات 111)، قيود اليومية (`DOC_TYPE=1, JV_TYPE=2`)، مطروحاً منها المردودات النقدية (`DOC_TYPE=5` بحسابات 111). تم اعتماد هذا المعيار رسمياً في الداشبورد.
"""

with open(r'c:\Users\amarn\OneDrive\Desktop\dbOnyxOnAntigravity\AI_MEMORY.md', 'a', encoding='utf-8') as f:
    f.write(text)
