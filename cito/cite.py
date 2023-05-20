import os

from cito.queries import claims
from cito.load_documents import create_collection

def cite(argument_path): 

    # Convert the relative path to an absolute path
    argument_path = os.path.expanduser(argument_path)

    # Read in argument
    with open(argument_path) as f:
        argument = f.read()

    # Convert argument into claims


    # Instantiate collection of evidence
    evidence_collection = create_collection()
