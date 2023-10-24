[![forthebadge cc-by](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0)
[![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/tyJX8dx)
![Python Version](https://img.shields.io/badge/Python-3.8-blue)
## Deepl-Trad

### Langage utilisé

Python

-------------

### Description du projet

Deepl-Trad est un outil de traduction basé sur l'API DeepL. Il permet de traduire du texte et des documents d'une langue à une autre en utilisant la puissante technologie de traduction de DeepL.

### Crédit, participants, organisation

Géré par l'équipe de développement de Unionrolistes.

- [Liste des contributeurs](Credit.md)
- [Licence](Licence.md)

-------------

### But du projet / public cible

Le but de ce projet est de fournir un moyen simple et efficace de traduire du texte et des documents pour les utilisateurs qui souhaitent tirer parti de la technologie de traduction de DeepL.

Ce projet s'adresse aux développeurs, aux utilisateurs individuels et à toute personne intéressée par la traduction de texte.

-------------

### Installation

Pour installer Deepl-Trad, suivez ces étapes :

1. sudo apt update ; sudo apt full-upgrade ; sudo apt install python3 ; sudo apt autoremove
1. `mkdir -p ~/.config/Deepl/ && mkdir -p ~/.config/Deepl/Result/ && mkdir -p ~/Deepl/ && wget -O ~/Deepl/Deepl-Trad.py https://raw.githubusercontent.com/Unitystation-fork/Unitystation-Others/main/Deepl-Trad/Deepl-trad.py && touch ~/.config/Deepl/Key.txt && touch ~/.config/Deepl/Deepl-Compteur.txt`
3. `pip install deepl`
4. Modifier le fichier `~/.config/Deepl/Key.txt` (avec nano ou geany)

-------------

### Mise à jour


-------------

### Utilisation

Pour utiliser Deepl-Trad, exécutez le script avec les commandes suivantes :

- Pour traduire un fichier Markdown : `python Deepl-Trad.py ./fichier.md`
- Pour traduire un répertoire : `python Deepl-Trad.py ./Dossier/`

Le résultat sera enregistré dans des fichiers avec le format "Nom_Lang.md", où "Nom" est le nom du fichier ou du répertoire d'origine, et "Lang" est la langue choisie.
`~/Deepl/Result/`

---

### Comment contribuer

Si vous souhaitez contribuer à ce projet, vous pouvez :

1. [Forker le référentiel](https://github.com/votre-utilisateur/Deepl-Trad/fork).
2. Créer une branche pour votre contribution : `git checkout -b ma-contribution`.
3. Faites vos modifications et committez-les.
4. Pousser vos modifications vers votre fork : `git push origin ma-contribution`.
5. Créer une [demande d'extraction](https://github.com/votre-utilisateur/Deepl-Trad/compare) avec une description détaillée de vos modifications.

Nous apprécions vos contributions !

-------------
