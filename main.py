from flask import Flask, render_template, request, redirect, url_for, flash
from function_json import get_video_list, create_new_id, save_video_list, add_video_into_list
import json
import os

app = Flask(__name__)
VIDEOS_FILE = "videos.json"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    video_list = get_video_list(VIDEOS_FILE)
    return render_template("videos.html", videos=video_list)

@app.route('/videos/add', methods=['POST'])
def add_video_post():
    # Récupérer les données du formulaire 
    title = request.form['title']
    url = request.form['url']

    # Lire le fichier videos.json et renvoie une liste des videos
    video_list = get_video_list(VIDEOS_FILE)
    print(f"------------------------------------------- première liste : {video_list}")

    # Créer une nouvelle ID
    new_id = create_new_id(video_list)
    print(f"le nouvel id sera : {new_id}")

    # Ajouter la nouvelle vidéo à la liste des vidéos
    video_list = add_video_into_list(video_list, new_id, title, url)
    print(f"-------------------------------------------  nouvelle liste : {video_list}")
    # ENregistrer la liste des vidéos dans le fichier videos.json
    print(save_video_list(video_list, VIDEOS_FILE))

    return redirect(url_for('add_video_get'))

# Route GET /videos/add
@app.route('/videos/add', methods=['GET'])          # GET : lecture/affichage
def add_video_get():
    return render_template('add_video.html')        # cherche et interprète le fichier add_video.html dans le dossier templates/

if __name__ == '__main__':                          # permet d’exécuter le code à l’intérieur uniquement si ce fichier est lancé directement
    app.run(debug=True)                             # Démarre le serveur de développement Flask et active le mode debug : rechargement automatique à chaque modification du code, affichage d’erreurs détaillées si un bug se produit.