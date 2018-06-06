import ndlib.models.epidemics.SIModel as si
import ndlib.models.epidemics.SIRModel as sir
import ndlib.models.epidemics.SISModel as sis
import ndlib.models.epidemics.ThresholdModel as threshold
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionPrevalence import DiffusionPrevalence
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend

print '\nIMPORTING NETWORKS'

g = nx.read_edgelist('../network/networks/edge_list.txt',
                     create_using=nx.DiGraph(), nodetype=int, data=False)
# er_g = nx.read_edgelist('../network/networks/er_edge_list.txt',
#                         create_using=nx.DiGraph(), nodetype=int, data=False)
# ba_g = nx.read_edgelist('../network/networks/ba_edge_list.txt',
#                         create_using=nx.Graph(), nodetype=int, data=False)

print '\nSI MODEL SIMULATION\n'

model_si = si.SIModel(g)

print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('percentage_infected', 0.05)
model_si.set_initial_status(cfg)

iterations = model_si.iteration_bunch(200)
trends_si = model_si.build_trends(iterations)

viz = DiffusionTrend(model_si, trends_si)
viz.plot('si_diffusion.pdf')
viz = DiffusionPrevalence(model_si, trends_si)
viz.plot('si_prevalence.pdf')

print '\nSIR MODEL SIMULATION\n'

model_sir = sir.SIRModel(g)

print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('gamma', float(raw_input('RECOVERY RATE: ')))
cfg.add_model_parameter('percentage_infected',
                        float(raw_input('PERCENTAGE INFECTED: ')))
model_sir.set_initial_status(cfg)

iterations = model_sir.iteration_bunch(200)
trends_sir = model_sir.build_trends(iterations)

viz = DiffusionTrend(model_sir, trends_sir)
viz.plot("sir_diffusion.pdf")
viz = DiffusionPrevalence(model_sir, trends_sir)
viz.plot('sir_prevalence.pdf')

print '\nSIS MODEL SIMULATION\n'

model_sis = sis.SISModel(g)

print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('lambda', float(raw_input('RECOVERY PROBABILITY: ')))
cfg.add_model_parameter('percentage_infected',
                        float(raw_input('PERCENTAGE INFECTED: ')))
model_sis.set_initial_status(cfg)

iterations = model_sis.iteration_bunch(200)
trends_sis = model_sis.build_trends(iterations)

viz = DiffusionTrend(model_sis, trends_sis)
viz.plot("sis_diffusion.pdf")
viz = DiffusionPrevalence(model_sis, trends_sis)
viz.plot('sis_prevalence.pdf')
