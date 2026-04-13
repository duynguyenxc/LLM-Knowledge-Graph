import networkx as nx
from pyvis.network import Network
import os

def generate_clean_graph(graphml_path: str, output_html_path: str, top_k=250):
    print(f"Loading GraphML from {graphml_path}...")
    if not os.path.exists(graphml_path):
        print("Error: GraphML not found.")
        return

    G = nx.read_graphml(graphml_path)
    print(f"Original graph: {G.number_of_nodes()} nodes.")

    # Sort nodes by total degree (connections) to find the most important concepts
    degrees = dict(G.degree())
    sorted_nodes = sorted(degrees.items(), key=lambda item: item[1], reverse=True)
    
    # Keep only the Top K most connected nodes to remove noise
    top_nodes = set([n for n, d in sorted_nodes[:top_k]])
    G_clean = G.subgraph(top_nodes)
    print(f"Clean graph: {G_clean.number_of_nodes()} nodes and {G_clean.number_of_edges()} edges.")

    # Create PyVis network with a clean White/Academic theme
    net = Network(height="100vh", width="100%", bgcolor="#f8f9fa", font_color="#333333", select_menu=True, filter_menu=True)
    
    # Enable pleasant physics since 250 nodes is light enough for the browser
    net.barnes_hut(gravity=-3000, central_gravity=0.3, spring_length=250, spring_strength=0.05, damping=0.09)

    color_map = {
        "Context": "#3498db",        # Blue
        "Intervention": "#e74c3c",   # Red
        "Mechanism_Resource": "#f1c40f", # Yellow
        "Mechanism_Response": "#e67e22", # Orange
        "Outcome": "#2ecc71",        # Green
    }

    # Add nodes
    for node_id, data in G_clean.nodes(data=True):
        label = data.get("label", str(node_id))
        title = data.get("description", label)
        group = data.get("type", "Entity")
        color = color_map.get(group, "#9b59b6")
        
        # Scale size based on degree
        size = 15 + (degrees[node_id] * 0.5)
        if size > 50: size = 50

        net.add_node(node_id, label=label[:35], title=f"[{group}]\n{title}", group=group, color=color, size=size)

    # Add edges
    for source, target, data in G_clean.edges(data=True):
        label = data.get("label", "")
        weight = float(data.get("weight", 1.0))
        net.add_edge(source, target, title=label, width=weight * 0.5, color="#bdc3c7")

    print(f"Generating clean HTML visualization at {output_html_path}...")
    net.save_graph(output_html_path)

if __name__ == "__main__":
    GRAPH_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "graph.graphml")
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "Literature_Knowledge_Graph_Clean.html")
    
    generate_clean_graph(GRAPH_PATH, OUTPUT_PATH, top_k=250)
