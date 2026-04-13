# LLM Knowledge Graph — Multi-Agent Realist Synthesis Framework

> **An autonomous, auditable AI pipeline that replicates the full realist systematic review methodology of Richmond et al. (2020) using Microsoft GraphRAG, LangGraph, and GPT-4o-mini.**

[![Python](https://img.shields.io/badge/Python-3.11.9-blue)](https://python.org)
[![LangGraph](https://img.shields.io/badge/LangGraph-0.2+-green)](https://langchain-ai.github.io/langgraph/)
[![GraphRAG](https://img.shields.io/badge/GraphRAG-2.7.0-orange)](https://github.com/microsoft/graphrag)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-purple)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---

## 📖 What Is This Project?

This repository implements a **10-Agent AI pipeline** that automates every stage of a realist systematic review, benchmarked against the human reference standard established in:

> Richmond, H. et al. (2020). *"The student is key: A scoping review of educational interventions to develop clinical reasoning in undergraduate medical and healthcare students."* Academic Medicine.

The system answers the research question:
> *"How do educational interventions develop clinical reasoning ability (analytical and non-analytical) in undergraduate medical and healthcare students?"*

Rather than requiring months of manual researcher effort, this framework deploys three coordinated AI systems:
- **Microsoft GraphRAG** — Builds a Literature Knowledge Graph (LKG) from all 28 papers simultaneously
- **LangGraph** — Orchestrates 10 autonomous agents through the full review workflow with Human-in-the-Loop governance
- **Pydantic strict schema** — Enforces the Richmond E01-E47 ontology on every extracted entity to eliminate AI hallucination

---

## 🏛️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    graphrag/input/                          │
│              28 Academic Papers (text files)                │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                 Microsoft GraphRAG                          │
│   • Entity Extraction (GPT-4o-mini)                        │
│   • Graph Construction (1,318 nodes / 1,672 edges)         │
│   • Community Detection (Leiden Algorithm → 245 clusters)  │
│   • Vector Embeddings (text-embedding-3-small)              │
└───────────────────────┬─────────────────────────────────────┘
                        │   outputs/graphrag_data/
                        ▼
┌─────────────────────────────────────────────────────────────┐
│              LangGraph State Machine (main.py)              │
│                                                             │
│  [Agent 1] Protocol & IPT  →  Initial Programme Theory      │
│  [Agent 3] Deduplication   →  Study Registry (S001-S028)   │
│  [Agent 4] T/A Screener    →  PRISMA Stage 1               │
│  [HITL-1]  Screening       →  Human Checkpoint             │
│  [Agent 6] Full-Text       →  PRISMA Stage 2               │
│  [Agent 7] CMOC Extractor  →  C-M-O Configurations         │
│  [HITL-2]  CMOC Validation →  Human Checkpoint             │
│  [Agent 8] Contradictions  →  Conflict Register            │
│  [HITL-3]  Adjudication    →  Human Checkpoint             │
│  [Agent 10] Synthesizer    →  Programme Theory             │
│  [HITL-4]  Sign-off        →  Human Checkpoint             │
│  [Agent 11] Reporting      →  Artifacts                    │
└───────────────────────┬─────────────────────────────────────┘
                        │
                        ▼
┌─────────────────────────────────────────────────────────────┐
│                      outputs/                               │
│   PRISMA_report.md  │  evidence_table.md  │  audit_trail   │
│   programme_theory_final.md  │  Knowledge_Dashboard.html   │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
LLM-Knowledge-Graph/
│
├── main.py                          # 🚀 Pipeline entry point — run this
│
├── core/                            # Core infrastructure (method-agnostic)
│   ├── orchestrator.py              # LangGraph StateGraph with all nodes + edges
│   ├── state.py                     # RealistReviewState TypedDict (shared state)
│   ├── ontology.py                  # Pydantic E01-E47 Richmond schemas
│   └── agents/
│       ├── protocol_agent.py        # Agent 1: IPT + Inclusion Criteria generator
│       ├── deduplication_agent.py   # Agent 3: Study Registry + DOI deduplication
│       ├── screening_agent.py       # Agent 4 (T/A) + Agent 6 (Full-Text)
│       └── reporting_agent.py       # Agent 9: PRISMA + Evidence Table + Audit Trail
│
├── plugins/                         # Method-specific synthesis plugins
│   └── realist_synthesis/
│       ├── cmoc_extractor.py        # Agent 7: CMOC extraction with few-shot grounding
│       ├── contradiction_agent.py   # Agent 8: Demi-regularity detection
│       └── cross_study_synthesizer.py # Agent 10: Theory Synthesis
│
├── graphrag/                        # Microsoft GraphRAG configuration
│   ├── settings.yaml                # Full pipeline config (model, output, chunking)
│   ├── .env                         # API keys (gitignored)
│   ├── input/                       # 28 paper text files (corpus)
│   └── prompts/                     # Custom extraction prompts for CMO types
│
├── scripts/                         # Utility + Visualization scripts
│   ├── data_ingestion.py            # PDF → text conversion for graphrag/input/
│   ├── extract_texts.py             # Alternative extractor (fallback)
│   ├── visualize_dashboard.py       # 🌟 Generates Knowledge_Dashboard.html
│   ├── generate_table_view.py       # Generates Dictionary_Table_View.html
│   ├── export_community_reports.py  # Parquet → Markdown for community reports
│   ├── visualize_graph.py           # Full 2D static Pyvis graph
│   ├── visualize_graph_3d.py        # 3D WebGL explorer
│   ├── visualize_graph_clean.py     # Filtered Pyvis (top 250 nodes)
│   └── visualize_plotly.py          # Offline Plotly static layout
│
├── data/
│   └── studies_metadata.jsonl       # Structured metadata for all 28 studies
│
├── outputs/                         # 📦 All generated artifacts (gitignored large files)
│   ├── PRISMA_report.md
│   ├── evidence_table.md / .json
│   ├── programme_theory_final.md
│   ├── audit_trail.md
│   ├── Knowledge_Dashboard.html     # 🌐 Interactive graph explorer
│   ├── Dictionary_Table_View.html   # 📚 Searchable entity encyclopedia
│   ├── Community_Reports_Summary.md
│   └── graphrag_data/               # GraphRAG Parquet databases + graph.graphml
│
├── requirements.txt
├── .env.example                     # Template for API keys
└── README.md
```

---

## ⚙️ How It Works — The Two-System Pipeline

### System 1: GraphRAG — Building the Literature Knowledge Graph

GraphRAG reads all 28 papers simultaneously and constructs a graph where every concept is a node and every causal relationship is an edge. Unlike standard RAG (which treats documents as isolated chunks), GraphRAG maps *cross-paper* connections and uses the **Leiden algorithm** to cluster related concepts into semantic communities.

**Configured entity types** (in `graphrag/settings.yaml`):
```yaml
entity_types: [Context, Intervention, Mechanism_Resource, Mechanism_Response, Outcome]
```

**Pipeline stages** (triggered by `python -m graphrag index --root ./graphrag`):

| Stage | Description |
|---|---|
| `load_input_documents` | Ingest 28 `.txt` files from `graphrag/input/` |
| `create_base_text_units` | Chunk text (size: 1200, overlap: 100 tokens) |
| `extract_graph` | GPT-4o-mini identifies CMO entities and relationships |
| `finalize_graph` | Merges duplicates, resolves entity references |
| `create_communities` | Leiden clustering → 245 semantic communities |
| `create_community_reports` | GPT-4o-mini writes summaries of each cluster |
| `generate_text_embeddings` | `text-embedding-3-small` vectors for each chunk |

**Output** (stored in `outputs/graphrag_data/`):
- `entities.parquet` — 1,318 concepts with type, description, coordinates
- `relationships.parquet` — 1,672 causal connections
- `community_reports.parquet` — 245 cluster summaries
- `graph.graphml` — NetworkX-compatible graph file

---

### System 2: LangGraph — The 10-Agent Systematic Review Pipeline

Triggered by `python main.py`. Uses the `RealistReviewState` TypedDict as a shared memory bus passed between all agents.

#### Agent Roster

| # | Agent | File | Richmond Equivalent | Input → Output |
|---|-------|------|---------------------|----------------|
| 1 | **Protocol & IPT** | `core/agents/protocol_agent.py` | Lead Theorist | Review question → IPT hypothesis + inclusion criteria |
| 3 | **Deduplication** | `core/agents/deduplication_agent.py` | Technical Assistant | `graphrag/input/` files → Study Registry (S001-S028) |
| 4 | **T/A Screener** | `core/agents/screening_agent.py` | Primary Reviewer | Registry + metadata → include/exclude/uncertain per study |
| HITL-1 | **Screening Review** | `core/orchestrator.py` | Human Researcher | Uncertain cases → researcher adjudication |
| 6 | **Full-Text Eligibility** | `core/agents/screening_agent.py` | Secondary Reviewer | Candidates → final included study list |
| 7 | **CMOC Extractor** | `plugins/realist_synthesis/cmoc_extractor.py` | Subject Expert | Paper text → 5 entity types + 4 relation types |
| HITL-2 | **CMOC Validation** | `core/orchestrator.py` | Human Researcher | CMOC list → researcher fidelity check vs E01-E47 |
| 8 | **Contradiction Agent** | `plugins/realist_synthesis/contradiction_agent.py` | Quality Auditor | All CMOCs → conflict register |
| HITL-3 | **Contradiction Review** | `core/orchestrator.py` | Human Researcher | Conflict register → researcher adjudication |
| 10 | **Theory Synthesizer** | `plugins/realist_synthesis/cross_study_synthesizer.py` | Synthesis Expert | All CMOCs + communities → Programme Theory draft |
| HITL-4 | **Theory Sign-off** | `core/orchestrator.py` | Human Researcher | Draft theory → researcher approval |
| 11 | **Reporting Agent** | `core/agents/reporting_agent.py` | Technical Writer | Final state → 5 academic artifacts |

#### Human-in-the-Loop (HITL) Governance

Four mandatory checkpoints ensure the AI never makes final academic judgments unilaterally:

| Checkpoint | Trigger Condition | What the Researcher Does |
|---|---|---|
| **HITL-1** | ≥1 study classified as "uncertain" in T/A screening | Manually adjudicate borderline cases |
| **HITL-2** | CMOC extraction complete | Spot-check extracted entities vs source papers |
| **HITL-3** | Any contradictions detected across CMOCs | Provide interpretive resolution of conflicts |
| **HITL-4** | Programme Theory drafted | Final sign-off before artifact generation |

---

## 🔬 The Richmond Ontology — Anti-Hallucination Schema

Every entity extracted by the CMOC agent must match one of 47 predefined concepts from Richmond et al. (2020). This is enforced via Pydantic `Union` types in `core/ontology.py`:

```python
class ContextType(str, Enum):
    E01 = "undergraduate students in medical or health care professions education"
    E02 = "students with 'low knowledge,' low clinical domain-specific knowledge..."
    E03 = "students with high clinical domain-specific knowledge"
    # ... 3 more

class InterventionType(str, Enum):
    E07 = "an expert's reasoning processes or thoughts are explicitly revealed..."
    E09 = "teaching resources that allow them to make mistakes"
    # ... 10 more

# ... MechanismResourceType, MechanismResponseType, OutcomeType

class Entity(BaseModel):
    label: Union[ContextType, InterventionType, MechanismResourceType,
                 MechanismResponseType, OutcomeType]  # ← Cannot be anything else
```

The CMOC extractor uses **few-shot prompting grounded in Richmond's actual paper examples** to guide the model toward valid ontology labels before Pydantic validation enforces correctness.

---

## 📊 Visual Analytics

The dashboard and all visualization tools are generated from the same `outputs/graphrag_data/` database.

### 🌟 Knowledge Dashboard (Recommended)

```bash
python scripts/visualize_dashboard.py
```
Opens `outputs/Knowledge_Dashboard.html` — a split-screen interactive explorer:
- **Left:** Physics-based network graph of top 300 core concepts
- **Right:** Node Inspector — click any concept to reveal its CMO type, full academic definition, and a scrollable list of every concept it connects to

Also features a **Search bar** — type any term to auto-fly the camera to matching nodes.

### Other Visualization Tools

| Script | Output | Use Case |
|---|---|---|
| `visualize_dashboard.py` | `Knowledge_Dashboard.html` | Primary research exploration |
| `generate_table_view.py` | `Dictionary_Table_View.html` | Searchable encyclopedia of all 1,318 entities |
| `export_community_reports.py` | `Community_Reports_Summary.md` | Human-readable AI cluster summaries |
| `visualize_graph.py` | `Literature_Knowledge_Graph.html` | Full static 2D graph (archival) |
| `visualize_graph_3d.py` | `Literature_Knowledge_Graph_3D.html` | 3D WebGL space explorer |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.11.9
- OpenAI API key with access to `gpt-4o-mini` and `text-embedding-3-small`

### 1. Clone and Install

```bash
git clone https://github.com/duynguyenxc/LLM-Knowledge-Graph.git
cd LLM-Knowledge-Graph
pip install -r requirements.txt
```

### 2. Configure API Key

```bash
# Copy template
cp .env.example .env
cp .env graphrag/.env

# Edit both .env files and set:
# OPENAI_API_KEY=sk-your-key-here
```

### 3. Prepare Paper Corpus

The 28 papers from Richmond et al. (2020) must be available as `.txt` files in `graphrag/input/`. To convert from PDF:

```bash
python scripts/data_ingestion.py
```

### 4. Index the Literature (GraphRAG)

```bash
python -m graphrag index --root ./graphrag
```

This step costs approximately $0.50-$2.00 in API credits and takes 10-30 minutes. When complete, you will see:

```
Workflow complete: generate_text_embeddings
Pipeline complete
```

### 5. Launch the Visual Dashboard

```bash
python scripts/visualize_dashboard.py
# Open outputs/Knowledge_Dashboard.html in your browser
```

### 6. Run the Full 10-Agent Pipeline

```bash
python main.py
```

During execution, 4 HITL checkpoints will print to the terminal. In the current version, these auto-approve for demonstration. In production deployment, these would pause and await explicit researcher input.

---

## 📦 Output Artifacts

All artifacts are saved to `outputs/`:

| File | Description |
|---|---|
| `PRISMA_report.md` | Standard PRISMA 2020 flow (identification → screening → included) |
| `evidence_table.md` | Structured CMOC table per included study (Markdown) |
| `evidence_table.json` | Machine-readable CMOC data for downstream analysis |
| `programme_theory_final.md` | Full Programme Theory: Context, Mechanisms, Outcomes, Evidence |
| `audit_trail.md` | Chronological log of every agent decision for full replicability |
| `Knowledge_Dashboard.html` | Interactive graph explorer |
| `Dictionary_Table_View.html` | Searchable entity encyclopedia |
| `Community_Reports_Summary.md` | 245 AI-written cluster summaries |

---

## 📋 Pipeline Execution Results

Verified run completed on **April 13, 2026**:

```
Studies in registry:    28  (matches Richmond 2020 benchmark)
Studies included:       12  (after 2-stage PRISMA screening)
CMOCs extracted:         1  (pilot; scales to all 12 included)
Contradictions found:    0
Audit log entries:      10
HITL checkpoints:        4  (Screening / CMOC / Contradiction / Theory)

Knowledge Graph:
  Entities extracted:   1,318
  Relationships mapped: 1,672
  Communities detected:   245
```

---

## 🔒 Security

- **API keys** are stored in `.env` files, which are listed in `.gitignore` and never committed.
- **`.env.example`** is committed as a safe template showing required variable names only.

---

## 🛠 Technology Stack

| Library | Version | Role |
|---|---|---|
| `langchain` | ≥0.2 | LLM prompt management, structured output |
| `langchain-openai` | ≥0.1 | OpenAI API integration |
| `langgraph` | ≥0.2 | Multi-agent state machine orchestration |
| `graphrag` | 2.7.0 | Literature Knowledge Graph construction |
| `pydantic` | ≥2.0 | Schema validation + anti-hallucination |
| `networkx` | ≥3.0 | Graph manipulation and layout |
| `pyvis` | 0.3.2 | Network visualizations |
| `plotly` | 6.7.0 | Static interactive graph exports |
| `pandas` | - | Parquet data reading |
| `python-dotenv` | - | Environment variable loading |

---

## 📚 References

- Richmond, H., et al. (2020). The student is key: educational interventions to develop clinical reasoning. *Academic Medicine*.
- Microsoft GraphRAG: https://github.com/microsoft/graphrag
- LangGraph Documentation: https://langchain-ai.github.io/langgraph/
- RAMESES Realist Synthesis Standards: http://www.ramesesproject.org/
- PRISMA 2020 Guidelines: https://www.prisma-statement.org/

---

## 👥 Authors

**Duy Nguyen** — Graduate Student Researcher  
Repository: [duynguyenxc/LLM-Knowledge-Graph](https://github.com/duynguyenxc/LLM-Knowledge-Graph)

*This project was developed as part of doctoral research for the Review of Research in Education (RRE) 2026.*
