TubbyMcFatDucks Blender to Forge Bot
====================================

This bot takes JSON data exported from Blender and executes keystrokes in Halo Infinite.

Getting Started
---------------

These instructions will help you get a copy of the project up and running on your local machine for development and testing purposes.

For help or further questions join my discord: discord.gg/h2HwUDpAjw

Prerequisites/Installation
--------------------------

This bot requires the installation of a modified version of Derek's Blender addon and the Forge Items library. You can find the modified addon at: [https://github.com/DerrikCreates](https://github.com/DerrikCreates)

1. Remove any previous Blender exporter if installed, then close Blender.
2. Copy the "Forge for Blender" folder to the following location:
   `AppData\Roaming\Blender Foundation\Blender\3.4\scripts\addons`
3. Open Blender.
4. In Blender, go to Edit > Preferences.
5. Search for "Forge for Blender" and check the box next to it.
6. Restart Blender.

Additionally, you need to install the following Python packages: pyautogui, pydirectinput, and pyperclip. These packages allow the bot to execute keystrokes to navigate menus and input object values.

1. Open a command prompt.
2. Run the following commands one by one, waiting for each installation to complete:
    pip install pyautogui 
    pip install pydirectinput 
    pip install pyperclip
3. Wait for the installations to complete.

Usage
-----

To use the bot:

1. Build your map in Blender using the Forge assets.
2. When you're ready to export, separate assets into folders based on their object type. The bot can only place one object type per run in Halo Infinite.
3. It is recommended to keep each batch around 150 objects. The bot quick saves at the end of each batch.
4. Open Halo infinite in windowed mode.
5. Place the inital object you will be exporting - REMEMBER the bot can only place run with one object type at a time so make sure the json reflects that
6. Open all menues in object property - insure the placed object was the last item highlighted in the object browser
7. Press 0 to reset the objects rotation
8. Highlight object name inside the property windowed
9. RUN BOT
10.!!!!!!!!!!!Do not click else where while bot is running - Only click stop and quit on the bot menue else the bot will start spamming keystrokes EVERYWHERE.!!!!!!!!!!!!!


Contributing
------------

Special thanks to Okom1 for testing each iteration of the bot since I can't run Halo on my PC.
Thanks to DerrikCreates for building the initial versions of the exporter and sparking my interest in picking up this project again.

Authors
-------

- TubbyMcFatDuck (Bot creator) - [Discord](https://discord.gg/h2HwUDpAjw)

License
-------

This project is licensed under the MIT License. See the LICENSE.txt file for details.

Acknowledgments
---------------

For more Halo fun, visit [HaloFunTime.com](https://halofuntime.com)
