import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Color, PatternFill, Font, Border
from openpyxl.styles import colors
from openpyxl.cell import Cell
import os
import glob
import csv
from xlsxwriter.workbook import Workbook

def convert_csv_xlsx():
    for csvfile in glob.glob(os.path.join('.', 'output.csv')):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt', encoding='utf8') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()

convert_csv_xlsx()


xfile = openpyxl.load_workbook('output.xlsx')
sheet = xfile['Sheet1']

def space_columns():
    sheet.column_dimensions['A'].width = 60
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 30
    sheet.column_dimensions['D'].width = 30


space_columns()

redFill = PatternFill(start_color='FFCC99',
                   end_color='FFCC99',
                   fill_type='solid')
sheet['A1'].fill = redFill
sheet.merge_cells('A1:E1')
greenFill = PatternFill(start_color='c6e0b4',
                   end_color='c6e0b4',
                   fill_type='solid')
sheet['A29'].fill = greenFill
sheet.merge_cells('A29:C29')
yellowFill = PatternFill(start_color='ffe699',
                   end_color='ffe699',
                   fill_type='solid')
sheet['A57'].fill = yellowFill
sheet.merge_cells('A57:B57')

xfile.save('output.xlsx')
