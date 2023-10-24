## Extract.sh 
#!/bin/bash

# Demander à l'utilisateur l'URL de la page cible
read -p "Entrez l'URL de la page : " url

# Télécharger le contenu de la page en utilisant wget
wget -q -O page.html "$url"

# Extraire le code source de la page en utilisant sed
sed -n '/<textarea/,/<\/textarea>/p' page.html > code_source.html

# Supprimer les balises <textarea> inutiles
sed -i 's/<textarea[^>]*>//g' code_source.html
sed -i 's/<\/textarea>//g' code_source.html

# Demander à l'utilisateur de fournir le nom du fichier de sortie
read -p "Entrez le nom du fichier de sortie (avec l'extension .wikicode) : " output_filename

# Renommer le fichier code_source.html en <nom>.wikicode
mv code_source.html "$output_filename"

# Vérifier et créer le dossier Result s'il n'existe pas
result_dir="./Result"
mkdir -p "$result_dir"

# Déplacer le fichier de sortie dans le dossier Result
mv "$output_filename" "$result_dir/$output_filename"

# Supprimer le fichier temporaire page.html
rm page.html

# Afficher un message de confirmation en jaune
echo -e "\e[33mExtraction réussie.\e[0m Le code source a été enregistré dans $result_dir/$output_filename."
