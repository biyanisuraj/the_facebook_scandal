import datetime
import json
import gzip
import time
from tweepy import API
from tweepy import AppAuthHandler
from tweepy import Cursor

CONSUMER_KEY = 'NHsKGfxrXTXlf2mfH2n0jbW1l'
CONSUMER_SECRET = 'W0HE0cTlfIcJtkIX5hClcH4ILgyv018Q8fWdo0sgRo5bdFzAMA'
ACCESS_TOKEN = '339641100-VOI2SsKVbSsQIfnHNSDohSJ4aB9rJpSXkDeYaeo3'
ACCESS_SECRET = 'wMUjClr78yjlsyWIjxVunFKQ8zYOjlzgMfItuRiec5Y3c'

auth = AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

q = '#facebookgate OR #cambridgeanalytica OR ' \
    '#deletefacebook OR #Zuckerberg'
items, item_counter = 1000000, 1
remaining_searches = int(
    api.rate_limit_status()['resources']
                           ['search']
                           ['/search/tweets']
                           ['remaining'])
since, until = '2018-03-24', '2018-03-25'

with gzip.open('./results.json.gz', 'w') as f:
    f.write('{ "tweets": [')
    for tweet in Cursor(api.search, q=q, since=since, until=until,
                        count=100).items(items):
        f.write(json.dumps(tweet._json, separators=(',', ': '),
                           sort_keys=True)+"\n")
        f.write(',\n') if item_counter < items else f.write('')

        if item_counter % 1000 == 0:
            remaining_searches = int(
                api.rate_limit_status()['resources']
                                       ['search']
                                       ['/search/tweets']
                                       ['remaining'])
            print 'Writed ' + str(item_counter) + ' tweets, ' \
                + str(remaining_searches) + ' remaining queries'

            if remaining_searches <= 10:
                now = datetime.datetime.now()
                reset = api.rate_limit_status()['resources']['search']['/search/tweets']['reset']
                reset = datetime.datetime.fromtimestamp(int(reset))

                print '\nRate limit exceeded, will continue at ' + \
                    reset.strftime('%Y-%m-%d %H:%M:%S')
                print 'Sleeping for ' \
                    + str(((reset - now).seconds + 120) / 60) + ' minutes\n'

                time.sleep((reset - now).seconds + 120)

                print '\nSleep time ended\n'

                remaining_searches = int(
                    api.rate_limit_status()['resources']['search']
                                           ['/search/tweets']['remaining'])

        item_counter += 1

    f.write(']}')
