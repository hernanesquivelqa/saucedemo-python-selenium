import requests
response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
print(response.status_code)  # Código de estado HTTP
print(response.json())  # Respuesta en formato JSON
