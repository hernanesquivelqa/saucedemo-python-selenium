import requests
from config import USERNAME_DEMOQA, PASSWORD_DEMOQA
class Api:
    def __init__(self):
        self.base_url = 'https://demoqa.com'
        self.api = requests
        self.endpoints = {
            'create_user': '/Account/v1/User',
            'generate_token': '/Account/v1/GenerateToken',
            'login': '/Account/v1/Login',
            'user': '/Account/v1/User/{username}',
            'update_user': '/Account/v1/User/{username}'
        }
        
    def create_new_user(self, username, password):
        url = self.base_url + self.endpoints['create_user']
        request_data = {
            "userName": username,
            "password": password
        }
        response = self.api.post(url, data=request_data) 
        #assert response.status_code == 201
        body: object =  response.json()
        return (body, response)
    def set_access_token(self):
        url = self.base_url + self.endpoints['generate_token']
        request_data = {
            "userName": USERNAME_DEMOQA,
            "password": PASSWORD_DEMOQA
        }
        response = self.api.post(url, data=request_data) 
        body: object =  response.json()
        return (body, response)
