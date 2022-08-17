from tests import BasePytest


class TestCreatePost(BasePytest):
    def _setUp(self):
        super()._setUp()
        self.url = '/post'

    def test_create_post_success(self):
        data = self.get_data_valid()
        print(data)
        response = self.testClient.post(
            url=self.url, data=data, headers=self.headers)
        print(response)
        assert response.status_code == 200

    @staticmethod
    def get_data_valid():
        data = {
            "content": "paradox",
        }

        return data
