import networkx as nx
import numpy as np
import pymongo


client = pymongo.MongoClient()
db = client['social_database_test']
collection = db[raw_input('USE COLLECTION: ')]
cursor = collection.find()

g = nx.Graph()
edges = 0

for i in xrange(0, cursor.count()):
    g.add_node(i, user=cursor[i]['user']['name'])

for i in xrange(0, cursor.count()):
    t1 = np.array(cursor[i]['hashtags'])

    if len(t1) == 0:
        continue

    for j in xrange(i + 1, cursor.count()):
        t2 = np.array(cursor[j]['hashtags'])

        if len(t2) == 0:
            continue
        elif len(np.intersect1d(t1, t2)) != 0:
            g.add_edge(i, j)
            edges += 1

            if edges % 1000 == 0:
                print 'ADDED ' + str(edges) + ' EDGES - PROCESSING NODE ' \
                    + str(i)

nx.write_gexf(g, './network.gexf')
