# -*- coding: utf-8 -*-

import collections
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import os
import random


def general_info(g, er_g, ba_g):
    print '\nOriginal network, nodes: ' + str(g.number_of_nodes()) + \
        ', edges: ' + str(g.number_of_edges()) + ', selfloops: ' + \
        str(g.number_of_selfloops())
    print '\nErdős–Rényi network, nodes: ' + str(er_g.number_of_nodes()) + \
        ', edges: ' + str(er_g.number_of_edges()) + ', selfloops: ' \
        + str(er_g.number_of_selfloops())
    print '\nBarabási–Albert network, nodes: ' + str(ba_g.number_of_nodes()) \
        + ', edges: ' + str(ba_g.number_of_edges()) + ', selfloops: ' + \
        str(ba_g.number_of_selfloops())


def degree_distribution_analysis(g, er_g, ba_g):
    in_degrees = collections.Counter(d for n, d in g.in_degree())
    in_degrees = [in_degrees.get(i, 0) for i in range(max(in_degrees) + 1)]
    max_d = max(list(d for n, d in g.in_degree()))
    min_d = min(list(d for n, d in g.in_degree()))

    print '\nOriginal network in-degree: max = ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in g.in_degree()))/len(list(d for n, d in g.
                                                            in_degree())))

    plt.plot(range(0, len(in_degrees)), in_degrees, '.', color='tomato',
             label='Original')

    in_degrees = collections.Counter(d for n, d in er_g.in_degree())
    in_degrees = [in_degrees.get(i, 0) for i in range(max(in_degrees) + 1)]
    max_d = max(list(d for n, d in er_g.in_degree()))
    min_d = min(list(d for n, d in er_g.in_degree()))

    print 'Erdős–Rényi network in-degree: ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in er_g.in_degree()))/len(
            list(d for n, d in er_g.in_degree())))

    plt.plot(range(0, len(in_degrees)), in_degrees, '.', color='steelblue',
             label=u'Erdős–Rényi')
    plt.loglog()

    plt.title(u'In-degree distribution')
    plt.xlabel('In-degree')
    plt.ylabel('Nodes')
    plt.legend()
    plt.savefig('./imgs/in_degree.pdf', format='pdf')
    plt.clf()

    out_degrees = collections.Counter(d for n, d in g.out_degree())
    out_degrees = [out_degrees.get(i, 0) for i in range(max(out_degrees) + 1)]
    max_d = max(list(d for n, d in g.out_degree()))
    min_d = min(list(d for n, d in g.out_degree()))

    print '\nOriginal network out-degree: max = ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in g.out_degree()))/len(list(d for n, d in g.
                                                             out_degree())))

    plt.plot(range(0, len(out_degrees)), out_degrees, '.', color='tomato',
             label='Original')

    out_degrees = collections.Counter(d for n, d in er_g.out_degree())
    out_degrees = [out_degrees.get(i, 0) for i in range(max(out_degrees) + 1)]
    max_d = max(list(d for n, d in er_g.out_degree()))
    min_d = min(list(d for n, d in er_g.out_degree()))

    print 'Erdős–Rényi network out-degree: max = ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in er_g.out_degree()))/len(
            list(d for n, d in er_g.out_degree())))

    plt.plot(range(0, len(out_degrees)), out_degrees, '.', color='steelblue',
             label=u'Erdős–Rényi')
    plt.loglog()
    plt.title(u'Out-degree distribution')
    plt.xlabel('Out-degree')
    plt.ylabel('Nodes')
    plt.legend()
    plt.savefig('./imgs/out_degree.pdf', format='pdf')
    plt.clf()

    hist = nx.degree_histogram(g)
    max_d = max(list(d for n, d in g.degree()))
    min_d = min(list(d for n, d in g.degree()))

    print '\nOriginal network degree: max = ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in g.degree()))/len(list(d for n, d in g.
                                                         degree())))

    plt.plot(range(0, len(hist)), hist, ".", color='tomato', label='Original')

    hist = nx.degree_histogram(er_g)
    max_d = max(list(d for n, d in er_g.degree()))
    min_d = min(list(d for n, d in er_g.degree()))

    print 'Erdős–Rényi network degree: max = ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in er_g.degree()))/len(list(d for n, d in er_g.
                                                            degree())))

    plt.plot(range(0, len(hist)), hist, ".", color='steelblue',
             label=u'Erdős–Rényi')

    hist = nx.degree_histogram(ba_g)
    max_d = max(list(d for n, d in ba_g.degree()))
    min_d = min(list(d for n, d in ba_g.degree()))

    print 'Barabási–Albert network degree: max = ' + str(max_d) + \
        ', min = ' + str(min_d) + ', avg = ' + \
        str(sum(list(d for n, d in ba_g.degree()))/len(list(d for n, d in ba_g.
                                                            degree())))

    plt.plot(range(0, len(hist)), hist, ".", color='deeppink',
             label=u'Barabási–Albert')

    plt.title("Degree Distribution")
    plt.xlabel("Degree")
    plt.ylabel("Nodes")
    plt.legend()
    plt.loglog()
    plt.savefig('./imgs/degree.pdf', format='pdf')
    plt.clf()


