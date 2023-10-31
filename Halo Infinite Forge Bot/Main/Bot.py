import json
import Keymanager
import sys
import mirvTranslator

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

# Bot.py Foreword
################################
# 
# At a high level, this script takes a giant command line string from GUI.py that contains all of the data needed for the "Lower
# Level Functions" (basically everything but GUI.py) to run without issue to user specifications. When you see sys.argv[N], we are 
# declaring the variable on the left equal to our Nth argument. This file mostly just sets up variables for things like your speed, 
# which collections you are printing, etc.
# 
################################

path = sys.argv[1] ## DOC - grabbing the path of the DCjson the user selected.

key_count = 0 
key_to_count = 'itemId'
objectList = []
listofLists = []

position_only = True if sys.argv[3].lower() == 'true' else False ## DOC - toggles whether to only print position and ignore rotation and scale.
low_performance = float(sys.argv[4]) ## DOC - we call this Low Perforance down here, but this is actually "Print Speed" on the UI. This value is, in seconds, the amount of time between keypresses. 0.012 seconds, and 0.024 seconds, and 0.030 seconds, are all just delays between keypresses to give your game more time to register and execute that keypress.
start_index = sys.argv[5] ## DOC - grabbing which index to start iterating from
stop_me = sys.argv[6] ## DOC - only matters if you load a DCjson over 500 objects, value comes back as 1, 2, and 3 in from left to right on the UI popup.
end_index = int(sys.argv[10]) ## DOC - grabbing which index to stop iteration
end_index_check = True if sys.argv[11].lower() == 'true' else False ## DOC - asking if end index should be enabled
save_interval = int(sys.argv[12]) ## DOC - grabbing your save interval value
save_interval_check = True if sys.argv[13].lower() == 'true' else False ## DOC - asking if save interval should be enabled

## DOC - vLog stand for "Verbose Log", if enabled prints out a considerably higher volume log output. Everywhere that you see "if vLog == True:", is a place where we push more info if vLog is enabled.
try:
    vLog = True if sys.argv[14].lower() == 'true' else False
except IndexError:
    vLog = False

## DOC - asking if Print By Collection (PBC) should be used
print_by_collection_check = True if sys.argv[15].lower() == 'true' else False

if vLog == True:
        print("vLOG: Bot.py: Trying to apply Start Index...")
        sys.stdout.flush()
try:
    start_index = int(start_index)
    if vLog == True:
        print("vLOG: Bot.py: Start Index: Successful.")
        sys.stdout.flush()
except ValueError:
    start_index = 0
    if vLog == True:
        print("vLOG: Bot.py: Start Index: Failed.")
        sys.stdout.flush()

if save_interval == 0:
    save_interval = 9999999

## DOC - Arguably one of the most important lines in the project, process_execute is the driver function that sends what we'll 
# call a "package" of objects to Keymanager for placement in-game. An important thing to note to provide context to why this whole 
# program is set up the way it is, is because in the early versions, *there was no PBC feature.* It was all bulk printing, your 
# entire DCjson would be printed in one big sprint or in packages that you define via the Start & End Index. But now, as you'll 
# see near the bottom of this file, EACH COLLECTION is individually added to a list of lists, and that nested list is iterated 
# through, and each collection is given its own process_execute command depending on if it is enabled or not.
def process_execute(item_List, path, stop_me, vLog, end_index, end_index_check, save_interval, save_interval_check, start_index, position_only, low_performance):
    if vLog == True:
        print("vLOG: Bot.py: process_execute called with objects from path: \n{}".format(str(path)))
        sys.stdout.flush()
    Keymanager.process_objects(item_List, path, stop_me, vLog, start_index=start_index, end_index=end_index, end_index_check=end_index_check, save_interval=save_interval, save_interval_check=save_interval_check, position_only=position_only, low_performance=low_performance)
    return

## DOC - retrieving the DCjson the user selected
with open(path, "r") as f:
    response = f.read()
    response_json = json.loads(response)

item_List = response_json['itemList']
subkeys = item_List[0].keys()

size = len(item_List)

## DOC - getting all of the unique collections names from the DCjson
for x in range(size):
    if (str({item_List[x]['collection']}).replace("'", "").replace("{","").replace("}","")) not in objectList:
        objectList.append(str({item_List[x]['collection']}).replace("'", "").replace("{","").replace("}",""))
#print(objectList)

## DOC - creating a list of lists of all of the different collections
for x in range(len(objectList)):
    collection = []
    for y in range(len(item_List)):
        if str({item_List[y]['collection']}).replace("'", "").replace("{","").replace("}","") == objectList[x]:
            collection.append(item_List[y])
    listofLists.append(collection)

if vLog == True:
    print("vLOG: Bot.py: Printing metadata:")
    print(len(response_json.keys()))
    print(response_json.keys())
    print(subkeys)
    print("vLOG: Bot.py: End metadata print.")
    sys.stdout.flush()

print("BOT CODE VERSION: v1.0.2") 

sys.stdout.flush()

for object_name in item_List:
    if key_to_count in object_name:
        key_count += 1

print(f"There are {key_count} objects in the JSON file.")
print('-' * 20)

stop_flag = False 

if position_only == False:
        mirvTranslator.setRotationAxis(low_performance, vLog)
## DOC - this is what spawns the GRD Spartan Doll. We spawn him in to force your movement widget to rotation so we can just 
# press 0 later on new objects and reset their rotation to (0,0,0).
if vLog == True:
    print("vLOG: Bot.py: Calling process_execute!")
    sys.stdout.flush()
## DOC - basically, grab each collection, if it was sent to enabled, print it, if not, skip it. Otherwise, just do a full 
# bulk print with every object.
if print_by_collection_check == True:
    for x in range(len(listofLists)):
        if sys.argv[x+16].lower() == 'true':
            print("\nPRINTING COLLECTION: {}\n".format(objectList[x]))
            process_execute(listofLists[x], path, stop_me, vLog, end_index, end_index_check, save_interval, save_interval_check, start_index, position_only, low_performance)
        else:
            print("\nSKIPPING COLLECTION: {}\n".format(objectList[x]))
    print("This print has concluded.")
else: 
    process_execute(item_List, path, stop_me, vLog, end_index, end_index_check, save_interval, save_interval_check, start_index, position_only, low_performance)