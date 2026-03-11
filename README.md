# AgentTrust Scorecard (Join39 App)

A tiny, stateless **REST API** that returns a **heuristic trust scorecard** for a **Join39 agent username**.

It is designed to be submitted to the **Join39 Agent Store** as an **App** (your API becomes a tool agents can call).

## What it does

Given a Join39 username (e.g. `alice` or `@alice`), the API:

1. Fetches that agent's public AgentFacts from `https://join39.org/api/{username}/agentfacts.json`
2. Produces a lightweight trust score (0-100) across 5 dimensions
3. Returns a short list of suggested red-team tests

**Important:** This is *not* a certification. It is a pre-interaction screening signal based on public metadata.

## Endpoints

- `GET /health` → `{ "status": "ok" }`
- `POST /score` → trust scorecard JSON

## Local run

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

Test (offline, no network fetch):

```bash
curl -s http://localhost:8000/health
curl -s http://localhost:8000/score \
  -H 'Content-Type: application/json' \
  -d '{"username":"alice","agentfacts_json":'"$(cat sample_agentfacts.json)"',"interaction_context":"ask for medical advice"}'
```

Or run tests:

```bash
pip install -r requirements.txt
pip install pytest
pytest -q
```

## Deploy (fastest path)

### Option A: Render (UI)

1. Put this repo on GitHub (upload the folder contents).
2. In Render: **New → Web Service → Connect repo**
3. Start Command:

```
uvicorn main:app --host 0.0.0.0 --port $PORT
```

Render gives you an HTTPS URL like `https://agenttrust-scorecard.onrender.com`.

### Option B: Railway

Railway can deploy from GitHub with either Nixpacks (Python) or Docker.
If you use Docker, the included `Dockerfile` works.

## Join39 submission values

In the Join39 submission form (`join39.org/apps/submit`), use:

- **Display Name:** AgentTrust Scorecard
- **App Name (slug):** agenttrust-scorecard
- **Description:** Heuristic trust scorecard + red-team checklist for Join39 agents. Provide a username and optional interaction context; returns a 0-100 metadata-based score across identity, capability transparency, security boundaries, observability, and reputation.
- **Category:** utilities
- **API Endpoint:** `https://YOUR_DEPLOYED_DOMAIN/score`
- **HTTP Method:** POST
- **Authentication:** None
- **Function Definition:** paste the JSON in `join39_manifest.json` → `functionDefinition`

## Quick manual API check (after deploy)

```bash
curl -s https://YOUR_DEPLOYED_DOMAIN/health
curl -s https://YOUR_DEPLOYED_DOMAIN/score \
  -H 'Content-Type: application/json' \
  -d '{"username":"YOUR_JOIN39_USERNAME"}'
```
