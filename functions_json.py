import os
import json


def get_video_list(file_path):
    """Lit le fichier JSON et renvoie une liste de vidéos."""
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as data:
            try:
                videos = json.load(data)                    # lit le contenu du fichier JSON et le convertit en objet Python
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


def save_video_list(video_list, target_file):
    """Ecrire la liste des vidéos dans un fichier .json"""
    with open(target_file, mode="w", encoding="utf-8") as f:        # ouvre le fichier .json (target_file) appelé "f", en mode écriture (effacera le contenu précédent)
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

    save_video_list(video_list, file_path)


def delete_video(target_video, file_path):
    video_list = get_video_list(file_path)
    for index, video in enumerate(video_list):
        if video["id"] == target_video["id"]:
            video_list.pop(index)
            break

    save_video_list(video_list, file_path)


def search_videos(file_path, word, numberOfView):
    """
    Recherche les vidéos selon leur titre ou une partie de leur titre et/ou
    dont leur nombre de vues est inférieur ou égal à celui indiqué.
    """
    # Si aucun critère n’est défini
    if word =="" and numberOfView == 0:
        return []
    # Charger le fichier JSON
    video_list = get_video_list(file_path)

    # Mise en forme du mot-clé : tout en minuscule, pas d'espace en premier ou en dernier
    word = word.lower().strip()

    results = []

    for video in video_list:
        # si word n'est pas vide
        if word:
            title_match = word in video["title"].lower()    # le titre est valide (true) si word est dans title, sinon invalide (false)
        else:
            title_match = True                              # si word est vide alors le titre est valide (true)

        # si numberOfView n'est pas nul
        if numberOfView > 0:
            views_match = video["views"] <= numberOfView    #  la vue est valide (true) si elle est <= à numberOfView, sinon invalide (false)
        else:
            views_match = True                              # si numberOfView est nul alors la vue est valide (true)

        # si les deux critères sont données :
        if word and numberOfView > 0:
            if title_match and views_match:
                results.append(video)
        # si seul une partie du titre est donné :
        elif word and numberOfView == 0:
            if title_match:
                results.append(video)
        # si seul le nombre de vue est donné :
        elif not word and numberOfView > 0:
            if views_match:
                results.append(video)

    return results
