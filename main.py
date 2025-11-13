from flask import Flask, render_template, request, redirect, url_for, flash
from function_json import get_video_list, create_new_id
import json
import os

app = Flask(__name__)
VIDEOS_FILE = "videos.json"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    video_list = ["test", "placeholder", "simple"]
    return render_template("videos.html", videos=video_list)

@app.route('/videos/add', methods=['POST'])
def add_video_post():
    # Récupérer les données du formulaire 
    title = request.form['title']
    url = request.form['url']

    # Lire le fichier videos.json et renvoie une liste des videos
    videos = get_video_list(VIDEOS_FILE)
    
    # Créer une nouvelle ID
    new_id = create_new_id(videos)

    # créer une nouvelle vidéo
    new_video = {
        "id": new_id,
        "title": title,
        "url": url,
        "views": 0,
    }

    # ajouter la nouvelle vidéo à la liste
    videos.append(new_video)

    # Ecrire dans le fichier .json
    with open(VIDEOS_FILE, 'w', encoding='utf-8') as f:
        json.dump(videos, f, indent=4, ensure_ascii=False)

# Route GET /videos/add
@app.route('/videos/add', methods=['GET'])          # GET : lecture/affichage
def add_video_get():
    return render_template('add_video.html')        # cherche et interprète le fichier add_video.html dans le dossier templates/

if __name__ == '__main__':                          # permet d’exécuter le code à l’intérieur uniquement si ce fichier est lancé directement
    app.run(debug=True)                             # Démarre le serveur de développement Flask et active le mode debug : rechargement automatique à chaque modification du code, affichage d’erreurs détaillées si un bug se produit.