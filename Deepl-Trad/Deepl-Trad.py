## Deepl-trad.py

import os
import deepl
import json
import subprocess
import sys
import re

# Listes des couleur

def colored_text(text, color_code):
    return f"\033[{color_code}{text}\033[0m"

# print(colored_text("Texte en Gris", "90m"))
# print(colored_text("Texte en Rouge", "91m"))
# print(colored_text("Texte en Vert", "92m"))
# print(colored_text("Texte en Jaune", "93m"))
# 
# print(colored_text("Texte en Bleu", "94m"))
# print(colored_text("Texte en Violet", "95m"))
# print(colored_text("Texte en Cyan", "96m"))
# print(colored_text("Texte en Blanc", "97m"))

# Fonction pour récupérer la valeur du compteur de caractères
def get_character_count(count_file):
    if os.path.exists(count_file):
        with open(count_file, "r") as f:
            data = json.load(f)
            character_count = data.get("character_count", 0)
            return character_count
    else:
        # Si le fichier n'existe pas, le compteur est à zéro
        return 0

# Fonction pour traduire un texte avec DeepL
def translate_with_deepl(text, source_lang, target_lang, auth_key):
    translator = deepl.Translator(auth_key)
    result = translator.translate_text(text, source_lang=source_lang, target_lang=target_lang)
    return result.text

# Fonction pour traduire un fichier
def translate_file(input_file, source_lang, target_lang, auth_key, count_file, shell_script):
    with open(input_file, "r") as f:
        text = f.read()

    translated_text = translate_with_deepl(text, source_lang, target_lang, auth_key)

    # Calculer le nombre de caractères dans le texte source
    current_character_count = get_character_count(count_file)
    character_count = len(text.split())

    if current_character_count >= character_count:
        # Si suffisamment de caractères sont disponibles, mettre à jour le compteur
        current_character_count -= character_count

        # Extraire le nom du fichier (sans extension) ou du répertoire
        file_name, _ = os.path.splitext(os.path.basename(input_file))

        # Créer le chemin du répertoire de résultat
        result_dir = os.path.expanduser('~/Deepl/Result')
        os.makedirs(result_dir, exist_ok=True)  # Créer le répertoire s'il n'existe pas

        # Créer le nom du fichier traduit
        output_file = os.path.join(result_dir, f"{file_name}_{target_lang}.md")

        # Écrire le texte traduit dans le fichier de sortie
        with open(output_file, "w") as f:
            f.write(translated_text)

        print(f"Traduction terminée. Fichier traduit: {output_file}")

        # Exécute le script Shell et capture la sortie
        result = subprocess.run([shell_script], shell=True, capture_output=True, text=True)

        # Affiche la sortie standard (stdout) de la commande
        print("Sortie de la commande Shell:")
        print(result.stdout)

        # Affiche la sortie d'erreur standard (stderr) de la commande
        print(colored_text("Erreur de la commande Shell:", "91m"))
        print(result.stderr)
        
        print("Nombre de caractères utilisés:", character_count)
        print("Nombre de caractères restants:", current_character_count)
    else:
        print(colored_text("Le nombre de caractères restants est insuffisant pour la traduction.", "91m"))
        print("Nombre de caractères nécessaires:", character_count)
        print("Nombre de caractères disponibles:", current_character_count)

def main():
    # Chemin du fichier de clé API DeepL
    deepl_api_key_path = os.path.expanduser("~/.config/Deepl/Key.txt")

    if os.path.isfile(deepl_api_key_path):
        with open(deepl_api_key_path, 'r') as f:
            DEEPL_AUTH_KEY = f.read().strip()
    else:
        print(colored_text("Erreur : Le fichier Key.txt est introuvable dans ~/.config/Deepl/", "91m"))
        print(colored_text("Veuillez créer un fichier Key.txt dans ce répertoire avec votre clé API DeepL.", "91m"))
        return  # Arrêter le script en cas d'erreur

    # Chemin du fichier de compteur
    count_file = os.path.expanduser("~/.config/Deepl/Deepl-Count.json")

    # Chemin vers le script Shell
    shell_script = "~/Deepl/Count.sh"

    # Demander la langue source
    # source_lang = input("Langue source (par exemple, FR, EN, DE) : ")
    source_lang_prompt = "Langue source (par exemple, FR, EN, DE) : "
    source_lang_prompt = re.sub(r'\bsource\b', colored_text('source','93m'), source_lang_prompt)
    source_lang = input(source_lang_prompt)

    # Demander la langue cible
    # target_lang = input("Langue cible (par exemple, FR, EN, DE) : ")
    target_lang_prompt = "Langue cible (par exemple, FR, EN, DE) : "
    target_lang_prompt = re.sub(r'\bcible\b', colored_text('cible','93m'), target_lang_prompt)
    target_lang = input(target_lang_prompt)
    
    # Passer en revue les fichiers dans le répertoire ou traiter le fichier d'entrée
    input_path_prompt = "Entrez le chemin vers le fichier ou le répertoire INPUT : "
    input_path_prompt = re.sub(r'\bINPUT\b', colored_text('INPUT','91m'), input_path_prompt)
    input_path = input(input_path_prompt)

    if os.path.isfile(input_path):
        # Si c'est un fichier, traduire le fichier
        translate_file(input_path, source_lang, target_lang, DEEPL_AUTH_KEY, count_file, shell_script)
    elif os.path.isdir(input_path):
        # Si c'est un répertoire, parcourir les fichiers et traduire chaque fichier texte
        for root, _, files in os.walk(input_path):
            for file in files:
                if file.endswith(".md"):
                    translate_file(os.path.join(root, file), source_lang, target_lang, DEEPL_AUTH_KEY, count_file, shell_script)
    else:
        print(colored_text("Le chemin spécifié n'existe pas.", "91m"))

if __name__ == "__main__":
    main()
