REQUIRED_DOCS = [
    "acta_constitutiva",
    "poder_representante",
    "csf",
    "ine"
]


def validate_documents(client_documents):
    missing = []

    for doc in REQUIRED_DOCS:
        if doc not in client_documents or not client_documents[doc]:
            missing.append(doc)

    return {
        "valid": len(missing) == 0,
        "missing": missing
    }

