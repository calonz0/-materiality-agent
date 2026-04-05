🌐 FRONTEND CONTEXT — AI FISCAL SYSTEM

---

## 📌 PURPOSE

Frontend is a thin UI layer designed to:

- Upload XML and PDF files
- Send user messages
- Display system responses

NO business logic lives here.

---

## 🏗️ ARCHITECTURE

```text
User → Browser → app.js → FastAPI Backend
📁 STRUCTURE
frontend/

├── index.html
├── app.js
└── style.css
📄 index.html
COMPONENTS:
File input (multiple)
Upload button
Chat container
Message input
Send button
🧠 app.js
FUNCTIONS
uploadFile()
Collects selected files
Sends FormData to backend
Endpoint: /upload
send()
Sends chat message
Endpoint: /chat
addMessage()
Renders messages in UI
🔗 API CALLS
POST http://localhost:8000/upload?client_id=test_client
POST http://localhost:8000/chat
🧠 BEHAVIOR
User selects XML + PDF
Clicks upload
Files sent to backend
Backend stores files
User triggers flow via chat
⚠️ LIMITATIONS
No validation of file types
No upload progress indicator
No error UI handling
No authentication
🚀 FUTURE IMPROVEMENTS
Drag & drop upload
File validation (XML/PDF)
Upload progress bar
Chat streaming
Better UI/UX
🎯 DESIGN PRINCIPLE

"Frontend is display-only. Intelligence lives in backend."


---

# 🧭 2. ARCHITECTURE.md

```bash
nano ~/materiality-agent/ARCHITECTURE.md
❗ PEGA TODO:
# 🏗️ SYSTEM ARCHITECTURE — AI FISCAL SYSTEM

---

## 📌 OVERVIEW

This system follows a layered architecture:

```text
Frontend → API → Interface → Orchestrator → Engines → Storage
🔹 LAYERS
🌐 FRONTEND
Handles UI
Sends HTTP requests
No logic
🚀 API (FastAPI)
Entry point
Defines endpoints:
/upload
/chat
🧠 INTERFACE
chat_handler.py
Handles session
Routes messages to flow
🔄 ORCHESTRATOR
conversational_flow.py
Controls system flow
State-driven execution
⚙️ ENGINES
materiality_engine
rule_engine
llm_client
📥 INGESTION
XML parsing
PDF parsing (future)
📑 VALIDATION
Document validation
📤 GENERATION
Output creation
🗂️ STORAGE
storage/clients/{client_id}/
🔥 FLOW (CORE LOGIC)
UPLOAD FILES
↓
DETECT XML/PDF
↓
PARSE DATA
↓
CLASSIFY OPERATION
↓
REQUEST DOCUMENTS
↓
VALIDATE
↓
GENERATE MATERIALITY
↓
OUTPUT
🧠 DESIGN PRINCIPLES
Modular
Scalable
Replaceable components
Backend-driven logic
🚀 FUTURE
Microservices
Database (PostgreSQL)
Auth layer
Queue system (Celery)

---

# 🧭 3. DEV_GUIDE.md

```bash
nano ~/materiality-agent/DEV_GUIDE.md
❗ PEGA TODO:
# 🧑‍💻 DEVELOPER GUIDE — AI FISCAL SYSTEM

---

## 🚀 HOW TO RUN

---

### BACKEND

```bash
cd ~/materiality-agent
python3 -m uvicorn backend.api.main:app --reload --host 0.0.0.0
FRONTEND
cd ~/materiality-agent/frontend
python3 -m http.server 3000
ACCESS
http://localhost:3000
http://127.0.0.1:8000/docs
📂 IMPORTANT FILES
File	Purpose
main.py	API entry
chat_handler.py	Message routing
conversational_flow.py	Core logic
upload_routes.py	File upload
🔄 FLOW CONTROL

All logic is driven by:

session["flow"]["step"]
🧠 DEBUGGING
Backend logs

Look for:

POST /upload → 200 OK
Common errors
Error	Cause
Upload failed	Backend off
404	Wrong endpoint
No response	Flow stuck
🧪 TESTING

Upload:

XML
PDF

Then send:

factura
🚀 NEXT DEVELOPMENT
XML parser
PDF parser
AI integration
DB migration
🎯 BEST PRACTICES
Do not mix frontend/backend logic
Keep flow deterministic
Log everything
Avoid hardcoding paths
💥 RULE

"If it's not in the flow, it doesn't exist."
