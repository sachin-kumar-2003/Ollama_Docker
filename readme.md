# Ollama + FastAPI Chat API (Local run LLM)

## Overview

This project creates a simple **chat API** using:

* **FastAPI** for the backend
* **Ollama** to run a local AI model
* **Docker Compose** to manage services

The API sends a message to the **Gemma 3 (1B)** model and returns the response.

---

## Project Structure

```
.
├── ollama_api.py
├── docker-compose.yml
└── README.md
```

---

## Requirements

* Docker
* Docker Compose
* Python 3.9+
* Ollama Docker image

---

## Docker Compose

The Ollama service runs inside Docker and exposes port **11434**.

```
services:
  ollama:
    image: ollama/ollama:latest
    ports:
      - '11434:11434'
    volumes:
      - models:/root/.ollama/models

volumes:
  models:
```

---

## FastAPI Code (ollama_api.py)

This API connects to Ollama and sends a message to the model.

Key features:

* Connects to Ollama at `http://localhost:11434`
* Pulls the model `gemma3:1b`
* Exposes a `/chat` endpoint

---

## How to Run

### 1. Start Ollama with Docker

```
docker-compose up -d
```

This will start the Ollama server on port **11434**.

---

### 2. Install Python Dependencies

```
pip install fastapi uvicorn ollama
```

---

### 3. Run the API

```
uvicorn ollama_api:app --reload
```

The API will be available at:

```
http://127.0.0.1:8000
```

---


## Notes

* The model is pulled automatically when the app starts.
* Ollama must be running before starting FastAPI.
* You can change the model name inside `ollama_api.py`.

---

## Done

Your local AI chat API is now running.
