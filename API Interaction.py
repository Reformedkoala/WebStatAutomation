import matomo_api as ma
import requests
'''
URL = 'https://mineslibrary.matomo.cloud'
TOKEN = '8510379384a55b02e47fe2c52665e13b'
api = ma.MatomoApi(URL, TOKEN)
'''
pars = ma.format.csv | ma.language.en | ma.translateColumnNames() \
       | ma.idSite.all | ma.date.lastMonth | ma.period.month \
       | ma.showColumns(ma.col.nb_visits, ma.col.nb_uniq_visitors, ma.col.nb_pageviews) \
       | ma.filter_limit(25)

my_headers = {'Authorization' : 'Bearer  {8510379384a55b02e47fe2c52665e13b}'}
response = requests.get('https://mineslibrary.matomo.cloud', headers=my_headers, params=pars)
print(response.json())

"""
with open('test_output_data.csv') as test_file:
       test_file.write(response)
"""