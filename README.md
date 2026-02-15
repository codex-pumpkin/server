# CodeX Server

Backend API service for authentication and quota management, built with FastAPI.

## Tech Stack
- Python 3.13
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
- Python `3.13` or newer
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


## Environment Variables (Mandatory)

The following environment variables **must be set** before starting the application:
 - `APP_MAIL`
 - `MAIL_PASSWORD`
 - `JWT_SECRET`
 - `CLIENT_SECRET`
 - `CLIENT_ID`


##  Docker Build & Run

Build the Docker image:

```bash
docker build -t codex-server .
```

Run the container using environment variables from a `.env` file:

```bash
docker run --env-file .env -p 8000:8000 codex-server
```

The application will start inside the container and be available at:

```
http://localhost:8000/docs
```

Using a `.env` file allows you to securely provide required environment variables at runtime without hardcoding them into the Docker image.