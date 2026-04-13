"""
main.py — Full Multi-Agent Pipeline Runner
==========================================
Runs the LangGraph orchestrator on all available papers in graphrag/input/,
then saves ALL outputs (entities, relationships, programme theory) to
the /outputs/ directory for human inspection and academic reporting.
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv
from core.orchestrator import orchestrator_app
from core.state import RealistReviewState

load_dotenv()

# ── Configuration ──────────────────────────────────────────────────────────────
INPUT_DIR  = r"d:\LLM-Knowledge-Graph\graphrag\input"
OUTPUT_DIR = r"d:\LLM-Knowledge-Graph\outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Helpers ────────────────────────────────────────────────────────────────────
def save_json(data, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"  [SAVED] {path}")
    return path

def save_text(text, filename):
    path = os.path.join(OUTPUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"  [SAVED] {path}")
    return path

# ── Main Pipeline ──────────────────────────────────────────────────────────────
def run_pipeline():
    print("=" * 70)
    print("  MULTI-AGENT REALIST SYNTHESIS FRAMEWORK")
    print("  Based on: Richmond et al. (2020) — RRE 2026")
    print("=" * 70)

    # Collect all papers
    txt_files = sorted([f for f in os.listdir(INPUT_DIR) if f.endswith(".txt")])
    print(f"\n[INFO] Found {len(txt_files)} papers in graphrag/input/\n")

    all_entities      = []
    all_relationships = []
    all_cmocs         = []
    all_contradictions = []
    programme_theory  = ""

    for i, txt_name in enumerate(txt_files, 1):
        txt_path = os.path.join(INPUT_DIR, txt_name)
        print(f"\n[{i}/{len(txt_files)}] Processing: {txt_name}")
        print("-" * 60)

        with open(txt_path, "r", encoding="utf-8") as f:
            text_content = f.read()

        initial_state = RealistReviewState(
            record_id=txt_name,
            paper_text=text_content,
            extracted_cmocs=[],
            leiden_communities=[],
            validation_status="pending",
            human_feedback="",
            contradictions_found=[],
            draft_programme_theory="",
            errors=[],
            iteration_count=0
        )

        try:
            final_state = orchestrator_app.invoke(initial_state)
        except Exception as e:
            print(f"  [ERROR] {e}")
            continue

        # ── Collect Entities & Relationships ──
        cmocs = final_state.get("extracted_cmocs", [])
        for cmoc in cmocs:
            if not cmoc:
                continue
            all_cmocs.append(cmoc.dict())

            for entity in cmoc.entities:
                all_entities.append({
                    "paper":    txt_name,
                    "id":       entity.id,
                    "category": entity.category.value,
                    "label":    entity.label.value if hasattr(entity.label, 'value') else str(entity.label),
                    "text":     entity.extracted_text
                })
                print(f"  [ENTITY]  [{entity.category.value}] {entity.id}: {entity.label.value if hasattr(entity.label, 'value') else entity.label}")

            for rel in cmoc.relationships:
                all_relationships.append({
                    "paper":     txt_name,
                    "source":    rel.source_id,
                    "target":    rel.target_id,
                    "type":      rel.relation_type.value,
                    "evidence":  rel.evidence_quote
                })
                print(f"  [RELATION] {rel.source_id} --{rel.relation_type.value}--> {rel.target_id}")

        # ── Contradictions ──
        contradictions = final_state.get("contradictions_found", [])
        if contradictions:
            all_contradictions.extend(contradictions)
            print(f"  [CONTRADICTION] {len(contradictions)} found")
        else:
            print(f"  [CONTRADICTION] None found")

        # ── Programme Theory (last paper sets the overall theory) ──
        theory = final_state.get("draft_programme_theory", "")
        if theory:
            programme_theory = theory

    # ═══════════════════════════════════════════════════════════════════════════
    # SAVE ALL OUTPUTS
    # ═══════════════════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("  SAVING OUTPUTS")
    print("=" * 70)

    # 1. Entities JSON
    save_json(all_entities, "entities.json")

    # 2. Relationships JSON
    save_json(all_relationships, "relationships.json")

    # 3. Full CMOC extraction records
    save_json(all_cmocs, "cmoc_full_records.json")

    # 4. Contradictions
    save_json(all_contradictions, "contradictions.json")

    # 5. Programme Theory (readable text)
    save_text(programme_theory, "programme_theory.txt")

    # 6. Summary report (markdown)
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    summary = f"""# Extraction Summary Report
Generated: {now}

## Statistics
- Papers processed: {len(txt_files)}
- Total Entities extracted: {len(all_entities)}
- Total Relationships extracted: {len(all_relationships)}
- Contradictions found: {len(all_contradictions)}

## Entity Breakdown
"""
    from collections import Counter
    cat_counts = Counter([e["category"] for e in all_entities])
    for cat, count in cat_counts.items():
        summary += f"- {cat}: {count}\n"

    summary += f"\n## All Entities\n| # | Paper | ID | Category | Label |\n|---|-------|-----|----------|-------|\n"
    for idx, e in enumerate(all_entities, 1):
        label_short = str(e['label'])[:60] + "…" if len(str(e['label'])) > 60 else str(e['label'])
        summary += f"| {idx} | {e['paper'][:30]} | {e['id']} | {e['category']} | {label_short} |\n"

    summary += f"\n## All Relationships\n| Source | Type | Target | Evidence |\n|--------|------|--------|----------|\n"
    for r in all_relationships:
        ev_short = r['evidence'][:60] + "…" if len(r['evidence']) > 60 else r['evidence']
        summary += f"| {r['source']} | {r['type']} | {r['target']} | {ev_short} |\n"

    summary += f"\n## Final Programme Theory\n\n{programme_theory}\n"
    save_text(summary, "SUMMARY_REPORT.md")

    # ═══════════════════════════════════════════════════════════════════════════
    print("\n" + "=" * 70)
    print("  PIPELINE COMPLETE")
    print(f"  >> {len(all_entities)} Entities | {len(all_relationships)} Relationships")
    print(f"  >> All output files saved to: {OUTPUT_DIR}")
    print("=" * 70)

if __name__ == "__main__":
    run_pipeline()
