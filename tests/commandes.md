# Commandes avec pytest
## installation et configuration initiale
installer pytest 
``` bash
pip install pytest
```
PASSED (test réussi)  
FAILED (test échoué)   
ERROR (test en erreur)  
SKIPPED (test ignoré)  


1) Catégoriser et organiser les tests : test.mark  

Exécuter des sous-ensembles spécifiques de tests : <span style="background-color: #4976a0ff;">@pytest.mark.category_name</span>
``` bash
pytest -v -m category_name
```
Ignorer temporairement certains tests : @pytest.mark.skip(reason="Fonctionnalité en cours de refactoring")  
Ignorer temporairement certains tests sous certaines conditions :  
&emsp;&emsp;<span style="background-color: #4976a0ff;">@pytest.mark.skipif(sys.version_info < (3, 8),</span>  
&emsp;&emsp;<span style="background-color: #4976a0ff;">reason="Nécessite Python 3.8 ou supérieur") </span>  
Réutiliser une même logique de test avec différentes valeurs d'entrée. 
``` bash

```

``` bash

```

``` bash

```

``` bash

```