import unittest
import pandas as pd
import os

class TestDataOperations(unittest.TestCase):
    def setUp(self):
        # Setup method runs before each test
        self.test_file_path = "path/to/your/test.csv"
        # Create a sample test CSV if needed for testing
        self.sample_data = pd.DataFrame({
            'column1': [1, 2, 3],
            'column2': ['a', 'b', 'c']
        })
        self.sample_data.to_csv(self.test_file_path, index=False)

    def tearDown(self):
        # Cleanup method runs after each test
        if os.path.exists(self.test_file_path):
            os.remove(self.test_file_path)

    def test_getAllData_file_exists(self):
        """Test if the method can successfully read an existing file"""
        result = getAllData(self.test_file_path)
        self.assertIsNotNone(result)
        self.assertTrue(isinstance(result, pd.DataFrame))

    def test_getAllData_file_not_found(self):
        """Test behavior when file doesn't exist"""
        with self.assertRaises(FileNotFoundError):
            getAllData("nonexistent_file.csv")

    def test_getAllData_empty_file(self):
        """Test behavior with empty CSV file"""
        # Create empty file
        pd.DataFrame().to_csv(self.test_file_path, index=False)
        result = getAllData(self.test_file_path)
        self.assertTrue(result.empty)

    def test_getAllData_corrupted_file(self):
        """Test behavior with corrupted CSV file"""
        # Write invalid CSV content
        with open(self.test_file_path, 'w') as f:
            f.write("This is not,valid\nCSV,data,extra,column")
        with self.assertRaises(pd.errors.EmptyDataError):
            getAllData(self.test_file_path)

    def test_getAllData_expected_columns(self):
        """Test if the loaded data has the expected structure"""
        result = getAllData(self.test_file_path)
        expected_columns = ['column1', 'column2']
        self.assertListEqual(list(result.columns), expected_columns)

    def test_getAllData_data_types(self):
        """Test if the data types in the loaded data are correct"""
        result = getAllData(self.test_file_path)
        self.assertEqual(result['column1'].dtype, 'int64')
        self.assertEqual(result['column2'].dtype, 'object')

if __name__ == '__main__':
    unittest.main()
