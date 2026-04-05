🧠 SYSTEM_CONTEXT.md (VERSIÓN PRO COMPLETA)
# 🧠 AI FISCAL SYSTEM — SYSTEM CONTEXT (ENTERPRISE VERSION)

---

## 📌 OVERVIEW

AI Fiscal System is a modular backend-driven platform designed to:

- Upload fiscal documents (XML + PDF)
- Parse and analyze financial data
- Classify operations (PRODUCT / SERVICE)
- Request required client documents
- Generate materiality documentation
- Produce structured outputs

The system is fully local-first and built for scalability into SaaS.

---

## 🏗️ ARCHITECTURE

```text
Frontend (UI)
    ↓
API (FastAPI)
    ↓
Chat Handler (Interface Layer)
    ↓
Conversational Flow (Orchestrator)
    ↓
Engines + Services
    ↓
Storage + Database
📁 PROJECT STRUCTURE
materiality-agent/

├── frontend/
│   ├── index.html
│   ├── app.js
│   └── style.css
│
├── backend/
│   ├── api/
│   │   ├── main.py
│   │   └── v1/
│   │       ├── upload_routes.py
│   │       ├── auth_routes.py
│   │       └── client_routes.py
│
│   ├── interface/
│   │   └── chat_handler.py
│
│   ├── orchestrator/
│   │   └── conversational_flow.py
│
│   ├── ingestion/
│   │   ├── invoice_parser.py
│   │   └── docx_reader.py
│
│   ├── classifiers/
│   │   └── service_classifier.py
│
│   ├── document_request/
│   │   └── document_checker.py
│
│   ├── validators/
│   │   └── document_validator.py
│
│   ├── engines/
│   │   ├── materiality_engine.py
│   │   ├── rule_engine.py
│   │   ├── llm_client.py
│   │   └── humanizer.py
│
│   ├── generators/
│   │   └── output_generator.py
│
│   ├── state/
│   │   ├── session_manager.py
│   │   └── flow_state.py
│
│   ├── database/
│   │   ├── users.json
│   │   ├── clients.json
│   │   └── companies.json
│
│   └── storage/
│       └── clients/
│           └── {client_id}/
│               ├── uploads/
│               └── outputs/
🌐 FRONTEND
📌 PURPOSE

UI layer for:

Uploading files (XML + PDF)
Sending chat messages
Displaying responses
📄 FILES
index.html
File input (multiple)
Upload button
Chat UI
app.js
FUNCTIONS:
send()
uploadFile()
addMessage()
🔗 API CONNECTIONS
POST /upload?client_id=test_client
POST /chat
🧠 BEHAVIOR
User selects XML + PDF
Clicks Upload
Files sent via FormData
Backend stores files
Chat triggers flow
⚙️ BACKEND
🚀 API LAYER (FastAPI)
main.py
ENDPOINTS:
GET  /
GET  /debug
POST /chat
POST /upload
📦 ROUTES
upload_routes.py

Handles:

Multiple file upload
Storage per client
files: List[UploadFile]
🧠 INTERFACE LAYER
chat_handler.py
RESPONSIBILITIES:
Receive user message
Manage session
Detect triggers
Call flow
🔄 ORCHESTRATOR
conversational_flow.py
CORE SYSTEM
🔥 FLOW (UPDATED)
START
↓
CHECK FILES (XML + PDF)
↓
PARSE XML
↓
PARSE PDF
↓
MERGE DATA
↓
CLASSIFY OPERATION
↓
REQUEST CLIENT DOCUMENTS
↓
VALIDATE DOCUMENTS
↓
GENERATE MATERIALITY
↓
GENERATE OUTPUT
↓
DONE
📌 STATES
START
INVOICE_UPLOADED
CLASSIFY
REQUEST_CLIENT_DOCS
WAITING_CLIENT_DOCS
GENERATE_MATERIALITY
GENERATE_OUTPUT
DONE
📥 INGESTION
invoice_parser.py

Extracts:

RFC
Amount
Date
UUID
📄 FUTURE
PDF parsing (PyMuPDF / pdfplumber)
XML parsing (ElementTree)
🧠 CLASSIFIER
service_classifier.py
classify_operation(data)

Returns:

PRODUCT
SERVICE
📑 DOCUMENT REQUEST
document_checker.py
get_required_documents()
✅ VALIDATION
document_validator.py
validate_documents(client_id, required_docs)
⚙️ ENGINES
materiality_engine.py

Core business logic:

generate_materiality(data, classification)
rule_engine.py
Business rules
Required documents
Operation mapping
llm_client.py
Local LLM integration (Ollama ready)
humanizer.py
Makes responses natural
📤 GENERATOR
output_generator.py
generate_output(client_id, materiality)
🗂️ STORAGE
backend/storage/clients/{client_id}/
STRUCTURE
uploads/
outputs/
🧠 SESSION MANAGEMENT
session_manager.py

Handles:

Session per client
Flow state
flow_state.py
get_initial_state()
🔐 DATABASE

JSON-based (temporary)

users.json
clients.json
companies.json
🚀 EXECUTION
BACKEND
cd ~/materiality-agent
python3 -m uvicorn backend.api.main:app --reload --host 0.0.0.0
FRONTEND
cd ~/materiality-agent/frontend
python3 -m http.server 3000
ACCESS
http://localhost:3000
http://127.0.0.1:8000/docs
🔥 CURRENT STATUS

✅ Upload XML + PDF
✅ Frontend connected
✅ Backend stable
✅ Flow structure ready
⏳ Parsing XML/PDF integration next
⏳ Materiality automation pending

🎯 DESIGN PRINCIPLE

"Frontend displays conversation. Backend drives intelligence."

🚀 FUTURE ROADMAP
PDF parser integration
XML structured extraction
Client DB automation
AI-assisted validation
SaaS deployment
💥 FINAL NOTE

This is no longer a prototype.

This is a modular AI-powered fiscal engine under construction.
---

