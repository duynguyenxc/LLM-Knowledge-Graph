import networkx as nx
import json
import os
import pandas as pd

def generate_dashboard(graphml_path: str, parquet_path: str, output_html_path: str, top_k=300):
    print(f"Loading GraphML for Dashboard from {graphml_path}...")
    G = nx.read_graphml(graphml_path)

    degrees = dict(G.degree())
    sorted_nodes = sorted(degrees.items(), key=lambda item: item[1], reverse=True)
    top_nodes = set([n for n, d in sorted_nodes[:top_k]])
    G_clean = G.subgraph(top_nodes)
    
    nodes = []
    edges = []

    color_map = {
        "Context": "#3498db", "Intervention": "#e74c3c", 
        "Mechanism_Resource": "#f1c40f", "Mechanism_Response": "#e67e22", 
        "Outcome": "#2ecc71"
    }

    # Load true attributes from Parquet
    print(f"Enriching nodes with metadata from {parquet_path}...")
    df = pd.read_parquet(parquet_path)
    lookup = {}
    for _, row in df.iterrows():
        title = str(row.get('title', ''))
        lookup[title] = {
            "type": str(row.get('type', 'Unknown')),
            "desc": str(row.get('description', 'No description available.'))
        }

    for node_id, data in G_clean.nodes(data=True):
        metadata = lookup.get(node_id, {"type": "Entity", "desc": "No context available."})
        group = metadata["type"]
        size = 10 + min(degrees[node_id], 30)
        
        # Build Relationships HTML
        rels_html = "<ul style='padding-left: 15px; font-size: 14px; color: #555; margin-top: 10px;'>"
        count = 0
        for src, tgt, edata in G_clean.edges(node_id, data=True):
            if count >= 20: 
                rels_html += "<li><i>...and more</i></li>"
                break
            other = tgt if src == node_id else src
            edge_label = edata.get("label", "is connected to")
            rels_html += f"<li style='margin-bottom: 5px;'><i>{edge_label}</i> <b>{other}</b></li>"
            count += 1
        rels_html += "</ul>"
        if count == 0:
            rels_html = "<p style='color: #888; font-style: italic;'>No core connections found.</p>"

        nodes.append({
            "id": node_id,
            "label": str(node_id)[:30],
            "full_name": str(node_id),
            "desc": metadata["desc"],
            "group": group,
            "color": color_map.get(group, "#9b59b6"),
            "value": size,
            "degree": degrees[node_id],
            "relations_html": rels_html
        })

    for source, target, data in G_clean.edges(data=True):
        edges.append({
            "from": source,
            "to": target,
            "label": data.get("label", ""),
            "arrows": "to"
        })

    graph_data_json = json.dumps({"nodes": nodes, "edges": edges})

    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Knowledge Graph Explorer</title>
    <script type="text/javascript" src="https://unpkg.com/vis-network/standalone/umd/vis-network.min.js"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body, html {{ height: 100%; margin: 0; padding: 0; background-color: #f8f9fa; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }}
        #wrapper {{ display: flex; height: 100vh; width: 100vw; }}
        #network_pane {{ flex: 3; height: 100%; border-right: 2px solid #ddd; background-color: #ffffff; }}
        #side_pane {{ flex: 1; height: 100%; padding: 25px; overflow-y: auto; background-color: #f1f3f5; box-shadow: -2px 0 5px rgba(0,0,0,0.05); }}
        .badge {{ font-size: 14px; margin-bottom: 15px; padding: 8px 12px; }}
        #node-title {{ font-weight: 700; font-size: 22px; color: #2c3e50; margin-bottom: 20px; border-bottom: 2px solid #ccc; padding-bottom: 10px; }}
        .info-box {{ background: white; padding: 15px; border-radius: 8px; border: 1px solid #dee2e6; }}
    </style>
</head>
<body>
    <div id="wrapper">
        <div id="network_pane"></div>
        <div id="side_pane">
            <h4 class="text-muted" style="margin-bottom: 20px;">Node Inspector</h4>
            
            <!-- Search Box -->
            <div class="input-group mb-4">
                <input type="text" id="search-box" class="form-control" placeholder="Search for a concept...">
                <button class="btn btn-outline-primary" type="button" id="search-btn">Find</button>
            </div>

            <p id="placeholder_text">Click on any node in the graph to view its detailed properties, definitions, and connections.</p>
            <div id="details_box" style="display: none;">
                <span id="node-type" class="badge bg-primary"></span>
                <div id="node-title"></div>
                
                <h6 class="text-muted">Description:</h6>
                <div class="info-box">
                    <p id="node-desc" style="line-height: 1.6; color: #495057;"></p>
                </div>
                
                <h6 class="text-muted mt-4">Graph Metrics:</h6>
                <div class="info-box" style="margin-bottom: 20px;">
                    <strong>Connections (Degree):</strong> <span id="node-degree"></span> nodes
                    <hr>
                    <strong>Connected to:</strong>
                    <div id="node-relationships" style="max-height: 250px; overflow-y: auto; background: #f8f9fa; border: 1px solid #eee; padding: 10px; border-radius: 5px;"></div>
                </div>
            </div>
        </div>
    </div>

    <script type="text/javascript">
        var raw_data = {graph_data_json};
        
        var container = document.getElementById('network_pane');
        var data = {{
            nodes: new vis.DataSet(raw_data.nodes),
            edges: new vis.DataSet(raw_data.edges)
        }};
        var options = {{
            nodes: {{
                shape: 'dot',
                font: {{ size: 14, face: 'Tahoma', color: '#333' }},
                borderWidth: 2,
                shadow: true
            }},
            edges: {{
                width: 1,
                color: {{ inherit: 'both', opacity: 0.5 }},
                smooth: {{ type: 'continuous' }}
            }},
            physics: {{
                forceAtlas2Based: {{
                    gravitationalConstant: -100,
                    centralGravity: 0.01,
                    springLength: 200,
                    springConstant: 0.08
                }},
                maxVelocity: 50,
                solver: 'forceAtlas2Based',
                timestep: 0.35,
                stabilization: {{ iterations: 150 }}
            }},
            interaction: {{
                hover: true,
                navigationButtons: true,
                keyboard: true
            }}
        }};

        var network = new vis.Network(container, data, options);

        // Click Event - Populate Side Panel
        network.on("click", function (params) {{
            if (params.nodes.length > 0) {{
                var nodeId = params.nodes[0];
                var clickedNode = data.nodes.get(nodeId);
                
                document.getElementById('placeholder_text').style.display = 'none';
                document.getElementById('details_box').style.display = 'block';
                
                // Color formatting
                document.getElementById('node-type').innerText = clickedNode.group;
                document.getElementById('node-type').style.backgroundColor = clickedNode.color;
                
                document.getElementById('node-title').innerText = clickedNode.full_name;
                document.getElementById('node-desc').innerText = clickedNode.desc;
                document.getElementById('node-degree').innerText = clickedNode.degree;
                document.getElementById('node-relationships').innerHTML = clickedNode.relations_html;
            }} else {{
                // Clicking empty space closes the panel
                document.getElementById('placeholder_text').style.display = 'block';
                document.getElementById('details_box').style.display = 'none';
            }}
        }});

        // Search Engine Feature
        document.getElementById('search-btn').addEventListener('click', function() {{
            var searchTerm = document.getElementById('search-box').value.toLowerCase();
            if (!searchTerm) return;
            
            var allNodes = data.nodes.get();
            var matchedNode = allNodes.find(n => n.full_name.toLowerCase().includes(searchTerm) || n.label.toLowerCase().includes(searchTerm));
            
            if (matchedNode) {{
                // Focus graph camera on the matched node
                network.selectNodes([matchedNode.id]);
                network.focus(matchedNode.id, {{
                    scale: 1.5,
                    animation: {{ duration: 1000, easingFunction: 'easeInOutQuad' }}
                }});
                
                // Emulate click to populate side panel
                network.emit('click', {{ nodes: [matchedNode.id] }});
            }} else {{
                alert("Concept '" + searchTerm + "' was not found in this core graph.");
            }}
        }});
        
        // Enter key support for search
        document.getElementById('search-box').addEventListener('keypress', function(e) {{
            if (e.key === 'Enter') {{
                document.getElementById('search-btn').click();
            }}
        }});
    </script>
</body>
</html>
"""

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Generated Interactive Dashboard at {output_html_path}")

if __name__ == "__main__":
    GRAPH_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "graph.graphml")
    PARQUET_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "entities.parquet")
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "Knowledge_Dashboard.html")
    generate_dashboard(GRAPH_PATH, PARQUET_PATH, OUTPUT_PATH)
