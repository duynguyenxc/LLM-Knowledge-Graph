import os
from core.orchestrator import orchestrator_app
from core.state import RealistReviewState
from dotenv import load_dotenv

load_dotenv()

def run_framework():
    print("Initializing Multi-Agent Framework for Realist Synthesis...")
    
    # Simulating data ingestion from GraphRAG input for one paper
    sample_paper_txt = r"d:\LLM-Knowledge-Graph\graphrag\input\201201linn.pdf.txt"
    
    text_content = ""
    if os.path.exists(sample_paper_txt):
        with open(sample_paper_txt, "r", encoding="utf-8") as f:
            text_content = f.read()
    else:
        print("Sample PDF text not found. Run scripts/data_ingestion.py first.")
        return

    # Initialize State
    initial_state = RealistReviewState(
        record_id="201201linn.pdf",
        paper_text=text_content,
        extracted_cmocs=[],
        leiden_communities=[],
        validation_status="pending",
        human_feedback="",
        contradictions_found=[],
        draft_programme_theory="",
        errors=[],
        iteration_count=0
    )

    print("\n--- Starting LangGraph Orchestration ---")
    
    # Execute Graph
    # We pass the state into the compiled graph
    final_state = orchestrator_app.invoke(initial_state)
    
    print("\n--- Execution Finished ---")
    status = final_state.get('validation_status')
    
    cmocs = final_state.get('extracted_cmocs', [])
    print(f"\nFinal Validation Status: {status}")
    print(f"Total CMOCs Extracted: {len(cmocs)}")
    
    contradictions = final_state.get('contradictions_found', [])
    if contradictions:
        print("\n--- CONTRADICTIONS ADJUDICATED ---")
        for idx, con in enumerate(contradictions):
            print(f"[{idx+1}] {con}")
    else:
        print("\n--- CONTRADICTIONS: None found ---")

    theory_draft = final_state.get('draft_programme_theory', '')
    print("\n================ FINAL PROGRAMME THEORY =================\n")
    print(theory_draft)
    print("\n==========================================================\n")

if __name__ == "__main__":
    run_framework()
