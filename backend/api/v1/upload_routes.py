from fastapi import APIRouter, UploadFile, File
from typing import List
import os

from backend.orchestrator.materiality_flow import MaterialityFlow

router = APIRouter()

BASE_DIR = "backend/storage/clients/test_client"


@router.post("/upload")
async def upload_files(files: List[UploadFile] = File(...)):

    upload_dir = os.path.join(BASE_DIR, "uploads")
    os.makedirs(upload_dir, exist_ok=True)

    saved_files = []

    for file in files:
        file_path = os.path.join(upload_dir, file.filename)

        with open(file_path, "wb") as f:
            f.write(await file.read())

        saved_files.append(file_path)

    print(f"[UPLOAD] Files saved: {saved_files}")

    # 🔥 DETECTAR SI ES FACTURA (XML)
    xml_files = [f for f in saved_files if f.endswith(".xml")]

    if xml_files:
        flow = MaterialityFlow("test_client")
        result = flow.run(xml_files[0])

        return {
            "stage": "WAITING_CLIENT_DOCS",
            "message": "Upload required client documents",
            "required_docs": result["required_docs"],
            "classification": result["classification"]
        }

    else:
        return {
            "stage": "CLIENT_DOCS_RECEIVED",
            "message": "Client documents uploaded successfully",
            "files": saved_files
        }
