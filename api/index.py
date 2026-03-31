"""Vercel entrypoint — exposes the FastAPI ASGI app."""
import sys
import traceback

try:
    from jobsgrep.main import app
except Exception as _e:
    # Surface import errors as a plain ASGI app so Vercel shows the real error
    _tb = traceback.format_exc()
    async def app(scope, receive, send):
        if scope["type"] == "http":
            body = f"Import failed:\n{_tb}".encode()
            await send({"type": "http.response.start", "status": 500,
                        "headers": [[b"content-type", b"text/plain"],
                                    [b"content-length", str(len(body)).encode()]]})
            await send({"type": "http.response.body", "body": body})

__all__ = ["app"]
