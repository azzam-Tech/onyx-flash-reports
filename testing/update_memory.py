with open("AI_MEMORY.md", "r", encoding="utf-8") as f:
    content = f.read()

target = "### 📈 قسم المبيعات وأداء المناديب\n"
new_entry = "### 📈 قسم المبيعات وأداء المناديب\n- **تقرير حركة المديونية والتحصيل الدوري (`debt_movement_summary`):** تم بناء تقرير حركة وتغيرات أرصدة المديونية بحسب فترات التقرير (افتتاحي + مبيعات شامل الضريبة - تحصيل = مديونية نهائية). يشتمل على الأعمدة الخمسة المطلوبة: المديونية الافتتاحية، صافي المبيعات شامل الضريبة (15%)، إجمالي التحصيل المعتمد، المديونية النهائية، والهدف (فارغ).\n"

if target in content and "debt_movement_summary" not in content:
    content = content.replace(target, new_entry)
    with open("AI_MEMORY.md", "w", encoding="utf-8") as f:
        f.write(content)
    print("AI_MEMORY.md updated")
else:
    print("Already updated or target missing")
