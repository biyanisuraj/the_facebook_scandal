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
    partitions = dict()

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
            partitions[k] = kclique

    return partitions


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

        return lp


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

        return coms_louvain


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

    return iterations


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

    return coms_demon


if __name__ == '__main__':
    print 'IMPORTING NETWORK\n'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    nodes = list(g.nodes())
    subsize = 1000
    randoms = [random.randint(0, len(nodes) - 1) for i in range(subsize)]

    p_kclique = apply_kclique(g.subgraph([nodes[r] for r in randoms]),
                              subsize=subsize)
    print '\n'
    p_labelprop = apply_labelprop(g.subgraph([nodes[r] for r in randoms]),
                                  subsize=subsize)
    print '\n'
    p_louvain = apply_louvain(g.subgraph([nodes[r] for r in randoms]),
                              subsize=subsize)
    print '\n'
    p_gn = apply_gn(g.subgraph([nodes[r] for r in randoms]), subsize=subsize)
    print '\n'
    p_demon = apply_demon(g.subgraph([nodes[r] for r in randoms]),
                          subsize=subsize)

    ps = [p_kclique, p_labelprop, p_louvain, p_gn, p_demon]

    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            if ps[i] == p_kclique:
                for k in p_kclique:
                    if ps[j] == p_labelprop:
                        comp = NF1(ps[i][k], ps[j]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                              'k_clique/k_clique_' + str(k) +
                                              '_labelprop_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/' +
                                               'k_clique/k_clique_' + str(k) +
                                               '_labelprop_details.csv')
                    elif ps[j] == p_louvain:
                        comp = NF1(ps[i][k], ps[j]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                              'k_clique/k_clique_' + str(k) +
                                              '_louvain_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/' +
                                               'k_clique/k_clique_' + str(k) +
                                               '_louvain_details.csv')
                    elif ps[j] == p_gn:
                        for iteration in ps[j]:
                            comp = NF1(ps[i][k], ps[j][iteration]).summary()
                            comp['scores'].to_csv(path_or_buf='./comparisons/'
                                                  + 'k_clique/k_clique_' +
                                                  str(k) + '_gn_it_' +
                                                  str(iteration) +
                                                  '_scores.csv')
                            comp['details'].to_csv(path_or_buf='./comparisons/'
                                                   + 'k_clique/k_clique_' +
                                                   str(k) + '_gn_it_' +
                                                   str(iteration) +
                                                   '_details.csv')
                    else:
                        comp = NF1(ps[i][k], ps[j]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                              'k_clique/k_clique_' + str(k) +
                                              '_demon_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/' +
                                               'k_clique/k_clique_' + str(k) +
                                               '_demon_details.csv')
            elif ps[i] == p_labelprop:
                if ps[j] == p_louvain:
                    comp = NF1(ps[i], ps[j]).summary()
                    comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                          'label_propagation/label_' +
                                          'propagation_louvain_scores.csv')
                    comp['details'].to_csv(path_or_buf='./comparisons/' +
                                           'label_propagation/label_' +
                                           'propagation_louvain_details.csv')
                elif ps[j] == p_gn:
                    for iteration in ps[j]:
                        comp = NF1(ps[i], ps[j][iteration]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/'
                                              + 'label_propagation/label_' +
                                              'propagation_gn_it_' +
                                              str(iteration) +
                                              '_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/'
                                               + 'label_propagation/label_' +
                                               'propagation_gn_it_' +
                                               str(iteration) +
                                               '_details.csv')
                else:
                    comp = NF1(ps[i], ps[j]).summary()
                    comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                          'label_propagation/label_' +
                                          'propagation_demon_scores.csv')
                    comp['details'].to_csv(path_or_buf='./comparisons/' +
                                           'label_propagation/label_' +
                                           'propagation_demon_details.csv')
            elif ps[i] == p_louvain:
                if ps[j] == p_gn:
                    for iteration in ps[j]:
                        comp = NF1(ps[i], ps[j][iteration]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/'
                                              + 'louvain/louvain_gn_it_' +
                                              str(iteration) +
                                              '_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/'
                                               + 'louvain/louvain_gn_it_' +
                                               str(iteration) +
                                               '_details.csv')
                else:
                    comp = NF1(ps[i], ps[j]).summary()
                    comp['scores'].to_csv(path_or_buf='./comparisons/'
                                          + 'louvain/louvain_demon_scores.csv')
                    comp['details'].to_csv(path_or_buf='./comparisons/'
                                           + 'louvain/louvain_demon_details' +
                                           '.csv')
            elif ps[i] == p_gn:
                for iteration in ps[i]:
                    comp = NF1(ps[i][iteration], ps[j]).summary()
                    comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                          'girvan_newman/gn_it_' +
                                          str(iteration) + '_demon_scores.csv')
                    comp['details'].to_csv(path_or_buf='./comparisons/' +
                                           'girvan_newman/gn_it_' +
                                           str(iteration) + '_demon_details' +
                                           '.csv')
