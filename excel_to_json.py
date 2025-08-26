import pandas as pd
import json

def excel_to_json(excel_file_path):
    try:
        # Read the Excel file
        excel_file = pd.read_excel(excel_file_path, sheet_name=None)
        
        # Convert each sheet to JSON
        json_data = {}
        for sheet_name, df in excel_file.items():
            json_data[sheet_name] = df.to_dict(orient='records')
        
        # Save the JSON data
        with open('output.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=4)
        
        print("Conversion successful. JSON saved to output.json")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
excel_to_json('example.xlsx')