def connected_components_analysis(g, er_g, ba_g):
    if nx.is_strongly_connected(g):
        print '\nThe original network is strongly connected with ' + \
            str(nx.number_strongly_connected_components(g)) + ' strongly ' \
            'connected components'
    elif nx.is_weakly_connected(g):
        print '\nThe original network is weakly connected with ' + \
            str(nx.number_weakly_connected_components(g)) + \
            ' weakly connected components'
    else:
        print '\nThe original network is neither strongly connected nor ' + \
            'weakly connected'

    if nx.is_strongly_connected(er_g):
        print 'The Erdős–Rényi network is strongly connected with ' + \
            str(nx.number_strongly_connected_components(er_g)) + ' strongly ' \
            'connected components'
    elif nx.is_weakly_connected(er_g):
        print 'The Erdős–Rényi is weakly connected with ' + \
            str(nx.number_weakly_connected_components(er_g)) + \
            ' weakly connected components'
    else:
        print 'The Erdős–Rényi is neither strongly connected nor weakly ' + \
            'connected'

    if nx.is_connected(ba_g):
        print 'The Barabási–Albert network is connected with ' + \
            str(nx.number_connected_components(ba_g)) + \
            ' connected components'
    else:
        print 'The Barabási–Albert is not connected'

    g_weak = collections.Counter(len(c)
                                 for c in nx.weakly_connected_components(g))
    g_strong = collections.Counter(
        len(c)for c in nx.strongly_connected_components(g)
    )
    er_weak = collections.Counter(len(c) for c in nx.
                                  weakly_connected_components(er_g))
    er_strong = collections.Counter(len(c) for c in nx.
                                    strongly_connected_components(er_g))

    x_weak = list(np.union1d(g_weak.keys(), er_weak.keys()))
    x_strong = list(np.union1d(g_strong.keys(), er_strong.keys()))

    plt.subplot(211)
    plt.bar(range(len(x_weak)),
            [g_weak[k] if k in g_weak else 0 for k in x_weak],
            color='tomato', label='Orginal', alpha=.5)
    plt.bar(range(len(x_weak)),
            [er_weak[k] if k in er_weak else 0 for k in x_weak],
            color='steelblue', label=u'Erdős–Rényi', alpha=.5)
    plt.xticks(range(len(x_weak)), x_weak)
    plt.title('Weakly connected components by length')
    plt.xlabel('Lenght')
    plt.ylabel('Connected components')
    plt.legend()

    plt.subplot(212)
    plt.bar(range(len(x_strong)),
            [g_strong[k] if k in g_strong else 0 for k in x_strong],
            color='tomato', label='Original', log=True, alpha=.5)
    plt.bar(range(len(x_strong)),
            [er_strong[k] if k in er_strong else 0 for k in x_strong],
            color='steelblue', label=u'Erdős–Rényi', log=True, alpha=.5)
    plt.xticks(range(len(x_strong)), x_strong)
    plt.title('Strongly connected components by length')
    plt.xlabel('Lenght')
    plt.ylabel('Connected components')
    plt.legend()
    plt.subplots_adjust(left=0.125, right=0.9, bottom=0.1, top=1.4, wspace=0.2,
                        hspace=0.2)
    plt.tight_layout()
    plt.savefig('./imgs/connectivity.pdf', format='pdf')
    plt.clf()


