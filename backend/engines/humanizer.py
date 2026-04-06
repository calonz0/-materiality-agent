import requests

OLLAMA_URL = "http://localhost:11434/api/generate"

def humanize_response(text: str) -> str:
    prompt = f"""
Eres un asistente fiscal profesional.

Tu tarea es reescribir el siguiente mensaje de forma clara, directa y profesional en español.

Reglas:
- usa espanol siempre
- Máximo 3 oraciones
- No agregues información extra
- No expliques de más
- No uses lenguaje informal
- Sé directo y preciso

Mensaje:
{text}

Respuesta:
"""

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()
        return result.get("response", text).strip()

    except Exception as e:
        print("[HUMANIZER ERROR]", e)
        return text
