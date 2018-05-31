import demon as dm
import community as louvain
import networkx as nx
import pquality
from collections import defaultdict
from networkx.algorithms import community


def apply_gn(g):
    print 'Computing Girvan-Newman score'

    gn_hierarchy = community.girvan_newman(g)
    coms_gn = [tuple(x) for x in next(gn_hierarchy)]

    return pquality.pquality_summary(g, coms_gn)


def apply_kclique(g):
    k = int(raw_input('Computing Kclique score, k: '))
    kclique = list(community.k_clique_communities(g.to_undirected(), k))
    kclique = [tuple(x) for x in kclique]

    return pquality.pquality_summary(g, kclique)


def apply_louvain(g):
    coms = louvain.best_partition(g.to_undirected())
    coms_to_node = defaultdict(list)

    for n, c in coms.items():
        coms_to_node[c].append(n)

    coms_louvain = [tuple(c) for c in coms_to_node.values()]

    return pquality.pquality_summary(g, coms_louvain)


if __name__ == '__main__':
    print 'Importing network'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    alg = raw_input('Algorithm to apply(gn/kclique/louvain/demon/labelprop))'
                    ': ')
    results = None

    if alg == 'gn':
        results = apply_gn(g)
    elif alg == 'kclique':
        results = apply_kclique(g)
    elif alg == 'louvain':
        results = apply_louvain(g)

    print results['Modularity']
