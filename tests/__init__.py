from fastapi.testclient import TestClient
from ..main import app
import pytest

class BasePytest:
    def _setUp(self):
        self.testClient = TestClient(app)
        self.token = self.get_token()
        self.headers = {
            'Authorization': 'Bearer {self.token}'}

    def get_token(self):
        return "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE2NjA4MTg1NTMsInVzZXJfaWQiOjF9.5ZUMotTh3SKHCk2Ygo0cJRW9PzAhUjEqqeyBl57oiOo"
