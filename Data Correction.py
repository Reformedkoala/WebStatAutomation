import pandas as pd

data = pd.read_csv('Libwizard_Test_Data.csv', encoding='UTF-16 LE')
data2 = pd.read_csv('Libwizard_Test_Data2.csv', encoding='UTF-16 LE')
data3 = pd.read_csv('Libwizard_Test_Data3.csv', encoding='UTF-16 LE')

print(data[['Label', 'Unique Pageviews', 'Pageviews', 'Bounce Rate', 'Exit rate']])
print(data2[['Label', 'Unique Clicks', "Clicks"]])
print(data3[['Label', 'Visits']])

