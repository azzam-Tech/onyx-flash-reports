import urllib.request
import json

try:
    with urllib.request.urlopen('http://127.0.0.1:8080/api/invoice/2614200219') as response:
        data = json.loads(response.read().decode())
        print("Status: 200")
        print("Bill No:", data.get('invoice_no'))
        print("Items count:", len(data.get('items', [])))
        for i, itm in enumerate(data.get('items', [])[:3]):
            print(f"Item {i+1}:", itm)
except Exception as e:
    print("Error:", e)
