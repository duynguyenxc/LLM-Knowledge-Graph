from langgraph.graph import StateGraph, END
from core.state import RealistReviewState
from plugins.realist_synthesis.cmoc_extractor import extract_cmoc_node
from plugins.realist_synthesis.contradiction_agent import detect_contradictions_node
from plugins.realist_synthesis.cross_study_synthesizer import synthesis_node

def hitl_validation_node(state: RealistReviewState) -> dict:
    """
    LangGraph Node: Master Control (HITL).
    Pauses execution and simulates waiting for human input to validate the extracted graph structure.
    """
    if state.get("errors"):
        return {"validation_status": "error_routed"}
        
    print(f"\n--- [HITL PENDING] Record {state.get('record_id')} ---")
    print("Waiting for researcher to validate CMOC extractions against Context definitions...")
    
    return {"validation_status": "approved"}

def validation_router(state: RealistReviewState) -> str:
    status = state.get("validation_status")
    if status == "rejected" or status == "error_routed":
        return "retry_extraction"
    return "check_contradictions"

# Initialize Graph
workflow = StateGraph(RealistReviewState)

# Add Nodes
workflow.add_node("extract_cmoc", extract_cmoc_node)
workflow.add_node("hitl_validation", hitl_validation_node)
workflow.add_node("check_contradictions", detect_contradictions_node)
workflow.add_node("synthesis_theory", synthesis_node)

# Add Edges
workflow.set_entry_point("extract_cmoc")
workflow.add_edge("extract_cmoc", "hitl_validation")
workflow.add_conditional_edges(
    "hitl_validation",
    validation_router,
    {
        "retry_extraction": "extract_cmoc",
        "check_contradictions": "check_contradictions"
    }
)
workflow.add_edge("check_contradictions", "synthesis_theory")
workflow.add_edge("synthesis_theory", END)

# Compile framework
orchestrator_app = workflow.compile()
