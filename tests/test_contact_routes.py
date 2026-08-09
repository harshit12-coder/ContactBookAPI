from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_create_contact():
    response = client.post("/contacts/", json={
        "name": "Test User1",
        "email": "testuser1@example.com",
        "phone": "9999999998",
        "address": "Test Address1"
    })
    assert response.status_code == 200
    contact_id = response.json()["id"]

    # CLEANUP — test khatam, ab jo banaya usse delete kar do
    client.delete(f"/contacts/{contact_id}")