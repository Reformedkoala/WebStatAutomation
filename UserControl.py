from API_Interaction import *
import os
user_site = 0
while user_site == 0:
    print('Hello and welcome to the web stats automation software.')
    print('Simply enter the site below and either the location you want to save to or the default Y: drive.')
    print('1) Library.Mines.edu')
    print('3) Primo(not functional yet)')
    print('4) LibGuides')
    print('5) Libcal')
    print('6) Libanswers')
    print('7) Libwizard')
    user_site = int(input('Enter the number of the site you want to access here: '))
    if (1 >= user_site >= 7) or user_site == 2:
        print('Please enter a valid input')
        print('++++++++++++++++++++++++++')
        user_site = 0
default = "Y:\LB\SharedSpace\Systems\WebStats\\"
print('All files will be save to the Y drive with a path of', default)
print('You must add a name for the file')
isFile = os.path.isdir(default)
if isFile != True :
    print('Error finding base directory for file please ensure that the required directory exists.')
    quit()
file_out = input('Choose the name for the file here with no extension: ')
file_out = default + file_out + '.csv'
print('The file you are saving to is', file_out)
page_titles(user_site, file_out)
outlinks(user_site, file_out)
referring_urls(user_site, file_out)
