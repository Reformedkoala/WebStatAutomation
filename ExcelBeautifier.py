import openpyxl
from openpyxl import Workbook
import pandas as pd



def convert_csv_xlsx():
    read_file = pd.read_csv (r'output.csv')
    read_file.to_excel (r'output.xlsx', index = None, header=True)


xfile = openpyxl.load_workbook('output.xlsx')
sheet = xfile['Sheet1']


def space_columns():
    sheet.column_dimensions['A'].width = 60
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 30
    sheet.column_dimensions['D'].width = 30
    xfile.save('output.xlsx')
