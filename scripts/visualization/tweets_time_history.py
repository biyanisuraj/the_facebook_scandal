from pymongo import MongoClient
import pymongo
import datetime

import numpy as np
import pandas as pd
##%matplotlib qt


CLIENT = MongoClient()
DB = CLIENT['social_database_test']
db = CLIENT.social_database_test

db.collection_names()

##cname=db.collection_names()[0]
##cname

tweets = db.merged_03_17_29

tweets.count()

from pprint import pprint
pprint(tweets.find_one())

tweet_dates=[date for date in tweets.find( projection = {'tweet_created_at':1})##.sort('tweet_created_at', pymongo.ASCENDING )
]

import time
import dateutil

dates_str=[]
for tweet in tweet_dates:
    dates_str.append(tweet['tweet_created_at'])

## parsing delle date ed ordinamento    
dates = [dateutil.parser.parse(date_str) for date_str in dates_str]

df = pd.DataFrame({"dates_str":dates_str, "dates":dates})

days=[date.day for date in df.dates]
hours=[date.hour for date in df.dates]
minutes=[date.minute for date in df.dates]

df = df.assign(day=days)
df = df.assign(hour=hours)
df = df.assign(minute=minutes)

df=df.sort_values('dates')

##df_count = df.groupby(['day','hour']).agg({'hour':np.size})

df_count = df.groupby(['day','hour']).size()

#df_sum = df.groupby(['day','hour']).()

index=df_count.index
labels = ["{}-{}:00".format(a[0],a[1]) for a in index]
xlabel = range(len(labels))



df_time=pd.DataFrame({'labels':labels,'xlabel':xlabel})
df_time.tail(200)

print(df_time.to_string())

eventi= {90:"zuckerberg message on facebook"}

end = 174

###########################################################
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt

SMALL_SIZE = 7
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=SMALL_SIZE)          # controls default text sizes
plt.rc('axes', titlesize=SMALL_SIZE)     # fontsize of the axes title
plt.rc('axes', labelsize=MEDIUM_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('ytick', labelsize=SMALL_SIZE)    # fontsize of the tick labels
plt.rc('legend', fontsize=SMALL_SIZE)    # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

###########################################################


fig, ax = plt.subplots(figsize=(10, 5))
plt.plot( xlabel, np.array(df_count) )

freq = 4
xlabel_cut = [ xlabel[i+2] for i in range(0,len(labels)-2,freq)]
labels_cut = [ labels[i+2] for i in range(0,len(labels)-2,freq)]

plt.xticks(xlabel_cut, labels_cut,rotation=70)

ax.axvline(eventi.keys(),0,1000, color = "orange")

plt.text(eventi.keys()[0], 200, eventi.values()[0], rotation=90,
         verticalalignment='bottom', color= "orange")


ax.axvline( end ,0,1000, color = "black")

##ax.axvline(100,0,1000)
plt.xlabel("Day and hour")
plt.ylabel("Number of new authors per hour")
plt.axis('tight')
fig.tight_layout()

plt.savefig("scripts/visualization/imgs/time_history.pdf")

plt.show()

plt.close()

###########################################################


