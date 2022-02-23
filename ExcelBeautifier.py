import xlwt
import openpyxl
from xlwt import Workbook
import pandas as pd

read_file = pd.read_csv (r'output.csv')
read_file.to_excel (r'output.xlsx', index = None, header=True)
