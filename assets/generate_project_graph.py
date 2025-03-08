import json
import networkx as nx
import matplotlib.pyplot as plt

with open("assets/project_graph.json", "r") as f:
    data = json.load(f)

G = nx.DiGraph()

for node in data["nodes"]:
    G.add_node(node["id"], label=node["label"])

for edge in data["edges"]:
    G.add_edge(edge["source"], edge["target"])


plt.figure(figsize=(6, 4))
pos = nx.spring_layout(G)
labels = {node["id"]: node["label"] for node in data["nodes"]}
nx.draw(G, pos, with_labels=True, labels=labels, node_color="lightblue", edge_color="gray", node_size=2000, font_size=10)


plt.savefig("project_graph.png", dpi=300, bbox_inches="tight")
