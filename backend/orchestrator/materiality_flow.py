from backend.classifiers.service_classifier import classify_operation
from backend.document_request.document_checker import get_required_documents
from backend.ingestion.invoice_parser import parse_invoice
from backend.interaction.data_collector import collect_client_documents


class MaterialityFlow:

    def __init__(self, client_id):
        self.client_id = client_id
        self.state = "START"

    def update_state(self, new_state):
        print(f"[FLOW] {self.state} → {new_state}")
        self.state = new_state

    def run(self, file_path):

        print("[FLOW] START")

        # STEP 1: Parse invoice
        invoice_data = parse_invoice(file_path)
        self.update_state("INVOICE_PARSED")

        # STEP 2: Classify
        classification = classify_operation(invoice_data)
        print(f"[FLOW] Classification: {classification}")
        self.update_state("CLASSIFIED")

        # STEP 3: Request documents
        required_docs = get_required_documents(classification)
        collect_client_documents(required_docs)
        self.update_state("WAITING_CLIENT_DOCS")

        return {
            "status": "waiting_documents",
            "required_docs": required_docs,
            "classification": classification
        }
