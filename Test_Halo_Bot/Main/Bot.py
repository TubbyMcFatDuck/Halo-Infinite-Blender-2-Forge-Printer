import json
import Keymolester
import sys
import time

Keymolester.focus_Halo()
time.sleep(0.5)

# Read the path to the JSON file from the command line
path = sys.argv[1]

key_count = 0
key_to_count = 'itemId'

position_only = True if sys.argv[3].lower() == 'true' else False
low_performance = True if sys.argv[4].lower() == 'true' else False  # Add this line to get the low_performance value


def process_execute(item_List, key_count, stop_flag, position_only, low_performance):
    key_count = Keymolester.process_objects(item_List, key_count, stop_flag, position_only=position_only, low_performance=low_performance)
    return

with open(path, "r") as f:
    response = f.read()
    response_json = json.loads(response)

item_List = response_json['itemList']
subkeys = item_List[0].keys()

print(("""MMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMWWMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWXK0kxO0XWMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWWMWXKOkxxkO0KKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXX0dc:,....';d0WMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMWKd:'.........';cdOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0O0Ol:cc:;,,'.....'ckXWMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWMWWKo'.................';okXWMMMMMMMMMMMMMMMMMMMMMMWXK0kxkkdc,,coc;:clc;;,,......;dKWMWMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMWWWXd,.......................,cxKNWWWMMMMMMWWWWWXKOxdoc::;:coxkxc,',;;,;::::;,'......'l0NWWWMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNk;.......................'',,,cxOOOOOkkkxxdddxdollc:;;;;;::oOK0ko:'..',,,;;;;;;,'....'l0NWWMMMMMMMMM
MMMMMMMMMMMMMMMMMWKl.........''''',,,;;:::;;;;;:;;;;;;::ccclllcccccldkxxdl;;;;;:lkXKkxdl;'.,;,',;ll:,''..'''l0WMMMMMMMMM
MMMMMMMMMMMWMMMMNx'...................''',''...''..''''''''''',;:cl:;,;coxoc;,,;;cdO0kxkkxl,'',,';loc,'''',,',oKWMMMMMMM
MMMMMMMMMMMWWWNO:....................''',,,''''''....'''',,,,'.',:cc;'',,:oxxl;,,;lxOkddxkkxl,'''',:;....''','.,oXWMMMMM
MMMMMMMMMMWWMXd'..........'''..........'''''...........',,,;;,..',;::;,,'',:oxxl;,;cdxdxxxdlclc,.................:0WWMMM
MMMMMMMMMMMWKc..............'..........''.............''.........'',;:;,'',;:coddoc:;;;:loollc;''..  .............:XWWMM
MMMMMMMMMWWk;...............''......''','''.........''..............',;;,,'''',;coddoc::;'',;;,'''................:XWWMM
MMMMMMMMMXo'................'''',,;;;;;;;;;;;;;;,'',,,................'',,,''..'''',;::cc:;'....,;,'........  ....oWMMMM
MMMMMMMMKc......,'..........;;,,;;,,,,;,,''.'',;;;::;'..................''................'''...';:c:;'....    ...kMMMMM
MMMMMMMK:....'...........',,,'..'',,,,;,,,,''.....';;;;,...........................................';:,....    ..;0MMMMM
MMMMMMNl........,;......''.....',,;;;;,'''',,,,''.....,;'..................................................    ..lNMMMMM
MMMMWNx.........;;..........',,;;:;,'..........'''''...................  ................................     . .kMMMMMM
MMMMM0,..................'',;;:;,'.......  ..........',,.................................................     . ,0MMMMMM
MMMMNo.................',,;::;,'.......'''..... ... ..''................................  . ..............      cXMMMMMM
MMMM0;...........'....,;;;;;,'....;lddxkOOOkxdoc'...............;;.................'.       ..............     .oWMMMMMM
MMMMk...........,,..';;;;;,,...,lkKXXXXXXKKKKKXX0x:'......'.....,c;.....          ...        .,,''........     .xMMMMMMM
MMMWo..........',..';;,;;,'..'d0XNNNNNNNNNNXX000KXXOl.  ...''....,c,...           ...  .  .  .;;::;,.. ...     .OMMMMMMM
MMMXc..........,'..;;,;;,'..,xKXNNWWWWWWWNNXXK0O0KKXKx,.....''....::....          .  ..........''','.. ...  .  ,0MMMMMMM
MMMK;.........',..,;,;;;,'.,xKXXNWMMMMMMWWNXXXKO0KK0KKx,.....''...'c;...........     .....  ...........        ;KMMMMMMM
MMMK;.........''.':;,;;;,..dKKXNWMMMMMMMWWNXXXKkOK0OkOKd. ....'....;:............    ...     ..........     .. ,0MMMMMMM
MMMK;............,:;,;;,'.,kKKXNWWMMMMMWWNNXXX0xOK0kxx00:  ...'....',...          .   .      .........  ..  .. .kMMMMMMM
MMMK;.......  ...,c;;;,,..c0KKXNNWWWMMWWNNXXXKkx00OkxxOKo.   .'..  ...        ..  ..  .      ....  ... ...     .oWMMMMMM
MMMX:....... ....,:;;;,,..cKK0KXNNNNNNNNNXXX0kkO00kxddkKd.   .........         .  .   .    ...........  ..      cXMMMMMM
MMMNl......  ....':;,,''..,kXKO0KXNNNXXXXK0kkOKK0OkxdxOKo..  ..'........         ...  .   ............. ..      ,0MMMMMM
MMMWx....... ..'..:;''''...o0OkOOO00KK0OkkkkkOOOOkkxxk00:..  ....  ';...         ...  .   ............   .     ..kWMMMMM
MMMM0,......  .'..,;,'.....,dk0KKK0OxdxO0KKK0kxddxddxkOd'... .'....;;...          ..  .   .............        .,dNMMMMM
MMMMNl......  ..'..,,.......,xKKKXXOoclk00OkkxkkkkxkKKd,......'....:,..                   ..............       ..cKMMMMM
MMMMWO,......  .''..,'.......'o0KKK0dc:ldxxdooooodkK0o'...........;:...              .    .............        ..,OMMMMM
MMMMMNo......   .,'..'........':dO0Kkl::loollcldkOOd:.......''...'c,...             ..     ..... .   .         ..'dWMMMM
MMMMMWK;......   .'..'''.........;lxOkdccldxxxkkdc,........'.....::....             ..     ....      ...       .,;dXMMMM
MMMMMMWO,........ ...'''','''.......',:;;:cc:;,..........'''.....'........          ...    .....     ...       ..,:OMMMM
MMMMMMMWO,......    .....,,....    .'..............  ......'''.  .............      .....   .....     .         .',xWMMM
MMMMMMMMW0:.. ...   .......     .':xOc...''........  ...   .................     .  .... .     ...              .''oNMMM
MMMMMMMMWWXc.  ..  ...       .,okKNWXl...,,'.......   .        .........          ....         ...  .          ....lXMWW
MMMMMMMMMMMNd.   ...        .lKWMMWWXl...;;,'......   .           ......                                .     . ..'xWMMM
MMMMMMMMMMWMW0;. ..          .,cokOOkc..'::,'......                  ......                         ..          ..oXMMMM
MMMMMMMMMMWWMMXo...         .. ......,'.'cc;,......                      .....              .        ... ..    .;kNWWWMM
MMMMMMMMMWMMMMWWO;.          .  .....,'.'ll:;'......  .                     .....         ...          ..  ...;xXWWMMMMM
MMMMMMMMMMMMMMMMMXx,.            .....'.':;';;.....   ....                              ......        ......,dXWMMMMMMMM
MMMMMMMMMMMMMMMMWWMNx;.            ..............  .  .....             ...            .......      .. ...,oKWWMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMNk;..      ..  ........'cxx,  ............     .......          ........     .   ..;xKWMMWMMMMMMMMM
MMMMMMMMMMMMMMMMWWMWWMMNk:.  .  .........,lkXWMK;  ............ ...........       .........       .  .cONWMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMNOc.   .......:kXWMWMM0,.. ..............'''....       ...... .  .       .,o0WMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMW0o,.    . .cKWMWWMMk'....'................      ............  ...  .'ckXWMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWWWXkc'.     :KWMWMMx.....,,'.......          ....... .........',;:lkKWWMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMWMWWMWKkc'...'dNWMMWd.....''......       ......... ..;oOKKKKKKKXNWMMMMMMMMMMWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWX0KKXWMMMMWd.............. ........... ..:xKNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWd.....,,,'..... ..    ...';:ckXWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXxoc::cc:,''''',,:clodkOKXNWMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWNKK0O00KKXXNWMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
$$$$$$$$\      $$\      $$\               $$\      $$\         $$$$$$$$\      $$\    $$$$$$$\                   $$\       
\__$$  __|     $$ |     $$ |              $$$\    $$$ |        $$  _____|     $$ |   $$  __$$\                  $$ |      
   $$ $$\   $$\$$$$$$$\ $$$$$$$\ $$\   $$\$$$$\  $$$$ |$$$$$$$\$$ |  $$$$$$\$$$$$$\  $$ |  $$ $$\   $$\ $$$$$$$\$$ |  $$\ 
   $$ $$ |  $$ $$  __$$\$$  __$$\$$ |  $$ $$\$$\$$ $$ $$  _____$$$$$\\____$$\_$$  _| $$ |  $$ $$ |  $$ $$  _____$$ | $$  |
   $$ $$ |  $$ $$ |  $$ $$ |  $$ $$ |  $$ $$ \$$$  $$ $$ /     $$  __$$$$$$$ |$$ |   $$ |  $$ $$ |  $$ $$ /     $$$$$$  / 
   $$ $$ |  $$ $$ |  $$ $$ |  $$ $$ |  $$ $$ |\$  /$$ $$ |     $$ | $$  __$$ |$$ |$$\$$ |  $$ $$ |  $$ $$ |     $$  _$$<  
   $$ \$$$$$$  $$$$$$$  $$$$$$$  \$$$$$$$ $$ | \_/ $$ \$$$$$$$\$$ | \$$$$$$$ |\$$$$  $$$$$$$  \$$$$$$  \$$$$$$$\$$ | \$$\ 
   \__|\______/\_______/\_______/ \____$$ \__|     \__|\_______\__|  \_______| \____/\_______/ \______/ \_______\__|  \__|
                                 $$\   $$ |                                                                               
                                 \$$$$$$  |                                                                               
                                  \______/                                                                                
 ______  __  __  ______  __    __                                                                                 
/\  __ \/\ \/ / /\  __ \/\ "-./  \                                                                                
\ \ \/\ \ \  _"-\ \ \/\ \ \ \-./\ \                                                                               
 \ \_____\ \_\ \_\ \_____\ \_\ \ \_\                                                                              
  \/_____/\/_/\/_/\/_____/\/_/  \/_/                                                                                                                                                                                           
 __  __  ______  __      ______  ______ __  __  __   __  ______ __  __    __  ______  ______  ______  __    __    
/\ \_\ \/\  __ \/\ \    /\  __ \/\  ___/\ \/\ \/\ "-.\ \/\__  _/\ \/\ "-./  \/\  ___\/\  ___\/\  __ \/\ "-./  \   
\ \  __ \ \  __ \ \ \___\ \ \/\ \ \  __\ \ \_\ \ \ \-.  \/_/\ \\ \ \ \ \-./\ \ \  __\\ \ \___\ \ \/\ \ \ \-./\ \  
 \ \_\ \_\ \_\ \_\ \_____\ \_____\ \_\  \ \_____\ \_\\"\_\ \ \_\\ \_\ \_\ \ \_\ \_____\ \_____\ \_____\ \_\ \ \_\ 
  \/_/\/_/\/_/\/_/\/_____/\/_____/\/_/   \/_____/\/_/ \/_/  \/_/ \/_/\/_/  \/_/\/_____/\/_____/\/_____/\/_/  \/_/ 
                                                                                                                  
"""))


print(len(response_json.keys()))
print(response_json.keys())
print(subkeys)
print(f"The value of position_only is: {position_only}")
print(f"The value of low_performance is: {low_performance}")  # Add this line to print the value of low_performance

sys.stdout.flush()

for object_name in item_List:
    if key_to_count in object_name:
        key_count += 1

print(f"There are {key_count} objects in the JSON file.")
print('-' * 20)

stop_flag = False 

while key_count is not None and key_count > 0:
    key_count = process_execute(item_List, key_count, stop_flag, position_only, low_performance)


##TO DO##
## Learn how to index and iterate a dictonary
## 
##
##
##
##
