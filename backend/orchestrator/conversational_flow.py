import os

from backend.engines.humanizer import humanize_response
from backend.engines.intent_detector import detect_intent
from backend.classifiers.service_classifier import classify_operation


def get_uploaded_files(client_id):
    path = f"backend/storage/clients/{client_id}/uploads"

    if not os.path.exists(path):
        return []

    return os.listdir(path)


def run_flow(client_id, message, session):

    print("🔥 FLOW AUTOMÁTICO 🔥")

    # 🔥 DETECTAR INTENCIÓN
    intent = detect_intent(message)
    print(f"[INTENT] {intent}")

    # 🔥 OBTENER ARCHIVOS
    files = get_uploaded_files(client_id)

    # ============================
    # 🔹 GREETING
    # ============================
    if intent == "greeting":
        return humanize_response(
            "Hola, estoy aquí para ayudarte a generar documentos de materialidad. Por favor sube tu factura para comenzar."
        )

    # ============================
    # 🔹 SIN ARCHIVOS
    # ============================
    if not files:
        return humanize_response(
            "No detecto archivos aún. Por favor sube tu XML y PDF para iniciar el proceso."
        )

    # ============================
    # 🔹 CON ARCHIVOS → CLASIFICACIÓN
    # ============================
    print(f"[FILES DETECTED] {files}")

    # 🔥 AQUÍ DESPUÉS VAMOS A LEER XML REAL
    sample_text = "Factura por servicios de consultoría tecnológica"

    operation_type = classify_operation(sample_text)

    print(f"[CLASSIFICATION] {operation_type}")

    # ============================
    # 🔹 RESULTADOS SEGÚN TIPO
    # ============================
    if operation_type == "PRODUCT":
        return humanize_response(
            "Detecté que esta operación corresponde a la venta de un producto. Procederemos con la generación de los documentos necesarios."
        )

    elif operation_type == "SERVICE":
        return humanize_response(
            "Detecté que esta operación corresponde a un servicio. Procederemos con la generación de la documentación correspondiente."
        )

    # ============================
    # 🔹 FALLBACK
    # ============================
    return humanize_response(
        "No pude determinar el tipo de operación. Revisaremos la información para continuar."
    )
