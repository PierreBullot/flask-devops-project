from flask import Flask, render_template, request, redirect, url_for
import functions_json

app = Flask(__name__)
# Récupérer les données du fichier .json
VIDEOS_FILE = "videos.json"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    video_list = functions_json.get_video_list(VIDEOS_FILE)
    return render_template("videos.html", videos=video_list)


@app.route("/videos/<int:target_id>", methods=["GET", "POST"])
def video(target_id):
    target_video = functions_json.get_video(target_id, VIDEOS_FILE)

    # Si aucune vidéo ayant l'id n'a été trouvée, redirige vers la liste des vidéos.
    if target_video is None:
        return redirect(url_for('videos'))

    # Cherche une vidéo avec l'id écrit dans l'url.
    if request.method == "GET":
        return render_template("video.html", video=target_video)

    if request.method == "POST":
        if "modify" in request.form:
            target_video["title"] = request.form["title"]
            functions_json.update_video(target_video, VIDEOS_FILE)
            return render_template("video.html", video=target_video)

        elif "delete" in request.form:
            functions_json.delete_video(target_video, VIDEOS_FILE)
            return redirect(url_for('videos'))

    return redirect(url_for('videos'))


# route GET /videos/search
@app.route('/videos/search', methods=["GET", "POST"])
def search_video():
    # methode devient POST quand le formulaire est validé
    if request.method == "POST":
        # Récupérer les données du formulaire 
        word = request.form['word']
        numberfView = int(request.form['number'])
        # Rechercher une vidéo contenant word dans son titre et un nombre de vue maximum parmi la liste des vidéos
        found_videos = functions_json.search_videos(VIDEOS_FILE,word , numberfView)
        # Afficher les vidéos trouvées
        if found_videos: 
            return render_template("videos.html", videos=found_videos)

        # Revenir à la page du formulaire d'ajout
        return redirect(url_for('home'))
    
    # methode devient GET quand la page s'affiche
    if request.method == "GET":
        return render_template('search_video.html')        # cherche et interprète le fichier search_video.html dans le dossier templates/


# Route POST/videos/add  et GET//videos/add
@app.route('/videos/add', methods=["GET", "POST"])
def add_video():
    if request.method == "POST":
        # Récupérer les données du formulaire 
        title = request.form['title']
        url = request.form['url']
        # Lire le fichier videos.json et renvoie une liste des videos
        video_list = functions_json.get_video_list(VIDEOS_FILE)
        # Créer une nouvelle ID
        new_id = functions_json.create_new_id(video_list)
        # Ajouter la nouvelle vidéo à la liste des vidéos
        video_list = functions_json.add_video_into_list(video_list, new_id, title, url)
        # enregistrer la liste des vidéos dans le fichier videos.json 
        # et afficher le message de réussite
        print(functions_json.save_video_list(video_list, VIDEOS_FILE))
        # revenir à la page du formulaire d'ajout
        return redirect(url_for('home'))
    
    if request.method == "GET":
        return render_template('add_video.html')        # cherche et interprète le fichier add_video.html dans le dossier templates/


if __name__ == '__main__':                          # permet d’exécuter le code à l’intérieur uniquement si ce fichier est lancé directement
    app.run(debug=True)                             # Démarre le serveur de développement Flask et active le mode debug : rechargement automatique à chaque modification du code, affichage d’erreurs détaillées si un bug se produit.