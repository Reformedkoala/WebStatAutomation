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
check = 0
while check == 0:
    print('Please enter the full directory path below or choose the default directory.')
    print('1) Default')
    default = r"Y:\LB\SharedSpace\Systems\WebStats\output.csv"
    isFile = os.path.exists(default)
    print(isFile)
    file_out = input('Enter Here:')
