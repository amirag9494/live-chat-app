# Real-time Chat App with FastAPI & WebSockets

A simple, lightweight real-time chat application built using **Python (FastAPI)** and **WebSockets**, featuring multiple user connections, usernames, and a clean interface.

## Features
* Real-time bidirectional communication using **WebSockets**.
* **Broadcast messaging** to all connected users simultaneously.
* **Username support** for tracking who sent each message.
* Clean separation of backend logic, HTML, CSS, and JavaScript.

## Tech Stack
* **Backend:** Python, FastAPI, Uvicorn, WebSockets
* **Frontend:** HTML5, CSS3, JavaScript (Vanilla)

## Project Structure
```text
live-chat-app/
│
├── main.py          # FastAPI server & WebSocket endpoints
├── index.html       # Main chat user interface
├── style.css        # UI styling
└── script.js        # WebSocket client-side logic & event handlers