from openpyxl import Workbook, load_workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Side
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule
from openpyxl.worksheet.table import Table, TableStyleInfo
from openpyxl.utils import get_column_letter
import os, sys

def is_sheet_empty(sheet):
    for row in sheet.iter_rows(min_row=2): # skip header
        for cell in row:
            if cell.value is not None:
                return False # if sheet has data beyond header
    return True # only header exists

# output file will be in same folder as script
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

# create tables in each remaining sheet
# and apply styles
orange_fill = PatternFill(
    start_color='FFA500', 
    end_color='FFA500', 
    fill_type='solid')

border = Border(
    left=Side(style="thin"), 
    right=Side(style="thin"), 
    top=Side(style="thin"), 
    bottom=Side(style="thin"))


for sheet_name in wb.sheetnames:
    sheet = wb[sheet_name]

    max_row = sheet.max_row
    max_column = sheet.max_column


    # define range of cells including header
    table_range = f'A1:{get_column_letter(max_column)}{max_row}'
    
    # create table with data range
    table = Table(displayName=f"Table_{sheet_name.replace(' ','')}", ref=table_range)
    
    # style = TableStyleInfo(
    #     name="TableStyleMedium2",
    #     showFirstColumn=False,
    #     showLastColumn=False,
    #     showRowStripes=False,
    #     showColumnStripes=False
    #     )
    # table.tableStyleInfo = style

    # apply orange fill to header row
    for col in range(1, max_column + 1):
        cell = sheet.cell(row=1, column=col)
        cell.fill = orange_fill

    # apply borders to each cell
    for row in sheet.iter_rows(min_row=1, max_row=max_row, min_col=1, max_col=max_column):
        for cell in row:
            cell.border = border

    # add table to sheet
    sheet.add_table(table)

# TODO apply conditional formatting



wb.save(excel_path)