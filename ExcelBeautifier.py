from openpyxl import Workbook
import os
import glob
import csv
from xlsxwriter.workbook import Workbook


# This function converts the csv data that we have cleaned into something that we can use a bit
# easier and make it look like the data that we already have
def convert_csv_xlsx(filename):
    # This just pulls in all the data from the csv file and allows us to iterate over it to write to an excel file
    for csvfile in glob.glob(os.path.join('.', filename)):
        workbook = Workbook(csvfile[:-4] + '.xlsx')
        worksheet = workbook.add_worksheet()
        with open(csvfile, 'rt') as f:
            reader = csv.reader(f)
            for r, row in enumerate(reader):
                for c, col in enumerate(row):
                    worksheet.write(r, c, col)
        workbook.close()


# This function allows us to automatically space the columns within the excel file so the user no longer has to do this
# themselves this is done through the openpyxl library
def space_columns(sheet):
    sheet.column_dimensions['A'].width = 60
    sheet.column_dimensions['B'].width = 30
    sheet.column_dimensions['C'].width = 30
    sheet.column_dimensions['D'].width = 30
