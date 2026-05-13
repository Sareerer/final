import pytest
from app import app

@pytest.fixture
def client():
    app.config['test'] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get('/api/health')
    assert response.status_code == 200
    data = response.get_json()
    assert data['status'] == 'ok'



def test_get_patients(client):
    response = client.get('/api/patients')
    assert response.status_code == 200
    data = response.get_json()
    assert isinstance(data, list)

def test_get_patiernt_not_found(client):
    response = client.get('/api/patients/9999')
    assert response.status_code == 404

def test_add_patient(client):
    response = client.post('/api/students', json={'name': 'Memoona', 'condition': 'nothing'})
    assert response.status_code == 201
    data = response.get_json()
    assert data['name'] == 'Memoona'
  assert data['condition'] == 'nothing'

def test_add_missing_field(client):
    response = client.post('/api/patients', json={'name': 'Hadi'})
    response = client.post('/api/patients', json={'condition': 'halleluijah'})
    assert response.status_code == 400
EOF

