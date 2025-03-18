import pytest
from config import random_num
from tests.api.demoqa.api_request import Api


class TestBookApi:

    def test_authorized(self):
        api = Api()
        [json, response] = api.authorized()

        assert response.status_code == 200
        assert json == True

    def test_generate_token(self):
        api = Api()
        [json, response] = api.set_access_token()
        assert response.status_code == 200
        assert json["token"] != None

    def test_get_book(self):
        api = Api()
        [json, response] = api.get_books()

        assert response.status_code == 200
        assert json["books"] != None

    

    def test_add_list_to_books(self):
        api = Api()
        api.set_access_token()
        [json, response] = api.get_books()
        book_id = json["books"][random_num]["isbn"]
        data = [{"isbn": book_id}]
        json, response = api.add_list_to_books(ids=data)
        assert response.status_code == 201

    

    def test_delete_book(self):
        api = Api()
        [json, response] = api.get_books()
        book_id = json["books"][random_num]["isbn"]
        api.set_access_token()

        json, response = api.delete_book(ids=book_id)

        assert response.status_code == 204


if __name__ == "__main__":
    pytest.main()
