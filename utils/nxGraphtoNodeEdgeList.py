import networkx as nx
from networkx.readwrite import json_graph
import json
import csv

__all__ = ['GraphtoCSV']

def GraphtoCSV(nxGraph, node_keys=['id'], edge_keys=['source','target'], measures=None):
    """convert nxGraph to a node list and edge list
    :param node_keys: is a list of keys in node json
    :param edge_keys: is a list of keys in edge json
    :param measures: is a the name of a centrality measure in networkx, 
    e.g. 'betweenness_centrality', or any measure that returns scores for nodes
    returns two CSVs, a node list and edges list with node_keys
    and edge_keys, respectively as columns."""
    data = json.loads(json_graph.dumps(nxGraph))
    nodes = data.get('nodes')
    edges = data.get('links')
    # if measures:
    #     methods = nx.__dict__#{'betweeness_centrality': nx.betweenness_centrality}
    #     props= {}
    #     for m in measures:
    #         import pdb; pdb.set_trace()
    #         score = methods[m](nxGraph)
    #         props[m] = score
    #     for node in nodes:
    #         for prop in props:
    #             node[prop] = props[prop][node['id']]

    node_f = csv.writer(open("nodes.csv", "wb+"))
    node_row = node_keys
    if measures:
        node_row = node_row + measures
    node_f.writerow(node_row)
    for n in nodes:
        node_f.writerow([n.get(key) for key in node_row])
    edge_f = csv.writer(open("edges.csv", "wb+"))
    edge_row = edge_keys
    edge_f.writerow(edge_row)
    for e in edges:
        edge_f.writerow([e.get(key) for key in edge_row])
