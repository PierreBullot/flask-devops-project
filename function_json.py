# function_json.py
import os
import json

def get_video_list(file_path):
    """Lit le fichier JSON et renvoie une liste de vidéos."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            try:
                videos = json.load(f)                       # lit le contenu du fichier JSON et le convertit en objet Python
            except json.JSONDecodeError:                    # Le fichier existe mais est vide ou corrompu
                videos = []                                 # initialise une liste vide
    else:
        videos = []                                         # initialise une liste vide
    return videos

def create_new_id(videos_file):
    """Crée une nouvelle ID."""
    new_id = 0                    # valeur par défaut si la liste est vide
    for v in videos_file:
        if v['id'] > new_id:
            new_id = v['id']      # recherche de la plus grande valeur de ID
    return new_id + 1

