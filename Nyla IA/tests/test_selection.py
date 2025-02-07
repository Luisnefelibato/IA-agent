import unittest
from modules.selection import TalentSelector

class TestSelection(unittest.TestCase):
    def setUp(self):
        self.selector = TalentSelector()
        self.responses = [
            {"candidate": "John Doe", "response": "interested"},
            {"candidate": "Jane Smith", "response": "not interested"},
        ]

    def test_preselect_candidates(self):
        # Test preselection of candidates based on responses
        selected_candidates = self.selector.preselect_candidates(self.responses)
        self.assertIsInstance(selected_candidates, list)
        self.assertEqual(len(selected_candidates), 1)
        self.assertEqual(selected_candidates[0], "John Doe")

if __name__ == "__main__":
    unittest.main()