[![Version - 1.0.2](https://img.shields.io/badge/Version-1.0.2-critical)](https://)

## Blender Add-On

To install the Blender Add-On

1. Install Blender 3.5+
2. In Blender, under "Edit" click "Preferences"
3. Click "Add-Ons"
4. Click "Install" and point at the 'Tubbys Blender Exporter.py'
5. Click refresh then restart Blender

## Blender Asset Library

To install the Blender Asset Library

1. In Blender, under "Edit" click "Preferences"
2. Click "File Paths"
3. Scroll down to Asset Libraries, Add a new Asset Library by clicking the "+"
4. Unzip the Forge For Infinite Asset Pack
4. Select the Forge For Infinite Asset Pack folder
## Blender to Forge Printer Bot

To install the Halo Infinite: B2FP Bot

1. Install Python 3.4+
2. Install the necessary python packages, open your command line prompt and **copy & paste** the following line:
```
pip install pyautogui PyQt5 pydirectinput keyboard pyperclip
```
3. Launch B2FP.exe
## Running Blender to Forge Printer Bot

To run the Halo Infinite: B2FP Bot

*Halo Infinite must be in **English (NA)** and your keyboard settings must be in **English (NA)** for the printer to function.*

1. Spawn any object
2. Go to Object Properties *(CTRL + 2)*
3. Ensure every folder is expanded. *(Press TAB to expand/collapse all property categories.)*
4. Use your arrow keys to hover over the "General" category at the very top of the list.
5. Without deselecting "General", go back to Object Properties *(CTRL + 1)*
6. Make sure all object folders and subfolders are collapsed. *(Hover over "Recents")*
7. Configure your settings/collections in the B2FP window.
8. Hit Start.
9. DO NOT touch anything, move anything, or type anything while the Bot is processing. *(The Bot should stop when Infinite is not the focused window, but chaos *can* happen)*
10. If, for any reason, you need to stop the Bot **immediately**, *HOLD **F***.
..10. Otherwise, move your cursor over to "Stop" and Left-Click to stop the Bot Process when you want it to stop (May Need to press twice).
## Testing

You can test the bot to make sure it is working properly on your machine without needing to make your own Blender file or Export your current project by using the DemoPrint.DCjson file provided in the Bot Download.

## Usage/Examples

### Recommended Settings

1. Turn off Borderless Fullscreen.
2. Set the Window size to the smallest size you can.
3. Reduce your graphics settings as much as you can to increase your FPS.
4. Move the Halo: Infinite window near, but not up against, the top-left corner of your screen.
5. Launch B2FP.exe
6. Move B2FP to the top-right of your window.
7. DO NOT overlap the windows. This can result in errors.
8. Run your bot!

**Note**: There are many factors that can negatively impact your ability to print at a fast speed with no errors. Consider the following:
- Disable V-Sync
- Set a stable minimum FPS and maximum FPS of no more than eg. 100-120
- Look up at the sky when printing your map.
- Your connection to 343s Infinite servers will affect print speed

If your Bot is making misinputs, slow down your print speed. Your Network Connection AND Network Stability can impact the consistency of the bot. Use the DemoPrint.DCjson to test and fine tune a good Print Speed for your bot on your specific machine. If you see yourself experiencing Packet Loss, Jitter, Latency Variation, or any other network condition, stop your print and wait for the issues to resolve.

If your Bot is making errors, enable the Verbose Log option in the UI and try to replicate the issue. Video recordings + Verbose Logs of errors are the most useful way to address issues. Try tuning your Print Speed slider to go slower if you run the game under 100fps.

**DO NOT attempt to print a DCjson OR a Collection that contains only 1 object.**
