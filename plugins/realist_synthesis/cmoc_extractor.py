import os
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from core.ontology import CMOCExtraction
from core.state import RealistReviewState

# This is the Few-Shot Prompt mapped directly to Richmond et al. (2020) and the KG Specification.
CMOC_EXTRACTION_PROMPT = """You are an expert academic in Realist Systematic Reviews, heavily trained on Richmond et al. (2020).
Your task is to extract Context-Mechanism-Outcome Configurations (CMOCs) from the provided scientific paper text.

CRITICAL INSTRUCTIONS:
1. You MUST extract entities ONLY matching the provided Ontology schemas.
2. A Context (C) is the backdrop or condition.
3. A Mechanism (M) has two parts: M_resource (what the intervention provides) and M_response (the internal cognitive/emotional reaction of the student).
4. An Outcome (O) is the result (e.g., diagnostic accuracy, cognitive load).
5. You MUST provide the exact verbatim 'extracted_text' and 'evidence_quote' from the text that grounds your extraction.

Here are 'Gold Standard' examples of expected logical reasoning:
- If a student has 'low clinical knowledge' (Context) and is placed in a 'real-life scenario' (Intervention), they experience 'cognitive overload' (Mechanism_Response) which LEADS_TO 'negative learning outcomes' (Outcome).

Paper ID: {record_id}
Text Chunk:
{text_chunk}

Human Feedback from previous failed extractions (if any): {human_feedback}

Extract the CMOC structural graph immediately:
"""

def extract_cmoc_node(state: RealistReviewState) -> dict:
    """
    LangGraph Node: CMOC Extraction Agent
    """
    text_chunk = state.get("paper_text", "")
    if not text_chunk:
        return {"errors": ["No text provided for extraction."]}
        
    llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
    structured_llm = llm.with_structured_output(CMOCExtraction)
    
    prompt = ChatPromptTemplate.from_template(CMOC_EXTRACTION_PROMPT)
    chain = prompt | structured_llm
    
    try:
        extraction_result = chain.invoke({
            "record_id": state.get("record_id", "Unknown"),
            "text_chunk": text_chunk[:10000], # Process in chunks in real app
            "human_feedback": state.get("human_feedback", "None")
        })
        
        # Merge back into LangGraph state
        return {"extracted_cmocs": [extraction_result]}
        
    except Exception as e:
        return {"errors": [f"Extraction failed: {str(e)}"]}
