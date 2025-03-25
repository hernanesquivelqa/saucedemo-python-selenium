import requests

update_data = {
    "title": "Título actualizado",
    "body": "Este es el contenido modificado",
    "userId": 1,
}

response = requests.put("https://jsonplaceholder.typicode.com/posts/1", json=update_data)
print(response.status_code)
print(response.json())
