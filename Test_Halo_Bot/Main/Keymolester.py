import pyautogui
import time

##Execution of Top Level Functions

key_count = 0
key_to_count = 'itemId'

def process_objects(item_list, key_count=0):
    for object_name in item_list:
        print(f"Processing object '{object_name['objectName']}'")
        start(object_name)
        key_count -= 1
        print(f"There are {key_count} objects left to process in the JSON file.")
        print('-' * 20)
        time.sleep(0.25)
    return key_count




##Notes for correct object selection later
#For objects with a scale smaller than .5 use ankle cover B - Note it won't work for objects with a scale larger than 99,800,150 XYZ respeactively
#For objects with a scale larger than 99,800,150 use Floor half B

## User required steps
# Spawn Object
# Required to start in OBJ prop tab with General highlited
# Consider saving after every 150 objects
#


#Keystrokes library
def duplicate_Obj():
    #pyautogui.hotkey('ctrl', 'd')
    print('Duplicate Object')

def get_Property():
    #pyautogui.hotkey('ctrl', '2')
    print('Get Property')

def open_close_Property():
    #pyautogui.typewrite('r')
    print('Open Close Property')

def top():
    #pyautogui.typewrite('z')
    print('Top')

def up():
    #pyautogui.typewrite(['up'])
    print('Up')

def down():
    #pyautogui.typewrite(['down'])
    print('Down')

def left():
    #pyautogui.typewrite(['left'])
    print('Left')

def right():
    #pyautogui.typewrite(['right'])
    print('Right')

def enter():
    #pyautogui.typewrite(['enter'])
    print('Enter')

def start(object_name):
    down()
    down()
    down()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''scaleX'']))')
    enter()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''scaleY'']))')
    enter()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''scaleZ'']))')
    enter()

    down()
    down()
    down()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''positionX'']))')
    enter()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''positionY'']))')
    enter()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''positionZ'']))')
    enter()

    down()
    down()
    down()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''rotationX'']))')
    enter()
    up()
    up()
    enter()
    print('pyautogui.typewrite(str(object_name[''rotationZ'']))')
    enter()
    down()
    enter()
    print('pyautogui.typewrite(str(object_name[''rotationY'']))')
    enter()

    top()
    open_close_Property()
    duplicate_Obj()
#Actions
#
#Start of script
#OBJ Prop Tab - Required to start at General
# X Scale - 4 Down Inputs 
#Enter/Space Bar
#Inpute Values
#Enter
#Y Scale - Down 1
# Enter/Space Bar
#Inpute Values
#Enter
#Z Scale - Down1
#Enter/Space Bar
#Input Values
#Enter

#X Pos - 4 Down Inputs
#Enter/Space Bar
#Input Values
#Enter
#Y Pos - Down 1
# Enter/Space Bar
#Inpute Values
#Enter
#Z Pos - Down 1
#Enter/Space Bar
#Input Values
#Enter

#ROLL(X) - 4 Down Inputs
#Enter/Space Bar
#Input Values
#Enter
#YAW(Z) Scale - 2 Up
#Enter/Space Bar
#Input Values
#Enter
#PITCH(Y) Scale - Down 1
# Enter/Space Bar
#Input Values
#Enter

# Return to General - Z
# Release obj prop menu - R
# Duplicate obj - Ctrl D
#
#
#

