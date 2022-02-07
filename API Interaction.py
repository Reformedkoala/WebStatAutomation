import matomo_api as ma
import requests
import json

URL = 'https://mineslibrary.matomo.cloud'
TOKEN = '8510379384a55b02e47fe2c52665e13b'

api = ma.MatomoApi(URL, TOKEN)

pars = ma.format.csv | ma.language.en | ma.translateColumnNames() \
       | ma.idSite.one_or_more(1) | ma.date.lastMonth | ma.period.month \
       | ma.showColumns(ma.col.nb_visits, ma.col.nb_uniq_visitors, ma.col.nb_pageviews) \
       | ma.filter_limit(25)


response = api.Actions().getExitPageUrls(pars)
with open('test_output_data.csv', 'w') as test_output:
    for i in response.text.split(','):
        test_output.write(i)
        test_output.write(',')
