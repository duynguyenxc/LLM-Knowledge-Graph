import json
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from core.state import RealistReviewState
from typing import Dict, Any, List

CONTRADICTION_PROMPT = """You are a senior Realist Synthesis adjudicator.
Your specific role within the multi-agent pipeline is to review a batch of extracted Context-Mechanism-Outcome Configurations (CMOCs) and identify any CONTRADICTIONS or DIVERGENT findings.

In Realist Synthesis, a contradiction often occurs when the same Context activates the same Mechanism but leads to completely opposing Outcomes (e.g., E46 vs E47). Or when similar Interventions trigger opposing Mechanisms in identical Contexts.

Review the following JSON dump of CMOCs extracted across studies.
CMOC Data:
{cmoc_data}

Identify any logical contradictions. If none exist, output exactly "NO_CONTRADICTIONS".
If contradictions exist, explicitly document them in a clear bulleted list, explaining the divergent paths.
"""

def detect_contradictions_node(state: RealistReviewState) -> dict:
    """
    LangGraph Node: Contradiction Agent
    Scans the aggregated CMOCs in memory to flag logical inconsistencies between studies.
    """
    cmocs = state.get("extracted_cmocs", [])
    if len(cmocs) < 2:
        # Not enough data to find cross-study contradictions
        return {"contradictions_found": []}
    
    # Serialize CMOCs to JSON for the LLM
    cmoc_dicts = [cmoc.dict() for cmoc in cmocs]
    cmoc_data_str = json.dumps(cmoc_dicts, indent=2)
    
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    prompt = ChatPromptTemplate.from_template(CONTRADICTION_PROMPT)
    chain = prompt | llm
    
    try:
        response = chain.invoke({"cmoc_data": cmoc_data_str})
        result_text = response.content.strip()
        
        if result_text == "NO_CONTRADICTIONS":
            return {"contradictions_found": []}
            
        return {"contradictions_found": [result_text]}
        
    except Exception as e:
        return {"errors": [f"Contradiction Agent failed: {str(e)}"]}
