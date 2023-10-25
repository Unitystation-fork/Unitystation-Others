[![forthebadge cc-by](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0) [![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/tyJX8dx)

## Wiki2MD - Convertisseur de Wikimedia à Markdown

### Langage utilisé
Python

-------------

### Description du projet
Wiki2MD est un ensemble de scripts Python qui permet de convertir du contenu Wiki (wikicode) en fichiers Markdown. 
Il est utile pour la conversion de contenu provenant de MediaWiki en Markdown, ce qui facilite la gestion et la publication de contenu.

### Crédit, participants, organisation
Le projet est géré par l'équipe de développement de Unionrolistes. 

Pour consulter la liste des contributeurs, veuillez vous référer au fichier `Credit.md`. 
Vous trouverez également des informations sur la licence dans le fichier `Licence.md`.

- [Credit](Credit.md)

**Licence** : [Licence](Licence.md)


-------------

### But du projet / public cible
Wiki2MD se compose de deux scripts principaux :

#### Extract.py
Le script `Extract.py` permet de télécharger le contenu d'une page Wikimedia spécifiée par l'utilisateur et de le convertir en fichier Markdown.


#### Wiki2MD.py
Le script `Wiki2MD.py` est l'outil principal pour la conversion de contenu Wikimedia en Markdown. 

Il offre des fonctionnalités avancées pour gérer la conversion de fichiers individuels ou de répertoires entiers de contenu Wikimedia.

-------------

### Installation
Pour installer les dépendances requises, utilisez la commande suivante :

```bash
pip install beautifulsoup4
```

[![forthebadge cc-by](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0) [![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/tyJX8dx)


---

### Description du projet
Wiki2MD est un outil de ligne de commande qui permet de convertir des pages Wikimedia (wikicode) en fichiers Markdown. 
Cet outil facilite la conversion de contenu Wikimedia en Markdown pour une utilisation dans la documentation, les pages web et d'autres applications.

---

### Crédits, Participants, Organisation
Projet géré par l'équipe de développement d'Unionrolistes.
---

### Objectif du projet / Public cible
#### Extract.py
Le script `Extract.py` permet de télécharger le contenu d'une page Wikimedia spécifiée par l'utilisateur et de le convertir en fichier Markdown.

#### Wiki2MD.py
Le script `Wiki2MD.py` est l'outil principal pour la conversion de contenu Wikimedia en Markdown. Il offre des fonctionnalités avancées pour gérer la conversion de fichiers individuels ou de répertoires entiers de contenu Wikimedia.

---

### Installation
Pour installer Wiki2MD, suivez ces étapes :

```bash
mkdir ~/Wiki2MD && wget https://raw.githubusercontent.com/Unitystation-fork/Unitystation-Others/main/Wikimedia-to-Markdown/Extract.py -O ~/Wiki2MD/Extract.py && wget https://raw.githubusercontent.com/Unitystation-fork/Unitystation-Others/main/Wikimedia-to-Markdown/Wiki2MD.py -O ~/Wiki2MD/Wiki2MD.py
```

### Utilisation
#### Extract.py

```bash
python3 Extract.py
```

Suivez les instructions pour entrer l'URL de la page cible.
attnetion, il faut copier l'url depuis la page "sources" de wiki

#### Wiki2MD.py

Pour convertir un fichier individuel :

```bash
python3 Wiki2MD.py chemin_du_fichier_wikicode.wiki chemin_du_fichier_markdown.md
```

Pour convertir un répertoire entier de fichiers wikicode :
```bash
python3 Wiki2MD.py chemin_du_répertoire_wikicode chemin_du_répertoire_markdown
```
Fonctionne également si vous ne donner pas de chemin, le bash vous demandera alors où est l'imput et l'output

Fonctionne avec`./` 

