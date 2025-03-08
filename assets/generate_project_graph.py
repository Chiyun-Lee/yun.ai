import json
import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

with open("assets/project_graph.json", "r") as f:
    data = json.load(f)

G = nx.DiGraph()

for node in data["nodes"]:
    G.add_node(node["id"], label=node["label"])

for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"])



pos = nx.spring_layout(G, k=1, seed=42)

labels = {node["id"]: node["label"].replace(" ", "\n") for node in data["nodes"]}
nx.draw(G, pos, with_labels=True, labels=labels, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)

plt.savefig("project_graph.png", dpi=300, bbox_inches="tight")
