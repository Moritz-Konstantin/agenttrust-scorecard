import os
import uvicorn

def get_port() -> int:
    raw = os.environ.get("PORT", "8000")
    try:
        return int(raw)
    except Exception:
        # safety fallback if something weird gets injected
        return 8000

if __name__ == "__main__":
    port = get_port()
    print(f"Starting uvicorn on 0.0.0.0:{port} (PORT env={os.environ.get('PORT')})")
    uvicorn.run("main:app", host="0.0.0.0", port=port, log_level="info")
