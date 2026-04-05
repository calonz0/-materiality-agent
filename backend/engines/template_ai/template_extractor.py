from engines.llm_client import LLMClient

TEMPLATE_PROMPT = """
You are an expert legal and financial document analyst.

Your task is to convert a real-world document into a reusable template.

Instructions:
- Identify variable information (names, dates, amounts, RFCs, addresses, roles, etc.)
- Replace them with placeholders using this format: {{field_name}}
- Keep the original wording and structure as much as possible
- Use meaningful field names (empresa, cliente, representante, monto, fecha, etc.)

Return ONLY valid JSON:

{{
  "template": "full text with placeholders",
  "fields": ["field1", "field2"]
}}

DOCUMENT:
{document}
"""

class TemplateExtractor:

    def __init__(self):
        self.llm = LLMClient()

    def extract_template(self, text: str) -> str:
        prompt = TEMPLATE_PROMPT.format(document=text)
        return self.llm.generate(prompt)
