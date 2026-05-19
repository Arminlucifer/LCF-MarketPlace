import requests

endpoint = "http://127.0.0.1:8000/api/products/"


TOKEN = "34fc6514215c5a6aafa92a1ab4cee08710509b9b"
headers = {'Authorization': f'Bearer {TOKEN}'}

try:
    respone = requests.get(endpoint, headers=headers)
    print("Status Code:", respone.status_code)
    print(respone.json())
except requests.exceptions.ConnectionError:
    print("Connection Error!")
