from pymongo import MongoClient
import pymongo
import datetime

import numpy as np
import pandas as pd

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

df_sum = df.groupby(['day','hour']).()

index=df_count.index
labels = ["{}-{}".format(a[0],a[1]) for a in index]
xlabel = range(len(labels))

xlabel_cut = [range(0,len(labels),10)]

df_time=pd.DataFrame({'labels':labels,'xlabel':xlabel})


eventi= {90:"zuckerberg message on facebook"}


###########################################################
import matplotlib.pyplot as plt

SMALL_SIZE = 8
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

index = np.array(df_count.index)

fig, ax = plt.subplots(figsize=(20, 5))

plt.plot( (xlabel), np.array(df_count) )
##plt.plot( (xlabel), np.array(df_sum) )

plt.xticks(xlabel, labels,rotation=45)

ax.axvline(eventi.keys(),0,1000, color = "orange")

##ax.axvline(100,0,1000)
plt.xlabel("Day and hour")
plt.ylabel("Number of new authors per hour")

plt.axis('tight')
plt.show()


plt.close()


###########################################################


df_dates=df.groupby( ['day','hour'] ).agg( { 'hour': np.size } )
df_dates=df.groupby( ['day','hour'] ).agg( { 'hour': np.size } )




###########################################################

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
