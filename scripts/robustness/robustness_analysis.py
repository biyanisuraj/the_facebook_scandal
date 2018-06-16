from __future__ import division
import operator
import matplotlib.pyplot as plt
import networkx as nx
import random
from collections import defaultdict


def test_cc(g, tests, iterations):
    for test in tests:
        g_copy = g.copy()

        print '\nTESTING ON ' + test

        cc_on_remotion = list()

        for i in range(iterations):
            num_cc = len(sorted(nx.connected_components(g_copy), key=len,
                                reverse=True))
            cc_on_remotion.append([i + 1, num_cc])

            if test == 'RANDOM':
                nodes = list(g_copy.nodes())
                g_copy.remove_node(nodes[random.randint(0, len(nodes) - 1)])
            elif test == 'DEGREE CENTRALITY':
                dc_sorted = sorted(nx.degree_centrality(g_copy).items(),
                                   key=operator.itemgetter(1), reverse=True)
                g_copy.remove_node(dc_sorted.pop(0)[0])
            else:
                bc_sorted = sorted(nx.betweenness_centrality(g_copy).items(),
                                   key=operator.itemgetter(1), reverse=True)
                g_copy.remove_node(bc_sorted.pop(0)[0])

        plt.plot([i[0] for i in cc_on_remotion],
                 [i[1] for i in cc_on_remotion])
        plt.xticks([1, 25, 50], ['1', '25', '50'])
        plt.title(test)
        plt.xlabel('Removed Nodes')
        plt.ylabel('Connected Components')
        plt.tight_layout()
        plt.savefig('../../report/images/tie_strength/test_cc_on_'
                    + test.lower().replace(' ', '_') + '.pdf')
        plt.clf()


def failure_propagation_model(g, phis, iterations):
    failed_over_it = defaultdict(list)

    print '\nFAILURE PROPAGATION SIMULATION'

    for phi in phis:
        nx.set_node_attributes(g, 0, 'failed')
        starter = list(g.nodes())[random.randint(0, len(g.nodes) - 1)]

        print 'STARTING WITH NODE ' + str(starter) + ' AND PHI ' + str(phi)

        g.nodes[starter]['failed'] = 1
        total_failed = 1

        for i in range(iterations):
            failed = list(g.nodes())[random.randint(0, len(g.nodes) - 1)]

            if g.nodes[failed]['failed'] == 0:
                threshold = 0
                neighbors = list(g.neighbors(failed))

                if len(neighbors) != 0:
                    for neighbor in neighbors:
                        if g.nodes[neighbor]['failed'] == 1:
                            threshold += 1

                    if threshold/len(neighbors) >= phi:
                        g.nodes[failed]['failed'] = 1
                        total_failed += 1

            if i % 1000 == 0:
                print 'TOTAL FAILED: ' + str(total_failed)

            failed_over_it[phi].append([i, total_failed])

    for phi in failed_over_it:
        plt.plot([i[0] for i in failed_over_it[phi]],
                 [i[1] for i in failed_over_it[phi]],
                 label=r'$\varphi = ' + str(phi) + '$')

    plt.title('Failure propagation model')
    plt.xlabel('Iteration')
    plt.ylabel('Failed nodes')
    plt.legend()
    plt.tight_layout()
    plt.savefig('../../report/images/tie_strength/failure_propagation_model'
                '.pdf')
    plt.clf()


if __name__ == '__main__':
    print 'IMPORTING NETWORK'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)

    nodes, degrees = list(g.nodes()), [d[1] for d in list(g.degree())]
    k_max, k_min = max(degrees), min(degrees)
    gamma = 2.6
    C = 1 / sum([d**(-gamma) for d in degrees])

    fc = 1 - (1/((((gamma - 2)/(3 - gamma)) * k_min**(gamma - 2) *
              k_max**(3 - gamma)) - 1))

    print 'THE CRITICAL THRESHOLD FOR THE NETWORK IS ' + str(fc)

    fc = 1 - (C / len(nodes)**((3 - gamma)/(gamma - 1)))

    print 'THE CRITICAL THRESHOLD BASED ON THE NETWORK SIZE IS ' + str(fc)

    test_cc(g.to_undirected(), ['DEGREE CENTRALITY', 'RANDOM'], 50)
    failure_propagation_model(g, [0.01, 0.001, 0.0001], 20000)
