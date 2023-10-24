##Count.sh
#!/bin/bash

# Chemin du fichier de clé API DeepL
DEEPL_API_KEY_FILE="$HOME/.config/Deepl/Key.txt"

if [ -f "$DEEPL_API_KEY_FILE" ]; then
    # Lire la clé API depuis le fichier
    DEEPL_AUTH_KEY=$(cat "$DEEPL_API_KEY_FILE")

    # Utiliser la clé pour faire une requête à l'API DeepL et enregistrer la réponse dans un fichier JSON
    DEEPL_RESPONSE=$(curl -sS -X GET 'https://api-free.deepl.com/v2/usage' --header "Authorization: DeepL-Auth-Key $DEEPL_AUTH_KEY")

    # Chemin du fichier de compteur
    DEEPL_COUNT_FILE="$HOME/.config/Deepl/Deepl-Count.json"

    # Formater la réponse JSON avec sed pour mettre le resultat sur plusieurs lignes
    echo "$DEEPL_RESPONSE" | sed 's/{/{\n/g; s/,/,\n/g; s/}/\n}/g' > "$DEEPL_COUNT_FILE"

    echo "Réponse de l'API enregistrée dans $DEEPL_COUNT_FILE"
else
    echo "Erreur : Le fichier Key.txt est introuvable dans ~/.config/Deepl/"
    echo "Veuillez créer un fichier Key.txt dans ce répertoire avec votre clé API DeepL."
    exit 1
fi


#!/bin/bash

# Chemin du fichier de clé API DeepL
DEEPL_API_KEY_FILE="$HOME/.config/Deepl/Key.txt"
DEEPL_COUNT_FILE="$HOME/.config/Deepl/Deepl-Count.json"

# Fonction pour afficher un message d'erreur et quitter le script
exit_with_error() {
    echo "Erreur : $1"
    exit 1
}

# Vérifier si le fichier de clé API existe
if [ ! -f "$DEEPL_API_KEY_FILE" ]; then
    exit_with_error "Le fichier Key.txt est introuvable dans ~/.config/Deepl/. Veuillez le créer avec votre clé API DeepL."
fi

# Lire la clé API depuis le fichier
DEEPL_AUTH_KEY=$(cat "$DEEPL_API_KEY_FILE")

# Effectuer une requête à l'API DeepL et enregistrer la réponse dans un fichier JSON
DEEPL_RESPONSE=$(curl -sS -X GET 'https://api-free.deepl.com/v2/usage' --header "Authorization: DeepL-Auth-Key $DEEPL_AUTH_KEY")

# Vérifier si la requête a réussi en vérifiant la présence de données JSON valides
if [ -z "$DEEPL_RESPONSE" ]; then
    exit_with_error "La requête à l'API DeepL n'a pas abouti. Vérifiez votre clé API et la connexion Internet."
fi

# Formater la réponse JSON pour une meilleure lisibilité
formatted_response=$(echo "$DEEPL_RESPONSE" | jq '.')

# Vérifier si jq est disponible pour formater la réponse JSON
if [ -z "$formatted_response" ]; then
    exit_with_error "L'outil jq n'est pas installé. Installez jq pour une meilleure lisibilité des données JSON."
fi

# Écrire la réponse JSON formatée dans le fichier DEEPL_COUNT_FILE
echo "$formatted_response" > "$DEEPL_COUNT_FILE"

echo "Réponse de l'API enregistrée dans $DEEPL_COUNT_FILE"
