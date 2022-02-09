import matomo_api as ma

# Variables for the api url and api token(do not share)
URL = 'https://mineslibrary.matomo.cloud'
TOKEN = '8510379384a55b02e47fe2c52665e13b'

# actual api variable we will reference to pull data
api = ma.MatomoApi(URL, TOKEN)


# Site ids- LIBWIZARD = 7, LIBANSWERS = 6, LIBCAL = 5, LIBGUIDES = 4, PRIMO(Don't use Matomo) = 3, Don't have
# access = 2, LIBRARY.MINES.EDU =1

# parameters changes based on which data we want
# Page titles parameters
pars_page_titles = ma.format.csv | ma.language.en | ma.translateColumnNames() \
       | ma.idSite.one_or_more(1) | ma.date.lastMonth | ma.period.month \
       | ma.showColumns(ma.col.nb_visits, ma.col.nb_uniq_visitors, ma.col.nb_pageviews, ma.col.bounce_rate,
                        ma.col.exit_rate) \
       | ma.filter_limit(25)

# The magic of web requests and for loops to store data into a csv file
response = api.Actions().getPageTitles(pars_page_titles)
with open('test_output_data.csv', 'w') as test_output:
    response = response.text.replace('\n', ',')
    test_output.write(' ')
    for i in response.split(','):
        if "pageTitle" == i[0:9]:
            test_output.write('\n')
            continue
        elif "Metadata" == i[0:8]:
            test_output.write('\n')
            continue
        else:
            test_output.write(i)
            test_output.write(',')

# Outlinks parameters
pars_outlinks = ma.format.csv | ma.language.en | ma.translateColumnNames() \
       | ma.idSite.one_or_more(1) | ma.date.lastMonth | ma.period.month \
       | ma.hideColumns(ma.col.sum_time_spent) \
       | ma.filter_limit(25)

response = api.Actions().getOutlinks(pars_outlinks)

#Referring URLs parameters
pars_referring_urls = ma.format.csv | ma.language.en | ma.translateColumnNames() \
       | ma.idSite.one_or_more(1) | ma.date.lastMonth | ma.period.month \
       | ma.showColumns(ma.col.nb_visits) \
       | ma.filter_limit(25)

response = api.Referrers().getWebsites(pars_referring_urls)
