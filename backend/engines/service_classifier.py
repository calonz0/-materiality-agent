from backend.engines.llm_client import LLMClient

llm = LLMClient()


def classify_operation(text):

    prompt = f"""
Eres un experto en análisis fiscal.

Tu tarea es clasificar una operación como:

PRODUCT
o
SERVICE

⚠️ REGLAS:
- PRODUCT: venta de bienes físicos
- SERVICE: prestación de servicios, consultoría, trabajos, etc.

⚠️ IMPORTANTE:
- Responde SOLO con una palabra:
PRODUCT
o
SERVICE
- No expliques nada
- No agregues texto extra

---

Texto a analizar:
"{text}"

---

Respuesta:
"""

    result = llm.generate(prompt).strip().upper()

    if "PRODUCT" in result:
        return "PRODUCT"
    elif "SERVICE" in result:
        return "SERVICE"

    return "UNKNOWN"
