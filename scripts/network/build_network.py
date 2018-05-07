import networkx as nx
import numpy as np
import pymongo


client = pymongo.MongoClient()
db = client['social_database_test']
collection = db[raw_input('USE COLLECTION: ')]
cursor = collection.find()

g = nx.Graph()
served_nodes = 0

print 'MAKING NODES'

for i in range(cursor.count()):
    g.add_node(i, user=cursor[i]['name'])

print 'CONNECTING NODES'
cursor = list([tweet['hashtags'] for tweet in collection.find()])

for i in range(len(cursor)):
    t1 = np.array(cursor[i])

    for j in range(i + 1, len(cursor)):
        t2 = np.array(cursor[j])

        if len(np.intersect1d(t1, t2)) != 0:
            g.add_edge(i, j)

    served_nodes += 1

    if served_nodes % 100 == 0:
        print 'SERVED ' + str(served_nodes) + ' NODES'

nx.write_edgelist(g, './edge_list.txt')
