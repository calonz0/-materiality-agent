from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# IMPORTS CORRECTOS
from backend.interface.chat_handler import handle_chat
from backend.api.v1.upload_routes import router as upload_router

app = FastAPI()

# CORS (para que frontend funcione sin problemas)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 🔥 ENDPOINT CHAT
@app.post("/chat")
async def chat_endpoint(data: dict):
    return handle_chat(data)


# 🔥 ENDPOINT UPLOAD (router separado)
app.include_router(upload_router)


# 🔥 HEALTH CHECK (útil para debug)
@app.get("/")
def root():
    return {"status": "Materiality Agent running"}
