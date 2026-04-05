from backend.engines.llm_client import LLMClient

llm = LLMClient()


def humanize_response(text):

    prompt = f"""
Eres un asistente experto en procesos fiscales y documentación empresarial.

Tu función es comunicarte con el usuario de forma:
- clara
- profesional
- amigable
- directa

⚠️ REGLAS IMPORTANTES:
- SIEMPRE responde en español
- NO cambies el significado del mensaje original
- NO agregues información que no esté en el mensaje base
- NO expliques de más
- NO uses emojis

Mensaje base:
"{text}"

Responde únicamente con el mensaje mejorado:
"""

    return llm.generate(prompt)
