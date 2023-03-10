== Importer la scene Communautaire Unitystation ==

	Ce tutoriel a pour objectif de vous guider pas à pas dans l'importation d'UNE scène pré-faite sur OBS Studio(sans modifier votre collection de scene actuelle). 
	En suivant ces instructions, vous pourrez facilement ajouter une scène "face-cam confessionnal" de type reality show à votre collection de scènes. 
	La scène sera commune à tous les streamers participant au projet communautaire UnityStation.
	(vous trouverez un aperçu dans le fichier "Result.png"
	
=== Scène UnityStation ===

    Téléchargez le fichier zip contenant la scène.
    Placez le zip dans le dossier %USERPROFILE%\image\OBS\. Si le dossier n'existe pas, créez-le en respectant les majuscules.
    Décompressez le zip avec un clic droit "extraire ici" (par exemple avec 7zip). 
    Vous devriez avoir un dossier nommé "UnityStation-Scene".

=== Introduction ===

	Avant de commencer, assurez-vous d'utiliser OBS version 27 ou ultérieure. 
	https://github.com/obsproject/obs-studio/releases
	Vous pouvez télécharger la dernière version sur le site Officiel. 
	(Pour Ubuntu) ajoutez le PPA-unstable de votre distribution.

=== Sauvegarde ===

	Avant toute modification, 
	il est vivement recommandé de faire une sauvegarde et une exportation de votre profil et de votre collection de scènes. 
	Pour cela, dans le menu OBS, sélectionnez "profils/collection de scènes", 
	renommez-les et exportez-les vers un dossier de sauvegarde, par exemple "/video/OBS/profils". 
	Veillez à donner des noms différents à vos profils et scènes pour éviter les confusions.

	Il est également recommandé d'avoir un dossier OBS contenant des images génériques et un dossier par scène pour vos sources. 
	Ainsi, lorsque vous sauvegardez ou exportez votre profil et votre collection de scènes, les images sont facilement sauvegardées avec.

=== Importation ===

  1  Fermez OBS.
  2  Allez sur le lien suivant : https://obsproject.com/forum/resources/source-copy.1261/
  3  Téléchargez la source et enregistrez-la dans votre dossier OBS pour la retrouver facilement. Il s'agit du fichier "source-copy-x.x.x-windows-installer.zip".
  4  Exécutez le fichier .exe (installer) puis relancez OBS.
  5  Dans le menu "Outils", sélectionnez "Sources Copy", "Load Scene" et choisissez le fichier "UnityStationWindows_1.5.json" qui se trouve dans le dossier "UnityStation-Scene" que vous avez créé précédemment.
  6  Vérifiez que la scène apparaît bien à la fin de votre liste de scènes.

=== Vérification finale ===

	Un menu peut parfois s'ouvrir pour vous informer qu'il manque des sources. 
	Cliquez sur "Chercher le dossier" et sélectionnez le dossier "UnityStation-Scene". 
	Il faudra sans doute remonter l'arborescence pour ne sélectionner que le dossier. 
	Une fois cela fait, il devrait passer de "manquant" à "trouvé".

Après l'importation, 
	Vérifiez aussi que vos Son entrée / sortie soient correctement gérés sur l'affichage du volume (généralement à droite), 
	et que les paramètres de la webcam (comme le cadrage) sont correctement réglés.
	Si l'image finale n'est pas centré, vous pouvez faire un clic droit sur l'aperçu de la webcam et faire transformer => centrer horizontalement
	si vous n'avez pas de fond vert, vous pouvez simplement forcer les valeur des filtre, l'effet fonctionnera également.
	
=== FIN ===
Merci d'avoir suivie ce tutoriel, Ecrit par Fr_Dae
Dae#5125 (discord)
