async function sendMessage() {
    const input = document.getElementById("messageInput");
    const message = input.value;

    if (!message) return;

    addMessage("You", message, "user");
    input.value = "";

    try {
        const response = await fetch("http://localhost:8000/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                client_id: "web_user",
                message: message
            })
        });

        const data = await response.json();

        console.log("BACKEND RESPONSE:", data);

        if (data && data.message) {
            addMessage("System", data.message, "bot");
        } else {
            addMessage("System", "⚠️ Respuesta vacía del servidor", "bot");
        }

    } catch (err) {
        console.error("ERROR:", err);
        addMessage("System", "❌ Error conectando al backend", "bot");
    }
}


function addMessage(sender, text, type) {
    const chat = document.getElementById("chat");

    const msg = document.createElement("div");
    msg.style.marginBottom = "10px";

    msg.innerHTML = `<strong>${sender}:</strong> ${text}`;

    chat.appendChild(msg);
    chat.scrollTop = chat.scrollHeight;
}


async function uploadFile() {
    const fileInput = document.getElementById("fileInput");
    const files = fileInput.files;

    if (!files.length) {
        alert("Selecciona archivos primero");
        return;
    }

    const formData = new FormData();

    for (let i = 0; i < files.length; i++) {
        formData.append("files", files[i]);
    }

    try {
        const response = await fetch("http://localhost:8000/upload", {
            method: "POST",
            body: formData
        });

        const data = await response.json();

        console.log("UPLOAD RESPONSE:", data);

        addMessage("System", "Archivos subidos correctamente", "bot");

    } catch (err) {
        console.error("UPLOAD ERROR:", err);
        addMessage("System", "❌ Error subiendo archivos", "bot");
    }
}
