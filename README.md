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
- `requirements.txt`: Python dependencies.

## Prerequisites
- Python `3.13` (recommended)
- `pip`

## Setup
From the project root:

```bash
cd server
python -m venv .venv
# Windows PowerShell
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

## Run (Development)
```bash
python -m src.main
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
- `APP_MAIL_SMTP_SERVER`
- `APP_MAIL_SMTP_PORT`
- `CLIENT_BASE_URL`

You can copy `.env_example` into `.env` and fill in real values:

```bash
cp .env_example .env
```

PowerShell equivalent:

```powershell
Copy-Item .env_example .env
```

Example:

```env
APP_MAIL=you@example.com
MAIL_PASSWORD=your_mail_password
JWT_SECRET=some_long_random_secret
CLIENT_SECRET=google_client_secret
CLIENT_ID=google_client_id
APP_MAIL_SMTP_SERVER=smtp.gmail.com
APP_MAIL_SMTP_PORT=587
CLIENT_BASE_URL=http://localhost:3000
```

## Tests
Run tests from the `server` directory:

```bash
pytest -q
```


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
