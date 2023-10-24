## Extract.sh 
#!/bin/bash

# Vérifier et créer le dossier Result s'il n'existe pas
result_dir="./Result"
mkdir -p "$result_dir"

# Demander à l'utilisateur l'URL de la page cible
read -p "Entrez l'URL de la page : " url

# Télécharger le contenu de la page en utilisant wget
wget -q -O page.html "$url"

# Extraire le titre de la page en utilisant grep
title=$(grep -oP '<title>.*?</title>' page.html)
title=$(echo "$title" | sed -e 's/<title>//;s/- Unitystation<\/title>//;s/ /_/g')

# Extraire le code source de la page en utilisant sed
sed -n '/<textarea/,/<\/textarea>/p' page.html > code_source.html

# Supprimer les balises <textarea> inutiles
sed -i 's/<textarea[^>]*>//g' code_source.html
sed -i 's/<\/textarea>//g' code_source.html

# Déplacer le fichier code_source.html dans le dossier Result
mv code_source.html "$result_dir/$title.wiki"
mv "$result_dir/View_source_for_"* "$result_dir/${0/View_source_for_/}"

# Supprimer le fichier temporaire page.html
rm page.html

# Afficher un message de confirmation en jaune
echo -e "\e[33mExtraction réussie. Le code source a été enregistré dans $result_dir/$title.wiki.\e[0m"
