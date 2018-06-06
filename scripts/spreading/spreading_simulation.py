import ndlib.models.epidemics.SIModel as si
import ndlib.models.epidemics.SIRModel as sir
import ndlib.models.epidemics.SISModel as sis
import ndlib.models.epidemics.ThresholdModel as threshold
import ndlib.models.ModelConfig as mc
import networkx as nx
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend

print 'IMPORTING NETWORKS'

g = nx.read_edgelist('../network/networks/edge_list.txt',
                     create_using=nx.DiGraph(), nodetype=int, data=False)
# er_g = nx.read_edgelist('../network/networks/er_edge_list.txt',
#                         create_using=nx.DiGraph(), nodetype=int, data=False)
# ba_g = nx.read_edgelist('../network/networks/ba_edge_list.txt',
#                         create_using=nx.Graph(), nodetype=int, data=False)

print 'SI MODEL SIMULATION'

model = si.SIModel(g)

print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('percentage_infected', 0.05)
model.set_initial_status(cfg)

iterations = model.iteration_bunch(200)
trends = model.build_trends(iterations)

viz = DiffusionTrend(model, trends)
viz.plot("si_diffusion.pdf")

print 'SIR MODEL SIMULATION'

model = sir.SIRModel(g)

print 'MODEL CONFIGURATION'

cfg = mc.Configuration()
cfg.add_model_parameter('beta', float(raw_input('INFECTION RATE: ')))
cfg.add_model_parameter('gamma', float(raw_input('RECOVERY RATE: ')))
cfg.add_model_parameter('percentage_infected', 0.05)
model.set_initial_status(cfg)

iterations = model.iteration_bunch(200)
trends = model.build_trends(iterations)

viz = DiffusionTrend(model, trends)
viz.plot("sir_diffusion.pdf")
