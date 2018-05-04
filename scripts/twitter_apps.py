import json
import os

app_names=["app_testing_1","app_testing_2"]

app_1 = {"CONSUMER_KEY":'NHsKGfxrXTXlf2mfH2n0jbW1l',
        "CONSUMER_SECRET":'W0HE0cTlfIcJtkIX5hClcH4ILgyv018Q8fWdo0sgRo5bdFzAMA',
        "ACCESS_TOKEN":'339641100-VOI2SsKVbSsQIfnHNSDohSJ4aB9rJpSXkDeYaeo3',
        "ACCESS_SECRET":'wMUjClr78yjlsyWIjxVunFKQ8zYOjlzgMfItuRiec5Y3c'}

app_2 = {"CONSUMER_KEY" : 'kqxqp14kVJE955UQ9DSTzKFRL',
        "CONSUMER_SECRET" : '89VHinn2I1R2HkibqhBWOlzb5mcPdi3nKA4dOGDOVi4bfesRTl',
        "ACCESS_TOKEN" : '339641100-cmprkH4kBGxrnU5E5e2prUEEaH8e5D1ebUy0r8h8',
        "ACCESS_SECRET" : 'p13lHpBMkSqi7qoh9ilwh2gewQlFhEeY1tDYP4Ju34a8V'}

app_3 = {"CONSUMER_KEY" : 'Sa5t3dnFXUNQ0yCFFso84Un55',
        "CONSUMER_SECRET" : 'Iye8I3cwWYeifor2XoMrcnB1BzvPOknjaWfc6qzaQXce1UFKDC',
        "ACCESS_TOKEN" : '339641100-IpPn3yYLfjxFPqmB6El6njKMg3rwP2vwRQfUCJVI',
        "ACCESS_SECRET" : '7FYFQpLsb5c9eiMyU3jhJGkH50zRnodUl6qxIo7rP506Z'}

app_4 = {"CONSUMER_KEY" : 'OCYrj2ETgccfOL2gpPoXyK7Bn',
        "CONSUMER_SECRET" : 'vu55fH18A92QvO7yOR7hNRtLQlyUeXhOLy1ZoXFxuCXHuZd3RG',
        "ACCESS_TOKEN" : '339641100-3ghIS36HLWWgHYihdFEY3GLdEpOb4x7qfpqIUVGI',
        "ACCESS_SECRET" : 'G7eUp5EhG2REVRGCGrkiPe1vbD51Es15BY2TaV1lWkbcx'}



app_new = {"CONSUMER_KEY" : '',
        "CONSUMER_SECRET" : '',
        "ACCESS_TOKEN" : '',
        "ACCESS_SECRET" : ''}


apps_dict = {"app_1":app_1,
             "app_2":app_2,
             "app_3":app_3,
             "app_4":app_4
}

#os.getcwd()

with open("scripts/twitter_apps.json","w") as f:
    f.write(json.dumps(apps_dict,indent=4,sort_keys=True))

with open("scripts/twitter_apps.json","r") as f2:
    apps = json.load(f2)
    
