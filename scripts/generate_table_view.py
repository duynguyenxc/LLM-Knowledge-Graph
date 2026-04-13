import pandas as pd
import os

def generate_table_view(parquet_path: str, output_html_path: str):
    print(f"Loading data from {parquet_path}...")
    if not os.path.exists(parquet_path):
        print("Error: Parquet file not found. Have you migrated the GraphRAG output?")
        return

    # Load Parquet
    df = pd.read_parquet(parquet_path)
    
    # Filter columns to what's important
    if 'title' in df.columns and 'type' in df.columns and 'description' in df.columns:
        df = df[['title', 'type', 'description']]
    else:
        df = df.iloc[:, :3] # fallback

    # Generate HTML Table with DataTables.net for searching & sorting
    html_template = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Literature Knowledge Graph - Dictionary</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <!-- DataTables CSS -->
    <link href="https://cdn.datatables.net/1.13.6/css/dataTables.bootstrap5.min.css" rel="stylesheet">
    <style>
        body {{ padding: 20px; background-color: #f8f9fa; }}
        .header {{ margin-bottom: 30px; border-bottom: 2px solid #3498db; padding-bottom: 10px; }}
        .badge-Context {{ background-color: #3498db; }}
        .badge-Intervention {{ background-color: #e74c3c; }}
        .badge-Mechanism_Resource {{ background-color: #f1c40f; color: black; }}
        .badge-Mechanism_Response {{ background-color: #e67e22; }}
        .badge-Outcome {{ background-color: #2ecc71; }}
    </style>
</head>
<body>
    <div class="container-fluid">
        <div class="header">
            <h2>📚 Dictionary of {len(df)} Extracted Concepts</h2>
            <p class="text-muted">Search, sort, and filter all nodes extracted from your literature.</p>
        </div>
        
        <table id="entitiesTable" class="table table-striped table-hover table-bordered" style="width:100%">
            <thead class="table-dark">
                <tr>
                    <th style="width: 20%;">Concept Name</th>
                    <th style="width: 15%;">CMO Type</th>
                    <th style="width: 65%;">Description (Context/Definition)</th>
                </tr>
            </thead>
            <tbody>
"""

    for _, row in df.iterrows():
        name = str(row.get('title', ''))
        etype = str(row['type'])
        desc = str(row['description'])
        
        badge_class = f"badge-{etype}" if etype in ["Context", "Intervention", "Mechanism_Resource", "Mechanism_Response", "Outcome"] else "bg-secondary"
        
        html_template += f"""
                <tr>
                    <td><strong>{name}</strong></td>
                    <td><span class="badge {badge_class}">{etype}</span></td>
                    <td>{desc}</td>
                </tr>
"""

    html_template += """
            </tbody>
        </table>
    </div>

    <!-- jQuery -->
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <!-- Bootstrap JS -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    <!-- DataTables JS -->
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/dataTables.bootstrap5.min.js"></script>
    
    <script>
        $(document).ready(function() {
            $('#entitiesTable').DataTable({
                "pageLength": 50,
                "order": [[ 1, "asc" ]] // Sort by Type initially
            });
        });
    </script>
</body>
</html>
"""

    with open(output_html_path, "w", encoding="utf-8") as f:
        f.write(html_template)
    print(f"Generated Table View at {output_html_path}")

if __name__ == "__main__":
    PARQUET_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "entities.parquet")
    OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "Dictionary_Table_View.html")
    generate_table_view(PARQUET_PATH, OUTPUT_PATH)
