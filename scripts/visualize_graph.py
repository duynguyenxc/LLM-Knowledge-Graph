import networkx as nx
from pyvis.network import Network
import os

def generate_interactive_graph(graphml_path: str, output_html_path: str):
    print(f"Loading GraphML from {graphml_path}...")
    
    if not os.path.exists(graphml_path):
        print("Error: GraphML file not found. Ensure GraphRAG completed successfully.")
        return

    # Load the graph
    G = nx.read_graphml(graphml_path)
    print(f"Loaded graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    # Create PyVis network
    net = Network(height="100vh", width="100%", bgcolor="#222222", font_color="white", select_menu=True, filter_menu=True)
    
    # Use simpler Barnes Hut physics and disable stabilization blocking to render instantly
    net.barnes_hut(gravity=-2000, central_gravity=0.1, spring_length=200, spring_strength=0.04)
    net.toggle_physics(False) # Turn off physics so it doesn't freeze the browser calculations

    # Convert node attributes (GraphRAG outputs can be string dicts)
    for node_id, data in G.nodes(data=True):
        label = data.get("label", str(node_id))
        title = data.get("description", label)
        group = data.get("type", "Entity")
        
        # Color nodes by type
        color_map = {
            "Context": "#3498db",        # Blue
            "Intervention": "#e74c3c",   # Red
            "Mechanism_Resource": "#f1c40f", # Yellow
            "Mechanism_Response": "#e67e22", # Orange
            "Outcome": "#2ecc71",        # Green
        }
        color = color_map.get(group, "#9b59b6") # Default purple

        net.add_node(node_id, label=label[:30], title=title, group=group, color=color, size=20)

    # Convert edges
    for source, target, data in G.edges(data=True):
        label = data.get("label", "")
        weight = float(data.get("weight", 1.0))
        net.add_edge(source, target, title=label, label=label, value=weight, color="#ffffff")

    # Generate the physics and layout options dynamically
    net.show_buttons(filter_=['physics'])
    
    print(f"Generating HTML visualization at {output_html_path}...")
    net.save_graph(output_html_path)
    print("Success! Open the HTML file in your browser.")

if __name__ == "__main__":
    GRAPH_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "graph.graphml")
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "Literature_Knowledge_Graph.html")
    
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    generate_interactive_graph(GRAPH_PATH, OUTPUT_PATH)
