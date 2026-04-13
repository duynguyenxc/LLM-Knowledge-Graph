import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from core.state import RealistReviewState

SYNTHESIS_PROMPT = """You are a master theoretician in Realist Synthesis (adhering to Richmond et al., 2020 standards).
Your final task in the multi-agent pipeline is to construct a cohesive 'Programme Theory'.

You are provided with:
1. All validated CMOCs extracted from the systematic review literature.
2. Contradiction reports (if any conflicting mechanisms were found).
3. GraphRAG Leiden Community Clusters (if available), which represent mathematically linked meta-concepts.

Using *only* the evidence provided, write a comprehensive narrative Programme Theory that answers: 'What works, for whom, in what respects, to what extent, in what contexts, and how?'
Ensure you explicitly name the Contexts (C), Mechanisms (M), and Outcomes (O).

CMOC Data:
{cmoc_data}

Contradictions Identified:
{contradictions}

Leiden Communities (Meta-concepts):
{leiden_clusters}

Draft the Final Programme Theory:
"""

def synthesis_node(state: RealistReviewState) -> dict:
    """
    LangGraph Node: Cross-Study Synthesizer
    Drafts the final realist programme theory.
    """
    cmocs = state.get("extracted_cmocs", [])
    contradictions = state.get("contradictions_found", [])
    leiden_clusters = state.get("leiden_communities", [])
    
    # Serialize data
    cmoc_data_str = json.dumps([c.dict() for c in cmocs], indent=2)
    leiden_str = json.dumps(leiden_clusters, indent=2)
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0.2)
    prompt = ChatPromptTemplate.from_template(SYNTHESIS_PROMPT)
    chain = prompt | llm
    
    try:
        response = chain.invoke({
            "cmoc_data": cmoc_data_str,
            "contradictions": "\n".join(contradictions) if contradictions else "None.",
            "leiden_clusters": leiden_str if leiden_clusters else "Not computed."
        })
        
        return {"draft_programme_theory": response.content.strip()}
        
    except Exception as e:
        return {"errors": [f"Synthesis Agent failed: {str(e)}"]}
