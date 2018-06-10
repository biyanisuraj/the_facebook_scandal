import demon as dm
import community as louvain
import networkx as nx
import pquality
import random
from collections import defaultdict
from networkx.algorithms import community
from nf1 import NF1


def extract_info(community):
    pass


def evaluate_partition(infos):
    if infos['alg'] == 'k-clique':
        results = pquality.pquality_summary(infos['network'],
                                            infos['partition'])
        results['Indexes'].to_csv(path_or_buf='./results/k_clique/indexes_' +
                                  str(infos['k']) + '.csv')
        results['Modularity'].to_csv(path_or_buf='./results/k_clique/' +
                                     'modularity_' + str(infos['k']) + '.csv')
    elif infos['alg'] == 'label propagation':
        results = pquality.pquality_summary(infos['network'],
                                            infos['partition'])
        results['Indexes'].to_csv(path_or_buf='./results/label_propagation/' +
                                  'indexes.csv')
        results['Modularity'].to_csv(path_or_buf='./results/' +
                                     'label_propagation/modularity.csv')
    elif infos['alg'] == 'louvain':
        results = pquality.pquality_summary(infos['network'],
                                            infos['partition'])
        results['Indexes'].to_csv(path_or_buf='./results/louvain/' +
                                  'indexes.csv')
        results['Modularity'].to_csv(path_or_buf='./results/' +
                                     'louvain/modularity.csv')
    elif infos['alg'] == 'girvan-newman':
        for iteration in infos['partition']:
            results = pquality.pquality_summary(infos['network'],
                                                infos['partition'][iteration])
            results['Indexes'].to_csv(path_or_buf='./results/girvan_newman/' +
                                      'iteration_' + str(iteration) +
                                      '_indexes.csv')
            results['Modularity'].to_csv(path_or_buf='./results/girvan_newman/'
                                         + 'iteration_' + str(iteration) +
                                         '_modularity.csv')
    else:
        results = pquality.pquality_summary(infos['network'],
                                            infos['partition'])
        results['Indexes'].to_csv(path_or_buf='./results/demon/indexes.csv')
        results['Modularity'].to_csv(path_or_buf='./results/demon/' +
                                     'modularity.csv')


def apply_kclique(g, subsize=1000):
    print 'COMPUTING K-CLIQUE SCORE'
    g = g.to_undirected()

    for k in [3, 4, 5]:
        kclique = list(community.k_clique_communities(g, k))
        kclique = [tuple(x) for x in kclique]

        if len(kclique) == 0:
            print 'NO COMMUNTIES FOR K = ' + str(k)
        else:
            max_len = max([len(c) for c in kclique])
            max_community = [c for c in kclique if len(c) == max_len][0]

            print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + \
                ' NODES FOR K = ' + str(k)

            extract_info(max_community)
            evaluate_partition({'alg': 'k-clique', 'network': g, 'k': k,
                               'partition': kclique})


def apply_labelprop(g, subsize=1000):
    print 'COMPUTING LABEL PROPAGATION SCORE'

    g = g.to_undirected()
    lp = list(community.label_propagation_communities(g))
    lp = [tuple(x) for x in lp]

    if len(lp) == 0:
        print 'NO COMMUNITIES FOR THE LABEL PROPAGATION ALGORITHM'
    else:
        max_len = max([len(c) for c in lp])
        max_community = [c for c in lp if len(c) == max_len][0]

        print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + ' NODES'

        extract_info(max_community)
        evaluate_partition({'alg': 'label propagation', 'network': g,
                           'partition': lp})


def apply_louvain(g, subsize=1000):
    print 'COMPUTING LOUVAIN SCORE'

    g = g.to_undirected()
    coms = louvain.best_partition(g)
    coms_to_node = defaultdict(list)

    for n, c in coms.items():
        coms_to_node[c].append(n)

    coms_louvain = [tuple(c) for c in coms_to_node.values()]

    if len(coms_louvain) == 0:
        print 'NO COMMUNITIES FOR THE LOUVAIN ALGORITHM'
    else:
        max_len = max([len(c) for c in coms_louvain])
        max_community = [c for c in coms_louvain if len(c) == max_len][0]

        print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + ' NODES'

        extract_info(max_community)
        evaluate_partition({'alg': 'louvain', 'network': g,
                           'partition': coms_louvain})


def apply_gn(g, subsize=1000):
    print 'COMPUTING GIRVAN-NEWMAN SCORE'
    ntimes = int(raw_input('ITERATIONS: '))
    iterations = dict()
    g = g.to_undirected()
    gn_hierarchy = community.girvan_newman(g)

    for i in range(ntimes):
        coms_gn = [tuple(x) for x in next(gn_hierarchy)]
        max_len = max([len(c) for c in coms_gn])
        max_community = [c for c in coms_gn if len(c) == max_len][0]

        print 'ON ITERATION ' + str(i + 1) + ' GREATEST COMMUNITY COMPOSED' \
            ' BY ' + str(max_len) + ' NODES'

        iterations[i + 1] = coms_gn

    extract_info(max_community)
    evaluate_partition({'alg': 'girvan-newman', 'network': g,
                       'partition': iterations})


def apply_demon(g, subsize=1000):
    print 'COMPUTING DEMON SCORE'
    g = g.to_undirected()
    epsilon = float(raw_input('EPSILON: '))

    d = dm.Demon(graph=g, min_community_size=3, epsilon=epsilon)
    coms_demon = d.execute()
    max_len = max([len(c) for c in coms_demon])
    max_community = [c for c in coms_demon if len(c) == max_len][0]

    print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + ' NODES'

    extract_info(max_community)
    evaluate_partition({'alg': 'demon', 'network': g,
                       'partition': coms_demon})


if __name__ == '__main__':
    print 'IMPORTING NETWORK\n'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    nodes = list(g.nodes())
    subsize = 1000
    randoms = [random.randint(0, len(nodes) - 1) for i in range(subsize)]

    apply_kclique(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)
    print '\n'
    apply_labelprop(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)
    print '\n'
    apply_louvain(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)
    print '\n'
    apply_gn(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)
    print '\n'
    apply_demon(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)

    # r_gn = r_gn[max(r_gn.keys())]['Communities']
    # res = [r_gn, r_kclique, r_louvain, r_lab, r_demon]

    # for i in range(len(res)):
    #     for j in range(i + 1, len(res)):
    #         if res[i] == r_gn:
    #             if res[j] == r_kclique:
    #                 f = open('./comparisons/gn_kclique.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #             elif res[j] == r_louvain:
    #                 f = open('./comparisons/gn_louvain.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #             elif res[j] == r_lab:
    #                 f = open('./comparisons/gn_labelprop.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #             else:
    #                 f = open('./comparisons/gn_demon.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #         elif res[i] == r_kclique:
    #             if res[j] == r_louvain:
    #                 f = open('./comparisons/kclique_louvain.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #             elif res[j] == r_lab:
    #                 f = open('./comparisons/kclique_labelprop.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #             else:
    #                 f = open('./comparisons/kclique_demon.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #         elif res[i] == r_louvain:
    #             if res[j] == r_lab:
    #                 f = open('./comparisons/louvain_labelprop.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #             else:
    #                 f = open('./comparisons/louvain_demon.txt', 'w')
    #                 f.write(str(NF1(res[i], res[j]).summary()))
    #                 f.close()
    #         elif res[i] == r_lab:
    #             f = open('./comparisons/labelprop_demon.txt', 'w')
    #             f.write(str(NF1(res[i], res[j]).summary()))
    #             f.close()
