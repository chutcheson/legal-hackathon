import os

from cito.queries import claims, evidence_classification
from cito.load_documents import create_collection

def cite(argument_path): 

    # Convert the relative path to an absolute path
    argument_path = os.path.expanduser(argument_path)

    # Read in argument
    with open(argument_path) as f:
        argument = f.read()

    # Convert argument into claims
    argument_claims = claims(argument)

    print(argument_claims)

    # Instantiate collection of evidence
    evidence_collection = create_collection()

    # Create a dictionary to store claims and their evidence
    res = {}

    # Find evidence for each claim
    for index, claim in enumerate(argument_claims):

        # Create a try / except block to handle errors
        try:

            # Get relevant documents
            documents = evidence_collection.query(
            query_texts=[claim],
            n_results=5
            )['documents'][0]

            # Convert results into single string
            document_text = "".join(documents)

            # Get supporting and opposing evidence
            classification = evidence_classification(claim, document_text)

            print(classification)

            # Create entry for claim in res dictionary
            res[index] = { "claim" : claim }

            # Update entry with classification information
            res[index].update(classification)

        except Exception as e:

            print(e)

            pass

    return res

