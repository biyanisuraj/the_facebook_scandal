import demon as dm
import community as louvain
import networkx as nx
import pquality
import random
from collections import defaultdict
from networkx.algorithms import community


def apply_gn(g, ntimes=5):
    print 'COMPUTING GIRVAN-NEWMAN SCORE FOR ' + str(ntimes) + ' ITERATIONS'

    results = dict()

    g = g.to_undirected()
    gn_hierarchy = community.girvan_newman(g)

    for i in range(ntimes):
        coms_gn = [tuple(x) for x in next(gn_hierarchy)]
        results[i] = pquality.pquality_summary(g, coms_gn)

    return results


def apply_kclique(g):
    g = g.to_undirected()
    k = int(raw_input('COMPUTING K-CLIQUE SCORE FOR K: '))
    kclique = list(community.k_clique_communities(g, k))
    kclique = [tuple(x) for x in kclique]

    try:
        return pquality.pquality_summary(g, kclique)
    except ValueError:
        return 'THERE ARE NO ' + str(k) + '-CLIQUES'


def apply_louvain(g):
    print 'COMPUTING LOUVAIN SCORE'

    g = g.to_undirected()
    coms = louvain.best_partition(g)
    coms_to_node = defaultdict(list)

    for n, c in coms.items():
        coms_to_node[c].append(n)

    coms_louvain = [tuple(c) for c in coms_to_node.values()]

    return pquality.pquality_summary(g, coms_louvain)


if __name__ == '__main__':
    print 'IMPORTING NETWORK'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    alg = raw_input('ALGORITHM TO APPLY(gn/kclique/louvain/demon/labelprop))'
                    ': ')
    results = None
    nodes = list(g.nodes())
    randoms = [random.randint(0, len(nodes) - 1) for i in range(1000)]

    if alg == 'gn':
        results = apply_gn(g.subgraph([nodes[r] for r in randoms]))
    elif alg == 'kclique':
        results = apply_kclique(g.subgraph([nodes[r] for r in randoms]))
    elif alg == 'louvain':
        results = apply_louvain(g.subgraph([nodes[r] for r in randoms]))
