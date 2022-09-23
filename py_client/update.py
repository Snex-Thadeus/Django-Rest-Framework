import requests


endpoint = "http://localhost:8000/api/product/1/update/" #PUT

data = {
    "title": "Hello world my good friend",
    "price": 14.87
}

get_response = requests.put(endpoint, json=data)
print(get_response.json())
# print(get_response.status_code)