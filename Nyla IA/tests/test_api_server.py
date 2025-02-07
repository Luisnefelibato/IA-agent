import unittest
import requests

class TestAPIServer(unittest.TestCase):
    BASE_URL = "http://localhost:5000"

    def test_search_talent(self):
        response = requests.get(f"{self.BASE_URL}/search_talent", params={"query": "music"})
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_schedule_audition(self):
        data = {"candidate_name": "John Doe", "location": "California"}
        response = requests.post(f"{self.BASE_URL}/schedule_audition", json=data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "Audition scheduled successfully")

if __name__ == "__main__":
    unittest.main()