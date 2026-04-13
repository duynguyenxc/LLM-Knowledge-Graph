from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, Field

class EntityCategory(str, Enum):
    CONTEXT = "Context"
    INTERVENTION = "Intervention"
    MECHANISM_RESOURCE = "Mechanism_Resource"
    MECHANISM_RESPONSE = "Mechanism_Response"
    OUTCOME = "Outcome"

class ContextType(str, Enum):
    E01 = "undergraduate students in medical or health care professions education"
    E02 = "students with 'low knowledge,' low clinical domain-specific knowledge, or an inability to use knowledge in a reasoning situation"
    E03 = "students with high clinical domain-specific knowledge"
    E04 = "positive student coping strategies or appropriate level of self-confidence or self-efficacy"
    E05 = "negative student coping strategies or lacking self-confidence or self-efficacy"
    E06 = "students with different levels of knowledge within a group"

class InterventionType(str, Enum):
    E07 = "an expert’s reasoning processes or thoughts are explicitly revealed and discussed"
    E08 = "instructed to use analytical reasoning alone"
    E09 = "teaching resources that allow them to make mistakes"
    E10 = "real-life scenarios, including simulation and simulated patients"
    E11 = "real cases"
    E12 = "strategies that promote knowledge retention"
    E13 = "accurate and timely feedback"
    E14 = "feedback is absent, incomplete or contains errors"
    E15 = "explicit and clear explanation of expert’s reasoning"
    E16 = "passive observation of experts without receiving explanation about their reasoning processes"
    E17 = "listen to near-peer think aloud their reasoning with the use of prompts and examples"
    E18 = "instructing to use both ‘non-analytical’ or pattern recognition and analytical or step-wise approach to reasoning"

class MechanismResourceType(str, Enum):
    E19 = "multiple relevant resources"

class MechanismResponseType(str, Enum):
    E20 = "understanding"
    E23 = "frustrated"
    E24 = "rely on non-analytical reasoning"
    E26 = "grateful for the learning experience"
    E27 = "build understanding"
    E31 = "pressure that their decision making could have a real impact"
    E32 = "fear"
    E33 = "stress"
    E34 = "pressure to perform"
    E35 = "cognitive load is increased"
    E39 = "build upon what they already know"
    E42 = "develop understanding of their successes and failures and generate plans for improvement"
    E45 = "confusion"

class OutcomeType(str, Enum):
    E21 = "insight into the reasoning process when diagnosing and managing patients"
    E22 = "positive learning experience"
    E25 = "high diagnostic accuracy"
    E28 = "positive impact on learning"
    E29 = "more complete illness scripts"
    E30 = "more accurate non-analytical reasoning"
    E36 = "poor illness script development"
    E37 = "faulty future non-analytical reasoning"
    E38 = "negative learning outcomes"
    E40 = "increased learning"
    E41 = "further engagement"
    E43 = "complete illness scripts"
    E44 = "successful non-analytical reasoning in the future"
    E46 = "increase in learning gain or outcomes, or increase in diagnostic accuracy"
    E47 = "decrease in learning gain or outcomes, or decrease in diagnostic accuracy"

class RelationType(str, Enum):
    PROVIDES = "PROVIDES"
    ENABLES = "ENABLES"
    LEADS_TO = "LEADS_TO"
    TRIGGERS = "TRIGGERS"

class Entity(BaseModel):
    id: str = Field(..., description="A unique identifier for the entity, e.g., 'E02'")
    category: EntityCategory = Field(..., description="The high-level category in the CMO framework")
    label: str = Field(..., description="The standard concept label from the Richmond KG specification")
    extracted_text: str = Field(..., description="The verbatim text span extracted from the paper")

class Relationship(BaseModel):
    source_id: str = Field(..., description="ID of the source entity")
    target_id: str = Field(..., description="ID of the target entity")
    relation_type: RelationType = Field(..., description="The type of causal link")
    evidence_quote: str = Field(..., description="The exact sentence from the paper proving this relationship")

class CMOCExtraction(BaseModel):
    record_id: str = Field(..., description="The DOI or paper ID this was extracted from")
    entities: List[Entity] = Field(default_factory=list, description="List of recognized entities")
    relationships: List[Relationship] = Field(default_factory=list, description="Causal relationships aligning with the CMO structure")

    class Config:
        schema_extra = {
            "example": {
                "record_id": "doi:10.1111/medu.14137",
                "entities": [
                    {
                        "id": "node_1",
                        "category": "Context",
                        "label": "students with 'low knowledge,' low clinical domain-specific knowledge, or an inability to use knowledge in a reasoning situation",
                        "extracted_text": "students with low knowledge"
                    }
                ],
                "relationships": [
                    {
                        "source_id": "node_1",
                        "target_id": "node_2",
                        "relation_type": "ENABLES",
                        "evidence_quote": "students with low knowledge are enabled to learn more effectively when..."
                    }
                ]
            }
        }
