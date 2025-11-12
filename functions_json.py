import json


def get_video_list():
    with open("videos.json", mode="r", encoding="utf-8") as videos_file:
        return json.load(videos_file)


def get_video(target_id):
    video_list = get_video_list()
    for video in video_list:
        if video["id"] == target_id:
            return video

    return None


def save_video_list(video_list):
    with open("videos.json", mode="w", encoding="utf-8") as videos_file:
        json.dump(video_list, videos_file)


def update_video(target_video):
    video_list = get_video_list()
    for video in video_list:
        if video["id"] == target_video["id"]:
            video["url"] = target_video["url"]
            video["title"] = target_video["title"]
            video["views"] = target_video["views"]
            break

    save_video_list(video_list)