def clustering_analysis(g, er_g, ba_g, subsize=1000):
    nodes = list(g.nodes())
    er_nodes = list(er_g.nodes())
    ba_nodes = list(ba_g.nodes())
    randoms = [random.randint(0, len(nodes) - 1) for i in range(1000)]

    triangles = nx.triangles(g.subgraph([nodes[r] for r in randoms]))
    clustering = nx.clustering(g.subgraph([nodes[r] for r in randoms]))

    plt.hist(sorted(triangles.values()), log=True)
    plt.title('Nodes per number of triangles')
    plt.xlabel('Triangles')
    plt.ylabel('Nodes')
    plt.tight_layout()
    plt.savefig('./imgs/triangles.pdf', format='pdf')
    plt.clf()

    plt.hist(sorted(clustering.values()), log=True, label='Unordered original',
             alpha=.6, color='tomato')
    clustering = nx.clustering(er_g.subgraph([er_nodes[r] for r in randoms]))
    plt.hist(sorted(clustering.values()), log=True, label=u'Erdős–Rényi',
             alpha=.6, color='steelblue')
    clustering = nx.clustering(ba_g.subgraph([ba_nodes[r] for r in randoms]))
    plt.hist(sorted(clustering.values()), log=True, label=u'Barabási–Albert',
             alpha=.6, color='deeppink')
    plt.title('Clustering coefficient per number of nodes on a sample of' +
              ' ' + str(subsize) + ' nodes')
    plt.xlabel('Clustering coefficient')
    plt.ylabel('Nodes')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./imgs/clustering_coefficient.pdf', format='pdf')
    plt.clf()


def density_analysis(g, er_g, ba_g):
    print "\nThe Original network's density is " + str(nx.density(g))
    print "The Erdős–Rényi network's density is " + str(nx.density(er_g))
    print "The Barabási–Albert network's density is " + str(nx.density(ba_g))


