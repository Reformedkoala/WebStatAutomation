from openpyxl import Workbook
import os
import glob
import csv
from xlsxwriter.workbook import Workbook

def convert_csv_xlsx(filename):
    for csvfile in glob.glob(os.path.join('.', filename)):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()


def space_columns(sheet):
    sheet.column_dimensions['A'].width = 60
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 30
    sheet.column_dimensions['D'].width = 30

