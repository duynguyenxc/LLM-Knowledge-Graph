import networkx as nx
import json
import os

def generate_3d_graph(graphml_path: str, output_html_path: str):
    print(f"Loading GraphML for 3D render from {graphml_path}...")
    if not os.path.exists(graphml_path):
        print("Error: GraphML not found.")
        return

    G = nx.read_graphml(graphml_path)
    print(f"Loaded graph with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

    # Prepare JSON data for 3d-force-graph
    nodes = []
    edges = []

    color_map = {
        "Context": "#3498db",        # Blue
        "Intervention": "#e74c3c",   # Red
        "Mechanism_Resource": "#f1c40f", # Yellow
        "Mechanism_Response": "#e67e22", # Orange
        "Outcome": "#2ecc71",        # Green
    }

    for node_id, data in G.nodes(data=True):
        group = data.get("type", "Entity")
        color = color_map.get(group, "#9b59b6")
        
        nodes.append({
            "id": node_id,
            "label": data.get("label", str(node_id)),
            "desc": data.get("description", ""),
            "group": group,
            "color": color
        })

    for source, target, data in G.edges(data=True):
        edges.append({
            "source": source,
            "target": target,
            "label": data.get("label", ""),
            "weight": float(data.get("weight", 1.0))
        })

    graph_data = json.dumps({"nodes": nodes, "links": edges})

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>3D Literature Knowledge Graph</title>
    <style> body {{ margin: 0; padding: 0; background-color: #111; overflow: hidden; }} </style>
    <script src="https://unpkg.com/3d-force-graph"></script>
</head>
<body>
    <div id="3d-graph"></div>

    <script>
        const gData = {graph_data};

        const elem = document.getElementById('3d-graph');

        const Graph = ForceGraph3D()(elem)
            .graphData(gData)
            .nodeLabel(node => `<div style="background: rgba(0,0,0,0.8); padding: 5px; border-radius: 4px; border: 1px solid ${{node.color}};"><b style="color: ${{node.color}};">${{node.group}}</b><br/>${{node.label}}<br/><i>${{node.desc.substring(0,100)}}...</i></div>`)
            .nodeColor(node => node.color)
            .nodeRelSize(5)
            .linkOpacity(0.2)
            .linkColor(() => 'rgba(255,255,255,0.4)')
            .linkWidth(link => link.weight * 0.5)
            .onNodeClick(node => {{
                // Aim at node from outside it
                const distance = 40;
                const distRatio = 1 + distance/Math.hypot(node.x, node.y, node.z);
                Graph.cameraPosition(
                    {{ x: node.x * distRatio, y: node.y * distRatio, z: node.z * distRatio }}, // new position
                    node, // lookAt (node)
                    3000  // ms transition duration
                );
            }});
            
    </script>
</body>
</html>
"""

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    
    print(f"Generated 3D HTML visualization at {output_html_path}")

if __name__ == "__main__":
    GRAPH_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "graph.graphml")
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "Literature_Knowledge_Graph_3D.html")
    generate_3d_graph(GRAPH_PATH, OUTPUT_PATH)
