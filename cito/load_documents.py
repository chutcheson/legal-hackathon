import os
import json
from copy import copy

import pandas as pd
from chromadb.config import Settings
import chromadb

def create_collection():

    # Path to the directory containing the legal materials 
    directory = "~/Projects/legal-hackathon/data/Emails.csv"

    # Expand the tilde (~) to the user's home directory
    directory = os.path.expanduser(directory)

    # Load the legal materials into a Pandas dataframe
    evidence_df = pd.read_csv(directory)[:100]

    #.sample(1000, random_state=42).reset_index(drop=True)

    # Create a Chroma client to store the emails
    chroma_client = chromadb.Client()

    # Create collection to store evidence
    evidence_collection = chroma_client.create_collection(name="evidence")

    # Create lists to store variables and metadata
    ids = []
    documents = []
    metadatas = []

    # Iterate over the evidence to store it in the database
    for record in evidence_df.to_dict(orient='records'):
        
        # Retrieve the important fields from the email record
        email_id = record['DocNumber']
        email_subject = record['ExtractedSubject']
        email_to = record['ExtractedTo']
        email_from = record['ExtractedFrom']
        email_cc = record['ExtractedCc']
        email_date_sent = record['ExtractedDateSent']
        email_text = record['ExtractedBodyText']

        # Create a smaller version of the email
        email_small = {
                "email_id": email_id,
                "email_subject": email_subject,
                "email_to": email_to,
                "email_from": email_from,
                "email_cc": email_cc,
                "email_date_sent": email_date_sent,
                "email_text": email_text
        }

        # Make a JSON string of the email
        email_string = json.dumps(email_small)

        # Save the email data for the loop
        ids.append(email_id)
        documents.append(email_string)
        del email_small['email_text']
        metadatas.append(email_small)

    evidence_collection.add(
        documents=documents,
        metadatas=metadatas,
        ids=ids
    )

    return evidence_collection
