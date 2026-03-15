import os
import sys
import types
from pathlib import Path


os.environ.setdefault("APP_MAIL_SMTP_SERVER", "smtp.example.com")
os.environ.setdefault("APP_MAIL_SMTP_PORT", "465")
os.environ.setdefault("APP_MAIL", "codex@example.com")
os.environ.setdefault("MAIL_PASSWORD", "secret")
os.environ.setdefault("CLIENT_BASE_URL", "http://localhost:4200")
os.environ.setdefault("JWT_SECRET", "test-secret")
os.environ.setdefault("CLIENT_ID", "client-id")
os.environ.setdefault("CLIENT_SECRET", "client-secret")
os.environ.setdefault("DATABASE_URL", "postgresql://codex:codex@localhost:5432/codex")
os.environ.setdefault("CHROMA_HOST", "localhost")
os.environ.setdefault("CHROMA_PORT", "8000")
os.environ.setdefault("ADMIN_EMAIL", "admin@example.com")
os.environ.setdefault("ADMIN_USERNAME", "admin")
os.environ.setdefault("ADMIN_PASSWORD", "password")


def _install_stub_modules() -> None:
    typer_module = types.ModuleType("typer")
    typer_module.prompt = lambda *args, **kwargs: ""
    sys.modules.setdefault("typer", typer_module)

    aiosmtplib_module = types.ModuleType("aiosmtplib")

    async def _send(*args, **kwargs):
        return None

    aiosmtplib_module.send = _send
    sys.modules.setdefault("aiosmtplib", aiosmtplib_module)

    openai_module = types.ModuleType("openai")

    class _BaseError(Exception):
        pass

    class AsyncOpenAI:
        def __init__(self, *args, **kwargs):
            self.responses = types.SimpleNamespace(create=None)
            self.chat = types.SimpleNamespace(completions=types.SimpleNamespace(create=None))

    openai_module.AsyncOpenAI = AsyncOpenAI
    openai_module.APIConnectionError = _BaseError
    openai_module.APIError = _BaseError
    openai_module.AuthenticationError = _BaseError
    openai_module.BadRequestError = _BaseError
    openai_module.NotFoundError = _BaseError
    openai_module.PermissionDeniedError = _BaseError
    openai_module.RateLimitError = _BaseError
    sys.modules.setdefault("openai", openai_module)

    litellm_module = types.ModuleType("litellm")

    async def _acompletion(*args, **kwargs):
        return types.SimpleNamespace(
            choices=[types.SimpleNamespace(message=types.SimpleNamespace(content="stub"))]
        )

    litellm_module.acompletion = _acompletion
    litellm_module.AuthenticationError = _BaseError
    litellm_module.APIConnectionError = _BaseError
    litellm_module.NotFoundError = _BaseError
    litellm_module.BadRequestError = _BaseError
    litellm_module.PermissionDeniedError = _BaseError
    litellm_module.APIError = _BaseError
    litellm_module.RateLimitError = _BaseError
    sys.modules.setdefault("litellm", litellm_module)

    chromadb_module = types.ModuleType("chromadb")

    class _Collection:
        def query(self, **kwargs):
            return {"documents": [["stub"]]}

    class _Client:
        def __init__(self, *args, **kwargs):
            pass

        def get_collection(self, **kwargs):
            return _Collection()

    chromadb_module.HttpClient = _Client
    chromadb_module.PersistentClient = _Client

    utils_module = types.ModuleType("chromadb.utils")
    embedding_functions_module = types.ModuleType("chromadb.utils.embedding_functions")
    embedding_functions_module.DefaultEmbeddingFunction = lambda: object()
    utils_module.embedding_functions = embedding_functions_module

    sys.modules.setdefault("chromadb", chromadb_module)
    sys.modules.setdefault("chromadb.utils", utils_module)
    sys.modules.setdefault("chromadb.utils.embedding_functions", embedding_functions_module)

    pyspice_module = types.ModuleType("PySpice")
    spice_module = types.ModuleType("PySpice.Spice")
    parser_module = types.ModuleType("PySpice.Spice.Parser")

    class SpiceParser:
        def __init__(self, *args, **kwargs):
            self.subcircuits = []

        def build_circuit(self):
            return types.SimpleNamespace(elements=[])

    parser_module.SpiceParser = SpiceParser
    spice_module.Parser = parser_module
    pyspice_module.Spice = spice_module

    sys.modules.setdefault("PySpice", pyspice_module)
    sys.modules.setdefault("PySpice.Spice", spice_module)
    sys.modules.setdefault("PySpice.Spice.Parser", parser_module)


_install_stub_modules()

from src.core.settings import settings


_pictures_dir = Path(__file__).resolve().parent / "_test_pictures"
_pictures_dir.mkdir(exist_ok=True)
settings.pictures_settings.path = str(_pictures_dir)
