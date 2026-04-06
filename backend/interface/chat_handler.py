import requests

# 🔥 ESTADO GLOBAL (simple por ahora)
FLOW_STATE = {
    "stage": "START"
}


def call_llm(prompt: str):
    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:3b-instruct-q4_K_M",
        "prompt": prompt,
        "stream": False
    })
    data = res.json()
    return data.get("response", "")


def handle_chat(data: dict):
    print("[CHAT] Incoming:", data)
    print("[FLOW STATE]:", FLOW_STATE["stage"])

    # 🔥 CONFIRMATION FLOW
    if "confirmation" in data:
        if data["confirmation"]:
            FLOW_STATE["stage"] = "CONFIRMED"
            return {
                "response": "Perfect. The operation has been confirmed. Proceeding with materiality document generation."
            }
        else:
            FLOW_STATE["stage"] = "REJECTED"
            return {
                "response": "Understood. Please clarify the operation so I can re-evaluate."
            }

    message = data.get("message", "").lower()

    # 🔥 STAGE 1 — START
    if FLOW_STATE["stage"] == "START":

        FLOW_STATE["stage"] = "WAITING_INVOICE"

        return {
            "response": "Hello. I am your Materiality Agent.\n\nTo begin the process, please upload the invoice (XML)."
        }

    # 🔥 STAGE 2 — WAITING FOR INVOICE
    if FLOW_STATE["stage"] == "WAITING_INVOICE":

        return {
            "response": "I am waiting for the invoice file. Please upload the XML to continue."
        }

    # 🔥 FALLBACK (CONTROLADO)
    prompt = f"""
    You are a Materiality Agent specialized in fiscal validation.

    You MUST:
    - Stay in role
    - Guide the user toward completing the materiality process
    - Do NOT give generic answers

    User message:
    {message}
    """

    llm_response = call_llm(prompt)

    return {
        "response": llm_response
    }
