import unittest
from modules.data_collection import DataCollector

class TestDataCollection(unittest.TestCase):
    def test_collect_data(self):
        collector = DataCollector()
        data = collector.collect_data()
        self.assertIsInstance(data, list)
        self.assertTrue(all(isinstance(item, dict) for item in data))

if __name__ == "__main__":
    unittest.main()