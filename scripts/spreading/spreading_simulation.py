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
    cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
    cfg.add_model_parameter('percentage_infected',
                            float(raw_input('PERCENTAGE INFECTED: ')))
    for_comparison = dict()

    for network in [g, er_g, ba_g]:
        model_si = si.SIModel(network)
        model_si.set_initial_status(cfg)
        iterations = model_si.iteration_bunch(200)
        trends_si = model_si.build_trends(iterations)

        if network is g:
            viz = DiffusionTrend(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/diffusion.pdf')
            viz = DiffusionPrevalence(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/prevalence.pdf')
            for_comparison['original_si'] = [model_si, trends_si]
        elif network is er_g:
            viz = DiffusionTrend(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/diffusion_er.pdf')
            viz = DiffusionPrevalence(model_si, trends_si)
            viz.plot('../../report/images/spreading/si/prevalence_er.pdf')
            for_comparison['er_si'] = [model_si, trends_si]
        else:
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
    viz.plot("../../report/images/spreading/si/trend_comparison.pdf")


def sir_model(g, er_g, ba_g):
    print '\nSIR MODEL SIMULATION'
    print 'MODEL CONFIGURATION'

    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
    cfg.add_model_parameter('gamma', float(raw_input('RECOVERY RATE: ')))
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
            viz.plot("../../report/images/spreading/sir/diffusion.pdf")
            viz = DiffusionPrevalence(model_sir, trends_sir)
            viz.plot('../../report/images/spreading/sir/prevalence.pdf')
            for_comparison['original_sir'] = [model_sir, trends_sir]
        elif network is er_g:
            viz = DiffusionTrend(model_sir, trends_sir)
            viz.plot("../../report/images/spreading/sir/diffusion_er.pdf")
            viz = DiffusionPrevalence(model_sir, trends_sir)
            viz.plot('../../report/images/spreading/sir/prevalence_er.pdf')
            for_comparison['er_sir'] = [model_sir, trends_sir]
        else:
            viz = DiffusionTrend(model_sir, trends_sir)
            viz.plot("../../report/images/spreading/sir/diffusion_ba.pdf")
            viz = DiffusionPrevalence(model_sir, trends_sir)
            viz.plot('../../report/images/spreading/sir/prevalence_ba.pdf')
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
    viz.plot("../../report/images/spreading/sir/trend_comparison.pdf")


def sis_model(g, er_g, ba_g):
    print '\nSIS MODEL SIMULATION'
    print 'MODEL CONFIGURATION'

    cfg = mc.Configuration()
    cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
    cfg.add_model_parameter('lambda',
                            float(raw_input('RECOVERY PROBABILITY: ')))
    cfg.add_model_parameter('percentage_infected',
                            float(raw_input('PERCENTAGE INFECTED: ')))

    for_comparison = dict()

    for network in [g, er_g, ba_g]:
        model_sis = sis.SISModel(g)
        model_sis.set_initial_status(cfg)
        iterations = model_sis.iteration_bunch(200)
        trends_sis = model_sis.build_trends(iterations)

        if network is g:
            viz = DiffusionTrend(model_sis, trends_sis)
            viz.plot("../../report/images/spreading/sis/diffusion.pdf")
            viz = DiffusionPrevalence(model_sis, trends_sis)
            viz.plot('../../report/images/spreading/sis/prevalence.pdf')
            for_comparison['original_sis'] = [model_sis, trends_sis]
        elif network is er_g:
            viz = DiffusionTrend(model_sis, trends_sis)
            viz.plot("../../report/images/spreading/sis/diffusion_er.pdf")
            viz = DiffusionPrevalence(model_sis, trends_sis)
            viz.plot('../../report/images/spreading/sis/prevalence_er.pdf')
            for_comparison['er_sis'] = [model_sis, trends_sis]
        else:
            viz = DiffusionTrend(model_sis, trends_sis)
            viz.plot("../../report/images/spreading/sis/diffusion_ba.pdf")
            viz = DiffusionPrevalence(model_sis, trends_sis)
            viz.plot('../../report/images/spreading/sis/prevalence_ba.pdf')
            for_comparison['ba_sis'] = [model_sis, trends_sis]

    viz = DiffusionTrendComparison([
                            for_comparison['original_sis'][0],
                            for_comparison['er_sis'][0],
                            for_comparison['ba_sis'][0]
                         ],
                         [
                            for_comparison['original_sis'][1],
                            for_comparison['er_sis'][1],
                            for_comparison['ba_sis'][1]
                         ])
    viz.plot("../../report/images/spreading/sis/trend_comparison.pdf")


def thr_model(g, er_g, ba_g):
    print '\nTHRESHOLD MODEL SIMULATION'
    print 'MODEL CONFIGURATION'

    cfg = mc.Configuration()
    cfg.add_model_parameter('percentage_infected',
                            float(raw_input('PERCENTAGE INFECTED: ')))
    thr = float(raw_input('THRESHOLD: '))

    for_comparison = dict()

    for network in [g, er_g, ba_g]:
        model_thr = threshold.ThresholdModel(network)

        for i in network.nodes():
            cfg.add_node_configuration("threshold", i, thr)

        model_thr.set_initial_status(cfg)
        iterations = model_thr.iteration_bunch(200)
        trends_thr = model_thr.build_trends(iterations)

        if network is g:
            viz = DiffusionTrend(model_thr, trends_thr)
            viz.plot("../../report/images/spreading/threshold/diffusion.pdf")
            viz = DiffusionPrevalence(model_thr, trends_thr)
            viz.plot('../../report/images/spreading/threshold/prevalence.pdf')
            for_comparison['original_thr'] = [model_thr, trends_thr]
        elif network is er_g:
            viz = DiffusionTrend(model_thr, trends_thr)
            viz.plot(
                    "../../report/images/spreading/threshold/diffusion_er.pdf")
            viz = DiffusionPrevalence(model_thr, trends_thr)
            viz.plot(
                '../../report/images/spreading/threshold/prevalence_er.pdf')
            for_comparison['er_thr'] = [model_thr, trends_thr]
        else:
            viz = DiffusionTrend(model_thr, trends_thr)
            viz.plot(
                "../../report/images/spreading/threshold/diffusion_ba.pdf")
            viz = DiffusionPrevalence(model_thr, trends_thr)
            viz.plot(
                '../../report/images/spreading/threshold/prevalence_ba.pdf')
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

    g = nx.read_edgelist('../network/networks/edge_list.txt',
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
            sis_model(g, er_g, ba_g)
        elif model == 'sir':
            sir_model(g, er_g, ba_g)
        else:
            thr_model(g, er_g, ba_g)

        model = raw_input('MODEL(si/sis/sir/thr/exit): ')
