import requests

endpoint = "http://127.0.0.1:8000/api/products/"


try:
    respone = requests.get(endpoint)
    print("Status Code:", respone.status_code)
    print(respone.json())
except requests.exceptions.ConnectionError:
    print("Connection Error!")
