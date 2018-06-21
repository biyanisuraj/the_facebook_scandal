import json
import os

##app_names=["app_testing_1","app_testing_2"]

app_1 = {"CONSUMER_KEY":'',
        "CONSUMER_SECRET":'',
        "ACCESS_TOKEN":'',
        "ACCESS_SECRET":''}

app_2 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}

app_3 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}

app_4 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}

app_5 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}


app_6 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}


app_7 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}

app_8 = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}


app_new = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}


apps_dict = {"app_1":app_1,
             "app_2":app_2,
             "app_3":app_3,
             "app_4":app_4,
             "app_5":app_5,
             "app_6":app_6,
             "app_7":app_7,
             "app_8":app_8
}

#os.getcwd()

with open("scripts/crawlers/twitter_apps.json","w") as f:
    f.write(json.dumps(apps_dict,indent=4,sort_keys=True))

with open("scripts/crawlers/twitter_apps.json","r") as f2:
    apps = json.load(f2)
    
#len(apps)
