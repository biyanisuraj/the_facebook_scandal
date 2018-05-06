import networkx as nx
import numpy as np
import pymongo


client = pymongo.MongoClient()
db = client['social_database_test']
collection = db[raw_input('USE COLLECTION: ')]
cursor = collection.find()

g = nx.Graph()
served_nodes = 0

for i in xrange(0, cursor.count()):
    g.add_node(i, user=cursor[i]['user']['name'])

for i in xrange(0, cursor.count()):
    t1 = np.array(cursor[i]['hashtags'])

    for j in xrange(i + 1, cursor.count()):
        t2 = np.array(cursor[j]['hashtags'])

        if len(np.intersect1d(t1, t2)) != 0:
            g.add_edge(i, j)

    served_nodes += 1

    if served_nodes % 100 == 0:
        print 'SERVED ' + str(served_nodes) + ' NODES

nx.write_gexf(g, './network.gexf')
