import requests


endpoint = "http://localhost:8000/api/product/" #POST

data = {
    "title": "This field is done",
    "price": 33.99
}

get_response = requests.post(endpoint, json=data)
print(get_response.json())
# print(get_response.status_code)