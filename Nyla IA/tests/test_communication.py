import unittest
from modules.communication import Communicator

class TestCommunication(unittest.TestCase):
    def setUp(self):
        self.communicator = Communicator()
        self.candidate = {"name": "John Doe", "email": "john@example.com", "phone": "123-456-7890", "talent": "music"}

    def test_contact_candidates(self):
        # Test contacting candidates
        responses = self.communicator.contact_candidates([self.candidate])
        self.assertIsInstance(responses, list)
        self.assertEqual(len(responses), 1)
        self.assertEqual(responses[0]["candidate"], "John Doe")
        self.assertEqual(responses[0]["response"], "interested")

    def test_send_email(self):
        # Test sending an email to a single candidate
        response = self.communicator._send_email(self.candidate)
        self.assertIsInstance(response, dict)
        self.assertEqual(response["candidate"], "John Doe")
        self.assertEqual(response["response"], "interested")

if __name__ == "__main__":
    unittest.main()