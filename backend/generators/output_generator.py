import os
import json

def generate_output(client_id, result):
    print("[GENERATOR] Generating output...")

    output_dir = f"../storage/clients/{client_id}/outputs"

    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, "result.json")

    with open(output_path, "w") as f:
        json.dump(result, f, indent=4)

    return output_path
