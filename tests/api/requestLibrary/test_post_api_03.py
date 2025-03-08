import requests

data = {
    "title": "Posting Data",
    "body": "Esto es una prueba de API con Python",
    "userId": 1,
}

response = requests.post("https://jsonplaceholder.typicode.com/posts", json=data)
print(response.status_code)
print(response.json())
