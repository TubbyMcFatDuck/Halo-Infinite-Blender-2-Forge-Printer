import subprocess
import os
import sys
import json
import urllib.request
import pyautogui
import time
import webbrowser
import re
import Keymanager
import math
from PyQt5.QtWidgets import QMessageBox, QColorDialog, QApplication,QMainWindow, QSlider, QLabel,QCheckBox, QToolTip, QPushButton, QFileDialog, QTextEdit, QTextBrowser, QSpinBox, QLineEdit, QMenu, QAction, QScrollArea, QProgressBar
from PyQt5.QtCore import Qt, QThread, pyqtSignal, pyqtSlot, QTimer, QCoreApplication
from PyQt5.uic import loadUi
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QTextCursor, QColor
import random
import configparser

#This is the Repo Information and this codes current version, This is used for version checking and not inclusive of all code contributors.
repo_owner = "TubbyMcFatDuck"
repo_name = "Halo-Infinite-Blender-2-Forge"
current_version = "1.0.0"

#This is used for dev mode functionality - TURNS OFF WINDOW MONITOR STOP ACTION
devMode = False
# DO NOT LEAVE THIS TRUE WHEN DEPLOYING - It will make Okom upset
# DO NOT LEAVE THIS TRUE WHEN DEPLOYING - It will make people cry
# DO NOT LEAVE THIS TRUE WHEN DEPLOYING - It will make keyboards explode
# DO NOT LEAVE THIS TRUE WHEN DEPLOYING - It will make TubbyMcFatDuck annoyed

objCounter = 0
objectList = []
collection_counts = []
collectionChecks = []
hours, minutes, seconds = 0,0,0
colOffset = False
colCounter = 0
objectListSizes = []
totalCount = 0
runtimeCount = 0
UGCData = []
UGCDataIndex = 0
UGCLink = ""

# Used for Ini File
config = configparser.RawConfigParser()
# Set the current working directory
main_dir = os.path.abspath(os.path.dirname(__file__))
# Set the path to the Bot
bot_path = os.path.join("Main", "Bot.py")


class stopWatchThread (QThread):
    stopwatch_signal = pyqtSignal(str, str, str)
    def __init__(self, main_ui):
        super(stopWatchThread, self).__init__()
        self.main_ui = main_ui
    
    def run(self):
        while self.main_ui.stopWatchRunning == True:
            time.sleep(1)
            self.main_ui.stopWatchUpdate()
    
class BotOutputThread(QThread):
    log_signal = pyqtSignal(str)

    def __init__(self, main_ui):
        super(BotOutputThread, self).__init__()
        self.main_ui = main_ui
    def run(self):
        # Move the code from read_bot_output() into this run() method
        with self.main_ui.bot_process.stdout:
            for line in iter(self.main_ui.bot_process.stdout.readline, b''):
                self.main_ui.log_to_gui(line.decode())
                sys.stdout.flush()  # Flush the standard output

class WindowMonitorThread(QThread):
    log_signal = pyqtSignal(str)
    global devMode
    def __init__(self, main_ui):
        super(WindowMonitorThread, self).__init__()
        self.main_ui = main_ui

    def run(self):
        # Move the code from monitor_active_window() into this run() method
        while not self.main_ui.stop_window_monitor:
            try:
                active_window_title = pyautogui.getActiveWindowTitle()
                if active_window_title != "Halo Infinite" and devMode == False:
                    self.main_ui.log_to_gui("\nWARNING: Halo Infinite is not the active window. STOPPING BOT!\n")
                    self.main_ui.stop_btn_action()
                    break
            except pyautogui.FailSafeException:
                pass

            time.sleep(1)


