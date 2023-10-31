import pydirectinput
import pyautogui
import pyperclip
import sys
import time
import Sorter
import keyboard

################################
#
# Written by: Uber/bpsherwo
#
# Documentation for this .py file will be notated with commented out code that looks like this, as well as 
# having ## DOC in front of any comments. If you are here and have not read the README.md, read that first.
#
# This Documentation will be an explanation of the code and all of the processes to a beginner such that you should not
# *need* to know how to code to understand what is going on. It may not cover 101% of what goes on in these files because
# not only would that be overkill, it would be redundant for alot of the code. If you already know Python, you're ahead.
# 
# If you are trying to understand the entire project top to bottom, here is the recommended order for you to read the
# files and their documentation (if you just want to understand this file, ignore this recommendation):
#
# Gui.py -> Bot.py -> Sorter.py -> Keymanager.py -> mirvTranslator.py
# 
# Do note that technically, Keymanager is ran before Sorter, but Sorter is called right at the beginning of Keymanager, and
# for reasons you will see later, cannot run without Sorter.
#
################################

# mirvTranslator.py Foreword
################################
#
# At a high level, mirvTranslator.py is the driving force behind the Object Properties menu navigation. When B2FP starts 
# finding an object in the Object Browser and applying transforms to it (position, scale, rotation) in the Object Properties 
# Menu, that is all mirvTranslator.py. Many of the functions higher up in the file only exist to reduce redundant lines of 
# code for identical keypresses and increase modularity (ex. Need to save? Run save the save function. Don't write out the 
# keypresses to back out of the menu and save every time.)
#
# It is rather obvious just by looking at it, but essentially this tool is just pressing keys on your keyboard and copy+pasting 
# transform values into the relative fields (and in the future, much much more) in-game so that you don't have to. Additionally, 
# we do it very fast.
#
################################

