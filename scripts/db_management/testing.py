import os
import re

path ="data/tweets_03_17_20/"
files = os.listdir('data/tweets_03_17_20')

os.getcwd()


import gzip

results = []
for file in files:
    print file
    with gzip.open(path+file, "r") as f:
        buff = f.read()
    out=re.findall(r"975792399975936005", buff)
    if(len(out)>0):
        print("trovato!")
        results.append(file)

print(results)        


    out=re.findall(r"BREAKINGNEWS Dow takes a 440 point dive on news that #CambridgeAnalytica stole user information on 50 Million FB", buff)


## il file corrotto è: risultati_17_20_22000_old.json.gz


