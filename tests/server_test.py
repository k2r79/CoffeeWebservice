from unittest import TestCase
import server
import requests

class TestUtils(TestCase):
    def setUp(self):
        self.app = server.app.test_client()

    def test_root(self):
        request = self.app.get("/")

        self.assertEquals(418, request.status_code)