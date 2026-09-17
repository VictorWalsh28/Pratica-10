import unittest
from app.app import app

class AppTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_health_check(self):
        response = self.client.get("/health-check")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})

    def test_index(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json()["status"], "ok")

if __name__ == "__main__":
    unittest.main()
