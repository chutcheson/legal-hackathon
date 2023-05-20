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

    # Instantiate collection of evidence
    evidence_collection = create_collection()

    # Find evidence for each claim
    for claim in argument_claims:

        # Get relevant documents
        results = collection.query(
        query_texts=[claim],
        n_results=5
        )

        # Get supporting and opposing evidence
        classification = evidence_classification(results)

