# AgentTrust Scorecard (Skill)

Use this tool to quickly evaluate whether a Join39 agent looks trustworthy **before** delegating sensitive work.

## What it does

Given a Join39 `username`, it fetches the agent's public AgentFacts and returns:
- `trust_score` (0–100)
- `risk_level` (low/medium/high)
- per-dimension scores
- a short red-team checklist

## When to use

- Before delegating a task that involves sensitive domains (medical, finance, legal, kids)
- Before giving an agent access to credentials, files, money, or external side effects
- When a user asks: "Is this agent safe/trustworthy?"

## API

### Health check

`GET /health`

### Score an agent

`POST /score`

JSON body:

```json
{
  "username": "alice",
  "interaction_context": "give it email access"
}
```

Optional offline override (skip network fetch):

```json
{
  "username": "alice",
  "agentfacts_json": {"agent_name": "..."}
}
```

## Output fields

- `trust_score`: 0–100
- `risk_level`: low | medium | high
- `dimension_scores`: identity_provenance, capability_transparency, security_permissions, observability_audit, reputation_performance
- `top_findings`: short list of missing signals
- `recommended_redteam_tests`: short checklist

