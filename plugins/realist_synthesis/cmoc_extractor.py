"""
plugins/realist_synthesis/cmoc_extractor.py — Agent 6: CMOC Extraction Agent
==============================================================================
Richmond Alignment: Subject Matter Expert / Data Extractor
Role: Deconstructs full-text passages into structured CMOCs aligned to the
strict Pydantic E01-E47 Richmond ontology.

Prompting Strategy:
- System: RAMESES realist synthesis specialist
- Few-shot: Grounded in Richmond's actual CMOCs from the 28 reference papers
- Schema enforcement: Pydantic E01-E47 Union types prevent hallucination
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from core.ontology import CMOCExtraction
from core.state import RealistReviewState

# ── Few-Shot Examples grounded in Richmond et al. (2020) ─────────────────────
RICHMOND_FEW_SHOT = """
EXAMPLE 1 — Paper: Linn et al. (2012)
Context: "novice learners, such as medical students, have limited clinical experience"
  → Context label: "students with 'low knowledge,' low clinical domain-specific knowledge..."
Intervention: "teach it within a skill framework in the clinical consultation room"
  → Intervention label: "teaching resources that allow them to make mistakes"
Mechanism Resource: "the idea of a 'coach' to assist the student... with instant feedback"
  → Mechanism_Resource label: "accurate and timely feedback"
Mechanism Response: "students having a basic understanding of the theoretical concepts"
  → Mechanism_Response label: "build understanding"
Outcome: "encourages personal reflection and refinement of clinical reasoning skills"
  → Outcome label: "positive impact on learning"

EXAMPLE 2 — Paper: Cancer Cytopathology Evered et al. (2013)
Context: "novice participants"
  → Context label: "students with 'low knowledge,' low clinical domain-specific knowledge..."
Intervention: "shown 20 nonannotated paired images (non-analytical group)"
  → Intervention label: "real-life scenarios, including simulation and simulated patients"
Mechanism Resource: "pattern recognition exposure"
  → Mechanism_Resource label: "multiple relevant resources"
Mechanism Response: "relied on intuitive pattern without analytical backing"
  → Mechanism_Response label: "rely on non-analytical reasoning"
Outcome: "high diagnostic accuracy through pattern recognition"
  → Outcome label: "more accurate non-analytical reasoning"
"""

CMOC_SYSTEM_PROMPT = f"""You are a specialist in RAMESES-compliant Realist Synthesis, acting as 
the Data Extraction Expert aligned with the Richmond et al. (2020) meta-review of clinical reasoning education.

YOUR TASK: Extract ONE primary CMOC (Context-Mechanism-Outcome Configuration) from the provided paper text.

EXTRACTION RULES:
1. Context: WHO are the students? (knowledge level, confidence, experience)
2. Intervention: WHAT educational method is provided?
3. Mechanism_Resource: WHAT does the intervention provide to students? (the resource)
4. Mechanism_Response: HOW do students respond cognitively/emotionally? (the internal reaction)
5. Outcome: WHAT measurable learning result occurs? (diagnostic accuracy, illness scripts, etc.)

ONTOLOGY CONSTRAINT: You MUST choose labels EXACTLY from the predefined E01-E47 schema.
Link each entity to a VERBATIM text span from the paper as evidence.

REFERENCE EXAMPLES FROM RICHMOND ET AL. (2020):
{RICHMOND_FEW_SHOT}

OUTPUT: Return a structured JSON matching the CMOCExtraction schema with entities and relationships.
"""

CMOC_PROMPT = ChatPromptTemplate.from_messages([
    ("system", CMOC_SYSTEM_PROMPT),
    ("human", """Paper ID: {record_id}

Full Text (extract):
{paper_text}

Extract the primary CMOC configuration. Choose context, mechanism, and outcome labels 
STRICTLY from the Richmond E01-E47 ontology.
""")
])


def extract_cmoc_node(state: RealistReviewState) -> dict:
    """
    Agent 6: CMOC Extraction Agent (Realist Synthesis Plugin)
    INPUT:  paper text from current_paper_text + record_id
    OUTPUT: structured CMOCExtraction appended to extracted_cmocs
    """
    record_id = state.get("current_record_id", "unknown_paper")
    paper_text = state.get("current_paper_text", "")

    if not paper_text:
        return {"errors": [f"No paper text provided for {record_id}"]}

    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    structured_llm = llm.with_structured_output(CMOCExtraction)
    chain = CMOC_PROMPT | structured_llm

    print(f"\n[AGENT 6] CMOC Extraction — {record_id[:50]}...")
    try:
        result = chain.invoke({
            "record_id": record_id,
            "paper_text": paper_text[:6000]
        })

        for e in result.entities:
            label_val = e.label.value if hasattr(e.label, 'value') else str(e.label)
            print(f"  [ENTITY]   [{e.category.value}] {e.id}: {label_val[:65]}")
        for r in result.relationships:
            print(f"  [RELATION] {r.source_id} --{r.relation_type.value}--> {r.target_id}")

        log = f"[CMOC Agent] Extracted {len(result.entities)} entities, {len(result.relationships)} relations from {record_id[:40]}"
        return {
            "extracted_cmocs": [result],
            "audit_log": [log]
        }
    except Exception as e:
        error = f"CMOC extraction failed for {record_id}: {e}"
        print(f"  [ERROR] {error}")
        return {"errors": [error]}
