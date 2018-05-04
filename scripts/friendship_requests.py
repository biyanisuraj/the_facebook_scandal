from pymongo import MongoClient
import pymongo

CLIENT = MongoClient()
DB = CLIENT['social_database_test']
db = CLIENT.social_database_test

db.collection_names()[0]
db.tweets_prova.find_one()

tweets = db.tweets_prova
tweets.count()

from pprint import pprint

pprint(tweets.find_one())


user_ids = [ str(userid["user"]["id"])
             for userid in tweets.find( projection = {"user.id" : 1})
             .sort('user.followers_count', pymongo.DESCENDING )
]

for id in user_ids:
    print(id)

# scrivo su file gli id degli utenti
with open("scripts/prova.txt", 'w') as f:
    for id in user_ids:
        f.write(id+'\n')

###########################################################

from tweepy import API
from tweepy import AppAuthHandler
from tweepy import OAuthHandler
from tweepy import Cursor
import datetime

CONSUMER_KEY = 'NHsKGfxrXTXlf2mfH2n0jbW1l'
CONSUMER_SECRET = 'W0HE0cTlfIcJtkIX5hClcH4ILgyv018Q8fWdo0sgRo5bdFzAMA'
ACCESS_TOKEN = '339641100-VOI2SsKVbSsQIfnHNSDohSJ4aB9rJpSXkDeYaeo3'
ACCESS_SECRET = 'wMUjClr78yjlsyWIjxVunFKQ8zYOjlzgMfItuRiec5Y3c'

auth = AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
api = API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
import tweepy

# richiesta su frienships
out = []
for i, user_id in enumerate(user_ids[:10]):
    print(i,user_ids[i])
    out.append(api.show_friendship(source_id= user_ids[0],
                                 target_id= user_ids[i]
    ))

    
pprint(api.rate_limit_status())


api.rate_limit_status()['resources']['friendships']['/friendships/show']
# sembrerebbe che abbiamo 15 richieste ogni 15 minuti!
# ovvero una al minuto
# in 24 h il numero massimo di richieste è:
24*60
50000/1440

###########################################################
# CONTEGGI SUL NUMERO DI RICHIESTE NECESSARIE

# usando l' autenticazione di tipo utente le richieste salgono a 180
## user authentication 180 friendships show requests

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

api = tweepy.API(auth)
api.rate_limit_status()['resources']['friendships']['/friendships/show']['limit']

# in 24h abbiamo:
n_account= 1 # al momento abbiamo un solo account, possiamo provare ad usarne di piú
finestre = 24*4 # finestre temporali di 15 minuti di richieste
richieste_24h = 180*finestre*n_account
richieste_24h

n_id = 2000 # numero di utenti unici
coppie = n_id*(n_id-1)/2
giorni_necessari = coppie/richieste_24h
giorni_necessari

###########################################################

reset = api.rate_limit_status()['resources']['friendships']['/friendships/show']['reset']
reset = datetime.datetime.fromtimestamp(int(reset))


# richiesta su frienships
out = []
for i, user_id in enumerate(user_ids[:10]):
    print(i,user_ids[i])
    out.append(api.show_friendship(source_id= user_ids[0],
                                 target_id= user_ids[i]
    ))


###########################################################
## prova richiesta degli id dei friends_count
pprint(api.rate_limit_status()['resources'])

api.rate_limit_status()['resources']['friends']['/friends/ids']

##  5000 friends per request
friends = (api.friends_ids(207323988))

friend_requests = 24*60

24*60*5000

friends
len(friends)

############################################################

# test su tweets
for tweet in tweets \
    .find(projection = ["user.name","user.friends_count","user.id"])\
    .limit(10)\
    .sort('user.friends_count', pymongo.DESCENDING ):
    pprint(tweet.values())
    

for tweet in tweets \
    .find(projection = ["user.name","user.friends_count","user.id"])\
    .limit(15000)\
    .sort('user.friends_count', pymongo.DESCENDING ):
    pprint(tweet.values())


    
    
for tweet in tweets \
    .find(projection = ["user.name","user.followers_count"])\
    .limit(10)\
    .sort('user.friends_count', pymongo.ASCENDING ):
    pprint(tweet['user']['name']\
           +" "+str(tweet['user']['followers_count'])
           )
    

###########################################################
###########################################################
###########################################################


friend_count = [ tweet['user']['friends_count']    
for tweet in tweets \
    .find(projection = ["user.name","user.friends_count"])\
    #    .limit(10)\
    .sort('user.friends_count', pymongo.DESCENDING )]



tot = np.sum(friend_count)

tot/5000


big = [friend for friend in friend_count if friend>5000]
little = [friend for friend in friend_count if friend<=5000]

len(big)
len(little)

plt.hist(big)
plt.show()

import matplotlib.pyplot as plt
import math
import numpy as np
%matplotlib qt

plt.hist(friend_count, bins= np.logspace(0,700000,10))

plt.hist(friend_count, bins= np.linspace(np.log10(1),np.log10(800000),100), color="blue")

plt.vlines(np.log10(5000),0,100)

plt.show()


plt.plot(np.log(friend_count), np.log(friend_count))
plt.show()

plt.close()

plt.clear()

###########################################################
# conteggio richieste per lista di friends
requests_24h = 24*60
utenti = 100000
n_accounts = 1

giorni_necessari = utenti/requests_24h/n_accounts
giorni_necessari
