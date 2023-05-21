import json
from capabilities import llm, llm_inline
from typing import List

@llm
def claims(argument: str) -> List[str]:
    """
    You are a legal expert, skilled at parsing arugments into their respective claims.
    
    Given the `argument`, break the argument into a list of claims. Each claim should be independent and should contain all information necessary to understand the claim. Return the claims as a JSON list.

    Example argument: Argument: The uprising in Libya started a wave of social protest. These social protests are dangerous to the United States and its interests. Hillary Clinton wrote an email to George Bush detailing these concerns in 2007.

    Example response: ["The uprising in Libya started a wave of social protest.", "The social protests in Libya are dangerous to the United States and its interests.", "Hillary Clinton wrote an email to George Bush detailing these concerns in 2007."]
    """

from pydantic import BaseModel

class Evidence(BaseModel):    
    text: str                
    reason: str              

class SupportingAndOpposingEvidence(BaseModel):      
    supporting_evidence: List[Evidence]              
    opposing_evidence: List[Evidence]                

@llm    
def _evidence_classification(claim: str, evidence: str) -> SupportingAndOpposingEvidence:
    """
    You are a legal expert, skilled at classifying evidence. Given the input evidence, classify it into two lists called `supporting_evidence` and `opposing_evidence`, with verbatim `text` and a `reason` why the evidence supports or opposes the `claim`.
    """
    
@llm_inline(regenerate=False)
def evidence_classification(claim: str, evidence: str):
    """
    Calls `_evidence_classification` and converts it to a dict.
    """
    return _evidence_classification(claim, evidence).dict()

# if __name__ == "__main__":
#     claim = "all life on Earth is intelligently designed"
#     evidence = """\
# - Evidence for Intelligent Design:

#   - Irreducible Complexity: Certain biological systems cannot have evolved step-by-step, and must therefore have been designed by an intelligent agent. For example, the bacterial flagellum, which consists of multiple interdependent parts, would be non-functional without all of its parts.

#   - Fine-tuning: The physical constants and initial conditions of the universe appear to be finely tuned for the existence of life. This implies that an intelligent agent deliberately set these values to enable life.

#   - Information Content: DNA and other biological molecules contain a high level of specified complexity that cannot be explained by chance. This suggests that they were designed by an intelligent agent.

# - Evidence against Intelligent Design:

#   - Imperfect Design: Many biological structures and systems are imperfect and inefficient, which is not what one would expect from an intelligent designer. For example, the human eye has a blind spot, and the recurrent laryngeal nerve takes a detour that is not necessary.

#   - Common Descent: The fossil record and genetic evidence strongly support the theory of common descent, which suggests that all living organisms share a common ancestor. This contradicts the idea of separate direct creation of different life forms.

#   - Natural Explanations: Many natural processes can account for the features of the universe and life, without the need for intelligent design. For example, natural selection can explain the diversity of life, and physical laws can explain the fine-tuning of the universe.
# """    
#     print(evidence_classification(claim, evidence))
