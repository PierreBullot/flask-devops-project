from flask import Flask, render_template, request, redirect, url_for
import functions_json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    video_list = functions_json.get_video_list()
    return render_template("videos.html", videos=video_list)


@app.route("/videos/<int:target_id>", methods=["GET", "POST"])
def video(target_id):
    target_video = functions_json.get_video(target_id)

    # Si aucune vidéo ayant l'id n'a été trouvée, redirige vers la liste des vidéos.
    if target_video is None:
        return redirect(url_for('videos'))


    # Cherche une vidéo avec l'id écrit dans l'url.
    if request.method == "GET":
        return render_template("video.html", video=target_video)

    if request.method == "POST":
        if "modify" in request.form:
            target_video["title"] = request.form["title"]
            functions_json.update_video(target_video)
            return render_template("video.html", video=target_video)

        elif "delete" in request.form:
            functions_json.delete_video(target_video)
            return redirect(url_for('videos'))

    return redirect(url_for('videos'))

