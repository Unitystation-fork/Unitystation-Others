## Extract.py
import os
import requests
from bs4 import BeautifulSoup

# Vérifier et créer le dossier Result s'il n'existe pas
result_dir = "./Result"
os.makedirs(result_dir, exist_ok=True)

# Demander à l'utilisateur l'URL de la page cible
url = input("Entrez l'URL de la page : ")

# Télécharger le contenu de la page en utilisant requests
response = requests.get(url)
if response.status_code != 200:
    print("La requête a échoué. Vérifiez l'URL ou votre connexion Internet.")
    exit(1)

# Analyser le contenu HTML de la page
soup = BeautifulSoup(response.text, 'html.parser')

# Extraire le titre de la page
title = soup.find('div', {'id': 'contentSub'}).find('a').get('title')

# Remplacer les espaces par des caractères de soulignement (_)
title = title.replace(' ', '_')

# Extraire le code source de la page
textarea = soup.find('textarea', {'name': 'wpTextbox1'})
if textarea:
    wikicode = textarea.get_text()
else:
    print("La balise textarea n'a pas été trouvée.")
    exit(1)

# Supprimer les balises <textarea> inutiles
wikicode = wikicode.replace('<textarea readonly="readonly" accesskey="," id="wpTextbox1" cols="80" rows="25" style="" class="mw-editfont-monospace" lang="en" dir="ltr" name="wpTextbox1">', '')
wikicode = wikicode.replace('</textarea>', '')

# Enregistrer le code source dans le fichier résultat
output_filename = os.path.join(result_dir, title + ".wiki")
with open(output_filename, 'w', encoding='utf-8') as output_file:
    output_file.write(wikicode)

# Afficher un message de confirmation en jaune
print("\033[93mExtraction réussie. Le code source a été enregistré dans " + output_filename + ".\033[0m")
