import time
import xml.etree.ElementTree as ET

import networkx as nx

import requests


def get_suggestions(s):
    payload = {"output": "toolbar", "q": s}
    r = requests.get("http://suggestqueries.google.com/complete/search", params=payload)
    time.sleep(0.1)  # BE CAREFUL!
    tree = ET.fromstring(r.text)
    return set([x.attrib["data"].replace(s, "") for x in tree.iter("suggestion")])


def get_neighbors(s):
    suggs = get_suggestions(s)
    return set([x.lstrip() for x in suggs if x])


def update_edges(g, node, neighbors):
    for n in neighbors:
        if n not in g:
            g.add_node(n, name=n)
        if (node, n) in g.edges:
            g.get_edge_data(node, n)["weight"] += 1
        else:
            g.add_edge(node, n, weight=1)


def walk(g, s, pattern="", radius=2):
    if radius <= 0:
        return
    g.add_node(s, name=s)
    neighbors = get_neighbors(s + pattern)
    update_edges(g, s, neighbors)
    for n in neighbors:
        walk(g, n, pattern=pattern, radius=radius - 1)


def build_graph(term, pattern=" vs ", radius=2, trim_leaves=True):
    g = nx.Graph()
    walk(g, term, pattern=pattern, radius=radius)
    for x, y in g.adj.items():
        g.nodes[x]['total_weight'] = sum([y[z]['weight'] for z in y])
    if trim_leaves and radius > 1:
        remove = [node for node, degree in dict(g.degree()).items() if degree < 2]
        g.remove_nodes_from(remove)
    return g
