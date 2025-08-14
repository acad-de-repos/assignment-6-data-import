import unittest
import pandas as pd
import os
from assignment import import_csv, import_json, import_excel

class TestDataImport(unittest.TestCase):
    def setUp(self):
        """Set up temporary data files for testing"""
        self.csv_file = 'test.csv'
        self.json_file = 'test.json'
        self.excel_file = 'test.xlsx'

        # Create dummy CSV file
        pd.DataFrame({'name': ['Alice'], 'age': [30]}).to_csv(self.csv_file, index=False)

        # Create dummy JSON file
        with open(self.json_file, 'w') as f:
            f.write('[{"name": "Bob", "age": 25}] ')

        # Create dummy Excel file
        pd.DataFrame({'name': ['Charlie'], 'age': [35]}).to_excel(self.excel_file, sheet_name='Sheet1', index=False)

    def tearDown(self):
        """Clean up created files after each test"""
        for f in [self.csv_file, self.json_file, self.excel_file]:
            if os.path.exists(f):
                os.remove(f)

    def test_import_csv(self):
        """Test that the import_csv function works correctly"""
        df = import_csv(self.csv_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df['name'].iloc[0], 'Alice')

    def test_import_json(self):
        """Test that the import_json function works correctly"""
        df = import_json(self.json_file)
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df['name'].iloc[0], 'Bob')

    def test_import_excel(self):
        """Test that the import_excel function works correctly"""
        df = import_excel(self.excel_file, 'Sheet1')
        self.assertIsInstance(df, pd.DataFrame)
        self.assertEqual(df.shape, (1, 2))
        self.assertEqual(df['name'].iloc[0], 'Charlie')

if __name__ == '__main__':
    unittest.main()
