# function_json.py
import os
import json

# def get_video_list():
#     with open("videos.json", mode="r", encoding="utf-8") as videos_file:
#         return json.load(videos_file)

def get_video_list(file_path):
    """Lit le fichier JSON et renvoie une liste de vidéos."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as data:
            try:
                videos = json.load(data)                       # lit le contenu du fichier JSON et le convertit en objet Python
            except json.JSONDecodeError:                    # Le fichier existe mais est vide ou corrompu
                videos = []                                 # initialise une liste vide
    else:
        videos = []                                         # initialise une liste vide
    return videos

def get_video(target_id, file_path):
    video_list = get_video_list(file_path)
    for video in video_list:
        if video["id"] == target_id:
            return video
    return None

def create_new_id(video_list):
    """Crée une nouvelle ID."""
    new_id = 0                    # valeur par défaut si la liste est vide
    for v in video_list:
        if v['id'] > new_id:
            new_id = v['id']      # recherche de la plus grande valeur de ID
    return new_id + 1


def save_video_list(video_list, FILE_JSON):
    """Ecrire la liste des vidéos dans un fichier .json"""
    with open(FILE_JSON, mode="w", encoding="utf-8") as f:          # ouvre le fichier .json (FILE_JSON) appelé "f", en mode écriture (effacera le contenu précédent)
        json.dump(video_list, f, indent=4, ensure_ascii=False)      # convertit la liste des vidéos (video_list) en texte JSON, ajoute une identation de 4 pour le formatage,
    return "Vidéo ajoutée avec succès !"                                                                # garde les caractères accentués sans les convertir en code Unicode et écrit-la dans le fichier appelé "f"


def add_video_into_list(video_list, new_id, new_title, new_url):
    """Ajoute une nouvelle vidéo à la liste des vidéos"""
    new_video = {
        "id": new_id,
        "title": new_title,
        "url": new_url,
        "views": 0,
    }
    video_list.append(new_video)
    return video_list

def update_video(target_video, file_path):
    video_list = get_video_list(file_path)
    for video in video_list:
        if video["id"] == target_video["id"]:
            video["url"] = target_video["url"]
            video["title"] = target_video["title"]
            video["views"] = target_video["views"]
            break
    save_video_list(video_list)

    