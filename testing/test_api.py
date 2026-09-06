import urllib.request
import urllib.error
import json

def test_api():
    req = urllib.request.Request('http://127.0.0.1:8080/api/visits/start', method='POST')
    req.add_header('Content-Type', 'application/json')
    data = json.dumps({'c_code': '1113'}).encode('utf-8')
    try:
        with urllib.request.urlopen(req, data=data) as response:
            print("Status Code:", response.getcode())
            print("Response Text:", response.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print("HTTP Error:", e.code)
        print("Response Text:", e.read().decode('utf-8'))
    except Exception as e:
        print("Exception:", e)

if __name__ == "__main__":
    test_api()