class mainUI (QMainWindow):
    stopwatch_signal = pyqtSignal(str, str, str)
    log_signal = pyqtSignal(str)
    feedback_signal = pyqtSignal(int)
    windowMonitor_signal = pyqtSignal()
    def __init__(self):
        super(mainUI, self).__init__()
        loadUi("Main/Gui.ui",self)
        self.setWindowTitle("HIFB {}".format(current_version))
    
        # Run check_latest_version on the first run
        self.first_run = True
        QTimer.singleShot(0, self.run_check_latest_version)

        self.timer = QTimer()
        self.timer.timeout.connect(self.displayUGC)
        self.timer.start(15 * 1000)  # 60 seconds * 1000 ms = 1 minute

        #Variables
        self.low_performance_var = 0.014
        self.bot_process = None
        self.stop_flag = False
        self.stop_window_monitor = False
        self.stopWatchRunning = False
        self.position_only_var = False
        self.upper_limit_check_var = False
        self.save_interval_var = True
        self.upper_limit = 0
        self.start_index_var = 0
        self.stop_me_var = 0
        self.x_bump = 0
        self.y_bump = 0
        self.z_bump = 0
        self.save_interval = 50
        self.verbose_log_var = False
        self.collectionTF = False

        self.file_path = None

        #Define our Widgets
            #Menu
        self.menuThemes = self.findChild(QMenu, "menuThemes")
        self.menuThemesClassic = self.findChild(QAction, "Classic")
        self.menuThemesDark = self.findChild(QAction, "Dark")
        self.menuThemesLeather = self.findChild(QAction, "Leather")
        self.menuThemesRose = self.findChild(QAction, "Rose")
        self.menuThemesWarm = self.findChild(QAction, "Warm")
        self.menuThemesSwamp = self.findChild(QAction, "Swamp")
        self.menuThemesCyber = self.findChild(QAction, "Cyber")
        self.menuThemesCustom = self.findChild(QAction, "Custom_2")
        self.menuHelpFaq = self.findChild(QAction, "FAQ")
        self.menuThemesCustomCreator = self.findChild(QAction, "actionTheme_Editor_2")
        self.menuThemesCustomCreatorButtons = self.findChild(QAction, "actionTheme_Editor_3")
        self.menuThemesCustomCreatorText = self.findChild(QAction, "actionTheme_Editor_4")


            #Slider
        self.printSpeedSlider = self.findChild(QSlider, "printSpeedSlider")
        self.printSpeedTimerLabel = self.findChild(QLabel, "printSpeedTimerLabel")
            #jsonSelector
        self.jsonSelectorButton = self.findChild(QPushButton, "jsonSelectorButton")
        self.jsonSelectedFileLabel = self.findChild(QLabel, "jsonSelectedFileLabel")
        self.objectCountLabel = self.findChild(QLabel, "objectCountLabel")
        self.printEstimatedSpeedLabel = self.findChild(QLabel, "printEstimatedSpeedLabel")
            #start/stop
        self.startButton = self.findChild(QPushButton, "startButton")
        self.stopButton = self.findChild(QPushButton, "stopButton")
            #Log
        self.logBoxTextBrowser = self.findChild(QTextEdit, "logBoxTextBrowser")
        self.logClearButton = self.findChild(QPushButton, "logClearButton")
        self.logExportButton = self.findChild(QPushButton, "logExportButton")
            #save interval
        self.saveCounterSpin = self.findChild(QSpinBox, "saveCounterSpin")
            #start Index/Stop Index
        self.startIndexText = self.findChild(QLineEdit, "startIndexText")
        self.stopIndexText = self.findChild(QLineEdit, "stopIndexText")
           #checkboxes
        self.endIndexCheckBox = self.findChild(QCheckBox, "endIndexCheckBox")
        self.positionOnlyCheckBox = self.findChild(QCheckBox, "positionOnlyCheckBox")
        self.saveIntervalCheckBox = self.findChild(QCheckBox, "saveIntervalCheckBox")
        self.verboseLogCheckBox = self.findChild(QCheckBox, "verboseLogCheckBox")
            #Offsets
        self.xoffsetText = self.findChild(QLineEdit, "xoffsetText")
        self.yoffsetText = self.findChild(QLineEdit, "yoffsetText")
        self.zoffsetText = self.findChild(QLineEdit, "zoffsetText")
            #Discord
        self.discordButton = self.findChild(QPushButton, "discordButton")
            #Collections
        self.printCollectionButton = self.findChild(QCheckBox, "printCollectionButton")
        self.collectionsScrollArea = self.findChildren(QScrollArea, "collectionsScrollArea")
            #Elapsed Time
        self.elapsedTimeLabel = self.findChild(QLabel, "elapsedTimeLabel")
            #Progress Bar
        self.collectionProgressLabel = self.findChild(QLabel, "collectionProgressLabel")
        self.objectsProgressLabel = self.findChild(QLabel, "objectsProgressLabel")
        self.totalProgressBar = self.findChild(QProgressBar, "totalProgressBar")
            #UGC Label
        self.UGCLabel = self.findChild(QLabel, "ugcLabel")
        self.UGCButton = self.findChild(QPushButton, "ugcButton")

        #Connect our Widgets to functions
            #UGC Button
        self.UGCButton.clicked.connect(self.UGCLabel_mousePressEvent)
            #signals - Need to find a better spot for these
        self.feedback_signal.connect(self.feedback)
        self.stopwatch_signal.connect(self.stopWatchUpdate)
        self.windowMonitor_signal.connect(self.stop_btn_action_2)

            #Menus
        self.menuThemesClassic.triggered.connect(lambda: self.change_theme(theme = "ClassicTheme"))
        self.menuThemesDark.triggered.connect(lambda: self.change_theme(theme = "DarkTheme"))
        self.menuThemesLeather.triggered.connect(lambda: self.change_theme(theme = "LeatherTheme"))
        self.menuThemesRose.triggered.connect(lambda: self.change_theme(theme = "RoseTheme"))
        self.menuThemesWarm.triggered.connect(lambda: self.change_theme(theme = "WarmTheme"))
        self.menuThemesSwamp.triggered.connect(lambda: self.change_theme(theme = "SwampTheme"))
        self.menuThemesCyber.triggered.connect(lambda: self.change_theme(theme = "CyberTheme"))
        self.menuThemesCustom.triggered.connect(lambda: self.change_theme(theme = "CustomTheme"))
        self.menuThemesCustomCreator.triggered.connect(self.themeCreator)
        self.menuThemesCustomCreatorButtons.triggered.connect(self.themeCreatorButtons)
        self.menuThemesCustomCreatorText.triggered.connect(self.themeCreatorText)
        self.menuHelpFaq.triggered.connect(lambda: webbrowser.open('https://discord.com/channels/1132093550553747518/1140483269570347078'))
            #slider
        self.printSpeedSlider.valueChanged.connect(self.printSpeedSlider_Slider_action)
        self.jsonSelectorButton.clicked.connect(self.browse_json_file)
            #start/stop
        self.startButton.clicked.connect(self.start_btn_action)
        self.stopButton.clicked.connect(self.stop_btn_action)
            #log
        self.logClearButton.clicked.connect(self.clear_log)
        self.logExportButton.clicked.connect(self.export_log)
        self.log_signal.connect(self.log_to_gui)
            #save interval
        self.saveCounterSpin.valueChanged.connect(self.saveCounterSpin_SpinBox_action)
            #start Index/Stop Index
        self.startIndexText.textChanged.connect(self.startIndexText_action)
        self.stopIndexText.textChanged.connect(self.stopIndexText_action)
            #checkboxes
        self.endIndexCheckBox.stateChanged.connect(self.endIndexCheckBox_action)
        self.positionOnlyCheckBox.stateChanged.connect(self.positionOnlyCheckBox_action)
        self.saveIntervalCheckBox.stateChanged.connect(self.saveIntervalCheckBox_action)
        self.verboseLogCheckBox.stateChanged.connect(self.verboseLogCheckBox_action)
        self.printCollectionButton.stateChanged.connect(self.updateColTFCounter)
            #Offsets
        self.xoffsetText.textChanged.connect(self.xoffsetText_action)
        self.yoffsetText.textChanged.connect(self.yoffsetText_action)
        self.zoffsetText.textChanged.connect(self.zoffsetText_action)
            #Discord
        self.discordButton.clicked.connect(self.discord_btn_action)
    

