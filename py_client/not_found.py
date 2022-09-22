import requests


endpoint = "http://localhost:8000/api/product/269768978784786897/" #GET


get_response = requests.get(endpoint)
print(get_response.json())
# print(get_response.status_code)