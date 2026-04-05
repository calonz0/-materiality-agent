def generate_materiality(context):
    """
    Genera análisis de materialidad (simulado por ahora)
    El LLM en el futuro solo generará texto aquí.
    """

    print("[MATERIALITY] Generating materiality analysis...")

    classification = context.get("classification")

    return {
        "analysis": f"This operation was classified as {classification}.",
        "risk_level": "LOW",
        "notes": "Simulated materiality output (LLM-ready)"
    }
