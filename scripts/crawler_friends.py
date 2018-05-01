from tweepy import API
from tweepy import AppAuthHandler
from tweepy import Cursor
import datetime

import json
from pprint import pprint

with open("scripts/twitter_apps.json", "r") as f:
    apps = json.load(f)
    

pprint(apps)

app_1=apps['app_1']

def twitter_auth(app):
    "restituisce un oggetto api, in input un dizionario con le credenziali dell'app"
    auth = AppAuthHandler(app['CONSUMER_KEY'], app['CONSUMER_SECRET'])
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

api_1 = twitter_auth(apps['app_1'])
api_2 = twitter_auth(apps['app_2'])

api_1.rate_limit_status()['resources']['friends']['/friends/ids']
api_2.rate_limit_status()['resources']['friends']['/friends/ids']

def rate_status(api):
    return api.rate_limit_status()['resources']['friends']['/friends/ids']

# lista di api, mi autentico con tutte:
apis = [twitter_auth( apps[app]) for app in apps.keys()]

friends = (api_1.friends_ids(207323988))
friends = (apis[1].friends_ids(207323988))

for api in apis:
    print rate_status(api)

    
###########################################################
# NUMERO DI RICHIESTE
# Abbiamo 15 richieste ogni 15 minuti per ogni app, ovvero una al minuto
# in 24 h il numero massimo di richieste è:
requests_24h = 24*60 # per singolo account

utenti = 100000
n_accounts = 10

giorni_necessari = utenti/requests_24h/n_accounts
giorni_necessari


