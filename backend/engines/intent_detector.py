from backend.engines.llm_client import LLMClient

llm = LLMClient()


def detect_intent(message):

    msg = message.lower().strip()

    # 🔥 REGLAS RÁPIDAS (CONFIABLES)
    if msg in ["hi", "hello", "hola", "hey"]:
        return "greeting"

    if "upload" in msg or "subi" in msg or "uploaded" in msg:
        return "upload_files"

    if "what" in msg or "how" in msg or "?" in msg:
        return "question"

    # 🔥 FALLBACK A LLM (solo si no sabemos)
    prompt = f"""
Classify the intent of this message into ONE word:

greeting
upload_files
question
unknown

Message:
"{message}"

Return ONLY one word.
"""

    result = llm.generate(prompt).lower()

    if "greeting" in result:
        return "greeting"
    elif "upload" in result:
        return "upload_files"
    elif "question" in result:
        return "question"

    return "unknown"
