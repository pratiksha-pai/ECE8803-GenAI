import networkx as nx
import matplotlib.pyplot as plt

# Initialize the DAG
dag = nx.DiGraph()

# Add nodes
nodes = ["season", "atmospheric_pressure", "rain", "allergies", "grass", "umbrellas", "dog_bark", "cat_mood", "cat_hide"]
dag.add_nodes_from(nodes)

# Add connections (edges)
connections = [("season", "allergies"), ("season", "rain"), ("season", "umbrellas"),
               ("atmospheric_pressure", "rain"), 
               ("rain", "umbrellas"), ("rain", "grass"), ("rain", "dog_bark"), ("rain", "cat_mood"),
               ("dog_bark", "cat_hide"),
               ("cat_mood", "cat_hide")]

dag.add_edges_from(connections)

# Draw the DAG
pos = nx.spring_layout(dag, seed=42)
nx.draw(dag, pos, with_labels=True, node_color='lightblue', font_weight='bold', node_size=1500, font_size=15)
plt.title("Directed Acyclic Graph (DAG)")
plt.show()


# Function to find all paths between two nodes in a DAG
def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]
    if not graph.has_node(start):
        return []
    paths = []
    for node in graph.successors(start):
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
    return paths

# List all unique paths between all pairs of nodes
all_paths = {}
for start_node in nodes:
    for end_node in nodes:
        if start_node != end_node:
            paths = find_all_paths(dag, start_node, end_node)
            if paths:
                all_paths[(start_node, end_node)] = paths

all_paths
