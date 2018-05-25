from pymongo import MongoClient
import pymongo

CLIENT = MongoClient()
DB = CLIENT['social_database_test']
db = CLIENT.social_database_test

db.collection_names()

cname=db.collection_names()[3]
cname

tweets = db.tweets_03_25_26

for userid in tweets.find( {"id":int(user_ids[1])} , projection = {"id" : 1,'friends_count':1}).sort('friends_count', pymongo.DESCENDING ).limit(10):
    pprint(userid)

tweets.count()

from pprint import pprint

pprint(tweets.find_one())

for userid in tweets.find( projection = {"id" : 1,'friends_count':1}).sort('friends_count', pymongo.DESCENDING ).limit(10):
    pprint(userid)

user_ids = [ str(userid["id"])
             for userid in tweets.find({'friends_count': {'$gt':0}}, projection = {"id" : 1})
             .sort('friends_count', pymongo.DESCENDING )
]

len(user_ids)


import json
    
# scrivo su file gli id degli utenti
with open("scripts/crawlers/user_ids_{}.json".format(cname), 'w') as f:
    f.write(json.dumps(user_ids))

###########################################################
# CONTEGGI SUL NUMERO DI RICHIESTE NECESSARIE

friend_count = [ tweet['friends_count']    
for tweet in tweets \
    .find(projection = ["name","friends_count"])\
    ##.limit(10)\
    .sort('friends_count', pymongo.DESCENDING )]

#friend_count

requests_needed = 0
for n in friend_count:
    if(n>5000):
        requests_needed += (n/5000+1)
    else:
        requests_needed += 1

import numpy as np
tot = np.sum(friend_count)
tot/5000

# conteggio richieste per lista di friends
requests_h = 60
requests_24h = 24*60
n_accounts = 8

giorni_necessari = requests_needed/requests_24h/n_accounts
giorni_necessari

ore_necessarie = requests_needed/requests_h/n_accounts
ore_necessarie


###########################################################
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









###########################################################
###########################################################
# CONTEGGI SUL NUMERO DI RICHIESTE NECESSARIE

# usando l' autenticazione di tipo utente le richieste salgono a 180
## user authentication 180 friendships show requests

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
