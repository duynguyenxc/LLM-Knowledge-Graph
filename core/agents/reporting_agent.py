"""
core/agents/reporting_agent.py — Agent 9 (final): Reporting & Audit Agent
==========================================================================
Richmond Alignment: Technical Writer
Role: Generates PRISMA flow counts, structured evidence tables, programme
theory diagrams, and AERA-RRE repository-ready audit artifacts.

Human Reference: Richmond's final paper contains the full programme theory,
CMOC tables, and a transparent audit trail of 28 included studies.
"""
import os
import json
from datetime import datetime
from collections import Counter
from core.state import RealistReviewState


def generate_reporting_node(state: RealistReviewState) -> dict:
    """
    Agent 9: Reporting & Audit Agent
    INPUT:  Entire shared state (all previous agent outputs)
    OUTPUT: PRISMA report, evidence table, audit log exported to /outputs/
    """
    print("\n[AGENT 9] Reporting & Audit Agent — Generating repository artifacts...")
    print("=" * 70)

    output_dir = r"d:\LLM-Knowledge-Graph\outputs"
    os.makedirs(output_dir, exist_ok=True)
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    prisma = state.get("prisma_counts", {})
    included = state.get("included_studies", [])
    cmocs = state.get("extracted_cmocs", [])
    contradictions = state.get("contradictions_found", [])
    theory = state.get("draft_programme_theory", "Not yet synthesized.")
    audit_log = state.get("audit_log", [])
    ipt = state.get("ipt_hypothesis", "Not specified")

    # ── 1. PRISMA Flow Report ────────────────────────────────────────────────
    prisma_report = f"""# PRISMA Flow Report
Generated: {now}

## Search & Identification
- Records identified: {prisma.get('records_identified', len(included))}
- Records after deduplication: {prisma.get('records_identified', len(included))}

## Screening
- Records screened (title/abstract): {prisma.get('records_screened', len(included))}
- Records excluded at title/abstract: {prisma.get('title_abstract_excluded', 0)}
- Full texts assessed for eligibility: {prisma.get('full_texts_assessed', len(included))}
- Full texts excluded: {prisma.get('full_text_excluded', 0)}

## Included
- Studies included in synthesis: {prisma.get('studies_included', len(included))}

## Realist Review Outputs
- Total CMOCs extracted: {len(cmocs)}
- Contradictions detected: {len(contradictions)}
- Programme Theory: {'Generated' if theory else 'Pending'}
"""
    with open(os.path.join(output_dir, "PRISMA_report.md"), "w", encoding="utf-8") as f:
        f.write(prisma_report)
    print("  [SAVED] PRISMA_report.md")

    # ── 2. Evidence Table ────────────────────────────────────────────────────
    evidence_rows = []
    for cmoc in cmocs:
        if not cmoc:
            continue
        entities = {e.category.value: (e.label.value if hasattr(e.label, 'value') else str(e.label))
                    for e in cmoc.entities}
        evidence_rows.append({
            "study_id": cmoc.record_id,
            "context": entities.get("Context", "—"),
            "mechanism_resource": entities.get("Mechanism_Resource", "—"),
            "mechanism_response": entities.get("Mechanism_Response", "—"),
            "outcome": entities.get("Outcome", "—"),
            "intervention": entities.get("Intervention", "—"),
            "relationships": len(cmoc.relationships)
        })

    with open(os.path.join(output_dir, "evidence_table.json"), "w", encoding="utf-8") as f:
        json.dump(evidence_rows, f, indent=2, ensure_ascii=False)
    print("  [SAVED] evidence_table.json")

    # ── 3. Structured Evidence Table (Markdown for human reading) ────────────
    md_table = f"# Evidence Table: Extracted CMOCs\nGenerated: {now}\n\n"
    md_table += "| # | Study | Context | Mechanism Resource | Mechanism Response | Outcome |\n"
    md_table += "|---|-------|---------|-------------------|-------------------|--------|\n"
    for i, row in enumerate(evidence_rows, 1):
        ctx = row['context'][:45] + '…' if len(row['context']) > 45 else row['context']
        mr = row['mechanism_resource'][:35] + '…' if len(row['mechanism_resource']) > 35 else row['mechanism_resource']
        mrsp = row['mechanism_response'][:35] + '…' if len(row['mechanism_response']) > 35 else row['mechanism_response']
        out = row['outcome'][:35] + '…' if len(row['outcome']) > 35 else row['outcome']
        md_table += f"| {i} | {row['study_id'][:25]} | {ctx} | {mr} | {mrsp} | {out} |\n"

    with open(os.path.join(output_dir, "evidence_table.md"), "w", encoding="utf-8") as f:
        f.write(md_table)
    print("  [SAVED] evidence_table.md")

    # ── 4. Programme Theory Document ─────────────────────────────────────────
    theory_doc = f"""# Final Programme Theory
Generated: {now}

## Initial Programme Theory (IPT)
{ipt}

## Synthesized Programme Theory (Refined)
{theory}

## Contradictions Identified
{chr(10).join(f'- {c}' for c in contradictions) if contradictions else 'None detected.'}

## Demi-Regularities (Recurrent Patterns)
{chr(10).join(f'- {d}' for d in state.get('demi_regularities', [])) if state.get('demi_regularities') else 'Not yet computed.'}
"""
    with open(os.path.join(output_dir, "programme_theory_final.md"), "w", encoding="utf-8") as f:
        f.write(theory_doc)
    print("  [SAVED] programme_theory_final.md")

    # ── 5. Full Audit Trail ──────────────────────────────────────────────────
    audit_doc = f"# Full Audit Trail\nGenerated: {now}\n\n"
    for i, entry in enumerate(audit_log, 1):
        audit_doc += f"{i}. {entry}\n"

    with open(os.path.join(output_dir, "audit_trail.md"), "w", encoding="utf-8") as f:
        f.write(audit_doc)
    print("  [SAVED] audit_trail.md")

    # ── 6. Contradiction Register ─────────────────────────────────────────────
    if contradictions:
        with open(os.path.join(output_dir, "contradiction_register.md"), "w", encoding="utf-8") as f:
            f.write(f"# Contradiction Register\nGenerated: {now}\n\n")
            for i, c in enumerate(contradictions, 1):
                f.write(f"## Contradiction {i}\n{c}\n\n---\n\n")
        print("  [SAVED] contradiction_register.md")

    print("\n  All repository artifacts saved to /outputs/")
    log = f"[Reporting Agent] {len(evidence_rows)} CMOC rows, {len(contradictions)} contradictions, All artifacts exported."
    return {"audit_log": [log], "evidence_table": evidence_rows}
