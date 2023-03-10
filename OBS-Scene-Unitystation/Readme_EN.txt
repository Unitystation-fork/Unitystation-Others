== Importing the Unitystation Community Scene

	This tutorial aims at guiding you step by step in importing a pre-made scene to OBS Studio. 
	By following these instructions, you will be able to easily add a "face-cam confessional" reality show scene to your scene collection. 
	The scene will be common to all streamers participating in the UnityStation community project.
	(you can find a preview in the file "Result.png")
	
=== UnityStation scene ===

    Download the zip file containing the scene.
    Place the zip in the folder %USERPROFILE%\image\OBS\. If the folder doesn't exist, create it in a case-sensitive way.
    Unzip the zip with a right click "extract here" (for example with 7zip). 
    You should have a folder named "UnityStation-Scene".

=== Introduction ===

	Before you start, make sure you are using OBS version 27 or later. 
	https://github.com/obsproject/obs-studio/releases
	You can download the latest version from the official website. 
	(For Ubuntu) add the PPA-unstable of your distribution.

=== Backup ==

	Before any modification, 
	it is highly recommended to make a backup and export of your profile and your scene collection. 
	To do this, in the OBS menu, select "profiles/scene collection", 
	rename them and export them to a backup folder, for example "/video/OBS/profiles". 
	Be sure to give different names to your profiles and scenes to avoid confusion.

	It is also recommended to have an OBS folder containing generic images and a scene folder for your sources. 
	This way, when you save or export your profile and scene collection, the images are easily saved with it.

=== Import ===

  1 Close OBS.
  2 Go to the following link: https://obsproject.com/forum/resources/source-copy.1261/
  3 Download the source and save it in your OBS folder to find it easily. It is the file "source-copy-x.x.x-windows-installer.zip".
  4 Run the .exe file (installer) and restart OBS.
  5 In the "Tools" menu, select "Sources Copy", "Load Scene" and choose the file "UnityStationWindows_1.5.json" which is located in the "UnityStation-Scene" folder you created earlier.
  6 Check that the scene appears at the end of your scene list.

=== Final check ===

	Sometimes a menu may open to inform you that sources are missing. 
	Click on "Find Folder" and select the "UnityStation-Scene" folder. 
	You may have to go up the tree to select only the folder. 
	Once this is done, it should change from "missing" to "found".

After the import, 
	Also check that your Sound In/Out is correctly managed on the volume display (usually on the right), 
	and that the webcam settings (such as framing) are correctly set.
	If the final image is not centred, you can right click on the webcam preview and do transform => centre horizontally
	if you don't have a green background, you can simply force the filter values, the effect will also work.
	
=== END ===
Thanks for following this tutorial, Written by Fr_Dae
Dae#5125 (discord)
