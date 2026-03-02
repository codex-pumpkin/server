import os

# Provide default settings for tests to avoid validation errors when importing modules
os.environ.setdefault("APP_MAIL_SMTP_SERVER", "localhost")
os.environ.setdefault("APP_MAIL_SMTP_PORT", "25")
os.environ.setdefault("APP_MAIL", "test@example.com")
os.environ.setdefault("MAIL_PASSWORD", "password")
os.environ.setdefault("CLIENT_BASE_URL", "http://localhost:4200")
# JWT secret required by settings
os.environ.setdefault("JWT_SECRET", "testsecret")
# Minimal google auth config to satisfy settings
os.environ.setdefault("CLIENT_ID", "testid")
os.environ.setdefault("CLIENT_SECRET", "testsecret")
# Use an in-memory sqlite database with async driver
os.environ.setdefault("DATABASE_URL", "sqlite+aiosqlite:///:memory:")
# Chroma settings can be dummy
os.environ.setdefault("CHROMA_HOST", "localhost")
os.environ.setdefault("CHROMA_PORT", "8000")
# Admin account defaults
os.environ.setdefault("ADMIN_EMAIL", "admin@example.com")
os.environ.setdefault("ADMIN_USERNAME", "admin")
os.environ.setdefault("ADMIN_PASSWORD", "admin")
