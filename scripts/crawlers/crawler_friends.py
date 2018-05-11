# -*- coding: utf-8 -*-
from tweepy import API
from tweepy import AppAuthHandler
from tweepy import Cursor
import tweepy
import datetime
import time
import os

import json
from pprint import pprint

with open("scripts/crawlers/twitter_apps.json", "r") as f:
    apps = json.load(f)
##pprint(apps)
    
with open("scripts/crawlers/user_ids_tweets_03_17_20.json") as f:
    user_ids = json.load(f)

# selezionare il PATH dove salvare i dati scaricati    
path = "user_data/friends_ids_03_17_20/"
    
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
            print(time.ctime())
            print("sleeping...")
            print(str(delta)+'seconds')
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

for api in apis:
    print(rate_status(api))

reset = datetime.datetime.fromtimestamp(int(rate_status(apis[7])["reset"]))
reset    

###########################################################

# error timeout handling
import signal, os, sys

def handler(signum, frame):
    print('Timeout Error', signum)
    raise tweepy.TweepError("My time-out error")

signal.signal(signal.SIGALRM, handler) # defining signal error

###########################################################

print("-- started crawling --")

start = datetime.datetime.now()
i_api=0 # prima api
user_count=0
L=len(user_ids)

i_user = 0

# #i_user = 89
# i_api=0

# try:
#     out = apis[i_api].friends_ids(18601648,cursor= next_cursor)
# except tweepy.TweepError as error:
#      if((error.message=="Not authorized.") or (error.message[0]['message']=="Sorry, that page does not exist.")) :
#          print("ok")
# error

while(i_user < L):
    next_cursor= -1
    page=0
    while(next_cursor!=0):
        try:
            user_id= user_ids[i_user]
            signal.alarm(30*60)
            i_api= check_api(i_api)
            signal.alarm(0)  # reset alarm 1
            signal.alarm(60)
            out = apis[i_api].friends_ids(user_id,cursor= next_cursor)
            signal.alarm(0)  # reset alarm 2
            next_cursor = out[1][1]
            # writing to file
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
         
        except tweepy.TweepError as error:
            e = sys.exc_info()
            signal.alarm(0)  # reset alarm 
            print("--Error, I'm handling it--")
            with open("{}log.txt".format(path), "a") as f:
                f.write(time.ctime())
                f.write('\n')
                f.write("user_id:"+str(user_id))
                f.write('\n')
                f.write("i_user:"+str(i_user))
                f.write('\n')
                f.write(str(e))
                f.write('\n')
            now = datetime.datetime.now()
            check_auth=False
            if(type(error.message) is str):
                if(error.message=="Not authorized."):
                   check_auth=True
            else:
                if(error.message[0]['message']=="Sorry, that page does not exist."):
                   check_auth=True
            if(check_auth==True):
                print("handling not available user")
                with open("{}Not_available_users.txt".format(path), "a") as f:
                    f.write(user_id)
                    f.write('\n')
                # skip user
                i_user+=1
                print("--Error handled, starting again--")
                time.sleep(2)
            else:
                print(time.ctime())
                print("Started from {} minutes".format((now-start).seconds/60))
                print("now sleeping")
                time.sleep(15*60)
                # lista di api, mi autentico nuovamente con tutte:
                apis = [twitter_auth( apps[app]) for app in apps.keys()]
                print("--Error handled, starting again--")
    i_user+=1
    if(i_user%10==0):
        now = datetime.datetime.now()
        print("Started from {} minutes".format((now-start).seconds/60))
        print("Downloaded friendships for {}/{} user".format(i_user,L))


###########################################################
print("-- Finished! --")
print("Downloaded friendships for {} user".format(user_count))

