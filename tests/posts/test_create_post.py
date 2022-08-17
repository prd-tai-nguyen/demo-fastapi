from tests import BasePytest
import pytest

class TestCreatePost(BasePytest):
    @pytest.fixture(autouse=True)
    def _setUp(self):
        super()._setUp()
        self.url = '/posts/'

    def test_create_post_success(self):
        data = self.get_data_valid()
        response = self.testClient.post(
            url=self.url, json=data, headers=self.headers)
        
        print(response)
        assert response.status_code == 200
        

    @staticmethod
    def get_data_valid():
        data = {
            "content": "paradox1",
        }

        return data
