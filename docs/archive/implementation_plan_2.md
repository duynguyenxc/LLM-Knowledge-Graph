# Project Goal and Definition

**Project:** Multi-Agent AI Framework for Realist Systematic Reviews in Education (RRE 2026 Submission)
**Objective:** To develop a professional, auditable, and scalable multi-agent artificial intelligence framework (leveraging Large Language Models, LangChain/LangGraph, and Microsoft GraphRAG). This system acts as a computational infrastructure to operationalize the explicit analytical operations of realist synthesis, without overriding final human normative judgment. 

The project will use the **Richmond et al. (2020)** paper as the definitive "gold-standard" worked example and benchmark to verify that the Agentic GraphRAG platform can reproduce the complex C-M-O (Context-Mechanism-Outcome) synthesis.

---

## Entity & Relationship Fidelity: Solving the "Big Concept" Extraction Problem

A core danger in using Generative AI for systematic reviews is the unsupervised extraction of arbitrary, trivial, or hallucinated entities. Because realist synthesis relies on finding profound "demi-regularities" and "big concepts" (e.g., *Cognitive Load*, *Self-efficacy*, *Non-analytical reasoning*), the framework must be strictly constrained. We solve this "garbage-in/garbage-out" problem through three architectural pillars:

1. **Strictly Typed Ontological Extraction:** We will NOT allow the LLM to extract open-ended graphs. We will constrain the `cmoc_extractor.py` agent using standard Python `pydantic` models that map directly to the 47 nodes/relations identified in the `Richmond-KG-Specification`. Candidate entities must be classified under specific bounds (e.g., C-Student-Level, M-Resource, M-Response, O-Diagnostic).
2. **Evidence-Grounded Graphing:** In building the Literature Knowledge Graph (LKG), every relationship (edge) and entity (node) MUST be tied to an explicit text span (claim) from the 28 Richmond studies. If the GraphRAG pipeline cannot locate a source citation, the relationship is instantly flagged and rejected.
3. **Leiden Community-Defined Abstractions:** Instead of letting the LLM guess what a "big concept" is, we use the graph-mathematical **Leiden algorithm**. It will cluster highly-connected foundational mechanisms across the 28 papers. The LLM only steps in to *summarize* the clusters that the math has already proven exist. 
4. **The "Master Control" HITL:** Before these entities are permanently committed to the knowledge graph, the framework will pause. The researcher will inspect the C-M-O extractions and explicitly approve them, ensuring logical, evidence-based alignment with human expertise.

---

## Evaluation Strategies ("Chuẩn Chỉ & Tối Ưu")

To prove to the journal (RRE 2026) that our framework does not fabricate knowledge, our Evaluation logic will use Richmond et al. (2020) as the immutable benchmark:

- **Metric 1: CMO Extraction Precision/Recall:** We will compare the explicit C-M-O triples identified by the agents against the 5 key Contexts explicitly listed in Richmond's Results section (e.g., *low knowledge*, *high domain knowledge*, *positive coping*, etc.). 
- **Metric 2: Concept Alignment Quality:** We will map the emergent GraphRAG "communities" back to the human-articulated mechanisms. Do our computationally clustered communities conceptually align with Richmond's narrative conclusions?
- **Metric 3: Document Overlap:** Ensure the AI's search and screening process reliably identifies the 28 included studies without excessive false positives/negatives.

---

## Professional Coding Standards & Architecture

To ensure the codebase is robust, maintainable, and aligned with professional GitHub repositories:
1. **Language:** All code, comments, variables, and documentation will be strictly in **English**.
2. **Type Hinting & Pydantic:** Python code will use strict typing (`typing`) to enforce the exact Entity schemas.
3. **Modularity:** Separation of concerns. The core infrastructure (retrieval, state management) will be entirely decoupled from the synthesis plugins.
4. **Environment:** Configuration will be managed via `.env` variables (e.g., `OPENAI_API_KEY`).

### Proposed Directory Structure

```text
LLM-Knowledge-Graph/
├── core/                                # Method-agnostic core infrastructure
│   ├── orchestrator.py                  # LangGraph StateGraph definition
│   ├── state.py                         # TypedDict / Pydantic models for AgentState
│   └── governance.py                    # HITL pausing and prompt-injection logic
├── plugins/                             # Method-specific analytic plugins
│   └── realist_synthesis/          
│       ├── cmoc_extractor.py            # Extracts Context, Mechanism (Resource/Response), Outcome
│       ├── cross_study_synthesizer.py   # Synthesizes patterns bridging the GraphRAG output
│       └── theory_generator.py          # Drafts the final programme theory
├── graphrag/                            # Microsoft GraphRAG infrastructure
│   ├── settings.yaml                    # GraphRAG config (Leiden algorithm)
│   └── indexer.py                       # Converts CMOCs -> Community-Defined Conceptual Entities
├── data/                                # Local data storage
│   ├── raw_pdfs/                        # The 28 studies (Richmond 2020)
│   ├── studies_metadata.jsonl           # Metadata mappings
│   └── knowledge_graph/                 # GraphRAG output artifacts
├── notebooks/                           # Evaluation metrics & replication of human workflows
├── scripts/                             # Utility scripts
├── requirements.txt                     # Python dependencies
└── main.py                              # Entry point for the framework pipeline
```

---

## Implementation Phases (Aligned to RRE 2026 Verification)

### Phase 1: Data Alignment & GraphRAG Setup
- Map the `studies_metadata.jsonl` and the 20+ Richmond papers into the data ingestion pipeline.
- Implement `indexer.py` to structure GraphRAG for extracting Candidate Contexts, Mechanisms, and Outcomes as first-class graph edges (e.g., *Context C -> activates Mechanism M -> leads to Outcome O*).

### Phase 2: Core Infrastructure & Agent Design
- Implement the LangGraph execution flow matching the **Human Workflow Specification** (Stage 1 to Stage 5).
- Build the `cmoc_extractor.py` agent, explicitly passing the structured `Pydantic` schemas to prevent AI hallucinatory behaviors.

### Phase 3: The Human-in-the-Loop Governance
- Implement the `governance` node that pauses LangGraph execution.
- This will output the candidate CMOC triples to the console. The researcher will validate "Structural Match" and "Evidence Grounding" before allowing the framework to proceed to cross-study synthesis.

### Phase 4: Output Generation & System Verification
- System outputs a draft Programme Theory, constrained entirely by connected nodes.
- We run the final Verification step: Comparing the GraphRAG/Agent output against the explicit 5 key contexts and CMOC findings documented in Richmond et al. (2020) to generate the quantitative qualitative findings for your paper.


> [!IMPORTANT]
> **Next Step Approval Request:** Do you approve the deep structural constraints on entity extraction (Pydantic forcing + Leiden community math) to solve the "garbage-in, garbage-out / big concepts" abstraction problem? If you approve, I will begin initializing the repository and writing the first data processing / Pydantic schema scripts.
