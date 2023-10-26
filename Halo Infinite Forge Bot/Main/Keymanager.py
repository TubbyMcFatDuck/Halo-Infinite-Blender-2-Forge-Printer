import pyautogui
import time
import pydirectinput
import sys
import pyperclip
import Sorter
import mirvTranslator
import keyboard


##### Execution of Object Processing Functions Start

key_count = 0
key_to_count = 'itemId'
start_index = 0
def process_objects(item_list, path, stop_me, vLog, start_index, end_index, end_index_check, save_interval, save_interval_check, position_only=None, low_performance=None):
    low_performance = low_performance
    ticker = 0
    Sorter.resetSorter()
    sorted_item_list = Sorter.initSorter(item_list, start_index, vLog)
    print("Starting at index: {}".format(ticker + start_index))
    if vLog == True:
        print("vLOG: Keymanager.py: Start Index: {}".format(start_index))
        print("vLOG: Keymanager.py: End Index: {}".format(end_index))
        print("vLOG: Keymanager.py: End Index Check: {}".format(end_index_check))
        print("vLOG: Keymanager.py: Save Interval: {}".format(save_interval))
        print("vLOG: Keymanager.py: Save Interval Check: {}".format(save_interval_check))
        print("vLOG: Keymanager.py: Position Only: {}".format(position_only))
        print("vLOG: Keymanager.py: Low Performance: {}".format(low_performance))
    listLength = len(sorted_item_list)
    while ticker < len(sorted_item_list):
        if vLog == True:
            print("vLOG: Keymanager.py: Entering process_objects loop.")
            sys.stdout.flush()
        while True:
            if vLog == True:
                print("vLOG: Keymanager.py: Emergency stopkey inside process_objects loop activated.")
                sys.stdout.flush()
            if keyboard.is_pressed("f"):
                print("EMERGENCY STOPKEY PRESSED -- TERMINATING BOT PROCESS")
                sys.exit(0)
            object = sorted_item_list[ticker]
            print("Processing objects: {} with itemIds: {}".format(object['objectName'], object['itemId']))
            # Recent 0
            # Prefabs 1
            # Accent 2
            ## Antennas 1
            ## Antennas MP 2
            ## Arena 3
            if str({object['itemId']}).find("-1546771230") == True:
                #Arena Corner Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ARENA_CORNER_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 3, 2)
                ticker += Sorter.obj_ARENA_CORNER_COVER

            elif str({object['itemId']}).find("-2028031834") == True:
                #Arena Cover A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ARENA_COVER_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 3, 3)
                ticker += Sorter.obj_ARENA_COVER_A

            elif str({object['itemId']}).find("-614479068") == True:
                #Arena Octagon Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ARENA_OCTAGON_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 3, 4)
                ticker += Sorter.obj_ARENA_OCTAGON_COVER
            ## Banished 4
            ## Banished MP 5 
            ## Barrels 6
            ## Barrels MP 7
            ## Bazaar 8
            elif str({object['itemId']}).find("622020449") == True:
                #Dirty Bucket
                mirvTranslator.objTranslationStartsDynamicAndFixed(sorted_item_list[ticker:Sorter.obj_DIRTY_BUCKET+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 8, 1)
                ticker += Sorter.obj_DIRTY_BUCKET

            elif str({object['itemId']}).find("-1647107999") == True:
                #Tire Bald
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIRE_BALD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 8, 2)
                ticker += Sorter.obj_TIRE_BALD
            ## Bazaar MP 9
            ## Bodies 10
            ## City Props 11
            ## City Props MP 12
            ## Cover 13
            elif str({object['itemId']}).find("1622837419") == True:
                #Concrete Barrier Long
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CONCRETE_BARRIER_LONG+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 0)
                ticker += Sorter.obj_CONCRETE_BARRIER_LONG

            elif str({object['itemId']}).find("-1705963242") == True:
                #Concrete Barrier Short
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CONCRETE_BARRIER_SHORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 1)
                ticker += Sorter.obj_CONCRETE_BARRIER_SHORT

            elif str({object['itemId']}).find("-1966393110") == True:
                #Curved Half Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_HALF_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 2)
                ticker += Sorter.obj_CURVED_HALF_COVER

            elif str({object['itemId']}).find("892365399") == True:
                #Gabion Rock Filled Tall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GABION_ROCK_FILLED_TALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 3)
                ticker += Sorter.obj_GABION_ROCK_FILLED_TALL

            elif str({object['itemId']}).find("2119077803") == True:
                #Gabion Sand Filled
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GABION_SAND_FILLED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 4)
                ticker += Sorter.obj_GABION_SAND_FILLED

            elif str({object['itemId']}).find("-599379455") == True:
                #Gabion Sand Filled Large
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GABION_SAND_FILLED_LARGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 5)
                ticker += Sorter.obj_GABION_SAND_FILLED_LARGE

            elif str({object['itemId']}).find("-379997344") == True:
                #Gabion Sand Filled Tall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GABION_SAND_FILLED_TALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 6)
                ticker += Sorter.obj_GABION_SAND_FILLED_TALL

            elif str({object['itemId']}).find("443142438") == True:
                #Plated Half Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PLATED_HALF_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 7)
                ticker += Sorter.obj_PLATED_HALF_COVER

            elif str({object['itemId']}).find("-1479214964") == True:
                #Steel Concrete Barrier Long
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_STEEL_CONCRETE_BARRIER_LONG+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 8)
                ticker += Sorter.obj_STEEL_CONCRETE_BARRIER_LONG

            elif str({object['itemId']}).find("-29809561") == True:
                #Steel Concrete Barrier Short
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_STEEL_CONCRETE_BARRIER_SHORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 9)
                ticker += Sorter.obj_STEEL_CONCRETE_BARRIER_SHORT

            elif str({object['itemId']}).find("-959850993") == True:
                #UNSC Deployable Cover Large
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_DEPLOYABLE_COVER_LARGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 10)
                ticker += Sorter.obj_UNSC_DEPLOYABLE_COVER_LARGE

            elif str({object['itemId']}).find("1346005877") == True:
                #UNSC Deployable Cover Small
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_DEPLOYABLE_COVER_SMALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 11, 11)
                ticker += Sorter.obj_UNSC_DEPLOYABLE_COVER_SMALL
            ## Cover MP 14
            ## Crates 15
            ## Crates MP 16
            ## Destructibles 17
            elif str({object['itemId']}).find("-1482624315") == True:
                #Plastic Crate Empty
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PLASTIC_CRATE_EMPTY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 15, 31)
                ticker += Sorter.obj_PLASTIC_CRATE_EMPTY
            
            elif str({object['itemId']}).find("792418577") == True:
                #Soda Crate Empty
                mirvTranslator.objTranslationStartsDynamicAndFixed(sorted_item_list[ticker:Sorter.obj_SODA_CRATE_EMPTY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 17, 35)
                ticker += Sorter.obj_SODA_CRATE_EMPTY
            ## Destructibles MP 18
            ## Ducts 19
            ## Fences 20
            ## Fences MP 21
            ## Forerunner 22
            elif str({object['itemId']}).find("-1445440002") == True:
                #Forerunner 24x60x24 Angled Support
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_24_X_60_X_24_ANGLED_SUPPORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 0)
                ticker += Sorter.obj_FORERUNNER_24_X_60_X_24_ANGLED_SUPPORT

            elif str({object['itemId']}).find("1075788544") == True:
                #Forerunner 8x36x32 Angled Support
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_8_X_36_X_32_ANGLED_SUPPORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 1)
                ticker += Sorter.obj_FORERUNNER_8_X_36_X_32_ANGLED_SUPPORT

            elif str({object['itemId']}).find("-2005024110") == True:
                #Forerunner Angled Cover Support
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_ANGLED_COVER_SUPPORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 2)
                ticker += Sorter.obj_FORERUNNER_ANGLED_COVER_SUPPORT

            elif str({object['itemId']}).find("-1045090467") == True:
                #Forerunner Beam A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 3)
                ticker += Sorter.obj_FORERUNNER_BEAM_A

            elif str({object['itemId']}).find("-799173690") == True:
                #Forerunner Beam B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 4)
                ticker += Sorter.obj_FORERUNNER_BEAM_B

            elif str({object['itemId']}).find("-952468892") == True:
                #Forerunner Behemoth Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEHEMOTH_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 5)
                ticker += Sorter.obj_FORERUNNER_BEHEMOTH_DOOR

            elif str({object['itemId']}).find("-1422001974") == True:
                #Forerunner Behemoth Hatch w/ Material Swap
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEHEMOTH_HATCH_W_MATERIAL_SWAP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 6)
                ticker += Sorter.obj_FORERUNNER_BEHEMOTH_HATCH_W_MATERIAL_SWAP

            elif str({object['itemId']}).find("1668509646") == True:
                #Forerunner Catwalk Beam
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_BEAM+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 7)
                ticker += Sorter.obj_FORERUNNER_CATWALK_BEAM

            elif str({object['itemId']}).find("896710904") == True:
                #Forerunner Catwalk Left A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 8)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_A

            elif str({object['itemId']}).find("-2030814116") == True:
                #Forerunner Catwalk Left B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 9)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_B

            elif str({object['itemId']}).find("-2064649151") == True:
                #Forerunner Catwalk Left C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 10)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_C

            elif str({object['itemId']}).find("-168835536") == True:
                #Forerunner Catwalk Left D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 11)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_D

            elif str({object['itemId']}).find("-1913952371") == True:
                #Forerunner Catwalk Left E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 12)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_E

            elif str({object['itemId']}).find("2125606605") == True:
                #Forerunner Catwalk Railing
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RAILING+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 13)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RAILING

            elif str({object['itemId']}).find("298221350") == True:
                #Forerunner Catwalk Right A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 14)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_A

            elif str({object['itemId']}).find("-72221914") == True:
                #Forerunner Catwalk Right B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 15)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_B

            elif str({object['itemId']}).find("-325594173") == True:
                #Forerunner Catwalk Right C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 16)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_C
            
            elif str({object['itemId']}).find("315322878") == True:
                #Forerunner Catwalk Right D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 17)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_D

            elif str({object['itemId']}).find("378350250") == True:
                #Forerunner Catwalk Right E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 18)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_E

            elif str({object['itemId']}).find("-754711308") == True:
                #Forerunner Control Point
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CONTROL_POINT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 19)
                ticker += Sorter.obj_FORERUNNER_CONTROL_POINT
                
            elif str({object['itemId']}).find("949417702") == True:
                #Forerunner Cover Block
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_BLOCK+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 20)
                ticker += Sorter.obj_FORERUNNER_COVER_BLOCK

            elif str({object['itemId']}).find("-1979502216") == True:
                #Forerunner Cover Full A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_FULL_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 21)
                ticker += Sorter.obj_FORERUNNER_COVER_FULL_A

            elif str({object['itemId']}).find("-1197972784") == True:
                #Forerunner Cover Full B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_FULL_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 22)
                ticker += Sorter.obj_FORERUNNER_COVER_FULL_B

            elif str({object['itemId']}).find("749094963") == True:
                #Forerunner Cover Full C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_FULL_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 23)
                ticker += Sorter.obj_FORERUNNER_COVER_FULL_C
                
            elif str({object['itemId']}).find("871087208") == True:
                #Forerunner Cover Full D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_FULL_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 24)
                ticker += Sorter.obj_FORERUNNER_COVER_FULL_D
            
            elif str({object['itemId']}).find("1912291805") == True:
                #Forerunner Cover Half A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_HALF_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 25)
                ticker += Sorter.obj_FORERUNNER_COVER_HALF_A

            elif str({object['itemId']}).find("736764419") == True:
                #Forerunner Cover Half Left B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_HALF_LEFT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 26)
                ticker += Sorter.obj_FORERUNNER_COVER_HALF_LEFT_B
            
            elif str({object['itemId']}).find("-987659891") == True:
                #Forerunner Cover Half Right B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_HALF_RIGHT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 27)
                ticker += Sorter.obj_FORERUNNER_COVER_HALF_RIGHT_B

            elif str({object['itemId']}).find("-960803919") == True:
                #Forerunner Decorative Pylon
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_DECORATIVE_PYLON+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 28)
                ticker += Sorter.obj_FORERUNNER_DECORATIVE_PYLON

            elif str({object['itemId']}).find("-204435982") == True:
                #Forerunner Door Small
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_DOOR_SMALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 29)
                ticker += Sorter.obj_FORERUNNER_DOOR_SMALL

            elif str({object['itemId']}).find("-67333374") == True:
                #Forerunner Door Small Animated
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_DOOR_SMALL_ANIMATED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 30)
                ticker += Sorter.obj_FORERUNNER_DOOR_SMALL_ANIMATED

            elif str({object['itemId']}).find("-834091054") == True:
                #Forerunner Hex Pillar 128x384
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_128_X_384+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 31)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_128_X_384

            elif str({object['itemId']}).find("79128260") == True:
                #Forerunner Hex Pillar 16x08
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_08+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 32)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_08

            elif str({object['itemId']}).find("-1538223866") == True:
                #Forerunner Hex Pillar 16x24
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_24+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 33)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_24

            elif str({object['itemId']}).find("1768944999") == True:
                #Forerunner Hex Pillar 16x384
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_384+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 34)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_384

            elif str({object['itemId']}).find("-1632544064") == True:
                #Forerunner Hex Pillar 16x48
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_48+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 35)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_48

            elif str({object['itemId']}).find("-638078883") == True:
                #Forerunner Hex Pillar 32x96
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_32_X_96+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 36)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_32_X_96

            elif str({object['itemId']}).find("-1362288785") == True:
                #Forerunner Hex Pillar 64x120
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_120+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 37)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_120

            elif str({object['itemId']}).find("1192970141") == True:
                #Forerunner Hex Pillar 64x168 A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 38)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_A

            elif str({object['itemId']}).find("981739802") == True:
                #Forerunner Hex Pillar 64x168 B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 39)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_B

            elif str({object['itemId']}).find("1233058388") == True:
                #Forerunner Hex Pillar 64x168 C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 40)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_C

            elif str({object['itemId']}).find("1993902058") == True:
                #Forerunner Hex Pillar 64x168 D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 41)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_D

            elif str({object['itemId']}).find("1164792644") == True:
                #Forerunner Hex Pillar 64x168 E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 42)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_E

            elif str({object['itemId']}).find("-263887254") == True:
                #Forerunner Hex Pillar 64x168 F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 43)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_F

            elif str({object['itemId']}).find("-1038479746") == True:
                #Forerunner Hex Pillar 64x168 G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 44)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_G

            elif str({object['itemId']}).find("1057087770") == True:
                #Forerunner Hex Pillar 64x168 H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 45)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_H

            elif str({object['itemId']}).find("1013202573") == True:
                #Forerunner Hex Pillar 64x168 I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 46)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_I

            elif str({object['itemId']}).find("-467276164") == True:
                #Forerunner Hex Pillar 64x168 J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 47)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_J

            elif str({object['itemId']}).find("-1734475997") == True:
                #Forerunner Hex Pillar 64x168 K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 48)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_K

            elif str({object['itemId']}).find("-871470067") == True:
                #Forerunner Hub Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HUB_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 49)
                ticker += Sorter.obj_FORERUNNER_HUB_COVER

            elif str({object['itemId']}).find("-1461734734") == True:
                #Forerunner Light Bridge Emitter
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_BRIDGE_EMITTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 50)
                ticker += Sorter.obj_FORERUNNER_LIGHT_BRIDGE_EMITTER

            elif str({object['itemId']}).find("776640986") == True:
                #Forerunner Machinery Cover A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_MACHINERY_COVER_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 51)
                ticker += Sorter.obj_FORERUNNER_MACHINERY_COVER_A

            elif str({object['itemId']}).find("1873654711") == True:
                #Forerunner Machinery Cover B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_MACHINERY_COVER_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 52)
                ticker += Sorter.obj_FORERUNNER_MACHINERY_COVER_B

            elif str({object['itemId']}).find("-899443081") == True:
                #Forerunner Pedestal
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PEDESTAL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 53)
                ticker += Sorter.obj_FORERUNNER_PEDESTAL

            elif str({object['itemId']}).find("-1294066737") == True:
                #Forerunner Pillar A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PILLAR_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 54)
                ticker += Sorter.obj_FORERUNNER_PILLAR_A

            elif str({object['itemId']}).find("536142106") == True:
                #Forerunner Pillar B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PILLAR_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 55)
                ticker += Sorter.obj_FORERUNNER_PILLAR_B

            elif str({object['itemId']}).find("-1160144719") == True:
                #Forerunner Pillar C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PILLAR_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 56)
                ticker += Sorter.obj_FORERUNNER_PILLAR_C

            elif str({object['itemId']}).find("1868092241") == True:
                #Forerunner Piston
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PISTON+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 57)
                ticker += Sorter.obj_FORERUNNER_PISTON
            
            elif str({object['itemId']}).find("-1429124637") == True:
                #Forerunner Platform 06x10x44 Left
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_LEFT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 58)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_LEFT

            elif str({object['itemId']}).find("711896173") == True:
                #Forerunner Platform 06x10x44 Right
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_RIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 59)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_RIGHT

            elif str({object['itemId']}).find("-924850999") == True:
                #Forerunner Platform 10x06x48 Left
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_LEFT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 60)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_LEFT

            elif str({object['itemId']}).find("1064872076") == True:
                #Forerunner Platform 10x06x48 Right
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_RIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 61)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_RIGHT

            elif str({object['itemId']}).find("1472515488") == True:
                #Forerunner Platform 12x04x56
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_04_X_56+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 62)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_04_X_56

            elif str({object['itemId']}).find("-2145450599") == True:
                #Forerunner Platform 12x10x42 Left A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 63)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_A

            elif str({object['itemId']}).find("2146232744") == True:
                #Forerunner Platform 12x10x42 Left B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 64)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_B

            elif str({object['itemId']}).find("436904182") == True:
                #Forerunner Platform 12x10x42 Right A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 65)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_A
            
            elif str({object['itemId']}).find("326965901") == True:
                #Forerunner Platform 12x10x42 Right B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 66)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_B

            elif str({object['itemId']}).find("445225109") == True:
                #Forerunner Platform 16x08x42
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_16_X_08_X_42+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 67)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_16_X_08_X_42

            elif str({object['itemId']}).find("2050656726") == True:
                #Forerunner Platform 16x08x42 Left A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 68)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_A

            elif str({object['itemId']}).find("-1353587005") == True:
                #Forerunner Platform 16x08x42 Left B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 69)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_B

            elif str({object['itemId']}).find("1194765758") == True:
                #Forerunner Platform 16x08x42 Right A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 70)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_A

            elif str({object['itemId']}).find("-1912169757") == True:
                #Forerunner Platform 16x08x42 Right B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 71)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_B

            elif str({object['itemId']}).find("1358501723") == True:
                #Forerunner Plinth
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLINTH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 72)
                ticker += Sorter.obj_FORERUNNER_PLINTH

            elif str({object['itemId']}).find("1572738626") == True:
                #Forerunner Podium Large A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PODIUM_LARGE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 73)
                ticker += Sorter.obj_FORERUNNER_PODIUM_LARGE_A

            elif str({object['itemId']}).find("1244902926") == True:
                #Forerunner Podium Large B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PODIUM_LARGE_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 74)
                ticker += Sorter.obj_FORERUNNER_PODIUM_LARGE_B

            elif str({object['itemId']}).find("-26953699") == True:
                #Forerunner Ramp
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RAMP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 75)
                ticker += Sorter.obj_FORERUNNER_RAMP

            elif str({object['itemId']}).find("592283351") == True:
                #Forerunner Ramp Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RAMP_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 76)
                ticker += Sorter.obj_FORERUNNER_RAMP_COVER

            elif str({object['itemId']}).find("-1058146113") == True:
                #Forerunner Support A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 77)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_A

            elif str({object['itemId']}).find("830462689") == True:
                #Forerunner Support B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 78)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_B

            elif str({object['itemId']}).find("260764033") == True:
                #Forerunner Support C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 79)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_C

            elif str({object['itemId']}).find("-925343768") == True:
                #Forerunner Support D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 80)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_D
            
            elif str({object['itemId']}).find("1460146008") == True:
                #Forerunner Totem Ring A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 81)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_A

            elif str({object['itemId']}).find("-25855440") == True:
                #Forerunner Totem Ring B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 82)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_B

            elif str({object['itemId']}).find("-2079373050") == True:
                #Forerunner Totem Ring C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 83)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_C

            elif str({object['itemId']}).find("626024360") == True:
                #Forerunner Totem Ring Chunk
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_CHUNK+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 84)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_CHUNK

            elif str({object['itemId']}).find("-1244774912") == True:
                #Forerunner Totem Ring Debris
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_DEBRIS+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 20, 85)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_DEBRIS
            ## Forerunner MP 23
            elif str({object['itemId']}).find("1647775476") == True:
                #Forerunner Beam A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 0)
                ticker += Sorter.obj_FORERUNNER_BEAM_A_MP

            elif str({object['itemId']}).find("88131037") == True:
                #Forerunner Beam B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 1)
                ticker += Sorter.obj_FORERUNNER_BEAM_B_MP

            elif str({object['itemId']}).find("-1213571076") == True:
                #Forerunner Behemoth Door MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEHEMOTH_DOOR_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 2)
                ticker += Sorter.obj_FORERUNNER_BEHEMOTH_DOOR_MP

            elif str({object['itemId']}).find("-1922196237") == True:
                #Forerunner Behemoth Hatch MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEHEMOTH_HATCH_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 3)
                ticker += Sorter.obj_FORERUNNER_BEHEMOTH_HATCH_MP

            elif str({object['itemId']}).find("919352820") == True:
                #Forerunner Catwalk Beam MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_BEAM_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 4)
                ticker += Sorter.obj_FORERUNNER_CATWALK_BEAM_MP

            elif str({object['itemId']}).find("-186672519") == True:
                #Forerunner Catwalk Left A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 5)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_A_MP

            elif str({object['itemId']}).find("-106437375") == True:
                #Forerunner Catwalk Left B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 6)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_B_MP

            elif str({object['itemId']}).find("130181798") == True:
                #Forerunner Catwalk Left C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 7)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_C_MP

            elif str({object['itemId']}).find("-660809723") == True:
                #Forerunner Catwalk Left D MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_D_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 8)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_D_MP

            elif str({object['itemId']}).find("1353884373") == True:
                #Forerunner Catwalk Left E MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_LEFT_E_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 9)
                ticker += Sorter.obj_FORERUNNER_CATWALK_LEFT_E_MP

            elif str({object['itemId']}).find("-120745116") == True:
                #Forerunner Railing MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RAILING_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 10)
                ticker += Sorter.obj_FORERUNNER_RAILING_MP

            elif str({object['itemId']}).find("929183006") == True:
                #Forerunner Catwalk Right A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 11)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_A_MP

            elif str({object['itemId']}).find("-1735909100") == True:
                #Forerunner Catwalk Right B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 12)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_B_MP

            elif str({object['itemId']}).find("-1455973470") == True:
                #Forerunner Catwalk Right C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 13)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_C_MP

            elif str({object['itemId']}).find("-2009318721") == True:
                #Forerunner Catwalk Right D MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_D_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 14)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_D_MP

            elif str({object['itemId']}).find("2089725512") == True:
                #Forerunner Catwalk Right E MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CATWALK_RIGHT_E_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 15)
                ticker += Sorter.obj_FORERUNNER_CATWALK_RIGHT_E_MP

            elif str({object['itemId']}).find("2038528974") == True:
                #Forerunner Cover Block MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_COVER_BLOCK_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 16)
                ticker += Sorter.obj_FORERUNNER_COVER_BLOCK_MP

            elif str({object['itemId']}).find("-233248761") == True:
                #Forerunner Full A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FULL_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 17)
                ticker += Sorter.obj_FORERUNNER_FULL_A_MP

            elif str({object['itemId']}).find("1276575246") == True:
                #Forerunner Full B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FULL_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 18)
                ticker += Sorter.obj_FORERUNNER_FULL_B_MP

            elif str({object['itemId']}).find("-586431020") == True:
                #Forerunner Full C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FULL_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 19)
                ticker += Sorter.obj_FORERUNNER_FULL_C_MP

            elif str({object['itemId']}).find("-692162926") == True:
                #Forerunner Full D MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FULL_D_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 20)
                ticker += Sorter.obj_FORERUNNER_FULL_D_MP

            elif str({object['itemId']}).find("546965436") == True:
                #Forerunner Half A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HALF_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 21)
                ticker += Sorter.obj_FORERUNNER_HALF_A_MP

            elif str({object['itemId']}).find("1119812098") == True:
                #Forerunner Half Left B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HALF_LEFT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 22)
                ticker += Sorter.obj_FORERUNNER_HALF_LEFT_B_MP

            elif str({object['itemId']}).find("822856101") == True:
                #Forerunner Half Right B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HALF_RIGHT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 23)
                ticker += Sorter.obj_FORERUNNER_HALF_RIGHT_B_MP

            elif str({object['itemId']}).find("731035848") == True:
                #Forerunner Door Small MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_DOOR_SMALL_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 24)
                ticker += Sorter.obj_FORERUNNER_DOOR_SMALL_MP

            elif str({object['itemId']}).find("-1678465842") == True:
                #Forerunner Hex Pillar 128x384 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_128_X_384_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 25)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_128_X_384_MP

            elif str({object['itemId']}).find("1202613303") == True:
                #Forerunner Hex Pillar 16x08 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_08_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 26)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_08_MP

            elif str({object['itemId']}).find("-1714897318") == True:
                #Forerunner Hex Pillar 16x24 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_24_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 27)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_24_MP

            elif str({object['itemId']}).find("-860937874") == True:
                #Forerunner Hex Pillar 16x384 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_384_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 28)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_384_MP

            elif str({object['itemId']}).find("-169309065") == True:
                #Forerunner Hex Pillar 16x48 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_48_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 29)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_16_X_48_MP

            elif str({object['itemId']}).find("1653755539") == True:
                #Forerunner Hex Pillar 32x96 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_32_X_96_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 30)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_32_X_96_MP

            elif str({object['itemId']}).find("1107103856") == True:
                #Forerunner Hex Pillar 64x120 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_120_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 31)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_120_MP

            elif str({object['itemId']}).find("-465209448") == True:
                #Forerunner Hex Pillar 64x168 A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 32)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_A_MP

            elif str({object['itemId']}).find("1636200601") == True:
                #Forerunner Hex Pillar 64x168 B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 33)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_B_MP

            elif str({object['itemId']}).find("-1933628756") == True:
                #Forerunner Hex Pillar 64x168 C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 34)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_C_MP

            elif str({object['itemId']}).find("1629359986") == True:
                #Forerunner Hex Pillar 64x168 D MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_D_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 35)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_D_MP

            elif str({object['itemId']}).find("1508523010") == True:
                #Forerunner Hex Pillar 64x168 E MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_E_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 36)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_E_MP

            elif str({object['itemId']}).find("-1532440566") == True:
                #Forerunner Hex Pillar 64x168 F MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_F_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 37)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_F_MP

            elif str({object['itemId']}).find("1012794313") == True:
                #Forerunner Hex Pillar 64x168 G MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_G_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 38)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_G_MP

            elif str({object['itemId']}).find("1073851953") == True:
                #Forerunner Hex Pillar 64x168 H MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_H_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 39)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_H_MP

            elif str({object['itemId']}).find("633436311") == True:
                #Forerunner Hex Pillar 64x168 I MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_I_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 40)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_I_MP

            elif str({object['itemId']}).find("-2144639762") == True:
                #Forerunner Hex Pillar 64x168 J MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_J_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 41)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_J_MP

            elif str({object['itemId']}).find("966084704") == True:
                #Forerunner Hex Pillar 64x168 K MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_K_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 42)
                ticker += Sorter.obj_FORERUNNER_HEX_PILLAR_64_X_168_K_MP

            elif str({object['itemId']}).find("-972592705") == True:
                #Forerunner Light Bridge Emitter MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_BRIDGE_EMITTER_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 43)
                ticker += Sorter.obj_FORERUNNER_LIGHT_BRIDGE_EMITTER_MP

            elif str({object['itemId']}).find("-189526008") == True:
                #Forerunner Pillar A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PILLAR_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 44)
                ticker += Sorter.obj_FORERUNNER_PILLAR_A_MP

            elif str({object['itemId']}).find("-599136376") == True:
                #Forerunner Pillar B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PILLAR_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 45)
                ticker += Sorter.obj_FORERUNNER_PILLAR_B_MP

            elif str({object['itemId']}).find("1445072349") == True:
                #Forerunner Pillar C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PILLAR_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 46)
                ticker += Sorter.obj_FORERUNNER_PILLAR_C_MP

            elif str({object['itemId']}).find("-529749711") == True:
                #Forerunner Piston MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PISTON_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 47)
                ticker += Sorter.obj_FORERUNNER_PISTON_MP

            elif str({object['itemId']}).find("1784897098") == True:
                #Forerunner Platform 06x10x44 Left MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_LEFT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 48)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_LEFT_MP

            elif str({object['itemId']}).find("-1423496106") == True:
                #Forerunner Platform 06x10x44 Right MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_RIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 49)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_06_X_10_X_44_RIGHT_MP
            
            elif str({object['itemId']}).find("-1666662463") == True:
                #Forerunner Platform 10x06x48 Left MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_LEFT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 50)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_LEFT_MP

            elif str({object['itemId']}).find("-1844231743") == True:
                #Forerunner Platform 10x06x48 Right MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_RIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 51)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_10_X_06_X_48_RIGHT_MP

            elif str({object['itemId']}).find("-1952778786") == True:
                #Forerunner Platform 12x04x56 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_04_X_56_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 52)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_04_X_56_MP

            elif str({object['itemId']}).find("-1391783956") == True:
                #Forerunner Platform 12x10x42 Left A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 53)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_A_MP

            elif str({object['itemId']}).find("-141261448") == True:
                #Forerunner Platform 12x10x42 Left B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 54)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_LEFT_B_MP

            elif str({object['itemId']}).find("-1922306718") == True:
                #Forerunner Platform 12x10x42 Right A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 55)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_A_MP

            elif str({object['itemId']}).find("-92830916") == True:
                #Forerunner Platform 12x10x42 Right B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 56)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_12_X_10_X_42_RIGHT_B_MP

            elif str({object['itemId']}).find("-426854799") == True:
                #Forerunner Platform 16x08x42 MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_16_X_08_X_42_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 57)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_16_X_08_X_42_MP

            elif str({object['itemId']}).find("1293268662") == True:
                #Forerunner Platform 18x06x46 Left A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 58)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_A_MP

            elif str({object['itemId']}).find("1205578211") == True:
                #Forerunner Platform 18x06x46 Left B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 59)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_LEFT_B_MP

            elif str({object['itemId']}).find("-1397239392") == True:
                #Forerunner Platform 18x06x46 Right A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 60)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_A_MP

            elif str({object['itemId']}).find("1631560885") == True:
                #Forerunner Platform 18x06x46 Right B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 61)
                ticker += Sorter.obj_FORERUNNER_PLATFORM_18_X_06_X_46_RIGHT_B_MP
            
            elif str({object['itemId']}).find("1623818481") == True:
                #Forerunner Support A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 62)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_A_MP

            elif str({object['itemId']}).find("-1329827127") == True:
                #Forerunner Support B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 63)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_B_MP
            
            elif str({object['itemId']}).find("-565700411") == True:
                #Forerunner Support C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 64)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_C_MP

            elif str({object['itemId']}).find("2121345589") == True:
                #Forerunner Totem Ring A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 65)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_A_MP

            elif str({object['itemId']}).find("1252026776") == True:
                #Forerunner Totem Ring B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 66)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_B_MP

            elif str({object['itemId']}).find("720172841") == True:
                #Forerunner Totem Ring C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 67)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_C_MP

            elif str({object['itemId']}).find("-438435490") == True:
                #Forerunner Totem Ring Chunk MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_CHUNK_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 68)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_CHUNK_MP

            elif str({object['itemId']}).find("-394272716") == True:
                #Forerunner Totem Ring Debris MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TOTEM_RING_DEBRIS_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 69)
                ticker += Sorter.obj_FORERUNNER_TOTEM_RING_DEBRIS_MP

            elif str({object['itemId']}).find("-902390836") == True:
                #Hacking Terminal MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_HACKING_TERMINAL_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 21, 70)
                ticker += Sorter.obj_HACKING_TERMINAL_MP
            ## Garbage 24
            elif str({object['itemId']}).find("1184267755") == True:
                #Civilian Dumpster
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CIVILIAN_DUMPSTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 22, 0)
                ticker += Sorter.obj_CIVILIAN_DUMPSTER

            elif str({object['itemId']}).find("1726341749") == True:
                #Dumpster
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DUMPSTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 22, 1)
                ticker += Sorter.obj_DUMPSTER

            elif str({object['itemId']}).find("-2143765828") == True:
                #Garbage Can
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GARBAGE_CAN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 22, 2)
                ticker += Sorter.obj_GARBAGE_CAN

            elif str({object['itemId']}).find("-1711743473") == True:
                #Trash Can Closed
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TRASH_CAN_CLOSED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 22, 3)
                ticker += Sorter.obj_TRASH_CAN_CLOSED
            ## Garbage MP 25
            ## Glass 26
            elif str({object['itemId']}).find("1004559525") == True:
                #Glass Transparent 50%
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLASS_TRANSPARENT_50_+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 24, 4)
                ticker += Sorter.obj_GLASS_TRANSPARENT_50_
            ## Missiles 27
            elif str({object['itemId']}).find("1175500974") == True:
                #Missile Launcher Turret
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MISSILE_LAUNCHER_TURRET+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 25, 0)
                ticker += Sorter.obj_MISSILE_LAUNCHER_TURRET

            elif str({object['itemId']}).find("1008197921") == True:
                #Missile Rack
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MISSILE_RACK+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 25, 1)
                ticker += Sorter.obj_MISSILE_RACK
            ## Missiles MP 28
            ## Panels 29
            elif str({object['itemId']}).find("1412353944") == True:
                #Skeletal Panel
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SKELETAL_PANEL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 27, 1)
                ticker += Sorter.obj_SKELETAL_PANEL
            ## Pipes 30
            ## Railings 31
            ## Railings MP 32
            ## Rubble 33
            elif str({object['itemId']}).find("-1254749247") == True:
                #UNSC Rubble Pile Small
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_RUBBLE_PILE_SMALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 31, 3)
                ticker += Sorter.obj_UNSC_RUBBLE_PILE_SMALL
            ## Sandbags 34
            ## Sandbags MP 35
            ## Signs 36
            ## Supports 37
            elif str({object['itemId']}).find("388597365") == True:
                #Angled Boomerang
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_BOOMERANG+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 0)
                ticker += Sorter.obj_ANGLED_BOOMERANG

            elif str({object['itemId']}).find("-447480679") == True:
                #Double Sided Bracket
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DOUBLE_SIDED_BRACKET+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 3)
                ticker += Sorter.obj_DOUBLE_SIDED_BRACKET

            elif str({object['itemId']}).find("-2121320675") == True:
                #Double Sided Support
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DOUBLE_SIDED_SUPPORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 4)
                ticker += Sorter.obj_DOUBLE_SIDED_SUPPORT

            elif str({object['itemId']}).find("-1937170314") == True:
                #Skinny Support
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SKINNY_SUPPORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 13)
                ticker += Sorter.obj_SKINNY_SUPPORT

            elif str({object['itemId']}).find("-1390333281") == True:
                #Skinny Support H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SKINNY_SUPPORT_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 14)
                ticker += Sorter.obj_SKINNY_SUPPORT_H

            elif str({object['itemId']}).find("-1534056042") == True:
                #Squared Truss
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SQUARED_TRUSS+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 15)
                ticker += Sorter.obj_SQUARED_TRUSS

            elif str({object['itemId']}).find("1366480576") == True:
                #Support A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUPPORT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 16)
                ticker += Sorter.obj_SUPPORT_A

            elif str({object['itemId']}).find("539061844") == True:
                #Support Bracket E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUPPORT_BRACKET_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 18)
                ticker += Sorter.obj_SUPPORT_BRACKET_E

            elif str({object['itemId']}).find("-832173783") == True:
                #Support Bracket I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUPPORT_BRACKET_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 19)
                ticker += Sorter.obj_SUPPORT_BRACKET_I

            elif str({object['itemId']}).find("586209564") == True:
                #Support Scaffolding
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUPPORT_SCAFFOLDING+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 21)
                ticker += Sorter.obj_SUPPORT_SCAFFOLDING

            elif str({object['itemId']}).find("589331469") == True:
                #Y Beam Support
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_Y_BEAM_SUPPORT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 35, 23)
                ticker += Sorter.obj_Y_BEAM_SUPPORT
            ## Tools MP 38
            ## UNSC 39
            elif str({object['itemId']}).find("933791967") == True:
                #Concrete Block E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CONCRETE_BLOCK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 17)
                ticker += Sorter.obj_CONCRETE_BLOCK_E
            
            elif str({object['itemId']}).find("-1571456834") == True:
                #Concrete Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CONCRETE_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 19)
                ticker += Sorter.obj_CONCRETE_COLUMN

            elif str({object['itemId']}).find("-512075585") == True:
                #Dry Erase Marker
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DRY_ERASE_MARKER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 26)
                ticker += Sorter.obj_DRY_ERASE_MARKER

            elif str({object['itemId']}).find("2140203211") == True:
                #Floor Podium
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_PODIUM+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 30)
                ticker += Sorter.obj_FLOOR_PODIUM

            elif str({object['itemId']}).find("1596726030") == True:
                #Gun Mount Girder A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GUN_MOUNT_GIRDER_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 38)
                ticker += Sorter.obj_GUN_MOUNT_GIRDER_A

            elif str({object['itemId']}).find("-1008738809") == True:
                #Metal Beam
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_METAL_BEAM+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 48)
                ticker += Sorter.obj_METAL_BEAM

            elif str({object['itemId']}).find("1648288687") == True:
                #Sleeping Bag Unrolled
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SLEEPING_BAG_UNROLLED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 64)
                ticker += Sorter.obj_SLEEPING_BAG_UNROLLED

            elif str({object['itemId']}).find("-1293145628") == True:
                #Truss Girder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TRUSS_GIRDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 69)
                ticker += Sorter.obj_TRUSS_GIRDER

            elif str({object['itemId']}).find("274133904") == True:
                #UNSC Bot Separation Pen
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_BOT_SEPARATION_PEN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 70)
                ticker += Sorter.obj_UNSC_BOT_SEPARATION_PEN

            elif str({object['itemId']}).find("-1525038282") == True:
                #UNSC Road
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_ROAD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 80)
                ticker += Sorter.obj_UNSC_ROAD

            elif str({object['itemId']}).find("1683702270") == True:
                #Wreckage Hull Support Beam B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WRECKAGE_HULL_SUPPORT_BEAM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 37, 102)
                ticker += Sorter.obj_WRECKAGE_HULL_SUPPORT_BEAM_B
            ## UNSC MP 40
            elif str({object['itemId']}).find("1806717236") == True:
                #Concrete Block A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CONCRETE_BLOCK_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 38, 4)
                ticker += Sorter.obj_CONCRETE_BLOCK_A_MP
            ## Vehicles 41
            ## Vehicles MP 42
            elif str({object['itemId']}).find("-1771771675") == True:
                #Tanker Truck MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TANKER_TRUCK_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 40, 1)
                ticker += Sorter.obj_TANKER_TRUCK_MP
            ## Wires 43
            elif str({object['itemId']}).find("1573061490") == True:
                #Cable
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CABLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 0)
                ticker += Sorter.obj_CABLE

            elif str({object['itemId']}).find("370473242") == True:
                #Cable Cap
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CABLE_CAP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 1)
                ticker += Sorter.obj_CABLE_CAP

            elif str({object['itemId']}).find("1074286548") == True:
                #Capped Cable
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CAPPED_CABLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 2)
                ticker += Sorter.obj_CAPPED_CABLE

            elif str({object['itemId']}).find("-1634935313") == True:
                #Curved Wires
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_WIRES+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 3)
                ticker += Sorter.obj_CURVED_WIRES
            
            elif str({object['itemId']}).find("-1116686113") == True:
                #UNSC Hanging Cables
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_HANGING_CABLES+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 4)
                ticker += Sorter.obj_UNSC_HANGING_CABLES

            elif str({object['itemId']}).find("-1565231419") == True:
                #UNSC Hanging Wires C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_HANGING_WIRES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 5)
                ticker += Sorter.obj_UNSC_HANGING_WIRES_C

            elif str({object['itemId']}).find("2098088261") == True:
                #UNSC Hanging Wires D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_HANGING_WIRES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 6)
                ticker += Sorter.obj_UNSC_HANGING_WIRES_D

            elif str({object['itemId']}).find("-1162102626") == True:
                #UNSC Hanging Wires E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_HANGING_WIRES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 2, 41, 7)
                ticker += Sorter.obj_UNSC_HANGING_WIRES_E
            ## Wires MP 44
            ## Workstations 45
            ## Workstations MP 46

            # Biomes 3
            ## Bushes MP 1
            ## Flora MP 2
            ## Ice and Snow 3
            ## Rocks - Alpine 4
            elif str({object['itemId']}).find("-223934709") == True:
                #Alpine Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 0)
                ticker += Sorter.obj_ALPINE_BOULDER

            elif str({object['itemId']}).find("-499246483") == True:
                #Alpine Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 1)
                ticker += Sorter.obj_ALPINE_ROCK_ARCH

            elif str({object['itemId']}).find("-1019954754") == True:
                #Alpine Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 2)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_A

            elif str({object['itemId']}).find("697241012") == True:
                #Alpine Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 3)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_B

            elif str({object['itemId']}).find("1941401960") == True:
                #Alpine Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 4)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_C

            elif str({object['itemId']}).find("1687711537") == True:
                #Alpine Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 5)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_D

            elif str({object['itemId']}).find("-1661170890") == True:
                #Alpine Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 6)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_E

            elif str({object['itemId']}).find("-1788087682") == True:
                #Alpine Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 7)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_F

            elif str({object['itemId']}).find("-1574092891") == True:
                #Alpine Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 8)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_G

            elif str({object['itemId']}).find("-531530003") == True:
                #Alpine Rock Chunk H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 9)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_H

            elif str({object['itemId']}).find("-1241957150") == True:
                #Alpine Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 10)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_I

            elif str({object['itemId']}).find("1529349723") == True:
                #Alpine Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 11)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_J

            elif str({object['itemId']}).find("1902587622") == True:
                #Alpine Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 12)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_K

            elif str({object['itemId']}).find("925775553") == True:
                #Alpine Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 13)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_L

            elif str({object['itemId']}).find("587667485") == True:
                #Alpine Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 14)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_M

            elif str({object['itemId']}).find("738376018") == True:
                #Alpine Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 15)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_N

            elif str({object['itemId']}).find("-841557003") == True:
                #Alpine Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 16)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_O
                
            elif str({object['itemId']}).find("729513625") == True:
                #Alpine Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 17)
                ticker += Sorter.obj_ALPINE_ROCK_CHUNK_P

            elif str({object['itemId']}).find("625689052") == True:
                #Alpine Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 18)
                ticker += Sorter.obj_ALPINE_ROCK_CLIFF

            elif str({object['itemId']}).find("1354863291") == True:
                #Alpine Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 19)
                ticker += Sorter.obj_ALPINE_ROCK_COLUMN

            elif str({object['itemId']}).find("81540265") == True:
                #Alpine Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 20)
                ticker += Sorter.obj_ALPINE_ROCK_FLAT

            elif str({object['itemId']}).find("-1195911236") == True:
                #Alpine Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 21)
                ticker += Sorter.obj_ALPINE_ROCK_GROUP_A

            elif str({object['itemId']}).find("1256258313") == True:
                #Alpine Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 22)
                ticker += Sorter.obj_ALPINE_ROCK_GROUP_B

            elif str({object['itemId']}).find("-1243139546") == True:
                #Alpine Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 23)
                ticker += Sorter.obj_ALPINE_STALACTITES_A

            elif str({object['itemId']}).find("-660642893") == True:
                #Alpine Stalactites 3
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 24)
                ticker += Sorter.obj_ALPINE_STALACTITES_B

            elif str({object['itemId']}).find("-1709550829") == True:
                #Alpine Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 25)
                ticker += Sorter.obj_ALPINE_STALACTITES_C

            elif str({object['itemId']}).find("-1470488868") == True:
                #Alpine Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 26)
                ticker += Sorter.obj_ALPINE_STALACTITES_D

            elif str({object['itemId']}).find("-263669555") == True:
                #Alpine Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 27)
                ticker += Sorter.obj_ALPINE_STALACTITES_E

            elif str({object['itemId']}).find("906312408") == True:
                #Alpine Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 3, 28)
                ticker += Sorter.obj_ALPINE_STALACTITES_F
            ## Rocks - Burnt Forest 5
            elif str({object['itemId']}).find("-2048057069") == True:
                #Burnt Forest Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 0)
                ticker += Sorter.obj_BURNT_FOREST_BOULDER

            elif str({object['itemId']}).find("2145126493") == True:
                #Burnt Forest Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 1)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_ARCH

            elif str({object['itemId']}).find("-1376531898") == True:
                #Burnt Forest Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 2)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_A

            elif str({object['itemId']}).find("-962364181") == True:
                #Burnt Forest Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 3)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_B

            elif str({object['itemId']}).find("992140588") == True:
                #Burnt Forest Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 4)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_C

            elif str({object['itemId']}).find("1582217019") == True:
                #Burnt Forest Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 5)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_D

            elif str({object['itemId']}).find("1048269080") == True:
                #Burnt Forest Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 6)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_E

            elif str({object['itemId']}).find("-483618691") == True:
                #Burnt Forest Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 7)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_F

            elif str({object['itemId']}).find("977304953") == True:
                #Burnt Forest Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 8)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_G

            elif str({object['itemId']}).find("892834596") == True:
                #Burnt Forest Rock Chunk H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 9)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_H

            elif str({object['itemId']}).find("-1699174246") == True:
                #Burnt Forest Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 10)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_I

            elif str({object['itemId']}).find("1627118028") == True:
                #Burnt Forest Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 11)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_J

            elif str({object['itemId']}).find("-1786323650") == True:
                #Burnt Forest Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 12)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_K

            elif str({object['itemId']}).find("1933259541") == True:
                #Burnt Forest Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 13)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_L

            elif str({object['itemId']}).find("-52133979") == True:
                #Burnt Forest Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 14)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_M

            elif str({object['itemId']}).find("-1607963715") == True:
                #Burnt Forest Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 15)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_N

            elif str({object['itemId']}).find("104888214") == True:
                #Burnt Forest Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 16)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_O

            elif str({object['itemId']}).find("-12189487") == True:
                #Burnt Forest Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 17)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CHUNK_P

            elif str({object['itemId']}).find("1398909075") == True:
                #Burnt Forest Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 18)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_CLIFF

            elif str({object['itemId']}).find("240189424") == True:
                #Burnt Forest Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 19)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_COLUMN

            elif str({object['itemId']}).find("-1197297166") == True:
                #Burnt Forest Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 20)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_FLAT

            elif str({object['itemId']}).find("-1551314345") == True:
                #Burnt Forest Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 21)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_GROUP_A

            elif str({object['itemId']}).find("-17537832") == True:
                #Burnt Forest Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 22)
                ticker += Sorter.obj_BURNT_FOREST_ROCK_GROUP_B

            elif str({object['itemId']}).find("-2120187886") == True:
                #Burnt Forest Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 23)
                ticker += Sorter.obj_BURNT_FOREST_STALACTITES_A

            elif str({object['itemId']}).find("463893312") == True:
                #Burnt Forest Stalactites B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 24)
                ticker += Sorter.obj_BURNT_FOREST_STALACTITES_B

            elif str({object['itemId']}).find("793368941") == True:
                #Burnt Forest Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 25)
                ticker += Sorter.obj_BURNT_FOREST_STALACTITES_C

            elif str({object['itemId']}).find("825511813") == True:
                #Burnt Forest Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 26)
                ticker += Sorter.obj_BURNT_FOREST_STALACTITES_D

            elif str({object['itemId']}).find("1956545209") == True:
                #Burnt Forest Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 27)
                ticker += Sorter.obj_BURNT_FOREST_STALACTITES_E

            elif str({object['itemId']}).find("2068056861") == True:
                #Burnt Forest Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BURNT_FOREST_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 4, 28)
                ticker += Sorter.obj_BURNT_FOREST_STALACTITES_F
            ## Rocks - Desert 6
            elif str({object['itemId']}).find("-453665744") == True:
                #Desert Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 0)
                ticker += Sorter.obj_DESERT_BOULDER

            elif str({object['itemId']}).find("-74922723") == True:
                #Desert Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 1)
                ticker += Sorter.obj_DESERT_ROCK_ARCH
                
            elif str({object['itemId']}).find("1143017283") == True:
                #Desert Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 2)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_A

            elif str({object['itemId']}).find("1048266527") == True:
                #Desert Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 3)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_B

            elif str({object['itemId']}).find("-755969645") == True:
                #Desert Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 4)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_C

            elif str({object['itemId']}).find("1470161378") == True:
                #Desert Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 5)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_D

            elif str({object['itemId']}).find("-1983915860") == True:
                #Desert Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 6)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_E

            elif str({object['itemId']}).find("-411298947") == True:
                #Desert Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 7)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_F

            elif str({object['itemId']}).find("-1381857670") == True:
                #Desert Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 8)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_G

            elif str({object['itemId']}).find("389561087") == True:
                #Desert Rock Chunk H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 9)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_H

            elif str({object['itemId']}).find("-878477843") == True:
                #Desert Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 10)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_I

            elif str({object['itemId']}).find("-768127056") == True:
                #Desert Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 11)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_J

            elif str({object['itemId']}).find("-2127492930") == True:
                #Desert Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 12)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_K

            elif str({object['itemId']}).find("304568000") == True:
                #Desert Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 13)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_L

            elif str({object['itemId']}).find("1237302024") == True:
                #Desert Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 14)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_M

            elif str({object['itemId']}).find("-1599682496") == True:
                #Desert Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 15)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_N

            elif str({object['itemId']}).find("1535507286") == True:
                #Desert Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 16)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_O

            elif str({object['itemId']}).find("506229040") == True:
                #Desert Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 17)
                ticker += Sorter.obj_DESERT_ROCK_CHUNK_P

            elif str({object['itemId']}).find("-608096869") == True:
                #Desert Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 18)
                ticker += Sorter.obj_DESERT_ROCK_CLIFF

            elif str({object['itemId']}).find("877335626") == True:
                #Desert Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 19)
                ticker += Sorter.obj_DESERT_ROCK_COLUMN

            elif str({object['itemId']}).find("-1927885221") == True:
                #Desert Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 20)
                ticker += Sorter.obj_DESERT_ROCK_FLAT

            elif str({object['itemId']}).find("-1276771669") == True:
                #Desert Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 21)
                ticker += Sorter.obj_DESERT_ROCK_GROUP_A

            elif str({object['itemId']}).find("1902037207") == True:
                #Desert Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 22)
                ticker += Sorter.obj_DESERT_ROCK_GROUP_B

            elif str({object['itemId']}).find("-1575790870") == True:
                #Desert Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 23)
                ticker += Sorter.obj_DESERT_STALACTITES_A

            elif str({object['itemId']}).find("-856427697") == True:
                #Desert Stalactites B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 24)
                ticker += Sorter.obj_DESERT_STALACTITES_B

            elif str({object['itemId']}).find("1188803818") == True:
                #Desert Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 25)
                ticker += Sorter.obj_DESERT_STALACTITES_C

            elif str({object['itemId']}).find("-2128216670") == True:
                #Desert Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 26)
                ticker += Sorter.obj_DESERT_STALACTITES_D

            elif str({object['itemId']}).find("2047488532") == True:
                #Desert Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 27)
                ticker += Sorter.obj_DESERT_STALACTITES_E

            elif str({object['itemId']}).find("-237488185") == True:
                #Desert Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DESERT_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 5, 28)
                ticker += Sorter.obj_DESERT_STALACTITES_F
            ## Rocks - Glacier 7
            elif str({object['itemId']}).find("-280090707") == True:
                #Glacier Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 0)
                ticker += Sorter.obj_GLACIER_BOULDER

            elif str({object['itemId']}).find("32433901") == True:
                #Glacier Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 1)
                ticker += Sorter.obj_GLACIER_ROCK_ARCH

            elif str({object['itemId']}).find("330109517") == True:
                #Glacier Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 2)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_A

            elif str({object['itemId']}).find("-1514901111") == True:
                #Glacier Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 3)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_B

            elif str({object['itemId']}).find("-598928316") == True:
                #Glacier Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 4)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_C

            elif str({object['itemId']}).find("2001436665") == True:
                #Glacier Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 5)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_D

            elif str({object['itemId']}).find("-2137189496") == True:
                #Glacier Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 6)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_E

            elif str({object['itemId']}).find("970316359") == True:
                #Glacier Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 7)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_F

            elif str({object['itemId']}).find("-294928196") == True:
                #Glacier Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 8)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_G

            elif str({object['itemId']}).find("157773966") == True:
                #Glacier Rock Chunk H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 9)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_H

            elif str({object['itemId']}).find("230300676") == True:
                #Glacier Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 10)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_I

            elif str({object['itemId']}).find("2036077727") == True:
                #Glacier Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 11)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_J

            elif str({object['itemId']}).find("-1310595169") == True:
                #Glacier Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 12)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_K

            elif str({object['itemId']}).find("-644420137") == True:
                #Glacier Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 13)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_L

            elif str({object['itemId']}).find("-2038184581") == True:
                #Glacier Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 14)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_M

            elif str({object['itemId']}).find("-1931847197") == True:
                #Glacier Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 15)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_N

            elif str({object['itemId']}).find("-935312532") == True:
                #Glacier Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 16)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_O

            elif str({object['itemId']}).find("-1136624030") == True:
                #Glacier Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 17)
                ticker += Sorter.obj_GLACIER_ROCK_CHUNK_P

            elif str({object['itemId']}).find("704374045") == True:
                #Glacier Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 18)
                ticker += Sorter.obj_GLACIER_ROCK_CLIFF

            elif str({object['itemId']}).find("1098097045") == True:
                #Glacier Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 19)
                ticker += Sorter.obj_GLACIER_ROCK_COLUMN

            elif str({object['itemId']}).find("-1769603043") == True:
                #Glacier Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 20)
                ticker += Sorter.obj_GLACIER_ROCK_FLAT

            elif str({object['itemId']}).find("-658254618") == True:
                #Glacier Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 21)
                ticker += Sorter.obj_GLACIER_ROCK_GROUP_A

            elif str({object['itemId']}).find("1191635031") == True:
                #Glacier Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 22)
                ticker += Sorter.obj_GLACIER_ROCK_GROUP_B

            elif str({object['itemId']}).find("1209018908") == True:
                #Glacier Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 23)
                ticker += Sorter.obj_GLACIER_STALACTITES_A

            elif str({object['itemId']}).find("635231024") == True:
                #Glacier Stalactites B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 24)
                ticker += Sorter.obj_GLACIER_STALACTITES_B

            elif str({object['itemId']}).find("-1767551077") == True:
                #Glacier Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 25)
                ticker += Sorter.obj_GLACIER_STALACTITES_C

            elif str({object['itemId']}).find("-464008717") == True:
                #Glacier Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 26)
                ticker += Sorter.obj_GLACIER_STALACTITES_D

            elif str({object['itemId']}).find("-2066994573") == True:
                #Glacier Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 27)
                ticker += Sorter.obj_GLACIER_STALACTITES_E

            elif str({object['itemId']}).find("-1600190957") == True:
                #Glacier Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GLACIER_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 6, 28)
                ticker += Sorter.obj_GLACIER_STALACTITES_F
            ## Rocks - Misc 8
            elif str({object['itemId']}).find("-319001155") == True:
                #Eroded Terrain Column A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ERODED_TERRAIN_COLUMN_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 0)
                ticker += Sorter.obj_ERODED_TERRAIN_COLUMN_A
                
            elif str({object['itemId']}).find("-319095573") == True:
                #Eroded Terrain Column B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ERODED_TERRAIN_COLUMN_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 1)
                ticker += Sorter.obj_ERODED_TERRAIN_COLUMN_B

            elif str({object['itemId']}).find("-1835432896") == True:
                #Eroded Terrain D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ERODED_TERRAIN_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 2)
                ticker += Sorter.obj_ERODED_TERRAIN_D

            elif str({object['itemId']}).find("1605936690") == True:
                #Eroded Terrain E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ERODED_TERRAIN_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 3)
                ticker += Sorter.obj_ERODED_TERRAIN_E

            elif str({object['itemId']}).find("-1531765676") == True:
                #Terrain Hex Granite A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TERRAIN_HEX_GRANITE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 5)
                ticker += Sorter.obj_TERRAIN_HEX_GRANITE_A

            elif str({object['itemId']}).find("1660588673") == True:
                #Terrain Hex Granite C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TERRAIN_HEX_GRANITE_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 6)
                ticker += Sorter.obj_TERRAIN_HEX_GRANITE_C
            ## Rocks - Space 9
            elif str({object['itemId']}).find("947954639") == True:
                #Space Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 0)
                ticker += Sorter.obj_SPACE_BOULDER

            elif str({object['itemId']}).find("-403512679") == True:
                #Space Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 1)
                ticker += Sorter.obj_SPACE_ROCK_ARCH

            elif str({object['itemId']}).find("524142540") == True:
                #Space Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 2)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_A

            elif str({object['itemId']}).find("1911987990") == True:
                #Space Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 3)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_B

            elif str({object['itemId']}).find("1952375295") == True:
                #Space Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 4)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_C

            elif str({object['itemId']}).find("1148559722") == True:
                #Space Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 5)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_D

            elif str({object['itemId']}).find("-588415057") == True:
                #Space Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 6)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_E

            elif str({object['itemId']}).find("-1439422134") == True:
                #Space Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 7)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_F

            elif str({object['itemId']}).find("700857788") == True:
                #Space Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 8)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_G

            elif str({object['itemId']}).find("-1814670706") == True:
                #Space Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 9)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_H

            elif str({object['itemId']}).find("-1653975283") == True:
                #Space Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 10)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_I

            elif str({object['itemId']}).find("-802845598") == True:
                #Space Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 11)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_J

            elif str({object['itemId']}).find("-1030104102") == True:
                #Space Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 12)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_K

            elif str({object['itemId']}).find("-813309069") == True:
                #Space Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 13)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_L

            elif str({object['itemId']}).find("-26569928") == True:
                #Space Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 14)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_M

            elif str({object['itemId']}).find("-679471545") == True:
                #Space Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 15)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_N

            elif str({object['itemId']}).find("523634536") == True:
                #Space Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 16)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_O

            elif str({object['itemId']}).find("-457598994") == True:
                #Space Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 17)
                ticker += Sorter.obj_SPACE_ROCK_CHUNK_P

            elif str({object['itemId']}).find("1554113302") == True:
                #Space Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 18)
                ticker += Sorter.obj_SPACE_ROCK_CLIFF

            elif str({object['itemId']}).find("1788115918") == True:
                #Space Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 19)
                ticker += Sorter.obj_SPACE_ROCK_COLUMN

            elif str({object['itemId']}).find("1255341472") == True:
                #Space Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 20)
                ticker += Sorter.obj_SPACE_ROCK_FLAT

            elif str({object['itemId']}).find("-671124120") == True:
                #Space Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 21)
                ticker += Sorter.obj_SPACE_ROCK_GROUP_A

            elif str({object['itemId']}).find("-1418057158") == True:
                #Space Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 22)
                ticker += Sorter.obj_SPACE_ROCK_GROUP_B

            elif str({object['itemId']}).find("-579761870") == True:
                #Space Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 23)
                ticker += Sorter.obj_SPACE_STALACTITES_A

            elif str({object['itemId']}).find("849552049") == True:
                #Space Stalactites B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 24)
                ticker += Sorter.obj_SPACE_STALACTITES_B

            elif str({object['itemId']}).find("-142862479") == True:
                #Space Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 25)
                ticker += Sorter.obj_SPACE_STALACTITES_C

            elif str({object['itemId']}).find("1017712650") == True:
                #Space Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 26)
                ticker += Sorter.obj_SPACE_STALACTITES_D

            elif str({object['itemId']}).find("-370548665") == True:
                #Space Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 27)
                ticker += Sorter.obj_SPACE_STALACTITES_E

            elif str({object['itemId']}).find("-608923979") == True:
                #Space Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPACE_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 8, 28)
                ticker += Sorter.obj_SPACE_STALACTITES_F
            ## Rocks - Tidal 10
            elif str({object['itemId']}).find("1208611533") == True:
                #Tidal Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 0)
                ticker += Sorter.obj_TIDAL_BOULDER

            elif str({object['itemId']}).find("1319039586") == True:
                #Tidal Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 1)
                ticker += Sorter.obj_TIDAL_ROCK_ARCH

            elif str({object['itemId']}).find("-400292641") == True:
                #Tidal Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 2)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_A

            elif str({object['itemId']}).find("-956199155") == True:
                #Tidal Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 3)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_B

            elif str({object['itemId']}).find("-189279896") == True:
                #Tidal Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 4)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_C

            elif str({object['itemId']}).find("1979171534") == True:
                #Tidal Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 5)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_D

            elif str({object['itemId']}).find("1539963162") == True:
                #Tidal Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 6)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_E

            elif str({object['itemId']}).find("-737904837") == True:
                #Tidal Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 7)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_F

            elif str({object['itemId']}).find("-1621053953") == True:
                #Tidal Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 8)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_G

            elif str({object['itemId']}).find("1981931021") == True:
                #Tidal Rock Chunk H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 9)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_H

            elif str({object['itemId']}).find("-2049266511") == True:
                #Tidal Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 10)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_I
                
            elif str({object['itemId']}).find("765147319") == True:
                #Tidal Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 11)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_J

            elif str({object['itemId']}).find("1212364087") == True:
                #Tidal Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 12)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_K

            elif str({object['itemId']}).find("-1536841963") == True:
                #Tidal Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 13)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_L

            elif str({object['itemId']}).find("-1418584172") == True:
                #Tidal Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 14)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_M

            elif str({object['itemId']}).find("-1484112608") == True:
                #Tidal Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 15)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_N

            elif str({object['itemId']}).find("1504213608") == True:
                #Tidal Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 16)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_O

            elif str({object['itemId']}).find("1047520077") == True:
                #Tidal Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 17)
                ticker += Sorter.obj_TIDAL_ROCK_CHUNK_P

            elif str({object['itemId']}).find("2014297245") == True:
                #Tidal Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 18)
                ticker += Sorter.obj_TIDAL_ROCK_CLIFF

            elif str({object['itemId']}).find("-360395851") == True:
                #Tidal Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 19)
                ticker += Sorter.obj_TIDAL_ROCK_COLUMN

            elif str({object['itemId']}).find("1375061790") == True:
                #Tidal Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 20)
                ticker += Sorter.obj_TIDAL_ROCK_FLAT

            elif str({object['itemId']}).find("990822374") == True:
                #Tidal Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 21)
                ticker += Sorter.obj_TIDAL_ROCK_GROUP_A

            elif str({object['itemId']}).find("1535950428") == True:
                #Tidal Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 22)
                ticker += Sorter.obj_TIDAL_ROCK_GROUP_B

            elif str({object['itemId']}).find("-85473346") == True:
                #Tidal Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 23)
                ticker += Sorter.obj_TIDAL_STALACTITES_A

            elif str({object['itemId']}).find("1756216113") == True:
                #Tidal Stalactites B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 24)
                ticker += Sorter.obj_TIDAL_STALACTITES_B

            elif str({object['itemId']}).find("-1658217552") == True:
                #Tidal Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 25)
                ticker += Sorter.obj_TIDAL_STALACTITES_C

            elif str({object['itemId']}).find("57604546") == True:
                #Tidal Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 26)
                ticker += Sorter.obj_TIDAL_STALACTITES_D

            elif str({object['itemId']}).find("1708640340") == True:
                #Tidal Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 27)
                ticker += Sorter.obj_TIDAL_STALACTITES_E

            elif str({object['itemId']}).find("836453594") == True:
                #Tidal Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TIDAL_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 9, 28)
                ticker += Sorter.obj_TIDAL_STALACTITES_F
            ## Rocks - Wetlands 11
            elif str({object['itemId']}).find("-416461967") == True:
                #Wetlands Boulder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_BOULDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 0)
                ticker += Sorter.obj_WETLANDS_BOULDER

            elif str({object['itemId']}).find("-1886308403") == True:
                #Wetlands Rock Arch
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_ARCH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 1)
                ticker += Sorter.obj_WETLANDS_ROCK_ARCH

            elif str({object['itemId']}).find("1047722046") == True:
                #Wetlands Rock Chunk A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 2)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_A

            elif str({object['itemId']}).find("2114351914") == True:
                #Wetlands Rock Chunk B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 3)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_B

            elif str({object['itemId']}).find("-1094046084") == True:
                #Wetlands Rock Chunk C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 4)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_C

            elif str({object['itemId']}).find("-1554213874") == True:
                #Wetlands Rock Chunk D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 5)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_D

            elif str({object['itemId']}).find("80415170") == True:
                #Wetlands Rock Chunk E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 6)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_E

            elif str({object['itemId']}).find("2031507976") == True:
                #Wetlands Rock Chunk F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 7)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_F

            elif str({object['itemId']}).find("2043245326") == True:
                #Wetlands Rock Chunk G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 8)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_G

            elif str({object['itemId']}).find("-1199633408") == True:
                #Wetlands Rock Chunk H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 9)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_H

            elif str({object['itemId']}).find("-330440355") == True:
                #Wetlands Rock Chunk I
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_I+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 10)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_I

            elif str({object['itemId']}).find("-728506015") == True:
                #Wetlands Rock Chunk J
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_J+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 11)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_J

            elif str({object['itemId']}).find("55315362") == True:
                #Wetlands Rock Chunk K
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_K+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 12)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_K

            elif str({object['itemId']}).find("1141287402") == True:
                #Wetlands Rock Chunk L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 13)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_L

            elif str({object['itemId']}).find("1020008154") == True:
                #Wetlands Rock Chunk M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 14)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_M

            elif str({object['itemId']}).find("-973614490") == True:
                #Wetlands Rock Chunk N
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_N+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 15)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_N

            elif str({object['itemId']}).find("-1717689578") == True:
                #Wetlands Rock Chunk O
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_O+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 16)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_O

            elif str({object['itemId']}).find("1224198617") == True:
                #Wetlands Rock Chunk P
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CHUNK_P+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 17)
                ticker += Sorter.obj_WETLANDS_ROCK_CHUNK_P

            elif str({object['itemId']}).find("1594176107") == True:
                #Wetlands Rock Cliff
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_CLIFF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 18)
                ticker += Sorter.obj_WETLANDS_ROCK_CLIFF

            elif str({object['itemId']}).find("18911395") == True:
                #Wetlands Rock Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 19)
                ticker += Sorter.obj_WETLANDS_ROCK_COLUMN

            elif str({object['itemId']}).find("2128612671") == True:
                #Wetlands Rock Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 20)
                ticker += Sorter.obj_WETLANDS_ROCK_FLAT

            elif str({object['itemId']}).find("-631162232") == True:
                #Wetlands Rock Group A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_GROUP_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 21)
                ticker += Sorter.obj_WETLANDS_ROCK_GROUP_A

            elif str({object['itemId']}).find("-1267055777") == True:
                #Wetlands Rock Group B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_ROCK_GROUP_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 22)
                ticker += Sorter.obj_WETLANDS_ROCK_GROUP_B

            elif str({object['itemId']}).find("267709012") == True:
                #Wetlands Stalactites A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_STALACTITES_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 23)
                ticker += Sorter.obj_WETLANDS_STALACTITES_A

            elif str({object['itemId']}).find("1137972971") == True:
                #Wetlands Stalactites B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_STALACTITES_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 24)
                ticker += Sorter.obj_WETLANDS_STALACTITES_B

            elif str({object['itemId']}).find("783352080") == True:
                #Wetlands Stalactites C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_STALACTITES_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 25)
                ticker += Sorter.obj_WETLANDS_STALACTITES_C

            elif str({object['itemId']}).find("-847195141") == True:
                #Wetlands Stalactites D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_STALACTITES_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 26)
                ticker += Sorter.obj_WETLANDS_STALACTITES_D

            elif str({object['itemId']}).find("696150591") == True:
                #Wetlands Stalactites E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_STALACTITES_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 27)
                ticker += Sorter.obj_WETLANDS_STALACTITES_E
                
            elif str({object['itemId']}).find("-623124596") == True:
                #Wetlands Stalactites F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WETLANDS_STALACTITES_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 10, 28)
                ticker += Sorter.obj_WETLANDS_STALACTITES_F
            ## Stumps MP 12
            ## Terrain 13
            elif str({object['itemId']}).find("-870851252") == True:
                #Bank Full
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BANK_FULL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 0)
                ticker += Sorter.obj_BANK_FULL

            elif str({object['itemId']}).find("-454569693") == True:
                #Bank Full TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_BANK_FULL_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 1)
                ticker += Sorter.obj_BANK_FULL_TI

            elif str({object['itemId']}).find("-683994261") == True:
                #Bank Half
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BANK_HALF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 2)
                ticker += Sorter.obj_BANK_HALF

            elif str({object['itemId']}).find("-251228686") == True:
                #Bank Half TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_BANK_HALF_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 3)
                ticker += Sorter.obj_BANK_HALF_TI

            elif str({object['itemId']}).find("-963974273") == True:
                #Bowl Hill
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BOWL_HILL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 4)
                ticker += Sorter.obj_BOWL_HILL

            elif str({object['itemId']}).find("-539718920") == True:
                #Bowl Hill TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_BOWL_HILL_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 5)
                ticker += Sorter.obj_BOWL_HILL_TI

            elif str({object['itemId']}).find("631526139") == True:
                #Ramp
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RAMP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 6)
                ticker += Sorter.obj_RAMP

            elif str({object['itemId']}).find("520558844") == True:
                #Ramp TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_RAMP_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 7)
                ticker += Sorter.obj_RAMP_TI
                
            elif str({object['itemId']}).find("-320436500") == True:
                #Ramp Corner Exterior
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RAMP_CORNER_EXTERIOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 8)
                ticker += Sorter.obj_RAMP_CORNER_EXTERIOR

            elif str({object['itemId']}).find("-515338164") == True:
                #Ramp Corner Exterior TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_RAMP_CORNER_EXTERIOR_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 9)
                ticker += Sorter.obj_RAMP_CORNER_EXTERIOR_TI

            elif str({object['itemId']}).find("-2071552351") == True:
                #Ramp Corner Interior
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RAMP_CORNER_INTERIOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 10)
                ticker += Sorter.obj_RAMP_CORNER_INTERIOR

            elif str({object['itemId']}).find("126867099") == True:
                #Ramp Corner Interior TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_RAMP_CORNER_INTERIOR_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 11)
                ticker += Sorter.obj_RAMP_CORNER_INTERIOR_TI

            elif str({object['itemId']}).find("1530590479") == True:
                #Ramp Transition
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RAMP_TRANSITION+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 12)
                ticker += Sorter.obj_RAMP_TRANSITION

            elif str({object['itemId']}).find("2137117489") == True:
                #Ramp Transition TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_RAMP_TRANSITION_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 13)
                ticker += Sorter.obj_RAMP_TRANSITION_TI

            elif str({object['itemId']}).find("-1207862562") == True:
                #Slope Helper 20
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SLOPE_HELPER_20+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 14)
                ticker += Sorter.obj_SLOPE_HELPER_20

            elif str({object['itemId']}).find("1988437591") == True:
                #Slope Helper 20 TI
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SLOPE_HELPER_20_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 15)
                ticker += Sorter.obj_SLOPE_HELPER_20_TI

            elif str({object['itemId']}).find("-863495419") == True:
                #Slope Helper 40
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SLOPE_HELPER_40+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 16)
                ticker += Sorter.obj_SLOPE_HELPER_40

            elif str({object['itemId']}).find("469262902") == True:
                #Slope Helper 40 TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_SLOPE_HELPER_40_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 17)
                ticker += Sorter.obj_SLOPE_HELPER_40_TI

            elif str({object['itemId']}).find("820488105") == True:
                #Slope Helper 60
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SLOPE_HELPER_60+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 18)
                ticker += Sorter.obj_SLOPE_HELPER_60

            elif str({object['itemId']}).find("118005238") == True:
                #Slope Helper 60 TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_SLOPE_HELPER_60_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 19)
                ticker += Sorter.obj_SLOPE_HELPER_60_TI

            elif str({object['itemId']}).find("-1549263449") == True:
                #Sphere Terrain
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPHERE_TERRAIN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 20)
                ticker += Sorter.obj_SPHERE_TERRAIN

            elif str({object['itemId']}).find("488175425") == True:
                #Sphere Terrain TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_SPHERE_TERRAIN_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 21)
                ticker += Sorter.obj_SPHERE_TERRAIN_TI

            elif str({object['itemId']}).find("2047061831") == True:
                #Terrace Terrain
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TERRACE_TERRAIN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 22)
                ticker += Sorter.obj_TERRACE_TERRAIN

            elif str({object['itemId']}).find("-662742038") == True:
                #Terrace Terrain TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_TERRACE_TERRAIN_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 23)
                ticker += Sorter.obj_TERRACE_TERRAIN_TI

            elif str({object['itemId']}).find("1133511843") == True:
                #Terrain Flat
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TERRAIN_FLAT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 24)
                ticker += Sorter.obj_TERRAIN_FLAT

            elif str({object['itemId']}).find("-1477909429") == True:
                #Terrain Flat TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_TERRAIN_FLAT_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 25)
                ticker += Sorter.obj_TERRAIN_FLAT_TI

            elif str({object['itemId']}).find("1574763282") == True:
                #Terrain Rugged
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TERRAIN_RUGGED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 26)
                ticker += Sorter.obj_TERRAIN_RUGGED

            elif str({object['itemId']}).find("-32087135") == True:
                #Terrain Rugged TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_TERRAIN_RUGGED_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 27)
                ticker += Sorter.obj_TERRAIN_RUGGED_TI

            elif str({object['itemId']}).find("590769305") == True:
                #Trench Terrain
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TRENCH_TERRAIN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 28)
                ticker += Sorter.obj_TRENCH_TERRAIN

            elif str({object['itemId']}).find("855143119") == True:
                #Trench Terrain TI
                mirvTranslator.objTranslationNoObjectMode(sorted_item_list[ticker:Sorter.obj_TRENCH_TERRAIN_TI+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 29)
                ticker += Sorter.obj_TRENCH_TERRAIN_TI
            ## Trees - Logs MP 14
            elif str({object['itemId']}).find("586555322") == True:
                #Fallen Tree A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FALLEN_TREE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 0)
                ticker += Sorter.obj_FALLEN_TREE_A

            elif str({object['itemId']}).find("841874352") == True:
                #Fallen Tree B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FALLEN_TREE_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 1)
                ticker += Sorter.obj_FALLEN_TREE_B

            elif str({object['itemId']}).find("886051836") == True:
                #Fallen Tree C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FALLEN_TREE_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 2)
                ticker += Sorter.obj_FALLEN_TREE_C

            elif str({object['itemId']}).find("898691168") == True:
                #Fallen Tree D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FALLEN_TREE_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 3)
                ticker += Sorter.obj_FALLEN_TREE_D

            elif str({object['itemId']}).find("2007348554") == True:
                #Fallen Tree E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FALLEN_TREE_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 4)
                ticker += Sorter.obj_FALLEN_TREE_E

            elif str({object['itemId']}).find("1836622048") == True:
                #Fallen Tree w/ Roots
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FALLEN_TREE_W_ROOTS+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 5)
                ticker += Sorter.obj_FALLEN_TREE_W_ROOTS

            elif str({object['itemId']}).find("-1509539713") == True:
                #Snagged Log A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SNAGGED_LOG_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 6)
                ticker += Sorter.obj_SNAGGED_LOG_A

            elif str({object['itemId']}).find("-425303348") == True:
                #Snagged Log B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SNAGGED_LOG_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 7)
                ticker += Sorter.obj_SNAGGED_LOG_B

            elif str({object['itemId']}).find("-2089225903") == True:
                #Snagged Log C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SNAGGED_LOG_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 8)
                ticker += Sorter.obj_SNAGGED_LOG_C

            elif str({object['itemId']}).find("-2099489993") == True:
                #Snagged Log D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SNAGGED_LOG_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 14, 9)
                ticker += Sorter.obj_SNAGGED_LOG_D
            ## Trees - Roots MP 15
            elif str({object['itemId']}).find("-1963622591") == True:
                #Root Cluster
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROOT_CLUSTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 15, 0)
                ticker += Sorter.obj_ROOT_CLUSTER

            elif str({object['itemId']}).find("1986307023") == True:
                #Roots A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROOTS_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 15, 1)
                ticker += Sorter.obj_ROOTS_A

            elif str({object['itemId']}).find("789136891") == True:
                #Roots B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROOTS_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 15, 2)
                ticker += Sorter.obj_ROOTS_B

            elif str({object['itemId']}).find("-158806131") == True:
                #Roots C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROOTS_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 15, 3)
                ticker += Sorter.obj_ROOTS_C

            elif str({object['itemId']}).find("427128330") == True:
                #Roots Hanging A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROOTS_HANGING_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 15, 4)
                ticker += Sorter.obj_ROOTS_HANGING_A

            elif str({object['itemId']}).find("-547831186") == True:
                #Roots Hanging B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROOTS_HANGING_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 15, 5)
                ticker += Sorter.obj_ROOTS_HANGING_B
            ## Trees MP 16
            elif str({object['itemId']}).find("357637473") == True:
                #Alpine Highlands Fir Medium B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_HIGHLANDS_FIR_MEDIUM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 0)
                ticker += Sorter.obj_ALPINE_HIGHLANDS_FIR_MEDIUM_B

            elif str({object['itemId']}).find("-548554634") == True:
                #Alpine Highlands Fir Small A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_HIGHLANDS_FIR_SMALL_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 1)
                ticker += Sorter.obj_ALPINE_HIGHLANDS_FIR_SMALL_A
                
            elif str({object['itemId']}).find("-1693312870") == True:
                #Alpine Highlands Fir Small B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_HIGHLANDS_FIR_SMALL_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 2)
                ticker += Sorter.obj_ALPINE_HIGHLANDS_FIR_SMALL_B

            elif str({object['itemId']}).find("1397030039") == True:
                #Alpine Highlands Fir Small C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ALPINE_HIGHLANDS_FIR_SMALL_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 3)
                ticker += Sorter.obj_ALPINE_HIGHLANDS_FIR_SMALL_C
                
            elif str({object['itemId']}).find("-683238530") == True:
                #Date Palm Large A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_LARGE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 4)
                ticker += Sorter.obj_DATE_PALM_LARGE_A

            elif str({object['itemId']}).find("605045097") == True:
                #Date Palm Large B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_LARGE_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 5)
                ticker += Sorter.obj_DATE_PALM_LARGE_B

            elif str({object['itemId']}).find("1173810012") == True:
                #Date Palm Large Dead
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_LARGE_DEAD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 6)
                ticker += Sorter.obj_DATE_PALM_LARGE_DEAD

            elif str({object['itemId']}).find("1168129635") == True:
                #Date Palm Medium A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_MEDIUM_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 7)
                ticker += Sorter.obj_DATE_PALM_MEDIUM_A

            elif str({object['itemId']}).find("680128648") == True:
                #Date Palm Medium B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_MEDIUM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 8)
                ticker += Sorter.obj_DATE_PALM_MEDIUM_B

            elif str({object['itemId']}).find("-564844169") == True:
                #Date Palm Sprout A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_SPROUT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 9)
                ticker += Sorter.obj_DATE_PALM_SPROUT_A

            elif str({object['itemId']}).find("-1463438133") == True:
                #Date Palm Sprout B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DATE_PALM_SPROUT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 10)
                ticker += Sorter.obj_DATE_PALM_SPROUT_B

            elif str({object['itemId']}).find("987637259") == True:
                #Dead Fir Medium A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DEAD_FIR_MEDIUM_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 11)
                ticker += Sorter.obj_DEAD_FIR_MEDIUM_A

            elif str({object['itemId']}).find("-855787963") == True:
                #Dead Fir Medium B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DEAD_FIR_MEDIUM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 12)
                ticker += Sorter.obj_DEAD_FIR_MEDIUM_B

            elif str({object['itemId']}).find("24646342") == True:
                #Larch Dead A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_DEAD_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 13)
                ticker += Sorter.obj_LARCH_DEAD_A

            elif str({object['itemId']}).find("-1342734883") == True:
                #Larch Dead B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_DEAD_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 14)
                ticker += Sorter.obj_LARCH_DEAD_B

            elif str({object['itemId']}).find("-873480580") == True:
                #Larch Dead C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_DEAD_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 15)
                ticker += Sorter.obj_LARCH_DEAD_C

            elif str({object['itemId']}).find("-486508423") == True:
                #Larch Large A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_LARGE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 16)
                ticker += Sorter.obj_LARCH_LARGE_A

            elif str({object['itemId']}).find("-43928113") == True:
                #Larch Large B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_LARGE_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 17)
                ticker += Sorter.obj_LARCH_LARGE_B

            elif str({object['itemId']}).find("380410325") == True:
                #Larch Large C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_LARGE_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 18)
                ticker += Sorter.obj_LARCH_LARGE_C

            elif str({object['itemId']}).find("2134553399") == True:
                #Larch Medium A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_MEDIUM_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 19)
                ticker += Sorter.obj_LARCH_MEDIUM_A

            elif str({object['itemId']}).find("-2034457539") == True:
                #Larch Medium B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_MEDIUM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 20)
                ticker += Sorter.obj_LARCH_MEDIUM_B

            elif str({object['itemId']}).find("-1214088543") == True:
                #Larch Small A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_SMALL_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 21)
                ticker += Sorter.obj_LARCH_SMALL_A

            elif str({object['itemId']}).find("-1301727892") == True:
                #Larch Small B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARCH_SMALL_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 22)
                ticker += Sorter.obj_LARCH_SMALL_B

            elif str({object['itemId']}).find("904339231") == True:
                #Sub Alpine Fir Extra Small
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_EXTRA_SMALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 23)
                ticker += Sorter.obj_SUB_ALPINE_FIR_EXTRA_SMALL

            elif str({object['itemId']}).find("-2133138017") == True:
                #Sub Alpine Fir Large A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_LARGE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 24)
                ticker += Sorter.obj_SUB_ALPINE_FIR_LARGE_A

            elif str({object['itemId']}).find("1663440900") == True:
                #Sub Alpine Fir Large B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_LARGE_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 25)
                ticker += Sorter.obj_SUB_ALPINE_FIR_LARGE_B

            elif str({object['itemId']}).find("155710515") == True:
                #Sub Alpine Fir Medium A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_MEDIUM_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 26)
                ticker += Sorter.obj_SUB_ALPINE_FIR_MEDIUM_A

            elif str({object['itemId']}).find("-1522591343") == True:
                #Sub Alpine Fir Medium B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_MEDIUM_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 27)
                ticker += Sorter.obj_SUB_ALPINE_FIR_MEDIUM_B

            elif str({object['itemId']}).find("1347497524") == True:
                #Sub Alpine Fir Medium C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_MEDIUM_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 28)
                ticker += Sorter.obj_SUB_ALPINE_FIR_MEDIUM_C

            elif str({object['itemId']}).find("-2028442082") == True:
                #Sub Alpine Fir Medium D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_MEDIUM_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 29)
                ticker += Sorter.obj_SUB_ALPINE_FIR_MEDIUM_D

            elif str({object['itemId']}).find("-221326530") == True:
                #Sub Alpine Fir Medium E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_MEDIUM_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 30)
                ticker += Sorter.obj_SUB_ALPINE_FIR_MEDIUM_E

            elif str({object['itemId']}).find("161400328") == True:
                #Sub Alpine Fir Medium F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_MEDIUM_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 31)
                ticker += Sorter.obj_SUB_ALPINE_FIR_MEDIUM_F

            elif str({object['itemId']}).find("1765650409") == True:
                #Sub Alpine Fir Small A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_SMALL_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 32)
                ticker += Sorter.obj_SUB_ALPINE_FIR_SMALL_A
 
            elif str({object['itemId']}).find("-1062039679") == True:
                #Sub Alpine Fir Small B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_SMALL_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 33)
                ticker += Sorter.obj_SUB_ALPINE_FIR_SMALL_B

            elif str({object['itemId']}).find("-1200356126") == True:
                #Sub Alpine Fir Small C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SUB_ALPINE_FIR_SMALL_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 13, 34)
                ticker += Sorter.obj_SUB_ALPINE_FIR_SMALL_C
            ## Water 17
            elif str({object['itemId']}).find("-414884733") == True:
                #Water Plane
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WATER_PLANE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 3, 16, 0)
                ticker += Sorter.obj_WATER_PLANE
            
            # Blockers 4
            ## One Way Blockers 1
            ## Player Blockers 2
            ## Projectile Blockers 3
            ## Team Blockers 4
            elif str({object['itemId']}).find("-1018432779") == True:
                #Team Blocker 128x128x128
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_128X128X128+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 0)
                ticker += Sorter.obj_TEAM_BLOCKER_128X128X128

            elif str({object['itemId']}).find("-1261696019") == True:
                #Team Blocker 128x2x64
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_128X2X64+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 1)
                ticker += Sorter.obj_TEAM_BLOCKER_128X2X64

            elif str({object['itemId']}).find("1252397759") == True:
                #Team Blocker 128x32x32
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_128X32X32+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 2)
                ticker += Sorter.obj_TEAM_BLOCKER_128X32X32

            elif str({object['itemId']}).find("-1762893655") == True:
                #Team Blocker 128x32x32 A
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_128X32X32_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 3)
                ticker += Sorter.obj_TEAM_BLOCKER_128X32X32_A

            elif str({object['itemId']}).find("-1243907050") == True:
                #Team Blocker 128x32x64
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_128X32X64+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 4)
                ticker += Sorter.obj_TEAM_BLOCKER_128X32X64

            elif str({object['itemId']}).find("973538166") == True:
                #Team Blocker 16x16x16
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_16X16X16+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 5)
                ticker += Sorter.obj_TEAM_BLOCKER_16X16X16

            elif str({object['itemId']}).find("-1737474781") == True:
                #Team Blocker 16x2x8
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_16X2X8+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 6)
                ticker += Sorter.obj_TEAM_BLOCKER_16X2X8

            elif str({object['itemId']}).find("-772142774") == True:
                #Team Blocker 16x32x8
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_16X32X8+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 7)
                ticker += Sorter.obj_TEAM_BLOCKER_16X32X8

            elif str({object['itemId']}).find("1184897444") == True:
                #Team Blocker 16x4x4
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_16X4X4+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 8)
                ticker += Sorter.obj_TEAM_BLOCKER_16X4X4

            elif str({object['itemId']}).find("-1116440378") == True:
                #Team Blocker 16x4x4 A
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_16X4X4_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 9)
                ticker += Sorter.obj_TEAM_BLOCKER_16X4X4_A

            elif str({object['itemId']}).find("-1664225091") == True:
                #Team Blocker 1x1x1
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_1X1X1+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 10)
                ticker += Sorter.obj_TEAM_BLOCKER_1X1X1

            elif str({object['itemId']}).find("-1342618612") == True:
                #Team Blocker 256x256x256
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_256X256X256+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 11)
                ticker += Sorter.obj_TEAM_BLOCKER_256X256X256

            elif str({object['itemId']}).find("-695072432") == True:
                #Team Blocker 256x2x128
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_256X2X128+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 12)
                ticker += Sorter.obj_TEAM_BLOCKER_256X2X128

            elif str({object['itemId']}).find("-324375991") == True:
                #Team Blocker 256x32x128
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_256X32X128+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 13)
                ticker += Sorter.obj_TEAM_BLOCKER_256X32X128

            elif str({object['itemId']}).find("-1420481844") == True:
                #Team Blocker 256x64x64
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_256X64X64+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 14)
                ticker += Sorter.obj_TEAM_BLOCKER_256X64X64

            elif str({object['itemId']}).find("177237589") == True:
                #Team Blocker 256x64x64 A
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_256X64X64_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 15)
                ticker += Sorter.obj_TEAM_BLOCKER_256X64X64_A

            elif str({object['itemId']}).find("1316554231") == True:
                #Team Blocker 2x2x2
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_2X2X2+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 16)
                ticker += Sorter.obj_TEAM_BLOCKER_2X2X2

            elif str({object['itemId']}).find("-512312831") == True:
                #Team Blocker 32x2x16
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_32X2X16+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 17)
                ticker += Sorter.obj_TEAM_BLOCKER_32X2X16

            elif str({object['itemId']}).find("-410788533") == True:
                #Team Blocker 32x32x16
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_32X32X16+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 18)
                ticker += Sorter.obj_TEAM_BLOCKER_32X32X16

            elif str({object['itemId']}).find("928931228") == True:
                #Team Blocker 32x32x32
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_32X32X32+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 19)
                ticker += Sorter.obj_TEAM_BLOCKER_32X32X32

            elif str({object['itemId']}).find("1337005876") == True:
                #Team Blocker 32x8x8
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_32X8X8+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 20)
                ticker += Sorter.obj_TEAM_BLOCKER_32X8X8

            elif str({object['itemId']}).find("-68300803") == True:
                #Team Blocker 32x8x8 A
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_32X8X8_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 21)
                ticker += Sorter.obj_TEAM_BLOCKER_32X8X8_A

            elif str({object['itemId']}).find("1735640563") == True:
                #Team Blocker 4x4x4
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_4X4X4+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 22)
                ticker += Sorter.obj_TEAM_BLOCKER_4X4X4

            elif str({object['itemId']}).find("1032218150") == True:
                #Team Blocker 64x16x16
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_64X16X16+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 23)
                ticker += Sorter.obj_TEAM_BLOCKER_64X16X16

            elif str({object['itemId']}).find("812349883") == True:
                #Team Blocker 64x16x16 A
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_64X16X16_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 24)
                ticker += Sorter.obj_TEAM_BLOCKER_64X16X16_A

            elif str({object['itemId']}).find("672283073") == True:
                #Team Blocker 64x2x32
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_64X2X32+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 25)
                ticker += Sorter.obj_TEAM_BLOCKER_64X2X32

            elif str({object['itemId']}).find("407729377") == True:
                #Team Blocker 64x32x32
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_64X32X32+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 26)
                ticker += Sorter.obj_TEAM_BLOCKER_64X32X32

            elif str({object['itemId']}).find("-1101324062") == True:
                #Team Blocker 64x64x64
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_64X64X64+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 27)
                ticker += Sorter.obj_TEAM_BLOCKER_64X64X64

            elif str({object['itemId']}).find("-1210852217") == True:
                #Team Blocker 8x2x2
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_8X2X2+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 28)
                ticker += Sorter.obj_TEAM_BLOCKER_8X2X2

            elif str({object['itemId']}).find("668419691") == True:
                #Team Blocker 8x2x2 A
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_8X2X2_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 29)
                ticker += Sorter.obj_TEAM_BLOCKER_8X2X2_A

            elif str({object['itemId']}).find("-1302862255") == True:
                #Team Blocker 8x2x4
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_8X2X4+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 30)
                ticker += Sorter.obj_TEAM_BLOCKER_8X2X4

            elif str({object['itemId']}).find("1321973632") == True:
                #Team Blocker 8x32x4
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_8X32X4+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 31)
                ticker += Sorter.obj_TEAM_BLOCKER_8X32X4

            elif str({object['itemId']}).find("-1868367315") == True:
                #Team Blocker 8x8x8
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_BLOCKER_8X8X8+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 4, 4, 32)
                ticker += Sorter.obj_TEAM_BLOCKER_8X8X8
            ## Universal Blockers 5
            ## Vehicle Blockers 6

            # Decals 5
            ## Building Signage 1
            ## Forerunner 2
            ## Letters 3
            ## Numbered Symbols 4
            ## Numbers 5
            ## UNSC 6

            # FX 6
            ## Ambient Life 1
            ## Atmospheric 2
            ## Energy 3
            ## Explosions 4
            ## Fire 5
            ## General 6
            ## Holograms 7
            ## Lens Flares 8
            ## Light Rays 9
            ## Liquids 10
            ## Smoke 11
            ## Sparks 12

            # Gameplay 7
            ## AI 1
            ## Audio 2
            ## Equipment 3
            ## Game Modes 4
            ## Launchers / Lifts 5
            ## Match Flow 6
            elif str({object['itemId']}).find("1980827929") == True:
                #Map Intro Camera
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_MAP_INTRO_CAMERA+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 6, 0)
                ticker += Sorter.obj_MAP_INTRO_CAMERA

            elif str({object['itemId']}).find("1006238451") == True:
                #Team Intro Arrow Front
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_INTRO_ARROW_FRONT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 6, 1)
                ticker += Sorter.obj_TEAM_INTRO_ARROW_FRONT

            elif str({object['itemId']}).find("-173177076") == True:
                #Team Intro Line Left
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_INTRO_LINE_LEFT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 6, 2)
                ticker += Sorter.obj_TEAM_INTRO_LINE_LEFT

            elif str({object['itemId']}).find("1747684183") == True:
                #Team Intro Line Right
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_TEAM_INTRO_LINE_RIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 6, 3)
                ticker += Sorter.obj_TEAM_INTRO_LINE_RIGHT

            elif str({object['itemId']}).find("298581842") == True:
                #Winning Team Outro
                mirvTranslator.objTranslationNoScale(sorted_item_list[ticker:Sorter.obj_WINNING_TEAM_OUTRO+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 6, 4)
                ticker += Sorter.obj_WINNING_TEAM_OUTRO
            ## Nav Mesh 7
            ## Player Spawning 8
            elif str({object['itemId']}).find("-361555940") == True:
                #Initial Spawn
                mirvTranslator.objTranslationStartsFixedNoScale(sorted_item_list[ticker:Sorter.obj_INITIAL_SPAWN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 8, 1)
                ticker += Sorter.obj_INITIAL_SPAWN

            elif str({object['itemId']}).find("-1533673853") == True:
                #Respawn Point
                mirvTranslator.objTranslationStartsFixedNoScale(sorted_item_list[ticker:Sorter.obj_RESPAWN_POINT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 8, 2)
                ticker += Sorter.obj_RESPAWN_POINT
            ## Sandbox 9
            ## Scripting 10
            ## Teleporters 11
            ## Vehicles 12 
            ## Vehicles - Damaged 13
            elif str({object['itemId']}).find("-1410050408") == True:
                #Ghost - Damaged
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_GHOST_DAMAGED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 13, 0)
                ticker += Sorter.obj_GHOST_DAMAGED

            elif str({object['itemId']}).find("641016943") == True:
                #Warthog - Damaged
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WARTHOG_DAMAGED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 7, 13, 1)
                ticker += Sorter.obj_WARTHOG_DAMAGED
            ## Volumes 14 
            ## Weapon Spawners 15
            ## Weapons 16

            # Halo Design Set 8
            ## Columns 1
            elif str({object['itemId']}).find("-1108230827") == True:
                #2x2 Round Column C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_2_X_2_ROUND_COLUMN_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 0)
                ticker += Sorter.obj_2_X_2_ROUND_COLUMN_C

            elif str({object['itemId']}).find("-885874693") == True:
                #2x2 Round Column D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_2_X_2_ROUND_COLUMN_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 1)
                ticker += Sorter.obj_2_X_2_ROUND_COLUMN_D

            elif str({object['itemId']}).find("2096053754") == True:
                #2x2 Square Column A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_2_X_2_SQUARE_COLUMN_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 2)
                ticker += Sorter.obj_2_X_2_SQUARE_COLUMN_A

            elif str({object['itemId']}).find("-1294229133") == True:
                #2x2 Square Column B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_2_X_2_SQUARE_COLUMN_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 3)
                ticker += Sorter.obj_2_X_2_SQUARE_COLUMN_B
            
            elif str({object['itemId']}).find("-1422631181") == True:
                #4x4 Round Column C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_4_X_4_ROUND_COLUMN_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 4)
                ticker += Sorter.obj_4_X_4_ROUND_COLUMN_C

            elif str({object['itemId']}).find("1947532949") == True:
                #4x4 Round Column D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_4_X_4_ROUND_COLUMN_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 5)
                ticker += Sorter.obj_4_X_4_ROUND_COLUMN_D

            elif str({object['itemId']}).find("2083372609") == True:
                #4x4 Square Column A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_4_X_4_SQUARE_COLUMN_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 6)
                ticker += Sorter.obj_4_X_4_SQUARE_COLUMN_A

            elif str({object['itemId']}).find("1607542385") == True:
                #4x4 Square Column B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_4_X_4_SQUARE_COLUMN_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 7)
                ticker += Sorter.obj_4_X_4_SQUARE_COLUMN_B
            
            elif str({object['itemId']}).find("1553385688") == True:
                #6x6 Round Column C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_6_X_6_ROUND_COLUMN_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 8)
                ticker += Sorter.obj_6_X_6_ROUND_COLUMN_C
            
            elif str({object['itemId']}).find("222107335") == True:
                #6x6 Round Column D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_6_X_6_ROUND_COLUMN_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 9)
                ticker += Sorter.obj_6_X_6_ROUND_COLUMN_D

            elif str({object['itemId']}).find("-446137873") == True:
                #6x6 Square Column A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_6_X_6_SQUARE_COLUMN_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 10)
                ticker += Sorter.obj_6_X_6_SQUARE_COLUMN_A

            elif str({object['itemId']}).find("727360123") == True:
                #6x6 Square Column B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_6_X_6_SQUARE_COLUMN_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 1, 11)
                ticker += Sorter.obj_6_X_6_SQUARE_COLUMN_B
            ## Columns MP 2
            ## Cover 3
            elif str({object['itemId']}).find("-1804795714") == True:
                #Ankle Cover Half Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANKLE_COVER_HALF_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 0)
                ticker += Sorter.obj_ANKLE_COVER_HALF_SIZE

            elif str({object['itemId']}).find("-157703089") == True:
                #Ankle Cover Quarter Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANKLE_COVER_QUARTER_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 1)
                ticker += Sorter.obj_ANKLE_COVER_QUARTER_SIZE
            
            elif str({object['itemId']}).find("2115878081") == True:
                #Full Cover Half Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FULL_COVER_HALF_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 2)
                ticker += Sorter.obj_FULL_COVER_HALF_SIZE

            elif str({object['itemId']}).find("-2030691315") == True:
                #Full Cover Standard Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FULL_COVER_STANDARD_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 3)
                ticker += Sorter.obj_FULL_COVER_STANDARD_SIZE

            elif str({object['itemId']}).find("286176533") == True:
                #Half Cover Half Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_HALF_COVER_HALF_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 4)
                ticker += Sorter.obj_HALF_COVER_HALF_SIZE

            elif str({object['itemId']}).find("1040169826") == True:
                #Half Cover Standard Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_HALF_COVER_STANDARD_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 5)
                ticker += Sorter.obj_HALF_COVER_STANDARD_SIZE
            
            elif str({object['itemId']}).find("902995208") == True:
                #Rock Half Cover A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROCK_HALF_COVER_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 6)
                ticker += Sorter.obj_ROCK_HALF_COVER_A
            
            elif str({object['itemId']}).find("2050581668") == True:
                #Rock Half Cover B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ROCK_HALF_COVER_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 3, 7)
                ticker += Sorter.obj_ROCK_HALF_COVER_B
            ## Cover MP 4
            ## Crates 5
            elif str({object['itemId']}).find("491753301") == True:
                #4.5x8 Crate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__4_5X8_CRATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 5, 0)
                ticker += Sorter.obj__4_5X8_CRATE
            
            elif str({object['itemId']}).find("253727975") == True:
                #4x4 Crate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__4X4_CRATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 5, 1)
                ticker += Sorter.obj__4X4_CRATE

            elif str({object['itemId']}).find("-1137520810") == True:
                #4x8 Crate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__4X8_CRATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 5, 2)
                ticker += Sorter.obj__4X8_CRATE

            elif str({object['itemId']}).find("355942414") == True:
                #8x16 Crate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__8X16_CRATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 5, 3)
                ticker += Sorter.obj__8X16_CRATE
            
            elif str({object['itemId']}).find("-89276352") == True:
                #8x8 Crate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__8X8_CRATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 5, 4)
                ticker += Sorter.obj__8X8_CRATE
            ## Crates MP 6
            ## Doorways 7
            elif str({object['itemId']}).find("-1843159215") == True:
                #Angled Double Doorway
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_DOUBLE_DOORWAY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 0)
                ticker += Sorter.obj_ANGLED_DOUBLE_DOORWAY

            elif str({object['itemId']}).find("-2102390651") == True:
                #Angled Single Doorway
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_SINGLE_DOORWAY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 1)
                ticker += Sorter.obj_ANGLED_SINGLE_DOORWAY
            
            elif str({object['itemId']}).find("1760817474") == True:
                #Curved Double Doorway
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_DOUBLE_DOORWAY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 2)
                ticker += Sorter.obj_CURVED_DOUBLE_DOORWAY
            
            elif str({object['itemId']}).find("759775548") == True:
                #Double Doorway
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_DOUBLE_DOORWAY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 3)
                ticker += Sorter.obj_DOUBLE_DOORWAY

            elif str({object['itemId']}).find("-983151539") == True:
                #Forerunner Doorway
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_DOORWAY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 4)
                ticker += Sorter.obj_FORERUNNER_DOORWAY

            elif str({object['itemId']}).find("492327815") == True:
                #Forerunner Doorway Wide
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_DOORWAY_WIDE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 5)
                ticker += Sorter.obj_FORERUNNER_DOORWAY_WIDE
            
            elif str({object['itemId']}).find("652937498") == True:
                #Single Doorway A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SINGLE_DOORWAY_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 6)
                ticker += Sorter.obj_SINGLE_DOORWAY_A

            elif str({object['itemId']}).find("1989569474") == True:
                #Single Doorway B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SINGLE_DOORWAY_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 7, 7)
                ticker += Sorter.obj_SINGLE_DOORWAY_B
            ## Doorways MP 8
            ## Floors 9
            elif str({object['itemId']}).find("2119916132") == True:
                #Floor Angled Standard A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_ANGLED_STANDARD_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 9, 0)
                ticker += Sorter.obj_FLOOR_ANGLED_STANDARD_A

            elif str({object['itemId']}).find("471557513") == True:
                #Fllor Angled Standard B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_ANGLED_STANDARD_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 9, 1)
                ticker += Sorter.obj_FLOOR_ANGLED_STANDARD_B

            elif str({object['itemId']}).find("-1554062464") == True:
                #Floor Half A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_HALF_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 9, 2)
                ticker += Sorter.obj_FLOOR_HALF_A
            
            elif str({object['itemId']}).find("-319219211") == True:
                #Floor Half B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_HALF_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 9, 3)
                ticker += Sorter.obj_FLOOR_HALF_B

            elif str({object['itemId']}).find("1561437000") == True:
                #Floor Quadruple Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_QUADRUPLE_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 9, 4)
                ticker += Sorter.obj_FLOOR_QUADRUPLE_SIZE

            elif str({object['itemId']}).find("796754322") == True:
                #Floor Standard
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOR_STANDARD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 9, 5)
                ticker += Sorter.obj_FLOOR_STANDARD
            ## Floors MP 10
            ## Railings 11
            elif str({object['itemId']}).find("2140930404") == True:
                #Curved Railing Half Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_RAILING_HALF_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 11, 0)
                ticker += Sorter.obj_CURVED_RAILING_HALF_SIZE
            
            elif str({object['itemId']}).find("-1335452897") == True:
                #Curved Railing Standard Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_RAILING_STANDARD_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 11, 1)
                ticker += Sorter.obj_CURVED_RAILING_STANDARD_SIZE

            elif str({object['itemId']}).find("-947456082") == True:
                #Railing Half Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RAILING_HALF_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 11, 2)
                ticker += Sorter.obj_RAILING_HALF_SIZE

            elif str({object['itemId']}).find("1635203824") == True:
                #Railing Standard Size
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RAILING_STANDARD_SIZE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 11, 3)
                ticker += Sorter.obj_RAILING_STANDARD_SIZE
            ## Railings MP 12
            ## Ramps 13
            elif str({object['itemId']}).find("-588839424") == True:
                #1 Over 3 Ramp Eighth A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_EIGHTH_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 0)
                ticker += Sorter.obj__1_OVER_3_RAMP_EIGHTH_A

            elif str({object['itemId']}).find("908393824") == True:
                #1 Over 3 Ramp Eighth B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_EIGHTH_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 1)
                ticker += Sorter.obj__1_OVER_3_RAMP_EIGHTH_B
            
            elif str({object['itemId']}).find("-1844206092") == True:
                #1 Over 3 Ramp Half A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_HALF_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 2)
                ticker += Sorter.obj__1_OVER_3_RAMP_HALF_A

            elif str({object['itemId']}).find("707549041") == True:
                #1 Over 3 Ramp Half B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_HALF_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 3)
                ticker += Sorter.obj__1_OVER_3_RAMP_HALF_B
            
            elif str({object['itemId']}).find("715160887") == True:
                #1 Over 3 Ramp Half C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_HALF_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 4)
                ticker += Sorter.obj__1_OVER_3_RAMP_HALF_C

            elif str({object['itemId']}).find("-1765693041") == True:
                #1 Over 3 Ramp Quarter
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_QUARTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 5)
                ticker += Sorter.obj__1_OVER_3_RAMP_QUARTER
            
            elif str({object['itemId']}).find("-984668480") == True:
                #1 Over 3 Ramp Sixteenth
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_SIXTEENTH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 6)
                ticker += Sorter.obj__1_OVER_3_RAMP_SIXTEENTH

            elif str({object['itemId']}).find("468997533") == True:
                #1 Over 3 Ramp Standard A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_STANDARD_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 7)
                ticker += Sorter.obj__1_OVER_3_RAMP_STANDARD_A

            elif str({object['itemId']}).find("1765455307") == True:
                #1 Over 3 Ramp Standard B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_3_RAMP_STANDARD_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 8)
                ticker += Sorter.obj__1_OVER_3_RAMP_STANDARD_B

            elif str({object['itemId']}).find("1461903299") == True:
                #1 Over 4 Ramp Half A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_4_RAMP_HALF_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 9)
                ticker += Sorter.obj__1_OVER_4_RAMP_HALF_A

            elif str({object['itemId']}).find("-152113334") == True:
                #1 Over 4 Ramp Half B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj__1_OVER_4_RAMP_HALF_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 10)
                ticker += Sorter.obj__1_OVER_4_RAMP_HALF_B
            
            elif str({object['itemId']}).find("1969407375") == True:
                #Corner Ramp Eighth A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CORNER_RAMP_EIGHTH_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only,  8, 13, 11)
                ticker += Sorter.obj_CORNER_RAMP_EIGHTH_A

            elif str({object['itemId']}).find("1451712685") == True:
                #Corner Ramp Eighth B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CORNER_RAMP_EIGHTH_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 12)
                ticker += Sorter.obj_CORNER_RAMP_EIGHTH_B
            
            elif str({object['itemId']}).find("-2065727303") == True:
                #Curved Ramp Standard Left
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_RAMP_STANDARD_LEFT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 13)
                ticker += Sorter.obj_CURVED_RAMP_STANDARD_LEFT

            elif str({object['itemId']}).find("-191674833") == True:
                #Curved Ramp Standard Right
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_RAMP_STANDARD_RIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 14)
                ticker += Sorter.obj_CURVED_RAMP_STANDARD_RIGHT

            elif str({object['itemId']}).find("1150132444") == True:
                #Four Way Ramp Eighth
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FOUR_WAY_RAMP_EIGHTH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 13, 15)
                ticker += Sorter.obj_FOUR_WAY_RAMP_EIGHTH
            ## Ramps MP 14
            ## Scale Objects 15
            elif str({object['itemId']}).find("2062928760") == True:
                #Player Scale Object
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PLAYER_SCALE_OBJECT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 15, 0)
                ticker += Sorter.obj_PLAYER_SCALE_OBJECT
            ## Walls 16
            elif str({object['itemId']}).find("1168502040") == True:
                #Angle Wall Half
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLE_WALL_HALF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 0)
                ticker += Sorter.obj_ANGLE_WALL_HALF

            elif str({object['itemId']}).find("-612639225") == True:
                #Angled Corner Wall Standard
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_CORNER_WALL_STANDARD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 1)
                ticker += Sorter.obj_ANGLED_CORNER_WALL_STANDARD
            
            elif str({object['itemId']}).find("691693133") == True:
                #Angled Wall Double Window A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_DOUBLE_WINDOW_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 2)
                ticker += Sorter.obj_ANGLED_WALL_DOUBLE_WINDOW_A

            elif str({object['itemId']}).find("1103502387") == True:
                #Angled Wall Double Window B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_DOUBLE_WINDOW_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 3)
                ticker += Sorter.obj_ANGLED_WALL_DOUBLE_WINDOW_B

            elif str({object['itemId']}).find("1383537765") == True:
                #Angled Wall Double Window C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_DOUBLE_WINDOW_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 4)
                ticker += Sorter.obj_ANGLED_WALL_DOUBLE_WINDOW_C

            elif str({object['itemId']}).find("-41069292") == True:
                #Angled Wall Standard A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_STANDARD_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 5)
                ticker += Sorter.obj_ANGLED_WALL_STANDARD_A

            elif str({object['itemId']}).find("1361150846") == True:
                #Angled Wall Standard B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_STANDARD_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 6)
                ticker += Sorter.obj_ANGLED_WALL_STANDARD_B

            elif str({object['itemId']}).find("-979944560") == True:
                #Angled Wall Window A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_WINDOW_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 7)
                ticker += Sorter.obj_ANGLED_WALL_WINDOW_A

            elif str({object['itemId']}).find("-147813598") == True:
                #Angled Wall Window B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_WINDOW_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 8)
                ticker += Sorter.obj_ANGLED_WALL_WINDOW_B

            elif str({object['itemId']}).find("1416644323") == True:
                #Angled Wall Window C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_ANGLED_WALL_WINDOW_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 9)
                ticker += Sorter.obj_ANGLED_WALL_WINDOW_C

            elif str({object['itemId']}).find("-173471027") == True:
                #Corner Wall Standard
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CORNER_WALL_STANDARD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 10)
                ticker += Sorter.obj_CORNER_WALL_STANDARD
            
            elif str({object['itemId']}).find("-936420252") == True:
                #Curved Double Window Wall A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_DOUBLE_WINDOW_WALL_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 11)
                ticker += Sorter.obj_CURVED_DOUBLE_WINDOW_WALL_A

            elif str({object['itemId']}).find("1662288531") == True:
                #Curved Double Window Wall B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_DOUBLE_WINDOW_WALL_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 12)
                ticker += Sorter.obj_CURVED_DOUBLE_WINDOW_WALL_B

            elif str({object['itemId']}).find("-341801782") == True:
                #Curved Wall Double
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_WALL_DOUBLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 13)
                ticker += Sorter.obj_CURVED_WALL_DOUBLE

            elif str({object['itemId']}).find("-960331706") == True:
                #Curved Wall Standard
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_WALL_STANDARD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 14)
                ticker += Sorter.obj_CURVED_WALL_STANDARD

            elif str({object['itemId']}).find("-1332366101") == True:
                #Curved Wall Triple
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_CURVED_WALL_TRIPLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 15)
                ticker += Sorter.obj_CURVED_WALL_TRIPLE

            elif str({object['itemId']}).find("101094355") == True:
                #Wall Cube Angled
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_CUBE_ANGLED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 16)
                ticker += Sorter.obj_WALL_CUBE_ANGLED

            elif str({object['itemId']}).find("-2128852445") == True:
                #Wall Cube Corner Angled
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_CUBE_CORNER_ANGLED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 17)
                ticker += Sorter.obj_WALL_CUBE_CORNER_ANGLED

            elif str({object['itemId']}).find("-1168178900") == True:
                #Wall Cube Standard
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_CUBE_STANDARD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 18)
                ticker += Sorter.obj_WALL_CUBE_STANDARD

            elif str({object['itemId']}).find("1662815138") == True:
                #Wall Double Window A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_DOUBLE_WINDOW_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 19)
                ticker += Sorter.obj_WALL_DOUBLE_WINDOW_A

            elif str({object['itemId']}).find("-2011335511") == True:
                #Wall Double Window B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_DOUBLE_WINDOW_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 20)
                ticker += Sorter.obj_WALL_DOUBLE_WINDOW_B

            elif str({object['itemId']}).find("-1513962159") == True:
                #Wall Half
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_HALF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 21)
                ticker += Sorter.obj_WALL_HALF
            
            elif str({object['itemId']}).find("1047093426") == True:
                #Wall Standard A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_STANDARD_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 22)
                ticker += Sorter.obj_WALL_STANDARD_A

            elif str({object['itemId']}).find("-1459663496") == True:
                #Wall Standard B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_STANDARD_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 23)
                ticker += Sorter.obj_WALL_STANDARD_B

            elif str({object['itemId']}).find("-725006759") == True:
                #Wall Window A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_WINDOW_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 24)
                ticker += Sorter.obj_WALL_WINDOW_A

            elif str({object['itemId']}).find("1064263013") == True:
                #Wall Window B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WALL_WINDOW_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 8, 16, 25)
                ticker += Sorter.obj_WALL_WINDOW_B
            ## Walls MP 17

            # Lights 9
            ## Forerunner Light 1
            ## Forerunner Light MP 2
            ## Forerunner No Light 3
            elif str({object['itemId']}).find("-1477845888") == True:
                #Forerunner Block Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BLOCK_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 0)
                ticker += Sorter.obj_FORERUNNER_BLOCK_LIGHT

            elif str({object['itemId']}).find("-2095885886") == True:
                #Forerunner Floor Trim Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FLOOR_TRIM_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 1)
                ticker += Sorter.obj_FORERUNNER_FLOOR_TRIM_LIGHT

            elif str({object['itemId']}).find("-1778719387") == True:
                #Forerunner Gravlift Receiver
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_GRAVLIFT_RECEIVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 2)
                ticker += Sorter.obj_FORERUNNER_GRAVLIFT_RECEIVER

            elif str({object['itemId']}).find("2049716768") == True:
                #Forerunner Ledge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LEDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 3)
                ticker += Sorter.obj_FORERUNNER_LEDGE

            elif str({object['itemId']}).find("474402863") == True:
                #Forerunner Light A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 4)
                ticker += Sorter.obj_FORERUNNER_LIGHT_A

            elif str({object['itemId']}).find("1501228877") == True:
                #Forerunner Light B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 5)
                ticker += Sorter.obj_FORERUNNER_LIGHT_B

            elif str({object['itemId']}).find("-1373672453") == True:
                #Forerunner Light C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 6)
                ticker += Sorter.obj_FORERUNNER_LIGHT_C
                
            elif str({object['itemId']}).find("174850678") == True:
                #Forerunner Light D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 7)
                ticker += Sorter.obj_FORERUNNER_LIGHT_D

            elif str({object['itemId']}).find("-838595300") == True:
                #Forerunner Light E
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_E+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 8)
                ticker += Sorter.obj_FORERUNNER_LIGHT_E

            elif str({object['itemId']}).find("2036668565") == True:
                #Forerunner Light F
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_F+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 9)
                ticker += Sorter.obj_FORERUNNER_LIGHT_F

            elif str({object['itemId']}).find("2025848228") == True:
                #Forerunner Light G
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_G+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 10)
                ticker += Sorter.obj_FORERUNNER_LIGHT_G

            elif str({object['itemId']}).find("201659451") == True:
                #Forerunner Light H
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_H+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 11)
                ticker += Sorter.obj_FORERUNNER_LIGHT_H

            elif str({object['itemId']}).find("62642658") == True:
                #Forerunner Support Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 12)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_LIGHT

            elif str({object['itemId']}).find("-1185462116") == True:
                #Forerunner Support Pillar
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_PILLAR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 13)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_PILLAR

            elif str({object['itemId']}).find("628448986") == True:
                #Forerunner Weapon Post A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_WEAPON_POST_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 3, 14)
                ticker += Sorter.obj_FORERUNNER_WEAPON_POST_A
            ## Forerunner No Light MP 4
            elif str({object['itemId']}).find("-605177168") == True:
                #Forerunner Block Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BLOCK_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 0)
                ticker += Sorter.obj_FORERUNNER_BLOCK_LIGHT_MP

            elif str({object['itemId']}).find("-826269345") == True:
                #Forerunner Ledge MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LEDGE_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 1)
                ticker += Sorter.obj_FORERUNNER_LEDGE_MP

            elif str({object['itemId']}).find("-244732778") == True:
                #Forerunner Light A MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_A_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 2)
                ticker += Sorter.obj_FORERUNNER_LIGHT_A_MP

            elif str({object['itemId']}).find("1383245021") == True:
                #Forerunner Light B MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_B_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 3)
                ticker += Sorter.obj_FORERUNNER_LIGHT_B_MP

            elif str({object['itemId']}).find("188391070") == True:
                #Forerunner Light C MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_C_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 4)
                ticker += Sorter.obj_FORERUNNER_LIGHT_C_MP

            elif str({object['itemId']}).find("-1193689671") == True:
                #Forerunner Light D MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_D_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 5)
                ticker += Sorter.obj_FORERUNNER_LIGHT_D_MP

            elif str({object['itemId']}).find("-858408105") == True:
                #Forerunner Light E MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_E_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 6)
                ticker += Sorter.obj_FORERUNNER_LIGHT_E_MP

            elif str({object['itemId']}).find("1639207829") == True:
                #Forerunner Light F MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_F_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 7)
                ticker += Sorter.obj_FORERUNNER_LIGHT_F_MP

            elif str({object['itemId']}).find("2065967474") == True:
                #Forerunner Light G MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_G_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 8)
                ticker += Sorter.obj_FORERUNNER_LIGHT_G_MP

            elif str({object['itemId']}).find("861961961") == True:
                #Forerunner Light H MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_LIGHT_H_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 9)
                ticker += Sorter.obj_FORERUNNER_LIGHT_H_MP

            elif str({object['itemId']}).find("523266499") == True:
                #Forerunner Support Pillar MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SUPPORT_PILLAR_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 4, 10)
                ticker += Sorter.obj_FORERUNNER_SUPPORT_PILLAR_MP
            ## Generic Light Objects 5
            ## UNSC Light 6
            ## UNSC Light MP 7
            ## UNSC No Light 8
            elif str({object['itemId']}).find("-2092865719") == True:
                #Exterior Wall w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_EXTERIOR_WALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 0)
                ticker += Sorter.obj_EXTERIOR_WALL_W_O_LIGHT

            elif str({object['itemId']}).find("-348792062") == True:
                #Flood Short w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOD_SHORT_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 1)
                ticker += Sorter.obj_FLOOD_SHORT_W_O_LIGHT

            elif str({object['itemId']}).find("-665722556") == True:
                #Flood Tall w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOD_TALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 2)
                ticker += Sorter.obj_FLOOD_TALL_W_O_LIGHT

            elif str({object['itemId']}).find("288063728") == True:
                #Fluorescent Covered Trim Dynamic w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_COVERED_TRIM_DYNAMIC_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 3)
                ticker += Sorter.obj_FLUORESCENT_COVERED_TRIM_DYNAMIC_W_O_LIGHT

            elif str({object['itemId']}).find("272492850") == True:
                #Fluorescent Covered Trim Small w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_COVERED_TRIM_SMALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 4)
                ticker += Sorter.obj_FLUORESCENT_COVERED_TRIM_SMALL_W_O_LIGHT

            elif str({object['itemId']}).find("-450394949") == True:
                #Fluorescent Covered Trim w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_COVERED_TRIM_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 5)
                ticker += Sorter.obj_FLUORESCENT_COVERED_TRIM_W_O_LIGHT

            elif str({object['itemId']}).find("596491061") == True:
                #Fluorescent Covered w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_COVERED_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 6)
                ticker += Sorter.obj_FLUORESCENT_COVERED_W_O_LIGHT

            elif str({object['itemId']}).find("1332895936") == True:
                #Fluorescent Exposed Extra Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_EXTRA_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 7)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_EXTRA_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("1150542342") == True:
                #Fluorescent Exposed Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 8)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("-811265781") == True:
                #Fluorescent Exposed Med w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_MED_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 9)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_MED_W_O_LIGHT

            elif str({object['itemId']}).find("263752497") == True:
                #Fluorescent Exposed Small w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_SMALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 10)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_SMALL_W_O_LIGHT

            elif str({object['itemId']}).find("1088075689") == True:
                #Fluorescent Exposed w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 11)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_W_O_LIGHT

            elif str({object['itemId']}).find("-1787638182") == True:
                #Flush Fluorescent Covered Extra Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUSH_FLUORESCENT_COVERED_EXTRA_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 12)
                ticker += Sorter.obj_FLUSH_FLUORESCENT_COVERED_EXTRA_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("-394843946") == True:
                #Flush Fluorescent Covered Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUSH_FLUORESCENT_COVERED_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 13)
                ticker += Sorter.obj_FLUSH_FLUORESCENT_COVERED_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("699771076") == True:
                #Flush Fluorescent Covered Med w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUSH_FLUORESCENT_COVERED_MED_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 14)
                ticker += Sorter.obj_FLUSH_FLUORESCENT_COVERED_MED_W_O_LIGHT

            elif str({object['itemId']}).find("1154362337") == True:
                #Interior Wall Covered w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_INTERIOR_WALL_COVERED_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 15)
                ticker += Sorter.obj_INTERIOR_WALL_COVERED_W_O_LIGHT

            elif str({object['itemId']}).find("-2142835366") == True:
                #Interior Wall Exposed w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_INTERIOR_WALL_EXPOSED_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 16)
                ticker += Sorter.obj_INTERIOR_WALL_EXPOSED_W_O_LIGHT

            elif str({object['itemId']}).find("2075366164") == True:
                #Multibulb Three Bulb Grill w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_THREE_BULB_GRILL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 17)
                ticker += Sorter.obj_MULTIBULB_THREE_BULB_GRILL_W_O_LIGHT

            elif str({object['itemId']}).find("-769693198") == True:
                #Multibulb Three Bulb w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_THREE_BULB_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 18)
                ticker += Sorter.obj_MULTIBULB_THREE_BULB_W_O_LIGHT

            elif str({object['itemId']}).find("-361590128") == True:
                #Multibulb Two Bulb Grill w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_TWO_BULB_GRILL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 19)
                ticker += Sorter.obj_MULTIBULB_TWO_BULB_GRILL_W_O_LIGHT

            elif str({object['itemId']}).find("-1789041313") == True:
                #Multibulb Two Bulb w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_TWO_BULB_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 20)
                ticker += Sorter.obj_MULTIBULB_TWO_BULB_W_O_LIGHT

            elif str({object['itemId']}).find("1847791240") == True:
                #Overhead Mount Double
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_MOUNT_DOUBLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 21)
                ticker += Sorter.obj_OVERHEAD_MOUNT_DOUBLE

            elif str({object['itemId']}).find("1781063909") == True:
                #Overhead Mount Quad
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_MOUNT_QUAD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 22)
                ticker += Sorter.obj_OVERHEAD_MOUNT_QUAD

            elif str({object['itemId']}).find("1435492872") == True:
                #Overhead Mount Single
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_MOUNT_SINGLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 23)
                ticker += Sorter.obj_OVERHEAD_MOUNT_SINGLE

            elif str({object['itemId']}).find("-224760473") == True:
                #Overhead Round Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_ROUND_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 24)
                ticker += Sorter.obj_OVERHEAD_ROUND_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("-792752403") == True:
                #Panel Flush Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_FLUSH_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 25)
                ticker += Sorter.obj_PANEL_FLUSH_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("959658482") == True:
                #Panel Flush Small w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_FLUSH_SMALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 26)
                ticker += Sorter.obj_PANEL_FLUSH_SMALL_W_O_LIGHT

            elif str({object['itemId']}).find("1775952448") == True:
                #Panel Large w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_LARGE_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 27)
                ticker += Sorter.obj_PANEL_LARGE_W_O_LIGHT

            elif str({object['itemId']}).find("-571550801") == True:
                #Panel Small w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_SMALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 28)
                ticker += Sorter.obj_PANEL_SMALL_W_O_LIGHT

            elif str({object['itemId']}).find("-1428715228") == True:
                #Puck Round Small w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PUCK_ROUND_SMALL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 29)
                ticker += Sorter.obj_PUCK_ROUND_SMALL_W_O_LIGHT

            elif str({object['itemId']}).find("1593117566") == True:
                #Puck Round w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PUCK_ROUND_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 30)
                ticker += Sorter.obj_PUCK_ROUND_W_O_LIGHT

            elif str({object['itemId']}).find("-689110961") == True:
                #Spot Round Straight w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPOT_ROUND_STRAIGHT_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 31)
                ticker += Sorter.obj_SPOT_ROUND_STRAIGHT_W_O_LIGHT

            elif str({object['itemId']}).find("404331836") == True:
                #Street Light w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_STREET_LIGHT_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 32)
                ticker += Sorter.obj_STREET_LIGHT_W_O_LIGHT

            elif str({object['itemId']}).find("-736909390") == True:
                #Traffic Lights
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_TRAFFIC_LIGHTS+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 33)
                ticker += Sorter.obj_TRAFFIC_LIGHTS

            elif str({object['itemId']}).find("1618136600") == True:
                #Work Light Grill w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_GRILL_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 34)
                ticker += Sorter.obj_WORK_LIGHT_GRILL_W_O_LIGHT

            elif str({object['itemId']}).find("648983616") == True:
                #Work Light Mount Large
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_LARGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 35)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_LARGE

            elif str({object['itemId']}).find("-1580981655") == True:
                #Work Light Mount Small
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_SMALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 36)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_SMALL

            elif str({object['itemId']}).find("666368264") == True:
                #Work Light Mount Tripod
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_TRIPOD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 37)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_TRIPOD

            elif str({object['itemId']}).find("1697274986") == True:
                #Work Light Mount Wall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_WALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 38)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_WALL

            elif str({object['itemId']}).find("-786160843") == True:
                #Work Light Trailer
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_TRAILER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 39)
                ticker += Sorter.obj_WORK_LIGHT_TRAILER

            elif str({object['itemId']}).find("-1633160588") == True:
                #Work Light w/o Light
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_W_O_LIGHT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 8, 40)
                ticker += Sorter.obj_WORK_LIGHT_W_O_LIGHT
            ## UNSC No Light MP 9
            elif str({object['itemId']}).find("-1505084120") == True:
                #Exterior Wall w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_EXTERIOR_WALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 0)
                ticker += Sorter.obj_EXTERIOR_WALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-306692525") == True:
                #Flood Short w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOD_SHORT_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 1)
                ticker += Sorter.obj_FLOOD_SHORT_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-2003059415") == True:
                #Flood Tall w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLOOD_TALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 2)
                ticker += Sorter.obj_FLOOD_TALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1431118831") == True:
                #Fluorescent Covered Trim Small w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_COVERED_TRIM_SMALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 3)
                ticker += Sorter.obj_FLUORESCENT_COVERED_TRIM_SMALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-342108257") == True:
                #Fluorescent Covered Trim w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_COVERED_TRIM_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 4)
                ticker += Sorter.obj_FLUORESCENT_COVERED_TRIM_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-1442398229") == True:
                #Fluorescent Exposed Extra Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_EXTRA_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 5)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_EXTRA_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("727666538") == True:
                #Fluorescent Exposed Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 6)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-29874442") == True:
                #Fluorescent Exposed Med w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_MED_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 7)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_MED_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1801576568") == True:
                #Fluorescent Exposed Small w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_SMALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 8)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_SMALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1260991046") == True:
                #Fluorescent Exposed w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUORESCENT_EXPOSED_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 9)
                ticker += Sorter.obj_FLUORESCENT_EXPOSED_W_O_LIGHT_MP

            elif str({object['itemId']}).find("909453265") == True:
                #Flush Fluorescent Covered Extra Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUSH_FLUORESCENT_COVERED_EXTRA_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 10)
                ticker += Sorter.obj_FLUSH_FLUORESCENT_COVERED_EXTRA_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1147018626") == True:
                #Flush Fluorescent Covered Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUSH_FLUORESCENT_COVERED_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 11)
                ticker += Sorter.obj_FLUSH_FLUORESCENT_COVERED_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("597808910") == True:
                #Flush Fluorescent Covered Med w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FLUSH_FLUORESCENT_COVERED_MED_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 12)
                ticker += Sorter.obj_FLUSH_FLUORESCENT_COVERED_MED_W_O_LIGHT_MP

            elif str({object['itemId']}).find("324830011") == True:
                #Interior Wall Covered w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_INTERIOR_WALL_COVERED_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 13)
                ticker += Sorter.obj_INTERIOR_WALL_COVERED_W_O_LIGHT_MP

            elif str({object['itemId']}).find("622918304") == True:
                #Interior Wall Exposed w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_INTERIOR_WALL_EXPOSED_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 14)
                ticker += Sorter.obj_INTERIOR_WALL_EXPOSED_W_O_LIGHT_MP

            elif str({object['itemId']}).find("164658352") == True:
                #Multibulb Three Bulb Grill w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_THREE_BULB_GRILL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 15)
                ticker += Sorter.obj_MULTIBULB_THREE_BULB_GRILL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-220644374") == True:
                #Multibulb Three Bulb w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_THREE_BULB_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 16)
                ticker += Sorter.obj_MULTIBULB_THREE_BULB_W_O_LIGHT_MP

            elif str({object['itemId']}).find("578404483") == True:
                #Multibulb Two Bulb Grill w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_TWO_BULB_GRILL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 17)
                ticker += Sorter.obj_MULTIBULB_TWO_BULB_GRILL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-442993746") == True:
                #Multibulb Two Bulb w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MULTIBULB_TWO_BULB_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 18)
                ticker += Sorter.obj_MULTIBULB_TWO_BULB_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1927012038") == True:
                #Overhead Mount Double MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_MOUNT_DOUBLE_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 19)
                ticker += Sorter.obj_OVERHEAD_MOUNT_DOUBLE_MP

            elif str({object['itemId']}).find("-1571274308") == True:
                #Overhead Mount Quad MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_MOUNT_QUAD_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 20)
                ticker += Sorter.obj_OVERHEAD_MOUNT_QUAD_MP

            elif str({object['itemId']}).find("-1220152662") == True:
                #Overhead Mount Single MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_MOUNT_SINGLE_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 21)
                ticker += Sorter.obj_OVERHEAD_MOUNT_SINGLE_MP

            elif str({object['itemId']}).find("1958275446") == True:
                #Overhead Round Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_OVERHEAD_ROUND_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 22)
                ticker += Sorter.obj_OVERHEAD_ROUND_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-1711294865") == True:
                #Panel Flush Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_FLUSH_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 23)
                ticker += Sorter.obj_PANEL_FLUSH_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("995417252") == True:
                #Panel Flush Small w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_FLUSH_SMALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 24)
                ticker += Sorter.obj_PANEL_FLUSH_SMALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-1577147684") == True:
                #Panel Large w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_LARGE_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 25)
                ticker += Sorter.obj_PANEL_LARGE_W_O_LIGHT_MP

            elif str({object['itemId']}).find("307008624") == True:
                #Panel Small w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_SMALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 26)
                ticker += Sorter.obj_PANEL_SMALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1247191702") == True:
                #Puck Round Small w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PUCK_ROUND_SMALL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 27)
                ticker += Sorter.obj_PUCK_ROUND_SMALL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("244260171") == True:
                #Puck Round w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PUCK_ROUND_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 28)
                ticker += Sorter.obj_PUCK_ROUND_W_O_LIGHT_MP

            elif str({object['itemId']}).find("679650438") == True:
                #Spot Round Straight w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SPOT_ROUND_STRAIGHT_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 29)
                ticker += Sorter.obj_SPOT_ROUND_STRAIGHT_W_O_LIGHT_MP

            elif str({object['itemId']}).find("179483038") == True:
                #Street Light w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_STREET_LIGHT_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 30)
                ticker += Sorter.obj_STREET_LIGHT_W_O_LIGHT_MP

            elif str({object['itemId']}).find("-1849988374") == True:
                #Work Light Grill w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_GRILL_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 31)
                ticker += Sorter.obj_WORK_LIGHT_GRILL_W_O_LIGHT_MP

            elif str({object['itemId']}).find("1273593611") == True:
                #Work Light Mount Large MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_LARGE_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 32)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_LARGE_MP

            elif str({object['itemId']}).find("2008437747") == True:
                #Work Light Mount Small MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_SMALL_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 33)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_SMALL_MP

            elif str({object['itemId']}).find("167736681") == True:
                #Work Light Mount Tripod MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_TRIPOD_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 34)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_TRIPOD_MP

            elif str({object['itemId']}).find("-1536593407") == True:
                #Work Light Mount Wall MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_MOUNT_WALL_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 35)
                ticker += Sorter.obj_WORK_LIGHT_MOUNT_WALL_MP

            elif str({object['itemId']}).find("272543426") == True:
                #Work Light Trailer MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_TRAILER_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 36)
                ticker += Sorter.obj_WORK_LIGHT_TRAILER_MP

            elif str({object['itemId']}).find("463162034") == True:
                #Work Light w/o Light MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WORK_LIGHT_W_O_LIGHT_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 9, 9, 37)
                ticker += Sorter.obj_WORK_LIGHT_W_O_LIGHT_MP
            # Primitives 10
            ## Blocks 1
            elif str({object['itemId']}).find("-340615357") == True:
                #Forerunner Block
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BLOCK+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 1, 1)
                ticker += Sorter.obj_FORERUNNER_BLOCK

            elif str({object['itemId']}).find("1759788903") == True:
                #Primitive Block
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_BLOCK+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 1, 2)
                ticker += Sorter.obj_PRIMITIVE_BLOCK

            elif str({object['itemId']}).find("-1076429309") == True:
                #UNSC Block
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_BLOCK+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 1, 3)
                ticker += Sorter.obj_UNSC_BLOCK
            ## Cones 2
            elif str({object['itemId']}).find("53527778") == True:
                #Forerunner Cone
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CONE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 2, 1)
                ticker += Sorter.obj_FORERUNNER_CONE

            elif str({object['itemId']}).find("-234187719") == True:
                #Primitive Cone
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_CONE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 2, 2)
                ticker += Sorter.obj_PRIMITIVE_CONE

            elif str({object['itemId']}).find("1354722998") == True:
                #UNSC Cone
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_CONE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 2, 3)
                ticker += Sorter.obj_UNSC_CONE
            ## Cylinders 3
            elif str({object['itemId']}).find("-945116642") == True:
                #Forerunner Cylinder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_CYLINDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 3, 1)
                ticker += Sorter.obj_FORERUNNER_CYLINDER

            elif str({object['itemId']}).find("728515706") == True:
                #Primitive Cylinder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_CYLINDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 3, 2)
                ticker += Sorter.obj_PRIMITIVE_CYLINDER

            elif str({object['itemId']}).find("1720205523") == True:
                #UNSC Cylinder
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_CYLINDER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 3, 3)
                ticker += Sorter.obj_UNSC_CYLINDER
            ## Pyramids 4
            elif str({object['itemId']}).find("-764178783") == True:
                #Forerunner Pyramid
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_PYRAMID+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 4, 1)
                ticker += Sorter.obj_FORERUNNER_PYRAMID

            elif str({object['itemId']}).find("1189747031") == True:
                #Primitive Pyramid
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_PYRAMID+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 4, 2)
                ticker += Sorter.obj_PRIMITIVE_PYRAMID

            elif str({object['itemId']}).find("-1822179569") == True:
                #UNSC Pyramid
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_PYRAMID+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 4, 3)
                ticker += Sorter.obj_UNSC_PYRAMID
            ## Rings 5
            elif str({object['itemId']}).find("-968540348") == True:
                #Forerunner Ring Eighth
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RING_EIGHTH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 4)
                ticker += Sorter.obj_FORERUNNER_RING_EIGHTH
                
            elif str({object['itemId']}).find("513213980") == True:
                #Forerunner Ring Full
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RING_FULL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 5)
                ticker += Sorter.obj_FORERUNNER_RING_FULL
                
            elif str({object['itemId']}).find("-1811390435") == True:
                #Forerunner Ring Half
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RING_HALF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 6)
                ticker += Sorter.obj_FORERUNNER_RING_HALF
                
            elif str({object['itemId']}).find("137154715") == True:
                #Forerunner Ring Quarter
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RING_QUARTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 7)
                ticker += Sorter.obj_FORERUNNER_RING_QUARTER

            elif str({object['itemId']}).find("-1706009392") == True:
                #Primitive Ring Eighth
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_RING_EIGHTH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 8)
                ticker += Sorter.obj_PRIMITIVE_RING_EIGHTH

            elif str({object['itemId']}).find("-1190828000") == True:
                #Primitive Ring Full
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_RING_FULL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 9)
                ticker += Sorter.obj_PRIMITIVE_RING_FULL

            elif str({object['itemId']}).find("-1298054065") == True:
                #Primitive Ring Half
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_RING_HALF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 10)
                ticker += Sorter.obj_PRIMITIVE_RING_HALF

            elif str({object['itemId']}).find("1875914002") == True:
                #Primitive Ring Quarter
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_RING_QUARTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 11)
                ticker += Sorter.obj_PRIMITIVE_RING_QUARTER

            elif str({object['itemId']}).find("-658815076") == True:
                #UNSC Ring Eighth
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_RING_EIGHTH+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 12)
                ticker += Sorter.obj_UNSC_RING_EIGHTH
                
            elif str({object['itemId']}).find("-906033151") == True:
                #UNSC Ring Full
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_RING_FULL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 13)
                ticker += Sorter.obj_UNSC_RING_FULL
                
            elif str({object['itemId']}).find("-1913644661") == True:
                #UNSC Ring Half
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_RING_HALF+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 14)
                ticker += Sorter.obj_UNSC_RING_HALF
                
            elif str({object['itemId']}).find("") == True:
                #UNSC Ring Quarter
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_RING_QUARTER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 5, 15)
                ticker += Sorter.obj_UNSC_RING_QUARTER
            ## Spheres 6
            elif str({object['itemId']}).find("398294344") == True:
                #Forerunner Sphere
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SPHERE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 6, 1)
                ticker += Sorter.obj_FORERUNNER_SPHERE

            elif str({object['itemId']}).find("1150182783") == True:
                #Primitive Sphere
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_SPHERE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 6, 2)
                ticker += Sorter.obj_PRIMITIVE_SPHERE

            elif str({object['itemId']}).find("-1121425050") == True:
                #UNSC Sphere
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_SPHERE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 6, 3)
                ticker += Sorter.obj_UNSC_SPHERE
            ## Trapezoids 7
            elif str({object['itemId']}).find("-1143152298") == True:
                #Forerunner Trapezoid
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TRAPEZOID+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 7, 1)
                ticker += Sorter.obj_FORERUNNER_TRAPEZOID

            elif str({object['itemId']}).find("1100028612") == True:
                #Primitive Trapezoid
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_TRAPEZOID+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 7, 2)
                ticker += Sorter.obj_PRIMITIVE_TRAPEZOID

            elif str({object['itemId']}).find("-966446051") == True:
                #UNSC Trapezoid
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_TRAPEZOID+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 7, 3)
                ticker += Sorter.obj_UNSC_TRAPEZOID
            ## Triangles 8
            elif str({object['itemId']}).find("-809878135") == True:
                #Forerunner Triangle
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_TRIANGLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 8, 1)
                ticker += Sorter.obj_FORERUNNER_TRIANGLE

            elif str({object['itemId']}).find("-1185205223") == True:
                #Primitive Triangle
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PRIMITIVE_TRIANGLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 8, 2)
                ticker += Sorter.obj_PRIMITIVE_TRIANGLE

            elif str({object['itemId']}).find("-400055490") == True:
                #UNSC Triangle
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_TRIANGLE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 10, 8, 3)
                ticker += Sorter.obj_UNSC_TRIANGLE

            # Props 11
            ## Sports 1
            ## Summertime 2
            elif str({object['itemId']}).find("892184937") == True:
                #Beach Chair
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BEACH_CHAIR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 11, 2, 0)
                ticker += Sorter.obj_BEACH_CHAIR

            elif str({object['itemId']}).find("1496044122") == True:
                #Beach Parasol
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BEACH_PARASOL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 11, 2, 1)
                ticker += Sorter.obj_BEACH_PARASOL

            elif str({object['itemId']}).find("-1428538952") == True:
                #Party Cup
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PARTY_CUP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 11, 2, 2)
                ticker += Sorter.obj_PARTY_CUP

            elif str({object['itemId']}).find("1070451058") == True:
                #Surfboard
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_SURFBOARD+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 11, 2, 3)
                ticker += Sorter.obj_SURFBOARD
                ## Toys 3

            # Structures 12
            ## Beams 1
            elif str({object['itemId']}).find("-1074641530") == True:
                #Forerunner Beam
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 0)
                ticker += Sorter.obj_FORERUNNER_BEAM

            elif str({object['itemId']}).find("415085333") == True:
                #Forerunner Beam Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 1)
                ticker += Sorter.obj_FORERUNNER_BEAM_CORNER

            elif str({object['itemId']}).find("1237066345") == True:
                #Forerunner Beam T Joint
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_T_JOINT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 2)
                ticker += Sorter.obj_FORERUNNER_BEAM_T_JOINT

            elif str({object['itemId']}).find("667736010") == True:
                #Forerunner Beam X Joint
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_BEAM_X_JOINT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 3)
                ticker += Sorter.obj_FORERUNNER_BEAM_X_JOINT

            elif str({object['itemId']}).find("-686604533") == True:
                #UNSC Beam
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_BEAM+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 4)
                ticker += Sorter.obj_UNSC_BEAM

            elif str({object['itemId']}).find("-758649770") == True:
                #UNSC Beam Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_BEAM_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 5)
                ticker += Sorter.obj_UNSC_BEAM_CORNER

            elif str({object['itemId']}).find("1446507005") == True:
                #UNSC Beam T Joint
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_BEAM_T_JOINT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 6)
                ticker += Sorter.obj_UNSC_BEAM_T_JOINT

            elif str({object['itemId']}).find("-2083526830") == True:
                #UNSC Beam X Joint
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_BEAM_X_JOINT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 1, 7)
                ticker += Sorter.obj_UNSC_BEAM_X_JOINT
            ## Bridges 2
            elif str({object['itemId']}).find("-657742300") == True:
                #Forerunner Infantry Bridge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_INFANTRY_BRIDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 0)
                ticker += Sorter.obj_FORERUNNER_INFANTRY_BRIDGE

            elif str({object['itemId']}).find("2146360427") == True:
                #Infantry Bridge Angle Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_INFANTRY_BRIDGE_ANGLE_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 1)
                ticker += Sorter.obj_FORERUNNER_INFANTRY_BRIDGE_ANGLE_CORNER

            elif str({object['itemId']}).find("2102877297") == True:
                #Infantry Bridge Chamfered Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_INFANTRY_BRIDGE_CHAMFERED_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 2)
                ticker += Sorter.obj_FORERUNNER_INFANTRY_BRIDGE_CHAMFERED_CORNER

            elif str({object['itemId']}).find("-1836916820") == True:
                #Forerunnre Infantry Bridge Elbow Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_INFANTRY_BRIDGE_ELBOW_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 3)
                ticker += Sorter.obj_FORERUNNER_INFANTRY_BRIDGE_ELBOW_CORNER

            elif str({object['itemId']}).find("-353192367") == True:
                #Recharge Bridge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RECHARGE_BRIDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 4)
                ticker += Sorter.obj_RECHARGE_BRIDGE

            elif str({object['itemId']}).find("1174986318") == True:
                #UNSC Infantry Bridge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_INFANTRY_BRIDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 5)
                ticker += Sorter.obj_UNSC_INFANTRY_BRIDGE

            elif str({object['itemId']}).find("-194975118") == True:
                #UNSC Infantry Bridge Angle Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_INFANTRY_BRIDGE_ANGLE_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 6)
                ticker += Sorter.obj_UNSC_INFANTRY_BRIDGE_ANGLE_CORNER

            elif str({object['itemId']}).find("674244938") == True:
                #UNSC Infantry Bridge Chamfered Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_INFANTRY_BRIDGE_CHAMFERED_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 7)
                ticker += Sorter.obj_UNSC_INFANTRY_BRIDGE_CHAMFERED_CORNER

            elif str({object['itemId']}).find("-318896539") == True:
                #UNSC Infantry Bridge Elbow Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_INFANTRY_BRIDGE_ELBOW_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 8)
                ticker += Sorter.obj_UNSC_INFANTRY_BRIDGE_ELBOW_CORNER

            elif str({object['itemId']}).find("-153902808") == True:
                #UNSC Vehicle Bridge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_VEHICLE_BRIDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 9)
                ticker += Sorter.obj_UNSC_VEHICLE_BRIDGE

            elif str({object['itemId']}).find("-887750500") == True:
                #UNSC Vehicle Bridge Angle Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_VEHICLE_BRIDGE_ANGLE_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 10)
                ticker += Sorter.obj_UNSC_VEHICLE_BRIDGE_ANGLE_CORNER

            elif str({object['itemId']}).find("-506324578") == True:
                #UNSC Vehicle Bridge Chamfered Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_VEHICLE_BRIDGE_CHAMFERED_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 11)
                ticker += Sorter.obj_UNSC_VEHICLE_BRIDGE_CHAMFERED_CORNER

            elif str({object['itemId']}).find("1491509867") == True:
                #UNSC Vehicle Bridge Elbow Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_VEHICLE_BRIDGE_ELBOW_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 2, 12)
                ticker += Sorter.obj_UNSC_VEHICLE_BRIDGE_ELBOW_CORNER
            ## Bridges MP 3
            elif str({object['itemId']}).find("1526415433") == True:
                #Recharge Bridge MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_RECHARGE_BRIDGE_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 3, 0)
                ticker += Sorter.obj_RECHARGE_BRIDGE_MP
            ## Columns 4
            elif str({object['itemId']}).find("-1489146921") == True:
                #Forerunner Round Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_ROUND_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 4, 0)
                ticker += Sorter.obj_FORERUNNER_ROUND_COLUMN

            elif str({object['itemId']}).find("858956944") == True:
                #Forerunner Square Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SQUARE_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 4, 1)
                ticker += Sorter.obj_FORERUNNER_SQUARE_COLUMN

            elif str({object['itemId']}).find("1171791424") == True:
                #UNSC Round Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_ROUND_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 4, 2)
                ticker += Sorter.obj_UNSC_ROUND_COLUMN

            elif str({object['itemId']}).find("-1722685555") == True:
                #UNSC Square Column
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_SQUARE_COLUMN+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 4, 3)
                ticker += Sorter.obj_UNSC_SQUARE_COLUMN
            ## Cover 5
            elif str({object['itemId']}).find("-750708567") == True:
                #Forerunner Full Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FULL_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 5, 0)
                ticker += Sorter.obj_FORERUNNER_FULL_COVER

            elif str({object['itemId']}).find("109718854") == True:
                #Forerunner Half Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_HALF_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 5, 1)
                ticker += Sorter.obj_FORERUNNER_HALF_COVER

            elif str({object['itemId']}).find("-1593549433") == True:
                #UNSC Full Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_FULL_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 5, 2)
                ticker += Sorter.obj_UNSC_FULL_COVER

            elif str({object['itemId']}).find("-183886613") == True:
                #UNSC Half Cover
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_HALF_COVER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 5, 3)
                ticker += Sorter.obj_UNSC_HALF_COVER
            ## Doors 6
            elif str({object['itemId']}).find("1070401816") == True:
                #Base Doorway
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BASE_DOORWAY+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 0)
                ticker += Sorter.obj_BASE_DOORWAY

            elif str({object['itemId']}).find("-1590149280") == True:
                #Base Doorway Angled
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_BASE_DOORWAY_ANGLED+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 1)
                ticker += Sorter.obj_BASE_DOORWAY_ANGLED

            elif str({object['itemId']}).find("-1496642065") == True:
                #Forerunner Spartan Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SPARTAN_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 2)
                ticker += Sorter.obj_FORERUNNER_SPARTAN_DOOR

            elif str({object['itemId']}).find("2094730747") == True:
                #Forerunner Spartan Doorframe
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_SPARTAN_DOORFRAME+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 3)
                ticker += Sorter.obj_FORERUNNER_SPARTAN_DOORFRAME

            elif str({object['itemId']}).find("-1170643676") == True:
                #Forerunner Vehicle Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_VEHICLE_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 4)
                ticker += Sorter.obj_FORERUNNER_VEHICLE_DOOR

            elif str({object['itemId']}).find("-1696071810") == True:
                #Forerunner Vehicle Doorframe
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_VEHICLE_DOORFRAME+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 5)
                ticker += Sorter.obj_FORERUNNER_VEHICLE_DOORFRAME

            elif str({object['itemId']}).find("-230028072") == True:
                #Massive Welded Gate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MASSIVE_WELDED_GATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 6)
                ticker += Sorter.obj_MASSIVE_WELDED_GATE

            elif str({object['itemId']}).find("-1501399034") == True:
                #Massive Wooden Gate
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_MASSIVE_WOODEN_GATE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 7)
                ticker += Sorter.obj_MASSIVE_WOODEN_GATE

            elif str({object['itemId']}).find("-90037795") == True:
                #UNSC Generic Doorframe Tall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_GENERIC_DOORFRAME_TALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 8)
                ticker += Sorter.obj_UNSC_GENERIC_DOORFRAME_TALL

            elif str({object['itemId']}).find("67116532") == True:
                #UNSC Generic Doorframe Tall Large
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_GENERIC_DOORFRAME_TALL_LARGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 9)
                ticker += Sorter.obj_UNSC_GENERIC_DOORFRAME_TALL_LARGE

            #elif str({object['itemId']}).find("") == True: We have 2 itemIds for this object, need to check which one is correct: -1909914527, 455197259
                #obj_UNSC_HEAVY_DOOR

            elif str({object['itemId']}).find("-617446958") == True:
                #UNSC Spartan Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_SPARTAN_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 11)
                ticker += Sorter.obj_UNSC_SPARTAN_DOOR

            elif str({object['itemId']}).find("690293631") == True:
                #UNSC Spartan Doorframe
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_SPARTAN_DOORFRAME+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 12)
                ticker += Sorter.obj_UNSC_SPARTAN_DOORFRAME

            elif str({object['itemId']}).find("195775167") == True:
                #UNSC Tank Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_TANK_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 13)
                ticker += Sorter.obj_UNSC_TANK_DOOR

            elif str({object['itemId']}).find("-321529155") == True:
                #UNSC Tank Doorframe
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_TANK_DOORFRAME+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 14)
                ticker += Sorter.obj_UNSC_TANK_DOORFRAME

            elif str({object['itemId']}).find("1640301935") == True:
                #UNSC Vehicle Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_VEHICLE_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 15)
                ticker += Sorter.obj_UNSC_VEHICLE_DOOR

            elif str({object['itemId']}).find("-1385032404") == True:
                #UNSC Vehicle Doorframe
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_VEHICLE_DOORFRAME+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 16)
                ticker += Sorter.obj_UNSC_VEHICLE_DOORFRAME

            elif str({object['itemId']}).find("-284129658") == True:
                #Welded Double Security Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WELDED_DOUBLE_SECURITY_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 17)
                ticker += Sorter.obj_WELDED_DOUBLE_SECURITY_DOOR

            elif str({object['itemId']}).find("836904696") == True:
                #Welded Security Door
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WELDED_SECURITY_DOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 6, 18)
                ticker += Sorter.obj_WELDED_SECURITY_DOOR
            ## Doors MP 7
            elif str({object['itemId']}).find("1233051095") == True:
                #Large Vent Hatch B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_LARGE_VENT_HATCH_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 7, 0)
                ticker += Sorter.obj_LARGE_VENT_HATCH_B

            #elif str({object['itemId']}).find("") == True: We have 2 itemIds for this object, need to check which one is correct: -1545927443, -435695488
                #obj_UNSC_HEAVY_DOOR_BASE_WEAR_MP

            elif str({object['itemId']}).find("-425933955") == True:
                #UNSC Heavy Door Wide MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_HEAVY_DOOR_WIDE_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 7, 2)
                ticker += Sorter.obj_UNSC_HEAVY_DOOR_WIDE_MP

            elif str({object['itemId']}).find("79767035") == True:
                #Welded Double Security Door MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WELDED_DOUBLE_SECURITY_DOOR_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 7, 3)
                ticker += Sorter.obj_WELDED_DOUBLE_SECURITY_DOOR_MP

            elif str({object['itemId']}).find("1857035317") == True:
                #Welded Security Door MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WELDED_SECURITY_DOOR_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 7, 4)
                ticker += Sorter.obj_WELDED_SECURITY_DOOR_MP

            elif str({object['itemId']}).find("812102300") == True:
                #Wooden Door MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WOODEN_DOOR_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 7, 5)
                ticker += Sorter.obj_WOODEN_DOOR_MP

            elif str({object['itemId']}).find("-1550592518") == True:
                #Wooden Doorframe MP
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_WOODEN_DOORFRAME_MP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 7, 6)
                ticker += Sorter.obj_WOODEN_DOORFRAME_MP
            ## Floors 8
            elif str({object['itemId']}).find("659152961") == True:
                #Forerunner Floor
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_FLOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 8, 0)
                ticker += Sorter.obj_FORERUNNER_FLOOR

            elif str({object['itemId']}).find("1474383960") == True:
                #UNSC Floor
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_FLOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 8, 1)
                ticker += Sorter.obj_UNSC_FLOOR

            elif str({object['itemId']}).find("434341535") == True:
                #UNSC Level Start Floor
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_LEVEL_START_FLOOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 8, 2)
                ticker += Sorter.obj_UNSC_LEVEL_START_FLOOR
            ## Slopes 9
            elif str({object['itemId']}).find("1479917222") == True:
                #Forerunner Ramp ST
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_RAMP_ST+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 0)
                ticker += Sorter.obj_FORERUNNER_RAMP_ST

            elif str({object['itemId']}).find("-687359198") == True:
                #Forerunner Stairs Connector
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_STAIRS_CONNECTOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 1)
                ticker += Sorter.obj_FORERUNNER_STAIRS_CONNECTOR

            elif str({object['itemId']}).find("-1917507734") == True:
                #Forerunner Stairs L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_STAIRS_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 2)
                ticker += Sorter.obj_FORERUNNER_STAIRS_L

            elif str({object['itemId']}).find("952915351") == True:
                #Forerunner Stairs M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_STAIRS_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 3)
                ticker += Sorter.obj_FORERUNNER_STAIRS_M

            elif str({object['itemId']}).find("2136274689") == True:
                #Forerunnre Stairs S
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_STAIRS_S+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 4)
                ticker += Sorter.obj_FORERUNNER_STAIRS_S

            elif str({object['itemId']}).find("755658281") == True:
                #Forerunnre Stairs XL
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_STAIRS_XL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 5)
                ticker += Sorter.obj_FORERUNNER_STAIRS_XL

            elif str({object['itemId']}).find("1022291482") == True:
                #Forerunner Stairs XS
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_STAIRS_XS+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 6)
                ticker += Sorter.obj_FORERUNNER_STAIRS_XS

            elif str({object['itemId']}).find("106177700") == True:
                #Forerunner Wedge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_WEDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 7)
                ticker += Sorter.obj_FORERUNNER_WEDGE

            elif str({object['itemId']}).find("-689909916") == True:
                #Metal Staircase
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_METAL_STAIRCASE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 8)
                ticker += Sorter.obj_METAL_STAIRCASE

            elif str({object['itemId']}).find("-795527550") == True:
                #UNSC Ramp
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_RAMP+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 9)
                ticker += Sorter.obj_UNSC_RAMP

            elif str({object['itemId']}).find("1225151943") == True:
                #UNSC Stairs Connector
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_STAIRS_CONNECTOR+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 10)
                ticker += Sorter.obj_UNSC_STAIRS_CONNECTOR

            elif str({object['itemId']}).find("-1954921178") == True:
                #UNSC Stairs L
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_STAIRS_L+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 11)
                ticker += Sorter.obj_UNSC_STAIRS_L

            elif str({object['itemId']}).find("1435073507") == True:
                #UNSC Stairs M
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_STAIRS_M+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 12)
                ticker += Sorter.obj_UNSC_STAIRS_M

            elif str({object['itemId']}).find("216539180") == True:
                #UNSC Stairs S
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_STAIRS_S+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 13)
                ticker += Sorter.obj_UNSC_STAIRS_S

            elif str({object['itemId']}).find("-1434565444") == True:
                #UNSC Stairs XL
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_STAIRS_XL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 14)
                ticker += Sorter.obj_UNSC_STAIRS_XL

            elif str({object['itemId']}).find("-2116213658") == True:
                #UNSC Stairs XS
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_STAIRS_XS+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 15)
                ticker += Sorter.obj_UNSC_STAIRS_XS

            elif str({object['itemId']}).find("-1729719259") == True:
                #UNSC Wedge
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WEDGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 9, 16)
                ticker += Sorter.obj_UNSC_WEDGE
            ## Walls 10
            elif str({object['itemId']}).find("-720374419") == True:
                #Forerunner Wall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_WALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 0)
                ticker += Sorter.obj_FORERUNNER_WALL

            elif str({object['itemId']}).find("-1891952860") == True:
                #Forerunner Wall Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_WALL_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 1)
                ticker += Sorter.obj_FORERUNNER_WALL_CORNER

            elif str({object['itemId']}).find("1042655230") == True:
                #Forerunner Window Wall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_FORERUNNER_WINDOW_WALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 2)
                ticker += Sorter.obj_FORERUNNER_WINDOW_WALL

            elif str({object['itemId']}).find("-864616770") == True:
                #Panel Wall Piece A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_WALL_PIECE_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 3)
                ticker += Sorter.obj_PANEL_WALL_PIECE_A

            elif str({object['itemId']}).find("-269997588") == True:
                #Panel Wall Piece B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_WALL_PIECE_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 4)
                ticker += Sorter.obj_PANEL_WALL_PIECE_B

            elif str({object['itemId']}).find("-1433860927") == True:
                #Panel Wall Piece C
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_WALL_PIECE_C+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 5)
                ticker += Sorter.obj_PANEL_WALL_PIECE_C

            elif str({object['itemId']}).find("-146692457") == True:
                #Panel Wall Piece D
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_PANEL_WALL_PIECE_D+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 6)
                ticker += Sorter.obj_PANEL_WALL_PIECE_D

            elif str({object['itemId']}).find("1092140526") == True:
                #UNSC Wall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 7)
                ticker += Sorter.obj_UNSC_WALL

            elif str({object['itemId']}).find("-697090925") == True:
                #UNSC Wall Corner
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_CORNER+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 8)
                ticker += Sorter.obj_UNSC_WALL_CORNER

            elif str({object['itemId']}).find("-314132422") == True:
                #UNSC Wall Generic 45 In A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_GENERIC_45_IN_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 9)
                ticker += Sorter.obj_UNSC_WALL_GENERIC_45_IN_A

            elif str({object['itemId']}).find("1936001334") == True:
                #UNSC Wall Generic 45 In B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_GENERIC_45_IN_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 10)
                ticker += Sorter.obj_UNSC_WALL_GENERIC_45_IN_B

            elif str({object['itemId']}).find("-58708148") == True:
                #UNSC Wall Generic 45 Out
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_GENERIC_45_OUT+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 11)
                ticker += Sorter.obj_UNSC_WALL_GENERIC_45_OUT

            elif str({object['itemId']}).find("322212374") == True:
                #UNSC Wall Generic Straight Large
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_GENERIC_STRAIGHT_LARGE+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 12)
                ticker += Sorter.obj_UNSC_WALL_GENERIC_STRAIGHT_LARGE

            elif str({object['itemId']}).find("595352945") == True:
                #UNSC Wall Generic Straight Narrow
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_GENERIC_STRAIGHT_NARROW+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 13)
                ticker += Sorter.obj_UNSC_WALL_GENERIC_STRAIGHT_NARROW

            elif str({object['itemId']}).find("2075885169") == True:
                #UNSC Wall Window Straight A
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_WINDOW_STRAIGHT_A+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 14)
                ticker += Sorter.obj_UNSC_WALL_WINDOW_STRAIGHT_A

            elif str({object['itemId']}).find("306231068") == True:
                #UNSC Wall Window Straight B
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WALL_WINDOW_STRAIGHT_B+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, 12, 10, 15)
                ticker += Sorter.obj_UNSC_WALL_WINDOW_STRAIGHT_B

            elif str({object['itemId']}).find("-1720425530") == True:
                #UNSC Window Wall
                mirvTranslator.objTranslation(sorted_item_list[ticker:Sorter.obj_UNSC_WINDOW_WALL+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, end_index, end_index_check, listLength, low_performance, position_only, 12, 10, 16)
                ticker += Sorter.obj_UNSC_WINDOW_WALL

            # Here is a new item template.
            # a, b, and c are how many downpresses needed to navigate to that object in the Forge Object Browser.
                #elif str({object['itemId']}).find("") == True:
                    #Object
                    #mirvTranslator.objTranslation(sorted_item_list[ticker:+ticker], ticker, vLog, stop_me, start_index, end_index, end_index_check, save_interval, save_interval_check, listLength, low_performance, position_only, a, b, c)
                    #ticker += 

            else:
                if vLog == True:
                    print("vLOG: Keymanager.py: Object had no written mapping in Keymanager:\n{}.\n".format(object))
                    sys.stdout.flush()
                print("This object matches no profile!")
                ticker += 1
            sys.stdout.flush()
            time.sleep(low_performance + 0.05)
            break
    if vLog == True:
        print("vLOG: Keymanager.py: Print completed.")
        sys.stdout.flush()
    #print("Objects processed: {} / {}".format(ticker + start_index, listLength + start_index))
    mirvTranslator.save(low_performance, vLog)
    mirvTranslator.goToObjBrowser(low_performance, vLog)
    print("-" * 20)
    if sys.argv[15].lower() == 'true':
        print("Collection Completed. Please check objects for placement, rotation, and scaling accuracy.")
    else: 
        print("Print Completed. Please check objects for placement, rotation, and scaling accuracy.")
    sys.stdout.flush()

##### Execution of Object Processing Functions End

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