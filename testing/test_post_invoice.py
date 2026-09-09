import urllib.request
import urllib.error
import json

payload = {
    "c_code": "2390",
    "pay_way": "credit",
    "bill_remark": "Test API Invoice",
    "ref_no": "WEB-TEST-001",
    "items": [
        {
            "i_code": "KMCT-55S4K",
            "qty": 2,
            "price": 10.0,
            "itm_unt": 1
        }
    ]
}

data = json.dumps(payload).encode('utf-8')
req = urllib.request.Request('http://127.0.0.1:8080/api/invoice', data=data, headers={'Content-Type': 'application/json'})

try:
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode())
        print("Success:", json.dumps(result, indent=2, ensure_ascii=False))
except urllib.error.HTTPError as e:
    error_body = e.read().decode()
    print(f"HTTP Error {e.code}:", error_body)
except Exception as e:
    print("Error:", e)
