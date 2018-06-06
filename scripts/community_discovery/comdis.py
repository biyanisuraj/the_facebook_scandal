import demon as dm
import community as louvain
import networkx as nx
import pquality
import random
from collections import defaultdict
from networkx.algorithms import community
from nf1 import NF1


def apply_gn(g, ntimes=5, subsize=1000):
    print 'COMPUTING GIRVAN-NEWMAN SCORE FOR ' + str(ntimes) + ' ITERATIONS'

    results = dict()

    g = g.to_undirected()
    gn_hierarchy = community.girvan_newman(g)

    for i in range(ntimes):
        coms_gn = [tuple(x) for x in next(gn_hierarchy)]
        results[i] = pquality.pquality_summary(g, coms_gn)

    write_results('girvan_newman', subsize, results)
    return results


def apply_kclique(g, subsize=1000):
    g = g.to_undirected()
    k = int(raw_input('COMPUTING K-CLIQUE SCORE FOR K: '))
    kclique = list(community.k_clique_communities(g, k))
    kclique = [tuple(x) for x in kclique]

    try:
        write_results('k_clique', subsize,
                      pquality.pquality_summary(g, kclique), k=k)
        return pquality.pquality_summary(g, kclique)
    except ValueError:
        return 'THERE ARE NO ' + str(k) + '-CLIQUES'


def apply_louvain(g, subsize=1000):
    print 'COMPUTING LOUVAIN SCORE'

    g = g.to_undirected()
    coms = louvain.best_partition(g)
    coms_to_node = defaultdict(list)

    for n, c in coms.items():
        coms_to_node[c].append(n)

    coms_louvain = [tuple(c) for c in coms_to_node.values()]

    write_results('louvain', subsize,
                  str(pquality.pquality_summary(g, coms_louvain)))
    return pquality.pquality_summary(g, coms_louvain)


def apply_labelprop(g, subsize=1000):
    print 'COMPUTING LABEL PROPAGATION SCORE'

    g = g.to_undirected()
    lp = list(community.label_propagation_communities(g))
    lp = [tuple(x) for x in lp]

    write_results('label_propagation', subsize,
                  pquality.pquality_summary(g, lp))
    return pquality.pquality_summary(g, lp)


def apply_demon(g, subsize=1000):
    g = g.to_undirected()
    epsilon = float(raw_input('Epsilon: '))
    d = dm.Demon(graph=g, min_community_size=3, epsilon=epsilon)
    coms_demon = d.execute()

    write_results('demon', subsize,
                  pquality.pquality_summary(g, coms_demon), epsilon=epsilon)
    return pquality.pquality_summary(g, coms_demon)


def write_results(algorithm, subsize, results, k=0, epsilon=0):
    f = open('./results/' + algorithm + '_results.txt', 'w')
    f.write('Subsize: ' + str(subsize) + '\n\n')

    if algorithm == 'girvan_newman':
        for res in results:
            f.write('Iteration: ' + str(res) + '\n')
            f.write(str(results[res]))
            f.write('\n\n')
    elif algorithm == 'k_clique':
        f.write('k: ' + str(k) + '\n\n')
        f.write(str(results))
    elif algorithm == 'demon':
        f.write('epsilon: ' + str(epsilon) + '\n\n')
        f.write(str(results))
    else:
        f.write(str(results))
    f.close()


if __name__ == '__main__':
    print 'IMPORTING NETWORK'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    alg = raw_input('ALGORITHM TO APPLY(gn/kclique/louvain/demon/labelprop/'
                    'end): ')
    nodes = list(g.nodes())
    subsize = 1000
    randoms = [random.randint(0, len(nodes) - 1) for i in range(subsize)]
    r_gn, r_kclique, r_louvain, r_lab, r_demon = None, None, None, None, None

    while alg != 'end':
        if alg == 'gn':
            r_gn = apply_gn(g.subgraph([nodes[r] for r in randoms]),
                            ntimes=5, subsize=subsize)
        elif alg == 'kclique':
            r_kclique = apply_kclique(
                                    g.subgraph([nodes[r] for r in randoms]),
                                    subsize=subsize)
        elif alg == 'louvain':
            r_louvain = apply_louvain(
                                    g.subgraph([nodes[r] for r in randoms]),
                                    subsize=subsize)
        elif alg == 'labelprop':
            r_lab = apply_labelprop(g.subgraph([nodes[r] for r in randoms]),
                                    subsize=subsize)
        else:
            r_demon = apply_demon(g.subgraph([nodes[r] for r in randoms]),
                                  subsize=subsize)

        alg = raw_input('ALGORITHM TO APPLY(gn/kclique/louvain/demon/'
                        'labelprop/end): ')

    # nf = NF1(res_lab, res_louvain)

    # print nf.summary()
