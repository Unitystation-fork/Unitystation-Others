##Deepl-trad.py

import os
import deepl
import datetime

# Chemin du fichier de clé API DeepL
deepl_api_key_path = os.path.expanduser("~/.config/Deepl/Key.txt")

if os.path.isfile(deepl_api_key_path):
    with open(deepl_api_key_path, 'r') as f:
        deepl_api_key = f.read().strip()
else:
    print("Erreur : Le fichier key.txt est introuvable dans ~/.config/Deepl/")
    print("Veuillez créer un fichier key.txt dans ce répertoire avec votre clé API DeepL.")
    exit(1)  # Arrêter le script en cas d'erreur


# Chemin du fichier de compteur
compteur_file = "~/.config/Deepl/Deepl-Compteur.txt"

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
        f.write(str(count))

# Fonction pour traduire un texte avec DeepL
def translate_with_deepl(text, source_lang, target_lang):
    translator = deepl.Translator(deepl_api_key)
    result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    return result.text

# Récupérer la valeur actuelle du compteur
current_word_count = get_word_count()
print("Nombre de mots disponibles:", current_word_count)

def reinitialiser_compteur_si_necessaire():
    # Obtenez la date actuelle
    date_actuelle = datetime.datetime.now()
    
    # Si c'est le 13 du mois, réinitialisez le compteur
    if date_actuelle.day == 13:
        # Réinitialisez le compteur à zéro
        compteur = 0
        # Enregistrez la nouvelle valeur du compteur dans un fichier ou une base de données
        enregistrer_compteur(compteur)

def enregistrer_compteur(compteur):
    # Code pour enregistrer la valeur du compteur dans un fichier ou une base de données
    # par exemple, vous pouvez utiliser le module 'open' pour écrire dans un fichier

# Fonction pour traduire un fichier
def translate_file(input_file, source_lang, target_lang):
    with open(input_file, "r") as f:
        text = f.read()

    translated_text = translate_with_deepl(text, source_lang, target_lang)

    # Calculer le nombre de mots dans le texte source
    word_count = len(text.split())

    if current_word_count >= word_count:
        # Si suffisamment de mots sont disponibles, mettre à jour le compteur
        current_word_count -= word_count
        update_word_count(current_word_count)

        # Extraire le nom du fichier (sans extension) ou du répertoire
        file_name, _ = os.path.splitext(os.path.basename(input_file))

        # Créer le nom du fichier traduit
        output_file = f"{file_name}_{target_lang}.md"

        # Écrire le texte traduit dans le fichier de sortie
        with open(output_file, "w") as f:
            f.write(translated_text)

        print(f"Traduction terminée. Fichier traduit: {output_file}")
        print("Nombre de mots utilisés:", word_count)
        print("Nombre de mots restants:", current_word_count)
    else:
        print("Le nombre de mots restants est insuffisant pour la traduction.")
        print("Nombre de mots nécessaires:", word_count)
        print("Nombre de mots disponibles:", current_word_count)

# Demander la langue source
source_lang = input("Langue source (par exemple, FR, EN, DE) : ")

# Demander la langue cible
target_lang = input("Langue cible (par exemple, FR, EN, DE) : ")

# Passer en revue les fichiers dans le répertoire ou traiter le fichier d'entrée
input_path = input("Entrez le chemin vers le fichier ou le répertoire : ")

if os.path.isfile(input_path):
    # Si c'est un fichier, traduire le fichier
    translate_file(input_path, source_lang, target_lang)
elif os.path.isdir(input_path):
    # Si c'est un répertoire, parcourir les fichiers et traduire chaque fichier texte
    for root, _, files in os.walk(input_path):
        for file in files:
            if file.endswith(".md"):
                translate_file(os.path.join(root, file), source_lang, target_lang)
else:
    print("Le chemin spécifié n'existe pas.")

# Afficher le nombre de mots restants après toutes les traductions
print("Nombre de mots restants après les traductions :", current_word_count)
