import json
import Keymanager
import sys
import mirvTranslator

path = sys.argv[1]

key_count = 0
key_to_count = 'itemId'
objectList = []
listofLists = []

position_only = True if sys.argv[3].lower() == 'true' else False
low_performance = float(sys.argv[4])
start_index = sys.argv[5]
stop_me = sys.argv[6]
end_index = int(sys.argv[10])
end_index_check = True if sys.argv[11].lower() == 'true' else False
save_interval = int(sys.argv[12])
save_interval_check = True if sys.argv[13].lower() == 'true' else False

try:    
    vLog = True if sys.argv[14].lower() == 'true' else False
except IndexError:
    vLog = False

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
        print("vLOG: Bot.py: StartIndex: Failed.")
        sys.stdout.flush()

def process_execute(item_List, path, stop_me, vLog, end_index, end_index_check, save_interval, save_interval_check, start_index, position_only, low_performance):
    if vLog == True:
        print("vLOG: Bot.py: process_execute called with objects from path: \n{}".format(str(path)))
        sys.stdout.flush()
    Keymanager.process_objects(item_List, path, stop_me, vLog, start_index=start_index, end_index=end_index, end_index_check=end_index_check, save_interval=save_interval, save_interval_check=save_interval_check, position_only=position_only, low_performance=low_performance)
    return

with open(path, "r") as f:
    response = f.read()
    response_json = json.loads(response)

item_List = response_json['itemList']
subkeys = item_List[0].keys()

size = len(item_List)

for x in range(size):
    if (str({item_List[x]['collection']}).replace("'", "").replace("{","").replace("}","")) not in objectList:
        objectList.append(str({item_List[x]['collection']}).replace("'", "").replace("{","").replace("}",""))
print(objectList)

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

print("CODE VERSION: v0.9.3") 

sys.stdout.flush()

for object_name in item_List:
    if key_to_count in object_name:
        key_count += 1

print(f"There are {key_count} objects in the JSON file.")
print('-' * 20)

stop_flag = False 

if position_only == False:
        mirvTranslator.setRotationAxis(low_performance, vLog)
if vLog == True:
    print("vLOG: Bot.py: Calling process_execute!")
    sys.stdout.flush()
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