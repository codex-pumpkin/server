from .database import EntityRepository
from .mail import MailSender
from .validator import CodeValidator
from .llm import AIClient
from .generator import GraphGenerator

# Chroma can fail to import on unsupported Python versions (e.g. 3.14).
# Keep package import usable for non-inference API routes.
try:
    from .chroma_database import SemanticRepository
except Exception:  # pragma: no cover
    SemanticRepository = None  # type: ignore

__all__ = [
    "SemanticRepository",
    "EntityRepository",
    "MailSender",
    "CodeValidator",
    "AIClient",
    "GraphGenerator"
]
