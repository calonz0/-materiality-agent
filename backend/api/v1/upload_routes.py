from fastapi import APIRouter, UploadFile, File
from backend.classifiers.service_classifier import classify_operation
from backend.interface.chat_handler import FLOW_STATE

router = APIRouter()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await file.read()

    print("[UPLOAD] File received:", file.filename)

    try:
        text = content.decode(errors="ignore")
    except:
        text = str(content)

    print("[UPLOAD CONTENT PREVIEW]:", text[:200])

    # 🔥 CAMBIO DE ESTADO
    FLOW_STATE["stage"] = "INVOICE_RECEIVED"

    result = classify_operation(text)

    FLOW_STATE["stage"] = "CLASSIFIED"

    print("[FLOW STATE UPDATED]:", FLOW_STATE["stage"])
    print("[CLASSIFIER RESULT]:", result)

    return result