def centrality_analysis(g, er_g, ba_g, subsize=500):
    colors = {u'Original': 'tomato', u'Erdős–Rényi': 'steelblue',
              u'Barabási–Albert': 'deeppink'}
    nodes = list(g.nodes())
    er_nodes = list(er_g.nodes())
    ba_nodes = list(ba_g.nodes())
    randoms = [random.randint(0, len(nodes) - 1) for i in range(subsize)]
    degree_cent = None
    g = g.subgraph([nodes[r] for r in randoms])
    er_g = er_g.subgraph([er_nodes[r] for r in randoms])
    ba_g = ba_g.subgraph([ba_nodes[r] for r in randoms])

    for network in [u'Original', u'Erdős–Rényi', u'Barabási–Albert']:
        if network == u'Original':
            degree_cent = nx.degree_centrality(g)
        elif network == u'Erdős–Rényi':
            degree_cent = nx.degree_centrality(er_g)
        else:
            degree_cent = nx.degree_centrality(ba_g)

        degree_cent = sorted(degree_cent.values())

        plt.hist(degree_cent, color=colors[network], alpha=.3, label=network)

    plt.title('Number of nodes per degree centrality (' + str(subsize) +
              ' nodes sample)')
    plt.xticks([0., 0.25, 0.5, 0.75, 1.], ['0.', '0.25', '0.5', '0.75', '1.'])
    plt.xlabel('Degree Centrality')
    plt.ylabel('Nodes')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./imgs/degree_centrality.pdf', format='pdf')
    plt.clf()

    for network in [u'Original', u'Erdős–Rényi', u'Barabási–Albert']:
        clos_cent = None

        if network == u'Original':
            clos_cent = (nx.closeness_centrality(g))
        elif network == u'Erdős–Rényi':
            clos_cent = (nx.closeness_centrality(er_g))
        else:
            clos_cent = (nx.closeness_centrality(ba_g))

        clos_cent = sorted(clos_cent.values())

        plt.hist(clos_cent, color=colors[network], alpha=.8, label=network)

    plt.title('Number of nodes per closeness centrality on a sample of '
              + str(subsize) + ' nodes')
    plt.xticks([0., 0.25, 0.5, 0.75, 1.], ['0.', '0.25', '0.5', '0.75', '1.'])
    plt.xlabel('Closeness Centrality')
    plt.ylabel('Nodes')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./imgs/closeness_centrality.pdf', format='pdf')
    plt.clf()

    for network in [u'Original', u'Erdős–Rényi', u'Barabási–Albert']:
        bet_cent = None

        if network == u'Original':
            bet_cent = (nx.betweenness_centrality(g))
        elif network == u'Erdős–Rényi':
            bet_cent = (nx.betweenness_centrality(er_g))
        else:
            bet_cent = (nx.betweenness_centrality(ba_g))

        bet_cent = sorted(bet_cent.values())

        plt.hist(bet_cent, color=colors[network], alpha=.8, label=network)

    plt.title('Number of nodes per betweenness centrality on a sample of '
              + str(subsize) + ' nodes')
    plt.xticks([0., 0.25, 0.5, 0.75, 1.], ['0.', '0.25', '0.5', '0.75', '1.'])
    plt.xlabel('Betweenness Centrality')
    plt.ylabel('Nodes')
    plt.legend()
    plt.tight_layout()
    plt.savefig('./imgs/betweenness_centrality.pdf', format='pdf')
    plt.clf()


if __name__ == '__main__':
    g = None
    er_g = None
    ba_g = None

    print 'Importing original netowrk'.upper()
    g = nx.read_edgelist('../network/networks/edge_list.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)

    print 'Importing Erdős–Rényi network'.upper()
    if os.path.isfile('../network/networks/er_edge_list.txt'):
        er_g = nx.read_edgelist('../network/networks/er_edge_list.txt',
                                create_using=nx.DiGraph(), nodetype=int,
                                data=False)
    else:
        er_g = nx.erdos_renyi_graph(g.number_of_nodes(), 0.001, directed=True)
        nx.write_edgelist(er_g, '../network/networks/er_edge_list.txt',
                          data=False)

    print 'Importing Barabási–Albert network'.upper()
    if os.path.isfile('../network/networks/ba_edge_list.txt'):
        ba_g = nx.read_edgelist('../network/networks/ba_edge_list.txt',
                                create_using=nx.Graph(), nodetype=int,
                                data=False)
    else:
        m = random.randint(1, g.number_of_nodes() - 1)
        ba_g = nx.barabasi_albert_graph(g.number_of_nodes(),
                                        sum(list(d for n, d in g.
                                                 degree()))/len(list(
                                                    d for n, d in g.degree())))
        nx.write_edgelist(ba_g, '../network/networks/ba_edge_list.txt')

    to_do = raw_input('TO DO(gen/dgr/cc/clst/da/cen/exit): ')

    while to_do != 'exit':
        if to_do == 'gen':
            general_info(g, er_g, ba_g)
        elif to_do == 'dgr':
            degree_distribution_analysis(g, er_g, ba_g)
        elif to_do == 'cc':
            connected_components_analysis(g, er_g, ba_g)
        elif to_do == 'clst':
            clustering_analysis(g.to_undirected(), er_g.to_undirected(), ba_g)
        elif to_do == 'da':
            density_analysis(g, er_g, ba_g)
        else:
            centrality_analysis(g, er_g, ba_g)

        to_do = raw_input('TO DO(gen/dgr/cc/clst/da/cen/exit): ')
