import unittest
from modules.audition_management import AuditionManager
from unittest.mock import patch
import io

class TestAuditionManagement(unittest.TestCase):
    def setUp(self):
        self.audition_manager = AuditionManager()
        self.selected_candidates = ["John Doe", "Jane Smith"]

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_organize_auditions(self, mock_stdout):
        # Test organizing auditions for selected candidates
        self.audition_manager.organize_auditions(self.selected_candidates)
        output = mock_stdout.getvalue()
        self.assertIn("Audition scheduled for luis Gomez in California or Florida.", output)
        self.assertIn("Audition scheduled for Juanito perez Smith in California or Florida.", output)

if __name__ == "__main__":
    unittest.main()