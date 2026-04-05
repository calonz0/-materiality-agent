import requests


class LLMClient:

    def __init__(self):
        self.host = "http://127.0.0.1:11434"
        self.model = "qwen2.5:3b-instruct-q4_K_M"  # 🔥 TU MODELO ACTUAL

    def generate(self, prompt):

        try:
            response = requests.post(
                f"{self.host}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False
                }
            )

            print("[LLM STATUS]", response.status_code)

            if response.status_code != 200:
                print("[LLM ERROR BODY]", response.text)
                return f"LLM error: {response.status_code}"

            data = response.json()

            print("[LLM DATA]", data)

            return data.get("response", "").strip()

        except Exception as e:
            return f"LLM connection error: {str(e)}"
