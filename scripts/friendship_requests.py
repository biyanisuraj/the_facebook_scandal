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
100000/1440

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



############################################################

# test su tweets
for tweet in tweets \
    
    .find(projection = ["user.name","user.followers_count"])\
    .limit(100)\
    .sort('user.followers_count', pymongo.DESCENDING ):
    pprint(tweet.values())
    


for tweet in tweets \
    .find(projection = ["user.name","user.followers_count"])\
    .limit(100000)\
    .sort('user.friends_count', pymongo.ASCENDING ):
    pprint(tweet['user']['name']\
           +" "+str(tweet['user']['followers_count'])
           )
    

