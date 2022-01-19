import matomo_api as ma
from requests import Response

URL = 'https://mineslibrary.matomo.cloud'
TOKEN = '8510379384a55b02e47fe2c52665e13b'
api = ma.MatomoApi(URL, TOKEN)
pars = ma.format.csv | ma.language.en | ma.translateColumnNames() \
       | ma.idSite.all | ma.date.lastMonth | ma.period.month \
       | ma.showColumns(ma.col.nb_visits, ma.col.nb_uniq_visitors, ma.col.nb_pageviews) \
       | ma.filter_limit(25)

qry_result = api.Actions().getExitPageUrls(pars)

"""
with open('test_file.csv') as test_file:
       test_file.write(qry_result)
"""