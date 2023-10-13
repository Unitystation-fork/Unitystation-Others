import os
import requests
from bs4 import BeautifulSoup

# Chemin du fichier de compteur
compteur_file = "/home/dae/Deepl-Compteur.txt"

# Chemin du fichier de clé API DeepL
deepl_api_key_path = os.path.expanduser("~/.config/Deepl/Key.txt")

if os.path.isfile(deepl_api_key_path):
    with open(deepl_api_key_path, 'r') as f:
        deepl_api_key = f.read().strip()
else:
    print("Erreur : Le fichier key.txt est introuvable dans ~/.config/Deepl/")
    print("Veuillez créer un fichier key.txt dans ce répertoire avec votre clé API DeepL.")
    exit(1)  # Arrêter le script en cas d'erreur

# Fonction pour récupérer la valeur du compteur de mots
def get_word_count():
    if os.path.exists(compteur_file):
        with open(compteur_file, "r") as f:
            return int(f.read())
    else:
        # Si le fichier n'existe pas, le compteur est à zéro
        return 0

# Fonction pour mettre à jour le compteur de mots
def update_word_count(count):
    with open(compteur_file, "w") as f:
        f.write(str(count)

# Fonction pour traduire un texte avec DeepL
def translate_with_deepl(text, target_lang):
    if not deepl_api_key:
        print("Veuillez spécifier une clé API DeepL valide.")
        return

    url = "https://api.deepl.com/v2/translate"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
    }
    data = {
        "auth_key": deepl_api_key,
        "text": text,
        "target_lang": target_lang,
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        response_data = response.json()
        translation = response_data.get("translations", [{}])[0].get("text", "")
        return translation
    else:
        print("Erreur lors de la traduction :", response.status_code)
        return ""

# Récupérer la valeur actuelle du compteur
current_word_count = get_word_count()
print("Nombre de mots disponibles:", current_word_count)

# Texte à traduire
text_to_translate = "Ceci est un exemple de texte à traduire."

# Langue cible pour la traduction (par exemple, "FR" pour le français)
target_language = "FR"

# Traduire le texte
translated_text = translate_with_deepl(text_to_translate, target_language)

if translated_text:
    print("Texte traduit :", translated_text)

    # Calculer le nombre de mots dans le texte source
    word_count = len(text_to_translate.split())
    print("Nombre de mots dans le texte source :", word_count)

    # Mettre à jour le compteur de mots
    current_word_count -= word_count
    print("Nouveau nombre de mots disponibles :", current_word_count)
    update_word_count(current_word_count)
else:
    print("La traduction a échoué.")
