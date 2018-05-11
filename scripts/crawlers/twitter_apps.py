import json
import os

##app_names=["app_testing_1","app_testing_2"]

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

app_5 = {"CONSUMER_KEY" : 'KJRUducKTC69sd06Yyll6ho3F',
        "CONSUMER_SECRET" : 'uyz3IgwQITdXHCwkOicMmFeNYJupRoqBnfcCzPeMY8RoL58IYa',
        "ACCESS_TOKEN" : '339641100-Y2TjBQPyxLGq0y6hNawvcYakxmSxjrZa4jgoBnMo',
        "ACCESS_SECRET" : 'lOvL23Bj2AlwocffH8vK12psL5KK0GZzQxagXVJorBZxv'}


app_6 = {"CONSUMER_KEY" : 'hJCIybUWZFXxJobv1CsXXQUkT',
        "CONSUMER_SECRET" : 'YseM8C30ktOCyHixpkjxHjLkpXuM3go8tV4Ecql9uUTPuhAUdR',
        "ACCESS_TOKEN" : '339641100-s2YKMfYIYjLr7XyUom0fB0t2WoVpeiLFhRLHrhH5',
        "ACCESS_SECRET" : 'sFlnBDiM4I2oeG1XOI5tD9yce1iBWDrzsvdfkSdT8ZAcL'}


app_7 = {"CONSUMER_KEY" : 'LnkJq4mBAGGPH4XuDmC0lhn1F',
        "CONSUMER_SECRET" : 'vr5Z7jzOq3Rielf5RzT3FUzxf6awP0ipVSRmjTSzpjWBZCNSLS',
        "ACCESS_TOKEN" : '339641100-dRRsFCRkuIlLMdDnTrD0N9Fb2HoApEaGsAhEp4It',
        "ACCESS_SECRET" : 'uIQcLAAogiOmLi3YfKaAIAn3rDrmbTos9eyd6LhERit2R'}

app_8 = {"CONSUMER_KEY" : 'PoqZiobxFxtlEa8uLuOC6Wrds',
        "CONSUMER_SECRET" : 'J2sW5ecoNjV9bfjd2l3QuNyDTCBVs1wRgDbkRKVl54LGqirvvF',
        "ACCESS_TOKEN" : '339641100-U4Omsk2zOyzKMvrOqSDsuxJZ0cfiQsaqP9b5NjwL',
        "ACCESS_SECRET" : 'NXgqp9bT6BBItyyVbbk1tbbscPzEDETSonbFxu7PUICgh'}


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
