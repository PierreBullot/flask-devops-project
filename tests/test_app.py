import pytest
import sys
import os
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
import main


def test_home_page():
    """Test que la page d'accueil fonctionne"""
    client = main.app.test_client()
    response = client.get('/')
    assert response.status_code == 200


def test_list_page():
    """Test que la page d'accueil fonctionne"""
    client = main.app.test_client()
    response = client.get('/videos')
    assert response.status_code == 200


def test_video_page():
    """Test que la page d'accueil fonctionne"""
    client = main.app.test_client()
    # Vérifier qu'une vidéo existante est bien affichée
    response = client.get('/videos/1')
    assert response.status_code == 200
    # Vérifier qu'une vidéo inexistante donne une redirection
    response = client.get('/videos/100')
    assert response.status_code == 302

