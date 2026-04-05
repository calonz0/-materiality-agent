from backend.engines.llm_client import LLMClient


def classify_operation(invoice_data):

    text = str(invoice_data)

    prompt = f"""
You are an expert financial classifier.

Classify this invoice as PRODUCT or SERVICE.

Rules:
- PRODUCT = physical goods
- SERVICE = consulting, maintenance, digital services

Respond ONLY with:
PRODUCT or SERVICE

Invoice:
{text}
"""

    llm = LLMClient()
    response = llm.generate(prompt)

    result = response.strip().upper()

    print("[AI RAW RESPONSE]", result)

    if "SERVICE" in result:
        return "SERVICE"
    elif "PRODUCT" in result:
        return "PRODUCT"

    return "SERVICE"

