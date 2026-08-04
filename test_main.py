from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_create_and_get_note():
    response = client.post("/notes", json={"title": "Test", "content": "Body"})
    assert response.status_code == 200
    note_id = response.json()["id"]

    get_response = client.get(f"/notes/{note_id}")
    assert get_response.status_code == 200
    assert get_response.json()["title"] == "Test"
