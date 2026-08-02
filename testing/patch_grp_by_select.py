with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

old_opt = '{"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["period","الفترات الزمنية"]]}'
new_opt = '{"name":"grp_by","label":"تجميع حسب","type":"select","default":"cc","options":[["cc","مراكز التكلفة"],["rep","المناديب"],["customer","العملاء"],["period","الفترات الزمنية"]]}'

if old_opt in content:
    content = content.replace(old_opt, new_opt)
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated grp_by dropdown option in TABS!")
else:
    print("Error: Could not find old_opt in app.py")
