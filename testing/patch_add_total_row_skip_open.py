with open(r"privet\onyx_reports\app.py", "r", encoding="utf-8") as f:
    content = f.read()

old_loop = """    for row in rows:
        for col_idx in range(len(cols)):
            if is_numeric[col_idx]:"""

new_loop = """    for row in rows:
        # إذا كان الصف هو سطر الرصيد الافتتاحي (رصيد ما قبل الفترة)، يُستبعد من إجمالي حركة الفترة (مدين/دائن)
        if row and len(row) > 1 and str(row[1]).strip() == "رصيد افتتاحي":
            continue
        for col_idx in range(len(cols)):
            if is_numeric[col_idx]:"""

if old_loop in content:
    content = content.replace(old_loop, new_loop)
    with open(r"privet\onyx_reports\app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully updated add_total_row to skip opening balance row!")
else:
    print("Error: Could not find old_loop in app.py")
