"""Vercel entrypoint — exposes the FastAPI ASGI app."""
from jobsgrep.main import app  # noqa: F401

__all__ = ["app"]
