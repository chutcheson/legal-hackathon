import json

from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage

from prompts import claims_prompt, classification_prompt

# Get JSON list of claims from text
def claims(text):
    
    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create a list of messages
    messages = [
        SystemMessage(content="You are a legal expert, skilled at parsing arugments into their respective claims."),
        claims_prompt.format(argument=text)
    ]

    # Get the JSON response from the chat model
    res = chat(messages).content

    # Convert JSON response into a Python object
    res = json.loads(res)

    return res

def evidence_classification(evidence):

    # Instantiate the chat model 
    chat = ChatOpenAI()

    # Create a list of messages
    messages = [
        SystemMessage(content="You are a legal expert, skilled at classifying evidence."),
        classification_prompt.format(evidence=evidence)
    ]

    # Get the JSON response from the chat model
    res = chat(messages).content

    # Convert JSON response into a Python object
    res = json.loads(res)

    print(res)

    return res


