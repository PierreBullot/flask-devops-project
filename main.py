from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/videos")
def videos():
    video_list = ["test", "placeholder", "simple"]
    return render_template("videos.html", videos=video_list)
