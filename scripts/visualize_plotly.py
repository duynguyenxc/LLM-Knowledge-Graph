import networkx as nx
import plotly.graph_objects as go
import os

def generate_fast_graph(graphml_path: str, output_html_path: str, top_k=500):
    print(f"Loading GraphML from {graphml_path}...")
    G = nx.read_graphml(graphml_path)
    
    # Filter to top K nodes for performance/readability
    degrees = dict(G.degree())
    sorted_nodes = sorted(degrees.items(), key=lambda item: item[1], reverse=True)
    top_nodes = set([n for n, d in sorted_nodes[:top_k]])
    G_clean = G.subgraph(top_nodes)
    print(f"Plotting graph with {G_clean.number_of_nodes()} core concepts...")

    # Offline Layout Calculation (the heavy physics math happens HERE in Python, not the browser!)
    pos = nx.spring_layout(G_clean, k=0.5, iterations=50)

    edge_x = []
    edge_y = []
    for edge in G_clean.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])

    edge_trace = go.Scatter(
        x=edge_x, y=edge_y,
        line=dict(width=0.5, color='#888'),
        hoverinfo='none',
        mode='lines'
    )

    node_x = []
    node_y = []
    node_text = []
    node_color = []
    node_size = []

    color_map = {
        "Context": "#3498db", "Intervention": "#e74c3c", 
        "Mechanism_Resource": "#f1c40f", "Mechanism_Response": "#e67e22", 
        "Outcome": "#2ecc71"
    }

    for node in G_clean.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        
        data = G_clean.nodes[node]
        group = data.get("type", "Entity")
        label = data.get("label", str(node))
        size = 10 + (degrees[node] * 0.5)
        
        node_color.append(color_map.get(group, "#9b59b6"))
        node_size.append(min(size, 40))
        node_text.append(f"<b>[{group}]</b><br>{label}")

    node_trace = go.Scatter(
        x=node_x, y=node_y,
        mode='markers+text',
        textposition='top center',
        text=[text.split("<br>")[1][:15] if len(text.split("<br>")[1]) > 15 else text.split("<br>")[1] for text in node_text], # Very short visible text
        hovertext=node_text,
        hoverinfo='text',
        marker=dict(
            showscale=False,
            color=node_color,
            size=node_size,
            line_width=1
        )
    )

    fig = go.Figure(data=[edge_trace, node_trace],
             layout=go.Layout(
                title=dict(text='Fast Core Knowledge Graph (Computed Offline)', font=dict(size=16)),
                showlegend=False,
                hovermode='closest',
                margin=dict(b=20,l=5,r=5,t=40),
                paper_bgcolor='rgba(255,255,255,1)',
                plot_bgcolor='rgba(255,255,255,1)',
                xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
                yaxis=dict(showgrid=False, zeroline=False, showticklabels=False))
                )

    fig.write_html(output_html_path, auto_open=False)
    print(f"Generated ultra-fast visualization at {output_html_path}")

if __name__ == "__main__":
    GRAPH_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "graph.graphml")
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "Literature_Knowledge_Graph_UltraFast.html")
    generate_fast_graph(GRAPH_PATH, OUTPUT_PATH)
