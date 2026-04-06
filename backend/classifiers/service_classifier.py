import requests

def classify_operation(text: str):

    prompt = f"""
    Classify the following operation as PRODUCT or SERVICE.
    Also explain WHY clearly.

    Text:
    {text[:1000]}
    """

    res = requests.post("http://localhost:11434/api/generate", json={
        "model": "qwen2.5:3b-instruct-q4_K_M",
        "prompt": prompt,
        "stream": False
    })

    data = res.json()
    response = data.get("response", "")

    print("[LLM RAW RESPONSE]:", response)

    if "service" in response.lower():
        op_type = "SERVICE"
    else:
        op_type = "PRODUCT"

    return {
        "operation_type": op_type,
        "justification": response
    }
