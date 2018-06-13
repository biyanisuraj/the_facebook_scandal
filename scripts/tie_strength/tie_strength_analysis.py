import operator
import matplotlib.pyplot as plt
import networkx as nx
import random


def test_cc_on_dc(g, iterations):
    print 'TESTING ON DEGREE CENTRALITY'

    cc_on_remotion = list()

    for i in range(iterations):
        num_cc = len(sorted(nx.connected_components(g), key=len, reverse=True))
        cc_on_remotion.append([i + 1, num_cc])

        dc_sorted = sorted(nx.degree_centrality(g).items(),
                           key=operator.itemgetter(1), reverse=True)

        g.remove_node(dc_sorted.pop(0)[0])

    plt.plot([i[0] for i in cc_on_remotion],
             [i[1] for i in cc_on_remotion])
    plt.xticks([1, 25, 50], ['1', '25', '50'])
    plt.title('Number of connected components per nodes removed by'
              ' degree centrality')
    plt.xlabel('Removed Nodes')
    plt.ylabel('Connected Components')
    plt.tight_layout()
    plt.savefig('../../report/images/tie_strength/test_cc_on_dc.pdf')
    plt.clf()


def test_cc_on_random(g, iterations):
    print 'TESTING ON RANDOM'

    cc_on_remotion = list()

    for i in range(iterations):
        num_cc = len(sorted(nx.connected_components(g), key=len, reverse=True))
        cc_on_remotion.append([i + 1, num_cc])

        nodes = list(g.nodes())
        g.remove_node(nodes[random.randint(0, len(nodes) - 1)])

    plt.plot([i[0] for i in cc_on_remotion],
             [i[1] for i in cc_on_remotion])
    plt.xticks([1, 25, 50], ['1', '25', '50'])
    plt.title('Number of connected components per nodes removed at random')
    plt.xlabel('Removed Nodes')
    plt.ylabel('Connected Components')
    plt.tight_layout()
    plt.savefig('../../report/images/tie_strength/test_cc_on_random.pdf')
    plt.clf()


if __name__ == '__main__':
    print 'IMPORTING NETWORK'

    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)

    test_cc_on_dc(g.to_undirected(), 50)
    test_cc_on_random(g.to_undirected(), 50)
