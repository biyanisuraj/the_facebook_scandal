from pymongo import MongoClient
import pymongo
import datetime

import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt


%matplotlib qt


CLIENT = MongoClient()
DB = CLIENT['social_database_test']
db = CLIENT.social_database_test

db.collection_names()

cname=db.collection_names()[0]

cname

tweets = db.tweets_17_21

tweets.count()

from pprint import pprint

pprint(tweets.find_one())

tweet_dates=[date for date in tweets.find( projection = {'tweet_created_at':1}).sort('tweet_created_at', pymongo.DESCENDING )
]

import time
import dateutil

dates_str=[]
for tweet in tweet_dates:
    dates_str.append(tweet['tweet_created_at'])

dates = [dateutil.parser.parse(date_str) for date_str in dates_str]

import numpy as np

hours = [date.hour for date in dates]
days = [date.day for date in dates]

import pandas as pd

df = pd.DataFrame({'day':days, 'hour': hours})


df_dates=df.groupby( ['day','hour'] ).agg( { 'hour': np.size } )

df_dates.describe()


import matplotlib.pyplot as plt

index = np.array(df_dates.index)

labels = ["{}-{}".format(a[0],a[1]) for a in index]

fig,ax =plt.plot(np.array(range(0,df_dates.shape[0])) , np.array( df_dates.hour) )

handles, labels = ax.get_legend_handles_labels()
ax.legend(handles, labels)

plt.scatter( labels , np.array( df_dates.hour) )
 lt.xticks(rotation=90
plt.axis('tight')
           
plt.show()
plt.close()



# Initialize the plot
fig = plt.figure()
ax = fig.add_subplot(1)


# Plot the data
ax1.bar([1,2,3],[3,4,5])
ax2.barh([0.5,1,2.5],[0,1,2])
ax2.axhline(0.45)
ax1.axvline(0.65)
ax3.scatter(x,y)

# Show the plot
plt.show()           
