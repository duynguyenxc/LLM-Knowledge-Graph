import pandas as pd
import json
import os

def export_reports(parquet_path, output_md):
    print(f"Loading {parquet_path}...")
    df = pd.read_parquet(parquet_path)
    
    # Sort by Hierarchy Level (0 is highest level global summary) and then by rank
    df = df.sort_values(by=['level', 'rank'], ascending=[True, False])
    
    with open(output_md, "w", encoding="utf-8") as f:
        f.write("# 🌐 GraphRAG Community Reports Overview\n\n")
        f.write("*(Extracted from community_reports.parquet)*\n\n")
        f.write("---\n\n")

        for _, row in df.iterrows():
            title = row.get("title", f"Community {row.get('community')}")
            level = row.get("level", -1)
            rank = row.get("rank", 0)
            summary = row.get("summary", "")
            findings = row.get("findings", [])
            
            f.write(f"## Level {level} | {title} (Rank: {rank})\n")
            f.write(f"**Summary:** {summary}\n\n")
            
            # Print findings safely
            if isinstance(findings, list) and len(findings) > 0:
                f.write("### Key Findings:\n")
                for fn in findings:
                    if isinstance(fn, dict):
                        f.write(f"- **{fn.get('explanation', '')}**\n")
            f.write("\n---\n\n")
            
    print(f"Successfully exported {len(df)} community reports to {output_md}")

if __name__ == "__main__":
    PARQUET_PATH = os.path.join(os.path.dirname(__file__), "..", "outputs", "graphrag_data", "community_reports.parquet")
    OUTPUT_MD = os.path.join(os.path.dirname(__file__), "..", "outputs", "Community_Reports_Summary.md")
    export_reports(PARQUET_PATH, OUTPUT_MD)
