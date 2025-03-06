import pytest
from tests.api.demoqa.api_request import Api

class TestBookApi:
    def create_new_user(self):
        api = Api()
        [body] = api.create_new_user("hernanasdk","Password1234!")




if __name__ == '__main__':
    pytest.main()