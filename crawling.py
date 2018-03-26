import sys
import os
import jsonpickle
import tweepy

CONSUMER_KEY='INSERT-CONSUMER'
CONSUMER_SECRET = 'INSERT-SECRET'
OAUTH_TOKEN = 'INSERT-TOKEN'
OAUTH_TOKEN_SECRET = 'INSERT-TOKEN-SECRET'

from tweepy import OAuthHandler

import json as json
 
auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)

auth.set_access_token(OAUTH_TOKEN, OAUTH_TOKEN_SECRET)
 
api = tweepy.API(auth)

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

searchQuery = "#facebookgate OR \
#cambridgeanalytica OR \
#deletefacebook \
"

###########################################################

#Maximum number of tweets we want to collect 
maxTweets = 100000

#The twitter Search API allows up to 100 tweets per query
tweetsPerQry = 100

tweetCount = 0

#Open a text file to save the tweets to
with open('risultati_15_18_100k.json', 'w') as f:

    #Tell the Cursor method that we want to use the Search API (api.search)
    #Also tell Cursor our query, and the maximum number of tweets to return
    for tweet in tweepy.Cursor(api.search,q=searchQuery, since='2018-03-15',until='2018-03-18').items(maxTweets) :         

        #Write the JSON format to the text file, and add one to the number of tweets we've collected
        f.write(jsonpickle.encode(tweet._json, unpicklable=False) + '\n')
        tweetCount += 1

    #Display how many tweets we have collected
    print("Downloaded {0} tweets".format(tweetCount))

###########################################################

