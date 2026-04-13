from typing import TypedDict, Annotated, List, Dict, Any
from .ontology import CMOCExtraction

def merge_list(a: List[Any], b: List[Any]) -> List[Any]:
    """Helper to merge lists in LangGraph state."""
    # If a is not a list, replace it or deal with it
    if not a: return b
    if not b: return a
    return a + b

class RealistReviewState(TypedDict):
    """
    LangGraph Complete State Machine for Realist Systematic Reviews.
    Tracks the trajectory of the Multi-Agent execution.
    """
    record_id: str
    paper_text: str
    
    # 1. Pipeline outputs
    extracted_cmocs: Annotated[List[CMOCExtraction], merge_list]
    
    # 2. GraphRAG outputs
    leiden_communities: List[Dict[str, Any]]
    
    # 3. Adjudication / HITL
    validation_status: str  # e.g., "pending", "approved", "rejected"
    human_feedback: str
    
    # 4. Final cross-study outputs
    contradictions_found: List[str]
    draft_programme_theory: str
    
    # 5. Routing details
    errors: List[str]
    iteration_count: int
