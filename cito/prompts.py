from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

claims_prompt_template = """
Argument: {argument}

Given the argument above. Break the argument into its claims.

Return the claims as a JSON list.

["Claim1", "Claim2", "Claim3"...]

Example argument: Argument: The uprising in Libya started a wave of social protest. These social protests are dangerous to the United States and its interests. Hillary Clinton wrote an email to George Bush detailing these concerns in 2007.

Example response: ["The uprising in Libya started a wave of social protest.", "These social protests are dangerous to the United States and its interests.", "Hillary Clinton wrote an email to George Bush detailing these concerns in 2007."]
"""

claims_prompt = HumanMessagePromptTemplate.from_template(claims_prompt_template)

classification_prompt_template = """
Claim: {claim}

Evidence: {evidence}

Given the JSON objects representing evidence provided above, determine whether any of the evidence supports or opposes the claim.

Return the classification as a JSON object.

{{
    "Supportive" : [
        {{ 
            "email_id" : "insert email id here",
            "text" : "insert text supporting the claim here"
            "reason" : "insert reason for classification here"
        }}, ...
    ],

    "Opposing" : [
        {{
            "email_id" : "insert email id here",
            "text" : "insert text opposing the claim here"
            "reason" : "insert reason for classification here"
        }}, ...
    ]
}}
"""

classification_prompt = HumanMessagePromptTemplate.from_template(classification_prompt_template)
