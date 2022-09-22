import requests

# endpoint = "https://httpbin.org/status/200/"
# endpoint = "http://localhost:8000/api/" #GET
endpoint = "http://localhost:8000/api/products/" #POST

# get_response = requests.get(endpoint, params={"productid": 123}, json={"query": "Hello World!"}) # API Method
get_response = requests.post(endpoint, json={"title": "Hello World!?"})
print(get_response.json())
# print(get_response.status_code)