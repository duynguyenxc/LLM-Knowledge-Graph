# Project Goal and Definition

**Project:** Multi-Agent AI Framework for Realist Systematic Reviews in Education (RRE 2026 Submission)
**Objective:** To develop a professional, auditable, and scalable multi-agent artificial intelligence framework (leveraging Large Language Models, LangChain/LangGraph, and Microsoft GraphRAG). This system acts as a computational infrastructure to operationalize the explicit analytical operations of realist synthesis, without overriding final human normative judgment. 

The project will use the **Richmond et al. (2020)** paper as the definitive "gold-standard" worked example and benchmark to verify that the Agentic GraphRAG platform can reproduce the complex C-M-O (Context-Mechanism-Outcome) synthesis.

---

## 1. Multi-Agent Architecture & Algorithmic Layers

The professor explicitly emphasized the **Multi AI Agent** approach. Traditional linear LLM pipelines cannot handle the complexity of systematic reviews. We will utilize a deeply layered architecture using **LangGraph** as a finite state machine (FSM), allowing agents to collaborate, argue, and iterate.

### Layer 1: Orchestration & State Management (LangGraph)
- **Algorithm:** Cyclic Graph Routing. The workflow is not a straight line. If an agent extracts poor data, a validator agent (or the human) can route the execution back to the extraction node with an error log, forcing a retry.
- **Global State (`AgentState`):** A shared memory object containing the current PDF text, extracted CMOC candidate arrays, screening logs, and the current few-shot prompt templates.

### Layer 2: Specialized Agent Nodes
Instead of one "smart AI," we deploy multiple "expert narrow AIs."
1. **Search & Screening Agent:** Evaluates Title/Abstract -> Full Text based on strict RRE inclusion criteria (False Positives/Negatives are logged here).
2. **CMOC Extraction Agent:** Scans text to identify causal chains. Uses GraphRAG to ground extraction in specific document claims.
3. **Contradiction Detection Agent (Adjudicator):** An agent explicitly tasked to find *conflicts* (e.g., one paper says simulation helps novices, another says it harms novices). 
4. **Cross-Study Synthesis Agent:** Analyzes the Leiden clusters (Community-Defined Entities) mathematically found by GraphRAG, and maps them to a draft "Programme Theory".

### Layer 3: Human-in-the-Loop (HITL) Governance
- **"Master Control":** The system automatically pauses at predefined checkpoints (e.g., before Graph clustering, before final Synthesis). The human researcher acts as the normative judge. 

---

## 2. Ontology Design & Prompt Engineering Strategy

If the schema is flawed or the prompts are weak, the AI's output will diverge entirely from Richmond's methodology. We will architect this with rigorous precision:

### A. Strict Ontology Mapping
- We will NOT let the AI invent entity categories. The ontology will be hard-coded into Python using **Pydantic** classes.
- We will map the exact 47 entities and relationships from the `Richmond-KG-Specification` (e.g., `E02: students with low knowledge`, `E20: understanding`, `R01: PROVIDES`, `R03: LEADS_TO`). 
- This ensures the LLM's GraphRAG extraction produces a graph geometrically identical to what Richmond and experts conceptualized.

### B. Analytical Prompt Engineering ("Prompt Chuẩn Chỉ")
- **Refusing "Zero-Shot" Laziness:** We will use dynamic **Few-Shot Prompting**. The prompt sent to the LLM will explicitly contain "Gold Standard" extraction examples built directly from the text of Richmond 2020. 
- **GraphRAG Prompt Tuning:** Microsoft GraphRAG requires domain-specific prompts to extract communities. We will run the formal `prompt-tune` pipeline to computationally generate the optimal extraction heuristics tailored *specifically* to clinical reasoning education.
- **Role-based Constraining:** Prompts will strictly enforce the "Realist Evaluator" persona (e.g., *"You are not searching for general summaries. You are searching exclusively for 'What works, for whom, in what contexts, and why?' Identify the Mechanism (Resource/Response) that Context C triggers to produce Outcome O."*).

---

## 3. Entity & Relationship Fidelity: The "Big Concept" Problem

A core danger in using Generative AI for systematic reviews is the unsupervised extraction of arbitrary, trivial, or hallucinated entities. We solve this "garbage-in/garbage-out" problem through three architectural pillars:
1. **Strictly Typed Ontological Extraction** (via the Pydantic models mentioned above).
2. **Evidence-Grounded Graphing:** Every relationship (edge) MUST be tied to an explicit text span. 
3. **Leiden Community-Defined Abstractions:** We use the graph-mathematical **Leiden algorithm** to cluster highly-connected mechanisms. The LLM only *summarizes* the abstract clusters ("Big Concepts") that the mathematics have definitively proven to exist across papers. 

---

## 4. Evaluation Strategies (Model Verification)

To prove to the journal (RRE 2026) that our framework is computationally sound, Evaluation uses Richmond et al. (2020) as the benchmark:
- **Metric 1: CMO Extraction Precision/Recall:** Do the platform-generated C-M-O triples structurally match Richmond's?
- **Metric 2: Concept Alignment Quality:** Do emergent GraphRAG "communities" (Leiden clusters) map onto Richmond's human-articulated mechanisms?
- **Metric 3: Document Overlap:** Does the automated pipeline retrieve the same 28 studies?

---

### Proposed Directory Structure

```text
LLM-Knowledge-Graph/
├── core/                                # Method-agnostic core infrastructure
│   ├── orchestrator.py                  # LangGraph StateGraph (Layer 1)
│   ├── state.py                         # Typed Dicts/Pydantic schema (Ontology)
│   └── governance.py                    # HITL pausing logic (Layer 3)
├── plugins/                             # Method-specific analytic plugins (Layer 2)
│   └── realist_synthesis/          
│       ├── screening_agent.py           # Pass A/Pass B screening
│       ├── cmoc_extractor.py            # Extracts Context, Mechanism, Outcome
│       ├── contradiction_agent.py       # Identifies conflicting evidence
│       └── cross_study_synthesizer.py   # Maps GraphRAG communities to theory
├── graphrag/                            # Microsoft GraphRAG infrastructure
│   ├── settings.yaml                    # GraphRAG config (Leiden algorithm)
│   └── prompts/                         # Tuned extraction prompts
├── data/                                # Local data storage
│   ├── raw_pdfs/                        # The 28 studies 
│   ├── studies_metadata.jsonl           # Metadata mappings
│   └── knowledge_graph/                 # Output artifacts
├── notebooks/                           # Evaluation metrics 
├── scripts/                             # Utility scripts
├── requirements.txt                     # Python dependencies
└── main.py                              # Pipeline entry point
```

> [!IMPORTANT]
> **To the Researcher:** The implementation plan now serves as a rigorous architectural blueprint capable of addressing the professor's strict demands for Multi-Agent coordination, prompt/ontology precision, and mechanism-outcome fidelity. Are we fully aligned to initialize the repository structure?
