# graphs.py
#   eschews plots (minimally focused)
# by: Noah Syrkis

# imports
import jax, json
import networkx as nx
from jax import grad
from jax.lib import xla_client


import plotly.graph_objects as go
import plotly.io as pio
import darkdetect

# plot computational graph for jax function (to Gephi).
def graphs_fn(loss_fn, params, x, y):
    x = jax.jit(loss_fn).lower(params,x, y).compile().as_text()
    def todotgraph(x):
        return xla_client._xla.hlo_module_to_dot_graph(xla_client._xla.hlo_module_from_text(x))
    with open("docs/t.dot", "w") as f:
        f.write(todotgraph(x))
    G = nx.drawing.nx_agraph.read_dot('docs/t.dot')
    for node, data in G.nodes(data=True):
        if data['label'] == 'ROOT':
            data['label'] = 'LOSS'
            continue
        label = data['label'].split('<b>')[1].split('</b><br/>')[0]
        if '.' in label:
            data['kind'] = label.split('.')[0]
            data['label'] = label
            continue
        if ' ' in label:
            data['kind'] = label.split(' ')[0]
            data['label'] = label
            continue
        else:
            data['label'] = label
        
    nx.write_gexf(G, 'docs/t.gexf')