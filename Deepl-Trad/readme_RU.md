[![forthebadge cc-by](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by/4.0)
[![](https://img.shields.io/badge/Discord-7289DA?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/tyJX8dx)
![Версия Python](https://img.shields.io/badge/Python-3.8-blue)
## Deepl-Trad

### Используемый язык

Python

-------------

### Описание проекта

Deepl-Trad - это инструмент перевода, основанный на API DeepL. Он переводит тексты и документы с одного языка на другой, используя мощную технологию перевода DeepL.

### Кредит, участники, организация

Управляется командой разработчиков Unionrolistes.

- Список участников](Credit.md)
- Лицензия](License.md)

-------------

### Цель проекта / целевая аудитория

Целью данного проекта является создание простого и эффективного средства перевода текстов и документов для пользователей, желающих воспользоваться преимуществами технологии перевода DeepL.

Проект ориентирован на разработчиков, индивидуальных пользователей и всех, кто интересуется вопросами перевода текстов.

-------------

### Установка

Для установки Deepl-Trad выполните следующие действия:

1. sudo apt update ; sudo apt full-upgrade ; sudo apt install python3 ; sudo apt autoremove
1. `mkdir -p ~/.config/Deepl/ && mkdir -p ~/.config/Deepl/Result/ && mkdir -p ~/Deepl/ && wget -O ~/Deepl/Deepl-Trad.py https://raw.githubusercontent.com/Unitystation-fork/Unitystation-Others/main/Deepl-Trad/Deepl-trad.py && touch ~/.config/Deepl/Key.txt && touch ~/.config/Deepl/Deepl-Counter.txt` 3.
3. `pip install deepl`
4. Измените файл `~/.config/Deepl/Key.txt` (с помощью nano или geany)

-------------

### Обновление


-------------

### Использование

Для использования Deepl-Trad запустите скрипт с помощью следующих команд:

- Для перевода файла в формате Markdown: `python Deepl-Trad.py ./file.md`.
- Для перевода каталога: `python Deepl-Trad.py ./Folder/`.

Результат будет сохранен в файлах формата "Name_Lang.md", где "Name" - имя исходного файла или каталога, а "Lang" - выбранный язык.
`~/Deepl/Result/`

---

### Как внести свой вклад

Если вы хотите внести свой вклад в этот проект, вы можете :

1. [Форк репозитория] (https://github.com/votre-utilisateur/Deepl-Trad/fork).
2. Создать ветку для своего вклада: `git checkout -b my-contribution`.
3. Внесите свои изменения и зафиксируйте их.
4. Переместите изменения в свою ветку: `git push origin my-contribution`.
5. Создайте [pull request](https://github.com/votre-utilisateur/Deepl-Trad/compare) с подробным описанием ваших изменений.

Мы ценим ваш вклад!

-------------
