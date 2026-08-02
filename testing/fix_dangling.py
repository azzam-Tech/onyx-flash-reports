with open(r'privet\onyx_reports\app.py', 'r', encoding='utf-8') as f:
    text = f.read()

dangling = """    except Exception as e:
        return jsonify({"success": False, "error": str(e)})"""

if dangling in text:
    text = text.replace(dangling, '')
    with open(r'privet\onyx_reports\app.py', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Dangling except block removed!")
else:
    print("Not found")
