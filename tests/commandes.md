# Commandes avec pytest
## installation et configuration initiale
installer pytest 
``` bash
pip install pytest
```

## Les décorateurs et leur utilisation
1) @pytest.mark pour catégoriser et organiser les tests    
Exécuter des sous-ensembles spécifiques de tests : <span style="background-color: #4976a0ff;">@pytest.mark.category_name</span>
``` bash
pytest -v -m category_name
```
2) skip et skipif pour la gestion conditionnelle  
Ignorer temporairement certains tests : <span style="background-color: #4976a0ff;">@pytest.mark.skip(reason="Fonctionnalité en cours de refactoring")</span>  
Ignorer temporairement certains tests sous certaines conditions :  
&emsp;&emsp;<span style="background-color: #4976a0ff;">@pytest.mark.skipif(sys.version_info < (3, 8),</span>  
&emsp;&emsp;<span style="background-color: #4976a0ff;">reason="Nécessite Python 3.8 ou supérieur") </span>  

3) parametrize pour les tests paramétrés  
Réutiliser une même logique de test avec différentes valeurs d'entrée: <span style="background-color: #4976a0ff;">@pytest.mark.parametrize</span>  

## Techniques avancées de test  
1) Les fixtures  
Préparer un environnement avant un test  
Fournir des objets réutilisables (client Flask, base de données en mémoire…)  
Eviter la duplication de code dans chaque test

2) Les scopes de fixtures  

PASSED (test réussi)  
FAILED (test échoué)   
ERROR (test en erreur)  
SKIPPED (test ignoré)  


``` bash

```

``` bash

```

``` bash

```

``` bash

```