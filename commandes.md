### Vérifier la branche sur laquelle on se trouve.
```Bash 
git status
```
### Aller sur une branche.
```Bash 
git checkout dev-pierre
```

### Avoir la dernière version de dev-pierre.
```Bash 
git pull origin dev-pierre
```

### Créer une nouvelle branche.
```Bash 
git checkout -b dev-muriel
```

### Pousser la branche sur Github pour la faire exister en ligne.
```Bash 
git push -u origin dev-muriel
```

### Vérifier la branche active qui sera marqué par une étoile *.
```Bash 
git branch
```

### Activer l'environnement virtuel.
```Bash 
.\.venv\Scripts\activate 
```

### Installer Flask dans l'environnement virtuel
```Bash 
pip install flask
```

### Enregistrement de Flask dans requirements.txt
```Bash 
pip freeze > requirements.txt
```

### Installer tout ce que contient le fichier requirements.txt
```Bash 
pip install -r requirements.txt
```

### fusionner la branche dev_pierre dans ma branche dev_muriel
Vérifier la branche sur laquelle on se trouve  
Se placer sur la branche dev_muriel si besoin  
Mettre à jour toutes les branches distantes  
```Bash 
git fetch origin
```
soit :  Fusionner dev-pierre dans dev-muriel
```Bash 
git merge origin/dev_pierre
```
soit : Fusionner dev-pierre dans dev-muriel seulement en local
```Bash 
git merge dev_pierre
```
Gérer les conflits  : choisir quelles parties garder et enregistrer les modifications  
Pousser ma branche dev-muriel sur github  
```Bash 
git push origin dev-muriel
```

