def format_citations(citations):

    res = ""

    for claim_idx in citations:

        claim = citations[claim_idx]["claim"]

        res += "=======================================\n"
        res += f"Claim Index: {claim_idx}\n"
        res += f"Claim: {claim}\n"
        res += "<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"

        supportive_evidence = citations[claim_idx]["supportive_evidence"]

        for document, evidence in supportive_evidence:

            res += f"Document: {document}\n"
            res += f"Evidence: {evidence['text']}\n"
            res += f"Reason: {evidence['reason']}\n"
            res += "---------------------------------------\n"

        res += ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"

        opposing_evidence = citations[claim_idx]["opposing_evidence"]

        for document, evidence in opposing_evidence:

            res += f"Document: {document}\n"
            res += f"Evidence: {evidence['text']}\n"
            res += f"Reason: {evidence['reason']}\n"
            res += "---------------------------------------\n"

        res += "=======================================\n"

    return res
