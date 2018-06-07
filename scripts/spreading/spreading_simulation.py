import ndlib.models.epidemics.SIModel as si
import ndlib.models.epidemics.SIRModel as sir
import ndlib.models.epidemics.SISModel as sis
import ndlib.models.epidemics.ThresholdModel as threshold
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionPrevalence import DiffusionPrevalence
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend
from ndlib.viz.mpl.TrendComparison import DiffusionTrendComparison

print '\nIMPORTING NETWORKS'

g = nx.read_edgelist('../network/networks/edge_list.txt',
                     create_using=nx.DiGraph(), nodetype=int, data=False)
er_g = nx.read_edgelist('../network/networks/er_edge_list.txt',
                        create_using=nx.DiGraph(), nodetype=int, data=False)
ba_g = nx.read_edgelist('../network/networks/ba_edge_list.txt',
                        create_using=nx.Graph(), nodetype=int, data=False)

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
        viz.plot('./visuals/si/diffusion.pdf')
        viz = DiffusionPrevalence(model_si, trends_si)
        viz.plot('./visuals/si/prevalence.pdf')
        for_comparison['original_si'] = [model_si, trends_si]
    elif network is er_g:
        viz = DiffusionTrend(model_si, trends_si)
        viz.plot('./visuals/si/diffusion_er.pdf')
        viz = DiffusionPrevalence(model_si, trends_si)
        viz.plot('./visuals/si/prevalence_er.pdf')
        for_comparison['er_si'] = [model_si, trends_si]
    else:
        viz = DiffusionTrend(model_si, trends_si)
        viz.plot('./visuals/si/diffusion_ba.pdf')
        viz = DiffusionPrevalence(model_si, trends_si)
        viz.plot('./visuals/si/prevalence_ba.pdf')
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
viz.plot("./visuals/si/trend_comparison.pdf")

print '\nSIR MODEL SIMULATION'
print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('gamma', float(raw_input('RECOVERY RATE: ')))
cfg.add_model_parameter('percentage_infected',
                        float(raw_input('PERCENTAGE INFECTED: ')))

for network in [g, er_g, ba_g]:
    model_sir = sir.SIRModel(network)
    model_sir.set_initial_status(cfg)
    iterations = model_sir.iteration_bunch(200)
    trends_sir = model_sir.build_trends(iterations)

    if network is g:
        viz = DiffusionTrend(model_sir, trends_sir)
        viz.plot("./visuals/sir/diffusion.pdf")
        viz = DiffusionPrevalence(model_sir, trends_sir)
        viz.plot('./visuals/sir/prevalence.pdf')
        for_comparison['original_sir'] = [model_sir, trends_sir]
    elif network is er_g:
        viz = DiffusionTrend(model_sir, trends_sir)
        viz.plot("./visuals/sir/diffusion_er.pdf")
        viz = DiffusionPrevalence(model_sir, trends_sir)
        viz.plot('./visuals/sir/prevalence_er.pdf')
        for_comparison['er_sir'] = [model_sir, trends_sir]
    else:
        viz = DiffusionTrend(model_sir, trends_sir)
        viz.plot("./visuals/sir/diffusion_ba.pdf")
        viz = DiffusionPrevalence(model_sir, trends_sir)
        viz.plot('./visuals/sir/prevalence_ba.pdf')
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
viz.plot("./visuals/sir/trend_comparison.pdf")

print '\nSIS MODEL SIMULATION'
print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('lambda', float(raw_input('RECOVERY PROBABILITY: ')))
cfg.add_model_parameter('percentage_infected',
                        float(raw_input('PERCENTAGE INFECTED: ')))

for network in [g, er_g, ba_g]:
    model_sis = sis.SISModel(g)
    model_sis.set_initial_status(cfg)
    iterations = model_sis.iteration_bunch(200)
    trends_sis = model_sis.build_trends(iterations)

    if network is g:
        viz = DiffusionTrend(model_sis, trends_sis)
        viz.plot("./visuals/sis/diffusion.pdf")
        viz = DiffusionPrevalence(model_sis, trends_sis)
        viz.plot('./visuals/sis/prevalence.pdf')
        for_comparison['original_sis'] = [model_sis, trends_sis]
    elif network is er_g:
        viz = DiffusionTrend(model_sis, trends_sis)
        viz.plot("./visuals/sis/diffusion_er.pdf")
        viz = DiffusionPrevalence(model_sis, trends_sis)
        viz.plot('./visuals/sis/prevalence_er.pdf')
        for_comparison['er_sis'] = [model_sis, trends_sis]
    else:
        viz = DiffusionTrend(model_sis, trends_sis)
        viz.plot("./visuals/sis/diffusion_ba.pdf")
        viz = DiffusionPrevalence(model_sis, trends_sis)
        viz.plot('./visuals/sis/prevalence_ba.pdf')
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
viz.plot("./visuals/sis/trend_comparison.pdf")

print '\nTHRESHOLD MODEL SIMULATION'

model_thr = threshold.ThresholdModel(g)

print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('percentage_infected',
                        float(raw_input('PERCENTAGE INFECTED: ')))

threshold = float(raw_input('THRESHOLD: '))
for i in g.nodes():
    cfg.add_node_configuration("threshold", i, threshold)

model_thr.set_initial_status(cfg)

iterations = model_thr.iteration_bunch(200)
trends_thr = model_thr.build_trends(iterations)

viz = DiffusionTrend(model_thr, trends_thr)
viz.plot("./visuals/threshold/diffusion.pdf")
viz = DiffusionPrevalence(model_thr, trends_thr)
viz.plot('./visuals/threshold/prevalence.pdf')
