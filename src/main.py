import sys
import asyncio

if sys.platform.startswith('win32'):
    # Windows requires a Proactor-based event loop policy for reliable async IO
    # behavior in this server process (for example with subprocess and socket tasks).
    asyncio.set_event_loop_policy(asyncio.WindowsProactorEventLoopPolicy())

import os
# Ensure the project root is available on sys.path so `src.*` imports resolve
# when this module is executed directly as an entrypoint script.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.persistence.impl.database.orm import create_tables
import uvicorn

if __name__ == "__main__":
    # Create database tables before starting the HTTP server so the application
    # can serve requests immediately without waiting for lazy initialization.
    create_tables()
    # Run the FastAPI app with a fixed host/port configuration for local and
    # containerized deployments; reload stays disabled for production-like runs.
    uvicorn.run(
        "src.service.main:app",
        host="0.0.0.0",
        port=8000,
        reload=False
    )
