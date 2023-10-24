[![forthebadge cc-by](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0)
[![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/tyJX8dx)
![Python Version](https://img.shields.io/badge/Python-3.8-blue)
## Deepl-Trad

### Language used

Python

-------------

### Project description

Deepl-Trad is a translation tool based on the DeepL API. It translates text and documents from one language to another using DeepL's powerful translation technology.

### Credit, participants, organisation

Managed by the Unionrolistes development team.

- List of contributors](Credit.md)
- License](License.md)

-------------

### Aim of the project / target audience

The aim of this project is to provide a simple and effective means of translating text and documents for users who wish to take advantage of the translation technology of DeepL.

The project is aimed at developers, individual users and anyone with an interest in text translation.

-------------

### Installation

To install Deepl-Trad, follow these steps:

1. sudo apt update ; sudo apt full-upgrade ; sudo apt install python3 ; sudo apt autoremove
1. `mkdir -p ~/.config/Deepl/ && mkdir -p ~/.config/Deepl/Result/ && mkdir -p ~/Deepl/ && wget -O ~/Deepl/Deepl-Trad.py https://raw.githubusercontent.com/Unitystation-fork/Unitystation-Others/main/Deepl-Trad/Deepl-trad.py && touch ~/.config/Deepl/Key.txt && touch ~/.config/Deepl/Deepl-Counter.txt` 3.
3. `pip install deepl`
4. Modify the `~/.config/Deepl/Key.txt` file (using nano or geany)

-------------

### Update


-------------

### Use

To use Deepl-Trad, run the script with the following commands:

- To translate a Markdown file: `python Deepl-Trad.py ./file.md`.
- To translate a directory: `python Deepl-Trad.py ./Folder/`

The result will be saved in files with the format "Name_Lang.md", where "Name" is the name of the original file or directory, and "Lang" is the chosen language.
`~/Deepl/Result/`

---

### How to contribute

If you would like to contribute to this project, you can :

1. [Fork the repository](https://github.com/votre-utilisateur/Deepl-Trad/fork).
2. Create a branch for your contribution: `git checkout -b my-contribution`.
3. Make your changes and commit them.
4. Push your changes to your fork: `git push origin my-contribution`.
5. Create a [pull request](https://github.com/votre-utilisateur/Deepl-Trad/compare) with a detailed description of your changes.

We appreciate your contributions!

-------------
