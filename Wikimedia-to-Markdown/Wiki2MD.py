# ecrit via Chat-GPT, conversion de wikicode vers MD par Fr_Dae pour Unionrolistes.fr / unitystation-fork
# CCBYNA
import re
import sys
import os

def convert_wikicode_to_markdown(wikicode):
	# Convertir les en-têtes
	wikicode = re.sub(r'==(.*?)==', r'# \1', wikicode)
	wikicode = re.sub(r'===(.*?)===', r'## \1', wikicode)
	wikicode = re.sub(r'====(.*?)====', r'### \1', wikicode)
	wikicode = re.sub(r'=====(.*?)=====', r'#### \1', wikicode)
	wikicode = re.sub(r'======(.*?)======', r'##### \1', wikicode)
	wikicode = re.sub(r'=======(.*?)=======', r'###### \1', wikicode)

	# Convertir les listes à puces
	wikicode = re.sub(r'^\* ', r'* ', wikicode, flags=re.MULTILINE)
	# Convertir les listes numérotées
	wikicode = re.sub(r'^# ', r'1. ', wikicode, flags=re.MULTILINE)
	
	# Convertir les liens
	wikicode = re.sub(r'\[\[([^\]]+?)\]\]', r'[\1](\1)', wikicode)
	# Convertir les images
	wikicode = re.sub(r'\[\[File:([^\]]+?)\]\]', r'![\1](\1)', wikicode)
	# Convertir les liens internes
	wikicode = re.sub(r'\[\[([^\]]+?)\]\]', r'[\1](\1)', wikicode)
	# Convertir les liens internes personnalisés en balises de lien Markdown
	wikicode = re.sub(r'\[\[([^|]+)\|([^]]+)\]\]', r'[\2](\1)', wikicode)
	# Convertir les liens externes
	wikicode = re.sub(r'\[([^\]]+?)\]', r'[\1]', wikicode)
	# Convertir les citations
	wikicode = re.sub(r'<ref(.*?)<\/ref>', r'[\1]', wikicode)
	
	# Convertir le gras
	wikicode = re.sub(r"'''(.*?)'''", r'**\1**', wikicode)
	# Convertir l'italique
	wikicode = re.sub(r"''(.*?)''", r'*\1*', wikicode)
	# Convertir le texte souligné en Markdown
	wikicode = re.sub(r'<u>(.*?)</u>', r'__\1__', wikicode)
	# Convertir le texte barré en Markdown
	wikicode = re.sub(r'<s>(.*?)</s>|<strike>(.*?)</strike>', r'~~\1\2~~', wikicode)

	# Supprimer les balises de commentaires
	wikicode = re.sub(r'<!--(.*?)-->', r'', wikicode)
	# Convertir les balises de texte préformaté en balises de code Markdown
	wikicode = re.sub(r'<pre>(.*?)</pre>', r'```\1```', wikicode)

	# Convertir les tables (exemples simples)
	wikicode = re.sub(r'{|', r'\n| ', wikicode)
	wikicode = re.sub(r'|}', r' |', wikicode)
	wikicode = re.sub(r'|-', r'\n|', wikicode)
	wikicode = re.sub(r'!', r'|', wikicode)

	return wikicode

def convert_file(input_file, output_file):
	try:
		with open(input_file, 'r', encoding='utf-8') as file:
			wikicode_text = file.read()

		markdown_text = convert_wikicode_to_markdown(wikicode_text)

		with open(output_file, 'w', encoding='utf-8') as file:
			file.write(markdown_text)

		print(f"Conversion terminée. Fichier Markdown généré avec succès : {output_file}")
	except FileNotFoundError:
		print("Le fichier d'entrée n'a pas été trouvé.")
	except Exception as e:
		print(f"Une erreur s'est produite : {str(e)}")

def convert_files_in_directory(input_directory, output_directory):
	if not os.path.exists(output_directory):
		os.makedirs(output_directory)

	for filename in os.listdir(input_directory):
		if filename.endswith(".wiki"):
			input_file = os.path.join(input_directory, filename)
			output_file = os.path.join(output_directory, filename.replace(".wiki", ".md"))

			convert_file(input_file, output_file)

if __name__ == "__main__":
	main()
