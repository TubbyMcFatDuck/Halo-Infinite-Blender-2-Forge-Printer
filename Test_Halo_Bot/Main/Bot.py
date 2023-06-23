import json
import Keymolester
import sys

# Read the path to the JSON file from the command line
path = sys.argv[1]

key_count = 0
key_to_count = 'itemId'

def process_execute(item_List, key_count):
    key_count = Keymolester.process_objects(item_List, key_count)
    return
    #print('ID', objectName['itemId'])
    #print('ID', objectName['objectName'])
    #print('X', objectName['positionX'])
    #print('Y', objectName['positionY'])
    #print('Z', objectName['positionZ'])
    #print('RX', objectName['rotationX'])
    #print('RY', objectName['rotationY'])
    #print('RZ', objectName['rotationZ'])

with open(path, "r") as f:
    response = f.read()
    response_json = json.loads(response)

item_List = response_json['itemList']
subkeys = item_List[0].keys()

print(len(response_json.keys()))

print(response_json.keys())

print(subkeys)


for object_name in item_List:
    if key_to_count in object_name:
        key_count += 1

print(f"There are {key_count} objects in the JSON file.")
print('-' * 20)
while key_count is not None and key_count > 0:
    key_count = process_execute(item_List, key_count)


##TO DO##
## Learn how to index and iterate a dictonary
## 
##
##
##
##