#Functions
    def displayUGC(self):
        global UGCData
        global UGCDataIndex
        global UGCLink

        # Check if 'ugcList' key exists in UGCData dictionary
        if 'ugcList' in UGCData:
            ugcList = UGCData['ugcList']
            if not ugcList or UGCDataIndex >= len(ugcList):
                UGCDataIndex = 0  # Go back to the first index

            item = ugcList[UGCDataIndex]
            image_url = item['imageurl']
            self.link_url = item['linkurl']
            UGCLink = self.link_url

            print(image_url, self.link_url)
            print(UGCDataIndex)
            print(len(ugcList))
            try:
                response = urllib.request.urlopen(image_url)
                image_data = response.read()
                pixmap = QtGui.QPixmap()
                pixmap.loadFromData(image_data)
                self.UGCLabel.setPixmap(pixmap)
                self.UGCLabel.setScaledContents(True)

            except urllib.error.HTTPError as e:
                print(f"Failed to download image. Error code: {e.code}")
            except urllib.error.URLError as e:
                print(f"Failed to download image. Reason: {e.reason}")

            UGCDataIndex += 1
            print (UGCDataIndex)
        else:
            print("ugcList key does not exist in UGCData dictionary")
                
    def UGCLabel_mousePressEvent(self):
            webbrowser.open(UGCLink)

    def run_check_latest_version(self):
        # Check the latest version
        self.check_latest_version(repo_owner, repo_name, current_version)

    def check_latest_version(self, repo_owner, repo_name, current_version):
        global UGCData
        # Get the latest release information
        if self.first_run:
            url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
            with urllib.request.urlopen(url) as response:
                if response.getcode() == 200:
                    release_info = json.loads(response.read())
                    latest_version = release_info['tag_name']
                    
                    # Compare the current version with the latest version
                    if current_version == latest_version:
                        print("You are using the latest version.")
                    else:
                        # Show a custom dialog with a button to open the repository URL
                        msg_box = QMessageBox()
                        msg_box.setWindowTitle("HIFB Version Checker")
                        msg_box.setText(f"A new version ({latest_version}) is available. Please update your application.")
                        msg_box.setWindowIcon(self.windowIcon())  # Set the same icon as the main app
                        open_repo_button = msg_box.addButton("Open Repository", QMessageBox.ActionRole)
                        ignore_button = msg_box.addButton("Ignore", QMessageBox.ActionRole)
                        msg_box.exec_()

                        # Check which button was clicked
                        clicked_button = msg_box.clickedButton()
                        if msg_box.clickedButton() == open_repo_button:
                            # Open the repository URL in a web browser
                            import webbrowser
                            repo_url = f"https://github.com/{repo_owner}/{repo_name}"
                            webbrowser.open(repo_url)

                            # Close the application
                            QCoreApplication.quit()
                        elif clicked_button == ignore_button:
                            print("You have chosen to ignore the update.")
                else:
                    print("Failed to fetch the latest release information.")
                
            url2 = f'https://raw.githubusercontent.com/{repo_owner}/{repo_name}/main/UGC.DCjson'
            try:
                headers = {'Content-Type': 'application/json'}
                request = urllib.request.Request(url2, headers=headers)
                with urllib.request.urlopen(request) as response:
                    UGCData = json.loads(response.read())
                    random.shuffle(UGCData['ugcList'])
                    print(UGCData)

                    # Use the data as needed
            except urllib.error.URLError as e:
                print('Failed to retrieve JSON data from the GitHub repository:', e)

            # Set first_run to False to prevent subsequent runs
            self.first_run = False
            self.displayUGC()

    @pyqtSlot(str, str, str)
    def stopWatchUpdate(self):
            if self.stopWatchRunning == True:
                global hours, minutes, seconds
                seconds += 1
                if seconds == 60:
                    minutes += 1
                    seconds = 0
                if minutes == 60:
                    hours += 1
                    minutes = 0

                hourString = f"{hours}" if hours > 9 else f"0{hours}"
                minuteString = f"{minutes}" if minutes > 9 else f"0{minutes}"
                secondString =f"{seconds}" if seconds > 9 else f"0{seconds}"

                self.elapsedTimeLabel.setText(f"Elapsed Time: " + hourString + ":" + minuteString + ":" + secondString)
        #Theme Functions
    def change_theme(self, theme):
        # Create a ConfigParser object
        global config

        # Read the INI file
        config.read(os.path.join("Main", "Settings.ini"))

        # Initialize styles with an empty string
        styles = ""

        try:
            # Get the styles for the selected theme
            styles = config.get(theme, 'stylesheet').strip('|"""')
            print('1Theme is:',styles)
        except (configparser.NoSectionError, configparser.NoOptionError):
            # Handle the case when the specified theme or stylesheet is not found
            print("Invalid theme or stylesheet1")
            pass

        # If the styles are a reference to another section
        if theme == "DefaultTheme":
            try:
                # Get the referenced theme for the default theme
                referenced_theme = config.get(theme, 'DefaultTheme').strip('|"""')
                print('2Theme is:',styles)
            except (configparser.NoOptionError, configparser.NoSectionError):
                # Handle the case when the referenced theme is not found
                print("Invalid referenced theme2")
                pass
            else:
                # Get the styles for the referenced theme
                try:
                    styles = config.get(referenced_theme, 'stylesheet').strip('|"""')
                    print('3Theme is:',styles)
                except (configparser.NoSectionError, configparser.NoOptionError):
                    # Handle the case when the styles for the referenced theme are not found
                    print("Invalid referenced theme styles3")
                    return
                
        # Update the default theme in the INI file
        if theme != "DefaultTheme":
            config.set("DefaultTheme", "defaultTheme", theme)
            print('Default Them is now:',styles)

        # Save the changes to the INI file
        with open(os.path.join("Main", "Settings.ini"), "w") as config_file:
            config.write(config_file)


        # Apply the styles to the GUI
        self.setStyleSheet(styles)

    def themeCreator(self):
        global config

        # Create a QColorDialog to choose a color
        color_dialog = QColorDialog()

        # Set the current color to the current color value of "CustomTheme"
        custom_theme_color = config.get("CustomTheme", "stylesheet").strip('|"""').splitlines()[3].split(":")[1].strip()
        current_color = QColor(custom_theme_color)
        color_dialog.setCurrentColor(current_color)

        # Open the QColorDialog for the user to select a color
        if color_dialog.exec_() == QColorDialog.Accepted:
            # Get the selected color
            selected_color = color_dialog.selectedColor()

            # Convert the selected color to a string in hexadecimal format
            selected_color_hex = selected_color.name()

            # Update the color value of "CustomTheme" in the INI file
            custom_theme_stylesheet = config.get("CustomTheme", "stylesheet").strip('|"""')
            custom_theme_stylesheet = custom_theme_stylesheet.replace(custom_theme_color, selected_color_hex + ";")

            # Calculate a shade lighter of the selected color
            selected_color_rgb = selected_color.red(), selected_color.green(), selected_color.blue()
            lighter_color_rgb = tuple(min(255, int(c * 1.2)) for c in selected_color_rgb)
            lighter_color_hex = '#{:02x}{:02x}{:02x}'.format(*lighter_color_rgb)

            menu_item_ids = ["menuBar QMenu::item:selected", "menuBar QMenu::item:hover", "menuBar QAction:selected", "menuBar QAction:hover"]
            for menu_item_id in menu_item_ids:
                menu_item_selector = f"QWidget#{menu_item_id} {{"
                start_index = custom_theme_stylesheet.find(menu_item_selector)
                end_index = custom_theme_stylesheet.find("}", start_index)
                menu_item_styles = custom_theme_stylesheet[start_index:end_index + 1]
                current_background_color_match = re.search(r"background-color:\s*(#(?:[0-9a-fA-F]{3}){1,2})", menu_item_styles)
                if current_background_color_match:
                    current_background_color = current_background_color_match.group(1)

                    # Replace the current background-color value with the shade lighter color
                    menu_item_styles = menu_item_styles.replace(current_background_color, lighter_color_hex)
                    custom_theme_stylesheet = custom_theme_stylesheet[:start_index] + menu_item_styles + custom_theme_stylesheet[end_index + 1:]
                
            custom_theme_stylesheet = '|"""' + custom_theme_stylesheet + '"""|'
            config.set("CustomTheme", "stylesheet", custom_theme_stylesheet)

            # Save the changes to the INI file
            with open(os.path.join("Main", "Settings.ini"), "w") as config_file:
                config.write(config_file)

            # Load the updated theme
            self.change_theme(theme="CustomTheme")
    

    def themeCreatorButtons(self):
        global config
        # Create a QColorDialog to choose a color
        color_dialog = QColorDialog()

        # Set the current color to the current color value of "CustomTheme"
        custom_theme_color = config.get("CustomTheme", "stylesheet").strip('|"""').splitlines()[3].split(":")[1].strip()
        current_color = QColor(custom_theme_color)
        color_dialog.setCurrentColor(current_color)

        # Open the QColorDialog for the user to select a color
        if color_dialog.exec_() == QColorDialog.Accepted:
            # Get the selected color
            selected_color = color_dialog.selectedColor()

            # Convert the selected color to a string in hexadecimal format
            selected_color_hex = selected_color.name()

            # Get the current background-color values of the buttons
            stylesheet = config.get("CustomTheme", "stylesheet").strip('|"""')

            # Find the current background-color values of the buttons
            button_ids = ["jsonSelectorButton", "logClearButton", "logExportButton", "discordButton", "ugcButton"]
            for button_id in button_ids:
                button_selector = f"QPushButton#{button_id} {{"
                start_index = stylesheet.find(button_selector)
                end_index = stylesheet.find("}", start_index)
                button_styles = stylesheet[start_index:end_index + 1]
                current_background_color = re.search(r"background-color:\s*(#(?:[0-9a-fA-F]{3}){1,2})", button_styles).group(1)

                # Replace the current background-color value with the selected color
                button_styles = button_styles.replace(current_background_color, selected_color_hex)
                stylesheet = stylesheet[:start_index] + button_styles + stylesheet[end_index + 1:]

            # Update the stylesheet value in the INI file
            config.set("CustomTheme", "stylesheet", '|"""' + stylesheet + '|"""')

            # Save the changes to the INI file
            with open(os.path.join("Main", "Settings.ini"), "w") as config_file:
                config.write(config_file)

            # Load the updated theme
            self.change_theme(theme="CustomTheme")

    def themeCreatorText(self):
        global config
        # Create a QColorDialog to choose a color
        color_dialog = QColorDialog()

        # Set the current color to the current color value of "CustomTheme"
        custom_theme_stylesheet = config.get("CustomTheme", "stylesheet").strip('|"""')

        # Open the QColorDialog for the user to select a color
        if color_dialog.exec_() == QColorDialog.Accepted:
            # Get the selected color
            selected_color = color_dialog.selectedColor()

            # Update the color value in the stylesheet
            custom_theme_stylesheet = re.sub(r"(?<!background-)color:\s*#[0-9a-fA-F]{6};", rf"color: {selected_color.name()};", custom_theme_stylesheet)

            # Update the stylesheet value in the INI file
            custom_theme_stylesheet = '|"""' + custom_theme_stylesheet + '"""|'
            config.set("CustomTheme", "stylesheet", custom_theme_stylesheet)

            # Save the changes to the INI file
            with open(os.path.join("Main", "Settings.ini"), "w") as config_file:
                config.write(config_file)

            # Load the updated theme
            self.change_theme(theme="CustomTheme")

    #Discord Functions
    def discord_btn_action(self):
        webbrowser.open('https://discord.gg/qzJenCtWgr')
    #Offset Functions
    def xoffsetText_action(self, value):
        self.x_bump = value
        print(self.x_bump)
    
    def yoffsetText_action(self, value):
        self.y_bump = value
        print(self.y_bump)
    
    def zoffsetText_action(self, value):
        self.z_bump = value
        print(self.z_bump)

    #Checkbox Functions
    def endIndexCheckBox_action(self, value):
        if value == 2:
            self.upper_limit_check_var = True
        else:
            self.upper_limit_check_var = False
        print(self.upper_limit_check_var)

    def positionOnlyCheckBox_action(self, value):
        if value == 2:
            self.position_only_var = True
        else:
            self.position_only_var = False
        print(self.position_only_var)
    
    def saveIntervalCheckBox_action(self, value):
        if value == 2:
            self.save_interval_var = True
        else:
            self.save_interval_var = False
        print(self.save_interval_var)

    def verboseLogCheckBox_action(self, value):
        if value == 2:
            self.verbose_log_var = True
        else:
            self.verbose_log_var = False
        print(self.verbose_log_var)

    #start Index/Stop Index function
    def startIndexText_action(self, value):
        self.start_index_var = value
        print(self.start_index_var)
    
    def stopIndexText_action(self, value):
        self.stop_me_var = value
        print(self.stop_me_var)

    #Save Interval function
    def saveCounterSpin_SpinBox_action(self, value):
        self.save_interval = value
        print(self.save_interval)

    #Print Speed Slider function
    def printSpeedSlider_Slider_action(self, value):
        self.low_performance_var = value / 1000
        self.printSpeedTimerLabel.setText(str(f"Print Speed = {self.low_performance_var}"))
        try:
            self.calculate_estimated_print_time(file_path=self.file_path)
        except:
            pass
        print(self.low_performance_var)

    #Start/Stop Button Function
    def start_btn_action(self):
        global collectionChecks
        global objCounter
        global colCounter
        global colOffset
        objCounter = 0
        colCounter = 0
        colOffset = False
        self.startButton.hide()
        self.stopButton.show()

        self.collectionProgressLabel.setText("Printing Collection:")
        path = self.file_path
        Keymanager.focus_Halo()
        stop_flag = bool(self.stop_flag)
        position_only = self.position_only_var
        low_performance = self.low_performance_var
        start_index = self.start_index_var
        stop_me = self.stop_me_var
        x_bump = self.x_bump
        y_bump = self.y_bump
        z_bump = self.z_bump
        upper_limit = self.upper_limit
        upper_limit_check = self.upper_limit_check_var
        save_interval = self.save_interval
        save_interval_check = self.save_interval_var
        collection_master = self.collectionTF
        verbose_log = self.verbose_log_var
        collectionFinal = list(map(str,self.checkbox_states.values()))
        print (collectionFinal)
        print(f"The value of low_performance is: {low_performance}")
        self.bot_process = subprocess.Popen(["python", bot_path, path, str(stop_flag), str(position_only), str(float(low_performance)), str(int(start_index)), str(int(stop_me)), str(int(x_bump)), str(int(y_bump)), str(int(z_bump)), str(int(upper_limit)), str(upper_limit_check), str(int(save_interval)), str(save_interval_check), str(verbose_log), str(collection_master)] + collectionFinal, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, bufsize=1)
        
        self.bot_output_thread = BotOutputThread(self)
        self.bot_output_thread.bot_process = self.bot_process
        self.bot_output_thread.finished.connect(self.bot_output_thread.deleteLater)
        self.bot_output_thread.log_signal.connect(self.log_signal.emit)
        self.bot_output_thread.start()

        self.window_monitor_thread = WindowMonitorThread(self)
        self.window_monitor_thread.stop_window_monitor = False
        self.window_monitor_thread.finished.connect(self.window_monitor_thread.deleteLater)
        self.window_monitor_thread.log_signal.connect(self.log_signal.emit)
        self.window_monitor_thread.start()

        global hours, minutes, seconds
        hours, minutes, seconds = 0,0,0
        self.stopwatch_thread = stopWatchThread(self)
        self.stopWatchRunning = True
        self.stopwatch_thread.finished.connect(self.stopwatch_thread.deleteLater)
        self.stopwatch_thread.stopwatch_signal.connect(self.stopwatch_signal.emit)
        self.stopwatch_thread.start()


    @pyqtSlot(str)
    def log_to_gui(self, message):
        global objCounter
        global colCounter
        global colOffset

        self.logBoxTextBrowser.moveCursor(QTextCursor.End)
        self.logBoxTextBrowser.insertPlainText(message)
        curString = re.sub(r'[0-9]', "",str(message))
        curString = curString.replace(" ", "").replace("/", "").replace(":", "").lower()
        curString = curString[:-2]
        #print(len(curString))
        #print(curString)
        if curString == 'objectsprocessed':
            objCounter += 1
            self.feedback_signal.emit(objCounter)
        if curString == 'thisprinthasconcluded.':
            self.stop_btn_action()
        if curString[0:14] == 'printcompleted':
            self.stop_btn_action()
        if curString[0:23] == 'emergencystopkeypressed':
            self.stop_btn_action()
        if curString[0:18] == 'skippingcollection':
            if colOffset == False:
                colOffset = True
            else:
                colCounter += 1
        if curString[0:18] == 'printingcollection':
            if colOffset == False:
                colOffset = True
            else:
                colCounter += 1
        self.logBoxTextBrowser.moveCursor(QTextCursor.End)

    def stop_btn_action(self):
        self.stop_flag = True
        self.stop_window_monitor = True
        self.stopWatchRunning = False
        self.windowMonitor_signal.emit()
        if self.bot_process is not None:
            self.bot_process.terminate()
            self.bot_process = None
            self.log_to_gui("Bot process terminated.")

        if hasattr(self, "BotOutputThread"):
            print("BotOutputThread exists")
            if BotOutputThread.isRunning():
                print("BotOutputThread is running now stopping it")
                BotOutputThread.quit()  # Stop the thread event loop
                BotOutputThread.wait()

        if hasattr(self, "WindowMonitorThread"):
            print("WindowMonitorThread exists")
            if WindowMonitorThread.isRunning():
                print("WindowMonitorThread is running now stopping it")
                WindowMonitorThread.quit()  # Stop the thread event loop
                WindowMonitorThread.wait()

        if hasattr(self, "stopWatchThread"):
            print("stopWatchThread exists")
            if stopWatchThread.isRunning():
                print("stopWatchThread is running now stopping it")
                stopWatchThread.quit()  # Stop the thread event loop
                stopWatchThread.wait()
        
        self.stop_flag = False
        self.stop_window_monitor = False
        self.stopWatchRunning = False

    @pyqtSlot()
    def stop_btn_action_2(self):
        self.startButton.show()
        self.stopButton.hide()

    @pyqtSlot(int)
    def feedback(self):
        global objCounter
        global runtimeCount
        global totalCount
        global colCounter

        if colCounter < len(collection_counts):
            collections = list(collection_counts.keys())
            collection = collections[colCounter]
        else:
            print("No collection found for the given index")

        newobjCounter = objCounter + int(self.start_index_var)

        previousObjCounter = None  # Store the previous value of objCounter

        # Check if the value of objCounter has changed
        if objCounter != previousObjCounter:
            previousObjCounter = objCounter
            if self.collectionTF:
                self.objectsProgressLabel.setText("Objects Processed: {} / {}".format(newobjCounter, runtimeCount))
                self.totalProgressBar.setValue(newobjCounter)
            else:
                self.objectsProgressLabel.setText("Objects Processed: {} / {}".format(newobjCounter, totalCount))
                self.totalProgressBar.setValue(newobjCounter)
            
        # Update the collectionProgressLabel
        self.collectionProgressLabel.setText("Printing Collection: {}".format(collection))
 
    #Log Functions   
    def clear_log(self):
        msg_box = QMessageBox()
        msg_box.setWindowTitle("HIFB Clear Log")
        msg_box.setText(f"Are you sure you want to clear the log?")
        msg_box.setWindowIcon(self.windowIcon())  # Set the same icon as the main app
        confirm_clear_button = msg_box.addButton("Clear Log", QMessageBox.ActionRole)
        ignore_button = msg_box.addButton("Never Mind", QMessageBox.ActionRole)
        msg_box.exec_()

        # Check which button was clicked
        clicked_button = msg_box.clickedButton()
        if msg_box.clickedButton() == confirm_clear_button:
            self.logBoxTextBrowser.clear()
        elif clicked_button == ignore_button:
            print("You have chosen to not clear the log")




    def export_log(self):
        import datetime
        exptime = datetime.datetime.now()
        exptime = 'HIFB ' + exptime.strftime('%m-%d-%y %H_%M %Z') + ' LOG'
        file_path, _  = QFileDialog.getSaveFileName(self, 'Save file', exptime, "txt files (*.txt)")   
        if file_path:
            with open(file_path, "w") as f:
                f.write(self.logBoxTextBrowser.toPlainText())

    #Browse JSON file function
    def browse_json_file(self):
        self.checkbox_states = {}
        self.object_name_count = 0
        global collection_counts
        global objectList
        global collectionChecks
        global objectListSizes
        global totalCount

        objectListSizes = []
        previous_file_path = self.file_path
        file_path, _ = QFileDialog.getOpenFileName(self, 'Open file', "", "DCjson files (*.DCjson);;json files (*.json);;All files (*)")
        if file_path:
            self.file_path = file_path
        else:
            if previous_file_path:
                self.file_path = previous_file_path

        # Display object count
        if file_path:
            try:
                self.jsonSelectedFileLabel.setText(file_path)
                self.calculate_estimated_print_time(file_path)
                with open(file_path) as f:
                    json_data = json.load(f)
                    object_list = json_data.get('itemList', [])
                    object_name_count = sum(1 for object_name in object_list if object_name.get('itemId'))
                    self.upper_limit = object_name_count
                    self.objectCountLabel.setText(f"Objects found in DCjson file: {object_name_count}")
                    self.stopIndexText.setText(str(object_name_count))
                    self.stopIndexText_action(value=object_name_count)
                    totalCount = object_name_count
                    self.objectsProgressLabel.setText(f"Objects Processed: 0 / {object_name_count}")
                    self.totalProgressBar.setMaximum(object_name_count)
                size = len(json_data['itemList'])

                # Clear existing layout items
                layout = self.scrollAreaWidgetContents.layout()
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

                objectListSizes = []
                objectList = []
                collection_counts = []
                del objectList[0:len(objectList)]

                layout = self.scrollAreaWidgetContents.layout()
                while layout.count():
                    item = layout.takeAt(0)
                    widget = item.widget()
                    if widget is not None:
                        widget.deleteLater()

                collection_counts = {}
                objectList = set()

                for item in object_list:
                    collection = item.get('collection', '')
                    if collection:
                        collection_counts[collection] = collection_counts.get(collection, 0) + 1
                        objectList.add(collection)

                checkboxes = []
                layout = self.scrollAreaWidgetContents.layout()
                for collection, count in collection_counts.items():
                    checkbox = QCheckBox(f"{collection} ({count})")
                    checkboxes.append(checkbox)
                    layout.addWidget(checkbox)
                    checkbox.stateChanged.connect(self.checkbox_state_changed)
                    self.checkbox_states[checkbox] = False

                # Print the collection names and their respective counts
                print(collection_counts)
            except KeyError:
                self.log_to_gui("ERROR: The selected DCjson does not have a 'Collection' key:value pair. Please export again with updated Blender Exporter.\nYou may still print, but all collection-related features will be disabled.")
            except FileNotFoundError as e:
                # Handle the file not found error
                print("File not found:", file_path)
                print("Error:", str(e))

    def checkbox_state_changed(self, state):
        checkbox = self.sender()  # Get the checkbox that emitted the signal
        collection = checkbox.text()  # Get the collection name from the checkbox
        checked = checkbox.isChecked()  # Get the checkmark state

        # Update the boolean value in the dictionary
        self.checkbox_states[checkbox] = checked
        

        # Do something with the checkmark state
        if checked:
            print(f"{collection} checkbox is checked")
            self.checkbox_states[checkbox] = True
            self.updateValues()
            print (self.checkbox_states[checkbox])
        else:
            print(f"{collection} checkbox is unchecked")
            self.checkbox_states[checkbox] = False
            self.updateValues()
            print (self.checkbox_states[checkbox])

    def print_checkbox_states(self):
        for checkbox, state in self.checkbox_states.items():
            print(state)

    #Estimated print time function
    def calculate_estimated_print_time(self, file_path):
        # Read the JSON file and calculate the object count
        object_count = 0
        try:
            with open(file_path) as f:
                json_data = json.load(f)
                object_list = json_data.get('itemList', [])
                object_count = 250 * sum(1 for object_name in object_list if object_name.get('itemId'))

            # Calculate the estimated print time in seconds
            estimated_print_time_seconds = self.low_performance_var * object_count

            # Convert to minutes if greater than 60 seconds
            if estimated_print_time_seconds > 60:
                estimated_print_time_minutes = estimated_print_time_seconds / 60
                estimated_print_time = round(estimated_print_time_minutes, 2)
                time_unit = "minutes"
            else:
                estimated_print_time = round(estimated_print_time_seconds, 2)
                time_unit = "seconds"
            
        except FileNotFoundError as e:
            # Handle the file not found error
                print("File not found:", file_path)
                print("Error:", str(e))

        # Display the estimated print time in the GUI
        self.printEstimatedSpeedLabel.setText(f"Estimated Print Time: {estimated_print_time} {time_unit}")

    def updateColTFCounter(self,value):
        global totalCount
        global runtimeCount
        if value == 2:
            self.collectionTF = True
        else:
            self.collectionTF = False
        print(self.collectionTF)

        if self.collectionTF == False:
            self.objectsProgressLabel.setText("Objects Processed: 0 / {}".format(totalCount))
            self.totalProgressBar.setMaximum(totalCount)
        else:
            self.objectsProgressLabel.setText("Objects Processed: 0 / {}".format(runtimeCount))
    
    def updateValues(self):
        global objectListSizes
        global runtimeCount
        global collection_counts
        updatedValue = 0
        print("Updating values")
        print(list(map(str, self.checkbox_states.values())))

        checkbox_keys = list(self.checkbox_states.keys())  # Convert dict_keys object to a list

        for x, value in enumerate(self.checkbox_states.values()):
            if bool(value) == True: 
                collection = str(checkbox_keys[x].text()).split(" (")[0]  # Remove the count from the collection name
                if collection in collection_counts:
                    count = collection_counts[collection]
                    updatedValue += count

        runtimeCount = updatedValue

        if self.collectionTF == True:
            self.objectsProgressLabel.setText("Objects Processed: 0 / {}".format(updatedValue))
            if updatedValue == 0:
                updatedValue = 999
            self.totalProgressBar.setMaximum(updatedValue)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = mainUI()
    ui.show()
    ui.change_theme("DefaultTheme")
    app.exec_()
#https://stackoverflow.com/questions/13674792/qobjectconnect-cannot-queue-arguments-of-type-qtextcursor