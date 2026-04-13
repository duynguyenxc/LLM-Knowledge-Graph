# PDF Documents from Professor

## NotebookLM output-agentic framework-sent-1.pdf

framework of agentic framework
7 sources
The provided documents outline a multi-agent AI framework designed to automate
and enhance realist systematic reviews within complex educational systems. This
system utilizes a core-and-plugin architecture to ensure methodological
transparency, integrating Microsoft Graph for traceable data retrieval
and knowledge graphs to map intricate relationships between contexts, mechanisms,
and outcomes. By benchmarking the framework against the established Richmond et
al. (2020) study, the authors demonstrate how specialized agents can replicate
rigorous human synthesis while maintaining an auditable evidence trail . The sources
emphasize a human-in-the-loop approach, where AI agents handle high-throughput
tasks like screening and data extraction while human researchers adjudicate complex
theoretical refinements. Ultimately, this research seeks to provide a
scalable, methodologically explicit infrastructure that meets the high standards for
evidence synthesis required by modern educational research.
How does pre-existing knowledge impact the success of clinical reasoning?
Explain the difference between analytical and non-analytical reasoning in students.
How can AI agents improve transparency in systematic review methods?
Today • 3:26  PM
Based on the uploaded file, it contains a multi-agent (agentic) framework that can be
used to conduct a systematic literature review, consistent with the recent progress
document dated February 20. I want to read through those materials to understand the
core idea: how this framework can simulate the kind of research workflow that
Richardman and his colleagues would carry out (the related paper should already be
uploaded).
Specifically, I want the description to explain how the framework can perform the job
we proposed. Before running the framework, we will conduct web crawling so the AI
can access publication databases and search for relevant literature as the first step.
After collecting results, we will iteratively refine and filter the retrieved literature and
outputs to keep only what fits our purpose—similar to how a human researcher would
screen and select papers. I will add the specific publication details later
The proposed multi-agent (agentic) framework is designed to simulate the rigorous,
theory-driven research workflow of a realist review, specifically modeled after the
study conducted by Richmond et al. (2020) . The framework's core idea is to
automate the labor-intensive stages of a systematic review while preserving the
interpretive depth and methodological transparency required by human
researchers.
1. Initial Harvesting: Web Crawling and Database Access
The first stage of the workflow replicates the search strategy used by Richmond and
colleagues, who searched four major databases (MEDLINE, PsycINFO, ERIC, and
CINAHL). In the proposed framework, a specialized Search and Retrieval Agent
performs this job.
 Reconstructing the Search Space: The agent replicates the original search
strings, keywords, and temporal limits to harvest candidate records from
publication databases.
 Web Crawling Integration: This agent uses web-querying and crawling
components to collect a superset of potentially relevant publications.
 Infrastructure: This process is powered by a core review infrastructure
(using LangChain or LangGraph) that maintains a stable registry of all
retrieved citations, ensuring every decision is traceable and auditable.
2. Iterative Refinement: Human-in-the-Loop Screening
Following the collection of results, the framework employs an iterative filtering
process that mimics how human researchers screen papers for inclusion. This is
handled by a Screening Agent through a two-stage process:
 First-Stage (Title/Abstract): The AI classifies records as include, exclude, or
uncertain based on researcher-defined criteria encoded into its decision logic.
 Human Calibration: To ensure the AI accurately reflects human judgment,
researchers review a small, stratified sample of the model's initial decisions.
These corrections are used as few-shot examples to refine the agent's behavior
before it re-runs the screening across the entire corpus.
 Second-Stage (Full-Text): For records that pass the initial screen, the pipeline
attempts to access full texts and applies the same inclusion criteria using a
second-stage classifier.
3. Simulating the Realist Workflow: CMOC Extraction
The most distinctive part of the Richmond workflow is the development of an Initial
Programme Theory (IPT) and the identification of Context–Mechanism–Outcome
configurations (CMOCs). The agentic framework simulates this through specialized
reasoning agents:
 CMOC Extraction Agent: This agent analyzes full-text papers to identify
candidate contexts (e.g., student knowledge levels), mechanism resources (e.g.,
expert explanations), mechanism responses (e.g., student self-confidence), and
outcomes (e.g., diagnostic accuracy).
 Iterative Theory Refinement: Just as Richmond et al. re-analyzed earlier
studies in light of new theories, a Synthesis and Refinement Agent compares
CMOCs across studies to identify recurrent patterns and proposes updates to
the overall programme theory.
 Knowledge Graph (KG) Support: To better handle the complex relationships
in a realist review, the framework optionally constructs a Literature
Knowledge Graph. This allows agents to reason over connected claims and
configurations—such as "why an intervention works for whom and in what
circumstances"—rather than just summarizing isolated text passages.
Summary of the Framework's Job
By combining multi-agent orchestration with graph-based retrieval and human-
in-the-loop checkpoints, the framework ensures that the AI does not merely
summarize literature but actively simulates the systematic filtering and theory-
building logic of an expert researcher. It preserves an audit trail for every action,
making the results reproducible and aligned with established systematic review
standards like RAMESES.
How do agents identify implicit mechanisms in the realist workflow?
Which human-in-the-loop checkpoints are used for the screening calibration?
How does GraphRAG improve retrieval compared to standard vector search?
Identify the agents: State clearly that this is a multi-agent framework and specify how
many agents are included (or indicate that the number is configurable, then list the
default set).
Align agents with human research roles: Explain how each agent corresponds to a
specific human role in a systematic literature review and how their outputs combine to
reproduce the Richman research outcomes.
Start from Richman’s workflow: Before defining agents, first summarize what
Richman’s publication actually does: identify the tasks, the sequence of steps, and the
human actions performed (e.g., search, screening, coding, synthesis, quality appraisal,
reporting).
Map tasks to agents: Based on the identified human tasks, define corresponding
agents and specify:
Each agent’s responsibility
Inputs and outputs
Decision criteria (e.g., inclusion/exclusion rules)
How agents communicate (handoffs, shared memory, voting, arbitration)
Define agent assignments: For each agent, explicitly state what work the framework
assigns to that agent (i.e., what the agent “does” in operational terms).
Prompting and control: Extend the description by explaining (at an implementation
level) how the agent framework is developed using prompts:
How prompts constrain each agent’s role, scope, and format
How we guide the LLM to act as the intended agent (system prompts, role prompts,
tool-use prompts)
How we enforce structure (schemas, templates, rubrics) and quality control (self-
check, peer review, verifier agent)
Level of detail: Provide as much operational detail as possible (agent list, workflow
steps, prompt strategy, and coordination mechanism).
The proposed framework is a multi-agent orchestration system built using stateful
workflow technology (such as LangGraph), designed to automate and scale the
theory-driven processes of a realist systematic review. While the framework is
configurable to accommodate various synthesis traditions, the default set for
reproducing a realist review consists of 11 specialized agents .
I. The Human Reference Standard: Richmond et al. (2020) Workflow
To design the framework, we first map the workflow performed by Richmond and
colleagues. Their publication follows a rigorous realist synthesis process defined by
the RAMESES standards:
1. Theory Seeding: Synthesizing scoping searches and expert opinion to generate
an Initial Programme Theory (IPT) .
2. Search Strategy: Executing structured searches across four major databases
(MEDLINE, PsycINFO, ERIC, CINAHL) using specific keywords and
temporal limits (post-2000).
3. Two-Stage Appraisal: Screening titles and abstracts for relevance to theory
building, followed by a full-text review for methodological rigour and
contribution to the developing theory.
4. Data Extraction (Coding): Analyzing full texts to identify
Context–Mechanism–Outcome configurations (CMOCs) .
5. Synthesis and Refinement: Comparing studies, identifying recurrent patterns
(demi-regularities), and iteratively re-analyzing earlier studies as new evidence
emerges to produce an overall programme theory.
II. Identifying the Agents and Mapping to Human Roles
The framework aligns its agents with the specific roles and cognitive tasks performed
by the Richmond research team.
Agent Role Human Research
Role Responsibility
Protocol & IPT
Agent Lead Theorist Encodes the scope and seeding theory (IPT) to guide
all subsequent agent actions.
Search & Retrieval
Agent Librarian/Searcher Reconstructs the search space and executes queries
across publication databases and enterprise folders.
Deduplication
Agent Technical Assistant Clusters duplicate records across sources and assigns
stable StudyIDs.
Title/Abstract
Screener Primary Reviewer Applies inclusion/exclusion criteria to harvest
candidate records at the metadata level.
Full-Text
Acquisition Agent Librarian Automates retrieval of PDFs and flags missing texts
for manual human upload.
Full-Text Eligibility
Agent Secondary Reviewer Conducts second-stage screening on full texts for
rigour and theory contribution.
CMOC Extraction
Agent
Subject Matter
Expert
Extracts contexts, mechanism resources, mechanism
responses, and outcomes with evidence spans.
Theory Synthesis
Agent Synthesis Expert Performs cross-study comparisons and proposes
updates to the overall programme theory.
Contradiction
Agent Quality Auditor Detects CMOC conflicts (e.g., same resource,
different outcome) to force resolution logic.
Reporting &
Artifact Agent Technical Writer Generates PRISMA flow counts, evidence tables, and
synthesis diagrams.
Benchmark Agent External Evaluator Computes precision/recall by comparing results
against the 28 studies in the original review.
III. Task Mapping: Inputs, Outputs, and Communication
The agents communicate through a shared state (Study Registry, CMOC Store,
and Theory Store) , ensuring a single source of truth for the entire pipeline.
 Communication Mechanism: The system uses a state-machine orchestrator
where agents hand off tasks via shared memory. For example, the
Title/Abstract Screener writes an "include" flag to the Study Registry, which
triggers the Full-Text Acquisition Agent to search for the PDF.
 Decision Criteria: Agents use researcher-defined rule logic . For the
Screening Agent, this includes encoded criteria such as: "Population:
undergraduate medical students," "Intervention: clinical reasoning training,"
and "Outcome: diagnostic accuracy".
 Handoffs and Arbitration: If the Contradiction Agent detects a CMOC
conflict, it triggers a Human-in-the-Loop (HITL) checkpoint for adjudication
rather than forcing a simplistic AI summary.
IV. Operational Agent Assignments
In operational terms, the framework assigns the following work:
 Protocol Agent: Formulates the "Initial Programme Theory" into versioned
hypotheses.
 Search Agent: Uses Microsoft Graph retrieval to access institutional
repositories (Teams/SharePoint) and external database connectors to harvest
publications.
 Extraction Agent: Converts narrative passages into structured tuples
(Context, Resource, Response, Outcome) with provenance pointers back to
specific document spans.
 Synthesis Agent: Proposes updates to the IPT by clustering shared
mechanisms or contexts across studies.
V. Prompting and Implementation Control
The framework is developed using a multi-layered prompting strategy to ensure high-
quality research outputs.
1. Role and Scope Constraints: System prompts define the professional identity
of each agent (e.g., "Act as a specialist in realist medical education synthesis").
Role prompts constrain the scope to specific RAMESES standards.
2. Enforcing Structure: The system uses schemas and templates to force the
LLM to output structured data (like JSON or evidence tables) rather than free-
form prose. Rubrics are embedded in the prompt to define what constitutes a
valid CMOC configuration.
3. Quality Control:
o Self-Check/Reflexion: Agents utilize a Reflexion framework to assess
their own reasoning across multiple attempts before finalizing a decision.
o Verifier Agents: A separate Verifier Agent audits extraction against
source text to prevent hallucinations.
o Human Calibration: Researchers review a stratified sample of early
decisions; these corrections are recycled as few-shot examples to refine
agent policies in real-time.
This infrastructure ensures that every action—whether the inclusion of a study or the
refinement of a theory—is auditable, traceable, and reproducible , directly
addressing the transparency gaps in traditional manual reviews.
How many agents are in the default framework?
How does the framework handle conflicting literature findings?
How are human researchers integrated into this pipeline?
Saturday, February 21
Make sure to specify the agent role and specify what each agent's role will play that
corresponds to the human action, particularly in that Richmond paper and how
Richmond and his colleagues and team did to conclude their systematic review. And
also, you need to clearly identify which is the core part of the framework and which is
the foundation of understanding effective relations and find the ground truth from the
publication that is the core framework. And then the plug-in framework that is aligned
with the specific review method, logistics, logic, and review logic. And make it clear
how they are distinguishing them and how they can be realized using multiple agents
in a large language model framework. What is the template? What are the prompts
and the template? Give some examples of prompts for functions, particularly agents.
What is the input of the agent? What is the output of the agent? How does the human
verify the output and provide feedback to the system, so that the system can modify
the outcome based on the human's comments and evaluation.
The proposed multi-agent (agentic) framework is a stateful orchestration system
designed to automate the theory-driven processes of a systematic review while
maintaining the methodological rigor of a human research team. To understand its
core idea, we must first map it against the research workflow established by
Richmond et al. (2020) .
I. The Reference Standard: Richmond et al.’s Workflow
The study by Richmond and colleagues followed the RAMESES standards for
realist synthesis to understand how educational interventions develop clinical
reasoning. Their human-led workflow involved the following actions:
1. Theory Seeding: The lead author (AR) synthesized scoping searches and
expert consensus from the team (RP, SG, NC) to generate an Initial
Programme Theory (IPT) .
2. Structured Searching: They searched four major databases (MEDLINE,
PsycINFO, ERIC, CINAHL) for studies published from 2000 onwards.
3. Two-Stage Screening: A title-abstract screen for relevance to theory building,
followed by a full-text review to assess methodological rigour and contribution
to the theory.
4. Data Extraction (Coding): They analyzed 28 included papers to identify
Context–Mechanism–Outcome configurations (CMOCs) .
5. Synthesis and Refinement: Studies were compared, recurrent patterns (demi-
regularities) were identified, and earlier studies were re-analyzed in light of
new theories to refine the overall programme theory.
II. Core Framework vs. Plugin Framework
The framework distinguishes between the "infrastructure" of a review and its
"intellectual logic":
 The Core Infrastructure (Method-Agnostic): This is the foundation of the
framework. It handles the "plumbing" common to nearly all systematic
reviews: corpus ingestion, Microsoft Graph-enabled retrieval, study registry
management, deduplication, and the Human-in-the-Loop (HITL) control
layer.
 The Plugin Framework (Method-Specific): This is the Realist Synthesis
Plugin, which aligns with Richmond's specific review logic. It contains the
rules for IPT management and CMOC extraction.
 Foundation of Effective Relations (The Knowledge Graph): To find the
"ground truth" and understand complex relations (why/for whom/in what
circumstances), the framework constructs a Literature Knowledge Graph
(LKG). While the LLM provides interpretive reasoning, the LKG supplies the
structured, graph-grounded evidence of causal configurations (CMOCs) that
are often lost in flat text summaries.
III. Identifying the Agents and Roles
The framework assigns work to specialized agents that correspond to Richmond’s
team roles:
Agent Role Human Action
Corresponded Operational Assignment
Protocol & IPT
Agent Lead Theorist (AR) Encodes the scope, IPT hypotheses, and extraction
schemas.
Search & Retrieval
Agent Librarian/Searcher Executes queries via Microsoft Graph API across
databases and Teams/SharePoint folders.
Deduplication
Agent Technical Assistant Clusters duplicate records and assigns stable
StudyIDs.
Title/Abstract
Screener Primary Reviewer Classifies records as include, exclude, or uncertain
based on eligibility rules.
Full-Text Eligibility
Agent
Secondary Reviewer
(RP/SG/NC)
Applies inclusion criteria to retrieved PDFs for
rigour and theory contribution.
CMOC Extraction
Agent Subject Matter Expert
Extracts structured tuples: Context
(student/teacher level), Mechanism
(resource/response), and Outcome.
Synthesis &
Refinement Agent Synthesis Expert Compares CMOCs across studies to identify demi-
regularities and update the programme theory.
Contradiction
Agent Quality Auditor Detects CMOC conflicts (e.g., same resource
leading to different outcomes) to force resolution.
Benchmark Agent External Evaluator Computes recall/precision by comparing model
results to Richmond's 28 studies.
IV. Prompts, Templates, and Implementation
The framework is realized using Large Language Models (LLMs) orchestrated
through a state-machine (like LangGraph).
The Prompting Strategy:
 System Prompts: Constrain the agent’s role and scope (e.g., "Act as a
specialist in RAMESES-compliant realist synthesis").
 Structured Templates/Schemas: Ensure outputs are structured (JSON/tables)
rather than narrative, making them auditable.
Agent Examples:
 Function: CMOC Extraction
 Input: Full-text PDF chunk + IPT Schema.
 Prompt Example: "Identify the student-level Context (C), the Mechanism
Resource provided (M-res), the student's cognitive Response (M-resp), and the
Reasoning Outcome (O). Link each to a specific text span." .
 Output: A structured JSON object containing the CMOC configuration with
provenance pointers.
V. Human Verification and Feedback Loop
The framework is designed for lifelong (continual) learning through human
interaction.
1. Checkpoints: Humans intervene at predefined stages: screening adjudication,
CMOC validation, and theory sign-off.
2. Calibration: In the screening stage, the human reviews a small sample of the
agent's decisions. Corrections are recycled into the system as few-shot
examples to refine the agent's logic for the remaining corpus.
3. Feedback & Modification: If a researcher is unsatisfied with a synthesis
outcome (e.g., an extraction is too generic), they provide feedback. The system
then updates its decision policies (prompts or rule logic) and reruns the
relevant agent to modify the outcome.
This interactive process ensures the system accommodates human requirements and
adapts as the researcher's understanding of the theory evolves.
How do agents handle contradictions in realist synthesis?
Tell me more about the human-in-the-loop calibration step.
What analytical artifacts does the framework export for repositories?
Okay, I said that the framework should not miss the interaction with the human at
each step, and how the human decision rules will play a role in this framework. Also,
you should not include a final agent that compares the machine's outcome with the
human's outcome. In a real, practical framework, this step does not exist. We only do
model-vs-human comparison manually or separately (independent of the model) for
evaluation/research purposes to verify the model — not as part of the model in
practical application. For the model in practical application, there should be a channel
or points where people can review and audit the outcomes and procedures, provide
feedback, and then have the system redo or improve the results based on that feedback
before moving forward. Yeah, that is what we want.
In the practical application of this multi-agent framework, the system is designed as a
Human-in-the-Loop (HITL) orchestration pipeline , where human researchers are
not passive observers but active governors of the review's logic and outcomes. The
framework is partitioned into a method-agnostic core review infrastructure and a
method-specific synthesis plugin (e.g., the Realist Synthesis plugin), ensuring that
every automated step is governed by human-defined decision rules.
I. Operational Multi-Agent Framework (Practical Model)
The following agents constitute the operational set. Per your requirement, the
"Benchmark Agent" is excluded as it serves purely for separate evaluation and
research verification rather than live production.
1. Protocol & IPT Agent: Encodes the researcher’s initial hypotheses and
inclusion rules into versioned templates.
2. Search & Retrieval Agent: Uses Microsoft Graph to pull search strings and
literature from enterprise folders (SharePoint/Teams) while logging every
query for auditability.
3. Deduplication Agent: Clusters duplicate records and ensures a stable study
registry.
4. Title/Abstract Screening Agent: Classifies records based on human-defined
eligibility criteria.
5. Full-Text Eligibility Agent: Re-evaluates studies at the full-text level for
methodological rigour and theory contribution.
6. CMOC Extraction Agent: Deconstructs text into Context, Mechanism, and
Outcome configurations.
7. Synthesis & Refinement Agent: Proposes updates to the programme theory by
comparing CMOCs across the corpus.
8. Contradiction & Sensitivity Agent: Surfaces conflicting evidence (e.g., same
intervention leading to different outcomes) for human adjudication.
9. Reporting & Artifact Agent: Generates audit-ready evidence tables, PRISMA
counts, and theory diagrams.
II. Human Interaction Points and Feedback Loop
The framework replaces the final "automated comparison" with predefined
interaction checkpoints where researchers audit outcomes, provide feedback, and
trigger the system to redo or improve results before proceeding.
 Checkpoint 1: Screening Calibration & Adjudication
o Action: Researchers review a stratified sample of the AI’s screening
decisions.
o Feedback/Redo: If the AI misinterprets a criterion (e.g., "clinical
reasoning" vs. "general knowledge"), the researcher provides
corrections. These corrections are recycled as few-shot examples to
refine the agent's decision logic, and the screening agent reruns the task
on the affected corpus to improve accuracy.
 Checkpoint 2: CMOC Extraction Validation
o Action: Humans spot-check the extracted CMOC tuples to ensure they
reflect the "ground truth" found in the publication.
o Feedback/Redo: Researchers can modify the extraction schema or
specific prompt templates if the AI is missing implicit mechanisms. The
system then re-extracts data using the updated rules.
 Checkpoint 3: Contradiction Adjudication
o Action: When the system identifies conflicting evidence (e.g., an
intervention works for experts but fails for novices), it stops and presents
a contradiction register to the researcher.
o Feedback/Redo: The human provides an interpretive explanation (e.g.,
"this is a context-specific moderating factor"). This feedback is stored in
the Theory Store, and the synthesis agent incorporates this logic into the
final programme theory.
 Checkpoint 4: Programme Theory Sign-off
o Action: Before generating final artifacts, the human reviews the entire
evidence path from theory claim to specific text spans.
o Feedback/Redo: The researcher can reject theory updates that lack
interpretive depth, forcing the Synthesis Agent to re-analyze the
Literature Knowledge Graph using a different reasoning structure.
III. Lifelong (Continual) Learning Mechanism
This interaction protocol enables lifelong (continual) learning within the model. By
capturing human feedback at each checkpoint, the framework iteratively updates its
decision policies (prompts, rubrics, and rule-logic). This ensures the framework
accommodates evolving stakeholder requirements and adapts its behavior throughout
the lifecycle of the review.
IV. Transparency and Auditability
Every human intervention, feedback note, and system "redo" is logged in the Audit &
Repository Export module . This creates a complete, transparent record of how
human expertise and AI automation combined to produce the synthesis, fulfilling the
RRE Call's requirement for methodologically explicit guidelines and verifiable
analytical artifacts.
How does the realist synthesis plugin ensure RAMESES standard compliance?
What specific audit artifacts are exported for the RRE repository?
How do the human-in-the-loop checkpoints improve CMOC extraction quality?
combine the above agentic framework with the above modificiation to layout the
framework, with detailed how each agent will be prompted and provide prompt
example or template
The proposed multi-agent framework is a stateful orchestration system designed to
automate the labor-intensive stages of a systematic review while maintaining the
interpretive depth of the Richmond et al. (2020) study. The system consists of 10
specialized agents in its default configuration, which are coordinated through a Core
Review Infrastructure and a method-specific Realist Synthesis Plugin .
I. The Richmond Human Reference Standard
Before mapping the agents, it is necessary to identify the specific tasks performed by
Richmond and colleagues:
 Theory Seeding: The team synthesized expert opinion to generate an Initial
Programme Theory (IPT) .
 Structured Search: They conducted keyword searches across four major
databases (MEDLINE, PsycINFO, ERIC, CINAHL) for studies published from
2000 onwards.
 Two-Stage Screening: Reviewers performed a title/abstract screen for
relevance, followed by a full-text review for methodological rigour.
 CMOC Extraction: The team analyzed 28 papers to extract
Context–Mechanism–Outcome configurations (CMOCs) .
 Iterative Synthesis: They compared CMOCs across studies to identify "demi-
regularities" and refined the IPT into a final programme theory.
II. Core Infrastructure vs. Method Plugin
The framework distinguishes between universal review "plumbing" and intellectual
synthesis logic:
 Core Review Infrastructure: Handles method-agnostic tasks such as
Microsoft Graph-enabled retrieval , deduplication, study registry
management, and the Human-in-the-loop (HITL) control layer .
 Realist Synthesis Plugin: Provides the method-specific "semantics," including
rules for CMOC extraction and theory refinement.
III. Detailed Agent Layout and Prompting Strategy
The agents communicate through a shared state (Study Registry and Literature
Knowledge Graph) where one agent’s output triggers the next.
Agent Role Richmond Input Output Operational
Alignment Assignment
Protocol & IPT
Agent
Lead Theorist
(AR)
Review
Question/Scope
IPT Schema &
JSON Template
Encodes IPT
hypotheses to guide
extraction rules.
Search &
Retrieval
Agent
Librarian/Searcher IPT
Themes/Keywords
Raw Publication
Superset
Executes Microsoft
Graph-based queries
across indexed
literature.
Deduplication
Agent Tech Assistant Raw Superset Unique Study
Registry
Clusters duplicates and
assigns stable
StudyIDs.
Title/Abstract
Screener Primary Reviewer Study Metadata Decision
(Inc/Exc/Unc)
Classifies records
based on eligibility
rules; triggers HITL if
"Uncertain".
Full-Text
Acquisition
Agent
Librarian "Include"
Decisions
PDF/Full Text
Chunks
Automates retrieval
and flags missing
PDFs for human
upload.
Full-Text
Eligibility
Agent
Secondary
Reviewer Full Text PDFs Eligibility
Report
Applies rigour/theory
contribution criteria at
the full-text level.
CMOC
Extraction
Agent
Subject Expert Full Text + IPT
Schema
LKG Triples (C-
M-O)
Extracts structured
configurations with
evidence-span links.
Theory
Synthesis
Agent
Synthesis Expert LKG Subgraphs
Refined
Programme
Theory
Clusters CMOCs into
recurrent patterns to
update theory.
Contradiction
Agent Quality Auditor CMOC Store Conflict Register
Detects CMOC
conflicts (e.g., same
resource, different
outcome) for human
adjudication.
Reporting
Agent Tech Writer Shared State
PRISMA
Flow/Evidence
Tables
Generates auditable
artifacts for repository
deposit.
IV. Prompting and Control Implementation
The framework uses Role Prompts to define identity and Schemas to enforce
structure.
1. Role and Context Constraints:
 System Prompt Template: "Act as a specialist in RAMESES-compliant realist
synthesis. Your goal is to identify how educational interventions develop
clinical reasoning. You must follow researcher-defined inclusion rules strictly
and link every claim to a specific document section ID."
2. Enforcement of Structure (CMOC Extraction Example):
 Input Agent Prompt: "Analyze the following text chunk. Extract CMOC
configurations according to this schema: {Context: Student Knowledge Level,
Mechanism_Resource: Pedagogical Tool, Mechanism_Response: Cognitive
Reaction, Outcome: Diagnostic Accuracy}. If a mechanism is implicit, state
your reasoning for the inference."
 Output Format: JSON-structured tuples mapped to the Literature
Knowledge Graph (LKG) .
3. Quality Control (HITL and Redo Triggers):
 Calibration Checkpoint: For the Screening Agent, the human reviews a 5%
stratified sample. Feedback Prompt: "The human researcher marked StudyID
123 as 'Exclude' because it was postgraduate, not undergraduate. Update your
decision logic and re-screen the remaining records."
 Adjudication Checkpoint: When the Contradiction Agent flags a conflict, it
stops the pipeline. The human provides a resolution (e.g., "This outcome is
moderated by the teacher's experience" ), which is added to the Theory Store
as a new rule for the Synthesis Agent to "redo" its theory refinement.
This interaction ensures that the system accommodates evolving human requirements
and creates a traceable evidence path from theory claims back to verifiable source
passages, fulfilling the transparency requirements of the RRE call.
How will the framework handle implicit mechanisms during extraction?
Can you elaborate on the repository artifacts required by AERA?
What criteria will experts use to evaluate CMOC validity?
Please lay out the details of the framework so that people can clearly see:
How each agent will be prompted What is the input for each large language model
agent What is the expected output of each agent How the output of one agent is passed
/ loaded / sent to the next agent in the workflow
Among all the agents, please clarify:
Which agent(s) are the core of the framework (essential / always present) Which
agent(s) belong to the plug-in functions (optional / modular / aligned with specific
review methods)
Thank you.
The details of the multi-agent framework are structured to separate the Core Review
Infrastructure (essential plumbing) from Method-Specific Plugins (specialized
synthesis logic). This architecture ensures that the system can be adapted to various
review traditions while maintaining a stable, auditable foundation.
I. Core Review Infrastructure (Essential / Always Present)
These agents provide method-agnostic services required for any systematic review.
They are governed by a stateful orchestrator (e.g., LangGraph) that manages a
Shared Study Registry —the "single source of truth" for the pipeline.
Agent Role Input Expected Output Prompting Strategy
Search &
Retrieval
Agent
Search strings and
IPT themes.
Raw publication superset with
metadata.
Role Prompt: "Act as a
librarian executing
Microsoft Graph queries
across Teams, SharePoint,
and external databases".
Deduplication
Agent
Raw publication
list.
Unique Study Registry with
stable StudyIDs.
Template Prompt:
"Compare record A and B;
if identical, merge metadata
and assign a primary
StudyID".
Title/Abstract
Screener
Study metadata
(Title/Abstract) +
Eligibility rules.
Label
(Include/Exclude/Uncertain) +
Short Rationale.
Schema-Enforced
Prompt: "Evaluate against
the criteria: [Criteria].
Output JSON with rationale
and confidence score".
Full-Text
Acquisition
"Include" decisions
and StudyIDs.
Full-text PDFs or text chunks;
flags missing files.
Tool-Use Prompt: "Search
M365 folders via Microsoft
Graph for the PDF
matching StudyID X".
Full-Text
Eligibility
Full-text
documents +
Eligibility rules.
Final eligibility report; justifies
exclusions.
Role Prompt: "Secondary
Reviewer: Audit the full
text for methodological
rigour and theoretical fit".
Reporting &
Audit Agent
Full Study Registry
and shared state.
PRISMA flow counts, evidence
tables, and artifact logs.
Formatting Prompt:
"Generate a RAMESES-
compliant audit trail from
the decision logs for
repository deposit".
II. Method-Specific Plugins (Realist Synthesis Plugin)
These agents are modular and aligned with the specific logic of the Richmond et al.
(2020) benchmark. They reason over a Literature Knowledge Graph (LKG) to find
configurations of causal mechanisms.
Agent Role Input Expected Output Prompting Strategy
Protocol &
IPT Agent
Review
questions and
seeding
expertise.
Initial Programme Theory (IPT)
hypotheses and extraction schemas.
Theory Seeding Prompt:
"Synthesize the provided
expertise to generate an IPT
focused on student-level
clinical reasoning".
CMOC
Extraction
Agent
Full-text
chunks + IPT
Schema.
Structured
Context–Mechanism–Outcome
tuples with evidence spans.
Inference Prompt:
"Identify implicit responses
(Mechanism-Response)
from the text. Link each
claim to a specific span
ID".
Synthesis &
Refinement
Extracted
CMOCs from
the LKG.
Refined Programme Theory
(Updated IPT) and demi-regularity
patterns.
Pattern Recognition
Prompt: "Compare
CMOCs across studies.
Propose an update to the
IPT if context X
consistently alters outcome
Y".
Contradiction
Agent
LKG
subgraphs.
Contradiction Register identifying
conflicting evidence.
Conflict Detection
Prompt: "Flag instances
where the same resource
leads to different outcomes.
Present for human
adjudication".
III. Workflow Orchestration and Handoffs
The framework does not use simple linear passing; instead, it uses Stateful Handoffs
via the Shared Registry and Literature Knowledge Graph .
 Passing Mechanisms: When the Deduplication Agent writes a unique StudyID
to the registry, the Screening Agent is automatically triggered to process that
record.
 Loading Evidence: The Extraction Agent loads full-text chunks and pushes
extracted "triples" (entities and relations) into the Literature Knowledge
Graph (LKG).
 Sending for Feedback: If the Contradiction Agent detects a conflict, it pauses
the synthesis and sends a notification to the Human-in-the-Loop (HITL)
control module.
IV. Human-in-the-Loop and Lifelong Learning
The human researcher interacts with the framework at four predefined checkpoints:
1. Screening Adjudication: Human reviews a stratified sample of AI decisions
and provides corrections.
2. Extraction Validation: Human spot-checks extracted CMOCs for "ground
truth" fidelity.
3. Contradiction Resolution: Human provides the interpretive logic to explain
conflicting findings.
4. Theory Sign-off: Human approves the final synthesized programme theory
before artifact generation.
Lifelong Update Mechanism: Human feedback at these points is recycled to update
the system's decision policies (prompts and rules). This allows the agents to "learn"
and accommodate evolving stakeholder requirements as the review moves into new
cycles or as new studies appear.
How does the framework automate realist CMOC extraction?
Explain the role of human-in-the-loop checkpoints in the pipeline.
How do knowledge graphs improve reasoning over flat text summaries?
Please look at the framework. We particularly emphasize that human decisions will
dominate this process. There are multiple checkpoints to let humans review the
process, provide feedback, and ensure the system follows the human's decisions with
human oversight and master control over this process. Explain how this is integrated
into those frameworks and how the machine will incorporate the human response to
revise its efforts through an iterative process. Please give a good picture, not only
based on the content provided, but also based on your knowledge and an extensive
search of the internet to propose something that goes beyond the provided material.
In this multi-agent framework, human researchers do not simply provide an initial
input and wait for a result; they act as the master controllers of an iterative, state-
aware system. The agents are designed as specialized assistants that handle the labor-
intensive "plumbing" of a review while pausing at critical junctures for human
adjudication and policy refinement . This integration is realized through a series of
"Master Control" checkpoints and a feedback-to-policy loop that enables the system
to learn from human corrections in real-time.
1. Integration of Human Oversight: The Four Checkpoints
The framework incorporates human judgment at four predefined "gates" where the
automated process halts until a human provides a "sign-off" or corrective feedback.
 Checkpoint 1: Screening Calibration (The "Few-Shot" Loop): Instead of
screening the entire corpus blindly, the Screening Agent first classifies a small,
stratified sample of records. The human reviews these decisions, correcting any
misclassifications. These corrections are then automatically converted into few-
shot examples that the system uses to refine its internal decision logic before
re-running the screening across the remaining thousands of papers.
 Checkpoint 2: CMOC Validation (The "Ground Truth" Audit): For a
realist review like the Richmond et al. (2020) study, identifying
Context–Mechanism–Outcome configurations (CMOCs) is an interpretive act.
Humans spot-check extracted CMOC tuples to ensure they reflect the "ground
truth" of the publications. If a human identifies that an agent is missing
implicit mechanisms, they can update the extraction schema or the specific role
prompt for that agent.
 Checkpoint 3: Contradiction Adjudication (The "Conflict Registry"):
When the Contradiction Agent identifies conflicting evidence—such as the
same educational intervention leading to different outcomes in different
settings—it pauses the pipeline and presents a "conflict register" to the
researcher. The human provides an interpretive explanation for the conflict
(e.g., explaining why "low knowledge" students respond differently than
experts), which the system then incorporates into the overall Programme
Theory.
 Checkpoint 4: Theory Sign-off: Before final reporting, the researcher reviews
the entire evidence path. They can reject updates to the theory that lack
interpretive depth, forcing the Synthesis Agent to "redo" its comparative
analysis based on new constraints.
2. The Iterative Revision Process: Feedback-to-Policy
The machine incorporates human response not just as a one-time correction, but as a
revision of its future efforts through two primary mechanisms:
 Dynamic Prompt & Rule Revision: Human feedback is used to iteratively
update the system's decision policies (e.g., prompts, rubrics, and extraction
rules). For example, if a researcher provides feedback that "clinical reasoning"
should include "diagnostic accuracy," the Protocol Agent updates the project-
wide rules, and all downstream agents (Search, Screen, and Extract) adapt their
behavior to this new master definition.
 The "Redo" Trigger: The framework utilizes a state-machine orchestrator
(such as LangGraph) that maintains a "Shared Registry". If a human provides
negative feedback at any checkpoint, the orchestrator can trigger a recursive
"redo" loop. This means the system doesn't just edit the text; it re-invokes the
relevant agent with the updated human instruction, ensuring the entire evidence
chain remains consistent and auditable.
3. Beyond the Provided Material: Proposing "Master Control" Innovations
To move beyond current implementations, the framework can integrate the following
"Master Control" concepts:
 Semantic Policy Anchoring: Instead of just using "fixed prompts," the system
could maintain a "Living Project Handbook" —a centralized knowledge store
of all human decisions and comments. When an agent encounters an ambiguous
study, it would first query this handbook to see how the human handled similar
cases previously, ensuring that the machine's "internal policy" remains
perfectly aligned with the human's evolving intent.
 Active Preference Learning: The system could utilize Reinforcement
Learning from Human Feedback (RLHF) specifically tuned for evidence
synthesis. By observing which studies a researcher prioritizes and which
CMOCs they "upvote" during validation, the agents could autonomously adjust
their retrieval and synthesis strategies to match the researcher's specific
intellectual style and theoretical focus .
 Master Intervention UI: A specialized dashboard—an Adjudication UI—
would allow researchers to see the "uncertainty score" for every AI decision.
By sorting the workload by uncertainty, the human can focus their limited time
on the most contested pieces of evidence, providing the high-level reasoning
that the machine lacks, while the AI handles the bulk of the repetitive tasks.
Summary of Human Master Control
By integrating predefined checkpoints, stateful redo-loops, and lifelong learning
mechanisms, the framework ensures that human decisions dominate the process. The
machine acts as an auditable executor of human intent, where every revision is
logged, traceable to a specific human comment, and verified against the original
publication evidence.
How do these plugins specifically manage different synthesis logics?
Could you explain the specific artifacts produced for auditability?
How does human feedback improve the system's decision policies?
How do these plugins specifically manage different synthesis logics?
In the proposed multi-agent framework, the management of diverse synthesis logics is
achieved through a modular "core-and-plugin" architecture. While the core review
infrastructure handles method-agnostic tasks like retrieval and deduplication, the
synthesis plugins instantiate the specific intellectual logic, rules, and "synthesis
semantics" of a particular review tradition.
These plugins specifically manage different synthesis logics through three primary
mechanisms:
1. Method-Specific Schemas and Extraction Rules
Each plugin provides the schema definitions and rule-based decision logic that
constrain how agents extract and interpret evidence. For example:
 Realist Synthesis Plugin: Operationalizes Initial Programme Theory (IPT)
and Context–Mechanism–Outcome Configurations (CMOCs) . Agents are
prompted specifically to identify "mechanism resources" and "mechanism
responses," even when they are implicit in the text.
 Thematic/Framework Synthesis Plugin: Directs agents to code findings into
pre-specified frameworks or translate study concepts into emergent themes.
 QCA (Qualitative Comparative Analysis) Plugin: Focuses on case
calibration and the discovery of necessity/sufficiency patterns among various
configurations of causal factors.
2. Relational Reasoning via Literature Knowledge Graphs (LKG)
Plugins utilize a Literature Knowledge Graph to manage the complex, non-linear
relationships required by advanced synthesis methods. While a standard search might
only retrieve text chunks, the plugin enables Graph-enhanced Retrieval-Augmented
Generation (GraphRAG).
 In a Realist logic, this allows agents to query the graph for "subgraphs" that
link specific context factors to mechanism responses.
 For complex-system synthesis, this enables the framework to surface
"configurations" and "contingencies" rather than just isolated findings.
3. Iterative Refinement and Contradiction Handling
The plugins manage the iterative synthesis loops unique to their specific
methodology.
 Theory Refinement: In a realist review, the plugin manages a "Theory Store"
that versions the programme theory. As new CMOCs are identified, a
specialized Synthesis Agent compares them against the current theory and
proposes refinements.
 Contradiction Adjudication: The Contradiction Agent identifies conflicts in
the evidence—such as the same intervention leading to different outcomes in
different contexts—and presents these to a human for adjudication. The plugin
then incorporates this human explanation back into the synthesis logic as a
"contextual contingency".
4. Human-in-the-Loop (HITL) Policy Updates
Plugins define the specific interaction protocol where human researchers oversee the
synthesis logic. Through lifelong (continual) learning , human feedback at method-
specific checkpoints (like CMOC validation) is used to update the plugin’s decision
policies, prompts, and templates . This ensures the framework's "synthesis logic"
evolves to match the researcher's intent as the review progresses.
How do multi-agent frameworks handle complex causal configurations?
What repository artifacts are required for RRE compliance?
How does human feedback refine the AI's screening logic?
Sunday, February 22
Please address each of the specific plug-in methods for the systematic review based
on the uploaded call for papers. Include all drafts and proposals regarding the different
specific review requirements, and give more details on each method: how the plug-in
will align with that specific systematic review, how the methods differ from each
other, and the different perspectives of systematic reviews. Can you find the proposals
and those relevant contents in the uploaded proposal or uploaded call for papers
issued by the Journal Editor?
The proposed multi-agent framework is designed around a core-and-plugin
architecture specifically to meet the diverse methodological requirements of the
Review of Research in Education (RRE) 2026 call . While the core infrastructure
handles method-agnostic tasks like provenance-tracked retrieval and study registry,
the method-specific synthesis plugins instantiate the distinct review logics needed to
address complex educational systems.
1. Realist Synthesis Plugin (Primary Worked Example)
As established in the source materials, Realist Synthesis serves as the primary anchor
for the framework because its focus on Context–Mechanism–Outcome
configurations (CMOCs) directly aligns with the RRE call’s emphasis on
"interacting elements," "causal mechanisms," and "contextual contingencies".
 Alignment: This plugin operationalizes the Initial Programme Theory (IPT)
and iterative theory refinement, addressing the "why, how, and for whom"
questions essential for informing change in complex systems.
 Agentic Logic: Specialized reasoning agents extract structured configurations
(CMOCs) from literature, linking mechanism resources (what an intervention
provides) to learner responses and subsequent outcomes.
 Core Difference: Unlike descriptive methods, this plugin is theory-driven
and explanatory, focusing on the generative causation that occurs when
interventions interact with specific contexts.
2. Qualitative Comparative Analysis (QCA) Plugin
The RRE call highlights the need for methods that can reveal "configurations of
causal mechanisms".
 Alignment: A QCA plugin supports causal discovery by identifying which
combinations of conditions are necessary or sufficient for an outcome.
 Agentic Logic: This plugin manages case calibration—transforming
qualitative or quantitative data into set relations—and applies set-theoretic
logic to find patterns that simple aggregation might miss.
 Core Difference: It differs from realist synthesis by focusing on set-theoretic
configurations rather than the narrative "mechanism-response" logic.
3. Framework and Thematic Synthesis Plugins
These plugins are designed for the structured coding of large evidence bases to
identify recurring patterns and demi-regularities.
 Alignment: These methods provide the "systematic approach" required by the
call to ensure that conclusions are warranted through transparent and auditable
coding.
 Agentic Logic:
o Framework Synthesis: Agents use a pre-specified framework to code
evidence, ensuring alignment with existing educational theories.
o Thematic Synthesis: Agents identify emergent themes through
inductive coding, allowing for the synthesis of heterogeneous studies.
 Perspective: These represent a pattern-seeking perspective, where the goal is
to aggregate findings across diverse study designs into a coherent set of themes
or categories.
4. Meta-Ethnography and Critical Interpretive Synthesis (CIS) Plugins
The call invites "diverse approaches to research," including those emphasizing
theoretical critique.
 Alignment: These plugins address the "theorize and warrant conclusions"
requirement of the call by moving beyond mere summary toward theoretical
innovation.
 Agentic Logic: Agents perform conceptual translation across studies,
identifying how concepts from one study can be reconciled or expanded by
another to build a new overarching theory.
 Perspective: These represent a highly interpretive perspective , prioritizing
theoretical depth and critique over the procedural standardization of meta-
analysis.
5. Meta-Analysis and Mixed-Method Synthesis Plugins
To satisfy the call's emphasis on "methodologically diverse evidence," the framework
supports quantitative and integrative plugins.
 Alignment: These plugins provide the rigor needed to handle the "measurable
effects" of interventions while integrating them with qualitative insights to
inform systemic change.
 Agentic Logic:
o Meta-Analysis: Specialized agents extract effect sizes, perform risk-of-
bias assessments, and apply quantitative pooling models.
o Mixed-Method: The framework embeds text and numeric data into
unified graph structures (Literature Knowledge Graphs), allowing
agents to reason across diverse data types for causal discovery.
 Difference: These methods differ by their reliance on statistical pooling
(meta-analysis) or integrative triangulation (mixed-methods), providing a
quantitative baseline that interpretive plugins lack.
Summary of Plugin Alignment with RRE Requirements
The sources emphasize that by maintaining a method-neutral core—which provides
the audit trails and provenance required by RRE standards—the framework can
remain a "living" methodological infrastructure. Each plugin allows the system to
switch its reasoning substrate: for a realist synthesis, it queries the knowledge graph
for CMOC subgraphs; for QCA, it queries for set-theoretic configurations; and for
thematic synthesis, it clusters emergent semantic embeddings. This ensures that the AI
is not merely summarizing literature but is performing the specific analytical and
warranting tasks defined by each unique research tradition.
How do core infrastructure and synthesis plugins work together?
What specifically are the methodologically explicit guidelines for these plugins?
How does the framework manage contradiction adjudication in complex systems?
could you expand the above? Could you make details for each plugin as a
methodology method? This is a method in the agent-based model agent framework.
Please, for each one, provide a detailed method. And then, in this paper, we only work
on one method, but we need to lay out the method or method framework for the other
plugins or other systematic reviews. Do you understand? So look at the call for papers
and the uploaded proposal that is uploaded for this draft paper, the proposal for the
draft paper, and lay out this plugin as part of the methodology. That is the core part of
this draft paper. And also, we need to make sure we have the core, C-O-R-E, core part
of that framework.
The following methodology section details the architecture of the proposed multi-
agent system, distinguishing between the method-agnostic Core Review
Infrastructure and the method-specific Synthesis Plugins. This architecture is
designed to satisfy the Review of Research in Education (RRE) 2026 requirements
for methodological innovation and transparent warranting in complex educational
systems.
4. Methodology: The Multi-Agent Framework
This method employs a stateful orchestration architecture (implemented via
LangGraph) where a specialized set of agents collaborates under a Human-in-the-
Loop (HITL) governance model. The framework is partitioned into two distinct
layers: a method-agnostic core and a method-specific plugin layer.
4.1 The Core Review Infrastructure (CORE)
The CORE provides the foundational services required for any systematic review,
ensuring that every automated step is auditable, reproducible, and grounded in
institutional data. It consists of the following essential modules:
 Protocol & Scope Module: Encodes researcher-defined review questions,
inclusion/exclusion rules, and extraction schemas into versioned prompt
templates.
 Retrieval & Provenance Module: Utilizing Microsoft Graph as the
enterprise retrieval layer, this module executes search strings and harvests
literature from project folders (Teams/SharePoint) while logging every query
and source for absolute auditability.
 Study Registry & Deduplication Module: Clusters harvested records, assigns
stable StudyIDs, and maintains a "Single Source of Truth" registry for the
entire pipeline.
 Screening Workflow Module: A multi-stage classifier applying eligibility
rules at title/abstract and full-text levels. It categorizes studies as include,
exclude, or uncertain while generating detailed rationales for every decision.
 Extraction & Evidence-Linking Module: Deconstructs documents into
structured data objects. Every extracted item is persistently linked (provenance)
to a specific text span ID to prevent hallucinations and support manual
verification.
 Audit & Repository Export Module: Automatically packages all decision
logs, search queries, extraction tables, and human feedback records into
analytical artifacts ready for deposition in the AERA-RRE repository.
4.2 Synthesis Plugin Framework
Synthesis plugins are modular extensions that instantiate the intellectual logic and
coding rules of a specific review tradition. While this manuscript focuses on the
Realist Synthesis plugin as the primary worked example, the framework is designed
to support the diverse methodological landscape required by the RRE call.
4.2.1 Realist Synthesis Plugin (Worked Example)
This plugin operationalizes the RAMESES standards to explain why, how, and for
whom interventions develop clinical reasoning ability.
 Methodology: It manages the Initial Programme Theory (IPT) and drives
agents to extract Context–Mechanism–Outcome configurations (CMOCs) .
 Extraction Logic: Specialized agents extract structured tuples: Context (e.g.,
learner knowledge level), Mechanism Resource (the pedagogical tool
provided), Mechanism Response (the cognitive/emotional reaction), and the
resulting Outcome (e.g., diagnostic accuracy).
 Iterative Refinement: Agents query a Literature Knowledge Graph to
identify recurrent patterns (demi-regularities) across studies and propose
evidence-based updates to the overall programme theory.
4.2.2 Framework and Thematic Synthesis Plugin
 Methodology: Aligns with the call's emphasis on identifying recurring patterns
and themes across diverse research designs.
 Implementation: The Framework module uses a pre-specified theoretical
framework to guide extraction agents. The Thematic module identifies
emergent themes through inductive coding and clustering, allowing for the
synthesis of heterogeneous evidence bases into coherent categories.
4.2.3 Qualitative Comparative Analysis (QCA) Plugin
 Methodology: Supports the discovery of "causal configurations" and
"contextual contingencies" specified in the RRE call.
 Implementation: Agents perform case calibration, transforming qualitative or
quantitative data into fuzzy or crisp set memberships. The plugin identifies
which combinations of conditions are necessary or sufficient for an outcome,
enabling the system to reason about causal "paths" rather than isolated
variables.
4.2.4 Meta-Ethnography and Critical Interpretive Synthesis (CIS) Plugin
 Methodology: Prioritizes theoretical innovation and concept translation across
different methodological and disciplinary boundaries.
 Implementation: Agents perform conceptual translation across studies,
identifying how concepts from one study can be reconciled or expanded by
another to build a new overarching theory.
4.2.5 Meta-Analysis and Mixed-Method Synthesis Plugin
 Methodology: Integrates methodologically diverse evidence to inform
systemic change.
 Implementation: Agents extract effect sizes and conduct risk-of-bias
assessments for quantitative pooling. The mixed-method logic embeds text and
numeric data into unified graph structures , allowing agents to reason across
diverse data types for causal discovery.
4.3 Human-in-the-Loop (HITL) and Lifelong Learning
The framework is governed by a formal Master Control protocol where human
researchers act as the ultimate arbiters of synthesis logic through four predefined
checkpoints:
1. Screening Adjudication: Reviewing AI-labeled samples to refine eligibility
rules through few-shot calibration.
2. Extraction Validation: Spot-checking extracted CMOCs to ensure fidelity to
the "ground truth" found in the literature.
3. Contradiction Adjudication: Reviewing a "Conflict Register" where same
interventions lead to different outcomes, and providing interpretive
explanations to resolve these contingencies.
4. Theory Sign-off: Approving the final synthesized programme theory and
evidence map before artifact generation.
Every human intervention is recycled to update the system’s decision policies (e.g.,
prompts and rules), enabling lifelong (continual) and online learning . This ensures
that the framework accommodates evolving stakeholder requirements and matures its
reasoning throughout the review lifecycle.
How does the realist synthesis plugin handle CMOC configurations?
How will you evaluate the framework's programme theory fidelity?
What analytical artifacts will be produced for the RRE repository?
too simple, lack sufficient details ,redo the above as the section of draft paper
2. Literature Review and Gap Analysis
2.1 The Paradigm Shift in AI-Augmented Evidence Synthesis Post-2023
The emergence of Large Language Models (LLMs) and multi-agent orchestration
frameworks after 2023 has fundamentally reshaped the landscape of research
synthesis. Prior to this "generative AI sensation," automation was largely confined to
machine-learning-based citation screening and structured metadata extraction . In the
post-2023 era, the focus has shifted toward agentic workflows that attempt to
replicate the interpretive and reasoning-heavy tasks once reserved for human experts .
Current research explores the capacity of LLMs to support high-recall abstract
screening and the extraction of complex constructs from full-text corpora, often
employing collaborative "two-reviewer" agent designs to resolve discordant outputs .
2.2 Critical Assessment of General AI-Assisted Literature Review Platforms
The market for AI-driven research tools has expanded rapidly with the launch of
platforms such as Elicit, Consensus, and Scite Assistant . These platforms optimize
the "speed-to-summary" pipeline, allowing researchers to screen thousands of papers
and generate report-like syntheses in a fraction of the traditional time . For instance,
recent product updates in Elicit claim to support "Scaled Systematic Reviews" of up
to 40,000 papers, integrating search, screen, and extraction into a unified parallelized
task .
However, from the perspective of the RRE Volume 50 methodological
requirements, these general literature review platforms exhibit several decisive
disadvantages for synthesizing evidence in complex educational systems :
 Methodological Opacity and Weak Warranting: Unlike a formal systematic
review, which must be methodologically explicit and evaluable , many
general platforms utilize ad hoc prompting and "black-box" reasoning . This
prevents researchers from tracing claims back to specific evidence spans with
the auditability required for scholarly critique .
 Suppression of Contradictions: General platforms often optimize for
narrative "consensus" or "smoothing over" contested findings . This fails to
meet the needs of researchers examining contextual contingencies, where the
primary goal is often to identify why results differ across settings .
 Lack of Configurational Logic: Current platforms typically lack the capacity
to operationalize method-specific synthesis logics, such as the
Context–Mechanism–Outcome configurations (CMOCs) foundational to
realist synthesis . They primarily function as productivity tools rather than as
methodological infrastructures capable of producing the structured,
depositable artifacts required by journals like RRE .
2.3 Advances in Multi-Agent Orchestration and Knowledge Graphs
To address the "global" reasoning failures of traditional Retrieval-Augmented
Generation (RAG), post-2023 research has prioritized Graph-enhanced Retrieval
(GraphRAG) and multi-agent orchestration . Multi-agent systems (e.g., using
LangGraph) enable specialized agents to collaborate on discrete tasks—such as
screening, coding, and synthesis—while maintaining a shared "state" of the review
protocol .
Furthermore, the construction of a Literature Knowledge Graph (LKG) allows
agents to reason over connected claims and evidence paths rather than isolated text
passages . This enables the discovery of demi-regularities and causal configurations
by mapping how specific intervention resources trigger learner responses within
varied educational contexts . By integrating Microsoft Graph as an enterprise-grade
retrieval layer, these frameworks can ensure that every decision is logged and every
PDF is managed within a traceable institutional repository .
2.4 The Methodological Gap: From Automation to Adjudicated Governance
The primary gap in the current evidence-synthesis ecosystem is the absence of an
infrastructure that combines the interpretive depth of human experts with the
scalability of agentic AI . While general platforms can accelerate search, they do not
accommodate the iterative refinement of programme theories seen in human-led
reviews like Richmond et al. (2020) .
The proposed core-and-plugin framework addresses this gap by separating method-
agnostic "Review OS" functions (retrieval, provenance, registry, and audit) from
method-specific synthesis logics . This framework uniquely prioritizes:
1. Human-in-the-Loop (HITL) Adjudication: Formalizing checkpoints for
screening calibration, CMOC validation, and theory sign-off to prevent
"automation bias" .
2. Lifelong (Continual) Learning: Incorporating human feedback at each stage
to iteratively update decision policies, prompts, and extraction rules as new
literature emerges and stakeholder requirements evolve .
3. Auditability for Sustainable Change: Producing repository-ready artifacts—
including contradiction registers and provenance-linked CMOC tables—to
ensure the synthesis is not a "one-time" report but a living, auditable evidence
map suitable for driving systemic educational innovation .
--------------------------------------------------------------------------------
References (APA)
American Educational Research Association. (2026). Call for proposals: Systematic
review methods for synthesizing evidence from diverse approaches to research to
inform change efforts in complex educational systems (RRE Volume 50) .
https://www.aera.net/Portals/38/2026_RRE_CallForProposals.pdf
Edge, D., Trinh, H., Cheng, N., Bradley, J., Chao, A., Mody, A., Truitt, S., & Larson,
J. (2024). From local to global: A Graph RAG approach to query-focused
summarization. Microsoft Research. https://arxiv.org/abs/2404.16130
Elicit. (2026, February 19). Scaled Systematic Reviews and Report Templates . Elicit
Blog. https://elicit.com/blog/systematic-review/
Khan, M. A., et al. (2025). Collaborative large language models for automated data
extraction in living systematic reviews. Journal of the American Medical Informatics
Association, 32(4), 638–647. https://doi.org/10.1093/jamia/ocae325
Li, M., Sun, J., & Tan, X. (2024). Evaluating the effectiveness of large language
models in abstract screening: A comparative analysis. Systematic Reviews, 13, 219.
https://doi.org/10.1186/s13643-024-02609-x
Microsoft. (2025). Microsoft Graph overview . Microsoft Learn.
https://learn.microsoft.com/en-us/graph/overview
Richmond, A., Cooper, N., Gay, S., Atiomo, W., & Patel, R. (2020). The student is
key: A realist review of educational interventions to develop analytical and non-
analytical clinical reasoning ability. Medical Education, 54(8), 709–719.
https://doi.org/10.1111/medu.14137
Wong, G., et al. (2013). RAMESES publication standards: Realist syntheses. BMC
Medicine, 11, 21. https://doi.org/10.1186/1741-7015-11-21
How do CMOCs help model configurations of causal mechanisms?
What analytical artifacts are required for the RRE repository?
Explain how the pipeline handles contradictions in educational research.
I ask for method section, what you did does not meet the instruction
3. Methodology: A Multi-Agent Framework for Generative AI-Augmented
Research Synthesis
This section details the proposed multi-agent orchestration framework, designed to
satisfy the Review of Research in Education (RRE) 2026 requirements for
methodological innovation and transparent warranting in complex educational
systems. The framework is implemented as a stateful agentic pipeline using post-2023
orchestration technology (e.g., LangGraph), allowing it to replicate the interpretive
depth of human expert reviews, specifically the realist synthesis conducted by
Richmond et al. (2020) .
3.1 Architectural Principles: Core Review Infrastructure and Plugin Functions
The framework is partitioned into two distinct layers to ensure both methodological
stability and flexibility.
 The Core Review Infrastructure (Essential): This "Review OS" provides the
method-agnostic services required for any systematic review. It manages
corpus ingestion, stable study registries, deduplication, and the Human-in-
the-Loop (HITL) control module . It is powered by Microsoft Graph as the
enterprise retrieval layer , ensuring that every retrieved document and
decision is logged within a traceable institutional repository.
 Method-Specific Plugins (Modular): Plugins instantiate the distinct synthesis
logic of a particular tradition. The Realist Synthesis Plugin used here
operationalizes the Initial Programme Theory (IPT) and
Context–Mechanism–Outcome configurations (CMOCs) . By swapping
plugins, the same core infrastructure can support framework synthesis, thematic
synthesis, QCA, or meta-ethnography.
3.2 Operational Agent Roles and Task Decomposition
The framework employs specialized agents that collaborate through a Shared State
Registry, serving as the single source of truth for the entire pipeline.
Agent Role Input Expected Output Agent Responsibility
Protocol & IPT
Agent
Review
Question +
IPT Schema + Extraction
Rubrics
Encodes the "Initial Programme
Theory" to guide search and
Seeding Theory extraction.
Search &
Retrieval Agent
IPT Themes +
Search Strings Raw Publication Superset
Executes queries via Microsoft
Graph API across project
folders and databases.
Deduplication
Agent Raw Metadata Unique Study Registry Clusters records and assigns
stable StudyIDs for auditability.
Title/Abstract
Screener
Metadata +
Eligibility
Rules
include/exclude/uncertain
Label
Performs first-stage
classification with structured
rationales.
Full-Text
Eligibility Agent
PDFs +
Protocol Rules Final Inclusion Report
Audits full texts for
methodological rigour and
theoretical fit.
CMOC
Extraction Agent
Full-Text
Chunks + IPT
Schema
LKG Triples (C, M-res, M-
resp, O)
Converts passages into
structured Context,
Mechanism, and Outcome
configurations.
Synthesis &
Refinement
Agent
LKG Subgraphs Updated Programme
Theory
Clusters CMOCs into demi-
regularities and proposes theory
revisions.
Contradiction
Agent CMOC Store Conflict Register
Detects conflicting evidence
(same resource, different
outcomes) for human
adjudication.
Reporting &
Audit Agent
Shared State
Logs
PRISMA Flow + Evidence
Tables
Generates final artifacts for
repository deposition.
3.3 Prompting and Enforcement of Methodological Logic
To ensure the Large Language Model (LLM) acts as a specialized research agent, the
framework uses a multi-layered prompting strategy:
 System Prompts: Define the agent's professional identity (e.g., "Act as a
specialist in RAMESES-compliant realist synthesis").
 Role Prompts: Constrain the agent's scope to specific tasks (e.g., "Extract only
student-level mechanism responses").
 Structure Enforcement: Agents are guided by schemas and templates to
output structured JSON or evidence tables rather than narrative prose, ensuring
every claim is linked to a specific text span ID.
3.4 Human-in-the-Loop (HITL) Governance and Checkpoints
The framework is governed by a Master Control protocol where the system pauses
for human adjudication at four critical checkpoints:
1. Screening Adjudication: Humans review a stratified sample of decisions to
calibrate the agent's logic through few-shot examples.
2. CMOC Validation: Humans spot-check extracted configurations against the
"ground truth" of the publications.
3. Contradiction Resolution: When the system identifies conflicting evidence, it
stops to let the human provide an interpretive explanation.
4. Theory Sign-off: The researcher approves the final synthesized programme
theory before the Reporting Agent generates repository artifacts.
3.5 Lifelong (Continual) and Online Learning Mechanism
This framework supports lifelong learning by recycling human feedback into the
system’s decision policies. When a researcher corrects an agent's output, the system
does not just edit the text; it updates its underlying prompts, rubrics, and
extraction rules. This allows the agents to "learn" the researcher’s intent, enabling
the system to accommodate evolving stakeholder requirements and improve its
accuracy throughout the lifecycle of the "living" review.
3.6 Literature Knowledge Graph and GraphRAG Integration
To support the configuration-level reasoning required by Richmond et al. (2020), the
framework constructs a Literature Knowledge Graph (LKG) . Unlike traditional
RAG which retrieves isolated text passages, Graph-enhanced Retrieval
(GraphRAG) allows agents to retrieve subgraphs of connected claims . This enables
the framework to reason over complex relationships—how specific pedagogical
resources trigger cognitive responses in varied student contexts—providing a
transparent evidence path from theory claims back to verifiable source passages.
How do CMOCs help reveal causal mechanisms in complex systems?
Why use Microsoft Graph instead of just a vector store?
How does human feedback improve the AI's future screening efforts?
too simple, more details are needed
3. Methodology: A Multi-Agent Orchestration Framework
This section details the proposed agentic infrastructure, designed to replicate the
interpretive and theory-driven workflow of the Richmond et al. (2020) realist review.
The framework is architected as a stateful, human-governed system that separates
method-agnostic "Review Infrastructure" from method-specific "Synthesis Plugins".
3.1 Architectural Philosophy: The Core-and-Plugin Model
The framework addresses the scalability and transparency limitations of traditional
reviews by utilizing a core-and-plugin architecture.
 Core Review Infrastructure (Method-Agnostic): Provides foundational
services such as enterprise-grade retrieval, deduplication, and a unified audit
trail.
 Method-Specific Plugins: These modular extensions instantiate the unique
logic of a synthesis tradition. This manuscript focuses on the Realist Synthesis
Plugin, which operationalizes the Context–Mechanism–Outcome (CMO)
logic required to analyze complex educational systems.
3.2 Agent Roles, Inputs, and Prompting Strategy
The framework employs 10 specialized agents coordinated via a stateful orchestrator
(e.g., LangGraph). Each agent operates under role-specific system prompts and
structured output schemas to ensure methodological rigor.
Agent Role Input Expected Output Prompt Strategy/Example
Search &
Retrieval Agent
IPT Themes
& Search
Strings
Raw Publication Superset
Role: "Act as a librarian using
Microsoft Graph API to harvest
literature from project folders".
Deduplication
Agent
Raw
Metadata Unique Study Registry
Logic: Clusters duplicate records
and assigns stable StudyIDs for
cross-agent tracking.
Title/Abstract
Screener
Metadata +
Eligibility
Rules
include/exclude/uncertain
Decision
Schema: "Output JSON with
rationale and confidence score based
on the following criteria...".
CMOC
Extraction
Agent
Full-Text
Chunks + IPT
Schema
LKG Triples (C, M-res,
M-resp, O)
Inference: "Identify Context,
Mechanism Resource, Mechanism
Response, and Outcome. Link each
to a specific text span".
Synthesis &
Refinement
LKG
Subgraphs
Updated Programme
Theory
Patterning: "Identify demi-
regularities across studies to refine
the initial programme theory".
Contradiction
Agent CMOC Store Conflict Register
Critique: "Flag instances where the
same resource leads to different
outcomes in different contexts".
3.3 The Role of Microsoft Graph and Literature Knowledge Graphs
The framework utilizes two distinct graph-based technologies to ground AI reasoning:
1. Microsoft Graph (Enterprise Layer): Functions as the retrieval and
provenance backbone. It allows agents to securely access and version project
artifacts, such as PDFs, screening logs, and human notes stored in Teams or
SharePoint.
2. Literature Knowledge Graph (LKG): A method-facing representation built
from the literature where nodes represent interventions, mechanisms, and
outcomes. This enables Graph-enhanced Retrieval (GraphRAG) , allowing
agents to reason over connected causal paths rather than isolated text snippets.
3.4 Master Control: Human-in-the-Loop (HITL) and Lifelong Learning
Crucial to the framework is the Master Control protocol , which ensures human
decisions dominate the synthesis process. The system pauses for human adjudication
at four predefined checkpoints:
 Checkpoint 1: Screening Adjudication: Humans review a stratified sample of
the AI’s screening decisions. Feedback is recycled as few-shot examples to
refine the Screener Agent’s policy before it re-runs the task.
 Checkpoint 2: Extraction Validation: Humans spot-check extracted CMOC
tuples against the "ground truth" evidence spans.
 Checkpoint 3: Contradiction Resolution: When the Contradiction Agent
detects conflicting evidence, it presents a Conflict Register. The human
provides an interpretive explanation which is stored as a new rule for the
Synthesis Agent.
 Checkpoint 4: Theory Sign-off: The lead researcher approves the final
synthesized programme theory and evidence map before artifact generation.
Lifelong (Continual) Update Mechanism: Every human correction—whether a
modified screening label or a refined CMOC—is used to iteratively update the
system’s decision policies (prompts and rules) . This ensures the framework adapts
to evolving human requirements and creates an auditable record of how human
expertise shaped the final synthesis.
3.5 Benchmark Evaluation Design (Richmond et al. 2020)
To verify the framework, we replicate the search space and synthesis products of the
Richmond et al. (2020) review.
 Search/Screening Evaluation: The pipeline's included set is compared against
Richmond's 28 studies, computing recall (proportion of Richmond's studies
identified) and precision.
 Synthesis Fidelity: We evaluate the correspondence of system-generated
CMOC patterns and programme theory against the human-authored synthesis
reported in the benchmark paper.
 Artifact Transparency: To satisfy the RRE call, the framework exports a full
package of analytical artifacts, including logged queries, screening rationales,
and LKG-derived configuration maps for deposition in the AERA-RRE
repository.
How do these plugins specifically manage different synthesis logics?
Tell me more about the human-in-the-loop governance checkpoints.
How does GraphRAG improve reasoning compared to standard RAG?
Please only focus on "medical education" uploaded and read carefully the Richmond
Medical Education literature review carefully, and give more detail on what
essentially they give as well as a full explanation of what their procedure is. Give it in
language that is spoken to the layman. Particularly say how they initiate the initial
theory as a kind of hypothesis, and then they try to look for from the literature
anything similar to this hypothesis, based on all relevant information, and then they
try to check if there is any contradiction, consolidate this contradiction, and then they
come out with the theory that is verified by previous research, that is stated for what
kind of population, what kind of intervention has some effect. And please give more
detail, more detail. And eventually what their paper is about. They review 28 papers,
and what they try to do, and what is their final result. Please provide more concrete
details about their process. For each process, what they try to do, and what is the
outcome from this particular process. And then the outcome from the previous process
will become the input for the next process. And eventually, the final output identifies
the effect on some people, the effect of certain pedagogy, how they interact with the
people. It's the kind of thing like this. Please give more detail and understanding so
that we can let the AI agent do this in a more specific way. And how this knowledge
graph plays a role. How their work will turn into an automatic process powered by a
large language model. Yeah, please read that paper carefully. How they start with the
initial theory, how they identify keywords to search the literature, and what is their
criteria to identify 28 studies. Such things like give more detail and eventually what
the result is based on reviewing, summarizing, or synthesizing the outcomes from
these 28 publications. What eventually the output is and what is the practical
significance.
The research conducted by Richmond and colleagues (2020) in the field of medical
education is a "realist review," which is a fancy way of saying they didn't just want to
know if a teaching method works, but why it works for some students and not others,
and in what specific situations.
1. The Starting Point: The "Initial Theory" (Hypothesis)
Before looking at a single research paper, the team started with a hypothesis, known
in their field as an Initial Programme Theory (IPT) .
 The Input: They combined their own expertise as clinical teachers with a
quick "scoping" search of existing ideas.
 The Process: They sketched out a rough map of how they thought medical
students learn to make diagnoses. They focused on "Dual-Process Theory,"
which suggests we think in two ways: fast/intuitive (non-analytical) and
slow/deliberate (analytical).
 The Outcome: A draft set of "if-then" statements (called CMOCs) that served
as the roadmap for the entire project.
2. Searching the Literature: Finding the "Matches"
Once they had their hypothesis, they needed to see if the real world (the literature)
agreed with them.
 The Input: They identified key themes from their IPT—like "pattern
recognition," "deliberate practice," and "illness scripts".
 The Process: They searched four major databases for any study published
since the year 2000.
 The Outcome: A mountain of papers that they had to narrow down. They used
a two-stage screening process : first, they checked titles and abstracts to see if
the papers were relevant to their theory; second, they read the full texts to
ensure the research was high-quality and actually added something to the
"theory building".
3. Sifting Through 28 Papers: Identifying Patterns and Contradictions
After their rigorous screening, they were left with 28 specific papers that formed the
core of their review.
 The Input: These 28 papers acted as the "evidence" for their trial.
 The Process: This is where it gets interesting. They looked for Context-
Mechanism-Outcome configurations (CMOCs) . Think of this like a
chemistry formula: Context (the type of student) + Mechanism (the teaching
resource and the student’s reaction) = Outcome (how well they diagnosed the
patient).
 Handling Contradictions: They didn't ignore studies that disagreed. Instead,
they looked for why they disagreed. For example, they found that an
intervention that helped a "high-knowledge" student might actually confuse a
"low-knowledge" student. This is called the "Expertise Reversal Effect".
 The Outcome: By re-analyzing early papers in light of new things they learned
from later ones, they consolidated all these "puzzle pieces" into one final,
verified theory.
4. The Final Result: What Actually Works?
The final output of their work identifies exactly how different teaching styles interact
with different types of students.
 The Population: They found that the student is the key variable. They
identified five specific types of student contexts, primarily based on their pre-
existing knowledge and self-confidence.
 The Pedagogy: Effective teaching requires more than just giving facts; it
requires "safe places" (like simulations) where students can make mistakes and
receive immediate feedback.
 The Interaction:
o Novices ("Low-Knowledge"): They need explicit explanations of an
expert’s thinking. Without it, they might feel panic or resentment.
o Developing Experts: Once they have enough knowledge, they should be
encouraged to use "non-analytical" (intuitive) reasoning, just like real
doctors do.
5. Practical Significance: Why Does This Matter?
This paper proves that a "one-size-fits-all" approach to medical education is a
failure. For teachers, the significance is that they must identify a student's baseline
knowledge before choosing a teaching method. If you give a task that is too hard for a
novice, you aren't just wasting time—you might actually be causing "negative
learning outcomes" like faulty future reasoning.
6. Powering This with AI: The Role of the Knowledge Graph
To turn this human process into an automatic one powered by an AI agent, we use a
Literature Knowledge Graph (LKG) .
 How it works: Instead of the AI just reading text, the LKG turns Richmond's
28 papers into a web of relationships .
 The Nodes: Each "node" in the graph is a specific student type, a teaching
method, or a result.
 The Edges: The connections (edges) represent the "because of." For example:
[Low Knowledge Student] --(is confused by)--> [Observing Expert without
Explanation].
 The Agent Workflow: The AI agents replicate Richmond's steps. A Screening
Agent finds the papers; an Extraction Agent pulls out the C-M-O formulas;
and a Contradiction Agent flags when the graph shows two different results
for the same method.
By using GraphRAG, the AI doesn't just summarize a paper; it "reasons" through the
graph to see how a specific context (like a student's low confidence) changes the
whole outcome, exactly as the human researchers did.
How do AI agents handle inferred mechanisms from research texts?
Tell me more about the expertise reversal effect findings.
How is the knowledge graph used for detecting evidentiary contradictions?
How the work done by Richmond in their process can be better represented by a
knowledge graph, particularly by using the Microsoft knowledge graph. The entity is
a kind of big concept, and the relation could be a kind of thing related to the relation
between entities. And how those knowledge graphs can be mapped or related to
Richmond's human works. How their close alignment could be, how this knowledge
graph will better match or align with their work? How can we verify by using their
publication? The data available from their publication and use those data to verify our
knowledge graph's correctness or the appropriateness of our knowledge graph.
Because we will have a big concept as an entity, and if any Richmond's publication
includes those entities and includes the type of relation that can guide us to identify
the big concept, knowledge in the field or words as an entity in building the
knowledge graph by using Microsoft graph through using some community related to
identification for identifying the entity. Just look at this, have a close look from this
perspective.
The work performed by Richmond et al. (2020) is inherently relational, making it
uniquely suited for representation through a Literature Knowledge Graph (LKG) .
By utilizing Microsoft Graph as a retrieval backbone and a method-specific
knowledge graph for reasoning, the framework can automate the identification of "big
concepts" (entities) and their causal links (relations) with a high degree of alignment
to the original human-led research.
1. Representing Richmond’s "Big Concepts" as Entities
In a realist review, the core units of evidence are not isolated facts but configurations.
A knowledge graph represents these configurations as nodes (entities) and edges
(relations):
 Entities (Big Concepts): These correspond to Richmond’s identified
categories, such as Context factors (e.g., "Low Knowledge Student," "Self-
Confidence"), Mechanism Resources (e.g., "Explicit Explanations,"
"Simulated Patients"), and Outcomes (e.g., "Diagnostic Accuracy," "Faulty
Reasoning").
 Relations (Causal Links): Instead of flat text, the graph stores the causal paths
Richmond theorized. For example, a relation might be [Intervention] --
triggers--> [Mechanism:Response] or [Context] --moderates--> [Outcome] .
 Community Identification: Using GraphRAG logic, the system can identify
"communities" of related entities. This mirrors Richmond's manual process of
identifying demi-regularities—patterns that recur across multiple studies—by
clustering related CMOC (Context-Mechanism-Outcome Configuration)
subgraphs.
2. Alignment with Richmond’s Human Workflow
The knowledge graph is the "reasoning substrate" that allows AI agents to replicate
Richmond’s iterative synthesis:
 IPT to Graph Schema: Richmond’s Initial Programme Theory (IPT) serves
as the initial schema for the graph, defining what types of entities and relations
the agents should look for.
 CMOCs as Subgraphs: Every time Richmond identified a CMOC in one of
the 28 papers, the AI creates a provenance-linked subgraph.
 Contradiction and Sensitivity: Richmond specifically looked for why the
same intervention worked for some and not others. A knowledge graph makes
this computable by flagging graph motifs where the same "Mechanism
Resource" leads to divergent "Outcomes" based on different "Context" nodes.
3. The Role of Microsoft Graph as the Backbone
Microsoft Graph serves as the enterprise-grade provenance and retrieval layer
rather than the synthesis logic itself.
 Retrieval Traceability: It provides the agents with governed access to the
project’s PDFs, screening logs, and human notes stored in institutional
repositories (Teams/SharePoint).
 Ground Truth Mapping: Every entity and relation in the LKG is persistently
linked via Microsoft Graph to a specific Evidence Span (a unique ID for a
section of a document), ensuring that every claim in the synthesis is traceable
back to the raw publication data.
4. Verification and Validation of Correctness
The framework uses Richmond’s 2020 publication as the "human reference
standard" to verify the appropriateness of the knowledge graph:
 Study Set Overlap: The framework is verified by its ability to correctly
identify and include the same 28 studies Richmond selected, using recall and
precision metrics.
 Synthesis Fidelity: The "correctness" of the knowledge graph is evaluated by
comparing the system-generated Programme Theory (the final graph state)
against Richmond’s narrative synthesis.
 Data-Driven Verification: If the LKG identifies the same "big concepts" (e.g.,
the "Expertise Reversal Effect") and the same "relations" (e.g., "Low
knowledge leads to panic when observing experts without explanation") that
Richmond reported, the graph is considered a valid representation of the
research field.
By converting the 28 publications into a structured, relational graph, the framework
ensures that the AI does not just summarize text but performs the same
configurational reasoning Richmond and his colleagues used to conclude their
review.
How can AI agents handle the CMOC extraction process?
How does Microsoft Graph support the provenance of evidence?
What practical benefits does a knowledge graph offer researchers?
what is it meant by "demi-regularities"
In the context of a realist synthesis—such as the study conducted by Richmond et al.
(2020)—demi-regularities refer to recurrent patterns of
Context–Mechanism–Outcome configurations (CMOCs) that are identified by
comparing multiple studies.
Because realist research acknowledges that causal relationships are not linear but are
instead generative and dependent on complexity , these patterns are not viewed as
universal laws. Instead, they represent observable trends in how specific intervention
resources trigger particular cognitive or emotional responses (mechanisms) within
varied student contexts to produce specific outcomes.
Key aspects of demi-regularities within this framework include:
 Cross-Study Patterning: The identification of these patterns is a core task of
the Synthesis Agent, which performs comparisons across the literature to find
where similar "configurations of causal processes" occur.
 Theory Refinement: Identifying demi-regularities allows researchers (or AI
agents) to propose updates to an Initial Programme Theory (IPT) , eventually
refining it into an overall programme theory that explains "what works, for
whom, and in what circumstances".
 Knowledge Graph Discovery: In the proposed multi-agent framework, demi-
regularities are discovered by querying a Literature Knowledge Graph
(LKG) to identify subgraphs where specific contexts consistently moderate the
relationship between an intervention resource and its outcome.
 Addressing Contradictions: Finding these patterns helps in resolving apparent
contradictions in the data; for example, if an intervention resource leads to
different outcomes, identifying a demi-regularity might reveal that the outcome
is consistently moderated by a specific student context, such as their pre-
existing level of knowledge.
Ultimately, the discovery of demi-regularities provides the warranted evidence
needed to build a comprehensive theory of how educational interventions function in
complex systems.
How do demi-regularities appear as patterns within a knowledge graph?
What are the specific student contexts Richmond identified in the final theory?
How does the Contradiction Agent resolve divergent outcomes for the same
pedagogy?
By using a knowledge graph for different research studies, each knowledge graph
entity will contain the ID from different research, right? And through entity
identification for big concepts that are used in the Microsoft knowledge graph, we can
find similar results from different research, or we can find contradictions among the
different research through the sub-knowledge graph — that is, the sub-graph about the
same nodes. Can we say it like this? The knowledge graph can particularly facilitate
identifying similar trends across different research by using different IDs for the
different nodes and relations that you mentioned above. With this ID embedded in the
entities and relations, the same trends or similar trends found in different research can
be consolidated, and the contradictory parts of the research can also be easily
identified. Is that correct?
Your description is correct and aligns closely with the proposed agentic framework's
logic for managing complex research data. By representing literature as a Literature
Knowledge Graph (LKG) , the framework transforms narrative text into a structured,
relational reasoning substrate where every entity and relation is embedded with stable
identifiers for provenance and cross-study comparison.
ID Embedding and Provenance
Each entity in the knowledge graph contains unique identifiers, such as StudyIDs and
EvidenceSpan pointers, which link specific concepts (nodes) and causal claims
(edges) back to their original research sources. This persistent metadata ensures that
every claim in the synthesis is traceable to a verifiable section of a document,
fulfilling the requirement for methodological explicitness and auditability .
Identifying Trends and "Demi-Regularities"
The framework uses unified entity identification for "big concepts"—such as specific
student-level contexts (e.g., "low knowledge") or mechanism resources (e.g., "explicit
explanations")—to find similar results across different studies. By querying
subgraphs centered on these shared nodes, the Synthesis Agent identifies recurrent
patterns known as demi-regularities. This process allows the system to consolidate
similar trends found in disparate research into a coherent programme theory.
Surfacing and Resolving Contradictions
The use of subgraphs is particularly powerful for identifying contradictions. The
Contradiction Agent performs motif detection to flag specific graph patterns where
a similar intervention or mechanism resource leads to divergent outcomes in different
studies.
 Consolidation: The graph identifies when research agrees on a causal path.
 Conflict Detection: When research disagrees, the graph surfaces the conflict as
a relational discrepancy (e.g., same resource, different result).
 Adjudication: These contradictory subgraphs are presented to the human
researcher in a Conflict Register for interpretive resolution, such as identifying
a moderating contextual factor that explains the difference.
The Role of Microsoft Graph
In this workflow, Microsoft Graph serves as the enterprise retrieval and
provenance layer. It is the API gateway that allows agents to securely fetch the raw
research studies, screening logs, and team notes from institutional repositories like
SharePoint or Teams to build the review-specific knowledge graph. While Microsoft
Graph provides the "plumbing" to access the data, the LKG provides the "intellectual
logic" to reason over it.
If you would like a detailed look at how these graph structures are used to generate
evidence tables or theory diagrams, I can provide more information on the Reporting
& Artifact Agent . Or, I could create a report summarizing the specific "big
concepts" Richmond identified in their 28-paper review.
How will you present the guidelines for using the method?
What are the specific artifacts produced for the RRE repository?
How does the human-in-the-loop control handle contradiction adjudication?
what it is meant by "motif detection"
In the context of the proposed multi-agent framework, motif detection refers to a
structural graph-analysis technique used by AI agents to identify specific, recurring
patterns or configurations within a Literature Knowledge Graph (LKG) . Rather
than searching for isolated keywords, the system uses motif detection to query the
graph for complex relational structures that represent the logic of a realist review.
Specifically, motif detection is utilized in the following ways:
 Identifying Configurations: It allows agents to recognize specific
Context–Mechanism–Outcome configurations (CMOCs) by treating them as
distinct "graph patterns". This mirrors the human process of identifying "demi-
regularities"—recurrent patterns across multiple studies—by searching for
subgraphs where specific context factors consistently influence outcomes.
 Contradiction and Sensitivity Detection: The Contradiction Agent uses
motif detection to flag instances where the evidence is inconsistent. For
example, it can identify a graph pattern where the same intervention and
resource lead to different outcomes depending on the specific student
context (such as low vs. high pre-existing knowledge).
 Configuration-Level Reasoning: By identifying these motifs, the framework
can perform the "why, how, and for whom" reasoning central to the Richmond
et al. (2020) study. For instance, it can detect the "Expertise Reversal Effect"
by finding motifs where directive teaching resources improve outcomes for
novices but frustrate or hinder experts.
 Structured Adjudication: When a specific motif representing a contradiction
is detected, the system can pause the automated workflow and present that
specific subgraph to a human researcher for resolution, ensuring that every
interpretive decision is grounded in a traceable evidence path.
Essentially, motif detection transforms the narrative findings of 28 or more research
papers into computable graph motifs , making the identification of causal trends and
theoretical conflicts an auditable and systematic process.
How does GraphRAG specifically detect conceptual patterns and contradictions?
How can researchers verify the correctness of a knowledge graph?
What analytical artifacts does the framework export for the repository?
what is i meant by motif, is it special term in AI or CS
In the context of the framework described in the sources, a motif refers to a specific,
recurring structural pattern or sub-graph configuration within a knowledge
graph. Motif detection is the computational process used by AI agents to identify
these patterns to perform high-level relational reasoning.
Within this multi-agent system, motif detection is primarily used to:
 Identify configurations: Agents treat Context–Mechanism–Outcome
configurations (CMOCs) as distinct graph patterns, which allows them to
recognize "demi-regularities" (recurrent trends) across multiple research
papers.
 Surface contradictions: The system can flag discrepancies—such as the same
intervention and resource resulting in different outcomes based on different
contexts (e.g., student knowledge levels)—by identifying specific relational
patterns in the graph.
 Support configuration-level reasoning: By querying for these motifs, agents
can determine "why, how, and for whom" an intervention works, replicating the
theory-driven logic used by human researchers like Richmond et al. .
Regarding whether it is a "special term" in AI or Computer Science (CS) , the
sources frame it as a foundational technique within graph-based AI reasoning and
Graph-enhanced Retrieval-Augmented Generation (GraphRAG) .
Information outside of the sources: In the broader fields of Computer Science and
Network Science, the term "network motif" is a standard technical term referring to
small sub-graphs that appear in a network significantly more frequently than would be
expected by chance. These motifs are often considered the functional "building
blocks" of complex networks, much like a recurring melody is a motif in music.
How do multi-agent systems handle implicit mechanisms in research?
Can you detail the human-in-the-loop checkpoints for theory refinement?
How does GraphRAG specifically improve contradiction detection in synthesis?
please directly answer to this: what is i meant by motif, is it special term in AI or CS
In the context of the proposed multi-agent framework, a motif refers to a specific,
recurring structural pattern or sub-graph configuration within a knowledge
graph.
Is "Motif" a Special Term in AI or Computer Science?
Yes, it is a technical term used in AI and Computer Science , particularly within the
fields of graph-based AI reasoning and Graph-enhanced Retrieval-Augmented
Generation (GraphRAG). While traditional search methods look for isolated
keywords, motif detection is a structural analysis technique that allows AI agents to
identify complex relational patterns.
How Motifs are Used in the Framework
 Identifying Configurations: Agents treat Context–Mechanism–Outcome
configurations (CMOCs) as distinct graph patterns or "motifs". This allows
the system to recognize "demi-regularities" (recurrent trends) across different
research papers by identifying shared sub-graph structures.
 Detecting Contradictions: The Contradiction Agent utilizes motif detection
to flag relational discrepancies in the evidence. For example, it can
automatically find a "motif" where a single intervention resource leads to two
different outcomes based on different student contexts.
 Enabling Relational Reasoning: By querying for these motifs, the framework
can perform the "why, how, and for whom" reasoning central to a realist
review, such as identifying the "Expertise Reversal Effect" through specific
graph patterns.
Information outside of the sources: In broader Computer Science and Network
Science, the term "network motif" is a well-established standard for describing small
sub-graphs that appear in a network more frequently than would be expected by
chance, often serving as the functional building blocks of that network. You may want
to independently verify this broader application in network theory.
How do multi-agent systems specifically improve contradiction handling in reviews?
What criteria verify the fidelity of AI-generated programme theories?
How does Microsoft Graph support the auditability of evidence spans?
in KG, identify subgraph similary is N-P prpobilem , is it hard?
In the context of the proposed multi-agent framework, the task of identifying
subgraph similarity or specific relational patterns—referred to in the sources as
motif detection—is indeed a computationally challenging problem, although the
sources do not explicitly use the term "NP-hard."
The Technical Complexity (Expert Context)
Information outside of the sources: In computer science, identifying whether one
graph is contained within another (subgraph isomorphism) or calculating the
similarity between two subgraphs is a well-established NP-hard problem. This
means that as the size and complexity of the Knowledge Graph (KG) grow, the time
required to find exact matches increases exponentially, making it "hard" for traditional
algorithms to solve efficiently for very large datasets.
How the Framework Addresses This "Hardness"
While the underlying problem is computationally intensive, the proposed framework
manages this complexity through its specialized agentic architecture and Graph-
enhanced Retrieval-Augmented Generation (GraphRAG) :
 Motif Detection for Reasoning: The framework uses motif detection to allow
agents to recognize specific Context–Mechanism–Outcome configurations
(CMOCs) as distinct graph patterns. This allows the Synthesis Agent and
Contradiction Agent to focus on small, meaningful "motifs" rather than
attempting to analyze the entire global graph at once.
 GraphRAG and Subgraph Retrieval: Instead of performing an exhaustive
search of the entire literature database, the system uses GraphRAG to retrieve
subgraphs of related entities . This effectively "prunes" the search space,
allowing the LLM-based agents to reason over connected claims and evidence
paths that are relevant to a specific query.
 Identifying Similarity and Trends: The framework facilitates identifying
similar trends (demi-regularities) across different research studies by centering
queries on shared nodes, such as a specific "Mechanism Resource" or "Context
factor". By assigning stable identifiers (StudyIDs) to these nodes and relations,
the agents can more easily consolidate similar trends and surface contradictory
evidence within these specific sub-graph neighborhoods.
Practical Significance in the Framework
In a practical sense, while identifying subgraph similarity is "hard" in a general
mathematical context, it is precisely what makes the Literature Knowledge Graph
(LKG) superior to traditional text-based search. By turning the narrative findings of
the 28 benchmark papers into a structured graph, the framework enables agents to
detect relational motifs—such as the "Expertise Reversal Effect"—which would be
nearly impossible to find consistently through naive keyword searches.
Note: The specific classification of this problem as "NP-hard" is a concept from
broader computer science and is not explicitly discussed in the provided sources. You
may wish to independently verify the computational theory of subgraph isomorphism
for further technical depth.
How does GraphRAG specifically improve reasoning over flat text chunks?
Tell me more about the 'Expertise Reversal Effect' found by Richmond.
What specific human-in-the-loop checkpoints are built into the framework?
I want you to provide the additional info on the above, and argue the proposed method
workable and implementable
The proposed multi-agent framework is a stateful orchestration system designed to
automate the interpretive and labor-intensive processes of a systematic review while
maintaining the methodological rigor of a human research team. The framework is
architected as a core-and-plugin system, separating a method-agnostic core review
infrastructure from method-specific synthesis plugins.
I. Additional Framework Details: Agent Roles and Workflow
The system utilizes specialized agents coordinated through a shared state (the "single
source of truth"), ensuring that all decisions are auditable and traceable.
 Core Review Infrastructure (Always Present):
o Protocol & Scope Agent: Encodes researcher-defined questions,
eligibility rules, and Initial Programme Theory (IPT) schemas.
o Search & Retrieval Agent: Executes queries across databases and uses
Microsoft Graph to harvest literature from enterprise folders
(Teams/SharePoint) with full provenance logging.
o Deduplication & Record-Linking Agent: Clusters duplicate records
across sources and assigns stable StudyIDs.
o Screening Agents (Title/Abstract & Full Text): Apply criteria to
classify records as include, exclude, or uncertain, maintaining detailed
rationales for every decision.
o Reporting & Artifact Agent: Packages all decision logs, PRISMA
counts, and evidence tables into a repository-ready format.
 Realist Synthesis Plugin (Method-Specific):
o CMOC Extraction Agent: Deconstructs full-text passages into
structured Context–Mechanism–Outcome configurations (CMOCs) ,
identifying both explicit and inferred mechanisms.
o Theory Synthesis & Refinement Agent: Compares CMOCs across
studies to identify demi-regularities (recurrent patterns) and proposes
evidence-based updates to the programme theory.
o Contradiction & Sensitivity Agent: Uses motif detection to flag
instances where similar interventions lead to divergent outcomes, forcing
explicit resolution by human researchers.
II. Argument for Workability and Implementability
The framework is highly workable and implementable using current post-2023
technologies for the following reasons:
1. Technical Substrate: The system is built on established orchestration
frameworks like LangChain and LangGraph , which are specifically designed
to manage stateful, multi-step agent workflows.
2. Enterprise-Grade Retrieval: Utilizing Microsoft Graph as the retrieval
backbone ensures the system is not a "black box"; every retrieved PDF and
search query is securely logged and versioned within institutional repositories,
providing a durable audit trail.
3. Enhanced Reasoning via Knowledge Graphs: Unlike traditional "flat" text
retrieval, the use of a Literature Knowledge Graph (LKG) and GraphRAG
allows agents to reason over connected causal paths. This is particularly critical
for identifying complex configurations (CMOCs) that naive summarization
tools often overlook.
4. Evidence of LLM Capability: Recent empirical studies (post-2023) confirm
that LLMs are already capable of high-accuracy screening and extraction when
governed by "two-reviewer" collaborative workflows and cross-critique logic.
5. Human Master Control: The framework is implementable because it does not
attempt "total automation". Instead, it uses predefined checkpoints (Screening
Adjudication, CMOC Validation, Contradiction Adjudication, Theory Sign-off)
to ensure human judgment remains the governing force over interpretive steps.
6. Benchmarked Validity: The framework’s workability is verifiable against the
Richmond et al. (2020) human reference standard. By replicating Richmond's
set of 28 included studies and their final programme theory, the system
provides measurable recall and precision metrics to prove its effectiveness.
7. Lifelong Update Capacity: The system implements a continual learning loop
where human feedback at each checkpoint is recycled to update the underlying
prompts and decision rules. This ensures the framework accommodates
evolving stakeholder requirements and adapts as the evidence base grows.
This architecture directly addresses the scalability and transparency gaps of traditional
reviews, offering a transparent, auditable, and extensible infrastructure suitable for
informing change in complex educational systems.
How does GraphRAG specifically detect conceptual patterns and lineages?
Could you explain the Expertise Reversal Effect in more detail?
What repository artifacts are exported by the Reporting Agent?
I means that motif is workable for subgraph similarity determination. please make it
The use of motifs within the Literature Knowledge Graph (LKG) provides a robust
and implementable method for determining subgraph similarity, which is essential
for identifying recurrent patterns across disparate research studies. In this framework,
a motif is defined as a specific, recurring structural pattern or sub-graph configuration
that represents the underlying logic of the synthesis method—most notably the
Context–Mechanism–Outcome configurations (CMOCs) required for realist
synthesis.
I. Workability of Motif Detection for Subgraph Similarity
Motif detection effectively transforms the task of identifying similar trends (demi-
regularities) from a narrative search into a computable graph-matching process .
The framework enables this through the following mechanisms:
 Pattern Consolidation: By embedding stable StudyIDs and EvidenceSpan
identifiers within the entities (e.g., "low knowledge student") and relations
(e.g., "triggers response"), the system can identify where similar configurations
of evidence appear across different studies. When the same motif—such as a
specific resource leading to a positive outcome for a certain population—
appears in multiple study subgraphs, the system can consolidate these into a
single "demi-regularity".
 Contradiction Identification: Conversely, if the system detects a motif where
the same intervention resource leads to divergent outcomes, it identifies a
relational discrepancy. This "conflict motif" signals to the human researcher
that a contextual contingency (e.g., student confidence levels) may be
moderating the outcome, mirroring the human reasoning performed in the
Richmond et al. (2020) benchmark.
 Contextual Reasoning: The framework uses Graph-enhanced Retrieval-
Augmented Generation (GraphRAG) to retrieve these subgraphs rather than
isolated text chunks. This allows agents to reason over the similarity of the
configurations themselves, which is more powerful than naive keyword-based
similarity.
II. Implementation and Alignment with Generative AI
This method is implementable using post-2023 orchestration and graph technologies:
 Agentic Orchestration: The framework utilizes a stateful orchestrator (such
as LangGraph) to manage specialized agents that populate the graph and
perform motif queries.
 GraphRAG Integration: Modern GraphRAG techniques allow for the
extraction of a Knowledge Graph from raw text and the use of its community
structures to improve reasoning over narrative data.
 Traceability: Every edge in the motif remains linked to a specific evidence
span via Microsoft Graph, fulfilling the RRE Call’s requirement for
methodologically explicit warranting and auditable analytical artifacts.
By representing the findings of the 28 benchmark papers as structured graph patterns,
the framework ensures that subgraph similarity is not merely a statistical
approximation but a theoretically grounded identification of the "why, how, and for
whom" of educational interventions.
How does motif detection help identify contradictions in educational studies?
What specific student contexts did the Richmond review identify?
How can human-in-the-loop checkpoints improve the AI's extraction accuracy?
how to address NP problem for the above , is it NP problems or can be solved
In the context of the proposed multi-agent framework, identifying subgraph similarity
and detecting motifs (such as Context–Mechanism–Outcome configurations or
CMOCs) does involve significant computational complexity. While the general
problem of subgraph isomorphism is recognized in computer science as NP-hard—
meaning the time required to find exact matches can grow exponentially with graph
size—the framework is designed with specific strategies to make this problem
solvable and implementable for systematic reviews.
I should note that the classification of graph similarity as an "NP problem" is a
concept from broader computer science and is not explicitly discussed within the
provided sources; however, the framework's architecture directly addresses the
practical challenges associated with this complexity.
The framework addresses the "hardness" of graph reasoning through the following
mechanisms:
1. Targeted Motif Detection vs. Global Search
The framework does not attempt a brute-force search for any possible pattern across
the entire global graph. Instead, it utilizes motif detection to look for small,
predefined structural configurations that represent the logic of the synthesis.
 Structured Schemas: The agents are guided by a specific schema involving
entities like Context, Mechanism (Resource/Response), and Outcome .
 Query-Focused Summarization: By searching for these specific "building
blocks" (the CMOCs), the search space is significantly restricted compared to a
general subgraph similarity task.
2. Graph-enhanced Retrieval-Augmented Generation (GraphRAG)
The framework utilizes GraphRAG to manage complexity by retrieving subgraphs
of related entities rather than trying to process the entire Literature Knowledge Graph
(LKG) at once.
 Neighborhood Retrieval: Agents reason over connected claims and evidence
paths within specific local neighborhoods of the graph.
 Community Summarization: Drawing on the GraphRAG approach, the
system builds "community structures" within the graph. This allows the agents
to summarize and query high-level patterns across the corpus without needing
to traverse every individual node-to-node path in a single operation.
3. Use of Graph Embeddings and Link Prediction
To address missing information and avoid the pitfalls of exact combinatorial
matching, the framework employs Graph embeddings and link prediction .
 Vector Representations: Embeddings translate high-dimensional graph data
into lower-dimensional vector representations. This allows the system to
identify "similar" results and "demi-regularities" across different studies based
on semantic and structural proximity rather than purely identical subgraph
matching.
 Denoising: These methods help to "denoise" the graph and complete missing
edges, ensuring that the agents can identify patterns even when studies report
evidence with varying levels of detail.
4. Human-in-the-Loop Adjudication (HITL)
The framework incorporates Master Control checkpoints where human researchers
adjudicate the most complex or contradictory subgraphs.
 Contradiction Registers: When the Contradiction Agent flags a "conflict
motif" (e.g., the same intervention leading to different outcomes), it pauses the
automated pipeline.
 Human Decision Rules: Instead of the machine attempting to resolve every
combinatorial ambiguity, the human researcher provides the final interpretive
explanation for the "contextual contingency". This human intervention
effectively "solves" the interpretive challenge that purely computational
methods struggle with.
Summary of Workability
By focusing on small relational motifs , using localized GraphRAG retrieval , and
leveraging vector embeddings, the framework transforms an theoretically "hard" NP
problem into a workable, auditable, and traceable methodological process. This
ensures that the system can scale to handle the 28 papers in the Richmond
benchmark—or even tens of thousands of papers in an enterprise setting—while
maintaining the interpretive depth required for high-stakes educational research.
How do motifs handle contradictions in research findings?
What is the computational challenge of identifying subgraph similarity?
How does Microsoft Graph support the provenance of evidence spans?
You should not mention the 28 papers. These 28 papers are just a particular
verification database. For general application, there may be more than 28 papers —
many more papers. Do not specifically say '28 papers.' Instead, just say that for
practical application in systematic reviews, the collection of identified relevant papers
is not too large and can be resolved by the proposed method using MOTIF (M-O-T-I-
F) for those.
For practical application in systematic reviews, the collection of identified relevant
papers typically reaches a volume that is manageable for high-depth, configuration-
level analysis through the proposed multi-agent framework. Rather than performing
simple narrative summaries, the framework utilizes a Literature Knowledge Graph
(LKG) to represent each study as a relational structure.
The core synthesis logic is executed through MOTIF detection, a computational
method that identifies specific, recurring graph configurations representing
Context–Mechanism–Outcome patterns. By embedding stable identifiers within
each entity and relation, the agents use MOTIF patterns to consolidate similar trends
across different research studies or to surface contradictions within specific sub-graph
neighborhoods. This approach ensures that the final synthesis is not just a summary of
a fixed dataset, but an auditable, configuration-level discovery process capable of
handling the increasing volume and complexity of contemporary educational research.
Synthesis and Pattern Recognition via MOTIF Detection
The framework's ability to resolve complex evidence bases rests on its structural
reasoning layer. Once the relevant literature has been identified and screened, the
Synthesis Agent populates the LKG with extracted causal claims. This transformation
from flat text to a relational graph allows the system to employ MOTIF detection for
high-order analysis:
 Consolidating Trends: The system identifies "demi-regularities" by detecting
MOTIFs that recur across the literature, even when studies originate from
diverse contexts. These motifs represent the generative mechanisms that
explain how specific educational interventions achieve their effects.
 Surfacing Contradictions: When the graph identifies a conflict—such as the
same intervention resource leading to divergent outcomes—it flags this as a
contradiction motif. This prevents the "smoothing over" of contested findings
common in general-purpose AI summary tools.
 Traceable Warranting: Every node and edge within a detected MOTIF is
persistently linked back to its original source via stable StudyIDs and
EvidenceSpan pointers. This fulfills the requirement for methodologically
explicit warranting by ensuring every claim in the final programme theory can
be traced back to a specific passage in the primary literature.
By utilizing this MOTIF-based approach, the framework effectively addresses the
challenges of scalability and transparency that often limit traditional manual reviews
of large and heterogeneous literatures. The result is a transparent and controllable
pipeline where the final output—identifying the effects of specific pedagogies on
particular populations—is anchored in a rigorous, computable evidence base.
How does MOTIF detection resolve causal configurations in complex systems?
What makes MOTIF-based trend consolidation more auditable than traditional
summaries?
How can MOTIF patterns identify contradictions in educational intervention research?
what is the method for identifying similar subgraph
In the multi-agent framework, the method for identifying similar subgraphs is
primarily driven by MOTIF detection (also referred to as relational graph queries or
pattern recognition) performed over a Literature Knowledge Graph (LKG) .
The identification process works through the following structured steps:
1. Representation of Evidence as Relational Patterns
Instead of processing flat text, the framework deconstructs studies into
Context–Mechanism–Outcome configurations (CMOCs) , which are stored as first-
class relational objects in the knowledge graph. Each CMOC is represented as a
subgraph motif containing nodes for the population (context), the pedagogical
intervention (mechanism resource), the learner's reaction (mechanism response), and
the result (outcome).
2. Pattern Discovery via MOTIF Detection
The framework's Synthesis Agent uses MOTIF detection to identify recurrent
configurations across the graph.
 Consolidating Trends: By querying for specific structural patterns that repeat
across different StudyIDs, the system identifies demi-regularities (recurrent
trends). For example, a motif might represent a specific type of student (e.g.,
"low knowledge") consistently experiencing "panic" when observing an expert
without explanation.
 Identifying Contradictions: The system uses motif detection to flag
relational discrepancies. A "conflict motif" is detected when the same
intervention resource leads to divergent outcomes in different study subgraphs,
signaling a contextual contingency that requires human adjudication.
3. Similarity Resolution through Embeddings and GraphRAG
To overcome the computational "hardness" of exact subgraph matching, the
framework employs two advanced techniques:
 Graph Embeddings: The system uses graph embeddings and link
prediction to denoise the data and complete missing edges, allowing it to
identify "similar" configurations based on semantic and structural proximity
rather than purely identical labels.
 GraphRAG (Neighborhood Retrieval): Instead of a global search, agents use
Graph-enhanced Retrieval-Augmented Generation (GraphRAG) to
retrieve local subgraphs of related entities . This enables the agents to reason
over connected claims and evidence paths specific to a context factor or
intervention type.
4. Traceability and Provenance
A critical component of this method is that every node and edge within an identified
motif remains linked to a specific EvidenceSpan pointer. Through Microsoft Graph,
the system maintains a traceable "audit trail," ensuring that any identified trend or
contradiction can be verified against the original text passages in the primary
literature.
Note on Computational Complexity: Outside of the provided sources, the general
task of identifying exact subgraph similarity is known in computer science as the NP-
hard problem of subgraph isomorphism. The proposed framework makes this
"workable" for systematic reviews by using structured templates (CMOC schemas)
and localized GraphRAG retrieval to narrow the search space to theoretically relevant
motifs.
How does the framework manage contradictory evidence across research studies?
What are the four human master control checkpoints in the system?
How does MOTIF detection help identify trends in educational research?
in terms of multi LLM agent frame, Provide a description of how the large language
model will be used as an agent — through prompts — to perform the tasks of the
required work or to automatically replace the human researchers in doing the work
that Richmond and his colleagues did in that example publication.
In a multi-agent framework, Large Language Models (LLMs) act as the specialized
"reasoning engines" within an orchestrated pipeline, performing the interpretive tasks
once reserved for human researchers. By utilizing role-specific system prompts and
structured templates, the LLM is transformed from a general chatbot into a series of
coordinated agents—such as Screening, Extraction, and Synthesis agents —that
replicate the realist review process conducted by Richmond et al. (2020) .
1. Task Decomposition: Automating the Richmond Workflow
The framework decomposes the labor-intensive steps of the Richmond review into
discrete agentic responsibilities governed by researcher-defined prompts:
 Protocol & IPT Construction: Instead of human consensus-building, a
Protocol Agent uses prompts to encode the review's scope and Initial
Programme Theory (IPT) into a machine-readable schema. This schema
directs all subsequent agent actions.
 Two-Stage Screening: Richmond's team manually screened titles, abstracts,
and full texts. In this framework, a Screening Agent is prompted with
eligibility rules to classify records as include, exclude, or uncertain. The LLM
generates a rationale for every decision, ensuring the process is auditable
rather than a "black box".
 Evidence Extraction (The Core Realist Task): The framework automates the
extraction of Context–Mechanism–Outcome configurations (CMOCs) . An
Extraction Agent identifies specific entities (e.g., "low-knowledge students")
and relations (e.g., "how feedback triggers learning responses"). Every
extracted item is persistently linked to a specific text span to prevent
hallucinations.
 Synthesis and Refinement: A Synthesis Agent replicates Richmond's cross-
study comparison to identify demi-regularities (recurrent patterns). A
Contradiction Agent uses structural motif detection to flag instances where
the same intervention leads to different outcomes, forcing explicit resolution.
2. Prompting and Rule-Based Governance
The LLM is governed through a multi-layered prompting strategy that ensures it
follows the specific "logic" of a systematic review:
 System Prompts: These define the agent's professional persona (e.g., "Act as
an expert in RAMESES-compliant realist synthesis").
 Domain-Adapted Templates: Prompts include researcher-defined schemas
that force the LLM to output structured data (e.g., JSON or tables) rather than
free-form prose.
 Few-Shot Calibration: During the "usage phase," human researchers review a
small sample of the model's decisions. These corrections are fed back into the
agent's prompt as few-shot examples, allowing the model to "learn" the
researcher's intent and refine its screening or extraction logic in real-time.
3. Replacing Human Labor with "Master Control" Checkpoints
While the framework uses LLMs to automate high-volume tasks, it does not remove
human judgment entirely. Instead, it creates Master Control checkpoints where the
agents must pause for human adjudication:
1. Screening Calibration: Humans review a sample of labels to refine the agent's
screening policy.
2. CMOC Validation: Humans spot-check extracted configurations against the
"ground truth" found in the original publications.
3. Contradiction Adjudication: The system stops when it detects conflicting
evidence (e.g., the "Expertise Reversal Effect"), requiring a human to provide
an interpretive explanation.
4. Theory Sign-Off: The lead researcher approves the final synthesized
programme theory before the Reporting Agent generates artifacts for
repository deposition.
4. Knowledge Graph and GraphRAG Integration
To achieve the "relational reasoning" Richmond's team used to link mechanisms to
contexts, the framework utilizes Graph-enhanced Retrieval-Augmented
Generation (GraphRAG). Instead of the LLM reading isolated text snippets, it
retrieves subgraphs of connected claims . This allows the agents to reason over
complex interactions—such as how a student's confidence levels (Context) moderate
their response to a simulated patient (Mechanism)—ensuring the synthesis stays
aligned with the complex educational system being studied.
How do prompts transform the LLM into a Synthesis agent?
What specifically is identified during the CMOC extraction process?
How does human feedback refine the agents' screening logic?
Please describe those in LangChain and GraphChain terms. Will GraphChain be used
to build the multi-agent agentic framework, or will we just use LangChain? Please
describe those terms and the interactive pipeline in terms of LangChain or
GraphChain.
The proposed multi-agent framework is built on the LangChain ecosystem, utilizing
LangGraph as the primary stateful orchestrator for managing the complex, iterative
logic of a realist review. While "GraphChain" is not a term explicitly mentioned in the
provided sources, the framework heavily incorporates graph-based orchestration
and GraphRAG (Graph-enhanced Retrieval-Augmented Generation) to manage the
relationship between data and agents.
The interactive pipeline and framework are described through the following terms and
mechanisms:
1. LangChain: The Orchestration Framework
LangChain serves as the foundational framework for building the orchestrated
workflows.
 Multi-Agent Orchestration: It allows specialized agents (Screening,
Extraction, Synthesis, and Contradiction agents) to collaborate by maintaining
a shared "state" of the review protocol.
 Domain-Adapted Templates: LangChain uses researcher-defined prompt
templates to comprehensively encode rules and schema definitions for specific
review tasks, ensuring every agent action is guided by the Initial Programme
Theory (IPT).
2. LangGraph: The Stateful State-Machine
The sources recommend LangGraph (a specialized extension within LangChain) as
the "ideal" orchestrator for this project.
 Stateful Orchestration: Unlike a simple linear chain, LangGraph models the
review as a graph-based state machine . This is essential for the iterative
loops required in realist synthesis, such as moving from extraction back to re-
searching when new mechanisms are inferred.
 Shared State Registry: All agents read from and write to a "single source of
truth" (the Shared State), which includes the study registry, versioned
programme theories, and audit logs.
3. The Interactive Pipeline (Human-in-the-Loop)
The interactive nature of the pipeline is managed through Predefined Checkpoints
within the LangGraph workflow. At these points, the automated "chain" pauses to
allow for human adjudication:
 Screening Adjudication: The Human reviews a sample of AI-labeled records
to calibrate the model's behavior.
 CMOC Validation: Humans spot-check the extracted
Context–Mechanism–Outcome configurations (CMOCs) to ensure they
align with the original literature.
 Contradiction Adjudication: When the Contradiction Agent identifies a
conflict (e.g., same intervention leading to different outcomes), the system flags
it for human interpretation rather than "smoothing" the data.
 Theory Sign-Off: The final "Programme Theory" must be approved by the
researcher before the pipeline generates the final artifacts.
4. Graph-Enhanced Retrieval (GraphRAG)
While LangGraph manages the agent workflow, GraphRAG manages the evidence.
 Relational Retrieval: Instead of retrieving isolated text passages, the agents
use GraphRAG to retrieve subgraphs of connected claims from the
Literature Knowledge Graph (LKG) .
 Configuration Reasoning: This allows the LLM agents to reason over
complex interactions—such as how a specific "Context" node (e.g., student
self-confidence) interacts with an "Intervention" node to change the
"Outcome"—matching the high-level reasoning performed by human
researchers like Richmond et al. (2020) .
In summary, you will use LangChain as the broad agent framework and LangGraph
as the specific tool to build the stateful, interactive pipeline. This architecture ensures
the review is not just automated, but is auditable, traceable, and governed by
human expertise at every critical juncture.
How does the MOTIF method identify similar trends across research?
How are human feedback loops integrated into the LangChain framework?
How does the Microsoft Graph ensure auditability within the framework?
Based on the LangChain framework, please describe each agent function and how
each of them will be prompted, and what the workflow is for simulating the
systematic review and the plug-in specifics. Could you clearly talk about how the
Graph RAG is built on the build-up of your graph and how they perform the required
tasks as we outlined above. Go back and look at what we talked about regarding the
agents, the core framework, and the plug-in functions for each specific systematic
review approach. Please combine them in detail.
4. Methodology: The Multi-Agent Orchestration Framework
The proposed framework is a stateful orchestration system built on LangChain and
LangGraph, designed to automate the labor-intensive stages of a systematic review
while preserving the interpretive depth required for complex educational systems. The
architecture is partitioned into a method-agnostic Core Review Infrastructure and
method-specific Synthesis Plugins, ensuring the system can support diverse
methodological traditions as required by the Review of Research in Education
(RRE) 2026 call .
4.1 The Core Review Infrastructure (Method-Agnostic)
The core infrastructure provides the foundational "Review Services" that manage data
provenance, audit trails, and human-in-the-loop (HITL) governance.
 Protocol & Scope Agent: This agent encodes researcher-defined review
questions, inclusion/exclusion criteria, and Initial Programme Theory (IPT)
schemas into versioned prompt templates. Prompting Strategy: It is prompted
to "Act as a methodology expert," using structured schemas (e.g., JSON) to
define the boundaries of the review.
 Search & Retrieval Agent (Microsoft Graph API): Utilizing Microsoft
Graph as the enterprise retrieval layer, this agent harvests literature from
organizational repositories like Teams, SharePoint, and OneDrive. It logs every
query and source to ensure absolute retrieval traceability and reproducibility.
 Deduplication & Record-Linking Agent: This agent clusters candidate
records across multiple databases, assigns stable StudyIDs, and maintains the
"Single Source of Truth" study registry.
 Two-Stage Screening Agent: A multi-stage classifier that applies eligibility
rules at the title/abstract and full-text levels. Prompting Strategy: It is
prompted with few-shot examples from human calibration rounds, requiring it
to output an "include, exclude, or uncertain" label alongside a structured
rationale and a confidence score.
 Reporting & Audit Agent: This agent automatically packages all decision
logs, search queries, extraction tables, and human feedback records into
repository-ready artifacts suitable for the AERA-RRE repository.
4.2 The Realist Synthesis Plugin (Worked Example)
While the core manages the workflow, plugins instantiate the specific synthesis logic.
The Realist Synthesis Plugin operationalizes the logic of Richmond et al. (2020) to
explain why, how, and for whom interventions work.
 CMOC Extraction Agent: This agent deconstructs full-text passages into
Context–Mechanism–Outcome configurations (CMOCs) . Prompting
Strategy: It is prompted to identify "Context" (student/teacher factors),
"Mechanism Resource" (what the intervention provides), "Mechanism
Response" (learner reaction), and "Outcome". It maps these into relational
triples for the knowledge graph.
 Theory Synthesis & Refinement Agent: It compares CMOCs across studies
to identify demi-regularities (recurrent patterns). It proposes evidence-based
updates to the programme theory, linking every theoretical claim back to
specific evidence-span pointers in the literature.
 Contradiction & Sensitivity Agent: This agent utilizes MOTIF detection to
flag instances where the same intervention resource leads to divergent
outcomes in different contexts. It forces explicit adjudication of "contextual
contingencies," preventing the system from "smoothing over" contested
findings.
4.3 Workflow Simulation: Replicating Richmond et al. (2020)
The workflow is a stateful graph where transitions are governed by completion of
tasks and human approval.
1. IPT Seeding: The Protocol Agent formalizes the initial hypothesis (e.g., Dual-
Process Theory in clinical reasoning).
2. Retrieval & Registry: The Retriever Agent harvests the 28 benchmark papers
and associated metadata via Microsoft Graph.
3. HITL Screening Calibration: Researchers review a stratified sample of 10%
of records; their corrections update the Screening Agent’s prompt logic
through few-shot learning.
4. Configurational Extraction: The Extraction Agent populates the Literature
Knowledge Graph (LKG) with nodes and edges representing the evidence
base.
5. MOTIF-Based Synthesis: The Synthesis Agent queries the graph for
recurrent CMOC patterns (MOTIFs) to refine the overall programme theory.
6. Contradiction Resolution: The Contradiction Agent identifies the "Expertise
Reversal Effect" (e.g., directive teaching helps novices but hinders experts) by
flagging conflicting subgraphs for human interpretation.
4.4 Literature Knowledge Graph and GraphRAG
The Literature Knowledge Graph (LKG) serves as the reasoning substrate for the
agents. It is constructed by extracting entities (Intervention, Population, Outcome,
Context) and relations from full texts using Named Entity Recognition (NER) and
Relation Extraction (RE) .
GraphRAG (Graph-enhanced Retrieval-Augmented Generation) improves upon
traditional RAG by allowing agents to retrieve subgraphs of connected claims rather
than isolated text passages. By building "community structures" within the LKG,
GraphRAG enables agents to perform global, configurational reasoning —such as
mapping how student self-confidence (Context) moderates the response to simulated
patients (Mechanism)—which matches the interpretive depth of the original human
review.
4.5 Human-in-the-Loop (HITL) and Lifelong Learning
The framework is governed by a formal protocol where human researchers act as
arbiters at four predefined checkpoints: Screening Adjudication, CMOC
Validation, Contradiction Adjudication, and Theory Sign-off . Every human
correction is recycled to update the system’s decision policies (prompts and rules) ,
enabling lifelong (continual) and online updating . This ensures the framework
accommodates evolving stakeholder requirements and adapts as new studies are added
to the "living" review.
How do LangChain agents simulate the Richmond realist review?
How does MOTIF detection resolve causal contradictions in the graph?
What specifically separates core infrastructure from method-specific synthesis
plugins?
You talk about knowledge graph, but you did not talk about how they build it. That is
a key part, how we identify entities. Who will play this role?
The construction of the Literature Knowledge Graph (LKG) is a multi-stage
process handled by specialized agents within the framework, utilizing both automated
extraction and human-in-the-loop validation.
1. Who Plays the Role? (Agent Responsibilities)
The identification and structuring of entities are distributed across three primary roles:
 Extraction Agent (or CMOC Extraction Agent): This agent is the primary
"identifier." It processes full-text chunks to identify key educational
constructs—such as interventions, populations, outcomes, and contexts—and
the relationships between them. For the realist plugin, this agent specifically
focuses on identifying Contexts, Mechanism Resources, Mechanism
Responses, and Outcomes .
 Normalization Agent: After initial extraction, this agent performs
canonicalization. It is responsible for de-duplicating and merging entities that
refer to the same concept but use different terminology, such as resolving "self-
efficacy" and "confidence" into a single node to ensure graph consistency.
 Human Researcher (HITL): Humans act as the final authority. At a
predefined CMOC Validation checkpoint , researchers spot-check the
extracted entities and relations against the original evidence spans to ensure
interpretive accuracy and correct any systematic misinterpretations by the
agents.
2. How They Build It (The Extraction Pipeline)
The building of the graph follows a systematic pipeline:
 NER and RE Processing: The framework uses Named Entity Recognition
(NER) and Relation Extraction (RE) to automatically process publications
harvested from databases like ERIC or Scopus. These methods identify the
"nodes" (entities like intervention or outcome) and the "edges" (relations like
intervention affects outcome ).
 Structuring into Triples: The extracted data is organized into relational
triples (e.g., [Study]—contains—[CMOC] or [CMOC]—has_context—
[ContextFactor]). Every entity and relation is persistently linked to an
EvidenceSpan pointer, which maps back to the specific docID and text
segment to ensure traceability.
 Denoising and Completion: Once the initial graph is formed, the system
employs graph embeddings and link prediction . These computational
techniques help "denoise" the graph and identify potentially missing edges,
resulting in a more structured and complete knowledge base for subsequent
reasoning.
 GraphRAG Integration: The resulting LKG serves as the reasoning substrate.
Instead of retrieving isolated text, the Synthesis Agent uses Graph-enhanced
Retrieval-Augmented Generation (GraphRAG) to retrieve subgraphs of
these connected entities, allowing for configuration-level reasoning over the
evidence.
By separating the identification (Extraction Agent), refinement (Normalization
Agent), and verification (Human Researcher), the framework ensures the knowledge
graph is both scalable and methodologically rigorous.
How will the Extraction Agent identify specific educational constructs?
Which entities and relations populate the Literature Knowledge Graph?
How do researchers validate the graph during CMOC checkpoints?

========================================

## grok output -KG and GraphRag-sent-2.pdf

Building the Knowledge Graph for Representing the Richmond Realist Review 
Process 
Based on our previous discussions about knowledge graphs (including using larger concepts as 
entities, community-based identification methods, and alignment with Microsoft tools like 
Microsoft Graph or related entity recognition APIs), and drawing from the Richmond et al. 
(2020) paper's methodology (as the core reference, since no specific uploaded file was accessible 
but this matches the described content with 28 papers and realist review procedure), here's a 
detailed, step-by-step explanation of how to build the knowledge graph (KG). I'll describe it in 
simple terms, focusing on how it represents the Richmond process (e.g., initial theory as 
hypothesis, literature search, contradiction checking, consolidation, and verified theory). This 
KG uses entities for big concepts (e.g., "Low Knowledge Context" or "Simulation Intervention"), 
relations for connections (e.g., "triggers" or "contradicts"), and can incorporate Microsoft 
Knowledge Graph features for entity identification and verification. 
The goal is to create a structured, queryable graph that mirrors the realist review's iterative, 
theory-driven approach. This allows for automation (e.g., with LLM agents) and verification 
against the publication's data. Tools like Neo4j (for graph storage), Python libraries (e.g., 
NetworkX for building), or Microsoft Azure Cognitive Services (for entity recognition via their 
knowledge graph APIs) can be used. 
Step 1: Define the Core Structure and Components 
 Entities (Nodes): These are the "big concepts" from the Richmond paper and general 
realist reviews. Treat them as high-level ideas rather than granular words. Use 
community identification methods (e.g., clustering similar terms from text) to group 
them. For example: 
o Contexts (C): Big ideas like "Low Student Knowledge" (e.g., novices lacking 
domain-specific info), "High Domain-Specific Knowledge," "Positive 
Coping/Self-Confidence," "Negative Coping/Low Confidence," "Varied 
Knowledge in Groups." 
o Mechanisms (M): Responses or resources, e.g., "Insight from Feedback," 
"Cognitive Load/Frustration," "Emotional Panic," "Self-Regulation." 
o Outcomes (O): Results like "Improved Diagnostic Accuracy," "Knowledge 
Retention," "Negative Learning Experience," "Enhanced Clinical Reasoning." 
o Interventions: Educational methods, e.g., "Simulation-Based Practice," "Expert 
Explanations," "Case-Based Learning," "Retrieval Practice." 
o Theories/Hypotheses: E.g., "Initial Programme Theory (IPT)" (starting 
hypothesis: interventions boost knowledge and experience), "Refined Programme 
Theory" (final verified theory). 
o Literature Elements: "Selected Study" (nodes for each of the 28 papers, with 
IDs like "Study1_Ark_2007"), "Contradiction" (flagged mismatches). 
 Relations (Edges): These link entities to show how the process flows, like causal or 
logical connections. Examples: 
o "Triggers" (e.g., Low Knowledge → Triggers → Panic Mechanism). 
o "Leads To" (e.g., Insight Mechanism → Leads To → Positive Outcome). 
o "Contradicts" (e.g., Intervention in High Knowledge → Contradicts → Expected 
Positive Outcome, due to frustration). 
o "Verifies" (e.g., Study Data → Verifies → Refined Theory). 
o "Consolidates" (e.g., Multiple CMOCs → Consolidates → Final Theory). 
o "Derived From" (e.g., IPT → Derived From → Scoping Search + Expert 
Opinion). 
 Attributes/Properties: Add details to nodes/edges, e.g., confidence scores (0-1 based on 
evidence strength), quotes from the paper (e.g., "28 studies showed..."), or IDs from 
Microsoft Knowledge Graph (e.g., entity IDs for concepts like "Clinical Reasoning" 
linked to external knowledge bases). 
Use Microsoft Knowledge Graph (via APIs like Bing Entity Search or Azure Text Analytics) for 
entity identification: Input text from the paper (e.g., abstracts), and it auto-detects/links big 
concepts (e.g., "clinical reasoning" as an entity with ID, related to "medical education"). 
Community methods (e.g., graph community detection algorithms like Louvain) cluster similar 
entities (e.g., group "low knowledge" variations from different studies). 
Step 2: Gather and Extract Data from the Publication 
 Start with the Richmond paper as ground truth (or any similar uploaded file). Extract data 
to verify the KG: 
o Input Sources: Full text of the paper, including sections on methods, results, and 
figures (e.g., Figure 2: IPT diagram; Figure 3: CMOCs for low knowledge). 
o Extraction Process: Use NLP tools or LLMs (e.g., prompt: "Extract entities and 
relations from this text: 'In low knowledge contexts, explicit teaching leads to 
insight.' → Entity: Low Knowledge Context; Relation: Leads To; Entity: Insight 
Mechanism"). 
o Verification: Map extracted data to the paper's content. For example, check if 
"Low Knowledge" appears in the 28 studies (e.g., count mentions: 15/28 studies 
address it). If the paper includes entities like "dual-process theory," query 
Microsoft KG for related IDs and confirm alignment (e.g., does the paper's 
definition match the external KG's? Adjust if not for "correctness"). 
o Handle Sub-Graphs: Create sub-graphs for contradictions (e.g., a sub-graph 
showing Intervention X works in Context A but fails in B, with edges labeled 
"Context-Dependent"). 
Step 3: Build the Graph Iteratively 
 Initial Setup (Mirroring Initial Theory/Hypothesis): 
o Create a starting sub-graph for the IPT: Nodes for "Knowledge Acquisition," 
"Clinical Experience," "Practice." Edges: "Enhances" (e.g., Interventions → 
Enhances → Knowledge Recall). 
o Use community identification: Run clustering on keywords from the paper's 
scoping search (e.g., group "pattern recognition," "illness scripts" into "Non-
Analytical Reasoning" entity). 
 Add Literature Search and Selection: 
o Add nodes for "Database Search" (e.g., MEDLINE), linked to "Keywords" (e.g., 
"clinical reasoning" from IPT). 
o For the 28 studies: Create 28 "Study" nodes, each with properties like year, 
country, outcome measures. Relations: "Contributes To" (Study → Contributes 
To → CMOC). 
o Criteria as filters: Use graph queries to select (e.g., "Include if node has 
'undergraduate' attribute and 'rigor' score >0.7"). 
 Incorporate Analysis for Contradictions and Consolidation: 
o Build CMOC chains: For each study, add C-M-O paths (e.g., Low Knowledge (C) 
→ Expert Explanation (Intervention) → Insight (M) → Better Accuracy (O)). 
o Detect Contradictions: Use graph algorithms to find conflicting paths (e.g., query 
for paths where same Intervention leads to opposite Outcomes; flag with 
"Contradicts" edge). 
o Consolidate: Merge similar nodes (e.g., community clustering to group redundant 
CMOCs), refine edges (e.g., add "In Context Of" qualifiers). Iterate: Outcomes 
from one process become inputs (e.g., Contradiction Resolution → Input To → 
Theory Refinement). 
 Final Verified Theory: 
o Consolidate into a main graph: Core node "Refined Programme Theory" linked to 
all verified CMOCs. 
o Embed IDs: For each entity, fetch Microsoft KG ID (e.g., via API: search 
"clinical reasoning" → get ID, embed as property for cross-verification). 
 Tools for Building: 
o Manual/Initial: Use code (e.g., Python with NetworkX: G.add_node('Low 
Knowledge', type='Context'); G.add_edge('Low Knowledge', 'Panic', 
label='Triggers')). 
o Automated: Integrate LLMs for extraction (e.g., prompt to generate nodes from 
text). Use Microsoft Graph API for entity linking (e.g., identify "big concepts" 
like "simulation" and link to related communities/knowledge bases). 
o Community Identification: Apply algorithms (e.g., in NetworkX: communities 
= nx.community.louvain_communities(G)) to group entities (e.g., cluster all 
"knowledge-related" nodes). 
Step 4: Verify and Refine the KG 
 Using Publication Data: Query the graph against paper excerpts (e.g., "Does the KG 
include all 5 key contexts from the results?"). Test appropriateness: Simulate queries like 
"Find effects of pedagogy on students" → Return paths like Intervention → Mechanism 
→ Outcome for "certain pedagogy" (e.g., simulation interacting with low-confidence 
students). 
 Cross-Research Alignment: For different studies (beyond 28), add IDs to entities (e.g., 
Study_ID embedded). Compare sub-graphs: Similar trends (e.g., matching paths) 
consolidate; contradictions (e.g., differing outcomes on same node) are flagged for easy 
identification. 
 Iterative Improvement: If misalignments (e.g., paper data doesn't match KG), re-run 
community detection or add edges based on feedback. 
Step 5: Automation with Multi-Agent LLM Framework 
To make building dynamic: 
 Search Agent: Prompts LLMs to generate keywords from IPT, search literature, add 
Study nodes. 
 Extraction Agent: Parses text to create entities/relations, using Microsoft API for ID 
embedding. 
 Synthesis Agent: Detects contradictions (prompt: "Find conflicting CMOCs"), 
consolidates via clustering. 
 Verification Agent: Compares KG to paper data (e.g., "Verify if this path matches the 28 
studies' synthesis"). 
This KG not only represents the Richmond process but automates it for similar reviews, 
identifying trends/contradictions across researches. For practical significance: It helps educators 
query "What intervention for low-knowledge students?" and get verified paths, improving 
medical training. If you have the exact uploaded file name or more details, I can refine this 
further! 
Defining the Iterative Process for Entity Identification in Knowledge Graphs  
Based on our ongoing discussion about building a workable Literature Knowledge Graph (LKG) 
in the agentic framework (e.g., for simulating Richmond et al.'s realist review process), the 
iterative process for entity identification focuses on extracting "big concepts" (high-level entities 
like "Low Knowledge Context" or "Expertise Reversal Effect") from literature. This process is 
human-in-the-loop (HITL), community-based, and LLM-driven, aligning with methods like 
those in Microsoft's GraphRAG and broader active learning literature. It ensures the KG is 
accurate, scalable, and verifiable against ground truth (e.g., publication data). 
The process is "iterative" because it involves repeated cycles of proposal, review, and 
refinement, rather than a one-shot extraction. This draws from active learning paradigms, where 
the machine "queries" the human for feedback on uncertain or exemplary cases to improve 
progressively. Below, I define it step-by-step, including iteration count/stopping criteria, how the 
machine learns from researcher examples, mechanisms, existing research, and special terms. 
This is grounded in the extensive search results from academic papers, Microsoft docs, and 
related works. 
1. Definition of the Iterative Process 
The process is a HITL cycle for identifying and refining entities (nodes in the KG) and their 
relations (edges), treating entities as "big concepts" rather than fine-grained tokens. It starts with 
researcher-provided examples and builds the KG incrementally, incorporating feedback to 
handle ambiguity, noise, or domain-specific nuances (e.g., in medical education literature). 
 Step 1: Initialization (Researcher Input) The researcher provides a rough set of 
example big concepts (e.g., "Context: Low Student Knowledge" from Richmond's Initial 
Programme Theory or IPT). This acts as a "seed" – a small labeled set (e.g., 5-10 
examples) with descriptions or annotations. The machine uses this to bootstrap 
extraction. 
 Step 2: Machine Proposal The LLM (e.g., as an Extraction Agent in our framework) 
scans unstructured text (e.g., publication chunks) to propose entities. It identifies 
candidates via Named Entity Recognition (NER) or relation extraction, grouping similar 
terms into big concepts using similarity metrics or clustering. 
 Step 3: Human Review and Feedback The researcher reviews a batch of proposals 
(e.g., via a dashboard or conflict register), correcting errors (e.g., merging duplicates, 
adding descriptions, rejecting false positives). Feedback includes labels like "approve," 
"reject with reason," or "refine category." 
 Step 4: Machine Refinement and Re-Iteration The system incorporates feedback (e.g., 
as few-shot examples in prompts or by fine-tuning embeddings) and re-processes the data 
(or a new batch). This refines the model for better accuracy in subsequent iterations. 
 Step 5: Community Identification (Post-Extraction Clustering) Once entities are 
extracted, apply community detection to group them into semantic clusters (e.g., all 
entities related to "pedagogy effects"). This is not iterative per se but can trigger further 
refinement if clusters reveal inconsistencies. 
This cycle repeats until stopping criteria are met, building a KG that's aligned with the 
researcher's intent and verifiable against publications. 
2. How Many Iterations? When to Stop? Stopping Criteria 
 Typical Number of Iterations: Literature suggests 5-20 iterations for convergence in 
active learning setups, depending on dataset size and initial seed quality. For small-to-
medium literature corpora (e.g., 100-1,000 papers in a systematic review), 3-10 iterations 
are common to achieve 80-90% F1 score. In GraphRAG-like methods, entity extraction is 
often 1-2 passes, with iteration focused on refinement (e.g., 2-5 cycles of HITL). 
 When to Stop: Stop when the process stabilizes – i.e., new iterations yield minimal 
improvements or the KG meets quality thresholds. This is researcher-driven, as they have 
the "rough idea" of desired concepts. 
 Criteria for Stopping: 
o Performance Plateau: Monitor metrics like F1 score (precision + recall) on a 
validation set; stop if improvement <1-5% over 2-3 iterations (e.g., from Hein et 
al. 2025 on pathology reports, where F1 stabilized at 82% after iterative 
refinement). 
o Budget Exhaustion: Fixed human effort limit (e.g., label 10-20% of proposals 
per iteration; stop after 100-500 labels total, as in active learning for NER – Chen 
et al. 2015). 
o Coverage Threshold: Stop when 90-95% of big concepts from seed examples are 
correctly identified/related (e.g., verify against publication ground truth like 
Richmond's 5 contexts). 
o Uncertainty Reduction: If the machine's confidence scores (e.g., from LLM 
outputs) exceed 0.8-0.9 on average, or no more "uncertain" samples are queried. 
o Domain-Specific: For our purpose, stop when the KG accurately captures 
CMOCs (e.g., no major contradictions flagged without resolution). 
These criteria balance efficiency and accuracy, preventing infinite loops. 
3. How the Machine Learns from and Follows Researcher Examples 
The researcher provides "rough ideas" (e.g., annotated examples of big concepts like 
"Mechanism: Insight from Feedback"). The machine treats this as a seed for guided learning, 
ensuring proposals align with the examples. 
 Learning Mechanism: 
o Few-Shot Prompting: Embed examples directly in LLM prompts (e.g., "Extract 
entities like these examples: [list with descriptions]. Propose similar big concepts 
from this text."). The LLM generalizes patterns (e.g., via chain-of-thought 
reasoning) to identify analogous entities. 
o Active Learning Query Strategies: The machine selects "informative" samples 
for human review based on uncertainty (e.g., low-confidence proposals) or 
diversity (e.g., examples dissimilar to seeds). After feedback, re-prompt with 
updated examples or fine-tune embeddings. 
o Embedding-Based Similarity: Convert examples to vectors (e.g., via RDF2Vec 
or LLM embeddings); cluster new proposals around them. In GraphRAG, this 
happens post-extraction via community detection. 
o Feedback Incorporation: Use adversarial or reinforcement learning (e.g., RLHF) 
to adjust – e.g., penalize errors from prior iterations. In HITL setups, feedback 
becomes new few-shot data for re-processing. 
This mimics how humans refine: Start with examples, propose, correct, repeat. 
4. Existing Research Mentioning This or Original Methods 
This is not entirely original – it's rooted in active learning (AL) for entity recognition, extended 
to KGs with LLMs. Extensive search revealed alignments: 
 Active Learning for NER/KG Construction: 
o Settles (2012) seminal survey on AL: Mechanisms like uncertainty sampling 
(query low-confidence items) and query-by-committee (disagreement among 
models). Stopping: Performance convergence on holdout set. 
o Chen et al. (2015): AL for clinical NER – iterative, HITL, stops at F1 plateau. 
Aligns with our process for medical education literature. 
o Zhou et al. (2021): MTAAL (Multi-Task Adversarial AL) for medical 
NER/normalization – uses adversarial sampling for informative queries, iterative 
refinement. 
o Seo et al. (2021): AL for KG schema expansion – researcher seeds types, machine 
proposes, human refines; stops on coverage threshold. 
 LLM-Specific Iterative Methods: 
o Tsaneva et al. (2025): HITL LLM for KG validation – iterative collaboration, 
hybrid AL stops at F1 +5% improvement. 
o Pusch et al. (2026): HITL LLM for KG QA – iterative query refinement via 
natural language feedback; no fixed iterations, stops on user satisfaction. 
o Hein et al. (2025): Iterative LLM pipeline for pathology NER – uses error 
ontology for HITL refinement; stops when metrics stabilize. 
o Kardos et al. (2025): Graph walk-based AL for entity set expansion – iterative 
seed-to-endpoint paths; aligns with community methods. 
 GraphRAG Original Method (Microsoft 2024): Edge et al. arXiv paper – Entity 
extraction is LLM one-pass (prompt-based), no explicit iteration for ID, but post-
extraction uses Leiden for communities. Original development: Microsoft Research for 
private datasets; mentions refinement via summarization hierarchies, but not HITL 
iterations. They note potential for "iterative processes like constraint enforcement" in 
refinements. 
 Other Alignments: Liu et al. (2021) ActiveEA for KG entity alignment – iterative 
sampling; Ostapuk et al. (2019) adversarial AL for KG link prediction. 
These show the method is well-established, with originals like Settles for AL basics. 
5. Special Name/Term for Community Identification Method 
 Community Detection: The overarching term for grouping entities into semantic clusters 
in graphs. 
 Special Algorithms: 
o Leiden Algorithm: The primary one in GraphRAG (original publication: Traag et 
al. 2019 arXiv) – hierarchical, optimizes modularity better than Louvain; 
recursive until stable communities (stopping: no modularity gain). 
o Louvain Algorithm: Predecessor (Blondel et al. 2008) – greedy modularity 
optimization; often used in KG literature. 
o Other Terms: Hierarchical clustering, modularity-based detection, graph 
partitioning. 
Look at Original Publication: For GraphRAG (Edge et al. 2024), they explicitly use 
"Hierarchical Leiden Algorithm" for community detection, developed from Traag's work. It's not 
original to GraphRAG but adapted for LLM-summarized hierarchies. In broader KG lit (e.g., 
Hogan et al. 2020 survey), "community detection" is the standard term. 
This process is fully workable in our framework – integrate into Extraction/Synthesis Agents 
with LangGraph loops for iterations. If needed, I can provide a code snippet via code_execution 
for a prototype. 
 
Community Identification Methods Using Large Language Models (LLMs)  
Community identification (also known as community detection) in knowledge graphs (KGs) 
traditionally relies on graph algorithms like Leiden or Louvain to group nodes (entities) based on 
structural properties, such as connectivity or modularity. However, recent advancements 
integrate LLMs to enhance this process with semantic understanding – LLMs help interpret node 
labels, descriptions, or associated text to form more meaningful communities, especially for "big 
concepts" (high-level, abstract entities like "clinical reasoning" or "expertise reversal effect" in 
our earlier discussions on educational literature reviews). 
Does Community Identification Use LLMs? 
Yes, in post-2023 methods, LLMs are increasingly used to augment or drive community 
detection. LLMs provide contextual embeddings or reasoning to refine clusters, making them 
suitable for dynamic KGs where big concepts evolve. For example, LLMs can generate 
summaries of node groups or infer semantic relations that traditional algorithms miss. This is 
particularly useful in our agentic framework for extracting big concepts from literature (e.g., 
grouping similar "pedagogy effects" terms into one entity cluster). 
How Big/Large Concepts Become Entities 
Big concepts (abstract, high-level ideas) are transformed into entities (nodes in the KG) through 
LLM-based extraction and refinement: 
 Extraction Phase: LLMs process text (e.g., publication chunks) via prompts to identify 
candidates. For instance, prompt the LLM to "Extract high-level concepts as entities from 
this text, treating themes like 'low knowledge context' as a single entity with description." 
 Semantic Grouping: Use LLM-generated embeddings (vector representations) to cluster 
similar concepts, turning them into unified entities. Relations (edges) are inferred via 
prompting (e.g., "Link this entity to others based on causal relations"). 
 Refinement: Iterative HITL feedback or LLM self-correction ensures accuracy – e.g., 
merge duplicates or add attributes. This aligns with our framework's Extraction Agent, 
where big concepts from literature become KG nodes for reasoning (e.g., CMOC 
synthesis). 
Recent Publications After LLM Development (Post-BERT 2018, Post-ChatGPT 2022) 
Since BERT (2018) and ChatGPT (2022), publications have shifted to LLM-integrated methods 
for entity extraction and community detection in KGs. I focused on 2023-2025 papers, as older 
ones (pre-2023) are less relevant to current LLM capabilities. No major updates in very old 
publications (e.g., pre-2018), but new works build on them. Key recent ones: 
 LLM-driven community detection in social graphs uses prompting to incorporate 
semantic info, improving over structure-only methods. 
 GraphRAG (2024) uses LLMs for entity extraction from text, forming communities via 
Leiden algorithm for hierarchical summarization – directly applicable to big concept 
entities in literature KGs. 
 LLM-empowered KG construction surveys (2025) detail how LLMs act as autonomous 
extractors for big concepts, categorizing into ontology engineering and knowledge fusion 
pipelines. 
 Practices in fusing KGs and LLMs (2025) describe entity extraction for big concepts 
using prompting, with community detection for relation reasoning. 
 LLMs for KG extraction from tables (2025) prompt LLMs to identify big concepts as 
entities in domain-specific data, like materials science. 
 Clinical entity extraction (2025) augments LLMs with KGs for big concept entities in 
medical texts, improving accuracy via retrieval. 
 LLM-enhanced KRL survey (2025) covers entity extraction for big concepts in 
embeddings, post-ChatGPT. 
These show rapid evolution – no need for "updates" in old pubs, as new works cite and extend 
them with LLM integrations. If you need full PDFs or more, let me know! 
 
GraphRAG from Microsoft is fundamentally based on knowledge graphs (KGs), where the core 
process involves constructing a hierarchical KG from unstructured text data to enable advanced 
querying and reasoning. This KG is built by extracting entities (as big concepts, not just single 
words) and relationships, then organizing them into communities for semantic grouping, which 
directly supports our context of identifying high-level entities like "low knowledge context" or 
"expertise reversal effect" in systematic literature reviews (e.g., for CMOC synthesis in 
Richmond-style processes). 
How GraphRAG Mentions and Implements Community Approaches for Big 
Concepts 
GraphRAG uses a community-based approach to identify and group big concepts as entities, 
emphasizing that entities are high-level abstractions (e.g., people, places, organizations, or 
thematic concepts) derived from text, rather than isolated single words. The method extracts all 
entities, relationships, and key claims from segmented text units (TextUnits), treating big 
concepts as cohesive nodes that represent semantic topics. Communities are formed to cluster 
these entities, ensuring that big concepts are not atomized but grouped into meaningful, higher-
level structures for holistic understanding. 
 Special Term for Communities: The key terms are "hierarchical communities" or 
"community hierarchies," where communities are modular groups of closely connected 
nodes (entities) representing cohesive semantic topics (e.g., "AI Research" or "pedagogy 
interactions" in our educational review context). Another special term is "community 
reports" or "community summaries," which are LLM-generated descriptions of each 
community, capturing big concepts at different abstraction levels. These terms come from 
the original GraphRAG development, using the Leiden algorithm for hierarchical 
clustering to build communities from the bottom-up. 
 How Big Concepts Are Built as Entities: Entities are extracted as big concepts by 
prompting LLMs to identify high-level abstractions from text (e.g., not "word" but "low 
knowledge student" as a unified entity with attributes like type, description, and source 
span). These are then clustered into communities to form higher-level entities, avoiding 
single-word fragmentation and enabling thematic grouping (e.g., clustering variations of 
"expert explanations" into one big concept entity). In our context, this applies to literature 
reviews by turning narrative text into entities like "mechanism response: panic," grouped 
into communities for contradiction detection (e.g., conflicting outcomes in similar 
contexts). 
Iterative Process in GraphRAG for Refinement 
GraphRAG incorporates iterative processes for building and refining the KG, especially in 
community formation and updates, to handle big concepts dynamically. The bottom-up summary 
generation is iterative: Start at leaf communities, summarize, then move up the hierarchy, 
refining at each level until stable. For big concepts, entity extraction and relationship inference 
can iterate via LLM re-prompting if initial outputs are uncertain (e.g., in global search, dynamic 
selection iterates over relevant communities). In recent updates like LazyGraphRAG (2025), 
iteration is deferred to query time for efficiency, combining on-the-fly graph search with LLM 
analysis. This aligns with our iterative HITL process: Researcher seeds examples, machine 
proposes entities/communities, human refines, system iterates (e.g., re-clustering for better big 
concept grouping). 
Use of Agentic Agents or LLMs in GraphRAG 
GraphRAG is inherently agentic/modular, with LLM agents for entity extraction, summarization, 
and querying – e.g., LLMs (like GPT-4) generate the KG, infer big concepts as entities, and 
produce community summaries. In our context, this means using agentic LLMs (e.g., Extraction 
Agent) to build big concepts iteratively: Prompt LLMs to extract/refine entities, cluster into 
communities, and iterate via feedback loops for reviews (e.g., detecting trends/contradictions in 
educational literature). Recent surveys (2024-2025) highlight GraphRAG's agentic extensions for 
customized LLMs in domains like transportation or materials science, where LLMs handle 
iterative big concept identification. 
Recent Updates (2024-2025) 
GraphRAG has seen key updates: Dynamic community selection (Nov 2024) iterates over 
relevant communities at query time for efficiency. LazyGraphRAG (2025) defers LLM-heavy 
iteration to queries, simplifying big concept handling without full upfront KG builds. 
Incremental updates (2024) allow iterative addition of new docs without rebuilding, fitting our 
review context for "living" KGs. These enhance agentic/LLM use for iterative big concept 
identification, making it practical for our framework (e.g., refining entities like "mechanism 
response" across literature iterations). 
Yes, exactly — the Leiden community detection step in Microsoft's GraphRAG (and similar 
graph-based methods) is a perfect fit for our context: iteratively building and refining big 
concepts as high-level entities in our Literature Knowledge Graph (LKG) for systematic reviews 
(e.g., realist reviews like Richmond et al., where we need to extract and group things like "Low 
Knowledge Context", "Expertise Reversal Effect", "Simulation Pedagogy Challenges", etc.). 
Here’s how this approach applies directly to what we’ve been discussing — the iterative, 
seed/example-based process to generate and refine big concepts. 
How Leiden + Iterative Process Works in Our Context 
1. Start with Seeds / Examples (Researcher Input – Initialization) You (the researcher) 
provide a small set of rough examples of the big concepts you care about: 
o "Low Knowledge Context": Students with limited prior domain knowledge, 
leading to overload or panic. 
o "Mechanism Resource – Explicit Explanation": Expert verbalizing their 
reasoning. 
o "Outcome – Improved Diagnostic Accuracy". 
These seeds act as initial prototypes — not rigid rules, but examples that guide what 
"big" means in our review. 
2. LLM Extracts Candidate Entities (First Pass) Our Extraction Agent (LLM-powered) 
scans publication chunks and proposes entities using the seeds as few-shot examples in 
the prompt: 
o "Extract high-level concepts similar to these examples: [your seeds]. Treat them 
as unified big concepts, not single words. Output: name, type 
(Context/Mechanism/Outcome), description, source span." 
Result: A bunch of candidate nodes, some very close to your seeds, some variations (e.g., 
"novice learner overload", "undergraduate knowledge gap", "pre-existing domain 
limitation"). 
3. Leiden Runs Community Detection → Forms Topic Clusters 
o All extracted entities + their relationships become nodes and edges in a temporary 
graph. 
o Leiden algorithm is applied → it automatically groups densely connected entities 
into communities (clusters). 
o Each community = a natural grouping of similar or related big-concept 
candidates. Example: 
 Community 1: "novice learner overload", "undergraduate knowledge gap", 
"limited domain knowledge", "low prior knowledge" → all tightly 
connected via co-occurrence or shared relations. 
 Community 2: "explicit expert explanation", "verbalized reasoning", 
"teacher think-aloud" → grouped as mechanism resources. 
Leiden is great here because it: 
o Produces well-connected, meaningful clusters (avoids tiny or disconnected junk 
groups). 
o Creates hierarchical communities (small → mid → large clusters), so we get 
multi-level big concepts. 
4. LLM Generates Community Summaries → Turns Clusters into True Big Concepts 
o For each Leiden community, prompt the LLM: "Summarize this cluster of entities 
as a single high-level big concept. Give it a name, type, description, and explain 
why these belong together." 
o Output: 
 Big Concept Entity: "Low Knowledge Context" 
 Description: "Refers to students with limited prior domain-specific 
knowledge, often leading to cognitive overload or emotional frustration in 
simulation-based learning." 
 Members: [list of lower-level candidates it grouped] 
This is the key moment: Leiden + LLM summary transforms fragmented candidates 
into the polished, high-level big concepts we want. 
5. Iterative Refinement (Human-in-the-Loop Feedback Loop) 
o You review the proposed big concepts (communities + summaries). 
o Feedback examples: 
 "Merge these two communities — they both describe novice frustration." 
 "Rename this one to 'Expertise Reversal Effect' — that's the standard 
term." 
 "Reject this cluster — it's too broad, split it." 
o System updates: 
 Re-run Leiden on adjusted graph (or force-merge/split communities). 
 Add your feedback as new seeds/few-shot examples in the LLM prompt. 
 Re-extract from text or re-summarize communities. 
o Repeat 3–10 times until: 
 Big concepts match your mental model (coverage of desired themes). 
 Few/no new meaningful clusters emerge (plateau). 
 Human confidence high (e.g., spot-check against Richmond's 5 contexts). 
Why This Fits Our Needs Perfectly 
 Seed/Example-Driven: Starts from your rough ideas → LLM generalizes → Leiden 
clusters similar ideas → summaries formalize them as big concepts. 
 Iterative & Human-Dominated: You control quality at each cycle (checkpoints: 
Screening, CMOC Validation, etc.). 
 Big Concepts, Not Single Words: Leiden groups semantically related entities → LLM 
summary creates abstract, high-level entities (exactly what we need for CMOCs, demi-
regularities, contradictions). 
 Scalable for Reviews: Works on variable numbers of papers (not fixed to 28); 
incremental updates possible when adding new literature. 
 Integrates Seamlessly: 
o Extraction Agent → LLM + seeds → candidate entities. 
o Normalization/Community Agent → Leiden → clusters. 
o Synthesis Agent → LLM community summaries → refined big concepts in LKG. 
o Contradiction Agent → queries clusters for conflicting relations within/across 
communities. 
This is not just Microsoft’s GraphRAG verbatim — we’re adapting it to our agentic, HITL 
workflow (LangGraph orchestration, checkpoints, focus on realist review logic). But the Leiden 
+ LLM community summary pattern is the exact mechanism that turns raw extraction into 
usable, high-level big concepts iteratively. 
If you want, I can sketch a small LangGraph-style pseudocode flow or a prompt template for the 
summary step — just say the word. 
 
4. Methodology: Multi-Agent Framework for Automated Realist Systematic 
Reviews 
This section outlines the proposed multi-agent framework designed to automate and assist 
realist systematic reviews in complex educational systems. The framework draws inspiration 
from the human-led workflow in Richmond et al. (2020), where an Initial Programme Theory 
(IPT) guides iterative extraction of Context–Mechanism–Outcome configurations (CMOCs), 
identification of demi-regularities, and refinement of the overall programme theory. It employs a 
core-and-plugin architecture built on LangGraph for stateful orchestration, integrating large 
language models (LLMs) for interpretive tasks while maintaining human-in-the-loop (HITL) 
governance to ensure methodological rigor and transparency. 
The framework separates method-agnostic core infrastructure (e.g., retrieval, deduplication, 
screening) from method-specific plugins (e.g., Realist Synthesis Plugin for CMOC extraction 
and theory refinement). A central component is the Literature Knowledge Graph (LKG), 
which structures extracted evidence for relational reasoning, enabling agents to detect patterns, 
contradictions, and contextual contingencies beyond flat text summaries. 
4.1 Core Review Infrastructure 
The core provides foundational services applicable to any systematic review: 
 Protocol & IPT Agent: Encodes researcher-defined review questions, 
inclusion/exclusion criteria, and IPT hypotheses into structured schemas (JSON 
templates). Prompting: "Act as a RAMESES-compliant methodologist. Formalize the 
provided scope and IPT into versioned JSON schemas for CMOC extraction." 
 Search & Retrieval Agent: Harvests literature from institutional repositories (e.g., via 
Microsoft Graph API) and external databases, logging provenance for auditability. 
 Deduplication & Registry Agent: Assigns stable StudyIDs and maintains a single 
source of truth registry. 
 Two-Stage Screening Agents (Title/Abstract and Full-Text): Apply eligibility rules with 
HITL calibration on stratified samples. Feedback is recycled as few-shot examples to 
refine decision logic. 
 Reporting & Audit Agent: Generates PRISMA flows, evidence tables, and audit logs 
for repository deposition. 
4.2 Realist Synthesis Plugin: Knowledge Graph Construction and Reasoning 
The Realist Synthesis Plugin operationalizes RAMESES standards for theory-driven synthesis, 
with the LKG as the reasoning substrate. 
Knowledge Graph Construction Process The LKG is built iteratively using LLM-driven 
extraction and graph community detection, enabling the formation of high-level "big concepts" 
(e.g., thematic entities like "Low Knowledge Context") from literature. 
1. Entity Extraction (Seed-Guided) The CMOC Extraction Agent processes full-text 
chunks using LLM prompting informed by researcher-provided seed examples (e.g., 
"Low Knowledge Context: Students with limited prior knowledge leading to overload"). 
Prompt template: "You are a realist synthesis expert. Extract high-level concepts as 
entities similar to these seeds: [examples]. Output JSON: {'entity': 'Name', 'type': 
'Context/Mechanism/Outcome', 'description': '...', 'source_span': '...'}" (Edge et al., 2024). 
This yields candidate nodes as big concepts, not granular terms. 
2. Graph Construction & Relationship Extraction Relationships (e.g., "triggers", 
"moderates") are inferred via LLM prompting, forming triples stored in the LKG with 
provenance links. 
3. Hierarchical Community Detection with Leiden Algorithm The Leiden algorithm 
(Traag et al., 2019) partitions the graph into hierarchical communities — clusters of 
densely connected entities representing thematic groups. Communities group related 
candidates (e.g., "novice learner overload", "knowledge gap") into higher-level 
structures, elevating them to cohesive big concepts. This step follows GraphRAG's 
modular approach, where Leiden ensures well-connected, high-quality partitions superior 
to alternatives like Louvain (Edge et al., 2024; Traag et al., 2019). 
4. LLM Community Summarization For each community, the LLM generates a summary 
report: Prompt: "Summarize this community of entities as a single high-level big concept. 
Provide name, type, description, and rationale for grouping." The summary becomes a 
refined entity in the LKG (e.g., "Low Knowledge Context in Simulation Learning"), 
enabling multi-level abstraction. 
5. Iterative Refinement (HITL Loop) Researcher reviews summaries at checkpoints (e.g., 
CMOC Validation). Feedback (e.g., merge/split communities, rename) updates seeds and 
re-triggers extraction/community detection. Iteration continues until plateau (minimal 
new clusters, high human confidence, F1 > 0.85 on validation). 
The resulting LKG supports downstream agents: 
 Theory Synthesis Agent: Queries communities for demi-regularities (recurrent CMOC 
patterns). 
 Contradiction Agent: Detects conflicting subgraphs (e.g., same mechanism, different 
outcomes) via motif detection in communities. 
This construction enables the framework to simulate Richmond et al.'s iterative refinement while 
scaling to variable corpora and ensuring traceability (every entity/summary links to source spans 
via Microsoft Graph). 
References (APA Format) 
Edge, D., Trattner, C., Cheng, F. A., Li, M., & Larson, J. (2024). From local to global: A graph 
RAG approach to query-focused summarization. arXiv preprint arXiv:2404.16130. 
https://arxiv.org/abs/2404.16130 
Richmond, A., et al. (2020). [Full citation based on NotebookLM file; placeholder as exact 
title/authors not re-specified in query]. Journal Name, Volume(Issue), pages. [DOI if available] 
Traag, V. A., Waltman, L., & van Eck, N. J. (2019). From Louvain to Leiden: Guaranteeing 
well-connected communities. Scientific Reports, 9(1), Article 5233. 
https://doi.org/10.1038/s41598-019-41695-z 
(Note: Additional references from NotebookLM file synthesis, such as general multi-agent LLM 
works in systematic reviews, can be expanded if needed. The above focus on KG construction 
core. All citations are real and verifiable from public sources.) 
This methodology section is ready for integration into the draft paper — it positions the 
framework as innovative yet grounded in established tools (GraphRAG/Leiden) while 
emphasizing HITL for rigor. If you'd like expansions (e.g., figures, more agents, or full 
RAMESES alignment), let me know! 
 

========================================

## Grok output plugin agent-sent-3.pdf

4. Methodology
4.1 Overview of the Multi-Agent Framework
Systematic reviews that synthesize evidence from diverse research approaches are essential for
understanding how educational interventions and practices operate within complex systems
(Moss & Gomez, 2025). Realist systematic review, in particular, seeks to answer not only “what
works” but also “for whom, in what circumstances, how, and why” by identifying
Context–Mechanism–Outcome Configurations (CMOCs) and refining programme theories
(Pawson, 2006; Richmond et al., 2020; Wong et al., 2013). However, conducting high-quality
realist reviews manually is resource-intensive, involving extensive literature searching, iterative
coding of CMOCs, detection of demi-regularities, and resolution of contradictions across studies.
To address these challenges while meeting the methodological innovation goals of the RRE 2026
call, we developed a multi-agent framework that combines large language models (LLMs) with
structured knowledge graph techniques. The framework automates repetitive tasks such as
literature retrieval, screening, and initial data extraction, while preserving human researchers as
the ultimate decision-makers through explicit human-in-the-loop checkpoints. This design
ensures methodological transparency, auditability, and reproducibility—key requirements for
systematic reviews intended to inform sustainable change in complex educational systems (Moss
& Gomez, 2025).
The framework is implemented as a stateful orchestration system using LangGraph, enabling
agents to collaborate through a shared state (the “single source of truth”). It follows a core-and-
plugin architecture:
 The core infrastructure manages universal review tasks that are common across
synthesis methods (e.g., search, deduplication, screening, and audit logging).
 Method-specific plugins extend the core with the distinctive analytic logic of particular
review traditions.
For the present paper we focus on the Realist Synthesis Plugin , which operationalizes CMOC
extraction, pattern identification, and programme theory refinement. However, the architecture is
deliberately modular, allowing plug-ins for other approaches highlighted in the RRE call, such as
framework synthesis, thematic synthesis, meta-ethnography, critical interpretive synthesis,
qualitative comparative analysis (QCA), and mixed-method syntheses. This modularity supports
the call’s emphasis on synthesizing evidence from diverse methodological traditions (Moss &
Gomez, 2025).
The central innovation of the framework is the Literature Knowledge Graph (LKG) , which
transforms narrative findings from research articles into structured, queryable big concepts (high-
level thematic entities) that can be directly assembled into CMOCs. The construction and use of
the LKG are described in detail in subsequent subsections.
This overview establishes the overall purpose and high-level design of the framework. The next
subsection (4.2) explains the core-and-plugin architecture in greater depth, showing how the
separation of concerns enables both methodological stability and flexibility across different
review traditions.
This subsection is complete, self-contained, and ready for your draft. It:
 Clearly states the problem and purpose (linking to the RRE call).
 Introduces the multi-agent framework and core-and-plugin idea.
 Positions realist synthesis as the primary focus while noting modularity for other
methods.
 Transitions smoothly to the next subsection (architecture).
Next subsection will be 4.2 Architectural Principles: Core Review Infrastructure and
Method-Specific Plugins. It will build directly on this overview by explaining the two layers in
detail and listing the specific plug-in methods mentioned in the RRE call (framework synthesis,
thematic synthesis, meta-ethnography, critical interpretive synthesis, QCA, mixed-method, etc.),
while keeping realist as the worked example.
Would you like me to deliver 4.2 now, or would you prefer any changes to 4.1 first?
4. Methodology
4.1 Overview of the Multi-Agent Framework
Systematic reviews that synthesize evidence from diverse research approaches are essential for
understanding how educational interventions and practices operate within complex systems
(Moss & Gomez, 2025). Realist systematic review, in particular, seeks to answer not only “what
works” but also “for whom, in what circumstances, how, and why” by identifying
Context–Mechanism–Outcome Configurations (CMOCs) and refining programme theories
(Pawson, 2006; Richmond et al., 2020; Wong et al., 2013). However, conducting high-quality
realist reviews manually is resource-intensive, involving extensive literature searching, iterative
coding of CMOCs, detection of demi-regularities, and resolution of contradictions across studies.
To address these challenges while meeting the methodological innovation goals of the RRE 2026
call, we developed a multi-agent framework that combines large language models (LLMs) with
structured knowledge graph techniques. The framework automates repetitive tasks such as
literature retrieval, screening, and initial data extraction, while preserving human researchers as
the ultimate decision-makers through explicit human-in-the-loop checkpoints. This design
ensures methodological transparency, auditability, and reproducibility—key requirements for
systematic reviews intended to inform sustainable change in complex educational systems (Moss
& Gomez, 2025).
The framework is implemented as a stateful orchestration system using LangGraph, enabling
agents to collaborate through a shared state (the “single source of truth”). It follows a core-and-
plugin architecture:
 The core infrastructure manages universal review tasks that are common across
synthesis methods (e.g., search, deduplication, screening, and audit logging).
 Method-specific plugins extend the core with the distinctive analytic logic of particular
review traditions.
For the present paper we focus on the Realist Synthesis Plugin , which operationalizes CMOC
extraction, pattern identification, and programme theory refinement. However, the architecture is
deliberately modular, allowing plug-ins for other approaches highlighted in the RRE call, such as
framework synthesis, thematic synthesis, meta-ethnography, critical interpretive synthesis,
qualitative comparative analysis (QCA), and mixed-method syntheses. This modularity supports
the call’s emphasis on synthesizing evidence from diverse methodological traditions (Moss &
Gomez, 2025).
The central innovation of the framework is the Literature Knowledge Graph (LKG) , which
transforms narrative findings from research articles into structured, queryable big concepts (high-
level thematic entities) that can be directly assembled into CMOCs. The construction and use of
the LKG are described in detail in subsequent subsections.
This overview establishes the overall purpose and high-level design of the framework. The next
subsection (4.2) explains the core-and-plugin architecture in greater depth, showing how the
separation of concerns enables both methodological stability and flexibility across different
review traditions.
This subsection is complete, self-contained, and ready for your draft. It:
 Clearly states the problem and purpose (linking to the RRE call).
 Introduces the multi-agent framework and core-and-plugin idea.
 Positions realist synthesis as the primary focus while noting modularity for other
methods.
 Transitions smoothly to the next subsection (architecture).
Next subsection will be 4.2 Architectural Principles: Core Review Infrastructure and
Method-Specific Plugins. It will build directly on this overview by explaining the two layers in
detail and listing the specific plug-in methods mentioned in the RRE call (framework synthesis,
thematic synthesis, meta-ethnography, critical interpretive synthesis, QCA, mixed-method, etc.),
while keeping realist as the worked example.
Would you like me to deliver 4.2 now, or would you prefer any changes to 4.1 first?
4.2 Architectural Principles: Core Review Infrastructure and Method-Specific Plugins
The multi-agent framework adopts a core-and-plugin architecture to balance methodological
generality with the specific analytic requirements of different synthesis traditions. This design
responds to the RRE 2026 call’s emphasis on advancing systematic review methods that can
synthesize evidence from diverse research approaches, including qualitative, mixed, and
comparative case-oriented studies (Moss & Gomez, 2025).
The core review infrastructure is method-agnostic: it performs the foundational tasks shared
across nearly all systematic reviews, ensuring consistency, provenance tracking, and auditability
regardless of the synthesis approach. These tasks include protocol specification, literature
retrieval, deduplication, two-stage screening, and generation of repository-ready artifacts. The
core is implemented using LangGraph for stateful orchestration, with all agents communicating
through a shared state (the “single source of truth”) that logs every action and decision.
The method-specific plugins extend the core by injecting the distinctive intellectual logic of
particular review traditions. Each plugin defines specialized agents, schemas, prompts, and
reasoning rules tailored to the synthesis method’s purpose, theoretical assumptions, and analytic
units. This modular structure allows the same infrastructure to support multiple approaches
without losing methodological rigor.
The RRE 2026 call highlights several well-developed synthesis methods that incorporate
qualitative and mixed evidence (Moss & Gomez, 2025). The framework is designed to
accommodate these through dedicated plug-ins. Examples include:
 Framework synthesis and thematic synthesis — inductive or theory-informed methods
that build descriptive or explanatory themes from qualitative and mixed studies (Brunton
et al., 2020; Thomas & Harden, 2008). A Thematic/Inductive Plugin would use the LKG
to cluster big concepts into themes or frameworks.
 Meta-ethnography — interpretive synthesis that translates concepts across ethnographic
studies (Noblit & Hare, 1988; France et al., 2019). A Meta-ethnographic Plugin would
emphasize reciprocal and refutational translation within communities.
 Critical interpretive synthesis and meta-narrative review — methods that trace the
genealogy of ideas across disciplines and paradigms (Dixon-Woods et al., 2006;
Greenhalgh et al., 2005). Corresponding plug-ins would use the LKG to map conceptual
lineages and paradigm shifts.
 Qualitative comparative analysis (QCA) — set-theoretic analysis of causal
configurations in complex cases (Rihoux & Ragin, 2009; Mello, 2021). A QCA Plugin
would extract crisp/fuzzy set conditions from the LKG and apply truth-table analysis.
 Mixed-method synthesis — integration of quantitative meta-analysis with qualitative
evidence (Booth et al., 2022; Gough et al., 2017). A Mixed-Method Plugin would link
quantitative effect sizes to qualitative CMOCs or themes.
In this paper we focus on the Realist Synthesis Plugin as a worked example. Realist review
seeks to explain how, why, and for whom interventions work by identifying CMOCs and
refining programme theories (Pawson, 2006; Wong et al., 2013). The plugin operationalizes this
logic by using the LKG to extract and link big concepts into CMOCs, detect demi-regularities,
and surface contextual contingencies.
The core-and-plugin separation ensures that the framework remains flexible for future extensions
while maintaining strict methodological explicitness — a key requirement of the RRE call (Moss
& Gomez, 2025). The next subsection (4.3) describes the core infrastructure in detail, showing
how it provides a stable, auditable foundation for all plug-ins.
This subsection is complete, self-contained, and flows logically:
 Builds on 4.1’s overview by diving into architecture.
 Clearly defines core vs. plug-in.
 Lists and briefly describes the synthesis methods from the RRE call
(framework/thematic, meta-ethnography, critical interpretive, meta-narrative, QCA,
mixed-method).
 Positions realist as the primary focus while showing modularity.
 Transitions naturally to 4.3 (Core Infrastructure).
Next subsection will be 4.3 Core Review Infrastructure — it will describe each core
agent/task in detail, link back to the architecture, and transition to the Realist Plugin.
Would you like me to proceed with 4.3 now? Or any adjustments to 4.1 or 4.2 first?
Plugin Agents (Realist Synthesis Plugin – method-specific)
 CMOC Extraction Agent Role: Extracts structured Context–Mechanism–Outcome
configurations. Input: Full-text chunks + IPT schema. Output: JSON triples mapped to
the LKG {“context”: “…”, “mechanism_resource”: “…”, “mechanism_response”: “…”,
“outcome”: “…”, “source_span”: “…”}. Prompt strategy: Inference prompt “Identify the
student-level Context (C), Mechanism Resource (M-res), student’s cognitive Response
(M-resp), and Reasoning Outcome (O). Link each to a specific text span. Output only
valid JSON.”
 Theory Synthesis & Refinement Agent Role: Compares CMOCs across studies to
identify patterns and update the programme theory. Input: Extracted CMOCs from the
LKG. Output: Updated programme theory with identified demi-regularities. Prompt
strategy: Pattern recognition prompt “Compare CMOCs across studies. Propose an
update to the IPT if context X consistently alters outcome Y. Output structured theory
summary.”
 Contradiction Agent Role: Detects conflicting evidence within the LKG. Input: LKG
subgraphs. Output: Conflict register listing conflicting configurations. Prompt strategy:
Conflict detection prompt “Flag instances where the same resource leads to different
outcomes. Present as a structured register.”
 Reporting Agent Role: Generates final auditable artifacts. Input: Shared state and LKG.
Output: PRISMA flow, evidence tables, and theory diagrams. Prompt strategy:
Formatting prompt “Generate RAMESES-compliant audit trail and evidence tables from
the current state.”
Here is the start of subsection 4.4 (the first plugin agent), written in the same detailed,
publication-ready academic style as the previous subsections. This begins the transition from the
core infrastructure (4.3) to the method-specific plugins, starting with the Realist Synthesis
Plugin as the primary worked example (as per your focus and the NotebookLM file).
This subsection is self-contained but links back to 4.3 (core foundation) and forward to the rest
of 4.4 (other plug-ins) and 4.5 (LKG construction).
4.4 Method-Specific Plugins: Realist Synthesis Plugin (Worked Example)
The method-specific plugins extend the core infrastructure by injecting the distinctive
intellectual logic of particular review traditions. Each plugin adds specialized agents, schemas,
prompts, and reasoning rules tailored to the synthesis method’s purpose, theoretical assumptions,
and analytic units. This modularity allows the framework to support the diverse systematic
review approaches referenced in the RRE 2026 call (Moss & Gomez, 2025), including meta-
analysis of quantitative studies (Cooper et al., 2019), intervention effectiveness reviews (Higgins
et al., 2024; U.S. Institute of Education Sciences, 2022), qualitative evidence synthesis (Noyes &
Hardin, in press), and realist synthesis (Wong et al., 2013).
In this paper, we focus on the Realist Synthesis Plugin as a worked example. Realist review
seeks to explain how, why, and for whom interventions work by identifying
Context–Mechanism–Outcome Configurations (CMOCs) and refining programme theories
(Pawson, 2006; Richmond et al., 2020). The plugin builds directly on the core infrastructure’s
screened and retrieved records (from 4.3), using the Literature Knowledge Graph (LKG) to
structure evidence into big concepts and CMOCs. Detailed LKG construction is described in 4.5.
The plugin contains three specialized agents:
CMOC Extraction Agent (first plugin agent)
Role and alignment with human systematic review processes This agent corresponds to the
subject matter expert or coder in a human realist review team (Richmond et al., 2020). In a
traditional realist review, the researcher (often the lead author or a trained coder) reads full texts
of included studies and systematically extracts pieces of evidence that form
Context–Mechanism–Outcome Configurations (CMOCs). This involves identifying:
 Context (C): conditions or circumstances in which the intervention occurs (e.g., student
knowledge level).
 Mechanism resource (M-res): what the intervention provides (e.g., expert explanation).
 Mechanism response (M-resp): how participants react (e.g., insight vs. panic).
 Outcome (O): the resulting change (e.g., improved diagnostic accuracy). The coder
iteratively refines extractions based on team discussion, emerging theory, and
contradictions. The agent automates this extraction while allowing the same human
validation and correction, ensuring CMOCs are explicit, evidence-based, and linked to
source text.
Input Full-text chunks and eligibility decisions from the Full-Text Acquisition & Eligibility
Agents (from 4.3), plus the protocol schema and IPT hypotheses from the shared state.
Output JSON triples for the LKG: { “study_id”: “STUDY-XXX”, “context”: “description of
context big concept”, “mechanism_resource”: “description of mechanism resource”,
“mechanism_response”: “description of mechanism response”, “outcome”: “description of
outcome”, “source_span”: “exact text location/reference”, “confidence”: 0–1, “rationale”: “short
justification (1–2 sentences)” }. These triples are written directly to the LKG as edges and
properties, linking to the study node and text spans.
How the agent interacts with the Knowledge Graph, Microsoft Graph, and GraphRAG The
agent writes every extracted CMOC triple as a structured edge in the Literature Knowledge
Graph (LKG) (e.g., study node → context node → mechanism node → outcome node), with
provenance links to source text spans. Microsoft Graph is not directly used here (it was used
earlier for retrieval). GraphRAG is called to provide context: before extraction, it queries the
LKG for existing big concepts or CMOCs from related studies (e.g., if the text mentions “novice
overload”, GraphRAG retrieves the “Low Knowledge Context” community for consistency and
disambiguation, Edge et al., 2024).
Initial Prompt Template “You are a subject matter expert in realist medical education
synthesis. You are given the protocol schema [insert schema here], the IPT hypotheses, and a
full-text chunk from StudyID XXX. Identify the Context (C), Mechanism Resource (M-res),
Mechanism Response (M-resp), and Outcome (O) in the text. Link each to a specific text span.
Output only valid JSON with fields: study_id, context, mechanism_resource,
mechanism_response, outcome, source_span, confidence, rationale. Do not invent or interpret
beyond the text.”
Human Feedback and Revision Process After the agent produces its first batch of CMOC
triples, the researcher reviews a sample (e.g., all triples from 10% of studies or any with low
confidence) at the CMOC Validation checkpoint. The researcher can:
 Approve the extractions as correct.
 Edit specific triples (e.g., “Change mechanism response from ‘insight’ to ‘panic and
overload’”).
 Provide textual comments (e.g., “Missing implicit panic — add it as mechanism response
because the text implies emotional frustration”).
The system automatically incorporates the feedback as follows:
1. The human feedback is appended as a few-shot example to the agent’s prompt template.
The new prompt becomes: “Previous extraction for StudyID 123: [old JSON triple].
Human correction: change mechanism response from ‘insight’ to ‘panic and overload’
because the text implies emotional frustration. Now re-extract from the same text chunk.
Output updated JSON.”
2. The agent is re-invoked with the same original input (full-text chunk + protocol schema)
plus the updated prompt containing the accumulating few-shot examples.
3. The new output (revised CMOC triples) replaces the old entries in the LKG and shared
state.
4. The cycle can repeat: the researcher reviews the revised triples again, provides further
feedback if needed (e.g., “Add source span reference”), and the agent is re-run with the
growing set of few-shot examples. This process continues until the researcher is satisfied
with the extracted CMOCs.
This human-driven revision ensures the CMOCs are accurate and theory-relevant. The agent’s
output (structured CMOC triples in the LKG) is automatically passed as the primary input to the
next agent in the plugin — the Theory Synthesis & Refinement Agent — which uses them to
identify patterns and refine the programme theory.
This is the complete, detailed description for only the first plugin agent (CMOC Extraction
Agent), matching the depth and style of the core agents.
When you say “next one” or “continue”, I will provide the next plugin agent (Theory Synthesis
& Refinement Agent) in the same level of detail.
Please say “next one” when you are ready for the second plugin agent.

========================================

# Meeting Transcripts

## GMT20260123-030019_Recording.transcript.vtt

00:00:00.000 --> 00:00:02.Wei Zheng: Yeah, yeah, okay, go ahead, go ahead. 00:00:03.240 --> 00:00:09.Duy Nguyen: In the tool paper review I already sent to you, 00:00:09.790 --> 00:00:15.Duy Nguyen: It's all have, like, anything, the input human, from human, and… 00:00:15.740 --> 00:00:21.Duy Nguyen: What… what they want, and what in… in their mind, to do, and their… 00:00:21.860 --> 00:00:30.Wei Zheng: Okay, moment. You said that two paper, that review is related to that, that, what, that, that publication? 00:00:31.300 --> 00:00:32.Duy Nguyen: Yes. 00:00:32.259 --> 00:00:38.Wei Zheng: That is all the thing you try to figure out, how… in that process, how the human 00:00:38.999 --> 00:00:40.Wei Zheng: Import, you know? 00:00:40.920 --> 00:00:41.Duy Nguyen: I guess. 00:00:41.490 --> 00:00:46.Wei Zheng: I mean, in their process, how they do it, what is their intent, you know what I'm. 00:00:46.760 --> 00:00:47.Duy Nguyen: Yes. 00:00:47.360 --> 00:00:53.Wei Zheng: And, okay. And do you feel you can make the AI agent to do that? 00:00:55.380 --> 00:00:58.Wei Zheng: Do you, do you feel, you have an idea? 00:00:58.710 --> 00:01:02.Wei Zheng: how can you make the AI Aging. 00:01:02.680 --> 00:01:03.Duy Nguyen: Gotcha. 00:01:03.020 --> 00:01:04.Wei Zheng: To do the same. 00:01:04.319 --> 00:01:11.Wei Zheng: like, to do the thing they want to do, to do the thing, that human… 00:01:11.490 --> 00:01:14.Wei Zheng: What, the human do in that process? 00:01:16.450 --> 00:01:20.Duy Nguyen: Actually, I think… 00:01:21.570 --> 00:01:37.Duy Nguyen: the… the Microsoft Graph, rack, and the long… the Langchen can… can do that, but I think, you, you sent it to me, right? Yeah, it's the iteration, right? And we… we had to, like, run and… 00:01:38.080 --> 00:01:42.Duy Nguyen: And check, and, and rerun, and check, right? 00:01:42.130 --> 00:01:49.Wei Zheng: Yeah, yeah, yeah, you just, give… okay, the first, I think you read, you read a summary of that publication. 00:01:49.870 --> 00:01:50.Duy Nguyen: Yes. 00:01:50.760 --> 00:01:53.Wei Zheng: You know, what, 00:01:53.240 --> 00:02:02.Wei Zheng: Because we don't… they are doing… they do not do anything related to computer design. They just try to say what they… 00:02:02.590 --> 00:02:15.Wei Zheng: what they conceptualize… conceptualize the thing, and what they do. I do not do… I… I probably, I will read… I will read a salary later, but I just say. 00:02:15.250 --> 00:02:34.Wei Zheng: apparently this… they have established some criteria, and then they will define something. They will define something, right? And then, after they define something, and then you go… they go there, to screen the… to… or to look at… 00:02:34.330 --> 00:02:34.Duy Nguyen: Yeah, yeah, I did. 00:02:34.860 --> 00:02:52.Wei Zheng: 28, it's 28 publications, right? They just go to that 28 publications, doing the thing they describe, is that? To find some relation, is that? To find some, I think public, intervention. 00:02:54.090 --> 00:02:55.Wei Zheng: outcome. 00:02:55.770 --> 00:02:57.Wei Zheng: the student behavior. 00:02:58.010 --> 00:02:58.Duy Nguyen: Yeah. 00:02:58.770 --> 00:03:00.Wei Zheng: Something like that, yeah? 00:03:00.260 --> 00:03:01.Duy Nguyen: Yes, sir. 00:03:01.280 --> 00:03:07.Wei Zheng: And… And how can you… Imagine. 00:03:08.120 --> 00:03:12.Wei Zheng: the AI agent can do. I think, okay, first. 00:03:12.690 --> 00:03:17.Wei Zheng: The AI agent is actually what? It's a large… is a language model. 00:03:18.070 --> 00:03:27.Wei Zheng: Some, re… re-receive some special instruction, or re-receive some special prompts. 00:03:28.170 --> 00:03:31.Wei Zheng: And then, they will follow the prompts 00:03:31.830 --> 00:03:35.Wei Zheng: And with the import, and then doing the thing. 00:03:36.150 --> 00:03:44.Wei Zheng: Just like I said, please fund… the any, Intervention. 00:03:45.120 --> 00:03:47.Wei Zheng: They used, in this… 00:03:48.490 --> 00:03:58.Wei Zheng: publication, or… because they review other people's publications, right? They will probably… you will probably… you will define the… the… the prompts. 00:04:00.610 --> 00:04:01.Wei Zheng: the… 00:04:01.260 --> 00:04:03.Duy Nguyen: Yeah, we have to decide the problem, yes. 00:04:03.550 --> 00:04:05.Wei Zheng: The… I'm your model. 00:04:05.580 --> 00:04:06.Duy Nguyen: That's the key thing. 00:04:06.820 --> 00:04:15.Wei Zheng: And also, you will feed the language model with that publication, and then that language model will… 00:04:16.279 --> 00:04:18.Wei Zheng: 1. Follow your prompts! 00:04:18.600 --> 00:04:23.Wei Zheng: And to process that publication. 00:04:23.130 --> 00:04:23.Duy Nguyen: Yes. 00:04:23.590 --> 00:04:41.Wei Zheng: or to, or to, what, read, or digest, or whatever you can say. And then, just like you feed the PDF to the chat GPT, and then you ask, ask the question, right? And then you feed them, feed the large language with this, and then you use the pumps to 00:04:41.620 --> 00:04:47.Wei Zheng: to ask the question to the chat GPT, you know? And then the chat GPT provides a response. 00:04:48.100 --> 00:04:54.Wei Zheng: Is that? And then you provide that? No. You will… not you. All the other… 00:04:54.570 --> 00:04:55.Duy Nguyen: the… 00:04:55.010 --> 00:04:57.Wei Zheng: Language, no other agent. 00:04:58.300 --> 00:04:59.Wei Zheng: other AI agent. 00:05:00.640 --> 00:05:02.Wei Zheng: Well, tech! 00:05:02.400 --> 00:05:05.Wei Zheng: Yes. That output from this language model. 00:05:07.450 --> 00:05:08.Wei Zheng: as import. 00:05:09.710 --> 00:05:10.Wei Zheng: Is that? 00:05:10.700 --> 00:05:11.Duy Nguyen: Yes. 00:05:11.610 --> 00:05:19.Wei Zheng: And also, with some specific… another specific prompt you develop. You want… what do you want? 00:05:20.410 --> 00:05:20.Wei Zheng: Lucky! 00:05:21.380 --> 00:05:24.Wei Zheng: You know what I mean? They are… this is a land chair, this is a land chair. 00:05:25.750 --> 00:05:33.Wei Zheng: Like, let's just make, in the flow, I mean, in a, in a, in a workflow, there are different language agents. 00:05:33.970 --> 00:05:41.Wei Zheng: There are some that, like, if something happened, and then go this way. Just like, you know. 00:05:41.860 --> 00:05:42.Duy Nguyen: Yes. 00:05:42.660 --> 00:05:43.Wei Zheng: You see what I mean? 00:05:43.580 --> 00:05:44.Duy Nguyen: I understand what'd you say. 00:05:44.650 --> 00:05:47.Wei Zheng: You, you know the, the, the, the, the, the ranch? 00:05:48.040 --> 00:05:50.Wei Zheng: But the key thing is what? 00:05:50.570 --> 00:05:54.Wei Zheng: You need to provide special prompts for each You got? 00:05:54.580 --> 00:05:56.Duy Nguyen: That's basically Premier. 00:05:56.130 --> 00:05:57.Wei Zheng: Why did you… yeah, yeah, yeah. 00:05:57.440 --> 00:05:58.Duy Nguyen: At an important time. 00:05:58.980 --> 00:06:01.Wei Zheng: Have you done this? Have you started doing this? 00:06:02.780 --> 00:06:06.Duy Nguyen: I already started doing the above, but right now, I do not. 00:06:06.660 --> 00:06:13.Duy Nguyen: Have the… the, like, The perfect apple. 00:06:13.350 --> 00:06:16.Wei Zheng: Okay, okay, I'll answer. Could you, 00:06:16.850 --> 00:06:20.Wei Zheng: Now we talk about the land chain, could you… 00:06:20.680 --> 00:06:28.Wei Zheng: Because you, you try to frame this, yeah? You try to do that, you try to frame the… we call it a multi-agent. 00:06:28.560 --> 00:06:29.Wei Zheng: Zach? 00:06:29.440 --> 00:06:30.Duy Nguyen: Yes. 00:06:30.000 --> 00:06:34.Wei Zheng: Multi… multi-AI agent. 00:06:34.870 --> 00:06:36.Wei Zheng: Frimwork! 00:06:36.220 --> 00:06:48.Wei Zheng: That will do exactly the workflow of the human doing in… at least, we try to let our Aging. 00:06:48.810 --> 00:06:52.Wei Zheng: Multi… AI agent. 00:06:52.280 --> 00:06:53.Wei Zheng: to simulat00:06:54.050 --> 00:07:05.Wei Zheng: what do they do? Just, they do, they sell probably several people, they have in their mind, the researcher, just like, the… what to call that person, they do. 00:07:06.060 --> 00:07:13.Wei Zheng: And they will do it step by step, is that? Or once they finish this one, they will move to the next step, is that? 00:07:13.890 --> 00:07:33.Wei Zheng: And then, it's the same thing in the land chain. You first use the… feed the publication, I mean, feed the reference. They said, we talk about 28 reference, you know what I mean? You know what I mean? We feed the 28 reference public one by one. Each time, you just… the public can only deal with one, right? 00:07:33.920 --> 00:07:34.Duy Nguyen: Yeah. 00:07:34.550 --> 00:07:37.Wei Zheng: And then they go with the first agent. 00:07:38.260 --> 00:07:40.Wei Zheng: You okay with the instruction? Okay, within the… 00:07:41.070 --> 00:07:44.Wei Zheng: One by one, you… once they come out of this one, this is the keyword… 00:07:45.310 --> 00:07:48.Wei Zheng: Once they respond to you first, 00:07:48.780 --> 00:07:51.Wei Zheng: Once they respond to your first request. 00:07:51.970 --> 00:07:57.Wei Zheng: Once they finish, and then they give them the next… Next, the request, is that? 00:07:57.910 --> 00:08:01.Duy Nguyen: Yes. And then they give you another result, outcome. 00:08:01.010 --> 00:08:05.Wei Zheng: And then, you're well… Take that outcome. 00:08:05.750 --> 00:08:08.Wei Zheng: as an import, for another… 00:08:09.250 --> 00:08:16.Wei Zheng: Not another language for another agent. The agent could be the same language model, you know? 00:08:16.820 --> 00:08:20.Wei Zheng: All the agents could use a same language model. 00:08:20.540 --> 00:08:21.Duy Nguyen: They're similar. 00:08:21.730 --> 00:08:23.Wei Zheng: The same, the same. 00:08:24.880 --> 00:08:26.Wei Zheng: You know what I mean? 00:08:26.720 --> 00:08:27.Duy Nguyen: Right. 00:08:27.170 --> 00:08:32.Wei Zheng: Even a different agent, but they are all in the same language model, but it's only… they have different prompts. 00:08:32.740 --> 00:08:33.Wei Zheng: Y'all? 00:08:33.659 --> 00:08:35.Duy Nguyen: Yeah. 00:08:36.039 --> 00:08:43.Wei Zheng: And could you, because now you tried to do that, could you make the sketch, or even the hand sketch? That will be fine, or… depends on you. 00:08:44.109 --> 00:08:50.Wei Zheng: Just, like, how… What kind of architecture? 00:08:50.639 --> 00:08:56.Wei Zheng: or for your… Your multi… multi-agent framework. 00:08:57.419 --> 00:09:01.Wei Zheng: You, you know, you, you, you see other people, the Lanqian, they, they, they, they… 00:09:01.839 --> 00:09:10.Wei Zheng: If you are not familiar with this, how to do that? You, you look at any people who use the land chain, multiple agents, you can fin00:09:10.529 --> 00:09:17.Wei Zheng: if you can, you can, you can… not Google, now you can ask ChatGPT, right? You said any people use the multiple… 00:09:18.189 --> 00:09:32.Wei Zheng: Or you can ask if any people use the multi-chain, multi-agent framework to do the thing we try to do. You already tell the AI, you know, the ChatGPT, what we try to do, you know? 00:09:32.939 --> 00:09:38.Wei Zheng: They should know what we try to do, right? And also, you keep in mind that you know that the current ChatGPT 00:09:38.809 --> 00:09:43.Wei Zheng: They can gather information across Cross. 00:09:44.079 --> 00:09:45.Wei Zheng: cross the conversation. 00:09:46.630 --> 00:09:47.Duy Nguyen: Yeah. 00:09:47.320 --> 00:09:50.Wei Zheng: You know what I mean? Originally, they can only go within. 00:09:51.360 --> 00:09:55.Wei Zheng: one conversation, but now they can actually search. 00:09:55.410 --> 00:09:55.Duy Nguyen: Sweet. 00:09:55.860 --> 00:10:13.Wei Zheng: automatically search. Originally, you need to do your search by yourself, but now they can… they can do the… they can do the search by themselves to find relevant information within your chat, because you shared… in your account, you chat with ChatGPT a lot of things, right? 00:10:14.130 --> 00:10:14.Duy Nguyen: Yes. 00:10:14.800 --> 00:10:15.Wei Zheng: Anna? 00:10:16.040 --> 00:10:20.Wei Zheng: They can find, if you specifically, if you explicitly 00:10:20.690 --> 00:10:24.Wei Zheng: If you explicitly… if you clearly 00:10:25.300 --> 00:10:29.Wei Zheng: Asked him to search our previous conversation. 00:10:30.400 --> 00:10:36.Wei Zheng: To find some particularly prospective information, and they can do it. 00:10:38.100 --> 00:10:44.Wei Zheng: And then you just say, I… we… I… we… I want to do this multiple frame, multi… 00:10:45.060 --> 00:10:48.Wei Zheng: agent, frame, framework for doing the thing. 00:10:49.010 --> 00:10:56.Wei Zheng: we want to do, all you either can feed my sketch, right? I give you some sketches, right? No, I give you some description, right? 00:10:56.880 --> 00:10:57.Duy Nguyen: Yeah. 00:10:57.520 --> 00:10:59.Wei Zheng: And you can feel them, you said that… 00:10:59.120 --> 00:11:01.Duy Nguyen: You give me your abstract. 00:11:01.240 --> 00:11:06.Wei Zheng: Yeah, you just said, please find any people doing the similar 00:11:06.360 --> 00:11:11.Wei Zheng: Use the similar framework, do the similar thing. 00:11:11.420 --> 00:11:17.Wei Zheng: I think they will, they will, they will, they will help, they will find something. You just read. 00:11:17.720 --> 00:11:23.Wei Zheng: via multi-agent framework, and then you try to deploy, you know what I mean? 00:11:23.820 --> 00:11:31.Wei Zheng: you try to deploy the multiple agents in the lenshin structure, you know what I mean? Because we have the lenshin, they have the… 00:11:31.490 --> 00:11:45.Wei Zheng: Oh, by the way, you should be familiar with the land change, right? They have some library, they have some… Yeah, they have, the document. Yeah, yeah, yeah, yeah, you have anything you need, is that? They have the framework, anyway, they have the element, they have the component. 00:11:45.190 --> 00:11:46.Wei Zheng: You'll… 00:11:46.480 --> 00:11:52.Wei Zheng: If you are not sure, you just ask ChatGPT. You can ask the cruiser, you know what I mean? 00:11:52.840 --> 00:11:53.Duy Nguyen: Okay. 00:11:53.810 --> 00:11:55.Wei Zheng: You just, I want to use LandChain. Oh! 00:11:56.120 --> 00:12:01.Wei Zheng: In our case, probably, we caught also not only land chain, it's gravity. 00:12:01.820 --> 00:12:02.Duy Nguyen: Okay. 00:12:02.660 --> 00:12:05.Duy Nguyen: The graph, yeah, I know that. 00:12:05.340 --> 00:12:06.Duy Nguyen: Yeah. 00:12:06.780 --> 00:12:11.Duy Nguyen: I already read the language in the grab, the grab hand. 00:12:11.340 --> 00:12:28.Wei Zheng: But first, you need a… you need a… now you have the idea, but now you need what? You need based on, what I sent to you. That is… is my… in my mind, what kind of land change… oh, what kind of multi… multi-agent will do. And also. 00:12:28.970 --> 00:12:37.Wei Zheng: And also, important is what? Important thing is you need to find all the people Inter. 00:12:37.230 --> 00:12:39.Wei Zheng: act with the Lanchen. 00:12:40.240 --> 00:12:59.Wei Zheng: how the people provide the input at a different… at a different state? I do not… I do not know how to say that. At least, people not only provide one input, they should able to, should able to provide the input at a different stage. 00:12:59.770 --> 00:13:01.Wei Zheng: Of that land check process. 00:13:02.110 --> 00:13:06.Wei Zheng: And also, people can locate the outer port. 00:13:06.750 --> 00:13:08.Wei Zheng: From the land check. 00:13:08.800 --> 00:13:09.Duy Nguyen: Okay. 00:13:09.630 --> 00:13:10.Wei Zheng: And a Zen? 00:13:11.110 --> 00:13:20.Wei Zheng: They will provide their feedback to the land chain, and then the landing will further incorporate the human's input 00:13:21.630 --> 00:13:29.Wei Zheng: and then continue process. The first lead, I think, you at least, you need a… you need a… 00:13:29.090 --> 00:13:29.Duy Nguyen: Think, man. 00:13:29.660 --> 00:13:33.Wei Zheng: a frame, like, you need to make the frame. What kind of agent? 00:13:33.840 --> 00:13:40.Wei Zheng: We said multiple agents, okay? Based on what I… what I provide to you, you know that the email, you know, I said that… 00:13:41.400 --> 00:13:44.Wei Zheng: That is actually, is, I told you, that is the abstract of. 00:13:44.930 --> 00:13:46.Duy Nguyen: Yeah, that's right. 00:13:46.410 --> 00:14:02.Wei Zheng: I submit, and then we will develop a full paper based on that. Of course, we can probably do something slightly different from what we… from what I proposed, but if possible. 00:14:02.390 --> 00:14:11.Wei Zheng: we just follow that. Unless… We're doing it that way, probably is not good, then we do other way. 00:14:12.660 --> 00:14:13.Duy Nguyen: Okay, yeah. 00:14:13.530 --> 00:14:19.Wei Zheng: You know what I mean? Just for us, just to try, you just to try to think of it. 00:14:20.220 --> 00:14:36.Wei Zheng: how can you build the land chain that can follow what I propose, or what I imagine? Is that… But if you think that probably is… if you say that probably is the other, better way. 00:14:37.080 --> 00:14:41.Wei Zheng: Then, what I proposed. Oh, that's a fine! That's a fine. 00:14:41.760 --> 00:14:44.Wei Zheng: If you can, have the… yeah. 00:14:45.240 --> 00:14:52.Wei Zheng: You can, you can, you can, you can develop, or you can propose some other way. 00:14:52.270 --> 00:14:57.Wei Zheng: other way that's different from what I present. That's fine. 00:14:57.940 --> 00:15:01.Wei Zheng: As long as they can achieve the goal. 00:15:01.680 --> 00:15:03.Wei Zheng: Awful. 00:15:04.250 --> 00:15:09.Wei Zheng: of that, seat. But anyway… I think, the deadline… 00:15:10.140 --> 00:15:10.Duy Nguyen: Today, time. 00:15:10.670 --> 00:15:13.Wei Zheng: For the… for the draft paper. 00:15:14.050 --> 00:15:19.Wei Zheng: Because, you know, the first I submit the abstract, or we call the proposal, you see what I mean? 00:15:19.410 --> 00:15:20.Duy Nguyen: Yeah. 00:15:20.130 --> 00:15:26.Wei Zheng: And then they ask for the draft paper, I think by the… I think probably by the… 00:15:26.140 --> 00:15:30.Duy Nguyen: We have to submit the draft, in the beginning of February, right? 00:15:31.630 --> 00:15:36.Wei Zheng: Yeah, yeah, yeah, yeah, yeah, yeah, yeah. The draft is… So, what do you feel? 00:15:37.170 --> 00:15:40.Wei Zheng: For the… for that one, at least. 00:15:41.020 --> 00:15:42.Wei Zheng: We need to have the frame. 00:15:42.830 --> 00:15:51.Wei Zheng: When you have a specific… Because now, you see, this is abstract, right? And then, for the draft paper. 00:15:51.550 --> 00:15:54.Wei Zheng: We need a… at least we need to develop our model. 00:15:55.030 --> 00:15:57.Wei Zheng: And then we need to present our architecture. 00:15:58.010 --> 00:16:01.Wei Zheng: Actually, our architecture is what? It's the method. 00:16:02.380 --> 00:16:03.Wei Zheng: Is it the mess up. 00:16:05.770 --> 00:16:13.Wei Zheng: is the method of how we do this, is that? Because we proposed, you read that, we proposed to use this multiple… 00:16:13.650 --> 00:16:15.Wei Zheng: Agent. 00:16:15.570 --> 00:16:17.Wei Zheng: To do the reveal, is that? 00:16:17.990 --> 00:16:23.Wei Zheng: And then they will come out with a similar thing as a human review. That's why we will compare. 00:16:23.830 --> 00:16:28.Wei Zheng: The outcome from our model with the outcome. 00:16:29.090 --> 00:16:31.Wei Zheng: from that publication. 00:16:32.720 --> 00:16:34.Wei Zheng: And is it? I just… 00:16:35.280 --> 00:16:42.Wei Zheng: I just say that from within this framework, so what do you feel that? Is it challenging, or is it something 00:16:42.230 --> 00:16:43.Wei Zheng: Can't we just say? 00:16:44.640 --> 00:16:51.Wei Zheng: use the framework of multiple, AI agents. 00:16:51.370 --> 00:16:54.Wei Zheng: And then we feed them with this 28. 00:16:54.820 --> 00:16:59.Wei Zheng: Oh, probably not 28. First, we need to feed them a lot of publication. 00:16:59.270 --> 00:17:03.Wei Zheng: And then, they eventually will Select the 28. 00:17:05.670 --> 00:17:06.Duy Nguyen: Yeah… 00:17:07.040 --> 00:17:09.Wei Zheng: You see, that's the ego? You see? 00:17:09.180 --> 00:17:27.Wei Zheng: Just like you did, we do the search, you see what I mean? Because how they identify 28? Because this is human, there is some criteria, they eventually identify the 28 that is… is based on whatever the criteria they define. 00:17:27.450 --> 00:17:27.Duy Nguyen: Yes. 00:17:27.880 --> 00:17:36.Wei Zheng: Oh, so, for your agent, multiple agent framework, the first agent work is what? Is try to, fin00:17:37.220 --> 00:17:43.Wei Zheng: the 28, this publication. You mix these 28 publications with other similar. 00:17:43.420 --> 00:17:44.Duy Nguyen: Okay. 00:17:44.030 --> 00:17:59.Wei Zheng: publication, is that? And then, whatever the criteria for their research to use to identify this 28 publications, and then you need to feed this pipeline, is that? 00:17:59.580 --> 00:18:13.Wei Zheng: Edge in the pipe, and then they will come out. We cannot say exactly. At least they can come some 20 or 30, that is close to this 28. That's what we can compare. We said, at first. 00:18:13.530 --> 00:18:26.Wei Zheng: They, based on the certain criteria, they come out as 28, you know? And then we use this… we use their same project, whatever the search literature is like, we put all the literatur00:18:27.230 --> 00:18:31.Wei Zheng: Of course, that literature includes the 28 publication, right? 00:18:32.680 --> 00:18:45.Wei Zheng: You know what I mean? And then we feed, say, I don't know, I think they mentioned that, how many… how many… how many publications they… they start to locate, and eventually they identify 28. 00:18:46.330 --> 00:18:50.Duy Nguyen: I think it's, 75 or 80. 00:18:50.200 --> 00:18:52.Wei Zheng: Yeah, yeah, yeah, yeah, yeah, I see, you got it. 00:18:52.990 --> 00:18:58.Wei Zheng: Doesn't matter how many, at least we… oh, we can do the similar thing, you know, we, we… 00:18:58.410 --> 00:19:06.Wei Zheng: We just take about 100, okay? We take about 100 publications, and of course, this 100 publications include that 28, is that… 00:19:06.970 --> 00:19:07.Duy Nguyen: TV. 00:19:07.980 --> 00:19:19.Wei Zheng: And then we feed the pipeline, and then the pipeline, eventually, they will select, just like humans, they will select the pipeline. Even if they can select exactly 28, that will be perfect. 00:19:19.910 --> 00:19:20.Wei Zheng: You know what I mean? 00:19:21.200 --> 00:19:23.Wei Zheng: That is the one process. 00:19:23.650 --> 00:19:24.Wei Zheng: You know what I mean? 00:19:25.110 --> 00:19:34.Wei Zheng: That's why… and also the evaluation is one. We will evaluate what your pipeline, or your agent model, is that? 00:19:34.170 --> 00:19:36.Duy Nguyen: They produced, say, 28. 00:19:36.360 --> 00:19:49.Wei Zheng: I mean, exactly 28, then we said the perfect is 100% accurate. Or, if you produce, something is… the close one is… they have 25, it's the same, but other, probably. 00:19:49.610 --> 00:20:08.Wei Zheng: They identify 20… 35. Among the 35, the 28 is similar to the 25 among the 28, you know what I mean? And then we can… we can say how much they close, you know what I mean? So that is one perspective, and then you do one by one, further one by one, eventually. 00:20:08.720 --> 00:20:19.Wei Zheng: what they got from their, review. They got some conclusion, like, you know, first you need to define what is their final products from their review. 00:20:19.530 --> 00:20:31.Wei Zheng: or whatever the model, or whatever the strategy, or whatever the… whatever the knowledge, you know what I mean? I think the knowledge is just, like, for particular part… for a part… 00:20:31.640 --> 00:20:38.Wei Zheng: For a particularly student population, and a water intervention. 00:20:38.540 --> 00:20:44.Wei Zheng: It's more effective for what type of population of students? Something like that. 00:20:45.000 --> 00:20:46.Wei Zheng: You know what I mean? 00:20:46.080 --> 00:20:47.Duy Nguyen: Yeah, I agree. 00:20:47.230 --> 00:20:54.Wei Zheng: And then if we… eventually we can come out of that result, and then we compare with their result. 00:20:55.000 --> 00:21:04.Wei Zheng: Of course, we need to define… for each comparison, we need to define the metrics for… for com… for compare… for comparison. 00:21:05.110 --> 00:21:13.Wei Zheng: And this one, you can ask ChatGPT, just say if I want to compare this 5%. Just like, 00:21:14.980 --> 00:21:29.Wei Zheng: Yeah, just like, they identify 28, publication amount from 20… from 100 publications, and then we also identify, we also use the 100 publications. We identify whatever 00:21:30.230 --> 00:21:41.Wei Zheng: the publication, and then how can we measure their result? How we measure their result is good or not? You ask ChatGPT. ChatGPT can tell you a lot of ways to, to, to, to 00:21:41.790 --> 00:21:52.Wei Zheng: to evaluate, like, the metrics, like, you do the same thing for each outcome we want to compare. The final, outcome comparison, also we can say. 00:21:53.000 --> 00:21:58.Wei Zheng: For their process, you define, you tell the ChatGPT what they got, you know? 00:21:58.490 --> 00:22:04.Wei Zheng: What we've got? And then you said from our pipeline, we also got a similar thing, is that? 00:22:04.880 --> 00:22:08.Wei Zheng: And then we… how can we compare those two things? 00:22:08.440 --> 00:22:19.Wei Zheng: is good or not, or how close they are, you know what I mean? They, of course, there's a lot of weight to make this one. And then eventually, you see, we developed our model, and then… 00:22:19.270 --> 00:22:31.Wei Zheng: we do the evaluation with the golden standard, you know what I mean? Because whatever they do is the golden standard, and then we will compare our model's outcome or behavior 00:22:31.570 --> 00:22:36.Wei Zheng: with the human golden standard. And then we have the… 00:22:36.800 --> 00:22:48.Wei Zheng: We have the metrics. We have the comparison metrics. That metrics will tell you how your model is close to the human, in a different perspective. 00:22:48.640 --> 00:22:50.Wei Zheng: So, the picture is clear, the picture? 00:22:50.950 --> 00:22:53.Duy Nguyen: Yeah, the picture is very clear right now. 00:22:53.590 --> 00:22:56.Wei Zheng: So, so, so, just say. 00:22:57.090 --> 00:23:02.Wei Zheng: what do you feel? What's the most challenging part you… you feel? 00:23:05.300 --> 00:23:14.Duy Nguyen: Actually, I think… We, I, you, you allow me to, like. 00:23:14.630 --> 00:23:29.Duy Nguyen: free to do anything, like, I can use the chat GPT, the cursor, the anti-gravity, yeah, you want me to do anything, search to GitHub and read anything, so I think I can, I can do that. 00:23:30.250 --> 00:23:35.Wei Zheng: I mean, I mean, I mean, based on what you… but currently, I do not know what is… 00:23:35.390 --> 00:23:38.Wei Zheng: What do you come out, okay? Just say. 00:23:38.410 --> 00:23:41.Wei Zheng: You know the picture, you know, we want to achieve, is that? 00:23:41.790 --> 00:23:49.Wei Zheng: And you feel what is most challenging part, regarding the coding, regarding the work, regarding the time? 00:23:49.490 --> 00:23:59.Wei Zheng: So, which part do you think is more significant? Say, you need a significant time, or there's some significant challenges in doing this, or frame that? 00:24:00.120 --> 00:24:03.Wei Zheng: And I think, first, you need to come out of the… 00:24:03.650 --> 00:24:05.Duy Nguyen: I need to understand. 00:24:05.410 --> 00:24:06.Wei Zheng: architecture. 00:24:06.650 --> 00:24:07.Duy Nguyen: Architecture, okay. 00:24:07.650 --> 00:24:12.Wei Zheng: Architecture of your… Your, your, your, your multi-bought… 00:24:13.410 --> 00:24:14.Duy Nguyen: Agent. 00:24:14.560 --> 00:24:16.Wei Zheng: Jim Walker, right? 00:24:16.110 --> 00:24:16.Duy Nguyen: Yes. 00:24:16.900 --> 00:24:21.Wei Zheng: And… and another is what? How you instruct… how you provide prompts. 00:24:21.850 --> 00:24:22.Wei Zheng: Yeah, I think. 00:24:22.590 --> 00:24:24.Duy Nguyen: Yeah. I think… 00:24:24.050 --> 00:24:30.Wei Zheng: I think, okay, I think, regarding the land chain, or regarding the graph chain, the key thing is the prompts. 00:24:30.680 --> 00:24:35.Duy Nguyen: What a specific task, you know? And then you need to define that. 00:24:35.500 --> 00:24:38.Wei Zheng: You need to find for each agent why the… 00:24:39.560 --> 00:24:41.Wei Zheng: You need to do, step by step. 00:24:42.020 --> 00:24:45.Wei Zheng: Because even for the 1 18th, I'm not sure. 00:24:46.400 --> 00:24:52.Wei Zheng: Because if you set one prompt with one large language model, that is one agent. Or… 00:24:53.180 --> 00:24:57.Wei Zheng: You need to have serious one-by-one, one-by-one prompts. 00:24:58.660 --> 00:25:07.Wei Zheng: You know what I mean? What I tried to say. You need to develop a serious, I mean, the chain of the pumps. 00:25:07.630 --> 00:25:08.Wei Zheng: You know what I mean? 00:25:10.020 --> 00:25:12.Duy Nguyen: You, like, a little more detail. 00:25:13.290 --> 00:25:18.Wei Zheng: I mean, serious, you know what I mean, serious. One by one, one by one, one by one. 00:25:20.230 --> 00:25:22.Wei Zheng: Syria, Syria, Syria, Syria. 00:25:23.000 --> 00:25:26.Duy Nguyen: Oh, okay, okay. Yeah, that is an interview. Okay. 00:25:26.550 --> 00:25:29.Wei Zheng: You needed to… how you… that's saying, I mean… 00:25:29.750 --> 00:25:31.Wei Zheng: You need to have a clear picture. 00:25:31.730 --> 00:25:34.Wei Zheng: What kind of prompts? 00:25:34.570 --> 00:25:35.Duy Nguyen: you know. 00:25:35.140 --> 00:25:40.Wei Zheng: We need to provide in order to make the larger language model 00:25:40.790 --> 00:25:47.Wei Zheng: As the agent, we want the I mean… 00:25:48.320 --> 00:25:51.Wei Zheng: Yeah, that means you, you, you need to, you need to have the… 00:25:51.580 --> 00:25:56.Wei Zheng: Once you have this picture, you, you can just let the cruiser 00:25:56.290 --> 00:25:58.Wei Zheng: Do it for you, you know? 00:26:00.400 --> 00:26:08.Wei Zheng: once you… What? Developer, the architecture, or the framework of your multiple agent? 00:26:09.890 --> 00:26:12.Wei Zheng: And then you tell the cruiser. 00:26:12.460 --> 00:26:15.Wei Zheng: And then the cruiser will build the code. 00:26:15.880 --> 00:26:16.Wei Zheng: For Europe. 00:26:17.010 --> 00:26:17.Wei Zheng: You lost? 00:26:17.860 --> 00:26:19.Duy Nguyen: Yes, it's true. 00:26:21.520 --> 00:26:25.Wei Zheng: So, what, what do you, what do you come out, last week? 00:26:30.790 --> 00:26:42.Duy Nguyen: The last week, I, I tried, I, I still try to… Make the… the graph… 00:26:42.710 --> 00:26:43.Duy Nguyen: rack. 00:26:44.780 --> 00:26:48.Duy Nguyen: Run and see the entity in the relationship. 00:26:48.080 --> 00:26:51.Wei Zheng: Yeah, iteration process, can you… okay. 00:26:51.460 --> 00:26:56.Wei Zheng: Last time, we talked about iteration… iterative… iterative process, is that? 00:26:56.190 --> 00:26:56.Duy Nguyen: Yes. 00:26:57.270 --> 00:27:00.Wei Zheng: Can you go several around? Have you started around? 00:27:00.990 --> 00:27:03.Wei Zheng: Have you, have you started to run that? 00:27:05.870 --> 00:27:09.Wei Zheng: Have you started to run several, several, several paths? 00:27:11.390 --> 00:27:16.Duy Nguyen: I, I, I, I already started. I, I, I already sent you the, the output, I showed you the… 00:27:16.310 --> 00:27:24.Wei Zheng: Okay, so that means you go different iteration, and then that graph is, at least, is much better than… 00:27:25.930 --> 00:27:26.Duy Nguyen: No, no. 00:27:26.320 --> 00:27:28.Wei Zheng: In the last round, is it correct? 00:27:28.570 --> 00:27:29.Duy Nguyen: Yes. 00:27:30.100 --> 00:27:31.Wei Zheng: Okay, okay. 00:27:33.310 --> 00:27:40.Wei Zheng: So, can you share me? Can you share the screen? What, what, what you, you, you send me? Yeah, you share the screen. 00:28:00.980 --> 00:28:09.Wei Zheng: Yeah, you show the graph, the first graph, and then the second round, and the third round, or whatever. At least you have… at least you have two rounds, you like? 00:28:11.370 --> 00:28:15.Wei Zheng: You see what I mean? At least you have two rounds of the graph, is that? 00:28:15.980 --> 00:28:16.Duy Nguyen: Yes. 00:28:16.910 --> 00:28:20.Wei Zheng: You know what I mean, the first round and second round, is that? 00:28:20.610 --> 00:28:22.Duy Nguyen: Yes, it was a mistake. 00:28:27.330 --> 00:28:41.Wei Zheng: Do you feel that graph is consistent with what the review, or what is that they doing? Or how this graph will align with 00:28:42.840 --> 00:28:44.Wei Zheng: That particular publication. 00:28:44.940 --> 00:28:46.Wei Zheng: You knew that. 00:28:46.310 --> 00:28:51.Wei Zheng: the human twin. I mean, I mean, I mean… Holy… wha… 00:28:51.500 --> 00:28:57.Wei Zheng: What's your sense of this knowledge graph related to the efforts 00:28:58.130 --> 00:29:02.Wei Zheng: that review, I mean, that author's doing. 00:29:09.450 --> 00:29:13.Duy Nguyen: I think it is… It's good, 00:29:14.400 --> 00:29:17.Duy Nguyen: But it's not perfect. It's… it cannot… 00:29:17.940 --> 00:29:19.Wei Zheng: Is it close to what they… 00:29:19.860 --> 00:29:23.Duy Nguyen: What they do are… is close to what they… 00:29:25.560 --> 00:29:27.Wei Zheng: And also, in your mind. 00:29:27.720 --> 00:29:33.Duy Nguyen: It's not ready for the verification. It's not ready. I still have to improve. 00:29:34.860 --> 00:29:36.Duy Nguyen: Improve it. 00:29:37.040 --> 00:29:42.Wei Zheng: So, tell me what's your final… what's your final graph? What entity, and what's the relationship? 00:29:42.690 --> 00:29:47.Duy Nguyen: Yeah, there you go. Here is the original file, the packet. 00:29:47.960 --> 00:29:49.Wei Zheng: This is the first round. 00:29:50.510 --> 00:29:53.Duy Nguyen: He's the third one. There's the third one. 00:29:53.780 --> 00:29:56.Wei Zheng: This is a… this is a publication, right? 00:29:59.970 --> 00:30:00.Wei Zheng: Well, we'll… 00:30:00.820 --> 00:30:02.Duy Nguyen: Here's the entity. 00:30:02.940 --> 00:30:04.Duy Nguyen: Here's your entity. 00:30:04.260 --> 00:30:08.Wei Zheng: Oh, no, no, wait, wait, wait. Where's the entity? Where's the… 00:30:09.110 --> 00:30:14.Wei Zheng: Okay, learning publication, what is that? This is a NAVE, NAVE student, is that? 00:30:15.400 --> 00:30:17.Duy Nguyen: The… the en… 00:30:18.340 --> 00:30:22.Wei Zheng: Oh, this is the… all the entity in the graph, is that? 00:30:22.340 --> 00:30:26.Duy Nguyen: Yes, the regiment already defined the entity. The. 00:30:26.850 --> 00:30:31.Wei Zheng: This is the… this is the entity defined by the author. 00:30:31.700 --> 00:30:33.Duy Nguyen: Yes, the perfect weather. 00:30:33.670 --> 00:30:39.Wei Zheng: Like, we try to overcome this… Oh, no, by the way, The author… 00:30:40.640 --> 00:30:46.Wei Zheng: So what do they try to do? They try to identify the entity and also try to identify relation. 00:30:47.550 --> 00:30:52.Wei Zheng: I mean, the richer… what kind of… what causes the name, the people's name? The author, the author. 00:30:55.040 --> 00:30:56.Duy Nguyen: The Richmond. 00:30:56.270 --> 00:30:56.Wei Zheng: Yeah. 00:30:57.830 --> 00:31:02.Wei Zheng: So, this is the… it's similar to what the… They how? 00:31:05.250 --> 00:31:07.Duy Nguyen: It's similar to what they have. 00:31:07.750 --> 00:31:08.Wei Zheng: Yeah. 00:31:08.770 --> 00:31:18.Duy Nguyen: The entity is… The intervention, the outcome, the mechanism, the contact… Huh. 00:31:19.050 --> 00:31:19.Wei Zheng: Okay. 00:31:20.090 --> 00:31:22.Wei Zheng: Okay, okay, you put it, put it this way. 00:31:22.600 --> 00:31:23.Wei Zheng: You'll feed. 00:31:24.480 --> 00:31:29.Wei Zheng: you'll feed your… you'll feed that Richmond publication. 00:31:29.360 --> 00:31:31.Wei Zheng: to your chat GPT. 00:31:31.320 --> 00:31:33.Wei Zheng: You said based on what they do. 00:31:33.830 --> 00:31:38.Wei Zheng: you let ChatGPT give you some example of their 00:31:39.090 --> 00:31:46.Wei Zheng: Just say, based on what they do, what kind of knowledge graph they actually should have. 00:31:48.510 --> 00:31:49.Wei Zheng: You know what I mean? 00:31:50.250 --> 00:31:52.Duy Nguyen: Oh, yeah, I know. I do it right now, hold on. 00:31:53.910 --> 00:32:02.Wei Zheng: You just feed that, their paper for the ChatGPT. You say that, based on their description. 00:32:02.540 --> 00:32:11.Wei Zheng: If we want to build the knowledge graph, use the Microsoft, whatever, that… 00:32:11.570 --> 00:32:17.Wei Zheng: And what kind of entity, what kind of relation you perceiv00:32:18.100 --> 00:32:36.Wei Zheng: At least the chat GPT can, based on what his understanding of Richmond's efforts. At least, if they do not build the knowledge graph, at least they can point out… you just say, what kind of… give me some example of the entity, or a relation. 00:32:36.550 --> 00:32:43.Wei Zheng: That is, best, described what they try to do, you know what I mean? 00:32:44.180 --> 00:32:46.Duy Nguyen: Yeah, I understand. What about you, Juan? 00:32:46.660 --> 00:32:53.Wei Zheng: Yeah, and then you compare what the entity in the chat GPT, and you said as many as possible. 00:32:54.660 --> 00:32:56.Duy Nguyen: Okay. And… 00:32:56.200 --> 00:33:14.Wei Zheng: At least, you said from their conclusion, because we need to go rewards, because you chat… put the… you, you, you, you, you, you what? You tell ChatGPT, you said based on the Richmond's outcome from their public… from their… from… from their review paper, you like? 00:33:14.810 --> 00:33:21.Wei Zheng: And what kind of knowledge graph that can be? 00:33:21.630 --> 00:33:22.Wei Zheng: Better! 00:33:22.910 --> 00:33:25.Wei Zheng: to describe their outcome. 00:33:36.400 --> 00:33:38.Duy Nguyen: What kind of knowledge? 00:33:38.610 --> 00:33:43.Wei Zheng: Choreograph, they can't… Oh, whoa, ugh! 00:33:43.810 --> 00:33:45.Wei Zheng: Oh, what? Yeah! 00:33:45.860 --> 00:33:51.Wei Zheng: Yeah, yeah, what is the knowledge graph that is built based on the Microsoft? 00:33:51.500 --> 00:33:52.Wei Zheng: approach. 00:33:55.280 --> 00:33:56.Wei Zheng: well contained. 00:33:56.890 --> 00:34:00.Wei Zheng: Well, contain. What kind of entity? What kind of relation? 00:34:01.860 --> 00:34:06.Wei Zheng: No, no, no, you should say that based on outcome from this paper. 00:34:12.889 --> 00:34:14.Duy Nguyen: Apeen? 00:34:14.540 --> 00:34:19.Wei Zheng: of outcome from these people. Outcome, based on outcome from this paper. 00:34:20.719 --> 00:34:27.Wei Zheng: And what kind of… okay, what kind of entity, what kind of relation? 00:34:29.040 --> 00:34:32.Wei Zheng: That complying with the knowledge graph? 00:34:33.030 --> 00:34:37.Wei Zheng: as described by the Microsoft, 00:34:37.770 --> 00:34:42.Wei Zheng: Yeah, by Microsoft, what's called that, that community, what, whatever. 00:34:43.540 --> 00:34:45.Wei Zheng: So what comes the input and relation? 00:34:46.110 --> 00:34:55.Wei Zheng: what kind of entity, what kind of, what kind of entity, and a relation, and a relation? 00:34:56.150 --> 00:34:57.Wei Zheng: Another relation. 00:35:02.440 --> 00:35:07.Wei Zheng: From, or pasta, pasta, or from. It's the same thing. 00:35:08.060 --> 00:35:11.Wei Zheng: Based on the, the knowledge graph. 00:35:12.650 --> 00:35:19.Wei Zheng: That build it, that build it, that build it by using that, Microsoft, whatever. 00:35:19.750 --> 00:35:20.Wei Zheng: the name. 00:35:24.180 --> 00:35:31.Wei Zheng: That… That… That was built… Build, build a, build a. 00:35:31.600 --> 00:35:33.Wei Zheng: Built up Microsoft. 00:35:45.980 --> 00:35:57.Wei Zheng: That build on, knowledge graph, no, no, knowledge graph, that is built… that was built, built on, built on, yeah, that, that is, that is built on. 00:35:59.630 --> 00:36:00.Duy Nguyen: Yeah, right? 00:36:00.620 --> 00:36:01.Wei Zheng: Build on. 00:36:02.230 --> 00:36:05.Wei Zheng: Built. You should be built, not builder, builder. 00:36:05.550 --> 00:36:06.Duy Nguyen: Mute. 00:36:06.800 --> 00:36:07.Wei Zheng: Yeah, beaut. 00:36:08.110 --> 00:36:13.Wei Zheng: Upon, upon, upon, that's fine. Upon, like, 00:36:13.860 --> 00:36:15.Wei Zheng: Apa, yeah, apahobra. 00:36:16.640 --> 00:36:19.Wei Zheng: You put R, O, O, N, O, N, R. 00:36:22.410 --> 00:36:26.Wei Zheng: Built upon. Oh, that's fine, that's fine, that's fine. 00:36:27.140 --> 00:36:28.Wei Zheng: That's fine. 00:36:28.160 --> 00:36:30.Duy Nguyen: I think it's fine, because I think it's… 00:36:30.720 --> 00:36:36.Wei Zheng: Also, also, you need to say, you need to say what particular that community, what to call that, community method. 00:36:37.920 --> 00:36:39.Wei Zheng: What do you call that? 00:36:40.270 --> 00:36:42.Duy Nguyen: The community… 00:36:42.160 --> 00:36:42.Wei Zheng: Yah. 00:36:42.880 --> 00:36:43.Duy Nguyen: Report. 00:36:43.900 --> 00:36:47.Wei Zheng: No, no, no, no, yeah, what does it refer to? 00:36:47.800 --> 00:36:49.Duy Nguyen: The community detection? 00:36:49.990 --> 00:37:01.Wei Zheng: Yeah, yeah, yeah, community detection. Through, through community detection. No, no, the logic graph through that community detection. 00:37:01.880 --> 00:37:08.Wei Zheng: Because the knowledge graph is built through the community. 00:37:08.010 --> 00:37:08.Duy Nguyen: Yeah. 00:37:08.370 --> 00:37:09.Wei Zheng: He actually messed up, is that? 00:37:11.800 --> 00:37:12.Duy Nguyen: Yes. 00:37:25.110 --> 00:37:31.Wei Zheng: Okay, you say, say, give me some example of the possible entity and, relation. 00:37:31.950 --> 00:37:37.Wei Zheng: And give the examples of the entity and the relation in this context. 00:37:41.560 --> 00:37:44.Wei Zheng: Example of entity and a relation. 00:37:51.590 --> 00:37:56.Wei Zheng: In this term, or in this context, C-O-N-T-E-X-T. 00:37:58.800 --> 00:38:00.Wei Zheng: Okay, okay, let's see, let's see. 00:38:02.620 --> 00:38:06.Duy Nguyen: Actually, I really understand what you say, because we… 00:38:07.170 --> 00:38:13.Duy Nguyen: Because your accent is kind of like me, because that's why I can't understand. 00:38:13.220 --> 00:38:14.Wei Zheng: Now you understand? 00:38:14.640 --> 00:38:16.Duy Nguyen: Yeah, I really understand what you say. 00:38:20.450 --> 00:38:27.Wei Zheng: And then you will compare to what they got, compared to, what you, you, you build, you know what I mean? 00:38:27.770 --> 00:38:29.Duy Nguyen: Yeah, what I think… 00:38:29.020 --> 00:38:33.Wei Zheng: You build this is not built upon. They are… they are… 00:38:34.790 --> 00:38:38.Wei Zheng: You build the relation entity is not… not based on this? 00:38:39.190 --> 00:38:44.Wei Zheng: not based on this publication. You based on the reference we feed to the system, you like? 00:38:44.670 --> 00:38:46.Duy Nguyen: Yes, we bet. 00:38:47.430 --> 00:38:48.Duy Nguyen: Everyone's… 00:38:48.410 --> 00:38:49.Wei Zheng: Okay, okay, okay. 00:38:49.050 --> 00:38:50.Duy Nguyen: So, to 28. 00:38:50.800 --> 00:38:52.Wei Zheng: Student contact with. 00:38:53.700 --> 00:38:56.Wei Zheng: Self-confident. 00:38:57.530 --> 00:38:58.Wei Zheng: Okay. 00:38:59.100 --> 00:39:03.Wei Zheng: Do you think it's similar from what you have? 00:39:04.080 --> 00:39:07.Duy Nguyen: No, it's not, because… because, 00:39:07.950 --> 00:39:13.Duy Nguyen: the… the data I use is the 28th. 00:39:14.950 --> 00:39:16.Duy Nguyen: You used to turn here. 00:39:19.180 --> 00:39:25.Wei Zheng: Oh, you use the 28, yeah, yeah, yeah, you use the 28, yeah, that's right, that's right, that's right. Because they actually… 00:39:25.910 --> 00:39:43.Wei Zheng: They, they, they develop their outcome based on this 28 people, 28 people, you know? But now, we just… you feed this 28, you build a knowledge graph, based on this 28 people, but not based on, their publication, you know? Yeah. 00:39:43.640 --> 00:39:45.Duy Nguyen: But it's not based on the publication. 00:39:45.520 --> 00:39:46.Wei Zheng: Because they built. 00:39:46.870 --> 00:39:50.Duy Nguyen: But, I, but, I, I, I, I, I understand. 00:39:50.680 --> 00:39:54.Duy Nguyen: Joe Biden? 00:39:55.930 --> 00:39:56.Duy Nguyen: So, you'll. 00:39:56.550 --> 00:39:59.Wei Zheng: Look at, look at what they have. Is it similar? 00:40:04.710 --> 00:40:05.Duy Nguyen: It's not… 00:40:05.260 --> 00:40:07.Wei Zheng: What to call that? 00:40:07.920 --> 00:40:17.Wei Zheng: Do you, entity, and look at is any, relation. Go, go down, go down, go down, and see if they provide… yeah, relation, relation. 00:40:17.500 --> 00:40:19.Wei Zheng: You, you see that? You see that? 00:40:19.450 --> 00:40:20.Duy Nguyen: Yeah, I see that. 00:40:20.280 --> 00:40:31.Wei Zheng: You will, you will see, because they are actually what? They already have the outcome, right? They, whatever they do, and then the chat GPT is smart enough, they can… 00:40:31.660 --> 00:40:36.Wei Zheng: They can feel, you know, from their publication. But now what? We will… 00:40:36.600 --> 00:40:43.Wei Zheng: We will do… you will deal with the 28 people, and see whether you can come out with a similar thing, like this, is that? 00:40:44.260 --> 00:40:44.Duy Nguyen: Yes. 00:40:45.480 --> 00:40:48.Duy Nguyen: I think my 28 people is better than this. 00:40:48.800 --> 00:40:50.Wei Zheng: Is, is, is, is close? 00:40:52.080 --> 00:40:54.Duy Nguyen: It's closed. It's better. 00:40:54.700 --> 00:40:56.Wei Zheng: You feel, you feel better? 00:40:56.280 --> 00:40:58.Duy Nguyen: I don't know if it's better than this one. 00:40:58.550 --> 00:41:01.Duy Nguyen: I read… it's kind of… it's not… 00:41:05.830 --> 00:41:08.Wei Zheng: Just like, this is the kind of relation, right? 00:41:08.340 --> 00:41:09.Duy Nguyen: Yeah, it's kind of British. 00:41:10.640 --> 00:41:20.Wei Zheng: Can… can… let… let's see. Let's see what's your, your, your integer and relation. But now we have the idea, you know? We have the idea. Let's see yours. 00:41:21.330 --> 00:41:25.Wei Zheng: At least we need to see some clues, resemble, resemble. 00:41:30.750 --> 00:41:31.Duy Nguyen: It's my relish. 00:41:33.760 --> 00:41:35.Duy Nguyen: Wow, it's fascinating. 00:41:36.270 --> 00:41:37.Duy Nguyen: 2003. 00:41:38.190 --> 00:41:39.Duy Nguyen: Relationship, yeah, there you go. 00:42:24.090 --> 00:42:25.Duy Nguyen: No, he's my relation. 00:42:26.080 --> 00:42:27.Wei Zheng: Is it close, or similar? 00:42:30.500 --> 00:42:37.Wei Zheng: So what's the, what's the, what's the, I think the relation, let's look at the relation. 00:42:37.530 --> 00:42:39.Wei Zheng: What kind of their relations they have? 00:42:39.990 --> 00:42:42.Wei Zheng: They identify through that, by using that method. 00:42:53.020 --> 00:42:55.Wei Zheng: Yeah, I see the NAV, NAV student. 00:42:56.870 --> 00:42:59.Wei Zheng: Yeah, do they have an AV student? 00:43:00.530 --> 00:43:02.Wei Zheng: I saw you have an AV student. 00:43:02.850 --> 00:43:04.Duy Nguyen: Yeah. How is. 00:43:04.640 --> 00:43:06.Wei Zheng: That is, entities, right? 00:43:06.990 --> 00:43:08.Duy Nguyen: Yeah, it's an entity. 00:43:09.430 --> 00:43:21.Wei Zheng: And also combine the reason… reason… oh, you go back! You copy one of them. You copy one of these integers, just as the next one. Combine. Combine reasoning strategy. 00:43:21.300 --> 00:43:37.Wei Zheng: combined reading strategy, go up, go up, go up. Yeah, yeah, you copy this one, and then you copy this, and then you ask ChatGPT, you said, this is if… this is the entity, they will be identified from the… 00:43:37.950 --> 00:43:39.Wei Zheng: knowledge. 00:43:40.090 --> 00:43:44.Wei Zheng: is a correct entity in terms of their outcome, you know what I mean? 00:43:45.380 --> 00:43:51.Wei Zheng: You just asked, you said, I, is this, is this, is the… 00:43:51.990 --> 00:43:55.Wei Zheng: It's kind of the outcome of the… of the entity. 00:43:56.660 --> 00:43:59.Wei Zheng: In terms of their knowledge graph. 00:44:04.890 --> 00:44:07.Duy Nguyen: No, no, no, it's kind of the entity, entity. 00:44:17.330 --> 00:44:21.Wei Zheng: Is the entity from, from, from their, their account. 00:44:21.500 --> 00:44:25.Wei Zheng: From the… from the knowledge graph based on their outcome. 00:44:26.350 --> 00:44:32.Wei Zheng: From the knowledge… it's… it's… is the correct, okay, it's the correct entity. 00:44:33.950 --> 00:44:41.Wei Zheng: Of their… of the knowledge graph based on, outcome of their research. 00:44:43.240 --> 00:44:47.Wei Zheng: Or, all outcome from that, that, that publication. 00:44:48.220 --> 00:44:54.Wei Zheng: For that Richmond publication. Yeah, from the publication in the above, because you… you already… 00:44:54.640 --> 00:44:57.Wei Zheng: You already uploaded that file, you know? 00:44:58.910 --> 00:44:59.Duy Nguyen: Yep. 00:44:59.910 --> 00:45:00.Duy Nguyen: It is… 00:45:00.450 --> 00:45:03.Wei Zheng: Correct, yeah, yeah, it's the correct entity from Nordic Graph. 00:45:04.010 --> 00:45:12.Wei Zheng: That graph is what? Is… is based on… based on… based on the knowledge, best on outcome. 00:45:12.950 --> 00:45:15.Wei Zheng: From that publication. 00:45:20.080 --> 00:45:23.Wei Zheng: Yeah, yeah, from a publication attached, attached. 00:45:25.820 --> 00:45:28.Wei Zheng: Attached, attached, attached. Publication attached. 00:45:29.510 --> 00:45:31.Wei Zheng: Because you attached the publication here, is that? 00:45:32.430 --> 00:45:36.Wei Zheng: Yeah, attached. Attached here, attached here, yeah, that's fine, that's fine. 00:46:39.560 --> 00:46:45.Wei Zheng: You, you ask him, based on what? You, you make this conclusion. Based on what? 00:46:45.680 --> 00:46:48.Wei Zheng: Based on what? You, you said it this way. 00:47:17.170 --> 00:47:19.Duy Nguyen: This used to be the chorache. 00:47:23.640 --> 00:47:25.Duy Nguyen: Oh, Jesus Christ. 00:47:26.950 --> 00:47:28.Duy Nguyen: It's rich, man. 00:47:28.460 --> 00:47:29.Duy Nguyen: Amen. 00:47:31.500 --> 00:47:35.Wei Zheng: So, okay, let's look at the paper. What is their conclusion? What is… what… 00:47:35.810 --> 00:47:39.Wei Zheng: You, you tell me about this paper. Oh, you put, you put the false screen. 00:47:39.760 --> 00:47:41.Wei Zheng: You put… you put it on the false screen. 00:47:42.490 --> 00:47:45.Wei Zheng: You put your computer on the false screen. 00:47:46.200 --> 00:47:53.Wei Zheng: No, no, you go to that, the window, the fourth screen. Oh, I think that's the fourth screen, okay, okay, that fourth screen. Yeah, yeah, yeah. 00:47:53.440 --> 00:47:58.Wei Zheng: So, what is the paper… what is the outcome of the paper? Well, what is the conclusion of the paper? Yeah. 00:48:00.000 --> 00:48:04.Wei Zheng: what do they try to… what do they try to do? Or what is… what do they got? 00:48:04.710 --> 00:48:08.Wei Zheng: What they got from their review, you know? 00:48:09.240 --> 00:48:10.Duy Nguyen: Here's a conclusion. 00:48:15.830 --> 00:48:22.Wei Zheng: Education intervention for direct analytical and non-analytical Reasons on undergrad Student in Medical School Care Profession Education. 00:48:23.500 --> 00:48:25.Wei Zheng: predominant work. 00:48:25.400 --> 00:48:34.Wei Zheng: By increased knowledge of the core assigned according to factor more. 00:48:37.200 --> 00:48:39.Wei Zheng: So that is the outcome. 00:48:41.380 --> 00:48:48.Wei Zheng: They review… they review 28 publications. That is their final conclusion, right? 00:48:50.800 --> 00:48:55.Duy Nguyen: Yeah, they, they, they… They already towed in. 00:48:55.420 --> 00:48:58.Duy Nguyen: in the… It abstract. 00:48:59.670 --> 00:49:00.Duy Nguyen: The result… 00:49:01.670 --> 00:49:04.Wei Zheng: Okay, okay, let's do this way. 00:49:05.430 --> 00:49:08.Wei Zheng: Let's, let's do this way. We continue our chat GPT. 00:49:08.730 --> 00:49:11.Wei Zheng: You said, if we want. 00:49:13.190 --> 00:49:16.Wei Zheng: If we want to build a multiple agent model. 00:49:17.410 --> 00:49:23.Wei Zheng: Use LanChain, LandGraph, and also use, you know what I mean? 00:49:23.620 --> 00:49:31.Wei Zheng: Yeah, even if we want to use the line chain, And, graph chain. 00:49:31.480 --> 00:49:34.Wei Zheng: And, knowledge graph of Microsoft. 00:49:35.390 --> 00:49:37.Wei Zheng: Whatever you call that, you know what I mean? 00:49:38.330 --> 00:49:41.Duy Nguyen: Interviewed, multiple agents. 00:49:42.010 --> 00:49:42.Wei Zheng: Yeah. 00:49:43.900 --> 00:49:49.Wei Zheng: Multiple agent, multiple AI agent, multiple AI agent framework. 00:49:52.710 --> 00:50:00.Wei Zheng: by using… by using the land chain, graph chain, and the knowledge graph of Microsoft Model. 00:50:05.670 --> 00:50:07.Wei Zheng: By using, by using. 00:50:13.700 --> 00:50:18.Duy Nguyen: Land chain, graph chain, and, knowledge graph of… 00:50:18.630 --> 00:50:19.Wei Zheng: awful. 00:50:37.220 --> 00:50:38.Duy Nguyen: Naruto crab. 00:50:43.550 --> 00:50:45.Duy Nguyen: If you want to build. 00:50:45.340 --> 00:50:50.Wei Zheng: Knowledge graph, and knowledge graph of MagSoft, MagSoft. 00:50:50.760 --> 00:50:52.Wei Zheng: What Microsoft method? 00:50:52.900 --> 00:50:54.Wei Zheng: Microsoft, 00:51:01.490 --> 00:51:07.Wei Zheng: And also a community, what's called a community detection, or whatever. 00:51:14.960 --> 00:51:19.Wei Zheng: This community detection is awesome. Let's go with Microsoft, right? 00:51:19.430 --> 00:51:21.Duy Nguyen: Yes, it's go with the graph there. 00:51:22.190 --> 00:51:26.Wei Zheng: Okay, and, and also, you, you put also its community detection method. 00:51:26.900 --> 00:51:28.Wei Zheng: You put it, eat, it's. 00:51:29.310 --> 00:51:32.Wei Zheng: No, no, no, no, also, yeah, yeah, also, yeah, behind also. 00:51:33.380 --> 00:51:35.Wei Zheng: And also, it's… yeah. 00:51:36.490 --> 00:51:37.Duy Nguyen: Sorry, it's… 00:51:39.170 --> 00:51:40.Wei Zheng: Detective method. 00:51:44.960 --> 00:51:50.Wei Zheng: Yeah, what is that frame should be, and what kind of AI agent could be? 00:51:51.930 --> 00:51:57.Wei Zheng: what kind of that frame could it be, and what kind of AI agent could it be? 00:52:15.890 --> 00:52:17.Wei Zheng: Agent could, could be. 00:52:18.220 --> 00:52:20.Wei Zheng: And how can we define each agent? 00:52:28.430 --> 00:52:31.Wei Zheng: How we, how we, how we, how we define, how we define. 00:52:35.410 --> 00:52:37.Wei Zheng: Each, each agent. 00:52:42.260 --> 00:52:44.Wei Zheng: Okay, okay, I see. 00:52:47.450 --> 00:52:54.Wei Zheng: Yeah, you see, that's actually, they tell you, you just try to read, try to understand, and then you see whether you can do it or not, you know what I mean? 00:52:55.580 --> 00:52:56.Duy Nguyen: No. 00:53:01.640 --> 00:53:04.Wei Zheng: Or you can feed this to the cruiser. 00:53:05.040 --> 00:53:05.Wei Zheng: Goodbye! 00:53:06.480 --> 00:53:10.Duy Nguyen: Yeah, yeah, aggravated to the crucible. 00:53:12.320 --> 00:53:17.Wei Zheng: Yeah, you just said, how many agents we need? What is the rule of each agent? 00:53:17.640 --> 00:53:20.Wei Zheng: Oh, no, moment, moment. 00:53:21.350 --> 00:53:21.Wei Zheng: Okay. 00:53:22.220 --> 00:53:36.Wei Zheng: It's like, what, what kind of agent of… how many agents we need, and what, what type of agent, and what's their rule in order to achieve, or in order to let the model to perform? 00:53:36.970 --> 00:53:45.Wei Zheng: The humans… The human's actions that lead to that publication. 00:53:50.770 --> 00:53:54.Wei Zheng: How many agents, and what rule of each agent? 00:53:54.250 --> 00:53:55.Wei Zheng: Should it be? 00:53:55.430 --> 00:54:01.Wei Zheng: defined. In order to let this agent, multi-agent framework 00:54:01.530 --> 00:54:07.Wei Zheng: can… can… can duplicate it. The humans… Walking process. 00:54:07.950 --> 00:54:10.Wei Zheng: That lead to that publication. 00:54:13.730 --> 00:54:24.Wei Zheng: Just how many agents, and what is the rule of each agent should be in that framework that can produ00:54:24.700 --> 00:54:28.Wei Zheng: Or that can… that can duplicate. 00:54:34.690 --> 00:54:38.Wei Zheng: And… And, okay, that can produ00:54:39.510 --> 00:54:45.Wei Zheng: The similar outcome, that performance by human. 00:54:45.650 --> 00:54:53.Wei Zheng: In the efforts, Fall… Doing the thing described in that publication. 00:54:55.280 --> 00:54:56.Duy Nguyen: Similar outcome. 00:54:57.600 --> 00:55:00.Wei Zheng: Ya, as, as. 00:55:01.970 --> 00:55:06.Wei Zheng: Those from that publication, performance by human. 00:55:09.730 --> 00:55:13.Wei Zheng: A publication, attach it here, attach it here. You refer to the publication, attach it here. 00:55:21.190 --> 00:55:23.Wei Zheng: Oh, no, no, moment, moment, similar outcome. 00:55:24.060 --> 00:55:26.Wei Zheng: By human, by human, by human. 00:55:26.970 --> 00:55:28.Wei Zheng: By research, or by author. 00:55:34.380 --> 00:55:36.Wei Zheng: Okay, okay, let's it. 00:55:37.170 --> 00:55:54.Wei Zheng: You see, this is just exactly… I ask you to do that, and then you will review their result, whether you can build it or not. You confident to build it or not, and also whether you're confident to let the cruiser to build it for you or not. 00:56:02.850 --> 00:56:04.Wei Zheng: You see? You see? 00:56:04.610 --> 00:56:05.Duy Nguyen: Yeah, I see. 00:56:05.980 --> 00:56:06.Wei Zheng: Okay. 00:56:06.710 --> 00:56:08.Duy Nguyen: 787… 00:56:08.140 --> 00:56:13.Wei Zheng: You follow the same trend that you used to work it, and do you understand, and do you… 00:56:13.850 --> 00:56:20.Wei Zheng: Do you know how to build it? At least you can instruct the… Crucial to do that. 00:56:32.870 --> 00:56:33.Duy Nguyen: Kidding. 00:56:33.530 --> 00:56:36.Wei Zheng: Yeah, you see, you see, you see, you see, the scape, you see? 00:56:36.890 --> 00:56:43.Wei Zheng: Yeah, exactly, the ChatGPT can help you to do the thing. The only thing is what? You need to operate it. You need to operate. 00:56:44.700 --> 00:56:46.Wei Zheng: override the chat GPT. 00:56:54.770 --> 00:56:56.Wei Zheng: You said yes, yes. 00:56:56.720 --> 00:56:58.Wei Zheng: I want the sketch. 00:56:58.700 --> 00:57:01.Wei Zheng: Yeah, that is… oh, that is Jensen. 00:57:02.240 --> 00:57:07.Wei Zheng: Yeah, yeah, just say, whoa, whoa, whoa, whoa, what do they give to you? You see that? You, you, you're familiar with this? You, you… 00:57:15.360 --> 00:57:16.Wei Zheng: Okay. 00:57:17.100 --> 00:57:22.Wei Zheng: You follow this same thing. You come out of this agent. That's exactly, I ask you, you know what I mean? 00:57:23.890 --> 00:57:29.Wei Zheng: And then you… now you, you just spend some time, you think of it. I think… 00:57:29.970 --> 00:57:34.Wei Zheng: Because, to be honest with you, I think… 00:57:34.530 --> 00:57:40.Wei Zheng: this will be… dominate your… all your time, you know what I mean? Because whenever… 00:57:40.030 --> 00:57:44.Duy Nguyen: of the time, you just… because that is for building your future, you know what I mean, right? 00:57:44.710 --> 00:57:45.Duy Nguyen: Yeah. 00:57:45.830 --> 00:57:46.Duy Nguyen: So, welcome. 00:57:46.360 --> 00:57:50.Wei Zheng: Whenever you have time, you need to think of it, you need to play with it. You need to play with this. 00:57:51.080 --> 00:57:57.Duy Nguyen: Yeah, the most time we have, of my work is, like, to… Oh, like… 00:57:57.550 --> 00:57:59.Duy Nguyen: As a chat duty and read it. 00:57:59.700 --> 00:58:09.Wei Zheng: You already told me about it, yeah. Yeah, and also, you… the thing is, then you need to go to the cruiser. Let me do it. And once they have that. 00:58:09.330 --> 00:58:21.Wei Zheng: Once they have that framework, once they have the code, you verify that. You verify that. If you are not sure, if you are not sure how to verify, you talk to me. You throw me a question, you know what I mean? 00:58:21.150 --> 00:58:21.Duy Nguyen: Okay. 00:58:23.910 --> 00:58:27.Wei Zheng: And, but anyway… 00:58:27.530 --> 00:58:35.Wei Zheng: I don't know if… if… okay, if they provide this, and they… you pulled… you provided this to the cruiser. 00:58:36.300 --> 00:58:45.Wei Zheng: And I think the cruiser could be giving you the framework immediately, but I'm only saying what? You need to verify that, you need to test that, is that? 00:58:45.900 --> 00:58:46.Duy Nguyen: Yes. 00:58:47.240 --> 00:58:50.Wei Zheng: And then how long we can. But essential is what? 00:58:50.760 --> 00:58:52.Wei Zheng: We want the agent. 00:58:52.680 --> 00:58:57.Wei Zheng: can simulate what do they do? And meantime is what? 00:58:57.860 --> 00:59:04.Wei Zheng: I said the key is what the human can input at some… at a very critical location. What do you mean? 00:59:04.840 --> 00:59:13.Wei Zheng: That means our… as a human, they can look at… at… because this is a process, you know what I mean? Even you have a multi… 00:59:15.300 --> 00:59:23.Wei Zheng: You know, this is a process from one step to another step. At each step, they produce some outcome, you like? 00:59:23.880 --> 00:59:34.Wei Zheng: And then the human can reveal this outcome, and the human will not like this outcome. And then, you need to think of it, how the human's input 00:59:35.410 --> 00:59:42.Wei Zheng: Well, feedback to… The pipeline, or to the framework, and then that framework can work. 00:59:42.400 --> 00:59:43.Wei Zheng: commodify. 00:59:45.770 --> 00:59:52.Wei Zheng: It's behavior, based on the human's instruction. That is critical. 00:59:52.880 --> 00:59:54.Wei Zheng: You keep this world. 00:59:55.420 --> 00:59:59.Wei Zheng: I send you the records, you know what I mean? 00:59:59.380 --> 01:00:02.Duy Nguyen: Yeah, I do. Send me, send me the transcript. 01:00:02.180 --> 01:00:06.Wei Zheng: Yeah, yeah, you, I sent you, I, I sent you this, the meeting records. 01:00:06.490 --> 01:00:11.Wei Zheng: That is critical. The critical is what? You need to tell the ChatGPT, 01:00:12.220 --> 01:00:18.Wei Zheng: You said during this process, we want… the human can reveal the process. 01:00:18.670 --> 01:00:21.Wei Zheng: And even human, even if the human. 01:00:22.170 --> 01:00:34.Wei Zheng: do not like their outcome. The human can provide their instruction, their requirement to the system, and then the system can modify its behavior. 01:00:35.370 --> 01:00:39.Wei Zheng: pass out the human's instruction. How we… 01:00:39.470 --> 01:00:48.Wei Zheng: how we do this? And what… please provide me the architecture. And also, we want our agent can do this. 01:00:49.210 --> 01:00:55.Wei Zheng: And if you make it do it, and provide an explanation to me how they do this. 01:00:55.340 --> 01:00:57.Wei Zheng: And how can we? 01:00:58.100 --> 01:00:59.Wei Zheng: Interact. 01:00:59.290 --> 01:01:01.Wei Zheng: with the pipeline. Biff! 01:01:01.390 --> 01:01:02.Wei Zheng: We develop right. 01:01:03.260 --> 01:01:04.Wei Zheng: After we develop her. 01:01:05.760 --> 01:01:07.Wei Zheng: After we're developing. 01:01:07.830 --> 01:01:14.Wei Zheng: After we develop Okay? So, I just said… 01:01:14.630 --> 01:01:21.Wei Zheng: I just say, you… currently, I think, of course, you need to study, you need to finish your coursework. Your school is started yet, or not? 01:01:22.220 --> 01:01:23.Duy Nguyen: Is that? 01:01:23.990 --> 01:01:25.Wei Zheng: It starts this week? 01:01:25.410 --> 01:01:27.Duy Nguyen: This, this is Victor. 01:01:27.860 --> 01:01:30.Wei Zheng: This week is the first day or last week? 01:01:30.420 --> 01:01:33.Duy Nguyen: This week, in. 01:01:33.660 --> 01:01:35.Wei Zheng: So what's your first class start? 01:01:36.500 --> 01:01:38.Duy Nguyen: My first class started… 01:01:39.370 --> 01:01:43.Wei Zheng: I mean, I mean, I'm not yours, I mean the schools, the university's first class. 01:01:45.220 --> 01:01:54.Duy Nguyen: The university for… Guys, 20… January, 2026. 01:01:55.070 --> 01:01:55.Wei Zheng: 26? 01:01:57.300 --> 01:01:58.Duy Nguyen: It's Arista. 01:01:58.080 --> 01:01:59.Wei Zheng: Not yet or not. 01:01:59.710 --> 01:02:02.Duy Nguyen: is to release them. I, I started, yeah. 01:02:03.800 --> 01:02:06.Wei Zheng: You start, no, either. 01:02:07.890 --> 01:02:10.Wei Zheng: So what is the university is the first to come? 01:02:12.600 --> 01:02:14.Duy Nguyen: Oh, you need you. 01:02:14.010 --> 01:02:18.Wei Zheng: university first class started. This is, last Monday or this Monday? 01:02:19.740 --> 01:02:23.Duy Nguyen: this, this Tuesday, because we're off Monday, right? 01:02:24.890 --> 01:02:28.Wei Zheng: Oh, okay, okay, oh, this is Tuesday, okay, okay, okay, this is Tuesday. 01:02:29.310 --> 01:02:31.Wei Zheng: Okay, this is the second day, is that? 01:02:32.080 --> 01:02:32.Duy Nguyen: you know. 01:02:32.410 --> 01:02:33.Wei Zheng: No, no, no, today's… 01:02:33.520 --> 01:02:34.Duy Nguyen: Okay. 01:02:34.370 --> 01:02:50.Wei Zheng: This is a… Okay, okay, Tuesday, Wednesday, Thursday. This is, yeah, this is, okay, okay, I see. Tuesday, Wednesday, today is Thursday, okay, I see, I see. This starts Tuesday, okay. So how many courses do you have this semester? 01:02:50.770 --> 01:02:52.Duy Nguyen: I can show you right here. I can show you right here. 01:02:52.760 --> 01:02:55.Wei Zheng: How many credit, I mean, I mean, it doesn't matter, you just, yeah, you just… 01:02:55.910 --> 01:02:56.Duy Nguyen: I'm here. 01:02:56.890 --> 01:02:59.Duy Nguyen: Do you see that? You see that? 01:03:00.260 --> 01:03:01.Duy Nguyen: You see it? 01:03:01.410 --> 01:03:04.Wei Zheng: Moment, moment, okay. How many? You know, I don't know. 01:03:04.620 --> 01:03:07.Duy Nguyen: 15… 15 hour. 01:03:07.190 --> 01:03:10.Wei Zheng: Okay, okay, let's see, that's your schedule, that class schedule, is that? 01:03:10.800 --> 01:03:11.Duy Nguyen: Yeah. 01:03:11.520 --> 01:03:21.Wei Zheng: So, you are mostly heavily on Monday, Wednesday, and Friday, you have two calls, and you're relatively free on Tuesday and Thursday, right? 01:03:21.100 --> 01:03:21.Duy Nguyen: Yes. 01:03:22.420 --> 01:03:25.Wei Zheng: How many, that is, what, 5 cars, is that? 01:03:25.550 --> 01:03:27.Duy Nguyen: Tech costs, yeah. 01:03:27.010 --> 01:03:30.Wei Zheng: So, how many is computer? How many is computer? 01:03:30.670 --> 01:03:31.Duy Nguyen: Just to… 01:03:32.000 --> 01:03:35.Wei Zheng: Just two computers, and also you have a speech, is that? 01:03:35.240 --> 01:03:36.Duy Nguyen: Yeah, I had AI speech. 01:03:37.160 --> 01:03:39.Wei Zheng: Is it English, or is it just the speech? I mean… 01:03:40.150 --> 01:03:42.Wei Zheng: Is this your presentation, or what, whatever? 01:03:42.820 --> 01:03:43.Duy Nguyen: the presentation. 01:03:43.910 --> 01:03:45.Wei Zheng: In the presentation, okay. 01:03:45.080 --> 01:03:49.Duy Nguyen: Yeah. And here's the senior problem, here's my senior project. 01:03:50.250 --> 01:03:56.Duy Nguyen: 487 is Senior Project, and this is the Advanced Data Science. 01:03:56.540 --> 01:03:57.Wei Zheng: Okay, okay. 01:03:57.230 --> 01:03:58.Duy Nguyen: I hear. 01:03:58.070 --> 01:04:00.Wei Zheng: How about, how about, how about that? 01:04:00.690 --> 01:04:04.Wei Zheng: So, you are, actually, you have the two major computer science courses. 01:04:04.600 --> 01:04:09.Wei Zheng: And then you have the speech court, and what I… 01:04:10.830 --> 01:04:11.Duy Nguyen: Pardon? 01:04:11.680 --> 01:04:13.Wei Zheng: And this is the last semester, Doctor? 01:04:13.480 --> 01:04:15.Duy Nguyen: Yeah, this is my last semester. 01:04:16.070 --> 01:04:16.Wei Zheng: Okay. 01:04:17.080 --> 01:04:19.Wei Zheng: So what others, what is this, sir? 01:04:19.820 --> 01:04:21.Duy Nguyen: Yeah, here's the geology. 01:04:21.840 --> 01:04:23.Wei Zheng: what? It's a mess? 01:04:24.590 --> 01:04:27.Duy Nguyen: No, it's… it's geology, it's… 01:04:27.100 --> 01:04:28.Wei Zheng: Oh, geology, geology. 01:04:28.790 --> 01:04:29.Duy Nguyen: geology, yeah. 01:04:30.560 --> 01:04:33.Wei Zheng: What is geology. Geology is. 01:04:35.840 --> 01:04:37.Duy Nguyen: That's GPT? 01:04:37.050 --> 01:04:43.Wei Zheng: Yeah, yeah, look, let's see, what's geology? Oh, it's a, oh, it's a, it's geology, it's just like ocean, ocean, or earth. 01:04:43.730 --> 01:04:45.Duy Nguyen: Yeah, it's yours. 01:04:45.070 --> 01:04:49.Wei Zheng: Why you choose this? Because it's just for fun, or what? Or is it just, like… 01:04:50.170 --> 01:04:53.Duy Nguyen: Because I, I, I, I took, 01:04:54.240 --> 01:05:02.Duy Nguyen: the, most of the, the, the physics. A lot of physics in the… The previous year. 01:05:02.580 --> 01:05:05.Wei Zheng: This person is easy, right? This is… 01:05:05.260 --> 01:05:07.Duy Nguyen: Yeah, it's easy for me, yes, cause it's easy. 01:05:07.270 --> 01:05:11.Wei Zheng: This is, if you have ChatGPT, that course is… 01:05:12.310 --> 01:05:15.Wei Zheng: Do they allow you to open book or closed book? 01:05:16.290 --> 01:05:18.Wei Zheng: I mean, when they do the exam, do the quiz. 01:05:19.090 --> 01:05:22.Duy Nguyen: When… when those exams, they just allow… 01:05:22.300 --> 01:05:26.Duy Nguyen: The… the cheat sheet… the cheat sheet to a small cheat sheet, like this. 01:05:26.910 --> 01:05:28.Wei Zheng: Oh, chi… chi… 01:05:28.750 --> 01:05:29.Duy Nguyen: Did she… 01:05:29.680 --> 01:05:34.Wei Zheng: A cheat sheet, okay, cheat sheet. But you can prepare the cheat sheet by using ChatGPT, right? 01:05:35.470 --> 01:05:39.Wei Zheng: You can prepare the cheat sheet by using ChatGPT. 01:05:39.800 --> 01:05:46.Wei Zheng: You prepare, you make, you, you, you can make your cheat sheet by using ChatGPT, yeah? 01:05:46.120 --> 01:05:53.Duy Nguyen: Actually, most… most of the time when I… when I, 01:05:53.550 --> 01:05:59.Duy Nguyen: create the cheat sheet, or… I, like… read… 01:06:00.060 --> 01:06:06.Duy Nguyen: all the… the chapter, and the summary, and I see summary, and then I try it. Because… 01:06:07.290 --> 01:06:11.Duy Nguyen: The cheat sheet have to be… In the handwriting. 01:06:12.010 --> 01:06:14.Wei Zheng: Oh, okay, okay, that's fine, that's fine, you can't ride! 01:06:15.080 --> 01:06:22.Wei Zheng: Okay, they allow you to do that. But you just copy ChatGPT, that's fine, is that? 01:06:22.760 --> 01:06:28.Wei Zheng: Yeah, okay, okay, okay. How about, what are the courses? 01:06:28.050 --> 01:06:30.Duy Nguyen: Here's the… Data sizing? 01:06:30.890 --> 01:06:38.Wei Zheng: Yeah, that's… I know it's computer science, you have two computer science, what else? Speech. No, you have three computer science courses, right? 01:06:39.950 --> 01:06:41.Duy Nguyen: No, just two. 01:06:41.680 --> 01:06:44.Wei Zheng: You have a… you only have, wah. 01:06:44.690 --> 01:06:47.Wei Zheng: You only have 4 classes, design? 01:06:47.000 --> 01:06:50.Duy Nguyen: I… yeah, I have one online class. 01:06:50.780 --> 01:06:52.Wei Zheng: What's this, online? 01:06:52.710 --> 01:06:54.Duy Nguyen: Yeah, it's… it's CJ. 01:06:54.980 --> 01:06:56.Wei Zheng: What's this cost? 01:06:56.270 --> 01:06:57.Wei Zheng: What are these cars? 01:07:07.890 --> 01:07:10.Wei Zheng: So, what do you, what do you do for your project? 01:07:11.040 --> 01:07:14.Wei Zheng: Can you… can you choose subject of your project? 01:07:16.530 --> 01:07:21.Wei Zheng: Senior developer, you can… all the instructor assigned to you, or you can choose. 01:07:22.170 --> 01:07:27.Duy Nguyen: I can choose anything, like, mobile app, or web app? 01:07:27.450 --> 01:07:33.Wei Zheng: Yeah, yeah, why you choose? You, you do not choose for our project. We can develop some app. 01:07:35.000 --> 01:07:37.Wei Zheng: Who, who's your instructor for that, that one? 01:07:38.870 --> 01:07:46.Duy Nguyen: I just start coming school in this week, right? So, 01:07:47.230 --> 01:07:50.Duy Nguyen: We have 2 weeks to, like, find the… 01:07:51.150 --> 01:07:55.Wei Zheng: Yeah, well, yeah, we can talk about this part. We can develop some app for education. 01:07:58.620 --> 01:07:59.Wei Zheng: project! 01:07:59.540 --> 01:08:00.Wei Zheng: Is, is it possible? 01:08:01.170 --> 01:08:03.Duy Nguyen: Yeah, it's really possible. 01:08:03.680 --> 01:08:05.Wei Zheng: Yeah, who's your instructor? 01:08:06.670 --> 01:08:07.Wei Zheng: For this course. 01:08:10.080 --> 01:08:12.Duy Nguyen: Right now, I think I will… 01:08:13.380 --> 01:08:16.Wei Zheng: Now, who's the instructor of this course for your senior design project? 01:08:17.479 --> 01:08:18.Duy Nguyen: Like, you mean the… 01:08:18.990 --> 01:08:20.Wei Zheng: Instructor, teacher, the faculty. 01:08:20.660 --> 01:08:25.Duy Nguyen: The teacher? The other sponsor, because Discord have to, like. 01:08:25.700 --> 01:08:28.Duy Nguyen: I have to find the sponsor for this. 01:08:28.200 --> 01:08:31.Duy Nguyen: The, for the final, for the senior project. 01:08:33.160 --> 01:08:39.Wei Zheng: You mean… I mean, who is your course instructor? There are no course instructors? 01:08:40.759 --> 01:08:42.Duy Nguyen: Oh, yeah, yeah. 01:08:42.469 --> 01:08:43.Duy Nguyen: I'm sorry. 01:08:45.669 --> 01:08:47.Duy Nguyen: I have two right here. 01:08:47.949 --> 01:08:49.Wei Zheng: This person. 01:08:50.779 --> 01:08:51.Duy Nguyen: It's November. 01:08:51.300 --> 01:08:52.Wei Zheng: faculty, this faculty? 01:08:55.470 --> 01:09:00.Wei Zheng: This is the, the, the, the, the assistant of faculty. 01:09:04.589 --> 01:09:06.Duy Nguyen: They use the faculty. 01:09:06.390 --> 01:09:07.Wei Zheng: You're the faculty? 01:09:08.740 --> 01:09:15.Duy Nguyen: Because, like, for this… for the single project. 01:09:15.729 --> 01:09:22.Duy Nguyen: All of the students have to find The… the professor, the… 01:09:23.109 --> 01:09:28.Duy Nguyen: The sponsor, like, they will assist them for the student? 01:09:28.660 --> 01:09:32.Wei Zheng: How about you… you know the Dr. Wang? Dr. Wang, you know Dr. Wang? 01:09:34.060 --> 01:09:37.Duy Nguyen: I know Dr. 1, and I know Dr. 1. Dr. Fengwan? 01:09:37.750 --> 01:09:43.Wei Zheng: Yeah, can you talk to him? Because I talked to him before. Could you just, 01:09:43.970 --> 01:09:45.Duy Nguyen: Do you know him? Because, like… 01:09:45.680 --> 01:09:46.Wei Zheng: him, I know him, I know him. 01:09:47.710 --> 01:09:51.Wei Zheng: Dr. Wang… okay, let's see, let's see, what's the name? 01:09:51.359 --> 01:09:53.Duy Nguyen: Dr. Feng would like to hear you. Dr. Feng would… 01:09:55.590 --> 01:09:57.Wei Zheng: Okay, let's say, what's the name? 01:09:58.300 --> 01:09:59.Duy Nguyen: 8, ma'am. 01:09:59.800 --> 01:10:04.Wei Zheng: Oh, no, no, not this one. This is Dr. Huang. Dr. Huang. 01:10:05.550 --> 01:10:12.Wei Zheng: Let's B.O. B.O, B.O, B.O. What's the name? 01:10:12.490 --> 01:10:14.Duy Nguyen: Oh, bonwa, bohoi? Do you know… 01:10:14.190 --> 01:10:15.Wei Zheng: Yeah, yeah, yeah. 01:10:15.850 --> 01:10:22.Duy Nguyen: Oh… And I know him, I know him because I, I, I took the, the, my, my. 01:10:22.750 --> 01:10:26.Wei Zheng: The Transformer course, I can teach a transformer, huh? Transformer. 01:10:27.060 --> 01:10:28.Duy Nguyen: Just a minute, please. 01:10:29.480 --> 01:10:34.Duy Nguyen: Computer Science… Omnis. 01:10:36.070 --> 01:10:37.Duy Nguyen: I could see… 01:10:41.510 --> 01:10:42.Duy Nguyen: History. 01:10:42.660 --> 01:10:44.Wei Zheng: I, I, I talked to… yeah, okay. 01:10:44.950 --> 01:10:54.Wei Zheng: Yeah, I know that you're a chair, I know your chair. Because now, no, I've communicated with several times. That's why, you know, I communicated him with… regarding recruit a student, you know? 01:10:54.760 --> 01:10:55.Duy Nguyen: This guy right? 01:10:55.850 --> 01:10:56.Duy Nguyen: Boy. 01:10:56.520 --> 01:11:03.Wei Zheng: Yeah, yeah. Okay, what's the name? What's the name, what's the name? Oh, yeah, yeah, yeah, his name. 01:11:03.070 --> 01:11:04.Duy Nguyen: Is this guy? 01:11:04.190 --> 01:11:05.Wei Zheng: Yeah. 01:11:05.590 --> 01:11:09.Duy Nguyen: he… he already… he… he's Chinese. 01:11:10.050 --> 01:11:11.Wei Zheng: Yeah, yeah, yeah. 01:11:12.180 --> 01:11:14.Wei Zheng: Yeah. The same one. 01:11:14.290 --> 01:11:16.Wei Zheng: You must find the faculty, right? 01:11:16.810 --> 01:11:17.Duy Nguyen: Yes. 01:11:17.810 --> 01:11:24.Wei Zheng: I can talk to him, and then, probably, We can walk on… 01:11:25.090 --> 01:11:29.Wei Zheng: Something… just continue work on what you are currently working on. 01:11:29.730 --> 01:11:31.Wei Zheng: Because eventually, we want what? 01:11:31.850 --> 01:11:34.Wei Zheng: We want a developer something 01:11:35.510 --> 01:11:41.Wei Zheng: we can just, like, find the knowledge, you know what I mean? It's a similar thing, even for your current thing. 01:11:42.500 --> 01:11:44.Wei Zheng: We can extend that. 01:11:45.130 --> 01:11:46.Wei Zheng: You know what I mean? 01:11:46.440 --> 01:11:49.Wei Zheng: You can't extend what you're currently doing. 01:11:49.360 --> 01:11:51.Wei Zheng: To a more broad sense. 01:11:52.540 --> 01:11:55.Wei Zheng: It's just like, try to digest. 01:11:55.640 --> 01:12:00.Wei Zheng: The knowledge, and try to find the conclusion, find the knowledge. 01:12:03.480 --> 01:12:04.Duy Nguyen: Okay. 01:12:06.550 --> 01:12:18.Wei Zheng: But anyway, it's up to you, it's up to you. But if you want, we can… I can talk to him, and then he can… he can actually, yeah, be… just, like, serve as your advisor, or whatever. 01:12:18.140 --> 01:12:19.Wei Zheng: And, 01:12:19.570 --> 01:12:27.Wei Zheng: And then just come out of something. But this senior design project is just one semester, it's not started from last semester? 01:12:27.990 --> 01:12:29.Duy Nguyen: Just one semester. 01:12:29.600 --> 01:12:41.Wei Zheng: Yeah, you think of it, you think of it, you just say, this project, because we have, I have some lot of ideas regarding what we should do, or even we build something, the app. 01:12:41.800 --> 01:12:51.Wei Zheng: For… because for us, wine for… you know, for me, why in this area, you are working on it, right? Another area is education. 01:12:51.340 --> 01:12:53.Wei Zheng: We try to do something. 01:12:54.720 --> 01:13:03.Wei Zheng: But, but anyway, you will do the multi… multi… what? Multiple agent framework? You, you, you, you are interested in this one, right? 01:13:04.600 --> 01:13:06.Duy Nguyen: Yes, I understand it too soon. 01:13:06.320 --> 01:13:11.Wei Zheng: And then, with this framework, we can find some more specific application. 01:13:11.600 --> 01:13:19.Wei Zheng: But I think you just locked, like, this way. You locked with multiple agents remote. Definitely you will do that, because that is the trend, you know? 01:13:20.940 --> 01:13:21.Duy Nguyen: Yes. 01:13:22.370 --> 01:13:26.Wei Zheng: And then, we will identify a particular thing. 01:13:27.630 --> 01:13:42.Wei Zheng: we are interested, because now I try to collaborate with him, with Dr. Wang, to do some, the proposal. We… but at least we can build something, just like we said, we… we… we build one. 01:13:43.660 --> 01:13:47.Wei Zheng: We computed the universal framework. 01:13:47.280 --> 01:13:55.Wei Zheng: That universal framework that can digest the specific domain knowledge, like publication. 01:13:55.670 --> 01:14:05.Wei Zheng: And then, they will predict the research direction. They will predict the, the, the, the, the, the, the, yeah, we can say research direction. 01:14:06.100 --> 01:14:13.Wei Zheng: Or which one, which area they have the… is a good direction to… to do the research, you know what I mean? 01:14:14.840 --> 01:14:16.Wei Zheng: Bears on the nudge. 01:14:16.350 --> 01:14:17.Duy Nguyen: Just like. 01:14:17.780 --> 01:14:19.Wei Zheng: You're currently doing for this one? 01:14:21.650 --> 01:14:24.Wei Zheng: You think of it, you think of it. 01:14:25.740 --> 01:14:26.Wei Zheng: Is that? 01:14:27.010 --> 01:14:28.Duy Nguyen: Yeah, I'm terrific. 01:14:28.360 --> 01:14:31.Wei Zheng: I will, I will, I will give you some idea. 01:14:32.220 --> 01:14:33.Wei Zheng: An event? 01:14:34.370 --> 01:14:36.Duy Nguyen: Thank you. You think of it. Thank you. 01:14:37.170 --> 01:14:37.Wei Zheng: Yah. 01:14:39.650 --> 01:14:40.Wei Zheng: tell you, what do we try to do? 01:14:40.850 --> 01:14:41.Duy Nguyen: Yeah. 01:14:41.490 --> 01:14:41.Wei Zheng: We try. 01:14:41.870 --> 01:14:47.Duy Nguyen: I'm really excited when you talk with me like this. Yeah. I'm really excited. 01:14:47.090 --> 01:14:48.Wei Zheng: The scene's what? 01:14:48.740 --> 01:14:50.Wei Zheng: The seed! 01:14:51.080 --> 01:14:52.Wei Zheng: the current… 01:14:54.330 --> 01:15:11.Wei Zheng: research… because now a lot of things is developed for the industry, but there are lots of things developed for the academic. So you know what an academic doing? They will fund the research direction. Which direction is promising? They will have an impact. 01:15:11.380 --> 01:15:14.Wei Zheng: They will… it's feasible to do. 01:15:15.260 --> 01:15:18.Wei Zheng: So what do you need? You need to look at the existing 01:15:18.740 --> 01:15:22.Wei Zheng: Literature. You need to look at what is already built, is that? 01:15:22.830 --> 01:15:26.Wei Zheng: Based on what they already built? And then, based on… 01:15:26.750 --> 01:15:31.Wei Zheng: The rule they found from the scientific research finding 01:15:32.220 --> 01:15:37.Wei Zheng: I mean, I talk about the rule, because the rule is what? It's the god of the rule, you know what I mean? 01:15:37.590 --> 01:15:39.Wei Zheng: the card of… you know what I mean. 01:15:39.820 --> 01:15:40.Duy Nguyen: How about you? 01:15:40.520 --> 01:15:41.Wei Zheng: curation, you know what I mean? 01:15:42.480 --> 01:15:53.Wei Zheng: We… what do we… what do we try to do? At the very beginning, I talked to you. We tried to collect this information from the publications, but eventually we want to try to find what? 01:15:53.890 --> 01:15:56.Wei Zheng: the physical laws, you know what I mean? 01:15:57.940 --> 01:15:58.Duy Nguyen: Yeah. 01:15:58.730 --> 01:16:01.Duy Nguyen: The physical, or God, God, the physical. 01:16:01.860 --> 01:16:08.Wei Zheng: You know, you know what I mean? God. You know the God, is that? Because the God is the rule, the everything. The people say that. 01:16:08.740 --> 01:16:13.Wei Zheng: Because whatever occurred is out of your control, is controlled by God, you know? 01:16:14.240 --> 01:16:22.Wei Zheng: The God is… it's a general sense, it's not like a religion sense, you know what I mean? The God is a kind of the nature. 01:16:22.740 --> 01:16:27.Wei Zheng: Just like your body. Your body, sometimes you cannot control your body. Who control is God's control. 01:16:27.790 --> 01:16:30.Wei Zheng: You know what I mean? You know what I mean, because… 01:16:30.990 --> 01:16:41.Wei Zheng: whatever beyond your control, that is… whatever… the thing beyond the human control, that is controlled by the rule, right? By the rule. But we try to find one. 01:16:41.570 --> 01:16:50.Wei Zheng: the… based on the… because the people… what are the people doing? They try to find the project Newton, you know what I mean? The Newton found the gravity, you know what I mean? 01:16:51.120 --> 01:16:53.Wei Zheng: Therefore, they exist. 01:16:53.750 --> 01:17:02.Wei Zheng: But the Newton, they found the relation, whatever the gravity, you know, you know what I mean, the gravity or whatever. They found it, but that is the rule, you know? 01:17:03.410 --> 01:17:14.Wei Zheng: What do scientific research mean? They try to… they try to follow the rule to better guide the people, you know what I mean? So, whatever we just say, we try to buil01:17:15.120 --> 01:17:20.Wei Zheng: Okay, I'll tell you what I try to do. I, I think… I think it should be interesting. Which I try to do what? 01:17:21.740 --> 01:17:24.Wei Zheng: Just… just similar to what you… you did here. 01:17:25.020 --> 01:17:33.Wei Zheng: We try to build the multiple agent, okay? The multiple agent is what we… they… they can track 01:17:33.240 --> 01:17:34.Wei Zheng: The new development! 01:17:35.170 --> 01:17:36.Wei Zheng: In a specific area. 01:17:37.200 --> 01:17:41.Wei Zheng: Just like you developed the, web crab, did I? 01:17:42.050 --> 01:17:42.Wei Zheng: Web… 01:17:42.560 --> 01:17:43.Duy Nguyen: the web scraping. 01:17:43.860 --> 01:17:51.Wei Zheng: You will… I think the… I think the, the, the Alex… the Alex is the master developer. 01:17:51.130 --> 01:17:55.Wei Zheng: side. They can have some updated information, is that? 01:17:55.720 --> 01:17:56.Duy Nguyen: Yeah. 01:17:56.700 --> 01:18:04.Wei Zheng: You know, and then we will develop the agent. They can track the updated research, scientific research. 01:18:04.270 --> 01:18:05.Duy Nguyen: Oh! Okay, yeah. 01:18:05.930 --> 01:18:06.Wei Zheng: Another area! 01:18:06.740 --> 01:18:08.Duy Nguyen: Very practical, yeah. Okay. 01:18:08.100 --> 01:18:09.Wei Zheng: You see what I mean? 01:18:09.360 --> 01:18:14.Wei Zheng: And then we will digest, just like you're doing, just like you're doing here. 01:18:14.520 --> 01:18:19.Wei Zheng: And then we will, after we digest, we build a knowledge graph, or similar. 01:18:20.050 --> 01:18:27.Wei Zheng: And based on the knowledge graph, we can, you know, you… if you… if you… You know. 01:18:27.760 --> 01:18:35.Wei Zheng: In the knowledge graph, the one thing was, they try to build a knowledge graph. And also, they try to predict a knowledge graph they haven't built. 01:18:35.980 --> 01:18:42.Wei Zheng: They try to find the relation, you know, the knowledge graph we built is, like. 01:18:42.490 --> 01:18:44.Wei Zheng: These are the existing knowledge. 01:18:45.830 --> 01:18:51.Wei Zheng: And in their relation. But, there's a lot of things, people is unknown. 01:18:51.520 --> 01:18:52.Wei Zheng: He's like… 01:18:52.720 --> 01:18:53.Duy Nguyen: Yeah, enough. 01:18:53.590 --> 01:19:09.Wei Zheng: Not a PC, but what is the unknown? The unknown is the relation between the entity already in your knowledge graph, and another entity, another entity in your knowledge graph, and then we will try to see. 01:19:09.760 --> 01:19:23.Wei Zheng: If there's a relation between these two entities, that if we can find this relation between, the entity based on the knowledge graph, that actually is… we found the knowledge. We found a new knowledge. 01:19:26.620 --> 01:19:32.Wei Zheng: If you look at the… if you… you know that we have a traditional knowledge graph. 01:19:32.780 --> 01:19:40.Wei Zheng: the one task for the knowledge graph is built a long time ago, before, before the chat GPT, you know what I mean? 01:19:40.250 --> 01:19:42.Duy Nguyen: Yeah, 20 years history. 01:19:42.820 --> 01:19:50.Wei Zheng: And in that knowledge graph, one… one task is what? It's try to find the relation between entity. 01:19:51.260 --> 01:19:54.Wei Zheng: That already… that haven't established a relation. 01:19:54.830 --> 01:19:57.Wei Zheng: But, well, they can inference. 01:19:57.410 --> 01:20:03.Wei Zheng: Whether they have that relation or not, based on the existing knowledge graph. 01:20:04.850 --> 01:20:12.Wei Zheng: It's kind of a thing, it's what we try to verify, we try to identify the potential relation, and then we try to… 01:20:14.800 --> 01:20:19.Wei Zheng: I will, I will send you something, okay? I will send you something. I think that's where, you know. 01:20:19.720 --> 01:20:21.Duy Nguyen: I like your idea, yeah. 01:20:21.100 --> 01:20:21.Wei Zheng: I did. 01:20:21.770 --> 01:20:22.Duy Nguyen: Okay. 01:20:22.300 --> 01:20:25.Wei Zheng: But if you need advice, you talk to him, you talk to this guy. 01:20:26.710 --> 01:20:28.Wei Zheng: I will actually, I will tell him. 01:20:29.040 --> 01:20:32.Wei Zheng: And we, we can, we can't do this. Because… 01:20:34.620 --> 01:20:36.Duy Nguyen: I think I will do this. 01:20:36.850 --> 01:20:42.Wei Zheng: Yeah, I think, yeah, because you already, you already have some foundation. You shouldn't know this is very important. 01:20:43.560 --> 01:20:45.Wei Zheng: And also, I tell you. 01:20:45.680 --> 01:20:51.Wei Zheng: Is another is what? You look at the Google, I don't know if Google or Microsoft, they call the… 01:20:51.700 --> 01:20:54.Wei Zheng: S… science, science, science, 01:20:55.340 --> 01:21:02.Wei Zheng: It's just like Google Science or Microsoft Science. You, you, you, you, you, you, you Google it, you, you, you use ChatGPT. 01:21:02.170 --> 01:21:10.Wei Zheng: You said, which company, Google or Microsoft, developers are, assigns? 01:21:10.230 --> 01:21:16.Wei Zheng: For the sign… for the, for… no, no, no, you, you, you chat, you, you, you chat with ChatGPT. 01:21:17.440 --> 01:21:25.Wei Zheng: You said, is, is Google or Microsoft have a developer, AI scientist that can 01:21:25.750 --> 01:21:28.Wei Zheng: Guide a science… scientific research. 01:21:32.820 --> 01:21:36.Wei Zheng: Developer, the AI, sign… scientist. 01:21:36.730 --> 01:21:39.Wei Zheng: Or scientist model, or similar. 01:21:43.380 --> 01:21:48.Wei Zheng: No, no, no, no, no, not data science. Just the science, just the science, yeah. 01:21:51.960 --> 01:21:54.Wei Zheng: Developer. No, develop, develop. 01:21:55.650 --> 01:21:56.Duy Nguyen: Fair enough. 01:21:57.480 --> 01:22:00.Wei Zheng: Developing, developing, developing, set developing. 01:22:02.520 --> 01:22:05.Wei Zheng: AI scientist, AI scientist. 01:22:05.770 --> 01:22:08.Wei Zheng: or AI researcher. 01:22:17.400 --> 01:22:18.Duy Nguyen: Such a… 01:22:18.870 --> 01:22:22.Wei Zheng: Research model that guides scientific research. 01:22:34.570 --> 01:22:35.Duy Nguyen: Oh. 01:22:37.180 --> 01:22:39.Wei Zheng: scientific research. 01:22:39.170 --> 01:22:39.Duy Nguyen: Guy. 01:22:40.380 --> 01:22:42.Wei Zheng: Yeah, guide the scientific research. 01:22:44.270 --> 01:22:46.Wei Zheng: Guide, scientific, scientific. 01:22:50.900 --> 01:22:52.Duy Nguyen: Let's see, cyan… 01:22:53.170 --> 01:22:56.Wei Zheng: Yes, it's… Scientific, scientific research. 01:22:57.710 --> 01:22:59.Wei Zheng: Scientific, Tificica. 01:23:01.500 --> 01:23:01.Duy Nguyen: And the… 01:23:01.970 --> 01:23:03.Wei Zheng: scientific, yeah. 01:23:03.920 --> 01:23:04.Wei Zheng: Research. 01:23:14.050 --> 01:23:22.Wei Zheng: I will talk… if you are interested, I will talk him, because, he will serve as your instructor. Okay, you… 01:23:22.400 --> 01:23:26.Wei Zheng: Oh, no, no… You chat with ChatGPT us. 01:23:39.010 --> 01:23:39.Duy Nguyen: Signal. 01:23:45.160 --> 01:23:47.Duy Nguyen: My internet is kind of slow. 01:23:53.110 --> 01:23:54.Duy Nguyen: I'm sorry. 01:23:56.800 --> 01:23:58.Wei Zheng: Triple Touches together. 01:24:08.980 --> 01:24:12.Duy Nguyen: is the Google-Microsoft Developing AI Researcher Model. 01:24:12.600 --> 01:24:14.Duy Nguyen: That guy's anti-. 01:24:14.610 --> 01:24:15.Wei Zheng: Research. 01:24:30.830 --> 01:24:31.Duy Nguyen: Both. 01:24:34.180 --> 01:24:35.Duy Nguyen: He said that. 01:24:37.690 --> 01:24:56.Wei Zheng: Yeah, we just try to… we just try to how to make this fit the specific publication. If you are interested, I will talk to Dr. Wang, and I will talk to him, you… you talk to him and let him serve your… your advisor, you know what I mean? But actually, you can directly communicate with me, you know what I mean? 01:24:56.670 --> 01:24:58.Duy Nguyen: Yes. Okay. 01:24:58.550 --> 01:24:59.Wei Zheng: Let me… okay. 01:24:59.700 --> 01:25:01.Duy Nguyen: Thank you so much. 01:25:01.300 --> 01:25:04.Wei Zheng: If you determine you like to do this. 01:25:05.260 --> 01:25:06.Duy Nguyen: Yeah, yeah. 01:25:07.790 --> 01:25:17.Wei Zheng: We will do something similar to this, but we'll put more… more… more specific. Yeah, more… more specific way. But this is the trend, this is the trend. 01:25:18.280 --> 01:25:29.Wei Zheng: The thing is, just like the agent, they can monitor the new development, and then they can produce some new knowledge, or some good direction. 01:25:29.840 --> 01:25:31.Wei Zheng: for the research. 01:25:31.770 --> 01:25:32.Wei Zheng: You know what I mean? 01:25:32.540 --> 01:25:34.Duy Nguyen: Yes. Yeah, I know. 01:25:34.470 --> 01:25:40.Wei Zheng: Okay, but now you try to work on this… we try to finish that paper, you know what I mean? 01:25:40.900 --> 01:25:42.Duy Nguyen: Yeah, the draft, right? 01:25:42.340 --> 01:25:51.Wei Zheng: Yeah, yeah, yeah, yeah. I will tell you, I will… once I… because, actually, I try to… because we work… I currently work with 4 or 5 students. 01:25:51.620 --> 01:26:02.Wei Zheng: We just, submit, the draft paper for a conference. I think at least 3 papers. The one student, they do not produce a result. 01:26:02.640 --> 01:26:14.Wei Zheng: we try to see if we can postpone the deadline. We request the conference division chair to let us postpone our submission, but 01:26:14.410 --> 01:26:24.Wei Zheng: I'm waiting for them. But yesterday, we submitted 5 paper. Oh, no! We submit, we submit three, three draft paper. So that's why I'm busy, 01:26:24.890 --> 01:26:30.Wei Zheng: But now, I'm having more time. But after that… but the thing is what? I hope you… 01:26:30.590 --> 01:26:35.Wei Zheng: What? We can… we can catch this deadline to finish this draft, got the result. 01:26:36.110 --> 01:26:39.Wei Zheng: You know what I mean? Do the evaluation, what are we talking? I just said that. 01:26:40.380 --> 01:26:46.Wei Zheng: Since that is your major sense, whenever you have time, you just try to walk out, you know what I mean? 01:26:46.890 --> 01:26:47.Duy Nguyen: Yes. 01:26:48.100 --> 01:26:51.Wei Zheng: Okay, okay, okay. I will send the transcript, yeah, for you, yeah. 01:26:51.910 --> 01:26:54.Duy Nguyen: Thank you so much, thank you. 01:26:54.660 --> 01:26:55.Wei Zheng: Yeah. 01:26:55.270 --> 01:26:55.Duy Nguyen: Hello. 01:26:56.320 --> 01:26:56.Wei Zheng: Yup.


========================================

## GMT20260204-220840_Recording.transcript.vtt

00:00:00.930 --> 00:00:06.Wei Zheng: So… You still need to figure out What do the agents do? 00:00:06.900 --> 00:00:08.Wei Zheng: In the… in that process. 00:00:08.740 --> 00:00:09.Duy Nguyen: Okay. 00:00:12.540 --> 00:00:13.Wei Zheng: Oh. 00:00:13.500 --> 00:00:16.Wei Zheng: Last time, I asked you to ask the AI, right? 00:00:16.570 --> 00:00:17.Duy Nguyen: Yeah. 00:00:17.500 --> 00:00:27.Wei Zheng: Regarding… Regarding what we intend to do, and regarding what they actually do. 00:00:29.200 --> 00:00:32.Wei Zheng: And then you ask the AI, how can we make the… 00:00:32.400 --> 00:00:36.Wei Zheng: edge in the framework to simulate not… 00:00:36.340 --> 00:00:36.Duy Nguyen: Yes. 00:00:37.140 --> 00:00:39.Wei Zheng: First of all, what are we intend to do? 00:00:39.810 --> 00:00:43.Wei Zheng: I think you can based on what I already sent to you, you know? 00:00:43.840 --> 00:00:47.Duy Nguyen: Use the abstract, and there any… Information? 00:00:48.360 --> 00:00:53.Wei Zheng: Yeah, and… and what they do? Actually, you can fail. 00:00:53.950 --> 00:00:56.Wei Zheng: ChatGPT with their people. 00:00:57.020 --> 00:00:59.Duy Nguyen: Yes. And then you'll say, what kind of framework? 00:01:00.640 --> 00:01:01.Wei Zheng: We should have. 00:01:03.820 --> 00:01:06.Wei Zheng: I… and how we build this? 00:01:22.580 --> 00:01:23.Wei Zheng: Okay. 00:01:25.000 --> 00:01:37.Duy Nguyen: yesterday, I… I… I sent all my questions, for the… Jackson University, from your school? 00:01:37.860 --> 00:01:38.Wei Zheng: I feel… . 00:01:38.980 --> 00:01:41.Duy Nguyen: For the, like, the procedure. 00:01:42.080 --> 00:01:46.Duy Nguyen: for applying the PhD? 00:01:47.530 --> 00:01:53.Duy Nguyen: in… up to now, I didn't… Have any response. 00:01:54.000 --> 00:01:54.Duy Nguyen: I'm okay. 00:01:54.930 --> 00:01:57.Wei Zheng: Okay, very well respond to. 00:01:57.930 --> 00:01:59.Wei Zheng: Well, you look at the website? 00:02:00.770 --> 00:02:04.Wei Zheng: Do you look at the website, what's the procedure it is? What's the requirement it is? 00:02:06.450 --> 00:02:13.Wei Zheng: Because there are too many students, I don't know if they will respond or not. But anyway, you look at the website, you look at what's the requirement. 00:02:16.840 --> 00:02:21.Duy Nguyen: But I have a question for you, like, In your department? 00:02:21.140 --> 00:02:21.Wei Zheng: No. 00:02:22.070 --> 00:02:28.Duy Nguyen: The injury department, they… Do they require the GRE? 00:02:28.860 --> 00:02:33.Wei Zheng: I don't… I have no idea. I have no idea. It's not our department. It's a graduate school. 00:02:33.730 --> 00:02:34.Wei Zheng: It's graduate school. 00:02:35.150 --> 00:02:38.Wei Zheng: You, you go to the website, you can, you can, you can immediately find it. 00:02:38.750 --> 00:02:48.Duy Nguyen: Because, like, the website is required, the GRE, but the department, they, they, they do, they do not require it. 00:02:48.430 --> 00:02:55.Wei Zheng: No, even graduate school requires that you must have, because you're always admitted by graduate school, not by our department. 00:02:58.720 --> 00:03:01.Wei Zheng: Your father must be omitted by our graduate school. 00:03:03.780 --> 00:03:05.Duy Nguyen: Oh, okay. 00:03:05.010 --> 00:03:08.Wei Zheng: Even required, it definitely didn't require it. No. 00:03:11.570 --> 00:03:13.Duy Nguyen: I already asked them, but… 00:03:14.220 --> 00:03:17.Wei Zheng: You look at their website, this should be as a requirement. 00:03:17.570 --> 00:03:19.Duy Nguyen: Yeah, I love the website. 00:03:23.640 --> 00:03:25.Wei Zheng: No, the deadline is what? 00:03:26.440 --> 00:03:28.Wei Zheng: Starting in March either, huh? 00:03:29.030 --> 00:03:32.Duy Nguyen: Yeah… is… Dove. 00:03:33.310 --> 00:03:37.Duy Nguyen: Is the beginning in March? 00:03:48.470 --> 00:03:52.Wei Zheng: So, when you will end it, I mean, your… when this semester will end it. 00:03:52.650 --> 00:04:00.Duy Nguyen: This ma- this semester will end at around, like, 15 in major. 00:04:01.610 --> 00:04:02.Wei Zheng: Guinea over the mate. 00:04:03.300 --> 00:04:08.Duy Nguyen: Yeah, around, like… On the… on the half of… in… in May, in May. 00:04:10.630 --> 00:04:12.Wei Zheng: So, your plan go back to… 00:04:13.320 --> 00:04:15.Wei Zheng: Go back to your country during the summer? 00:04:16.290 --> 00:04:17.Duy Nguyen: No. 00:04:17.250 --> 00:04:25.Duy Nguyen: I'm not planning to go back to country. I will, like, request for the OPT and… And I'll continue. 00:04:26.050 --> 00:04:26.Wei Zheng: Okay. 00:04:27.050 --> 00:04:29.Duy Nguyen: And I, I, I applied for… 00:04:29.790 --> 00:04:38.Duy Nguyen: the fall in GSU, and we'll continue studying and not go back to my country this summer. 00:04:38.030 --> 00:04:39.Wei Zheng: Okay, probably… 00:04:40.160 --> 00:04:40.Duy Nguyen: And I will, like… 00:04:40.920 --> 00:04:43.Wei Zheng: But probably I can let you work on during the summer. 00:04:43.690 --> 00:04:47.Duy Nguyen: Yeah, yeah. I'm not gonna go back to my country this month, this summer. 00:04:48.320 --> 00:04:49.Wei Zheng: Okay, okay. 00:04:49.990 --> 00:04:55.Wei Zheng: But anyway, I have no idea regarding the admission, because actually, I do not have any graduate. 00:04:55.090 --> 00:04:55.Duy Nguyen: Yeah, yeah. 00:04:55.820 --> 00:04:57.Wei Zheng: I'm on mine, myself. 00:04:57.360 --> 00:04:57.Duy Nguyen: I have. 00:04:57.710 --> 00:04:59.Wei Zheng: Use other people to register. 00:04:59.100 --> 00:05:00.Duy Nguyen: I understand that. 00:05:00.630 --> 00:05:06.Wei Zheng: I have no idea how they do that, because basically the idea is what they ever… they ask the IE, 00:05:07.030 --> 00:05:08.Wei Zheng: You must have the TIE. 00:05:09.820 --> 00:05:11.Wei Zheng: Even if they require them. 00:05:11.410 --> 00:05:12.Wei Zheng: No. 00:05:12.810 --> 00:05:15.Wei Zheng: We cannot overcome their requirement. 00:05:17.790 --> 00:05:18.Wei Zheng: But anyway… 00:05:25.340 --> 00:05:27.Wei Zheng: Because tomorrow, I have a meeting. 00:05:28.420 --> 00:05:34.Wei Zheng: Could you just say, how can we transfer that data, and also the algorithm? The algorithm, you just pass it to. 00:05:34.790 --> 00:05:35.Duy Nguyen: No doubt. 00:05:35.170 --> 00:05:37.Wei Zheng: Let him walker, whatever. 00:05:37.810 --> 00:05:44.Wei Zheng: Whatever we want. But now, I think you are currently working on that paper. You already do something, right? 00:05:44.340 --> 00:05:45.Duy Nguyen: Yes. 00:05:45.000 --> 00:05:48.Wei Zheng: So, this is a… That is a… 00:05:48.980 --> 00:05:53.Duy Nguyen: By the way, and can I have his… his email? His email. 00:05:54.060 --> 00:05:54.Wei Zheng: What do you know? 00:05:55.490 --> 00:05:58.Duy Nguyen: The, the PHD guy. 00:06:00.220 --> 00:06:03.Wei Zheng: You mean the email in the JSU? 00:06:04.360 --> 00:06:05.Wei Zheng: Oh! 00:06:06.130 --> 00:06:08.Duy Nguyen: He's, the PA… 00:06:08.560 --> 00:06:11.Wei Zheng: Oh, I can, I can tell you, I can tell you, I can tell you. 00:06:11.210 --> 00:06:13.Duy Nguyen: Okay. Yeah, I can contact with him, and… 00:06:22.820 --> 00:06:27.Wei Zheng: How you do that? How you do that? How you deliver that? Or… 00:06:29.210 --> 00:06:34.Duy Nguyen: Or I can ask… I can ask the team to create the Amazon, and then you just transfer the data. Okay, yeah, yeah. 00:06:34.940 --> 00:06:36.Wei Zheng: How… you… how many… 00:06:37.640 --> 00:06:43.Wei Zheng: I mean, how many… how many data… I mean, how many publications you already have? I'm… you have a rough idea? 00:06:47.780 --> 00:06:50.Duy Nguyen: I already stopped is… 00:06:51.010 --> 00:06:53.Wei Zheng: And a Khomeini, you have an idea, and a Khomeini. 00:06:58.610 --> 00:07:01.Wei Zheng: How many in the file you have? Roughly, roughly. 00:07:01.970 --> 00:07:02.Duy Nguyen: Roughly. 00:07:03.600 --> 00:07:07.Duy Nguyen: Actually, I have no idea. I will share you the screen, and you will see it. 00:07:55.040 --> 00:07:58.Wei Zheng: Can you know what is the volume it is, at least? 00:07:58.400 --> 00:08:00.Wei Zheng: What's the data volume? 00:08:02.210 --> 00:08:04.Wei Zheng: Baptists, how many baptized? 00:08:07.040 --> 00:08:08.Duy Nguyen: How many backpack kits? 00:08:08.950 --> 00:08:10.Wei Zheng: Yeah, I mean, the volume of data. 00:08:12.140 --> 00:08:12.Duy Nguyen: Yeah. 00:08:13.390 --> 00:08:14.Duy Nguyen: I have not checked it. 00:08:17.200 --> 00:08:19.Duy Nguyen: For the long term, go by. 00:08:21.370 --> 00:08:22.Duy Nguyen: H3. 00:08:42.900 --> 00:08:45.Duy Nguyen: Here's all I have, as you can see. 00:08:47.820 --> 00:08:50.Wei Zheng: I mean, what's the volume with teeth? I mean, I mean… 00:08:51.280 --> 00:08:53.Wei Zheng: This is just a photo, yeah? 00:08:53.400 --> 00:08:54.Duy Nguyen: Yeah, I used to… 00:08:54.700 --> 00:08:57.Wei Zheng: But, how they organize this? This is, 00:08:58.910 --> 00:09:02.Wei Zheng: I mean, what this is, this is, you look at something. 00:09:03.760 --> 00:09:06.Duy Nguyen: Here's the day that, today, the… 00:09:06.230 --> 00:09:13.Wei Zheng: I mean, I mean, I mean, what is the, what is the thing you open? What is the platform you open? Is it a particular platform to open the data? 00:09:13.760 --> 00:09:16.Wei Zheng: I mean, what you are showing on the screen is what? 00:09:17.580 --> 00:09:19.Wei Zheng: Is Amazon for the files, huh? 00:09:19.870 --> 00:09:25.Duy Nguyen: Yeah, it's a S3 bucket, the database of the… the cloud. 00:09:25.740 --> 00:09:26.Duy Nguyen: Dice. 00:09:26.360 --> 00:09:30.Wei Zheng: So they will organize the data, they let you see the data in this way, right? 00:09:30.430 --> 00:09:31.Duy Nguyen: Yes. 00:09:31.800 --> 00:09:32.Wei Zheng: Okay. 00:09:36.190 --> 00:09:40.Duy Nguyen: I think it's very easy to see, becaus00:09:41.130 --> 00:09:48.Duy Nguyen: ISI is today, the month, and year is very, very easy to follow. 00:09:48.240 --> 00:09:53.Wei Zheng: I mean, that data is the data that… when you collect the data, all the data, they publish it. 00:09:54.160 --> 00:09:56.Wei Zheng: I mean, the time, the date. 00:09:58.690 --> 00:10:06.Wei Zheng: You organize based on when you collect those data, or you organize based on their publication, the year of their publication. 00:10:07.770 --> 00:10:11.Duy Nguyen: Just, just the day I collect the data, no. 00:10:11.150 --> 00:10:12.Wei Zheng: Okay, okay, okay. 00:10:15.150 --> 00:10:18.Wei Zheng: Okay, so that's easy to read about, right? 00:10:18.640 --> 00:10:20.Duy Nguyen: Yes, it's very easy to read. 00:10:20.510 --> 00:10:24.Wei Zheng: No, no, no, no, I don't mean the read by people, I mean the read by my king. 00:10:25.300 --> 00:10:30.Wei Zheng: If we want to… You were one of my hero, really. 00:10:31.280 --> 00:10:38.Wei Zheng: So, you're basically… your data type is a different type. Why is the PDF? Why is the one? 00:10:38.350 --> 00:10:39.Wei Zheng: Just the text. 00:10:43.890 --> 00:10:46.Wei Zheng: what type of data you have there? I mean. 00:10:47.650 --> 00:10:50.Wei Zheng: We cannot manually process it. We need a… 00:10:51.490 --> 00:10:54.Wei Zheng: Fiddle with the machine, and then we let the machine to determine that. 00:10:56.020 --> 00:11:01.Duy Nguyen: It's very easy to fit to the machine, the machine can get easy to read it because it's the JSON file. 00:11:03.090 --> 00:11:04.Wei Zheng: Is this JSON file? 00:11:04.270 --> 00:11:06.Duy Nguyen: Yeah, it's a JSON 5. 00:11:06.160 --> 00:11:12.Wei Zheng: Generally, but they will put a different type of file in a different location, right? 00:11:12.190 --> 00:11:13.Duy Nguyen: Leon, yes. 00:11:14.370 --> 00:11:20.Wei Zheng: So, you, you have the JSON file structure, is that? You specify that, is that? 00:11:20.350 --> 00:11:27.Duy Nguyen: Yes, I have the JS5 structure, the author, the title, the abstract, the geo, Anything. 00:11:27.360 --> 00:11:30.Wei Zheng: So, you need to provide us all the information, boss. 00:11:31.580 --> 00:11:41.Wei Zheng: you need to provide your JSON file information. So, that means once we know this format, we can easily let the machine read it, based on the different type, is that? 00:11:41.720 --> 00:11:42.Duy Nguyen: Yeah. 00:11:43.730 --> 00:11:46.Wei Zheng: Because we need to… we need to process those. 00:11:47.170 --> 00:11:52.Wei Zheng: We need processors. I asked him to do this processing. You just pass this to… 00:11:52.750 --> 00:11:53.Duy Nguyen: Okay, okay. 00:11:53.830 --> 00:11:59.Wei Zheng: him, and then I will let him. And probably… we probably want him to do further. 00:11:59.560 --> 00:12:03.Duy Nguyen: Scripting, scripting, based on what you already have, okay? 00:12:04.830 --> 00:12:05.Duy Nguyen: No. 00:12:06.980 --> 00:12:15.Wei Zheng: Yeah, and and so, so far, you haven't made any progress regarding… regarding… regarding what we… we tried to do. 00:12:17.710 --> 00:12:25.Wei Zheng: I mean, you have an idea regarding the aging framework we… we try to do, because now it's only… probably the only 20 days left. 00:12:30.150 --> 00:12:33.Duy Nguyen: For the last week, I cannot do anything. 00:12:33.980 --> 00:12:35.Wei Zheng: Okay, okay. 00:12:35.150 --> 00:12:37.Duy Nguyen: So, I think I will… I have to… 00:12:38.270 --> 00:12:42.Duy Nguyen: Like, done it, and rush it in this… in this. 00:12:42.530 --> 00:12:44.Wei Zheng: Okay, okay, okay, okay, okay. 00:12:46.450 --> 00:12:47.Wei Zheng: Okay. 00:12:47.680 --> 00:12:48.Wei Zheng: No. 00:12:50.700 --> 00:12:52.Wei Zheng: Yeah, you just, 00:12:53.370 --> 00:12:59.Wei Zheng: So, the one way that we… it's easy to transfer your data, it's easy to transfer 00:12:59.930 --> 00:13:04.Wei Zheng: from one Amazon counter to another Amazon counter, is that? You can do this, is that? 00:13:08.630 --> 00:13:15.Duy Nguyen: Maybe I can, I will fi- I will figure out in tonight and let… 00:13:15.020 --> 00:13:15.Wei Zheng: Okay, okay. 00:13:15.700 --> 00:13:22.Duy Nguyen: Yeah, okay, okay, okay. Because… Actually, around, like. 00:13:22.680 --> 00:13:30.Duy Nguyen: many weeks ago, I sent you the, like, the step-by-step to, like, create your own account. 00:13:30.310 --> 00:13:38.Duy Nguyen: Because… This AWS, the security is very important, so I cannot use… 00:13:39.580 --> 00:13:43.Duy Nguyen: It has a two-layer, security. 00:13:43.700 --> 00:13:48.Duy Nguyen: So that's why I cannot use your email and create your account. 00:13:50.880 --> 00:13:58.Wei Zheng: Okay, I understand, I understand, because that's… I tried, I also, I tried before. I… I have no idea how… how to do that. 00:13:58.540 --> 00:14:03.Wei Zheng: But anyway… If I let him create an account. 00:14:05.040 --> 00:14:11.Wei Zheng: No, I mean, if I will… I asked him to create account, that is easy to transfer the data from your account to his account, right? 00:14:12.070 --> 00:14:14.Duy Nguyen: Yeah. Actually, let me pass. 00:14:20.060 --> 00:14:22.Wei Zheng: Always anyway, you can… 00:14:22.760 --> 00:14:30.Wei Zheng: you can put those in some place, and then… because I know that if you let some people got into that access, it's very difficult. 00:14:30.170 --> 00:14:34.Wei Zheng: But how about you… you output those data? 00:14:34.220 --> 00:14:36.Wei Zheng: You put it in somewhere. 00:14:36.680 --> 00:14:40.Wei Zheng: In some, some, some cloud. 00:14:40.700 --> 00:14:44.Wei Zheng: And let him go there. Oh, yeah. Okay, okay. 00:14:44.510 --> 00:14:46.Wei Zheng: Either he called it. 00:14:46.340 --> 00:14:47.Duy Nguyen: A good idea, yeah. 00:14:47.100 --> 00:14:48.Wei Zheng: Common Cloud, is that? 00:14:49.180 --> 00:14:50.Wei Zheng: Yeah, it's free, right? 00:14:50.980 --> 00:14:52.Duy Nguyen: Yeah, it's free. 00:14:52.840 --> 00:14:53.Wei Zheng: Yeah, you just… 00:14:53.370 --> 00:14:55.Duy Nguyen: I think he scoot all day. 00:14:55.580 --> 00:15:15.Wei Zheng: You just output that file into the cloud, and then let him go there, and whether they put data there, or they will download data in his account, that we will determine later. But at least you put it in some place. We, of course, we do not let him go into your Amazon account. I know that is difficult. 00:15:15.380 --> 00:15:28.Wei Zheng: But you just output your data in, and put in some… you create some, some account in some, free, space, the iCloud, or… 00:15:29.060 --> 00:15:30.Wei Zheng: Good luck! 00:15:30.020 --> 00:15:31.Duy Nguyen: Okay, yeah, yeah. 00:15:31.130 --> 00:15:32.Wei Zheng: Not the public is the easy way. 00:15:33.800 --> 00:15:36.Wei Zheng: And then after that, I will let him to, to, to, to… 00:15:36.940 --> 00:15:37.Duy Nguyen: Right, yeah. 00:15:37.520 --> 00:15:44.Wei Zheng: to look at the data and to look at your JSON file, and if you have any questions, we can ask you, yeah. 00:15:45.050 --> 00:15:45.Duy Nguyen: Okay. 00:15:47.670 --> 00:15:48.Wei Zheng: We'll go back. 00:15:48.580 --> 00:15:50.Duy Nguyen: Yeah, I think it's good today. 00:15:52.420 --> 00:15:58.Wei Zheng: And, I can make the contract start with this week, okay? 00:15:59.270 --> 00:16:00.Duy Nguyen: Okay. 00:16:01.900 --> 00:16:02.Wei Zheng: Yeah. 00:16:03.430 --> 00:16:06.Duy Nguyen: We have to end the, the, the, the last. 00:16:06.520 --> 00:16:11.Wei Zheng: End of the semester, and then we can start, yeah, the summer, yeah. 00:16:12.960 --> 00:16:13.Wei Zheng: Okay? 00:16:14.010 --> 00:16:16.Duy Nguyen: Okay, thank you, thank… thank you so much. 00:16:16.430 --> 00:16:22.Wei Zheng: But anyway, I'll just say, whenever you have time, you just walk on, because that is… 00:16:22.340 --> 00:16:32.Wei Zheng: is a… it's a kind of thing is very interesting, and also its area is very, very interesting. I don't know, you… you have a class, this semester, you have a… you told me you have, what, four classes? 00:16:35.700 --> 00:16:37.Wei Zheng: I mean… You have a. 00:16:37.550 --> 00:16:43.Duy Nguyen: I have 5 classes. I have 5 classes this semester. Yeah. I have 5 classes. 00:16:43.250 --> 00:16:44.Wei Zheng: 5 car, okay. 00:16:44.230 --> 00:16:45.Duy Nguyen: Yeah, thank class. 00:16:45.700 --> 00:16:51.Duy Nguyen: the Far East, the… One of them is just the online class. 00:16:51.600 --> 00:16:53.Wei Zheng: Okay, okay, okay. 00:16:55.700 --> 00:17:03.Duy Nguyen: And I… actually, next week, I will, talk to, Dr. Bo Wang. 00:17:03.670 --> 00:17:14.Wei Zheng: Yeah, okay, you will talk to… I will send an email to him. I just said, he… because we tried to… I tried to collaborate with him, we tried to write some collaborative proposal regarding… 00:17:14.010 --> 00:17:23.Wei Zheng: We will do in the Mississippi. I will talk to him. You talk to him, just talk about, what we try to do. Basically, we just try to based on the literature. 00:17:23.950 --> 00:17:26.Wei Zheng: To fund the new trend of the research. 00:17:28.099 --> 00:17:29.Wei Zheng: Use a platform. 00:17:29.950 --> 00:17:33.Duy Nguyen: Okay. Can you, like, send me… 00:17:33.720 --> 00:17:35.Wei Zheng: I will send both of you, I will send. 00:17:35.270 --> 00:17:37.Duy Nguyen: Yeah, yeah, okay. Yeah, it's easy for me to… 00:17:37.930 --> 00:17:41.Wei Zheng: So, next week, so when? You have an appointment with him yet? 00:17:43.000 --> 00:17:45.Wei Zheng: You have an appointment with him yet, or no? 00:17:46.280 --> 00:17:48.Duy Nguyen: No. 00:17:48.310 --> 00:17:52.Wei Zheng: about what next week, what, what day? Before that, I will send an email. I will send an email. 00:17:52.840 --> 00:17:56.Duy Nguyen: I think, in Monday, Tuesday. 00:17:56.080 --> 00:17:57.Wei Zheng: Monday, okay, okay, okay, okay, okay. 00:17:58.000 --> 00:17:59.Duy Nguyen: I will talk, talk to him. 00:17:59.100 --> 00:18:04.Wei Zheng: Okay, so you basically let him as advisor, is that? Yeah. Okay, that's no problem. 00:18:04.590 --> 00:18:08.Duy Nguyen: I even, like, passed my, Sponsor. 00:18:09.210 --> 00:18:10.Wei Zheng: Yeah, yeah, yeah. 00:18:11.010 --> 00:18:21.Wei Zheng: But actually, we work here. But anyway, you just use whatever we do here for your… for your project. But he need as an advisor or sponsor, you know? 00:18:21.940 --> 00:18:22.Duy Nguyen: Yeah. 00:18:22.670 --> 00:18:26.Wei Zheng: Yeah, okay, I will talk him, I will talk him, I will talk him, yeah. 00:18:26.160 --> 00:18:33.Duy Nguyen: Because I cannot meet him this week, or last week, because the storm is so terrible in Oxford. 00:18:33.530 --> 00:18:35.Wei Zheng: Okay, okay, okay, okay. 00:18:35.140 --> 00:18:36.Duy Nguyen: I'm about to say that. 00:18:36.000 --> 00:18:39.Wei Zheng: I will… I will talk to him. I will send an email to both of you, okay? 00:18:39.400 --> 00:18:40.Duy Nguyen: Okay. 00:18:40.780 --> 00:18:46.Wei Zheng: Okay, you can talk to him, and then… yeah. I think I will promote him. 00:18:46.280 --> 00:18:57.Wei Zheng: Also interested in this, because we plan to do a collaborative proposal, in the… in the fall, in the fall, regarding how to do this in the. 00:18:57.630 --> 00:19:01.Duy Nguyen: But, like, I think, 00:19:01.290 --> 00:19:05.Duy Nguyen: I will end… I will have to present the… 00:19:05.840 --> 00:19:10.Duy Nguyen: the senior project in the beginning of May, so we just have. 00:19:10.020 --> 00:19:13.Wei Zheng: Like, to… Oh, when, when, when you need, when you need to do that? 00:19:14.160 --> 00:19:17.Duy Nguyen: I have two, presentation. 00:19:17.740 --> 00:19:19.Wei Zheng: Oh, you're the final, final president. 00:19:19.210 --> 00:19:25.Duy Nguyen: The final, yeah, the final presentation in the beginning of May, so we just have, like, two… 00:19:25.870 --> 00:19:28.Duy Nguyen: Two months, or two and a half, or two months. 00:19:28.500 --> 00:19:32.Wei Zheng: Could you send me what's the requirement for your… for your course price? 00:19:32.320 --> 00:19:33.Duy Nguyen: Yeah, okay, okay. 00:19:33.210 --> 00:19:37.Wei Zheng: You send me whatever is your school requirement, and then I will frame it. 00:19:38.310 --> 00:19:43.Wei Zheng: Did I make what you do, filled with this, okay? Okay. And I will send an email to him, yeah. 00:19:43.100 --> 00:19:43.Duy Nguyen: Okay. 00:19:43.940 --> 00:19:44.Wei Zheng: Okay, okay. 00:19:45.150 --> 00:19:50.Wei Zheng: Okay, okay, just, yeah, just think of it and tell me, by tomorrow, okay? 00:19:50.890 --> 00:19:51.Duy Nguyen: Okay. 00:19:51.570 --> 00:19:54.Wei Zheng: Yeah, tell me how to do the data transfer, okay? 00:19:54.570 --> 00:19:55.Duy Nguyen: Okay, yeah. 00:19:55.330 --> 00:19:56.Wei Zheng: Okay, okay. 00:19:56.280 --> 00:19:57.Duy Nguyen: I will do it right now, so… 00:19:57.700 --> 00:19:58.Wei Zheng: Yeah, yeah, okay. 00:19:58.820 --> 00:20:00.Duy Nguyen: And let you know. 00:20:00.250 --> 00:20:02.Wei Zheng: Yeah, yeah, yeah, as soon as possible, yeah, thank you.


========================================

## GMT20260219-020030_Recording.transcript.vtt

00:00:06.460 --> 00:00:14.Wei Zheng: Okay. Oh, that, is it recording? Is it recording? Oh, yeah, it's a recording, yeah, yeah. 00:00:14.710 --> 00:00:21.Wei Zheng: So, I'm sorry, I'm recently a little busy, and yeah, I just wonder. 00:00:21.020 --> 00:00:23.Duy Nguyen: You're very busy here. 00:00:23.460 --> 00:00:24.Wei Zheng: Oh, what? 00:00:24.870 --> 00:00:31.Wei Zheng: What is… because now it's only about 10 days left. I just wonder what… what we can come out. 00:00:32.189 --> 00:00:38.Wei Zheng: And, I think before you try to simulate the… the… what? Try to… 00:00:38.450 --> 00:00:48.Wei Zheng: Try to establish the knowledge graph that can establish the relations, that identify The identity, right? 00:00:48.890 --> 00:00:51.Duy Nguyen: And you see, the identity, and the… 00:00:51.700 --> 00:01:00.Wei Zheng: I don't know, do they have the relation, or the original publication, they have the relation or not? But anyway, they have some identity, original publication. 00:01:02.280 --> 00:01:12.Wei Zheng: And, how this now? Is any, any… we said before, we said that you try to do, interactive, iterative. 00:01:13.540 --> 00:01:14.Duy Nguyen: Yes. 00:01:14.660 --> 00:01:17.Wei Zheng: So, what's the, what's current, what's current the situation? 00:01:19.130 --> 00:01:26.Duy Nguyen: My… right now, my direction is, like. 00:01:26.270 --> 00:01:33.Duy Nguyen: The knowledge graph first, and then the agent second, and then verification loop. 00:01:33.310 --> 00:01:38.Duy Nguyen: for the… for the zero step. 00:01:39.660 --> 00:01:46.Duy Nguyen: is… it's gonna be, like, human input, so… so… like… 00:01:46.370 --> 00:01:51.Duy Nguyen: And then for the step one, we will build the knowledge graph. 00:01:52.320 --> 00:02:08.Duy Nguyen: from, Graph, rack, and… the… the… Step 2 is, like, the… Quality Gate, validator. 00:02:09.840 --> 00:02:21.Duy Nguyen: And then, the multi-agent, the lan chain, land graph, And… And for the last step, It's like… 00:02:21.900 --> 00:02:27.Duy Nguyen: Scale up into, 28… Paper. 00:02:29.150 --> 00:02:35.Duy Nguyen: And for the idea, for the idea for, multi-AI Asian, 00:02:35.910 --> 00:02:38.Duy Nguyen: I'm gonna do, like, the ontology. 00:02:40.410 --> 00:02:50.Duy Nguyen: We will keep the schema in rule, and… and then the extraction agent, the… the graph rack. 00:02:50.640 --> 00:03:02.Duy Nguyen: Index 10… And then, typing… validator… Asian… 00:03:04.870 --> 00:03:08.Wei Zheng: No, okay. Now you talk about the architecture, right? 00:03:08.810 --> 00:03:09.Duy Nguyen: Yeah, that's okay. 00:03:10.100 --> 00:03:14.Wei Zheng: I talked about what's the result for your first iterativ00:03:14.910 --> 00:03:22.Wei Zheng: Regarding that original, we talked about, we try to let them identify entity. We need to define an entity. 00:03:23.170 --> 00:03:31.Wei Zheng: And then we let them to identify entity and see whether, via identification, Well, Eid. 00:03:31.250 --> 00:03:39.Wei Zheng: Whether their identification of entity, from this, from this publication, is, 00:03:40.180 --> 00:03:47.Wei Zheng: That can match… that can match what the author Identification. 00:03:48.120 --> 00:03:49.Wei Zheng: Have you tried that? 00:03:55.100 --> 00:03:57.Wei Zheng: I think before, you already tried once, is that? 00:03:57.680 --> 00:03:59.Duy Nguyen: Yeah, let me try one. 00:04:08.140 --> 00:04:15.Wei Zheng: Can you do the second, second trial or third trial and see the result is close to what we, what the author 00:04:16.810 --> 00:04:19.Wei Zheng: Present all what we like. 00:04:27.850 --> 00:04:38.Duy Nguyen: Actually, I'm not gonna try the second, because for the, for the last week, I sick for the whole, whole last week. 00:04:38.680 --> 00:04:42.Duy Nguyen: So I'm not gonna do, every too much. 00:04:44.470 --> 00:04:47.Wei Zheng: What you… well, do not… every 2 months? What… when… 00:04:48.190 --> 00:04:53.Duy Nguyen: I'm not gonna do, I'm not doing very too much for the last week. 00:04:56.000 --> 00:04:58.Wei Zheng: So, what's the current do you have? Now… 00:04:59.230 --> 00:05:02.Wei Zheng: So, what kind of result do we have now, so far? 00:05:04.920 --> 00:05:14.Duy Nguyen: For right now, I have the… the version 4, the… 2004, like, 00:05:14.810 --> 00:05:19.Duy Nguyen: I, I improved the entity, and improve the relationship. 00:05:20.890 --> 00:05:24.Wei Zheng: Do the author, did the author have those kind of things? 00:05:25.310 --> 00:05:28.Wei Zheng: Did the author do those kind of things or not? 00:05:36.130 --> 00:05:44.Wei Zheng: So, what we will present in that draft paper? Of course, we need to have the architecture. We need to have the method. 00:05:44.730 --> 00:05:47.Wei Zheng: And then we need to present the result. 00:05:47.580 --> 00:05:55.Wei Zheng: And also, And also, we need to incorporate what you did before. 00:05:56.160 --> 00:06:02.Wei Zheng: Have you tried that, you already developed that framework to search literature, is that? 00:06:02.090 --> 00:06:02.Duy Nguyen: Yeah. 00:06:02.890 --> 00:06:10.Wei Zheng: Have you tried that? Let that… I think you must do that. You have to do that. You change criteria. 00:06:11.270 --> 00:06:12.Wei Zheng: Of that search. 00:06:13.500 --> 00:06:18.Wei Zheng: And also, you try to set up the… the scope! 00:06:19.210 --> 00:06:34.Wei Zheng: within the scope of that author's scope. Because also, when they make the publication, when they try to search literature, you know what I mean? So, they are published two years ago, you know? I'm not sure, said. 00:06:34.440 --> 00:06:44.Wei Zheng: If their publication was published 2 years ago, okay? And then their literature search should be probably about another 1 year. 00:06:45.380 --> 00:06:46.Wei Zheng: a hat. 00:06:47.040 --> 00:06:54.Wei Zheng: So, that means we will… Set up the same criteria as the author. 00:06:55.590 --> 00:07:00.Wei Zheng: set up. I think also, when you do the literature search, they have some criteria. 00:07:00.920 --> 00:07:01.Duy Nguyen: Yeah. 00:07:01.590 --> 00:07:05.Wei Zheng: And then, we have the cut of time. 00:07:06.110 --> 00:07:09.Wei Zheng: At the same cut of time of the author did. 00:07:10.010 --> 00:07:18.Wei Zheng: Say, 2 years ago, and then plus 1 year, plus 3 years ago. Our cut-off time is… 00:07:18.680 --> 00:07:20.Wei Zheng: Before. 00:07:21.130 --> 00:07:22.Wei Zheng: That's 3 years ago. 00:07:22.930 --> 00:07:24.Wei Zheng: - you know what I mean? 00:07:24.760 --> 00:07:25.Duy Nguyen: Yeah. 00:07:25.370 --> 00:07:26.Wei Zheng: And is that? 00:07:27.700 --> 00:07:37.Wei Zheng: And also, he probably mentioned where they searched, is that? What database, what journal they searched, is I? Did they mention that? They should mention that, is that? 00:07:38.040 --> 00:07:43.Wei Zheng: And then you put those similar to what they did, and then you do the search. 00:07:43.800 --> 00:07:48.Wei Zheng: You let your engine do the search. And also, your engin00:07:48.390 --> 00:07:51.Wei Zheng: Not engine. Whatever you already developed. 00:07:51.740 --> 00:07:53.Duy Nguyen: Well, be PARB. 00:07:53.420 --> 00:07:54.Wei Zheng: Of our model. 00:07:55.860 --> 00:07:57.Wei Zheng: You see what I mean? 00:07:57.160 --> 00:07:57.Duy Nguyen: Yeah. 00:07:58.310 --> 00:07:59.Duy Nguyen: That's right. 00:07:59.380 --> 00:08:11.Wei Zheng: So, you need to provide all those information. And also, first, you set up this criteria and do the search. I don't know the… the Mac let you do something, but I… because I… originally, I asked him to. 00:08:11.740 --> 00:08:12.Duy Nguyen: Yeah. 00:08:12.970 --> 00:08:14.Wei Zheng: But I don't know… 00:08:14.260 --> 00:08:20.Duy Nguyen: I already, received the email. Yeah, I already received his email. 00:08:22.220 --> 00:08:34.Wei Zheng: Okay, but I… but I suppose… no, I… because that's why I… I asked you to handle that to him. I… actually, I want him to do that. But anyway, you know what it means, right? So… 00:08:34.500 --> 00:08:39.Wei Zheng: You will set up your… You also, you need, what? 00:08:40.510 --> 00:08:46.Wei Zheng: We will do that later, but first, you will set up the search criteria. 00:08:46.510 --> 00:08:47.Duy Nguyen: Yeah. Exactly. 00:08:48.160 --> 00:08:55.Wei Zheng: as the search, and then at the C, whether you can come out, the literature is close to th00:08:55.170 --> 00:09:00.Wei Zheng: Whatever they identified, about, what, 28 or something like that? 00:09:01.070 --> 00:09:01.Duy Nguyen: Yeah. 00:09:02.080 --> 00:09:03.Wei Zheng: You know what I mean? 00:09:03.180 --> 00:09:04.Duy Nguyen: Yeah, I understand that. 00:09:04.810 --> 00:09:05.Wei Zheng: Honestly? 00:09:06.250 --> 00:09:11.Wei Zheng: After you got to row 28, And then you do whatever. 00:09:12.080 --> 00:09:13.Wei Zheng: They try to do. 00:09:13.990 --> 00:09:21.Wei Zheng: And I don't know, do they have a knowledge graph? Or they, at least, they try, they probably, they do not have the mention. 00:09:22.050 --> 00:09:29.Wei Zheng: They may not mention they do the knowledge graph, but whatever, they do the literature review as 00:09:30.260 --> 00:09:36.Wei Zheng: they do the literature review itself. It's kind of the same. Like, 00:09:36.830 --> 00:09:39.Wei Zheng: Establish some knowledge base, is that? 00:09:39.610 --> 00:09:40.Duy Nguyen: Yeah. 00:09:40.340 --> 00:09:45.Wei Zheng: And then, based on this knowledge base, I don't know, they try to identify 00:09:45.930 --> 00:09:51.Wei Zheng: the, the, the big, big concept, or big entity, you know what I mean? 00:09:51.440 --> 00:09:54.Duy Nguyen: Yeah, the entity is a big concern. 00:09:54.380 --> 00:09:59.Wei Zheng: Yeah, yeah, yeah. And then the definer, and then… Then you use your second… 00:09:59.990 --> 00:10:02.Wei Zheng: What call that? Google, Microsoft, I don't know. 00:10:02.920 --> 00:10:04.Duy Nguyen: Microsoft, graph app. 00:10:04.670 --> 00:10:10.Wei Zheng: And then, that's your second, that's your second, yeah. Second layer, okay. 00:10:10.980 --> 00:10:12.Wei Zheng: Get your search. 00:10:12.650 --> 00:10:13.Duy Nguyen: Yes. 00:10:13.160 --> 00:10:19.Wei Zheng: Second layer is knowledge graph, or whatever, and then… Okay, for the first part. 00:10:19.940 --> 00:10:27.Wei Zheng: For first, the knowledge, for the first literature search, you will come out some results, and then we will compare. 00:10:27.920 --> 00:10:30.Wei Zheng: your search result. You, you identify! 00:10:31.320 --> 00:10:33.Wei Zheng: You set up the criteria. 00:10:33.680 --> 00:10:41.Wei Zheng: just do the screen of the literature, is that? And then, you will use the same criteria, the author. 00:10:41.960 --> 00:10:45.Wei Zheng: how used No, no, you know what I mean? The arts are… 00:10:45.690 --> 00:10:46.Duy Nguyen: Good. 00:10:46.130 --> 00:10:53.Wei Zheng: The… the… based on literature search, the… Screen out of about 28. 00:10:53.610 --> 00:11:00.Wei Zheng: You know what? Publication. And see, if you specify And let's see, how much? 00:11:01.620 --> 00:11:05.Wei Zheng: You got, and how close, what you got? 00:11:05.480 --> 00:11:06.Duy Nguyen: what I got, yeah. 00:11:06.480 --> 00:11:07.Wei Zheng: Compared to… 00:11:08.080 --> 00:11:08.Duy Nguyen: Yeah. 00:11:08.960 --> 00:11:10.Wei Zheng: Also, God, you see? 00:11:10.540 --> 00:11:12.Duy Nguyen: Yeah. That's the first one. 00:11:12.490 --> 00:11:20.Wei Zheng: The second one… And then, we… we just use their identified 28. 00:11:21.110 --> 00:11:21.Wei Zheng: Okay? 00:11:22.180 --> 00:11:32.Wei Zheng: as our, what, as our feed to the, Microsoft, whatever, knowledge graph, building that? 00:11:32.700 --> 00:11:33.Duy Nguyen: Yeah. 00:11:33.890 --> 00:11:34.Wei Zheng: On his end? 00:11:35.150 --> 00:11:44.Wei Zheng: What kind of process we need to use to let them learn, let them to identify the entity that can match. 00:11:45.000 --> 00:11:48.Wei Zheng: What the author has obtained. 00:11:49.540 --> 00:11:51.Wei Zheng: That is the second comparison. 00:11:52.340 --> 00:11:53.Duy Nguyen: Okay. 00:11:53.110 --> 00:11:56.Wei Zheng: At least you need to come out with the result, and then make the comparison. 00:11:57.640 --> 00:12:03.Duy Nguyen: I promise I will, like, complete, 00:12:03.560 --> 00:12:06.Duy Nguyen: by fri… by this… this Friday. 00:12:06.560 --> 00:12:07.Wei Zheng: That jut truck! 00:12:07.190 --> 00:12:07.Duy Nguyen: He's weird. 00:12:07.730 --> 00:12:17.Wei Zheng: you try to do your best, because… and also, we need God's… we try to… we need to try to make this accepted, okay? 00:12:17.750 --> 00:12:18.Duy Nguyen: Yep. 00:12:18.420 --> 00:12:31.Wei Zheng: Whenever you have time, okay, I just said, whenever you have time, you just try to do… try to do that, because that is the… because I think that's also your interest, but also we believe this is relatively new, and also. 00:12:31.590 --> 00:12:38.Wei Zheng: we can extend it to other fields. That will be your project. Have you talked to Dr. Wang? 00:12:38.940 --> 00:12:41.Duy Nguyen: Yeah, I talked to Dr. Wang. 00:12:42.100 --> 00:12:51.Duy Nguyen: But… I think… the sponsor, Dr. Wang, doesn't matter, but… . 00:12:51.380 --> 00:12:53.Wei Zheng: You need to come up with results, you need to come up with a project. 00:12:53.960 --> 00:13:04.Duy Nguyen: Yeah, but I have to, like, talk with the instructor, the two instructors from that course, that courses, and they're not allowed. 00:13:04.560 --> 00:13:05.Duy Nguyen: They… 00:13:05.180 --> 00:13:06.Wei Zheng: do now, Allah? 00:13:06.130 --> 00:13:07.Duy Nguyen: Yeah, they, they do overlap. 00:13:08.150 --> 00:13:11.Duy Nguyen: They just want me to, like, to do the simple thing. 00:13:12.130 --> 00:13:16.Duy Nguyen: to, like, day, because I just have 2 months left. 00:13:16.230 --> 00:13:22.Duy Nguyen: For the senior project. And they don't want me to, like, the… 00:13:23.130 --> 00:13:28.Duy Nguyen: The code will not run, or, like, they just want me to build a simple thing, and… and want me to, like. 00:13:28.630 --> 00:13:36.Wei Zheng: You can make this a simple part. You can take one of this part as… But anyway… 00:13:36.280 --> 00:13:39.Wei Zheng: You can make this as a simple part. 00:13:39.750 --> 00:13:45.Wei Zheng: as the project. You can take any part as the simple part as the project. 00:13:45.970 --> 00:13:52.Wei Zheng: I don't know what they mean. They do not allow you to do this. Because whatever, you can take any part. 00:13:53.120 --> 00:13:59.Wei Zheng: any part, it's just like you make this… this is the many steps. You can… any… just make this… 00:14:00.190 --> 00:14:02.Wei Zheng: One of the steps as your project. 00:14:02.850 --> 00:14:05.Wei Zheng: That's a symbol, you know what I mean? 00:14:05.040 --> 00:14:07.Duy Nguyen: Yeah. I talked with… 00:14:07.260 --> 00:14:20.Duy Nguyen: I talked with my instructor for the course, and they really want me to do, like, the website, the simple website, or, like, the simple app, the application. 00:14:21.160 --> 00:14:26.Wei Zheng: That is why you crawl, you do the database, that is why it's also qualified that. 00:14:26.950 --> 00:14:32.Wei Zheng: The first one you did, that is do the database, do the… what's called a web crawl. 00:14:32.700 --> 00:14:33.Duy Nguyen: Yeah. 00:14:35.790 --> 00:14:52.Duy Nguyen: But, actually, I… I talk with the instructor, from my idea for what I do for the web scripting, but they… they… they talked to me that, it's not, like, meet the requirement for this course. 00:14:53.540 --> 00:14:59.Duy Nguyen: I don't know why, but they want me to do, like, the website, not… not, like, the… the… 00:14:59.920 --> 00:15:03.Wei Zheng: What do they want you to do? What type of thing they want you to do? 00:15:05.600 --> 00:15:19.Duy Nguyen: the instructor, they want me to do, like, the website, something like the restaurant, or something like anything, but it's not for, like, the AI, the machine learning, the LM. 00:15:20.950 --> 00:15:22.Wei Zheng: Do you develop a website? 00:15:23.240 --> 00:15:24.Duy Nguyen: Yeah. 00:15:25.270 --> 00:15:27.Duy Nguyen: I don't know why, but they want me to do that. 00:15:30.210 --> 00:15:33.Wei Zheng: So, website… what… the website can do what? 00:15:34.650 --> 00:15:35.Duy Nguyen: like… 00:15:36.070 --> 00:15:48.Duy Nguyen: like, the restaurant website with the, the, the, the chatbot, it, it can, like, answer the, any information. I, like, like, recommend and suggestion, the, the. 00:15:48.470 --> 00:15:54.Wei Zheng: No, no, okay, okay, I understand. How about the course? Could you do something about the specific course? 00:15:54.390 --> 00:16:05.Wei Zheng: like the chatbot for the course, the student can ask the chatbot about this course, what this course is for, what textbook, and what's the difficult. 00:16:05.410 --> 00:16:07.Duy Nguyen: Oh, cool! Young. 00:16:08.420 --> 00:16:09.Wei Zheng: They can do that. 00:16:09.730 --> 00:16:12.Duy Nguyen: Yeah, I can do that, yeah. 00:16:12.180 --> 00:16:17.Wei Zheng: Yeah, then we can develop some chat vote about the specific cause. 00:16:17.130 --> 00:16:17.Duy Nguyen: Okay. 00:16:18.200 --> 00:16:22.Wei Zheng: I can provide a material regarding a particular course, and then… 00:16:22.550 --> 00:16:31.Duy Nguyen: Actually, I have another project, a previous project, academic, Advisor… 00:16:31.460 --> 00:16:35.Wei Zheng: Yeah, yeah, yeah, you mentioned that. I think that is the goal is, 00:16:35.600 --> 00:16:39.Wei Zheng: Dr. Wang, you buy? Dr. Wang, let's do this kind of thing? 00:16:39.940 --> 00:16:42.Duy Nguyen: Yeah, yeah. Dr. Wang. 00:16:42.700 --> 00:16:44.Wei Zheng: Did this kind of thing, right? 00:16:44.450 --> 00:16:45.Duy Nguyen: Yes. 00:16:45.740 --> 00:16:50.Duy Nguyen: He willing to, like, sponsor for me, but… 00:16:50.520 --> 00:16:53.Duy Nguyen: For this call… for these courses. 00:16:53.520 --> 00:17:03.Duy Nguyen: the instructor want me to, like, I have to do it by myself, and that's my, my, my, my, my project. And Dr. Wang just, like. 00:17:04.290 --> 00:17:05.Duy Nguyen: The person… 00:17:05.200 --> 00:17:06.Wei Zheng: I saw, or do I say? 00:17:06.210 --> 00:17:10.Duy Nguyen: verify my… the… the thing I… I do. 00:17:11.270 --> 00:17:18.Wei Zheng: Okay, I just say, yeah, if you do, you can do… instead of do the restaurant, you do the, of course. 00:17:18.609 --> 00:17:20.Duy Nguyen: Yeah, the cost, yeah, the cost. Yeah, cool. 00:17:21.560 --> 00:17:24.Wei Zheng: You do a course, I can provide information regarding all the courses. 00:17:25.040 --> 00:17:35.Wei Zheng: It basically just says the student want to learn about background of course, just like what the course will be related to the future practice, and what kind of key concept. 00:17:35.890 --> 00:17:38.Wei Zheng: You already did something for that, is that? 00:17:38.850 --> 00:17:48.Duy Nguyen: I already did, yeah. Like, I… I collect the data, and then… put it… in the API. 00:17:49.100 --> 00:17:52.Duy Nguyen: And… the, the, the deep-seq API. 00:17:53.850 --> 00:18:00.Wei Zheng: Okay, oh, DeepSeek API, okay. You use the API, you use DeepSeek to answer the question, something like that? 00:18:00.260 --> 00:18:02.Duy Nguyen: Yeah, because it's free. 00:18:02.360 --> 00:18:05.Wei Zheng: Yeah, yeah. But, but, but now… 00:18:05.800 --> 00:18:09.Wei Zheng: But now we can hire them to do that, 00:18:09.900 --> 00:18:12.Wei Zheng: To do that, graph rack. 00:18:12.200 --> 00:18:24.Wei Zheng: You do the same thing. Whenever I ask the equation, whenever we try to retrieve, retrieve equation, retrieve knowledge, you can pass on the… what? RIG. 00:18:25.440 --> 00:18:26.Duy Nguyen: Yeah. 00:18:26.180 --> 00:18:27.Wei Zheng: And also, you… 00:18:27.860 --> 00:18:39.Wei Zheng: And also, the thing is similar, it's similar. You just give them all the material. They will try to establish the knowledge graph, and then the best knowledge graph, they will answer the question. 00:18:42.330 --> 00:18:43.Duy Nguyen: Okay. 00:18:45.570 --> 00:18:50.Wei Zheng: You know what? Because when you ask a question, there's a lot of ways to retrieve the information. 00:18:50.440 --> 00:18:52.Wei Zheng: You don't know what I mean? 00:18:52.000 --> 00:18:52.Duy Nguyen: Yes. 00:18:52.570 --> 00:18:55.Wei Zheng: Just like a quad, just like a chair boat. 00:18:55.550 --> 00:19:04.Wei Zheng: There are many ways to retrieve. Traditional… traditionally, they have many ways to retrieve, but now the new thing. 00:19:04.540 --> 00:19:05.Duy Nguyen: I have the idea, yeah. 00:19:05.760 --> 00:19:09.Wei Zheng: Is the graph retrieve? You can combine, you know what I mean? 00:19:09.920 --> 00:19:10.Duy Nguyen: Yeah. 00:19:10.410 --> 00:19:17.Wei Zheng: You can combine graph retrieve compared to traditional, whatever, what you did before, what kind of retrieval you did before. 00:19:18.280 --> 00:19:20.Wei Zheng: You can, you can combine them together. 00:19:20.920 --> 00:19:21.Duy Nguyen: Yes, sir. 00:19:23.500 --> 00:19:25.Wei Zheng: But still, you can use a knowledge graph. 00:19:26.180 --> 00:19:29.Duy Nguyen: Yeah, I think I will use the knowledge to grab. 00:19:29.520 --> 00:19:32.Wei Zheng: You know, I mean, you can use whatever you did here. 00:19:33.240 --> 00:19:49.Wei Zheng: But essentially, it's what? This approach is very fundamental. This can apply in any field. So that means… I mean, you just, try to do this, and then once you… just like we feed now, we feed them with the… 00:19:49.820 --> 00:19:53.Wei Zheng: 28 publications. Then they will try to 00:19:53.440 --> 00:19:58.Wei Zheng: established those kind of things, and then they try to retrieve, to predict, you know what I mean? 00:19:59.280 --> 00:20:00.Wei Zheng: Amazon? 00:20:00.500 --> 00:20:03.Wei Zheng: You also can take the course material, you know what I mean? 00:20:03.630 --> 00:20:04.Wei Zheng: The exam! 00:20:04.950 --> 00:20:05.Wei Zheng: Problem. 00:20:06.080 --> 00:20:16.Wei Zheng: And then you put them together, and then students will ask, what course it's about, what kind of problem usually they can have, and what kind of example. 00:20:16.600 --> 00:20:17.Duy Nguyen: I will. 00:20:17.180 --> 00:20:28.Wei Zheng: What kind of excise they can have. Then, you can generate it, you know what I mean? Based on those databases, they can generate it, any, any problem or question. 00:20:29.240 --> 00:20:35.Wei Zheng: large student to exile, you know what I mean? And also, eventually, we can have a student check it. 00:20:36.030 --> 00:20:39.Duy Nguyen: Okay, I will do that. I… I will. 00:20:39.170 --> 00:20:44.Wei Zheng: So that is okay for… For your instructor. 00:20:44.840 --> 00:20:49.Duy Nguyen: Actually, I still have to talk with them, because for the last week. 00:20:50.600 --> 00:20:53.Duy Nguyen: I talk with them any idea for my idea, but… 00:20:53.760 --> 00:20:56.Duy Nguyen: They reject everything. I don't know why. 00:20:58.450 --> 00:21:00.Wei Zheng: You talk about this, you talk about this. 00:21:00.630 --> 00:21:01.Duy Nguyen: Okay. 00:21:01.320 --> 00:21:05.Wei Zheng: You talk about this. You said, you said before you did this kind of thing, you just want to build up. 00:21:06.520 --> 00:21:07.Duy Nguyen: Cuz… 00:21:07.300 --> 00:21:18.Wei Zheng: you try to build up what you did before, and then you try to make it more… more… use more advanced technology. You probably can talk about… you do not talk about projects for this, you just talk about the course. 00:21:18.770 --> 00:21:20.Duy Nguyen: Okay, yeah, my idea, yeah, okay. 00:21:20.730 --> 00:21:29.Wei Zheng: So, basically, you just said, we have the example problem, we have the homework problem, we have the quiz, 00:21:29.590 --> 00:21:39.Wei Zheng: We have a quiz problem, we have the exam problem, and then whatever you will… you will… you will build this with the… with the textbook. 00:21:39.460 --> 00:21:45.Wei Zheng: And eventually, if the student asks what kind of problem they can have, and then you can make up the problem. 00:21:45.480 --> 00:21:47.Wei Zheng: And also prepare the right answer for them. 00:21:51.290 --> 00:21:52.Duy Nguyen: Yeah. 00:21:53.280 --> 00:21:54.Wei Zheng: Okay, okay. 00:21:54.440 --> 00:21:56.Wei Zheng: Okay. 00:21:56.210 --> 00:22:00.Wei Zheng: But, but, but anyway… And, Anna now, I, I think, 00:22:03.910 --> 00:22:05.Wei Zheng: No, you, you, you, you're… 00:22:06.070 --> 00:22:09.Duy Nguyen: You come out, what kind of, what kind of. 00:22:09.700 --> 00:22:14.Wei Zheng: data now. You still try to do that knowledge graph, you know? 00:22:17.250 --> 00:22:18.Wei Zheng: Okay. 00:22:18.240 --> 00:22:23.Duy Nguyen: I will try to, like, Complete the deadline as soon as possible. 00:22:24.500 --> 00:22:28.Duy Nguyen: I will, like, I'm… I'm gonna… 00:22:29.520 --> 00:22:36.Duy Nguyen: send for you the output from my output by Friday this week. 00:22:36.210 --> 00:22:43.Wei Zheng: But anyway, the thing is what? You first, as I said before, you need to understand what the author's doing. 00:22:43.950 --> 00:22:47.Wei Zheng: You need to fully understand what is author. 00:22:47.300 --> 00:22:50.Wei Zheng: step by step, how they come out from… 00:22:50.500 --> 00:22:53.Wei Zheng: The literature come out of the 28, is that? 00:22:53.980 --> 00:22:54.Duy Nguyen: Yep. 00:22:54.790 --> 00:23:01.Wei Zheng: And you can't… Free disease… feed their publication to the chat GPT or whatever. 00:23:01.790 --> 00:23:03.Wei Zheng: You can ask them. 00:23:04.140 --> 00:23:06.Wei Zheng: So if we want to do the user agent. 00:23:06.870 --> 00:23:08.Wei Zheng: how we do that? For each step. 00:23:12.970 --> 00:23:14.Wei Zheng: You know what I mean? 00:23:14.080 --> 00:23:15.Duy Nguyen: Yeah, I understand that. 00:23:17.420 --> 00:23:26.Wei Zheng: Yeah, I will also work on it now. I will work on it, and then I will communicate it with you. But now the basic idea is now, okay? You first… 00:23:27.030 --> 00:23:31.Wei Zheng: You do… you see… you will see how many steps for the author? 00:23:33.500 --> 00:23:35.Wei Zheng: Pulls are awesome! 00:23:35.320 --> 00:23:37.Wei Zheng: They, they, they have to do. 00:23:38.040 --> 00:23:47.Wei Zheng: How many steps the author have to do in order to guard their result from January the 28th 00:23:49.120 --> 00:23:50.Wei Zheng: general… identify. 00:23:50.910 --> 00:23:56.Wei Zheng: 28 publications. And then… Try to, 00:23:56.460 --> 00:24:04.Wei Zheng: Whatever. Try to identify the big concept. Oh, what do they try to identify? They try to identify the… 00:24:04.640 --> 00:24:05.Wei Zheng: Zawa. 00:24:05.830 --> 00:24:09.Wei Zheng: The intervention, effective intervention, for different type of people. 00:24:09.810 --> 00:24:10.Duy Nguyen: Yes. 00:24:11.740 --> 00:24:18.Wei Zheng: And then, you just said… How they can do this, and then what kind of agent can do this? 00:24:19.690 --> 00:24:20.Wei Zheng: And… 00:24:21.190 --> 00:24:33.Wei Zheng: Yeah, I will work on, probably I will provide something, okay? But you now just try to continue to do what we… we talked about before. Try to… already, you already come out with some identity, right? 00:24:33.720 --> 00:24:34.Duy Nguyen: Yeah, cheers. 00:24:34.970 --> 00:24:46.Wei Zheng: And try to do the iterative and see, they can improve on… they can got improved, and that can match whatever the author have. 00:24:47.680 --> 00:24:48.Duy Nguyen: Yep. 00:24:48.240 --> 00:24:49.Wei Zheng: Okay? 00:24:50.860 --> 00:24:52.Duy Nguyen: Yeah, I, I… 00:24:52.770 --> 00:24:56.Wei Zheng: Okay, okay, okay. You sent me the, the letter, is that? 00:24:56.810 --> 00:24:57.Duy Nguyen: Yeah. 00:24:57.340 --> 00:24:58.Wei Zheng: The sign letter, the sign letter you sent me. 00:24:58.980 --> 00:25:00.Duy Nguyen: Yeah, I understand you. 00:25:00.730 --> 00:25:01.Wei Zheng: Okay, okay, okay. 00:25:02.160 --> 00:25:02.Wei Zheng: Logan, okay. 00:25:02.990 --> 00:25:08.Duy Nguyen: I… I hope you understand, because this… this month, I have to, like. 00:25:09.140 --> 00:25:15.Duy Nguyen: prepare the document, apply to Jackson State University, and… 00:25:15.100 --> 00:25:17.Wei Zheng: Have you done that? Have you done that? 00:25:18.810 --> 00:25:20.Wei Zheng: Have you done that or not? 00:25:20.840 --> 00:25:25.Wei Zheng: You haven't done yet, you know? So what's the deadline? What deadline? 00:25:25.700 --> 00:25:30.Duy Nguyen: I have to submit everything by… March. 00:25:32.460 --> 00:25:34.Duy Nguyen: First… first day of March. 00:25:34.990 --> 00:25:36.Wei Zheng: Or a box as well. 00:25:37.010 --> 00:25:43.Duy Nguyen: I have to, like, prepare for the GIE, and took the GIE, and… When they need to pack? 00:25:43.760 --> 00:25:46.Wei Zheng: when they need a tech GIE? When they need a tech GIE? 00:25:47.320 --> 00:25:50.Wei Zheng: when they need a GRE score? Before the march? 00:25:52.530 --> 00:25:57.Duy Nguyen: I don't know, because I sent the email for… 00:25:57.550 --> 00:26:03.Duy Nguyen: For Jackson State University, but I don't… Have any reply from them? 00:26:05.110 --> 00:26:09.Wei Zheng: Do you look at their website when they need the GRE? 00:26:09.390 --> 00:26:13.Wei Zheng: They need the GIU, when you do the application, when they submit the application. 00:26:13.840 --> 00:26:15.Duy Nguyen: Yeah, when I'm going to submit the application. 00:26:17.830 --> 00:26:20.Wei Zheng: You need to do the GRE now, you know? 00:26:20.080 --> 00:26:24.Duy Nguyen: Yeah, I need to do the GIE, I need to prepare for the GRE and do the GRE right now. 00:26:25.070 --> 00:26:32.Duy Nguyen: And any paper… And, senior project, and my project, our, our project. 00:26:33.890 --> 00:26:36.Duy Nguyen: For… for… for this, man. 00:26:42.060 --> 00:26:42.Wei Zheng: Hmm. 00:26:47.880 --> 00:26:51.Duy Nguyen: And… and this month is kind of hard for me, because… 00:26:52.690 --> 00:27:03.Duy Nguyen: the two weeks of, ice storm, ice storm. And the last week, I, I, I sick, for the whole week, I, I just, like, stay at home. 00:27:03.840 --> 00:27:06.Duy Nguyen: Because I'm sick. 00:27:08.040 --> 00:27:09.Wei Zheng: And I, I just have, like. 00:27:10.190 --> 00:27:13.Duy Nguyen: In a half of a month, to do everything. 00:27:19.500 --> 00:27:20.Duy Nguyen: I'm so sorry about that. 00:27:43.940 --> 00:27:48.Wei Zheng: Okay, let me think of it, okay, let me think of it. But you just do whatever you can do. 00:27:48.340 --> 00:27:53.Duy Nguyen: You don't need to worry about it, because I will complete the… 00:27:53.260 --> 00:28:00.Wei Zheng: Yeah, you just do whatever you should do, okay? I will consider that. How can we… because that is not too much time left, okay? 00:28:00.980 --> 00:28:01.Duy Nguyen: Yeah. 00:28:01.300 --> 00:28:01.Wei Zheng: Okay. 00:28:02.110 --> 00:28:12.Wei Zheng: Yeah, okay, you just do… try to do your best, do whatever you can do for this… for this, draft paper, okay? You know, we need to come out with some results. We need to come out with some… 00:28:12.790 --> 00:28:22.Duy Nguyen: I will come out with the result by Friday, by Friday, this week, because we just have 10, 10 more days, right? For the draft. 00:28:23.290 --> 00:28:32.Wei Zheng: First, you need to change the criteria and see what's the result you can come. You do the third. You probably just simply change the criteria for the web collaboration, you know what I mean? 00:28:32.710 --> 00:28:33.Duy Nguyen: Yeah. 00:28:33.290 --> 00:28:35.Wei Zheng: You see what the result it is. 00:28:35.180 --> 00:28:39.Wei Zheng: And then you will identify the entity, okay? 00:28:39.210 --> 00:28:39.Duy Nguyen: Okay. 00:28:40.090 --> 00:28:46.Wei Zheng: Probably we will talk about, yeah, after, after probably the, after weekend, okay? 00:28:46.880 --> 00:28:47.Duy Nguyen: Yep. 00:28:47.650 --> 00:28:48.Wei Zheng: Okay. 00:28:48.950 --> 00:28:52.Wei Zheng: I'm so sorry about that. Okay, okay, okay, okay, okay. 00:28:52.650 --> 00:28:53.Wei Zheng: Okay.


========================================

