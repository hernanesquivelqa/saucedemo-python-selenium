import json
import random
import requests
from tests.api.file import save_json_to_file
from config import USERNAME_DEMOQA, PASSWORD_DEMOQA, USER_ID_DEMOQA, BEARER_DEMOQA


class Api:
    def __init__(self):
        self.base_url = "https://demoqa.com"
        self.api = requests
        self.endpoints = {
            "create_user": "/Account/v1/User",
            "authorized": "/Account/v1/Authorized",
            "generate_token": "/Account/v1/GenerateToken",
            "get_books": "/BookStore/v1/Books",
            "add_list_to_books": "/BookStore/v1/Books",
            "delete_book_of_the_list": "/BookStore/v1/Book",
            "login": "/Account/v1/Login",
            "user": "/Account/v1/User/{username}",
            "update_user": "/Account/v1/User/{username}",
        }
        self.access_token = None
        self.isbn_count = None

    def save_response_json(self, data: object, file_name: str):
        save_json_to_file(json_data=data, dir_path="integration/res", file_name=file_name)

    def create_new_user(self, username: str, password: str):
        url = self.base_url + self.endpoints["create_user"]
        request_data = {"userName": username, "password": password}
        response = self.api.post(url, json=request_data)
        # assert response.status_code == 201
        body: object = response.json()
        return body, response

    def authorized(self):
        url = self.base_url + self.endpoints["authorized"]
        request_data = {"userName": USERNAME_DEMOQA, "password": PASSWORD_DEMOQA}
        response = self.api.post(url, json=request_data)
        body: object = response.json()
        return body, response

    def set_access_token(self):
        url = self.base_url + self.endpoints["generate_token"]
        request_data = {"userName": USERNAME_DEMOQA, "password": PASSWORD_DEMOQA}
        response = self.api.post(url, json=request_data)
        body: object = response.json()
        self.access_token: str = body["token"]
        return body, response

    def get_books(self):
        url = self.base_url + self.endpoints["get_books"]

        response = self.api.get(url)
        body: object = response.json()
        self.isbn = body["books"][1]["isbn"]
        self.isbn_count = len(body["books"])
        return body, response

    def delete_book(self, ids):
        url = self.base_url + self.endpoints["delete_book_of_the_list"]
        auth = {"Authorization": f"Bearer {self.access_token}"}

        request_data = {"isbn": ids, "userId": USER_ID_DEMOQA}
        response = self.api.delete(url, json=request_data, headers=auth)

        # Si el código de respuesta es 204, retornamos un diccionario vacío
        if response.status_code == 204:
            return {}, response

        # Para otros códigos de respuesta, intentamos parsear JSON
        return response.json(), response

    def add_list_to_books(self, ids):
        url = self.base_url + self.endpoints["add_list_to_books"]
        auth = {"Authorization": f"Bearer {self.access_token}"}
        request_data = {"userId": USER_ID_DEMOQA, "collectionOfIsbns": ids}
        response = self.api.post(url, json=request_data, headers=auth)
        bodyText = response.text
        body: object = json.loads(bodyText)
        self.save_response_json(data=body, file_name='add_book_to_collection.json')
        return body, response
