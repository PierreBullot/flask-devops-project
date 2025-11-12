from flask import Flask, render_template, request
import json

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    with open("videos.json", mode="r", encoding="utf-8") as videos_file:
        video_list = json.load(videos_file)
    return render_template("videos.html", videos=video_list)


@app.route("/videos/<int:target_id>", methods=["GET", "PUT", "DELETE"])
def video(target_id):
    if request.method == "GET":
        with open("videos.json", mode="r", encoding="utf-8") as videos_file:
            videos_data = json.load(videos_file)
            for video_data in videos_data:
                if video_data["id"] == target_id:
                    target_video = video_data
                    return render_template("video.html", video=target_video)

    video_list = [{"title": "test"}, {"title": "placeholder"}, {"title": "simple"}]
    return render_template("videos.html", videos=video_list)

    # with open("hello_frieda.json", mode="w", encoding="utf-8") as write_file:
    #     json.dump(dog_data, write_file)
