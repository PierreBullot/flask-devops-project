import pytest
import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import main
import functions_json


@pytest.fixture
def client():
    client = main.app.test_client()
    return client


@pytest.fixture
def save_file():
    return [{
        "id": 1,
        "url": "https://youtube.com/watch?v=abc123",
        "title": "titre 1",
        "views": 0
    },
    {
        "id": 2,
        "url": "https://youtube.com/watch?v=abc123",
        "title": "Titre 2",
        "views": 0
    },
    {
        "id": 3,
        "url": "https://youtube.com/watch?v=abc123",
        "title": "Titre 3",
        "views": 0
    }]


def test_home_page(client):
    """Teste que la page d'accueil fonctionne."""
    response = client.get('/')
    assert response.status_code == 200


def test_list_page(client):
    """Teste que la page qui affiche la liste des vidéos fonctionne."""
    response = client.get('/videos')
    assert response.status_code == 200


def test_video_page(client, save_file, monkeypatch):
    """Teste que la page qui affiche une vidéo particulière fonctionne."""
    monkeypatch.setattr('main.functions_json.get_video_list', lambda arg: save_file)
    monkeypatch.setattr('main.functions_json.update_video', lambda arg1, arg2: save_file)
    monkeypatch.setattr('main.functions_json.delete_video', lambda arg1, arg2: save_file)

    # Vérifier qu'une vidéo existante est bien affichée
    response = client.get('/videos/1')
    assert response.status_code == 200

    # Vérifier qu'une vidéo inexistante donne une redirection
    response = client.get('/videos/4')
    assert response.status_code == 302

    # Vérifier que la modification d'une vidéo fonctionne
    response = client.post('/videos/2', data={
        "title": "titre test",
        "modify": "Modifier"
    })
    assert response.status_code == 200
