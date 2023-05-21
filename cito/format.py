def format_citations(citations):

    # create return string
    res = "" 

    # loop over claims
    for claim_idx in citations:

        # get the claim
        claim = citations[claim_idx]["claim"]


        # add the claim metadata to the string 
        res += "=======================================\n\n"
        res += f"Claim Index: {claim_idx}\n"
        res += f"Claim: {claim}\n\n"

        # get the supportive evidence
        res += "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< SUPPORTIVE\n"
        supportive_evidence = citations[claim_idx]["supportive_evidence"]

        # loop over the supportive evidence
        for document, evidence in supportive_evidence:

            # write out the supportive evidence element
            res += f"Document: {document}\n"
            res += f"Evidence: {evidence['text']}\n"
            res += f"Reason: {evidence['reason']}\n"
            res += "---------------------------------------\n"


        # get the opposing evidence
        res += "OPPOSING >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"
        opposing_evidence = citations[claim_idx]["opposing_evidence"]

        # loop over the opposing evidence
        for document, evidence in opposing_evidence:

            # write out the opposing evidence element
            res += f"Document: {document}\n"
            res += f"Evidence: {evidence['text']}\n"
            res += f"Reason: {evidence['reason']}\n"
            res += "---------------------------------------\n"

        # add newlines between documents
        res += "\n\n\n\n"

    return res