## DOC - Simply a function to press CTRL+V.
def paste(vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering paste() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        time.sleep(.055)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('v')
        pydirectinput.keyUp('ctrl')
        if vLog == True:
            print('vLOG: mirvTranslator.py: Paste')
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting paste() function.")
            sys.stdout.flush()
        break

## DOC - Simply a function to exit out of any menus and save your game.
def save(low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering save() function.")
        sys.stdout.flush()
    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in save() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance
        time.sleep(0.075)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('3')
        pydirectinput.keyUp('ctrl')
        time.sleep(0.075)
        pydirectinput.press(['escape'])
        time.sleep(0.075)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('s')
        pydirectinput.keyUp('ctrl')
        time.sleep(0.075)
        print('Map Saved!')
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting save() function.")
            sys.stdout.flush()
        break

## DOC - Duplicaes an object. We don't actually use this anymore, but we figured we'd leave it in case we need to use it in the future.
def duplicate_Obj(vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering duplicate_Obj() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('d')
        time.sleep(.02)
        pydirectinput.keyUp('ctrl')
        print('Duplicating Object')
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting duplicate_Obj() function.")
            sys.stdout.flush()
        break

## DOC - Simply goes to the Object Properties Menu.
def goToProperties(low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering goToProperties() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance
        pydirectinput.keyDown('ctrl')
        time.sleep(0.055)
        pydirectinput.press('2')
        time.sleep(0.055)
        pydirectinput.keyUp('ctrl')
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting goToProperties() function.")
            sys.stdout.flush()
        break

## DOC - This one literally presses 0. Don't ask me why we did this.
def resetRotation(low_performance, position_only, vLog):
    pydirectinput.PAUSE = low_performance
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering resetRotation() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        time.sleep(low_performance + 0.3)
        if position_only == False:
            pydirectinput.press('0')
            sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting resetRotation() function.")
            sys.stdout.flush()
        break

## DOC - Simply goes to the Object Browser Menu.
def goToObjBrowser(low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering goToObjBrowser() function.")
        sys.stdout.flush()
    pydirectinput.PAUSE = low_performance
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        time.sleep(low_performance + 0.05)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('1')
        pydirectinput.keyUp('ctrl')
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting goToObjBrowser() function.")
            sys.stdout.flush()
        break

## DOC - This function presses 1, 2, and 0 a few times. Sometimes your widgets "soft-lock" when you send inputs to your game quickly, this function eases out of the soft-lock. Pressing 0 also resets rotation.
def onetwozero(low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering onetwozero() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance
        time.sleep(0.1)
        pydirectinput.press('1',presses= 2)
        time.sleep(0.1)
        pydirectinput.press('2',presses= 2)
        time.sleep(0.1)
        pydirectinput.press('0',presses= 2)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting onetwozero() function.")
            sys.stdout.flush()
        break

## DOC - This is the function that has mapping to go from "Recent" in the Object Browser to the current object.
def moveToObject(s1,s2,s3, low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering moveToObject() function.")
        print("vLOG: mirvTranslator.py: Keypresses to Folder: {}".format(s1))
        print("vLOG: mirvTranslator.py: Keypresses to Subfolder: {}".format(s2))
        print("vLOG: mirvTranslator.py: Keypresses to Object: {}".format(s3))
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance + 0.002
        pydirectinput.press(['down'],presses= s1)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses= s2)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses= s3)
        pydirectinput.press(['space'])
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting moveToObject() function.")
            sys.stdout.flush()
        break

## DOC - This function is identical to moveToObject() above, but does not actually spawn the object. 
def moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering moveToObjectNoSpawn() function.")
        print("vLOG: mirvTranslator.py: Keypresses to Folder: {}".format(s1))
        print("vLOG: mirvTranslator.py: Keypresses to Subfolder: {}".format(s2))
        print("vLOG: mirvTranslator.py: Keypresses to Object: {}".format(s3))
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance + 0.002
        pydirectinput.press(['down'],presses= s1)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses= s2)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses= s3)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting moveToObjectNoSpawn() function.")
            sys.stdout.flush()
        break

## DOC - This function goes from wherever you are in the Object Browser to the root, aka "Recents".
def revMoveToObject(s3,s2,s1, low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering revMoveToObject() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance + 0.002
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('1')
        pydirectinput.keyUp('ctrl')
        time.sleep(0.075)
        pydirectinput.press('backspace')
        time.sleep(0.075)
        pydirectinput.press('backspace')
        time.sleep(0.075)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('1')
        pydirectinput.keyUp('ctrl')
        time.sleep(0.075)
        pydirectinput.press('tab')
        pydirectinput.press('tab')
        pydirectinput.press('z')
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting revMoveToObject() function.")
            sys.stdout.flush()
        break

## DOC - This function spawns a GRD Spartan Doll and uses it to force your transform widget to the rotation widget.
def setRotationAxis(low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering setRotationAxis() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance
        sys.stdout.flush()
        print("Forcing Rotation Axis...")
        pydirectinput.press('ctrl', presses=2)
        pydirectinput.press(['up'],presses=2)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses=3)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses=5)
        pydirectinput.press(['space'])
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling onetwozero() function.")
            sys.stdout.flush()
        onetwozero(low_performance, vLog)
        pydirectinput.keyDown('space')
        pydirectinput.keyDown('shift')
        time.sleep(0.3)
        pydirectinput.keyUp('shift')
        pydirectinput.keyUp('space')
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        pydirectinput.press(['up'],presses=5)
        pydirectinput.press(['escape'])
        pydirectinput.press(['up'],presses=3)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'], presses=2)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting setRotationAxis() function.")
            sys.stdout.flush()
        break

## DOC - Different from the similar sounding duplicateObject function, this function spawns another of whatever the most recently spawned object is.
def replicateObject(low_performance, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering replicateObject() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        pydirectinput.PAUSE = low_performance
        pydirectinput.press('ctrl')
        time.sleep(low_performance+0.10)
        pydirectinput.keyDown('ctrl')
        pydirectinput.press('1')
        pydirectinput.keyUp('ctrl')
        pydirectinput.press(['space'])
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting replicateObject() function.")
            sys.stdout.flush()
        break

## DOC - Called when a user asked to be warned when they print 500 objects, stop_me was 2.
def objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog):
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objectOverflowCheck() function.")
        sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        failsafe = pyautogui.confirm('500 objects have been printed in the current sprint!\nHalo Infinite crashing is extremely likely past this point.\nContinue?', title="HIFB v0.9.3", buttons=('Continue','Save & Continue','Save & End Print'))
        if failsafe == "Continue":
            print("You asked for it...")
        elif failsafe == "Save & Continue":
            print("Saving and proceeding...")
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling save() function.")
            sys.stdout.flush()
            save(low_performance, vLog)
        elif failsafe == "Save & End Print":
            print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling save() function.")
                sys.stdout.flush()
            save(low_performance, vLog)
            print("Please check objects for placement, rotation, and scaling accuracy.")
            sys.exit(0)
        else:
            print('You asked for it...')
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objectOverflowCheck() function.")
            sys.stdout.flush()
        break

## DOC - This object translation function is for "normal" objects, meaning they spawn on Phased physics, have an Object Mode field, and 
# scale, rotate, and position menus. You will notice that every object translation function has a daughter function, which is the 
# giveProperties equivalent function for each menu configuration. For example, objTranslationNoScale() has the daughter function 
# givePropertiesNoScale(). objTranslationNoObjectMode() has the daughter function givePropertiesNoObjectMode(), etc. All of the 
# "parent" functions from here down to the bottom of this file are all essentially the same, except they each point to their own 
# daughter function. With that said, I will document only objTranslation() and giveProperties(), and you can apply the same logic 
# to each of them.
# 
# Note: There is alot of duplicate, inefficient, and extraneous code in the object Translation functions (that needs to be fixed/technical debt has to be paid). Be my guest if you want to optimize it.
def objTranslation(objects, ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, s1, s2, s3):
    
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objTranslation() function.")
        sys.stdout.flush()


    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in objTranslation() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        print("Object(s) have standard menu layout.")
        subTick = ticker
        pydirectinput.PAUSE = low_performance
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling moveToObject() function.")
            sys.stdout.flush()
        moveToObject(s1,s2,s3, low_performance, vLog)

## DOC - Starts iterating through the list of the objects passed down to it. Points to its daughter function, giveProperties(), to 
# input scale, position, and rotation, in that order.
        for object in objects:
            if vLog == True:
                print("vLOG: mirvTranslator.py: Processing Object: {} / {}".format(subTick + start_index, listLength + start_index))
                print("vLOG: mirvTranslator.py: Calling resetRotation() function.")
                sys.stdout.flush()
            resetRotation(low_performance, position_only, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling goToProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            goToProperties(low_performance, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling giveProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            giveProperties(object, low_performance, position_only, vLog)
            time.sleep(0.1)
            pydirectinput.press('z')

## DOC - Checks the value of End Index against the current index of the print. If a user enabled End Index and set a value, it would end here.
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if End Index Check is True...")
                print("vLOG: mirvTranslator.py: Pre-check value = {}".format(vLog))
                sys.stdout.flush()
            if end_index_check == True:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: End Index Check was True.")
                    sys.stdout.flush()
                if subTick == (end_index - start_index - 1):
                    print("End Index Reached! Saving and ending bot process.")
                    print("Objects processed: {} / {}".format(subTick + start_index + 1, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)

## DOC - Logic to pause the bot process and ask the user if they want to continue or not every 500 objects (if they opted to do so)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if subTick has reached stop_me threshold...")
                sys.stdout.flush()
            if subTick == 499 or subTick == 999 or subTick == 1499 or subTick == 1999 or subTick == 2499 or subTick == 2999 or subTick == 3499 or subTick == 3999 or subTick == 4499 or subTick == 4999:
                if vLog == True:
                    print("vLOG: mirvtranslator.py: subTick reached stop_me threshold!")
                    sys.stdout.flush()
                if stop_me == '1':
                    print("Recommended object limit exceeded! Halo Infinite crash is likely...")
                    sys.stdout.flush()
                elif stop_me == '2':
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling objectOverflowCheck() function.")
                        sys.stdout.flush()
                    objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog)
                elif stop_me == '3':
                    print("Recommended object limit reached!")
                    print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
                else:
                    print("Stop_me was not 1, 2, or 3.")

## DOC - Logic to see if the bot needs to stop and save the game, then resume printing
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if save_interval_check is True & subTick is not 0...")
                print("vLOG: mirvTranslator.py: subTick: {}".format(subTick))
                sys.stdout.flush()
            if save_interval_check == True and subTick != 0:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: save_interval_check was True.")
                    sys.stdout.flush()
                if ((subTick+1) % save_interval) == 0:
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling moveToObjectNoSpawn() function.")
                        sys.stdout.flush()
                    moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog)

## DOC - If the number of objects spawned is not equal to the list size of the current group of objects, spawn in another object of the same itemId.
            if objects.index(object) != (len(objects)-1):
                time.sleep(0.1)
                if vLog == True:
                    print("vLOG: mirvTranslator.py: Calling replicateObject() function.")
                    sys.stdout.flush()
                replicateObject(low_performance, vLog)
                time.sleep(0.1)

            
            subTick += 1
            
            print("Objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            sys.stdout.flush()

## DOC - When a group of objects with this mapping has been printed, return to root ("Recents") and prepare to go to the next object type.
        print("Returning Home...")
        sys.stdout.flush()
        time.sleep(0.15)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
            sys.stdout.flush()
        revMoveToObject(s3,s2,s1, low_performance, vLog)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objTranslation() function.")
            sys.stdout.flush()
        break

## DOC - The giveProperties function simply takes the transform values from the item's export data, copies the 
# values, and pastes them in-game in the appropriate field. Other giveProperties variations include keypresses 
# to set physics to Phased, change Object Mode from Dynamic to Static, etc.
def giveProperties(object, low_performance, position_only, vLog):
    
    #clipboard = ""

    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering giveProperties() function.")
        sys.stdout.flush() 
    
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
## DOC - If you set an X, Y, or Z Offset, that is applied here.
        xBump = int(sys.argv[7])
        yBump = int(sys.argv[8])
        zBump = int(sys.argv[9])
        
        pydirectinput.PAUSE = low_performance
        time.sleep(low_performance + 0.05)
        if position_only == False:
        #Scale Manipulation
            print("Processing Scale of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Scale X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses= 4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Z
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
        else:
            pydirectinput.press(['down'],presses= 5)

    #Position Manipulation
        print("Processing Position of object: {}".format({object['objectName']}))
        sys.stdout.flush()

        #Position X
        time.sleep(low_performance)
        pydirectinput.press(['down'],presses= 4)
        pydirectinput.press(['space']) 
        object['positionX'] = float(object['positionX']) + xBump
        pyperclip.copy(str(object['positionX']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionY'] = float(object['positionY']) + yBump
        pyperclip.copy(str(object['positionY']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionZ'] = float(object['positionZ']) + zBump
        pyperclip.copy(str(object['positionZ']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        if position_only == False:
        #Rotation Manipulation
            print("Processing Rotation of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Rotation X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses=4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Rotation Z
            pydirectinput.press(['up'],presses=2)
            pydirectinput.press(['space'])  
            pyperclip.copy(str(object['rotationZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])

            #Rotation Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
            sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting giveProperties() function.")
            sys.stdout.flush()
        break

def objTranslationNoScale(objects, ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, s1, s2, s3):
    
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objTranslationNoScale() function.")
        sys.stdout.flush()
    
    
    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in objTranslationNoScale() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        print("Object(s) has no Scale Menu!")
        subTick = ticker
        pydirectinput.PAUSE = low_performance
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling moveToObject() function.")
            sys.stdout.flush()
        moveToObject(s1,s2,s3, low_performance, vLog)


        for object in objects:
            if vLog == True:
                print("vLOG: mirvTranslator.py: Processing Object: {} / {}".format(subTick + start_index, listLength + start_index))
                print("vLOG: mirvTranslator.py: Calling resetRotation() function.")
                sys.stdout.flush()
            resetRotation(low_performance, position_only, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling goToProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            goToProperties(low_performance, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling givePropertiesNoScale() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            givePropertiesNoScale(object, low_performance, position_only, vLog)
            time.sleep(0.1)
            pydirectinput.press('z')


            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if End Index Check is True...")
                print("vLOG: mirvTranslator.py: Pre-check value = {}".format(vLog))
                sys.stdout.flush()
            if end_index_check == True:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: End Index Check was True.")
                    sys.stdout.flush()
                if subTick == (end_index - start_index - 1):
                    print("End Index Reached! Saving and ending bot process.")
                    print("Objects processed: {} / {}".format(subTick + start_index + 1, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)


            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if subTick has reached stop_me threshold...")
                sys.stdout.flush()
            if subTick == 499 or subTick == 999 or subTick == 1499 or subTick == 1999 or subTick == 2499 or subTick == 2999 or subTick == 3499 or subTick == 3999 or subTick == 4499 or subTick == 4999:
                if vLog == True:
                    print("vLOG: mirvtranslator.py: subTick reached stop_me threshold!")
                    sys.stdout.flush()
                if stop_me == '1':
                    print("Recommended object limit exceeded! Halo Infinite crash is likely...")
                    sys.stdout.flush()
                elif stop_me == '2':
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling objectOverflowCheck() function.")
                        sys.stdout.flush()
                    objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog)
                elif stop_me == '3':
                    print("Recommended object limit reached!")
                    print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
                else:
                    print("Stop_me was not 1, 2, or 3.")


            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if save_interval_check is True & subTick is not 0...")
                print("vLOG: mirvTranslator.py: subTick: {}".format(subTick))
                sys.stdout.flush()
            if save_interval_check == True and subTick != 0:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: save_interval_check was True.")
                    sys.stdout.flush()
                if ((subTick+1) % save_interval) == 0:
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling moveToObjectNoSpawn() function.")
                        sys.stdout.flush()
                    moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog)


            if objects.index(object) != (len(objects)-1):
                time.sleep(0.1)
                if vLog == True:
                    print("vLOG: mirvTranslator.py: Calling replicateObject() function.")
                    sys.stdout.flush()
                replicateObject(low_performance, vLog)
                time.sleep(0.1)
            
            
            subTick += 1
            
            print("Objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            sys.stdout.flush()
        

        print("Returning Home...")
        sys.stdout.flush()
        time.sleep(0.15)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
            sys.stdout.flush()
        revMoveToObject(s3,s2,s1, low_performance, vLog)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objTranslationNoScale() function.")
            sys.stdout.flush()
        break

def givePropertiesNoScale(object, low_performance, position_only, vLog):
    if vLog == True:
            print("vLOG: mirvTranslator.py: Entering givePropertiesNoScale() function.")
            sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        xBump = int(sys.argv[7])
        yBump = int(sys.argv[8])
        zBump = int(sys.argv[9])
        
        pydirectinput.PAUSE = low_performance
        time.sleep(low_performance + 0.05)

        #Position Manipulation
        print("Processing Position of object: {}".format({object['objectName']}))
        sys.stdout.flush()

        #Position X
        time.sleep(low_performance)
        pydirectinput.press(['down'],presses= 6)
        pydirectinput.press(['space']) 
        object['positionX'] = float(object['positionX']) + xBump
        pyperclip.copy(str(object['positionX']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionY'] = float(object['positionY']) + yBump
        pyperclip.copy(str(object['positionY']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionZ'] = float(object['positionZ']) + zBump
        pyperclip.copy(str(object['positionZ']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        if position_only == False:
            #Rotation Manipulation
            print("Processing Rotation of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Rotation X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses=4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Rotation Z
            pydirectinput.press(['up'],presses=2)
            pydirectinput.press(['space'])  
            pyperclip.copy(str(object['rotationZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])

            #Rotation Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
            sys.stdout.flush()
            if vLog == True:
                print("vLOG: mirvTranslator.py: Exiting givePropertiesNoScale() function.")
                sys.stdout.flush()
            break

def objTranslationStartsFixedNoScale(objects, ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, s1, s2, s3):
    
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objTranslationStartsFixedNoScale() function.")
        sys.stdout.flush()

    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in objTranslationStartsFixedNoScale() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        print("Object(s) starts with Fixed physics and has No Scale Menu!")
        subTick = ticker
        pydirectinput.PAUSE = low_performance
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling moveToObject() function.")
            sys.stdout.flush()
        moveToObject(s1,s2,s3, low_performance, vLog)

        for object in objects:
            if vLog == True:
                print("vLOG: mirvTranslator.py: Processing Object: {} / {}".format(subTick + start_index, listLength + start_index))
                print("vLOG: mirvTranslator.py: Calling resetRotation() function.")
                sys.stdout.flush()
            resetRotation(low_performance, position_only, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling goToProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            goToProperties(low_performance, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling givePropertiesStartsFixedNoScale() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            givePropertiesStartsFixedNoScale(object, low_performance, position_only, vLog)
            time.sleep(0.1)
            pydirectinput.press('z')

            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if End Index Check is True...")
                print("vLOG: mirvTranslator.py: Pre-check value = {}".format(vLog))
                sys.stdout.flush()
            if end_index_check == True:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: End Index Check was True.")
                    sys.stdout.flush()
                if subTick == (end_index - start_index - 1):
                    print("End Index Reached! Saving and ending bot process.")
                    print("Objects processed: {} / {}".format(subTick + start_index + 1, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
            

            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if subTick has reached stop_me threshold...")
                sys.stdout.flush()
            if subTick == 499 or subTick == 999 or subTick == 1499 or subTick == 1999 or subTick == 2499 or subTick == 2999 or subTick == 3499 or subTick == 3999 or subTick == 4499 or subTick == 4999:
                if vLog == True:
                    print("vLOG: mirvtranslator.py: subTick reached stop_me threshold!")
                    sys.stdout.flush()
                if stop_me == '1':
                    print("Recommended object limit exceeded! Halo Infinite crash is likely...")
                    sys.stdout.flush()
                elif stop_me == '2':
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling objectOverflowCheck() function.")
                        sys.stdout.flush()
                    objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog)
                elif stop_me == '3':
                    print("Recommended object limit reached!")
                    print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
                else:
                    print("Stop_me was not 1, 2, or 3.")

            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if save_interval_check is True & subTick is not 0...")
                print("vLOG: mirvTranslator.py: subTick: {}".format(subTick))
                sys.stdout.flush()
            if save_interval_check == True and subTick != 0:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: save_interval_check was True.")
                    sys.stdout.flush()
                if ((subTick+1) % save_interval) == 0:
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling moveToObjectNoSpawn() function.")
                        sys.stdout.flush()
                    moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog)

            if objects.index(object) != (len(objects)-1):
                time.sleep(0.1)
                if vLog == True:
                    print("vLOG: mirvTranslator.py: Calling replicateObject() function.")
                    sys.stdout.flush()
                replicateObject(low_performance, vLog)
                time.sleep(0.1)

            subTick += 1
        
            print("Objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            sys.stdout.flush()
        
        print("Returning Home...")
        sys.stdout.flush()
        time.sleep(0.15)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
            sys.stdout.flush()
        revMoveToObject(s3,s2,s1, low_performance, vLog)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objTranslationStartsFixedNoScale() function.")
            sys.stdout.flush()
        break

def givePropertiesStartsFixedNoScale(object, low_performance, position_only, vLog):
    #clipboard = ""

    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering givePropertiesStartsFixedNoScale() function.")
        sys.stdout.flush() 
    
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        xBump = int(sys.argv[7])
        yBump = int(sys.argv[8])
        zBump = int(sys.argv[9])
        
        pydirectinput.PAUSE = low_performance
        time.sleep(low_performance + 0.05)
    
    #Correcting Physics type...
        pydirectinput.press(['down'],presses= 3)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses= 3)
        pydirectinput.press(['space'])
        pydirectinput.press(['down'],presses= 3)

    #Position Manipulation
        print("Processing Position of object: {}".format({object['objectName']}))
        sys.stdout.flush()

        #Position X
        time.sleep(low_performance)
        pydirectinput.press(['space']) 
        object['positionX'] = float(object['positionX']) + xBump
        pyperclip.copy(str(object['positionX']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionY'] = float(object['positionY']) + yBump
        pyperclip.copy(str(object['positionY']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionZ'] = float(object['positionZ']) + zBump
        pyperclip.copy(str(object['positionZ']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        if position_only == False:
        #Rotation Manipulation
            print("Processing Rotation of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Rotation X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses=4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Rotation Z
            pydirectinput.press(['up'],presses=2)
            pydirectinput.press(['space'])  
            pyperclip.copy(str(object['rotationZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])

            #Rotation Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
            sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting giveProperties() function.")
            sys.stdout.flush()
        break

def objTranslationStartsDynamicAndFixed(objects, ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, s1, s2, s3):
    
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objTranslationStartsDynamicAndFixed() function.")
        sys.stdout.flush()


    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in objTranslationStartsDynamicAndFixed() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        print("Object(s) starts Dynamic and Fixed!")
        subTick = ticker
        pydirectinput.PAUSE = low_performance
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling moveToObject() function.")
            sys.stdout.flush()
        moveToObject(s1,s2,s3, low_performance, vLog)
        
        
        for object in objects:
            if vLog == True:
                print("vLOG: mirvTranslator.py: Processing Object: {} / {}".format(subTick + start_index, listLength + start_index))
                print("vLOG: mirvTranslator.py: Calling resetRotation() function.")
                sys.stdout.flush()
            resetRotation(low_performance, position_only, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling goToProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            goToProperties(low_performance, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling givePropertiesStartsDynamicAndFixed() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            givePropertiesStartsDynamicAndFixed(object, low_performance, position_only, vLog)
            time.sleep(0.1)
            pydirectinput.press('z')
            #pydirectinput.press(['down'])
            #pydirectinput.press(['space'])
            time.sleep(0.055)
            #pydirectinput.press(['enter'])
           
           
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if End Index Check is True...")
                print("vLOG: mirvTranslator.py: Pre-check value = {}".format(vLog))
                sys.stdout.flush()
            if end_index_check == True:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: End Index Check was True.")
                    sys.stdout.flush()
                if subTick == (end_index - start_index - 1):
                    print("End Index Reached! Saving and ending bot process.")
                    print("Objects processed: {} / {}".format(subTick + start_index + 1, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
            
            
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if subTick has reached stop_me threshold...")
                sys.stdout.flush()
            if subTick == 499 or subTick == 999 or subTick == 1499 or subTick == 1999 or subTick == 2499 or subTick == 2999 or subTick == 3499 or subTick == 3999 or subTick == 4499 or subTick == 4999:
                if vLog == True:
                    print("vLOG: mirvtranslator.py: subTick reached stop_me threshold!")
                    sys.stdout.flush()
                if stop_me == '1':
                    print("Recommended object limit exceeded! Halo Infinite crash is likely...")
                    sys.stdout.flush()
                elif stop_me == '2':
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling objectOverflowCheck() function.")
                        sys.stdout.flush()
                    objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog)
                elif stop_me == '3':
                    print("Recommended object limit reached!")
                    print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
                else:
                    print("Stop_me was not 1, 2, or 3.")
            
            
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if save_interval_check is True & subTick is not 0...")
                print("vLOG: mirvTranslator.py: subTick: {}".format(subTick))
                sys.stdout.flush()
            if save_interval_check == True and subTick != 0:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: save_interval_check was True.")
                    sys.stdout.flush()
                if ((subTick+1) % save_interval) == 0:
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling moveToObjectNoSpawn() function.")
                        sys.stdout.flush()
                    moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog)
            
            
            if objects.index(object) != (len(objects)-1):
                time.sleep(0.1)
                if vLog == True:
                    print("vLOG: mirvTranslator.py: Calling replicateObject() function.")
                    sys.stdout.flush()
                replicateObject(low_performance, vLog)
                time.sleep(0.1)
            
            
            subTick += 1
            
            print("Objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            sys.stdout.flush()
        

        print("Returning Home...")
        sys.stdout.flush()
        time.sleep(0.15)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
            sys.stdout.flush()
        revMoveToObject(s3,s2,s1, low_performance, vLog)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objTranslationStartsDynamicAndFixed() function.")
            sys.stdout.flush()
        break

def givePropertiesStartsDynamicAndFixed(object, low_performance, position_only, vLog):
    if vLog == True:
            print("vLOG: mirvTranslator.py: Entering givePropertiesStartsDynamicAndFixed() function.")
            sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        xBump = int(sys.argv[7])
        yBump = int(sys.argv[8])
        zBump = int(sys.argv[9])
        
        pydirectinput.PAUSE = low_performance
        time.sleep(low_performance + 0.05)

        pydirectinput.press(['down'],presses= 3)
        pydirectinput.press(['space'])
        time.sleep(0.075)
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        time.sleep(0.2)
        pydirectinput.press(['down'],presses= 4)
        pydirectinput.press(['space'])
        time.sleep(0.075)
        pydirectinput.press(['down'],presses= 2)
        pydirectinput.press(['space'])
        time.sleep(0.075)
        pydirectinput.press(['up'],presses=3)
        time.sleep(0.075)

        if position_only == False:
        #Scale Manipulation
            print("Processing Scale of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Scale X
            time.sleep(low_performance)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Z
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
        else:
            pydirectinput.press(['down'],presses= 5)

    #Position Manipulation
        print("Processing Position of object: {}".format({object['objectName']}))
        sys.stdout.flush()

        #Position X
        time.sleep(low_performance)
        pydirectinput.press(['down'],presses= 4)
        pydirectinput.press(['space']) 
        object['positionX'] = float(object['positionX']) + xBump
        pyperclip.copy(str(object['positionX']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionY'] = float(object['positionY']) + yBump
        pyperclip.copy(str(object['positionY']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionZ'] = float(object['positionZ']) + zBump
        pyperclip.copy(str(object['positionZ']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        if position_only == False:
        #Rotation Manipulation
            print("Processing Rotation of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Rotation X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses=4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Rotation Z
            pydirectinput.press(['up'],presses=2)
            pydirectinput.press(['space'])  
            pyperclip.copy(str(object['rotationZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])

            #Rotation Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
            sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting givePropertiesStartsDynamicAndFixed() function.")
            sys.stdout.flush()
        break

def objTranslationNoObjectMode(objects, ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, s1, s2, s3):
    
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objTranslationNoObjectMode() function.")
        sys.stdout.flush()
    
    
    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in objTranslationNoObjectMode() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        print("Object(s) has no Object Mode setting!")
        subTick = ticker
        pydirectinput.PAUSE = low_performance
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling moveToObject() function.")
            sys.stdout.flush()
        moveToObject(s1,s2,s3, low_performance, vLog)
       
       
        for object in objects:
            if vLog == True:
                print("vLOG: mirvTranslator.py: Processing Object: {} / {}".format(subTick + start_index, listLength + start_index))
                print("vLOG: mirvTranslator.py: Calling resetRotation() function.")
                sys.stdout.flush()
            resetRotation(low_performance, position_only, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling goToProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            goToProperties(low_performance, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling givePropertiesNoObjectMode() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            givePropertiesNoObjectMode(object, low_performance, position_only, vLog)
            time.sleep(0.1)
            pydirectinput.press('z')
            
            
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if End Index Check is True...")
                print("vLOG: mirvTranslator.py: Pre-check value = {}".format(vLog))
                sys.stdout.flush()
            if end_index_check == True:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: End Index Check was True.")
                    sys.stdout.flush()
                if subTick == (end_index - start_index - 1):
                    print("End Index Reached! Saving and ending bot process.")
                    print("Objects processed: {} / {}".format(subTick + start_index + 1, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
            
            
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if subTick has reached stop_me threshold...")
                sys.stdout.flush()
            if subTick == 499 or subTick == 999 or subTick == 1499 or subTick == 1999 or subTick == 2499 or subTick == 2999 or subTick == 3499 or subTick == 3999 or subTick == 4499 or subTick == 4999:
                if vLog == True:
                    print("vLOG: mirvtranslator.py: subTick reached stop_me threshold!")
                    sys.stdout.flush()
                if stop_me == '1':
                    print("Recommended object limit exceeded! Halo Infinite crash is likely...")
                    sys.stdout.flush()
                elif stop_me == '2':
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling objectOverflowCheck() function.")
                        sys.stdout.flush()
                    objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog)
                elif stop_me == '3':
                    print("Recommended object limit reached!")
                    print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
                else:
                    print("Stop_me was not 1, 2, or 3.")
            
            
            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if save_interval_check is True & subTick is not 0...")
                print("vLOG: mirvTranslator.py: subTick: {}".format(subTick))
                sys.stdout.flush()
            if save_interval_check == True and subTick != 0:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: save_interval_check was True.")
                    sys.stdout.flush()
                if ((subTick+1) % save_interval) == 0:
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling moveToObjectNoSpawn() function.")
                        sys.stdout.flush()
                    moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog)
            
            
            if objects.index(object) != (len(objects)-1):
                time.sleep(0.1)
                if vLog == True:
                    print("vLOG: mirvTranslator.py: Calling replicateObject() function.")
                    sys.stdout.flush()
                replicateObject(low_performance, vLog)
                time.sleep(0.1)

            
            subTick += 1
            
            print("Objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            sys.stdout.flush()
        

        print("Returning Home...")
        sys.stdout.flush()
        time.sleep(0.15)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
            sys.stdout.flush()
        revMoveToObject(s3,s2,s1, low_performance, vLog)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objTranslationNoObjectMode() function.")
            sys.stdout.flush()
        break

def givePropertiesNoObjectMode(object, low_performance, position_only, vLog):
    if vLog == True:
            print("vLOG: mirvTranslator.py: Entering givePropertiesNoObjectMode() function.")
            sys.stdout.flush()
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        xBump = int(sys.argv[7])
        yBump = int(sys.argv[8])
        zBump = int(sys.argv[9])
        
        pydirectinput.PAUSE = low_performance
        time.sleep(low_performance + 0.05)
        if position_only == False:
        #Scale Manipulation
            print("Processing Scale of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Scale X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses= 3)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Z
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
        else:
            pydirectinput.press(['down'],presses= 5)

    #Position Manipulation
        print("Processing Position of object: {}".format({object['objectName']}))
        sys.stdout.flush()

        #Position X
        time.sleep(low_performance)
        pydirectinput.press(['down'],presses= 4)
        pydirectinput.press(['space']) 
        object['positionX'] = float(object['positionX']) + xBump
        pyperclip.copy(str(object['positionX']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionY'] = float(object['positionY']) + yBump
        pyperclip.copy(str(object['positionY']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionZ'] = float(object['positionZ']) + zBump
        pyperclip.copy(str(object['positionZ']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        if position_only == False:
        #Rotation Manipulation
            print("Processing Rotation of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Rotation X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses=4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Rotation Z
            pydirectinput.press(['up'],presses=2)
            pydirectinput.press(['space'])  
            pyperclip.copy(str(object['rotationZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])

            #Rotation Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
            sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting givePropertiesNoObjectMode() function.")
            sys.stdout.flush()
        break

def objTranslationConfig8(objects, ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, s1, s2, s3):
    
    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering objTranslationConfig8() function.")
        sys.stdout.flush()


    while True:
        if vLog == True:
            print("vLOG: mirvTranslator.py: Emergency stopkey in objTranslation() activated.")
            sys.stdout.flush()
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
        print("Object(s) have standard menu layout.")
        subTick = ticker
        pydirectinput.PAUSE = low_performance
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling moveToObject() function.")
            sys.stdout.flush()
        moveToObject(s1,s2,s3, low_performance, vLog)

        for object in objects:
            if vLog == True:
                print("vLOG: mirvTranslator.py: Processing Object: {} / {}".format(subTick + start_index, listLength + start_index))
                print("vLOG: mirvTranslator.py: Calling resetRotation() function.")
                sys.stdout.flush()
            resetRotation(low_performance, position_only, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling goToProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            goToProperties(low_performance, vLog)
            if vLog == True:
                print("vLOG: mirvTranslator.py: Calling giveProperties() function.")
                sys.stdout.flush()
            time.sleep(0.1)
            givePropertiesConfig8(object, low_performance, position_only, vLog)
            time.sleep(0.1)
            pydirectinput.press('z')

            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if End Index Check is True...")
                print("vLOG: mirvTranslator.py: Pre-check value = {}".format(vLog))
                sys.stdout.flush()
            if end_index_check == True:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: End Index Check was True.")
                    sys.stdout.flush()
                if subTick == (end_index - start_index - 1):
                    print("End Index Reached! Saving and ending bot process.")
                    print("Objects processed: {} / {}".format(subTick + start_index + 1, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)

            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if subTick has reached stop_me threshold...")
                sys.stdout.flush()
            if subTick == 499 or subTick == 999 or subTick == 1499 or subTick == 1999 or subTick == 2499 or subTick == 2999 or subTick == 3499 or subTick == 3999 or subTick == 4499 or subTick == 4999:
                if vLog == True:
                    print("vLOG: mirvtranslator.py: subTick reached stop_me threshold!")
                    sys.stdout.flush()
                if stop_me == '1':
                    print("Recommended object limit exceeded! Halo Infinite crash is likely...")
                    sys.stdout.flush()
                elif stop_me == '2':
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling objectOverflowCheck() function.")
                        sys.stdout.flush()
                    objectOverflowCheck(subTick, low_performance, listLength, start_index, vLog)
                elif stop_me == '3':
                    print("Recommended object limit reached!")
                    print("Stopped bot process, objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    print("Please check objects for placement, rotation, and scaling accuracy.")
                    sys.exit(0)
                else:
                    print("Stop_me was not 1, 2, or 3.")

            if vLog == True:
                print("vLOG: mirvTranslator.py: Checking if save_interval_check is True & subTick is not 0...")
                print("vLOG: mirvTranslator.py: subTick: {}".format(subTick))
                sys.stdout.flush()
            if save_interval_check == True and subTick != 0:
                if vLog == True:
                    print("vLOG: mirvTranslator.py: save_interval_check was True.")
                    sys.stdout.flush()
                if ((subTick+1) % save_interval) == 0:
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
                        sys.stdout.flush()
                    revMoveToObject(s3,s2,s1, low_performance, vLog)
                    print("Saving map...")
                    sys.stdout.flush()
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling save() function.")
                        sys.stdout.flush()
                    save(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
                        sys.stdout.flush()
                    goToObjBrowser(low_performance, vLog)
                    if vLog == True:
                        print("vLOG: mirvTranslator.py: Calling moveToObjectNoSpawn() function.")
                        sys.stdout.flush()
                    moveToObjectNoSpawn(s1,s2,s3, low_performance, vLog)

            if objects.index(object) != (len(objects)-1):
                time.sleep(0.1)
                if vLog == True:
                    print("vLOG: mirvTranslator.py: Calling replicateObject() function.")
                    sys.stdout.flush()
                replicateObject(low_performance, vLog)
                time.sleep(0.1)

            
            subTick += 1
            
            print("Objects processed: {} / {}".format(subTick + start_index, listLength + start_index))
            sys.stdout.flush()

        print("Returning Home...")
        sys.stdout.flush()
        time.sleep(0.15)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling goToObjBrowser() function.")
            sys.stdout.flush()
        goToObjBrowser(low_performance, vLog)
        if vLog == True:
            print("vLOG: mirvTranslator.py: Calling revMoveToObject() function.")
            sys.stdout.flush()
        revMoveToObject(s3,s2,s1, low_performance, vLog)
        sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting objTranslationConfig8() function.")
            sys.stdout.flush()
        break

def givePropertiesConfig8(object, low_performance, position_only, vLog):
    
    #clipboard = ""

    if vLog == True:
        print("vLOG: mirvTranslator.py: Entering givePropertiesConfig8() function.")
        sys.stdout.flush() 
    
    while True:
        if keyboard.is_pressed("f"):
            print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
            sys.exit(0)
## DOC - If you set an X, Y, or Z Offset, that is applied here.
        xBump = int(sys.argv[7])
        yBump = int(sys.argv[8])
        zBump = int(sys.argv[9])
        
        pydirectinput.PAUSE = low_performance
        time.sleep(low_performance + 0.05)
        if position_only == False:
        #Scale Manipulation
            print("Processing Scale of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Scale X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses= 3)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Scale Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['scaleY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 
        else:
            pydirectinput.press(['down'],presses= 5)

    #Position Manipulation
        print("Processing Position of object: {}".format({object['objectName']}))
        sys.stdout.flush()

        #Position X
        time.sleep(low_performance)
        pydirectinput.press(['down'],presses= 4)
        pydirectinput.press(['space']) 
        object['positionX'] = float(object['positionX']) + xBump
        pyperclip.copy(str(object['positionX']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionY'] = float(object['positionY']) + yBump
        pyperclip.copy(str(object['positionY']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Position Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space'])
        object['positionZ'] = float(object['positionZ']) + zBump
        pyperclip.copy(str(object['positionZ']))
        paste(vLog)
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        if position_only == False:
        #Rotation Manipulation
            print("Processing Rotation of object: {}".format({object['objectName']}))
            sys.stdout.flush()

            #Rotation X
            time.sleep(low_performance)
            pydirectinput.press(['down'],presses=4)
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationX']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter']) 

            #Rotation Z
            pydirectinput.press(['up'],presses=2)
            pydirectinput.press(['space'])  
            pyperclip.copy(str(object['rotationZ']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])

            #Rotation Y
            pydirectinput.press(['down'])
            pydirectinput.press(['space']) 
            pyperclip.copy(str(object['rotationY']))
            paste(vLog)
            time.sleep(0.055)
            pydirectinput.press(['enter'])
            sys.stdout.flush()
        if vLog == True:
            print("vLOG: mirvTranslator.py: Exiting givePropertiesConfig8() function.")
            sys.stdout.flush()
        break