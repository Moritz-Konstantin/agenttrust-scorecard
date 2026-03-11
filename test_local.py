import json
from fastapi.testclient import TestClient

from main import app


def test_health():
    c = TestClient(app)
    r = c.get('/health')
    assert r.status_code == 200
    assert r.json() == {'status': 'ok'}


def test_score_offline_agentfacts_override():
    c = TestClient(app)
    agentfacts = json.load(open('sample_agentfacts.json'))
    r = c.post('/score', json={'username': 'alice', 'agentfacts_json': agentfacts, 'interaction_context': 'ask for medical advice'})
    assert r.status_code == 200
    data = r.json()
    assert data['username'] == 'alice'
    assert 0 <= data['trust_score'] <= 100
    assert data['risk_level'] in ['low','medium','high']
    assert 'dimension_scores' in data
