def build_context(
    client_id,
    invoice_data,
    classification,
    client_documents,
    required_documents
):
    """
    Construye el contexto completo del sistema
    """

    print("[CONTEXT] Building context...")

    return {
        "client_id": client_id,
        "invoice_data": invoice_data,
        "classification": classification,
        "client_documents": client_documents,
        "required_documents": required_documents
    }
