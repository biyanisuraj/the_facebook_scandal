import ndlib.models.epidemics.SIModel as si
import ndlib.models.epidemics.SIRModel as sir
import ndlib.models.epidemics.SISModel as sis
import ndlib.models.epidemics.ThresholdModel as threshold
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionPrevalence import DiffusionPrevalence
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
from ndlib.viz.mpl.TrendComparison import DiffusionTrendComparison


def si_model(g, er_g, ba_g):
    print '\nSI MODEL SIMULATION'
    print 'MODEL CONFIGURATION'

    cfg = mc.Configuration()
    beta = float(raw_input('INFECTION RATE: '))
    cfg.add_model_parameter('beta', beta )
    cfg.add_model_parameter('percentage_infected',
                            float(raw_input('PERCENTAGE INFECTED: ')))
    for_comparison = dict()

    for network in [g, er_g, ba_g]:
        model_si = si.SIModel(network)
        model_si.set_initial_status(cfg)
        iterations = model_si.iteration_bunch(200)
        trends_si = model_si.build_trends(iterations)

        if network is g:
            print 'Original graph'
            model_si.name = 'G'
            viz = DiffusionTrend(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/diffusion.pdf')
            viz = DiffusionPrevalence(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/prevalence.pdf')
            for_comparison['original_si'] = [model_si, trends_si]
        elif network is er_g:
            print 'ER graph'
            model_si.name = 'ER'
            viz = DiffusionTrend(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/diffusion_er.pdf')
            viz = DiffusionPrevalence(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/prevalence_er.pdf')
            for_comparison['er_si'] = [model_si, trends_si]
        else:
            print 'BA graph'
            model_si.name = 'BA'
            viz = DiffusionTrend(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/diffusion_ba.pdf')
            viz = DiffusionPrevalence(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/prevalence_ba.pdf')
            for_comparison['ba_si'] = [model_si, trends_si]

    viz = DiffusionTrendComparison([
                            for_comparison['original_si'][0],
                            for_comparison['er_si'][0],
                            for_comparison['ba_si'][0]
                         ],
                         [
                            for_comparison['original_si'][1],
                            for_comparison['er_si'][1],
                            for_comparison['ba_si'][1]
                         ])
    viz.plot("../../report/images/spreading/si/trend_comparison_beta{}.pdf".format(beta))


def sir_model(g, er_g, ba_g, g_stat):
    print '\nSIR MODEL SIMULATION WITH GAMMA ' + g_stat.upper() + ' THAN BETA'
    print 'MODEL CONFIGURATION'

    beta = float(raw_input('INFECTION PROBABILITY: '))
    gamma = float(raw_input('REMOVAL PROBABILITY: '))

    if g_stat == 'smaller':
        while gamma >= beta:
            print 'ERROR! GAMMA HAS TO BE SMALLER THAN BETA!'
            gamma = float(raw_input('REMOVAL PROBABILITY: '))
    else:
        while gamma <= beta:
            print 'ERROR! GAMMA HAS TO BE GREATER THAN BETA!'
            gamma = float(raw_input('REMOVAL PROBABILITY: '))

    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', beta)
    cfg.add_model_parameter('gamma', gamma)
    cfg.add_model_parameter('percentage_infected',
                            float(raw_input('PERCENTAGE INFECTED: ')))

    for_comparison = dict()

    for network in [g, er_g, ba_g]:
        model_sir = sir.SIRModel(network)
        model_sir.set_initial_status(cfg)
        iterations = model_sir.iteration_bunch(200)
        trends_sir = model_sir.build_trends(iterations)

        if network is g:
            viz = DiffusionTrend(model_sir, trends_sir)
            viz.plot("../../report/images/spreading/sir/diffusion_"
                     + g_stat + ".pdf")
            for_comparison['original_sir'] = [model_sir, trends_sir]
        elif network is er_g:
            viz = DiffusionTrend(model_sir, trends_sir)
            viz.plot("../../report/images/spreading/sir/diffusion_er_"
                     + g_stat + ".pdf")
            for_comparison['er_sir'] = [model_sir, trends_sir]
        else:
            viz = DiffusionTrend(model_sir, trends_sir)
            viz.plot("../../report/images/spreading/sir/diffusion_ba_"
                     + g_stat + ".pdf")
            for_comparison['ba_sir'] = [model_sir, trends_sir]

    viz = DiffusionTrendComparison([
                            for_comparison['original_sir'][0],
                            for_comparison['er_sir'][0],
                            for_comparison['ba_sir'][0]
                         ],
                         [
                            for_comparison['original_sir'][1],
                            for_comparison['er_sir'][1],
                            for_comparison['ba_sir'][1]
                         ])
    viz.plot("../../report/images/spreading/sir/trend_comparison_"
             + g_stat + ".pdf")


def sis_model(net, graph_name):
    print '\nSIS MODEL SIMULATION - ' + graph_name + ' network'

    for_comparison = dict()
    degrees = [d for n, d in net.degree]
    mean_k = sum(degrees)/len(degrees)

    for state in ['ENDEMIC', 'FREE']:
        print 'MODEL CONFIGURATION - ' + state + ' STATE'

        if state == 'ENDEMIC':
            beta = float(raw_input('INFECTION PROBABILITY: '))
            
            print 'MU HAS TO BE LESS THAN ' + str(beta*(mean_k+1))
            mu = float(raw_input('RECOVERY PROBABILITY: '))

            while mu >= (beta*(mean_k+1)):
                print 'ERROR! MU HAS TO BE LESS THAN ' + str(beta*(mean_k+1))
                mu = float(raw_input('RECOVERY PROBABILITY: '))
        else:
            print 'MU HAS TO BE GREATER THAN ' + str(beta*(mean_k+1))
            mu = float(raw_input('RECOVERY PROBABILITY: '))

            while mu <= beta*(mean_k+1):
                print 'ERROR! MU IS NOT GREATER THAN ' + str(beta*(mean_k+1))
                mu = float(raw_input('RECOVERY PROBABILITY: '))

        cfg = mc.Configuration()
        cfg.add_model_parameter('beta', beta)
        cfg.add_model_parameter('lambda', mu)
        cfg.add_model_parameter('percentage_infected',
                                float(raw_input('PERCENTAGE INFECTED: ')))
        model_sis = sis.SISModel(net)
        model_sis.set_initial_status(cfg)
        model_sis.name = str(graph_name)+"-"+state.lower()
        print model_sis.name

        iterations = model_sis.iteration_bunch(200)
        trends_sis = model_sis.build_trends(iterations)

        viz = DiffusionTrend(model_sis, trends_sis)
        viz.plot('../../report/images/spreading/sis/diffusion_' +
                 graph_name + '_' + state.lower() + '.pdf')
        for_comparison[state.lower() + '_state'] = [model_sis, trends_sis]

    viz = DiffusionTrendComparison([for_comparison['endemic_state'][0],
                                   for_comparison['free_state'][0]],
                                   [for_comparison['endemic_state'][1],
                                   for_comparison['free_state'][1]])
    viz.plot('../../report/images/spreading/sis/diffusion_' + graph_name +
             '_comparison.pdf')


def thr_model(g, er_g, ba_g):
    print '\nTHRESHOLD MODEL SIMULATION'
    print 'MODEL CONFIGURATION'

    cfg = mc.Configuration()
    cfg.add_model_parameter('percentage_infected',
                            float(raw_input('PERCENTAGE INFECTED: ')))
    thr = float(raw_input('THRESHOLD: '))

    for_comparison = dict()

    count = 0
    labels = ['G', 'ER', 'BA']
    for network in [g, er_g, ba_g]:
        model_thr = threshold.ThresholdModel(network)
        model_thr.name = labels[count]
        print model_thr.name
        count+=1
        
        for i in network.nodes():
            cfg.add_node_configuration("threshold", i, thr)

        model_thr.set_initial_status(cfg)
        iterations = model_thr.iteration_bunch(100)
        trends_thr = model_thr.build_trends(iterations)

        if network is g:
            viz = DiffusionTrend(model_thr, trends_thr)
            viz.plot("../../report/images/spreading/threshold/diffusion.pdf")
            for_comparison['original_thr'] = [model_thr, trends_thr]
        elif network is er_g:
            viz = DiffusionTrend(model_thr, trends_thr)
            viz.plot(
                    "../../report/images/spreading/threshold/diffusion_er.pdf")
            for_comparison['er_thr'] = [model_thr, trends_thr]
        else:
            viz = DiffusionTrend(model_thr, trends_thr)
            viz.plot(
                "../../report/images/spreading/threshold/diffusion_ba.pdf")
            for_comparison['ba_thr'] = [model_thr, trends_thr]

    viz = DiffusionTrendComparison([for_comparison['original_thr'][0],
                                   for_comparison['er_thr'][0],
                                   for_comparison['ba_thr'][0]], [
                                   for_comparison['original_thr'][1],
                                   for_comparison['er_thr'][1],
                                   for_comparison['ba_thr'][1]])
    viz.plot("../../report/images/spreading/threshold/trend_comparison.pdf")


if __name__ == '__main__':
    print '\nIMPORTING NETWORKS'

    g = nx.read_edgelist('../network/networks/edge_list_reversed.txt',
                         create_using=nx.DiGraph(), nodetype=int, data=False)
    er_g = nx.read_edgelist('../network/networks/er_edge_list.txt',
                            create_using=nx.DiGraph(), nodetype=int,
                            data=False)
    ba_g = nx.read_edgelist('../network/networks/ba_edge_list.txt',
                            create_using=nx.Graph(), nodetype=int, data=False)

    model = raw_input('MODEL(si/sis/sir/thr/exit): ')

    while model != 'exit':
        if model == 'si':
            si_model(g, er_g, ba_g)
        elif model == 'sis':
            sis_model(g, 'G')
            sis_model(er_g, 'ER')
            sis_model(ba_g, 'BA')
        elif model == 'sir':
            sir_model(g, er_g, ba_g, 'smaller')
            sir_model(g, er_g, ba_g, 'greater')
        else:
            thr_model(g, er_g, ba_g)

        model = raw_input('MODEL(si/sis/sir/thr/exit): ')
