import matomo_api as ma

# Variables for the api url and api token(do not share)
URL = 'https://mineslibrary.matomo.cloud'
TOKEN = '8510379384a55b02e47fe2c52665e13b'

# actual api variable we will reference to pull data
api = ma.MatomoApi(URL, TOKEN)


# Site ids- LIBWIZARD = 7, LIBANSWERS = 6, LIBCAL = 5, LIBGUIDES = 4, PRIMO = 3 (Included but not yet), Don't have
# access = 2, LIBRARY.MINES.EDU = 1

# parameters changes based on which data we want
# Page titles parameters
def page_titles(user_input, file_out):
    pars_page_titles = ma.format.csv | ma.language.en | ma.translateColumnNames() \
           | ma.idSite.one_or_more(user_input) | ma.date.lastMonth | ma.period.month \
           | ma.showColumns(ma.col.nb_visits, ma.col.nb_uniq_visitors, ma.col.nb_pageviews, ma.col.bounce_rate,
                            ma.col.exit_rate) \
           | ma.filter_limit(25)

    # The magic of web requests and for loops to store data into a csv file
    response = api.Actions().getPageTitles(pars_page_titles)
    with open(file_out, 'a') as output:
        response = response.text.replace('\n', ',')
        output.write(' ')
        for i in response.split(','):
            if "pageTitle" == i[0:9]:
                output.write('\n')
                continue
            elif "Metadata" == i[0:8]:
                output.write('\n')
                continue
            else:
                output.write(i)
                output.write(',')

# Outlinks parameters
def outlinks(user_input, file_out):
    pars_outlinks = ma.format.csv | ma.language.en | ma.translateColumnNames() \
           | ma.idSite.one_or_more(user_input) | ma.date.lastMonth | ma.period.month \
           | ma.hideColumns(ma.col.sum_time_spent) \
           | ma.filter_limit(25)

    response = api.Actions().getOutlinks(pars_outlinks)
    with open(file_out, 'a') as output:
        response = response.text
        response = response.split(',')
        for i in response:
            output.write(i)
            output.write(',')

#Referring URLs parameters
def referring_urls(user_input, file_out):
    pars_referring_urls = ma.format.csv | ma.language.en | ma.translateColumnNames() \
           | ma.idSite.one_or_more(user_input) | ma.date.lastMonth | ma.period.month \
           | ma.showColumns(ma.col.nb_visits) \
           | ma.filter_limit(25)
    response = api.Referrers().getWebsites(pars_referring_urls)
    with open(file_out, 'a') as output:
        response = response.text.replace('\n', ',')
        output.write('\n')
        for i in response.split(','):
            if "referrerName" == i[0:12]:
                output.write('\n')
                continue
            elif "Metadata" == i[0:8]:
                output.write('\n')
                continue
            else:
                output.write(i)
                output.write(',')
