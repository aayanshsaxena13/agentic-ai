# Import statements are put here...
import pandas as pd
import os
import json
from openpyxl import Workbook

# Locate input and output paths...
file_path = os.path.join(os.path.dirname(__file__), "..", "input", "excel_input.json")
output_path = os.path.join(os.path.dirname(__file__), "..", "output", "excel.xlsx")

def automateToExcel():
    # Data loading...
    with open(file_path, "r") as f:
        data = json.loads(f.read())

    df = pd.DataFrame(data)

    # This is the last part...
    df.to_excel(output_path, index=False)
    return "Generated excel spreadsheet using Agentic AI..."