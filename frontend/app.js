
const chat = document.getElementById("chat");
const input = document.getElementById("messageInput");
const statusDiv = document.getElementById("status");

function addMessage(text, type) {
    const div = document.createElement("div");
    div.className = "message " + type;
    div.innerText = text;
    chat.appendChild(div);
    chat.scrollTop = chat.scrollHeight;
}

// SEND MESSAGE
async function sendMessage() {
    const msg = input.value;
    if (!msg) return;

    addMessage("You: " + msg, "user");
    input.value = "";

    const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({message: msg})
    });

    const data = await res.json();

    addMessage("System: " + (data.response || "No response"), "system");
}

// ENTER KEY
input.addEventListener("keydown", function(e) {
    if (e.key === "Enter") {
        e.preventDefault();
        sendMessage();
    }
});

// UPLOAD FILE
async function uploadFile() {
    const file = document.getElementById("fileInput").files[0];
    if (!file) return alert("Select file");

    const formData = new FormData();
    formData.append("file", file);

    statusDiv.innerText = "Flow: Uploading...";

    try {
        const res = await fetch("http://127.0.0.1:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await res.json();

        console.log("UPLOAD RESPONSE:", data);

        if (!data.operation_type) {
            addMessage("System: Upload failed", "system");
            return;
        }

        statusDiv.innerText = "Flow: Classified";

        addMessage("Detected: " + data.operation_type, "system");
        addMessage("Reason: " + data.justification, "system");

        showDecision();

    } catch (err) {
        console.error(err);
        addMessage("System: Upload error", "system");
    }
}

// CONFIRM / REJECT UI
function showDecision() {
    const div = document.createElement("div");

    div.innerHTML = `
        <br>
        <button onclick="confirmDecision(true)">✔ Confirm</button>
        <button onclick="confirmDecision(false)">✖ Reject</button>
    `;

    chat.appendChild(div);
}

// CONFIRM ACTION
async function confirmDecision(val) {
    const res = await fetch("http://127.0.0.1:8000/chat", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({confirmation: val})
    });

    const data = await res.json();

    addMessage("System: " + (data.response || ""), "system");
}
