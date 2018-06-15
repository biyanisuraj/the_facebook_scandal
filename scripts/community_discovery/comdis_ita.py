import community as louvain
import csv
import demon as dm
import networkx as nx
import pquality
import random
from collections import Counter, defaultdict
from networkx.algorithms import community
from nf1 import NF1
from pymongo import MongoClient


CLIENT = MongoClient()
DB = CLIENT['social_database_test']
TABLE = DB['merged_03_17_25']


def extract_info(com_info):
    cursor = TABLE.find({'id': {'$in': [id for id in com_info['community']]}})
    tags = Counter()
    langs = Counter()
    info_coms = {'ncommunities': com_info['ncommunities'],
                 'maxcomlen': com_info['maxcomlen'],
                 'mincomlen': com_info['mincomlen']}

    for record in cursor:
        for tag in record['hashtags']:
            tags.update([tag])
        langs.update([record['lang']])

    with open(com_info['fname'] + 'infos.csv', 'w') as csvfile:
        fieldnames = tags.keys() + langs.keys() + ['ncommunities',
                                                   'maxcomlen', 'mincomlen']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        tags.update(langs)
        tags.update(info_coms)
        writer.writeheader()
        writer.writerow(tags)


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
        results['Indexes'].to_csv(path_or_buf='./results/demon/'
                                  + str(infos['epsilon']) + '_indexes.csv')
        results['Modularity'].to_csv(path_or_buf='./results/demon/'
                                     + str(infos['epsilon']) +
                                     '_modularity.csv')


def apply_kclique(g, subsize=1000):
    print 'COMPUTING K-CLIQUE SCORE'
    g = g.to_undirected()
    partitions = dict()

    for k in [2, 3, 4, 5]:
        print 'executing for k = {}'.format(k) 
        temp = community.k_clique_communities(g, k)
        kclique = list(temp)
        del(temp)
        import gc
        gc.collect()
        kclique = [tuple(x) for x in kclique]

        if len(kclique) == 0:
            print 'NO COMMUNITIES FOR K = ' + str(k)
        else:
            max_len = max([len(c) for c in kclique])
            min_len = min([len(c) for c in kclique])
            max_community = [c for c in kclique if len(c) == max_len][0]

            print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + \
                ' NODES FOR K = ' + str(k)

            extract_info({'community': max_community,
                          'fname': './results/k_clique/' + str(k),
                          'ncommunities': len(kclique),
                          'maxcomlen': max_len,
                          'mincomlen': min_len})
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
        min_len = min([len(c) for c in lp])
        max_community = [c for c in lp if len(c) == max_len][0]

        print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + ' NODES'

        extract_info({'community': max_community,
                      'fname': './results/label_propagation/',
                      'ncommunities': len(lp),
                      'maxcomlen': max_len,
                      'mincomlen': min_len})
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
        min_len = min([len(c) for c in coms_louvain])
        max_community = [c for c in coms_louvain if len(c) == max_len][0]

        print 'GREATEST COMMUNITY COMPOSED BY ' + str(max_len) + ' NODES'

        extract_info({'community': max_community,
                      'fname': './results/louvain/',
                      'ncommunities': len(coms_louvain),
                      'maxcomlen': max_len,
                      'mincomlen': min_len})
        evaluate_partition({'alg': 'louvain', 'network': g,
                           'partition': coms_louvain})

        return coms_louvain


def apply_gn(g, subsize=1000):
    print 'COMPUTING GIRVAN-NEWMAN SCORE'
    #ntimes = int(raw_input('ITERATIONS: '))
    ntimes = 3
    iterations = dict()
    g = g.to_undirected()
    gn_hierarchy = community.girvan_newman(g)

    for i in range(ntimes):
        coms_gn = [tuple(x) for x in next(gn_hierarchy)]
        max_len = max([len(c) for c in coms_gn])
        min_len = min([len(c) for c in coms_gn])
        max_community = [c for c in coms_gn if len(c) == max_len][0]

        print 'ON ITERATION ' + str(i + 1) + ' GREATEST COMMUNITY COMPOSED' \
            ' BY ' + str(max_len) + ' NODES'

        iterations[i + 1] = coms_gn

        extract_info({'community': max_community,
                      'fname': './results/girvan_newman/it_' + str(i + 1) +
                      '_',
                      'ncommunities': len(coms_gn),
                      'maxcomlen': max_len,
                      'mincomlen': min_len})

    evaluate_partition({'alg': 'girvan-newman', 'network': g,
                       'partition': iterations})

    return iterations


