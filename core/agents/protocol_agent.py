"""
core/agents/protocol_agent.py — Agent 1: Protocol & IPT Agent
==============================================================
Richmond Alignment: Lead Theorist (AR)
Role: Encodes the Initial Programme Theory (IPT) and researcher-defined
rules into versioned extraction schemas that govern ALL downstream agents.

Human Reference: Richmond's team synthesized expert consensus and scoping
searches to generate their IPT based on Dual-Process Theory before any
systematic searching began.
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field
from typing import List


class IPTSchema(BaseModel):
    """Structured Initial Programme Theory output."""
    hypothesis_statement: str = Field(
        ..., description="The core 'if-then' theory statement"
    )
    key_contexts: List[str] = Field(
        ..., description="Student/teacher contexts to look for (e.g., 'low knowledge students')"
    )
    key_mechanisms: List[str] = Field(
        ..., description="Pedagogical resources and learner responses to look for"
    )
    expected_outcomes: List[str] = Field(
        ..., description="Learning outcomes the review expects to track"
    )
    inclusion_criteria: str = Field(
        ..., description="Formal inclusion/exclusion rules for screening agents"
    )
    search_keywords: List[str] = Field(
        ..., description="Keywords derived from the IPT for the Search Agent"
    )


PROTOCOL_SYSTEM_PROMPT = """You are the Lead Theorist in a RAMESES-compliant Realist Systematic Review.
Your role corresponds to the lead author (AR) in the Richmond et al. (2020) study of clinical reasoning education.

TASK: Generate a formal Initial Programme Theory (IPT) and extraction schema based on the provided review question.

RICHMOND BENCHMARK CONTEXT:
Richmond and colleagues began with Dual-Process Theory: the idea that clinical reasoning involves 
both fast/intuitive (non-analytical) and slow/deliberate (analytical) thinking. 
Their IPT focused on: WHO is the learner (context), WHAT the intervention provides (mechanism resource),
HOW the learner responds (mechanism response), and WHAT the outcome is (diagnostic accuracy, illness scripts).

OUTPUT FORMAT: Produce a structured IPT schema that will govern all downstream extraction agents.
"""

PROTOCOL_PROMPT = ChatPromptTemplate.from_messages([
    ("system", PROTOCOL_SYSTEM_PROMPT),
    ("human", """Review Question: {review_question}

Generate the Initial Programme Theory (IPT) and formal inclusion criteria for this systematic review.
The IPT should be grounded in Dual-Process Theory of clinical reasoning.
""")
])


def run_protocol_agent(review_question: str) -> dict:
    """
    Agent 1: Protocol & IPT Agent
    INPUT:  Review question from researcher
    OUTPUT: Structured IPT schema injected into shared state
    """
    llm = ChatOpenAI(model="gpt-4o", temperature=0)
    structured_llm = llm.with_structured_output(IPTSchema)
    chain = PROTOCOL_PROMPT | structured_llm

    print("\n[AGENT 1] Protocol & IPT Agent — Generating Initial Programme Theory...")
    ipt = chain.invoke({"review_question": review_question})

    log_entry = f"[Protocol Agent] IPT generated. Hypothesis: {ipt.hypothesis_statement[:80]}..."
    print(f"  IPT: {ipt.hypothesis_statement}")
    print(f"  Keywords: {ipt.search_keywords}")

    return {
        "ipt_hypothesis": ipt.hypothesis_statement,
        "inclusion_criteria": ipt.inclusion_criteria,
        "audit_log": [log_entry]
    }
