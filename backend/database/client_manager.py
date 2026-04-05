import json
import os

BASE_PATH = os.path.dirname(__file__)
CLIENTS_FILE = os.path.join(BASE_PATH, "clients.json")


def load_clients():
    if not os.path.exists(CLIENTS_FILE):
        return {"clientes": []}

    with open(CLIENTS_FILE, "r") as f:
        return json.load(f)


def save_clients(data):
    with open(CLIENTS_FILE, "w") as f:
        json.dump(data, f, indent=2)


def find_client(client_id):
    data = load_clients()

    for client in data["clientes"]:
        if client["id"] == client_id:
            return client

    return None


def create_client(client_id):
    data = load_clients()

    new_client = {
        "id": client_id,
        "documentos": {}
    }

    data["clientes"].append(new_client)
    save_clients(data)

    return new_client