def apply_demon(g, subsize=1000):
    print 'COMPUTING DEMON SCORE'
    g = g.to_undirected()
    iterations = dict()

    for eps in [0.25, 0.50, 0.75]:
        d = dm.Demon(graph=g, min_community_size=3, epsilon=eps)
        coms_demon = d.execute()
        max_len = max([len(c) for c in coms_demon])
        min_len = min([len(c) for c in coms_demon])
        max_community = [c for c in coms_demon if len(c) == max_len][0]

        print 'FOR EPSILON ' + str(eps) + ' GREATEST COMMUNITY COMPOSED BY ' \
            + str(max_len) + ' NODES'

        extract_info({'community': max_community,
                      'fname': './results/demon/' + str(eps) + '_',
                      'ncommunities': len(coms_demon),
                      'maxcomlen': max_len,
                      'mincomlen': min_len})
        evaluate_partition({'alg': 'demon', 'network': g, 'epsilon': eps,
                            'partition': coms_demon})

        iterations[eps] = coms_demon

    return iterations


if __name__ == '__main__':
    print 'IMPORTING NETWORK\n'

    import datetime
    import time
    start = datetime.datetime.now()
    g = nx.read_edgelist('../network/networks/g_ita_edge_list_clean.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    nodes = list(g.nodes())
    print len(nodes)
    
    ##p_kclique = apply_kclique(g)
    print '\n'
    stop = datetime.datetime.now()
    timing = (stop-start).seconds/60
    print "ELAPSED TIME:" + str(timing) + " minutes"

    p_labelprop = apply_labelprop(g)
    print '\n'
    
    stop = datetime.datetime.now()
    timing = (stop-start).seconds/60
    print "ELAPSED TIME:" + str(timing) + " minutes"

    p_louvain = apply_louvain(g)
    print '\n'

    stop = datetime.datetime.now()
    timing = (stop-start).seconds/60
    print "ELAPSED TIME:" + str(timing) + " minutes"

    p_gn = apply_gn(g)
    print '\n'
    stop = datetime.datetime.now()
    timing = (stop-start).seconds/60
    print "ELAPSED TIME:" + str(timing) + " minutes"
        
    p_demon = apply_demon(g)

    stop = datetime.datetime.now()
    timing = (stop-start).seconds/60
    print "ELAPSED TIME:" + str(timing) + " minutes"
    
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
                        for iteration in ps[j]:
                            comp = NF1(ps[i][k], ps[j][iteration]).summary()
                            comp['scores'].to_csv(path_or_buf='./comparisons/'
                                                  + 'k_clique/k_clique_' +
                                                  str(k) + '_demon_' +
                                                  str(iteration) + '_scores.' +
                                                  'csv')
                            comp['details'].to_csv(path_or_buf='./comparisons/'
                                                   + 'k_clique/k_clique_' +
                                                   str(k) + '_demon_' +
                                                   str(iteration) +
                                                   '_details.csv')
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
                    for iteration in ps[j]:
                        comp = NF1(ps[i], ps[j][iteration]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/'
                                              + 'label_propagation/label_' +
                                              'propagation_demon_' +
                                              str(iteration) +
                                              '_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/'
                                               + 'label_propagation/label_' +
                                               'propagation_demon_' +
                                               str(iteration) +
                                               '_details.csv')
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
                    for iteration in ps[j]:
                        comp = NF1(ps[i], ps[j][iteration]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/'
                                              + 'louvain/louvain_demon_' +
                                              str(iteration) + '_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/'
                                               + 'louvain/louvain_demon_' +
                                               str(iteration) + '_details.csv')
            elif ps[i] == p_gn:
                for iteration in ps[i]:
                    for it in ps[j]:
                        comp = NF1(ps[i][iteration], ps[j][it]).summary()
                        comp['scores'].to_csv(path_or_buf='./comparisons/' +
                                              'girvan_newman/gn_it_' +
                                              str(iteration) +
                                              '_demon_' + str(it) +
                                              '_scores.csv')
                        comp['details'].to_csv(path_or_buf='./comparisons/' +
                                               'girvan_newman/gn_it_' +
                                               str(iteration) +
                                               '_demon_' + str(it) +
                                               '_details.csv')
