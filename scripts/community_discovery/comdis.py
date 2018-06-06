import demon as dm
import community as louvain
import networkx as nx
import pquality
import random
from collections import defaultdict
from networkx.algorithms import community
from nf1 import NF1


def apply_gn(g, subsize=1000):
    print 'COMPUTING GIRVAN-NEWMAN SCORE'
    ntimes = int(raw_input('ITERATIONS: '))

    coms = dict()
    results = dict()

    g = g.to_undirected()
    gn_hierarchy = community.girvan_newman(g)

    for i in range(ntimes):
        coms_gn = [tuple(x) for x in next(gn_hierarchy)]
        results[i] = pquality.pquality_summary(g, coms_gn)
        coms[results[i]['Modularity']['value'].values[0]] = {
            'Iteration': i, 'Communities': coms_gn}

    write_results('girvan_newman', subsize, results)
    return coms


def apply_kclique(g, subsize=1000):
    print 'COMPUTING K-CLIQUE SCORE'
    g = g.to_undirected()
    k = int(raw_input('K: '))
    kclique = list(community.k_clique_communities(g, k))
    kclique = [tuple(x) for x in kclique]

    try:
        write_results('k_clique', subsize,
                      pquality.pquality_summary(g, kclique), k=k)
        return kclique
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
    return coms_louvain


def apply_labelprop(g, subsize=1000):
    print 'COMPUTING LABEL PROPAGATION SCORE'

    g = g.to_undirected()
    lp = list(community.label_propagation_communities(g))
    lp = [tuple(x) for x in lp]

    write_results('label_propagation', subsize,
                  pquality.pquality_summary(g, lp))
    return lp


def apply_demon(g, subsize=1000):
    print 'COMPUTING DEMON SCORE'
    g = g.to_undirected()
    epsilon = float(raw_input('EPSILON: '))

    d = dm.Demon(graph=g, min_community_size=3, epsilon=epsilon)
    coms_demon = d.execute()

    write_results('demon', subsize,
                  pquality.pquality_summary(g, coms_demon), epsilon=epsilon)
    return coms_demon


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
    nodes = list(g.nodes())
    subsize = 1000
    randoms = [random.randint(0, len(nodes) - 1) for i in range(subsize)]

    r_gn = apply_gn(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)
    r_kclique = apply_kclique(g.subgraph([nodes[r] for r in randoms]),
                              subsize=subsize)
    r_louvain = apply_louvain(g.subgraph([nodes[r] for r in randoms]),
                              subsize=subsize)
    r_lab = apply_labelprop(g.subgraph([nodes[r] for r in randoms]),
                            subsize=subsize)
    r_demon = apply_demon(g.subgraph([nodes[r] for r in randoms]),
                          subsize=subsize)

    r_gn = r_gn[max(r_gn.keys())]['Communities']
    res = [r_gn, r_kclique, r_louvain, r_lab, r_demon]

    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if res[i] == r_gn:
                if res[j] == r_kclique:
                    f = open('./comparisons/gn_kclique.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
                elif res[j] == r_louvain:
                    f = open('./comparisons/gn_louvain.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
                elif res[j] == r_lab:
                    f = open('./comparisons/gn_labelprop.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
                else:
                    f = open('./comparisons/gn_demon.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
            elif res[i] == r_kclique:
                if res[j] == r_louvain:
                    f = open('./comparisons/kclique_louvain.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
                elif res[j] == r_lab:
                    f = open('./comparisons/kclique_labelprop.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
                else:
                    f = open('./comparisons/kclique_demon.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
            elif res[i] == r_louvain:
                if res[j] == r_lab:
                    f = open('./comparisons/louvain_labelprop.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
                else:
                    f = open('./comparisons/louvain_demon.txt', 'w')
                    f.write(str(NF1(res[i], res[j]).summary()))
                    f.close()
            elif res[i] == r_lab:
                f = open('./comparisons/labelprop_demon.txt', 'w')
                f.write(str(NF1(res[i], res[j]).summary()))
                f.close()
