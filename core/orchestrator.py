from langgraph.graph import StateGraph, END
from core.state import RealistReviewState
from plugins.realist_synthesis.cmoc_extractor import extract_cmoc_node

def hitl_validation_node(state: RealistReviewState) -> dict:
    """
    LangGraph Node: Master Control (HITL).
    Pauses execution and simulates waiting for human input to validate the extracted graph structure.
    """
    if state.get("errors"):
        return {"validation_status": "error_routed"}
        
    print(f"\n--- [HITL PENDING] Record {state.get('record_id')} ---")
    print("Waiting for researcher to validate CMOC extractions against Context definitions...")
    
    # In a real deployed app, this would use langgraph's interrupt() or breakpoint logic.
    # We will simulate that the human has 'approved' for now.
    
    return {"validation_status": "approved"}

def validation_router(state: RealistReviewState) -> str:
    """
    Conditional logic: If rejected, re-route back to CMOC extraction. 
    If approved, route to END (or next phase).
    """
    status = state.get("validation_status")
    if status == "rejected" or status == "error_routed":
        return "retry_extraction"
    return "synthesis"

# Initialize Graph
workflow = StateGraph(RealistReviewState)

# Add Nodes
workflow.add_node("extract_cmoc", extract_cmoc_node)
workflow.add_node("hitl_validation", hitl_validation_node)
workflow.add_node("synthesis", lambda state: {"draft_programme_theory": "Synthesis complete (Mock)."})

# Add Edges
workflow.set_entry_point("extract_cmoc")
workflow.add_edge("extract_cmoc", "hitl_validation")
workflow.add_conditional_edges(
    "hitl_validation",
    validation_router,
    {
        "retry_extraction": "extract_cmoc",
        "synthesis": "synthesis"
    }
)
workflow.add_edge("synthesis", END)

# Compile framework
orchestrator_app = workflow.compile()
