let ws = null;
let username = "";

function joinChat() {
    const inputName = document.getElementById("usernameText").value.trim();
    if (inputName === "") {
        alert("Please enter a valid name!");
        return;
    }
    username = inputName;
    document.getElementById("my-username").innerText = username;
    
    document.getElementById("login-section").style.display = "none";
    document.getElementById("chat-section").style.display = "block";

    ws = new WebSocket("ws://localhost:8000/ws");

    ws.onmessage = function(event) {
        const messages = document.getElementById('messages');
        const message = document.createElement('li');
        const content = document.createTextNode(event.data);
        message.appendChild(content);
        messages.appendChild(message);
        messages.scrollTop = messages.scrollHeight;
    };
}

function sendMessage(event) {
    event.preventDefault();

    const input = document.getElementById("messageText");
    const messageText = input.value.trim();
    
    if (messageText === "") return;

    if (!ws || ws.readyState !== WebSocket.OPEN) {
        alert("WebSocket is not connected!");
        return;
    }

    const data = {
        sender: username,
        message: messageText
    };

    ws.send(JSON.stringify(data));
    input.value = '';
}