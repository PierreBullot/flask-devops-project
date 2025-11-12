from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    video_list = ["test", "placeholder", "simple"]
    return render_template("videos.html", videos=video_list)


# Route GET /videos/add
@app.route('/videos/add', methods=['GET'])          # GET : lecture/affichage
def add_video():
    return render_template('add_video.html')        # cherche et interprète le fichier add_video.html dans le dossier templates/

if __name__ == '__main__':                          # permet d’exécuter le code à l’intérieur uniquement si ce fichier est lancé directement
    app.run(debug=True)                             # Démarre le serveur de développement Flask et active le mode debug : rechargement automatique à chaque modification du code, affichage d’erreurs détaillées si un bug se produit.