import pytest
import sys
import os

# On ajoute le répertoire parent au path pour pouvoir importer 'app' et 'utils'.
# sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# os.path.dirname(__file__)  :  Renvoie le chemin du dossier où se trouve le fichier actuel.
# os.path.join(..., '..')    :  Remonte au dossier parent.
# os.path.abspath(...)       :  Convertit ça en un chemin absolu complet.
# sys.path                   :  C'est la liste des répertoires où Python cherche les modules à importer.
# sys.path.insert(0, ...)    :  Ajoute le chemin du dossier parent au début de sys.path
# cette ligne peut-être supprimée et remplacée par le fichier pytest.ini à la racine avec dedans : 
#           [pytest]    
#           pythonpath = .

@pytest.fixture
def sample_data():
    """Fixture: retourne une liste d'exemples d'objets (simule des enregistrements).
    Réutilisable dans les tests nécessitant des données d'exemple."""
    return [
        {'id':1, 'url':'http://example.com/1', 'title': 'Example 1', 'views': '0'},
        {'id':2, 'url':'http://example.com/2', 'title': 'Example 2', 'views': '10'},
        {'id':3, 'url':'http://example.com/3', 'title': 'Example 3', 'views': '50'}
    ]


@pytest.fixture
def client():
    """Fixture: crée et configure un client comme s'il utilisait l'appli dans un
     navigateur afin de tester l'appli sans utiliser de serveur réel
    Ce client est réutilisable dans les tests suivants. """
    from main import app
    # 
    app.config['TESTING'] = True
    return app.test_client()


def test_home_page(client):
    """Vérifie que la page d'accueil répond 'OK (200)' et contient le mot 'Accueil'."""
    response = client.get('/')
    assert response.status_code == 200
    assert "Accueil" in str(response.data)

def test_search_page(client, sample_data, monkeypatch):
    monkeypatch.setattr('main.search_video', lambda: sample_data)
    response = client.get('/videos/search')
    assert '<div class="video-item">' not in str(response.data), "Get request on /videos/search should not return any video"
    
    # vérifie qu'une seule réponse est donnée quand tout le titre et le nombre de vues sont donnés
    response = client.post(
        '/videos/search', 
        data = {'word': 'azetatrat', 'number': '0'}, 
        follow_redirects=True)
    assert '<div class="video-item">' in str(response.data), "Should return azetatrat"

    # vérifie qu'une seule réponse est donnée quand une partie du titre et le nombre de vues sont donnés
    response = client.post(
        '/videos/search', 
        data = {'word': 'azeta', 'number': '0'}, 
        follow_redirects=True)
    assert '<div class="video-item">' in str(response.data), "Should return azetatrat"

    # vérifie qu'une réponse est donnée quand seul le nombre de vues est donné
    response = client.post(
        '/videos/search', 
        data = {'word': '', 'number': '2'}, 
        follow_redirects=True)
    assert '<div class="video-item">' in str(response.data), "Should return everything when views <= 2"

    # vérifie qu'une réponse est donnée quand seul le titre est donné
    response = client.post(
        '/videos/search', 
        data = {'word': 'azetatrat', 'number': '0'}, 
        follow_redirects=True)
    assert '<div class="video-item">' in str(response.data), "Should return azetatrat when views == 0"

    # vérifie que la page n'est pas chargée quand rien n'est trouvé
    response = client.post(
        '/videos/search', 
        data = {'word':'zzzzzzzzzzzzzz', 'number': '-2'})
    assert '<div class="video-item">' not in str(response.data), "Should not return anything"

    # vérifie que la page n'est pas chargée quand le titre et le nombre de vues sont vides
    response = client.post(
        '/videos/search', 
        data = {'word':'', 'number': '0'})
    assert '<div class="video-item">' not in str(response.data), "Should not return anything"

    # vérifie que la page n'est pas chargée quand le nombre de vues est incorrect
    response = client.post(
        '/videos/search', 
        data = {'word': 'azetatrat', 'number': '-2'})
    assert '<div class="video-item">' not in str(response.data), "Should return azetatrat when views == 0"
