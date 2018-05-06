# -*- coding: utf-8 -*-
from tweepy import API
from tweepy import AppAuthHandler
from tweepy import Cursor
import datetime
import time

import json
from pprint import pprint

with open("scripts/twitter_apps.json", "r") as f:
    apps = json.load(f)
    
with open("scripts/user_ids.json") as f:
    user_ids = json.load(f)

###########################################################
def twitter_auth(app):
    """ restituisce un oggetto api, 
    in input un dizionario con le credenziali dell'app """
    auth = AppAuthHandler(app['CONSUMER_KEY'], app['CONSUMER_SECRET'])
    api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    return api

def rate_status(api):
    return api.rate_limit_status()['resources']['friends']['/friends/ids']

###########################################################

# lista di api, mi autentico con tutte:
apis = [twitter_auth( apps[app]) for app in apps.keys()]

###########################################################
def check_api(i_api):
    """ 
    - controllo l'api, usando l'indice, passo alla successiva
    se le richieste disponibili sono terminate
    - metto a dormire dopo l'ultima app e ricomincio
    """
    if(rate_status(apis[i_api])["remaining"]==0):
        print("api:{}".format(i_api))
        print(rate_status(apis[i_api]))
        print("changing api")

        if( i_api == (len(apis)-1) ):
            # TODO: put to sleep
            now = datetime.datetime.now()
            reset = datetime.datetime.fromtimestamp(int(rate_status(apis[i_api])["reset"]))
            delta = (reset-now).seconds
            print("sleeping...")
            time.sleep(delta)
            # ricomincio ciclo apis
            i_api = 0
        else:
            ## cambio api
            i_api += 1
    return i_api

###########################################################

import gzip
import datetime

# for user_id in user_ids
for api in apis:
    print(rate_status(api))

now = datetime.datetime.now()
reset = datetime.datetime.fromtimestamp(int(rate_status(apis[2])["reset"]))

delta = (reset-now).seconds
delta/60

    
###########################################################
path = "user_data/"

print("-- started crawling --")
i_api=0 # prima api
user_count=0
L=len(user_ids)

for user_id in user_ids:
    next_cursor= -1
    page=0
    while(next_cursor!=0):
        i_api= check_api(i_api)
        i_api= check_api(i_api)
        out = apis[i_api].friends_ids(user_id,cursor= next_cursor)
        next_cursor = out[1][1]
        
        with gzip.open("{}user_{}_{}.json.gz".format(path,user_id,page), "w") as f:
            f.write('{')
            f.write('"user_id": {} ,'.format(user_id)) 
            f.write(' "friends_ids": ')
            f.write(json.dumps(out[0]))
            f.write(',')
            f.write(' "cursor": ')
            f.write(json.dumps(out[1]))
            f.write('}')
        page+=1
    user_count+=1
    if(user_count%100==0):
        print("Downloaded friendships for {}/{} user".format(user_count,L))
        
###########################################################
print("-- Finished! --")
print("Downloaded friendships for {} user".format(user_count))


###########################################################
# NUMERO DI RICHIESTE
# Abbiamo 15 richieste ogni 15 minuti per ogni app, ovvero una al minuto
# in 24 h il numero massimo di richieste è:
requests_24h = 24*60  # per singolo account

utenti = 100000
n_accounts = 10

giorni_necessari = utenti/requests_24h/n_accounts
#giorni_necessari

###########################################################
