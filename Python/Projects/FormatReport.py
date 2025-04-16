from openpyxl import Workbook, load_workbook
from openpyxl.styles import Color, PatternFill, Font, Border, Side, Alignment
from openpyxl.styles.differential import DifferentialStyle
from openpyxl.formatting.rule import ColorScaleRule, CellIsRule, FormulaRule, Rule
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

    # skip empty sheets
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

alignment = Alignment(
    horizontal='left',
    vertical='center'
)

# formatting rules

# scrap
red_fill = PatternFill(bgColor='FFC7CE')
dxf = DifferentialStyle(fill=red_fill)
scrap = Rule(type="expression", dxf=dxf)

# ram
memory_rules = {
    "DDR3": "D9E1F2",  # light blue
    "DDR4": "C6EFCE",  # light green
    "DDR5": "06402B",  # dark green
}


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
            cell.alignment = alignment

    # "autofit" columns
    for col in sheet.columns:
        max_length = 0
        column = col[0].column
        column_letter = get_column_letter(column)

        # get longest cell width in column
        for cell in col:
            try:
                if cell.value:
                    cell_length = len(str(cell.value))
                    if cell_length > max_length:
                        max_length = cell_length
            except:
                pass

        # fit column widths based on max length
        adjusted_width = max_length + 1
        sheet.column_dimensions[column_letter].width = adjusted_width
            
    # apply conditional formatting
    match sheet_name:
        case 'Dash Inventory': # manually looping because conditional formatting gets overwritten
            for row in sheet.iter_rows(min_row=2, max_row=max_row, min_col=1, max_col=1):
                for cell in row:
                    if cell.value == "SCRP":  
                        cell.fill = PatternFill(start_color='FFC7CE', end_color='FFC7CE', fill_type='solid')

        case "Desktops":
            scrap.formula = ['$C2="SCRP"']
            sheet.conditional_formatting.add(f"C2:C{max_row}", scrap)
            for mem_type, color in memory_rules.items():
                rule = Rule(
                    type='expression',
                    formula=[f'$K2="{mem_type}"'],
                    dxf=DifferentialStyle(fill=PatternFill(bgColor=color))
                )
                sheet.conditional_formatting.add(f"K2:K{max_row}", rule)

        case "Laptops":
            scrap.formula = ['$C2="SCRP"']
            sheet.conditional_formatting.add(f"C2:C{max_row}", scrap)
            for mem_type, color in memory_rules.items():
                rule = Rule(
                    type='expression',
                    formula=[f'$K2="{mem_type}"'],
                    dxf=DifferentialStyle(fill=PatternFill(bgColor=color))
                )
                sheet.conditional_formatting.add(f"K2:K{max_row}", rule)

        case "Networking":
            scrap.formula = ['$C2="SCRP"']
            sheet.conditional_formatting.add(f"C2:C{max_row}", scrap)

        case "Servers":
            scrap.formula = ['$C2="SCRP"']
            sheet.conditional_formatting.add(f"C2:C{max_row}", scrap)
            for mem_type, color in memory_rules.items():
                rule = Rule(
                    type='expression',
                    formula=[f'$N2="{mem_type}"'],
                    dxf=DifferentialStyle(fill=PatternFill(bgColor=color))
                )
                sheet.conditional_formatting.add(f"N2:N{max_row}", rule)

    # TODO add manual looping to format empty cells in middle of each table
    
    # add table to sheet
    sheet.add_table(table)

wb.save(excel_path)