# CodeX Server

Backend API service for authentication and quota management, built with FastAPI.

## Tech Stack
- Python 3.11+
- FastAPI + Uvicorn
- SQLAlchemy + SQLite
- OpenAI SDK
- ChromaDB (semantic retrieval)

## Project Structure
- `src/main.py`: local entry point (creates DB tables and starts Uvicorn).
- `src/service/main.py`: FastAPI app registration.
- `src/service/apis/`: API routers.
- `src/business/`: business-layer managers.
- `src/persistence/`: DB, LLM, mail, and vector-store integrations.
- `requeirements.txt`: Python dependencies (filename is intentionally spelled this way in repo).

## Prerequisites
- Python `3.11` or newer
- `pip`

## Setup
```bash
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -r requeirements.txt
```

## Run (Development)
```bash
python src/main.py
```

Server starts on:
- `http://localhost:8000`

Useful docs:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Available API Routes
### Authentication
- `GET /auth/google/login`
- `GET /auth/google/callback`
- `POST /auth/login`
- `POST /auth/signup`
- `POST /auth/refresh`
- `POST /auth/logout`
- `POST /auth/request-password-reset`
- `POST /auth/submit-password-reset`
- `POST /auth/request-email-verification`
- `POST /auth/submit-email-verification`

### Quota
- `GET /quota`
- `PUT /quota`

## Data and Persistence
- SQLite file: `database.db` (created automatically when starting the app).
- ChromaDB data and documents are under `src/persistence/impl/chroma_database/`.

## Configuration Notes
Current settings are defined directly in `src/core/settings.py` (mail, JWT, LLM). For production use:
- move secrets/API keys to environment variables,
- rotate any exposed credentials,
- disable debug-style logging and `reload=True`.

## Quick Health Check
After startup:
```bash
curl http://localhost:8000/docs
```
You should receive the Swagger UI HTML page.
