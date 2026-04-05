from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.v1.upload_routes import router as upload_router
from backend.interface.chat_handler import handle_request

app = FastAPI()

# 🔥 CORS (permite conexión con frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔹 Root endpoint
@app.get("/")
def root():
    return {"status": "ok"}

# 🔹 Debug endpoint
@app.get("/debug")
def debug():
    return {"message": "debug ok"}

# 🔥 CHAT ENDPOINT (CORREGIDO)
@app.post("/chat")
async def chat(request: dict):
    client_id = request.get("client_id", "test_client")
    message = request.get("message", "")

    response = handle_request(client_id, message)

    # ✅ SIEMPRE devolver JSON con "message"
    return {"message": str(response)}

# 🔹 Upload routes
app.include_router(upload_router)
