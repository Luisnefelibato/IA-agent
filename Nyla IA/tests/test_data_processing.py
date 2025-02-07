import unittest
from modules.data_processing import DataProcessor

class TestDataProcessing(unittest.TestCase):
    def test_process_data(self):
        processor = DataProcessor()
        raw_data = [{"name": "John Doe", "talent": "music"}]
        processed_data = processor.process_data(raw_data)
        self.assertEqual(len(processed_data), 1)

if __name__ == "__main__":
    unittest.main()