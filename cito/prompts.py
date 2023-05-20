from langchain.prompts.chat import (
    ChatPromptTemplate,
    SystemMessagePromptTemplate,
    AIMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

claims_prompt_text = """
Argument: {argument}

Given the argument above. Break the argument into its claims.

Return the claims as a JSON list.

["Claim1", "Claim2", "Claim3"...]

Example argument: Argument: The uprising in Libya started a wave of social protest. These social protests are dangerous to the United States and its interests. Hillary Clinton wrote an email to George Bush detailing these concerns in 2007.

Example response: ["The uprising in Libya started a wave of social protest.", "These social protests are dangerous to the United States and its interests.", "Hillary Clinton wrote an email to George Bush detailing these concerns in 2007."]
"""

claims_prompt = HumanMessagePromptTemplate(input_variables=["argument"])
