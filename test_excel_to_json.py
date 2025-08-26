import unittest
import pandas as pd
from excel_to_json import excel_to_json
import json
import os

class TestExcelToJson(unittest.TestCase):

    def setUp(self):
        # Create a sample Excel file for testing
        data = {
            'Sheet1': pd.DataFrame({
                'Name': ['John', 'Anna'],
                'Age': [28, 24]
            })
        }
        with pd.ExcelWriter('test.xlsx') as writer:
            data['Sheet1'].to_excel(writer, sheet_name='Sheet1', index=False)

    def tearDown(self):
        # Remove the test files
        if os.path.exists('test.xlsx'):
            os.remove('test.xlsx')
        if os.path.exists('output.json'):
            os.remove('output.json')

    def test_excel_to_json(self):
        excel_to_json('test.xlsx')
        self.assertTrue(os.path.exists('output.json'))

        with open('output.json', 'r') as json_file:
            json_data = json.load(json_file)
            self.assertIn('Sheet1', json_data)
            self.assertEqual(len(json_data['Sheet1']), 2)

if __name__ == '__main__':
    unittest.main()