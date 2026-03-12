FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY main.py ./

# IMPORTANT: run via a shell so ${PORT} expands; fallback to 8000 locally
CMD sh -c "python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-8000}"
