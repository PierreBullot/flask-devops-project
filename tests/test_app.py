import pytest
import sys
import os

# On ajoute le répertoire parent au path pour pouvoir importer 'app' et 'utils'.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
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
    """Fixture: crée et configure un client de test Flask.
    Ce client est réutilisable dans les tests suivants. """
    from app import app
    app.config['TESTING'] = True
    return app.test_client()


def test_home(client):
    """Vérifie que la page d'accueil répond 'OK (200)' et contient le mot 'Welcome'."""
    response = client.get('/')
    assert response.status_code == 200
    assert "Welcome" in str(response.data)


def test_products(client):
    """Vérifie la route /products retourne une liste attendue."""
    response = client.get('/products')
    assert response.status_code == 200
    products = response.get_json()
    assert len(products) == 4
    assert 'Product 1' in products

    