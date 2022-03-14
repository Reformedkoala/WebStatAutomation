from openpyxl import load_workbook
import os
import glob
import csv
from xlsxwriter.workbook import Workbook

# This function converts the csv data that we have cleaned into something that we can use a bit
# easier and make it look like the data that we already have
def convert_csv_xlsx(csvfile, sheet):
    csv_data = []
    with open(csvfile) as file:
        reader = csv.reader(file)
        for row in reader:
            csv_data.append(row)
    for row in csv_data:
        sheet.append(row)


# This function allows us to automatically space the columns within the excel file so the user no longer has to do this
# themselves this is done through the openpyxl library
def space_columns(sheet):
    sheet.column_dimensions['A'].width = 50
    sheet.column_dimensions['B'].width = 20
    sheet.column_dimensions['C'].width = 20
    sheet.column_dimensions['D'].width = 20
