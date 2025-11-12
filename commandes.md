### Vérifier la branche sur laquelle on se trouve.
git status

### Aller sur une branche.
git checkout dev-pierre

### Avoir la dernière version de dev-pierre.
git pull origin dev-pierre

### Créer une nouvelle branche.
git checkout -b dev-muriel

### Pousser la branche sur Github pour la faire exister en ligne.
git push -u origin dev-muriel

### Vérifier la branche active qui sera marqué par une étoile *.
git branch

### Activer l'environnement virtuek.
.\\.venv\Scripts\activate  <!-- bonne écriture : .\.venv\Scripts\activate  -->

### Installer Flask dans l'environnement virtuel
pip install flask

### Enregistrement de Flask dans requirements.txt
pip freeze > requirements.txt

### Installer tout ce que contient le fichier requirements.txt
pip install -r requirements.txt
