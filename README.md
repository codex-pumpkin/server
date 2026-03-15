<p align="center">
  <img src="Logo.svg" alt="Project Logo" width="500"/>
</p>

# CodeX Server Component
This repository contains the code for the CodeX server component.

## Project Structure
- `public/`: Public assets
- `src/`: Source files. Main index and script file
    - `app/environment`: Infrastructure to get environment configuration
    - `app/model/network`: Connection to the REST-API of the backend
    - `app/model/domain`: Domain models for the entities
    - `app/model/authentication`: Abstraction over the authentication. Keeps the currently authenticated account

## Project Structure
- `src/main.py`: local entry point
- `src/service/main.py`: FastAPI app registration
- `src/service/apis/`: API routers
- `src/business/`: Business-layer managers
- `src/persistence/`: DB, LLM, mail, and vector-store integrations
- `requirements.txt`: Python dependencies

## Running
Required: 
- `python 3.13`
- pip

To run the server, do:
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m src.main
```

On windows, use

```bash
.\.venv\Scripts\Activate.ps1
```

to create a virtual environment.

## Containerization
The project can be built into an image using
```bash
docker build . -t codex/server
```

The building process is configured by the `Dockerfile`, that mainly does:
1. Install apt-packages
2. Install python requirements

### Container startup
On startup, the `src.main` file is executed.
This file, before running the REST-API via uvicorn, performs miscellaneous initializations, like
- Creating the database tables
- Creating data directories

**Only** on the initial, i.e. first, startup, one singular admin-account is created.
The credentials refer to the ones set via the `ADMIN_USERNAME`, `ADMIN_EMAIL` and `ADMIN_PASSWORD` environment variables.
While these can be changed, as with every account, this is strongly discouraged.
Other admin-accounts cannot be created after the initial startup.

## Deployment

After the project has been built into an image, it can be used via docker.

An example docker-compose configuration [is provided](/docker-compose.yml).

### Environment parameters

| Parameter Name              | Description                                                                                                          |
|-----------------------------|----------------------------------------------------------------------------------------------------------------------|
| APP_MAIL                    | The username to the SMTP server. Usually the email-address.                                                          |
| MAIL_PASSWORD               | The password to the SMTP server.                                                                                     |
| APP_MAIL_SMTP_SERVER        | The host of the SMTP server.                                                                                         |                                 |
| APP_MAIL_SMTP_PORT          | The port of the SMTP server.                                                                                         |                                 |
| JWT_SECRET                  | The secret used to sign JWT's.                                                                                       |                                 |
| CLIENT_SECRET               | The client secret of the google cloud project.                                                                       |                                 |
| CLIENT_ID                   | The client ID of the google cloud project.                                                                           |                                 |
| CLIENT_BASE_URL             | The base url on which the frontend is running. No trailing slash.                                                    |                                 |
| DATABASE_URL                | The postgres url to connect to the database. Must be of format `postgresql://<user>:<password>@<host>:<port>/<name>` |                                 |
| CHROMA_PORT                 | The port of the chroma database.                                                                                     |                                 |
| CHROMA_HOST                 | The host of the chroma database.                                                                                     |                                 |
| ADMIN_USERNAME              | The username of the created admin account.                                                                           |                                 |
| ADMIN_EMAIL                 | The email-address of the created admin account.                                                                      |                                 |
| ADMIN_PASSWORD              | The password of the created admin account.                                                                           |                                 |
| OPENAI_API_KEY              | The OpenAi api key for the embedding function.                                                                       |                                 |
| EMAIL_VERIFICATION_REQUIRED | Whether users should have to verify their email to access the server. Only used for load tests.                      |                                 |

### Volumes
The following directories are used by the container:
- `/app/docs`: Input directory for the PDF-files used as an input for the RAG-system
- `/app/pictures`: Storage directory for profile-pictures of accounts

They can be bound to volumes or local paths.

## Unit tests
Major components are tested using `pytest`.

To run all unit tests, use
```bash
pytest -q
```

This will create a coverage report in `coverage/`.
