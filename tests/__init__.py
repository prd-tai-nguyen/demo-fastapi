from fastapi.testclient import TestClient
from main import app

class BasePytest:
    def _setUp(self):
        self.testClient = TestClient(app)
        self.headers = {
            "Authorization": f'Bearer {self.get_token()}'}

    def get_token(self):
        return "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjEwMTY0NzAsInVzZXJfaWQiOjF9.iozTM_-auGgJrfLX-JKtS1_Ajw8xnYvAGgZ7up3VaX4"
