import sys
import os
import jsonpickle
import tweepy
import time

CONSUMER_KEY='NHsKGfxrXTXlf2mfH2n0jbW1l'
CONSUMER_SECRET = 'W0HE0cTlfIcJtkIX5hClcH4ILgyv018Q8fWdo0sgRo5bdFzAMA'
OAUTH_TOKEN = '339641100-VOI2SsKVbSsQIfnHNSDohSJ4aB9rJpSXkDeYaeo3'
OAUTH_TOKEN_SECRET = 'wMUjClr78yjlsyWIjxVunFKQ8zYOjlzgMfItuRiec5Y3c'

from tweepy import OAuthHandler

import json as json
 
##auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
#auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET) 
##api = tweepy.API(auth)

###########################################################
#Switching to application authentication
auth = tweepy.AppAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)


#Setting up new api wrapper, using authentication only
api = tweepy.API(auth, wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
 
#Error handling
if (not api):
    print ("Problem Connecting to API")
 
###########################################################
#You can check how many queries you have left using rate_limit_status() method

api.rate_limit_status()['resources']['search']


########################################################### 
#Maximum number of tweets we want to collect 
maxTweets = 1000000

#The twitter Search API allows up to 100 tweets per query

tweetCount = 0


searchQuery = "#facebookgate OR \
#cambridgeanalytica OR \
#deletefacebook OR #zuckerberg"

#searchQuery = "#zuckerberg"


day_since=22
day_to=23


start_time = time.ctime()
start=time.time()
print "Started crawling at:"
print start_time

##since='2018-04-{}'.format(day_since),
##until='2018-04-{}'.format(day_to),
##max_id = 984216689234628609
##since_id = 983801866726334465,
##since='2018-04-{}'.format(day_since)

f=open('data/risultati_{}_{}_{}.json'.format(day_since, day_to, tweetCount), 'w')
    #Tell the Cursor method that we want to use the Search API (api.search)
    #Also tell Cursor our query, and the maximum number of tweets to return
for tweet in tweepy.Cursor(api.search,q=searchQuery,
                           since='2018-04-{}'.format(day_since),
                           until='2018-04-{}'.format(day_to),
                           ##max_id   = 984010360616378373,
                           count=100).items(maxTweets) :         

    #Write the JSON format to the text file, and add one to the number of tweets we've collected
    f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
    tweetCount += 1
    
    if(tweetCount%500==0):
        f.close()
        
        print(".. downloaded tweets: {}".format(tweetCount))
        minuti=(time.time()-start)/60
        print("running_time: {:.1f} minutes".format(minuti))

        print("stream rate: {:.1f} tweet per s MAX_RATE = 50 tweet per s".format(tweetCount/minuti/60) )

        if(tweet):
            f_id=open("data/lastid.txt", 'w')
            f_id.write(str(tweet.id))
            f_id.close()
            print(tweet.text)
            print(str(tweet.created_at))
            print(str(tweet.id))
                        
        
        os.system("gzip data/*.json")
        
        
        f=open('data/risultati_{}_{}_{}.json'.format(day_since, day_to, tweetCount), 'w')
        
        
        print("now sleeping zzz")
        ##pisa time.sleep(4)
        ##home
        time.sleep(3)
        print("running again")



#Display how many tweets we have collected
print("Downloaded {0} tweets".format(tweetCount))

###########################################################

