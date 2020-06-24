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
        if (node, n) in g.edges:
            g.get_edge_data(node, n)["weight"] += 1
        else:
            g.add_edge(node, n, weight=1)


def walk(g, s, pattern="", radius=2):
    if radius <= 0:
        return
    neighbors = get_neighbors(s + pattern)
    update_edges(g, s, neighbors)
    for n in neighbors:
        walk(g, n, pattern=pattern, radius=radius - 1)


def build_graph(term, pattern=" vs ", radius=2):
    g = nx.Graph()
    walk(g, term, pattern=pattern, radius=radius)
    return g
