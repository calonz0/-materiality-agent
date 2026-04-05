import json
import os

RULES_PATH = os.path.join(
    os.path.dirname(__file__),
    "../context/golden_rules.json"
)


def load_rules():
    with open(RULES_PATH, "r") as f:
        return json.load(f)


def get_client_required_documents():
    rules = load_rules()
    return rules["client_required_documents"]


def get_operation_documents(classification):
    rules = load_rules()

    if classification not in rules["operation_outputs"]:
        raise Exception("Invalid classification")

    return rules["operation_outputs"][classification]
