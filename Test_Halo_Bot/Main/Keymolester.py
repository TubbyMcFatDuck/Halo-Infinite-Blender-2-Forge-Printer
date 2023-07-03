import pyautogui
import time
import pydirectinput
import sys
import pyperclip

##########LOOK INTO COPY PASTE FUNCTION RATHER THAN TYPEWRITE##########

##Execution of Top Level Functions

key_count = 0
key_to_count = 'itemId'



def process_objects(item_list, key_count=0, stop_flag=False, position_only=None):
    for object_name in item_list:

        print(f"Processing object '{object_name['objectName']}'")
        sys.stdout.flush()

        if position_only:
            start_position(object_name, position_only)
        else:
            start(object_name, position_only)

        key_count -= 1
        print(f"There are {key_count} objects left to process in the JSON file.")
        print('-' * 20)
        if key_count == 0:
            save()
        sys.stdout.flush()
        time.sleep(0.10)
    

    return key_count


def focus_Halo():# Get the list of all open windows
    windows = pyautogui.getAllWindows()  
    # Find the Halo Infinite window by searching for its title
    halo_window = None
    for window in windows:
        if window.title == "Halo Infinite":
            halo_window = window
            break

    # Focus on the Halo Infinite window
    if halo_window:
        pyautogui.click(halo_window.left + 10, halo_window.top + 10)


##Notes for correct object selection later
#For objects with a scale smaller than .5 use ankle cover B - Note it won't work for objects with a scale larger than 99,800,150 XYZ respeactively
#For objects with a scale larger than 99,800,150 use Floor half B

## User required steps
# Spawn Object
# Required to start in OBJ prop tab with General highlited
# Consider saving after every 150 objects
#

def paste():
    time.sleep(.055)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    print('Paste')
    sys.stdout.flush()

def reset_rotation():
    time.sleep(.02)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('0')
    pydirectinput.keyUp('ctrl')
    
def save():
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('s')
    pydirectinput.keyUp('ctrl')
    print('Save batch')

#Keystrokes library
def duplicate_Obj():
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('d')
    time.sleep(.02)
    pydirectinput.keyUp('ctrl')
    print('Duplicating Object')
    sys.stdout.flush()

def get_Property():
    time.sleep(.05)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('2')
    pydirectinput.keyUp('ctrl')
    print('Get Property')



def start(object_name, position_only):
    pydirectinput.PAUSE=0.012
    print(f"processing({object_name}) Scale")
    sys.stdout.flush()
    pydirectinput.press(['down'],presses= 3)
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['scaleX']))
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down'])
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['scaleY']))
    
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down'])
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['scaleZ']))
    
    paste()
    pydirectinput.press(['enter']) 

    print(f"processing({object_name}) Position")
    sys.stdout.flush()
    pydirectinput.press(['down'],presses= 4)
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['positionX']))
    
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down']) 
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['positionY']))
    
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down'])
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['positionZ']))
    
    paste()
    pydirectinput.press(['enter']) 

    print(f"processing({object_name}) Rotation")
    sys.stdout.flush()
    pydirectinput.press(['down'],presses= 4)
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['rotationX']))
    
    paste()
    pydirectinput.press(['enter'])  
    pydirectinput.press(['up'],presses=2)
    pydirectinput.press(['enter'])  
    pyperclip.copy(str(object_name['rotationZ']))
    
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down'])
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['rotationY']))
    
    paste()
    pydirectinput.press(['enter'])
    
    time.sleep(0.2)
    pydirectinput.press('z')
    pydirectinput.press(['down'])
    pydirectinput.press('q')
    time.sleep(0.25)
    pydirectinput.press('enter')
    time.sleep(0.2)
    pydirectinput.press('0')
    get_Property()

def start_position(object_name, position_only):
    pydirectinput.PAUSE=0.012
    print(f"processing({object_name}) POSITION ONLY")
    sys.stdout.flush()
    pydirectinput.press(['down'],presses= 9)
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['positionX']))
    
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down']) 
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['positionY']))
    
    paste()
    pydirectinput.press(['enter']) 
    pydirectinput.press(['down'])
    pydirectinput.press(['enter']) 
    pyperclip.copy(str(object_name['positionZ']))
    
    paste()
    pydirectinput.press(['enter']) 

    time.sleep(0.2)
    pydirectinput.press('z')
    pydirectinput.press(['down'])
    pydirectinput.press('q')
    time.sleep(0.25)
    pydirectinput.press('enter')
    time.sleep(0.2)
    pydirectinput.press('0')
    get_Property()

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

