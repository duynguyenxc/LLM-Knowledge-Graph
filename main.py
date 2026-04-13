"""
main.py — Full 10-Agent Pipeline Runner (v2)
============================================
Runs the complete Multi-Agent Realist Synthesis Framework aligned with
the Richmond et al. (2020) Human Reference Standard.

Pipeline:
  Phase 0: Protocol & IPT
  Phase 1: Study Registry Build (Deduplication)
  Phase 2: Two-Stage Screening (T/A + Full Text) with HITL CP1
  Phase 3: CMOC Extraction with HITL CP2
  Phase 4: Contradiction Detection with HITL CP3
  Phase 5: Theory Synthesis with HITL CP4
  Phase 6: Reporting & Audit Artifacts
"""

import os
import json
from datetime import datetime
from dotenv import load_dotenv

from core.orchestrator import orchestrator_app
from core.state import RealistReviewState
from core.agents.deduplication_agent import build_study_registry_from_input
from core.agents.protocol_agent import run_protocol_agent

load_dotenv()

INPUT_DIR     = r"d:\LLM-Knowledge-Graph\graphrag\input"
METADATA_FILE = r"d:\LLM-Knowledge-Graph\data\studies_metadata.jsonl"
OUTPUT_DIR    = r"d:\LLM-Knowledge-Graph\outputs"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Review Question (researcher-defined) ──────────────────────────────────────
REVIEW_QUESTION = """
How do educational interventions develop clinical reasoning ability 
(analytical and non-analytical) in undergraduate medical and healthcare students?
"""

def run_full_pipeline():
    print("=" * 70)
    print("  MULTI-AGENT REALIST SYNTHESIS FRAMEWORK v2.0")
    print("  10-Agent Pipeline | Richmond et al. (2020) Benchmark")
    print("=" * 70)
    print(f"  Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"  Review Question: {REVIEW_QUESTION.strip()}")
    print("=" * 70)

    # ── PHASE 0: Protocol & IPT ───────────────────────────────────────────────
    print("\n[PHASE 0] Generating Initial Programme Theory...")
    protocol_state = run_protocol_agent(REVIEW_QUESTION)
    ipt = protocol_state["ipt_hypothesis"]
    criteria = protocol_state["inclusion_criteria"]

    # ── PHASE 1: Build Study Registry ─────────────────────────────────────────
    print("\n[PHASE 1] Building Study Registry from ingested papers...")
    registry_state = build_study_registry_from_input(INPUT_DIR, METADATA_FILE)
    study_registry = registry_state["study_registry"]
    print(f"  Registry: {len(study_registry)} unique studies")

    # ── Read one paper for CMOC extraction ───────────────────────────────────
    # (Full pipeline: iterates all included; for demo we pass all through state)
    sample_paper_text = ""
    sample_record_id = ""
    if study_registry:
        sample = study_registry[0]
        sample_record_id = sample["source_file"]
        try:
            with open(sample["source_file"], "r", encoding="utf-8", errors="replace") as f:
                sample_paper_text = f.read(8000)
        except:
            sample_paper_text = sample.get("abstract", "No text available")

    # ── Initialize Full LangGraph State ──────────────────────────────────────
    initial_state: RealistReviewState = {
        # Phase 0
        "ipt_hypothesis": ipt,
        "inclusion_criteria": criteria,
        "review_question": REVIEW_QUESTION.strip(),
        # Phase 1
        "raw_candidate_pool": [],
        "study_registry": study_registry,
        # Phase 2 (populated by screening agents)
        "title_abstract_decisions": [],
        "full_text_decisions": [],
        "included_studies": [],
        # Phase 3 CMOC
        "current_record_id": sample_record_id,
        "current_paper_text": sample_paper_text,
        "extracted_cmocs": [],
        # HITL
        "validation_status": "pending",
        "human_feedback": "",
        "hitl_checkpoint": "none",
        # Synthesis
        "leiden_communities": [],
        "contradictions_found": [],
        "demi_regularities": [],
        "draft_programme_theory": "",
        "programme_theory_version": 1,
        # Reporting
        "prisma_counts": registry_state.get("prisma_counts", {}),
        "evidence_table": [],
        "audit_log": protocol_state.get("audit_log", []) + registry_state.get("audit_log", []),
        # Meta
        "errors": [],
        "iteration_count": 0
    }

    # ── PHASES 2-6: Run LangGraph Pipeline ───────────────────────────────────
    print("\n[PHASES 2-6] Executing LangGraph Multi-Agent Pipeline...")
    print("-" * 70)

    final_state = orchestrator_app.invoke(initial_state)

    # ── Summary ───────────────────────────────────────────────────────────────
    print("\n" + "=" * 70)
    print("  PIPELINE COMPLETE")
    print("=" * 70)
    print(f"  Studies in registry:   {len(final_state.get('study_registry', []))}")
    print(f"  Studies included:      {len(final_state.get('included_studies', []))}")
    print(f"  CMOCs extracted:       {len(final_state.get('extracted_cmocs', []))}")
    print(f"  Contradictions:        {len(final_state.get('contradictions_found', []))}")
    print(f"  Audit log entries:     {len(final_state.get('audit_log', []))}")
    print(f"  HITL checkpoints:      4 (Screening / CMOC / Contradiction / Theory)")
    print(f"  Output directory:      {OUTPUT_DIR}")
    print("=" * 70)
    print("\n  Output files:")
    for fname in os.listdir(OUTPUT_DIR):
        fsize = os.path.getsize(os.path.join(OUTPUT_DIR, fname))
        print(f"    {fname:<40} ({fsize:,} bytes)")

if __name__ == "__main__":
    run_full_pipeline()
