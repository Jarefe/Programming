from openpyxl import Workbook, load_workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule
import os, sys

def is_sheet_empty(sheet):
    for row in sheet.iter_rows(min_row=2): # skip header
        for cell in row:
            if cell.value is not None:
                return False # if sheet has data beyond header
    return True # only header exists


script_dir = os.path.dirname(os.path.abspath(__file__))
excel_path = os.path.join(script_dir, "Test Output.xlsx")

# load existing workbook
try:
    original_path = 'C:/Users/test/Downloads/Report 1.xlsx' # TODO change to be dynamic
    original_wb = load_workbook(original_path)
except:
    print("Error loading file, stopping program")
    sys.exit(1)

# create new workbook
wb = Workbook()

# remove default sheet from wb
wb.remove(wb.active)

# copy all non empty sheets 
for sheet_name in original_wb.sheetnames:
    original_sheet = original_wb[sheet_name]

    if is_sheet_empty(original_sheet):
        print(f'{sheet_name} is empty; skipping')
        continue

    new_sheet = wb.create_sheet(title=sheet_name)

    for row in original_sheet.iter_rows():
        for cell in row:
            new_sheet.cell(row=cell.row, column=cell.column, value=cell.value)


