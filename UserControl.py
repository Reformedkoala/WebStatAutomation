# Along the development process I created a CLI in order to interact with the code as an early form of interface.  This
# later changed into the GUI now being used.


# IMPORTANT THIS IS NOT FOR IMPLEMENTATION PURPOSES AND WAS ONLY FOR DEVELOPMENT
"""
from API_Interaction import *
from ExcelBeautifier import *
import openpyxl
import os

# Initializing any variables we may need as well as importing all files
user_site = 0
# Current command line interface
# TODO make this into a visual interface eventually
while user_site == 0:
    # Prompting user for all inputs
    print('Hello and welcome to the web stats automation software.')
    print('Simply enter the site below and either the location you want to save to or the default Y: drive.')
    print('1) Library.Mines.edu')
    print('3) Primo(not functional yet)')
    print('4) LibGuides')
    print('5) Libcal')
    print('6) Libanswers')
    print('7) Libwizard')
    user_site = int(input('Enter the number of the site you want to access here: '))
    # Cleaning user input to ensure that they don't enter something wrong(this will be much easier with a graphical
    # interface and won't really be a thing)
    if (1 >= user_site >= 7) or user_site == 2:
        print('Please enter a valid input')
        print('++++++++++++++++++++++++++')
        user_site = 0
# Setting up our file path that the user chooses with a default directory of the webstats storage
default = "Y:\LB\SharedSpace\Systems\WebStats\\"
print('All files will be save to the Y drive with a path of', default)
print('You must add a name for the file')
isFile = os.path.isdir(default)
# Checks to ensure the base directory exists and the user has access to the directory(Done to avoid the user possibly
# not having access to the Y drive.  If this errors and the directory exists try running the program as administrator.
if isFile != True:
    print('Error finding base directory for file please ensure that the required directory exists.')
    quit()
# Prompting the user for the name of the file they would like
file_out = input('Choose the name for the file here with no extension: ')
# Combining user input into the file name
file_out = default + file_out + '.csv'
print('The file you are saving to is', file_out)
# Calling the page_titles function to get the data for page titles(More decsription in API_interaction)
page_titles(user_site, file_out)
# Calling outlinks function to get the data for outlinks(More decsription in API_interaction)
outlinks(user_site, file_out)
# Calling the refferring_urls function to get the data for referring urls(More decsription in API_interaction)
referring_urls(user_site, file_out)
# Calling the convert csv to excel file to ensure we are now making an excel file to edit later
convert_csv_xlsx(file_out)
# Converts and copies our csv filename
delete_file = file_out
file_out = file_out[:-4]
file_out += '.xlsx'
# Deletes the csv file to ensure we don't have two of the same file
os.remove(delete_file)
# Creates a workbook from the excel file in order to edit and clean up
xfile = openpyxl.load_workbook(file_out)
sheet = xfile[
    'Sheet1']  # TODO make this a variable for integration with current data and change the sheet based on data
# Spaces all columns within the excel file and saves the file and sheet
space_columns(sheet)
xfile.save(file_out)
"""