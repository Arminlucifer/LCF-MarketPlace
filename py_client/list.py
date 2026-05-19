import requests

endpoint = "http://127.0.0.1:8000/api/products/"

respone = requests.get(endpoint)
payload = {'min_price': 200}

try:
    respone = requests.get(endpoint, params=payload)
    print("Status Code:", respone.status_code)
    print("Data:", respone.json())
except requests.exceptions.ConnectionError:
    print("Connection Error!")
