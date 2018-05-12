import json
import gzip
import networkx as nx
import numpy as np
import os
import pymongo
import sys


client = pymongo.MongoClient()
table = client['social_database_test'][raw_input('USE COLLECTION: ')]

users = list(table.find({}, {'id': 1, '_id': 0}))
ids = np.array(list(), dtype=int)

for u in users:
    ids = np.append(ids, u['id'])

g = nx.DiGraph()
scanned_files = 0

for fname in os.listdir(sys.argv[1]):
    if fname in ['Not_available_users.txt', 'log.txt', '.DS_Store']:
        continue
    else:
        cfile = gzip.open(sys.argv[1] + '/' + fname, 'r')
        jfile = json.load(cfile)
        friends = np.array(jfile['friends_ids'], dtype=int)

        intersection = np.intersect1d(ids, friends)

        if len(intersection) == 0:
            continue
        else:
            for u in intersection:
                g.add_edge(jfile['user_id'], u)

        cfile.close()

    scanned_files += 1

    if scanned_files % 1000 == 0:
        print 'SCANNED ' + str(scanned_files) + ' FILES'

print 'CREATED GRAPH WITH ' + str(len(g.nodes)) + ' NODES AND ' \
    + str(len(g.edges)) + ' EDGES'
