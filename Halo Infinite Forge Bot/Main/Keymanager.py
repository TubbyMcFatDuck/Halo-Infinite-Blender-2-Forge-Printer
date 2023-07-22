import pyautogui
import time
import pydirectinput
import sys
import pyperclip
import Sorter

##### Execution of Object Processing Functions Start

key_count = 0
key_to_count = 'itemId'
low_performance=0.012
start_index = 0

def process_objects(item_list, path, start_index, position_only=None, low_performance=0.012):
    print(start_index)
    sorted_item_list = Sorter.sortItems(item_list)
    ticker = start_index
    listLength = len(sorted_item_list)
    Sorter.initSorter(path)
    if position_only == False:
        setRotationAxis(low_performance)
    print("Starting at index: {}".format(ticker))
    while ticker < len(sorted_item_list):
        object = sorted_item_list[ticker]
        print("Processing objects: {} with itemIds: {}".format(object['objectName'], object['itemId']))
        if str({object['itemId']}).find("-612639225") == True:
            #Angled Corner Wall Standard
            objTranslation(sorted_item_list[ticker:Sorter.angledCornerWallStandard+ticker], ticker, listLength, low_performance, position_only, 8, 16, 1)
            ticker += Sorter.angledCornerWallStandard

        elif str({object['itemId']}).find("-2102390651") == True:
            #Angled Single Doorway
            objTranslation(sorted_item_list[ticker:Sorter.angledSingleDoorway+ticker], ticker, listLength, low_performance, position_only, 8, 7, 1)
            ticker += Sorter.angledSingleDoorway

        elif str({object['itemId']}).find("631526139") == True:
            #Ramp
            objTranslation(sorted_item_list[ticker:Sorter.ramp+ticker], ticker, listLength, low_performance, position_only, 3, 12, 6)
            ticker += Sorter.ramp

        elif str({object['itemId']}).find("1530590479") == True:
            #Ramp Transition
            objTranslation(sorted_item_list[ticker:Sorter.rampTransition+ticker], ticker, listLength, low_performance, position_only, 3, 12, 12)
            ticker += Sorter.rampTransition
        
        elif str({object['itemId']}).find("691693133") == True:
            #Angled Wall Double Window A
            objTranslation(sorted_item_list[ticker:Sorter.angledWallDoubleWindowA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 2)
            ticker += Sorter.angledWallDoubleWindowA

        elif str({object['itemId']}).find("1103502387") == True:
            #Angled Wall Double Window B
            objTranslation(sorted_item_list[ticker:Sorter.angledWallDoubleWindowB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 3)
            ticker += Sorter.angledWallDoubleWindowB
        
        elif str({object['itemId']}).find("-319219211") == True:
            #Floor Half B
            objTranslation(sorted_item_list[ticker:Sorter.floorHalfB+ticker], ticker, listLength, low_performance, position_only, 8, 9, 3)
            ticker += Sorter.floorHalfB

        elif str({object['itemId']}).find("-588839424") == True:
            #1 Over 3 Ramp Eighth A
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampEighthA+ticker], ticker, listLength, low_performance, position_only, 8, 13, 0)
            ticker += Sorter.oneOverThreeRampEighthA

        elif str({object['itemId']}).find("908393824") == True:
            #1 Over 3 Ramp Eighth B
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampEighthB+ticker], ticker, listLength, low_performance, position_only, 8, 13, 1)
            ticker += Sorter.oneOverThreeRampEighthB
        
        elif str({object['itemId']}).find("2062928760") == True:
            #Player Scale Object
            objTranslation(sorted_item_list[ticker:Sorter.playerScaleObject+ticker], ticker, listLength, low_performance, position_only, 8, 15, 0)
            ticker += Sorter.playerScaleObject

        elif str({object['itemId']}).find("-1844206092") == True:
            #1 Over 3 Ramp Half A
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampHalfA+ticker], ticker, listLength, low_performance, position_only, 8, 13, 2)
            ticker += Sorter.oneOverThreeRampHalfA

        elif str({object['itemId']}).find("707549041") == True:
            #1 Over 3 Ramp Half B
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampHalfB+ticker], ticker, listLength, low_performance, position_only, 8, 13, 3)
            ticker += Sorter.oneOverThreeRampHalfB
        
        elif str({object['itemId']}).find("715160887") == True:
            #1 Over 3 Ramp Half C
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampHalfC+ticker], ticker, listLength, low_performance, position_only, 8, 13, 4)
            ticker += Sorter.oneOverThreeRampHalfC

        elif str({object['itemId']}).find("-1765693041") == True:
            #1 Over 3 Ramp Quarter
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampQuarter+ticker], ticker, listLength, low_performance, position_only, 8, 13, 5)
            ticker += Sorter.oneOverThreeRampQuarter
        
        elif str({object['itemId']}).find("-984668480") == True:
            #1 Over 3 Ramp Sixteenth
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampSixteenth+ticker], ticker, listLength, low_performance, position_only, 8, 13, 6)
            ticker += Sorter.oneOverThreeRampSixteenth

        elif str({object['itemId']}).find("468997533") == True:
            #1 Over 3 Ramp Standard A
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampStandardA+ticker], ticker, listLength, low_performance, position_only, 8, 13, 7)
            ticker += Sorter.oneOverThreeRampStandardA

        elif str({object['itemId']}).find("1765455307") == True:
            #1 Over 3 Ramp Standard B
            objTranslation(sorted_item_list[ticker:Sorter.oneOverThreeRampStandardB+ticker], ticker, listLength, low_performance, position_only, 8, 13, 8)
            ticker += Sorter.oneOverThreeRampStandardB

        elif str({object['itemId']}).find("1461903299") == True:
            #1 Over 4 Ramp Half A
            objTranslation(sorted_item_list[ticker:Sorter.oneOverFourRampHalfA+ticker], ticker, listLength, low_performance, position_only, 8, 13, 9)
            ticker += Sorter.oneOverFourRampHalfA

        elif str({object['itemId']}).find("-152113334") == True:
            #1 Over 4 Ramp Half B
            objTranslation(sorted_item_list[ticker:Sorter.oneOverFourRampHalfB+ticker], ticker, listLength, low_performance, position_only, 8, 13, 10)
            ticker += Sorter.oneOverFourRampHalfB

        elif str({object['itemId']}).find("-1108230827") == True:
            #2x2 Round Column C
            objTranslation(sorted_item_list[ticker:Sorter.twoBytwoRoundColumnC+ticker], ticker, listLength, low_performance, position_only, 8, 1, 0)
            ticker += Sorter.twoBytwoRoundColumnC

        elif str({object['itemId']}).find("-885874693") == True:
            #2x2 Round Column D
            objTranslation(sorted_item_list[ticker:Sorter.twoBytwoRoundColumnD+ticker], ticker, listLength, low_performance, position_only, 8, 1, 1)
            ticker += Sorter.twoBytwoRoundColumnD

        elif str({object['itemId']}).find("2096053754") == True:
            #2x2 Square Column A
            objTranslation(sorted_item_list[ticker:Sorter.twoBytwoSquareColumnA+ticker], ticker, listLength, low_performance, position_only, 8, 1, 2)
            ticker += Sorter.twoBytwoSquareColumnA

        elif str({object['itemId']}).find("-1294229133") == True:
            #2x2 Square Column B
            objTranslation(sorted_item_list[ticker:Sorter.twoBytwoSquareColumnB+ticker], ticker, listLength, low_performance, position_only, 8, 1, 3)
            ticker += Sorter.twoBytwoSquareColumnB

        elif str({object['itemId']}).find("491753301") == True:
            #4.5x8 Crate
            objTranslation(sorted_item_list[ticker:Sorter.fourDotFivebyEightCrate+ticker], ticker, listLength, low_performance, position_only, 8, 5, 0)
            ticker += Sorter.fourDotFivebyEightCrate
        
        elif str({object['itemId']}).find("253727975") == True:
            #4x4 Crate
            objTranslation(sorted_item_list[ticker:Sorter.fourByfourCrate+ticker], ticker, listLength, low_performance, position_only, 8, 5, 1)
            ticker += Sorter.fourByfourCrate

        elif str({object['itemId']}).find("-1422631181") == True:
            #4x4 Round Column C
            objTranslation(sorted_item_list[ticker:Sorter.fourByfourRoundColumnC+ticker], ticker, listLength, low_performance, position_only, 8, 1, 4)
            ticker += Sorter.fourByfourRoundColumnC

        elif str({object['itemId']}).find("1947532949") == True:
            #4x4 Round Column D
            objTranslation(sorted_item_list[ticker:Sorter.fourByfourRoundColumnD+ticker], ticker, listLength, low_performance, position_only, 8, 1, 5)
            ticker += Sorter.fourByfourRoundColumnD

        elif str({object['itemId']}).find("2083372609") == True:
            #4x4 Square Column A
            objTranslation(sorted_item_list[ticker:Sorter.fourByfourSquareColumnA+ticker], ticker, listLength, low_performance, position_only, 8, 1, 6)
            ticker += Sorter.fourByfourSquareColumnA

        elif str({object['itemId']}).find("1607542385") == True:
            #4x4 Square Column B
            objTranslation(sorted_item_list[ticker:Sorter.fourByfourSquareColumnB+ticker], ticker, listLength, low_performance, position_only, 8, 1, 7)
            ticker += Sorter.fourByfourSquareColumnB

        elif str({object['itemId']}).find("-1137520810") == True:
            #4x8 Crate
            objTranslation(sorted_item_list[ticker:Sorter.fourByeightCrate+ticker], ticker, listLength, low_performance, position_only, 8, 5, 2)
            ticker += Sorter.fourByeightCrate

        elif str({object['itemId']}).find("1553385688") == True:
            #6x6 Round Column C
            objTranslation(sorted_item_list[ticker:Sorter.sixBysixRoundColumnC+ticker], ticker, listLength, low_performance, position_only, 8, 1, 8)
            ticker += Sorter.sixBysixRoundColumnC
        
        elif str({object['itemId']}).find("222107335") == True:
            #6x6 Round Column D
            objTranslation(sorted_item_list[ticker:Sorter.sixBysixRoundColumnD+ticker], ticker, listLength, low_performance, position_only, 8, 1, 9)
            ticker += Sorter.sixBysixRoundColumnD

        elif str({object['itemId']}).find("-446137873") == True:
            #6x6 Square Column A
            objTranslation(sorted_item_list[ticker:Sorter.sixBysixSquareColumnA+ticker], ticker, listLength, low_performance, position_only, 8, 1, 10)
            ticker += Sorter.sixBysixSquareColumnA

        elif str({object['itemId']}).find("727360123") == True:
            #6x6 Square Column B
            objTranslation(sorted_item_list[ticker:Sorter.sixBysixSquareColumnB+ticker], ticker, listLength, low_performance, position_only, 8, 1, 11)
            ticker += Sorter.sixBysixSquareColumnB

        elif str({object['itemId']}).find("-89276352") == True:
            #8x8 Crate
            objTranslation(sorted_item_list[ticker:Sorter.eightByeightCrate+ticker], ticker, listLength, low_performance, position_only, 8, 5, 3)
            ticker += Sorter.eightByeightCrate

        elif str({object['itemId']}).find("355942414") == True:
            #8x16 Crate
            objTranslation(sorted_item_list[ticker:Sorter.eightBysixteenCrate+ticker], ticker, listLength, low_performance, position_only, 8, 5, 4)
            ticker += Sorter.eightBysixteenCrate

        elif str({object['itemId']}).find("1168502040") == True:
            #Angle Wall Half
            objTranslation(sorted_item_list[ticker:Sorter.angleWallHalf+ticker], ticker, listLength, low_performance, position_only, 8, 16, 0)
            ticker += Sorter.angleWallHalf
        
        elif str({object['itemId']}).find("-1843159215") == True:
            #Angled Double Doorway
            objTranslation(sorted_item_list[ticker:Sorter.angledDoubleDoorway+ticker], ticker, listLength, low_performance, position_only, 8, 7, 0)
            ticker += Sorter.angledDoubleDoorway

        elif str({object['itemId']}).find("1383537765") == True:
            #Angled Wall Double Window C
            objTranslation(sorted_item_list[ticker:Sorter.angledWallDoubleWindowC+ticker], ticker, listLength, low_performance, position_only, 8, 16, 4)
            ticker += Sorter.angledWallDoubleWindowC

        elif str({object['itemId']}).find("-41069292") == True:
            #Angled Wall Standard A
            objTranslation(sorted_item_list[ticker:Sorter.angledWallStandardA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 5)
            ticker += Sorter.angledWallStandardA

        elif str({object['itemId']}).find("1361150846") == True:
            #Angled Wall Standard B
            objTranslation(sorted_item_list[ticker:Sorter.angledWallStandardB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 6)
            ticker += Sorter.angledWallStandardB

        elif str({object['itemId']}).find("-979944560") == True:
            #Angled Wall Window A
            objTranslation(sorted_item_list[ticker:Sorter.angledWallWindowA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 7)
            ticker += Sorter.angledWallWindowA

        elif str({object['itemId']}).find("-147813598") == True:
            #Angled Wall Window B
            objTranslation(sorted_item_list[ticker:Sorter.angledWallWindowB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 8)
            ticker += Sorter.angledWallWindowB

        elif str({object['itemId']}).find("1416644323") == True:
            #Angled Wall Window C
            objTranslation(sorted_item_list[ticker:Sorter.angledWallWindowC+ticker], ticker, listLength, low_performance, position_only, 8, 16, 9)
            ticker += Sorter.angledWallWindowC

        elif str({object['itemId']}).find("-173471027") == True:
            #Corner Wall Standard
            objTranslation(sorted_item_list[ticker:Sorter.cornerWallStandard+ticker], ticker, listLength, low_performance, position_only, 8, 16, 10)
            ticker += Sorter.cornerWallStandard
        
        elif str({object['itemId']}).find("-936420252") == True:
            #Curved Double Window Wall A
            objTranslation(sorted_item_list[ticker:Sorter.curvedDoubleWindowWallA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 11)
            ticker += Sorter.curvedDoubleWindowWallA

        elif str({object['itemId']}).find("1662288531") == True:
            #Curved Double Window Wall B
            objTranslation(sorted_item_list[ticker:Sorter.curvedDoubleWindowWallB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 12)
            ticker += Sorter.curvedDoubleWindowWallB

        elif str({object['itemId']}).find("-341801782") == True:
            #Curved Wall Double
            objTranslation(sorted_item_list[ticker:Sorter.curvedWallDouble+ticker], ticker, listLength, low_performance, position_only, 8, 16, 13)
            ticker += Sorter.curvedWallDouble

        elif str({object['itemId']}).find("-960331706") == True:
            #Curved Wall Standard
            objTranslation(sorted_item_list[ticker:Sorter.curvedWallStandard+ticker], ticker, listLength, low_performance, position_only, 8, 16, 14)
            ticker += Sorter.curvedWallStandard

        elif str({object['itemId']}).find("-1332366101") == True:
            #Curved Wall Triple
            objTranslation(sorted_item_list[ticker:Sorter.curvedWallTriple+ticker], ticker, listLength, low_performance, position_only, 8, 16, 15)
            ticker += Sorter.curvedWallTriple

        elif str({object['itemId']}).find("101094355") == True:
            #Wall Cube Angled
            objTranslation(sorted_item_list[ticker:Sorter.wallCubeAngled+ticker], ticker, listLength, low_performance, position_only, 8, 16, 16)
            ticker += Sorter.wallCubeAngled

        elif str({object['itemId']}).find("-2128852445") == True:
            #Wall Cube Corner Angled
            objTranslation(sorted_item_list[ticker:Sorter.wallCubeCornerAngled+ticker], ticker, listLength, low_performance, position_only, 8, 16, 17)
            ticker += Sorter.wallCubeCornerAngled

        elif str({object['itemId']}).find("-1168178900") == True:
            #Wall Cube Standard
            objTranslation(sorted_item_list[ticker:Sorter.wallCubeStandard+ticker], ticker, listLength, low_performance, position_only, 8, 16, 18)
            ticker += Sorter.wallCubeStandard

        elif str({object['itemId']}).find("1662815138") == True:
            #Wall Double Window A
            objTranslation(sorted_item_list[ticker:Sorter.wallDoubleWindowA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 19)
            ticker += Sorter.wallDoubleWindowA

        elif str({object['itemId']}).find("-2011335511") == True:
            #Wall Double Window B
            objTranslation(sorted_item_list[ticker:Sorter.wallDoubleWindowB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 20)
            ticker += Sorter.wallDoubleWindowB

        elif str({object['itemId']}).find("-1513962159") == True:
            #Wall Half
            objTranslation(sorted_item_list[ticker:Sorter.wallHalf+ticker], ticker, listLength, low_performance, position_only, 8, 16, 21)
            ticker += Sorter.wallHalf
        
        elif str({object['itemId']}).find("1047093426") == True:
            #Wall Standard A
            objTranslation(sorted_item_list[ticker:Sorter.wallStandardA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 22)
            ticker += Sorter.wallStandardA

        elif str({object['itemId']}).find("-1459663496") == True:
            #Wall Standard B
            objTranslation(sorted_item_list[ticker:Sorter.wallStandardB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 23)
            ticker += Sorter.wallStandardB

        elif str({object['itemId']}).find("-725006759") == True:
            #Wall Window A
            objTranslation(sorted_item_list[ticker:Sorter.wallWindowA+ticker], ticker, listLength, low_performance, position_only, 8, 16, 24)
            ticker += Sorter.wallWindowA

        elif str({object['itemId']}).find("1064263013") == True:
            #Wall Window B
            objTranslation(sorted_item_list[ticker:Sorter.wallWindowB+ticker], ticker, listLength, low_performance, position_only, 8, 16, 25)
            ticker += Sorter.wallWindowB

        elif str({object['itemId']}).find("-1804795714") == True:
            #Ankle Cover Half Size
            objTranslation(sorted_item_list[ticker:Sorter.ankleCoverHalfSize+ticker], ticker, listLength, low_performance, position_only, 8, 3, 0)
            ticker += Sorter.ankleCoverHalfSize

        elif str({object['itemId']}).find("-157703089") == True:
            #Ankle Cover Quarter Size
            objTranslation(sorted_item_list[ticker:Sorter.ankleCoverQuarterSize+ticker], ticker, listLength, low_performance, position_only, 8, 3, 1)
            ticker += Sorter.ankleCoverQuarterSize

        elif str({object['itemId']}).find("1969407375") == True:
            #Corner Ramp Eighth A
            objTranslation(sorted_item_list[ticker:Sorter.cornerRampEighthA+ticker], ticker, listLength, low_performance, position_only,  8, 13, 11)
            ticker += Sorter.cornerRampEighthA

        elif str({object['itemId']}).find("1451712685") == True:
            #Corner Ramp Eighth B
            objTranslation(sorted_item_list[ticker:Sorter.cornerRampEighthB+ticker], ticker, listLength, low_performance, position_only, 8, 13, 12)
            ticker += Sorter.cornerRampEighthB

        elif str({object['itemId']}).find("-983151539") == True:
            #Forerunner Doorway
            objTranslation(sorted_item_list[ticker:Sorter.forerunnerDoorway+ticker], ticker, listLength, low_performance, position_only, 8, 7, 4)
            ticker += Sorter.forerunnerDoorway

        elif str({object['itemId']}).find("492327815") == True:
            #Forerunner Doorway Wide
            objTranslation(sorted_item_list[ticker:Sorter.forerunnerDoorwayWide+ticker], ticker, listLength, low_performance, position_only, 8, 7, 5)
            ticker += Sorter.forerunnerDoorwayWide

        elif str({object['itemId']}).find("1760817474") == True:
            #Curved Double Doorway
            objTranslation(sorted_item_list[ticker:Sorter.curvedDoubleDoorway+ticker], ticker, listLength, low_performance, position_only, 8, 7, 2)
            ticker += Sorter.curvedDoubleDoorway

        elif str({object['itemId']}).find("2140930404") == True:
            #Curved Railing Half Size
            objTranslation(sorted_item_list[ticker:Sorter.curvedRailingHalfSize+ticker], ticker, listLength, low_performance, position_only, 8, 11, 0)
            ticker += Sorter.curvedRailingHalfSize

        elif str({object['itemId']}).find("-191674833") == True:
            #Curved Ramp Standard Right
            objTranslation(sorted_item_list[ticker:Sorter.curvedRampStandardRight+ticker], ticker, listLength, low_performance, position_only, 8, 13, 14)
            ticker += Sorter.curvedRampStandardRight
        
        elif str({object['itemId']}).find("759775548") == True:
            #Double Doorway
            objTranslation(sorted_item_list[ticker:Sorter.doubleDoorway+ticker], ticker, listLength, low_performance, position_only, 8, 7, 3)
            ticker += Sorter.doubleDoorway

        elif str({object['itemId']}).find("2119916132") == True:
            #Floor Angled Standard A
            objTranslation(sorted_item_list[ticker:Sorter.floorAngledStandardA+ticker], ticker, listLength, low_performance, position_only, 8, 9, 0)
            ticker += Sorter.floorAngledStandardA

        elif str({object['itemId']}).find("471557513") == True:
            #Fllor Angled Standard B
            objTranslation(sorted_item_list[ticker:Sorter.floorAngledStandardB+ticker], ticker, listLength, low_performance, position_only, 8, 9, 1)
            ticker += Sorter.floorAngledStandardB

        elif str({object['itemId']}).find("-1554062464") == True:
            #Floor Half A
            objTranslation(sorted_item_list[ticker:Sorter.floorHalfA+ticker], ticker, listLength, low_performance, position_only, 8, 9, 2)
            ticker += Sorter.floorHalfA

        elif str({object['itemId']}).find("1561437000") == True:
            #Floor Quadruple Size
            objTranslation(sorted_item_list[ticker:Sorter.floorQuadrupleSize+ticker], ticker, listLength, low_performance, position_only, 8, 9, 4)
            ticker += Sorter.floorQuadrupleSize

        elif str({object['itemId']}).find("796754322") == True:
            #Floor Standard
            objTranslation(sorted_item_list[ticker:Sorter.floorStandard+ticker], ticker, listLength, low_performance, position_only, 8, 9, 5)
            ticker += Sorter.floorStandard

        elif str({object['itemId']}).find("1150132444") == True:
            #Four Way Ramp Eighth
            objTranslation(sorted_item_list[ticker:Sorter.fourWayRampEighth+ticker], ticker, listLength, low_performance, position_only, 8, 13, 15)
            ticker += Sorter.fourWayRampEighth
        
        elif str({object['itemId']}).find("2115878081") == True:
            #Full Cover Half Size
            objTranslation(sorted_item_list[ticker:Sorter.fullCoverHalfSize+ticker], ticker, listLength, low_performance, position_only, 8, 3, 2)
            ticker += Sorter.fullCoverHalfSize

        elif str({object['itemId']}).find("-2030691315") == True:
            #Full Cover Standard Size
            objTranslation(sorted_item_list[ticker:Sorter.fullCoverStandardSize+ticker], ticker, listLength, low_performance, position_only, 8, 3, 3)
            ticker += Sorter.fullCoverStandardSize

        elif str({object['itemId']}).find("286176533") == True:
            #Half Cover Half Size
            objTranslation(sorted_item_list[ticker:Sorter.halfCoverHalfSize+ticker], ticker, listLength, low_performance, position_only, 8, 3, 4)
            ticker += Sorter.halfCoverHalfSize

        elif str({object['itemId']}).find("1040169826") == True:
            #Half Cover Standard Size
            objTranslation(sorted_item_list[ticker:Sorter.halfCoverStandardSize+ticker], ticker, listLength, low_performance, position_only, 8, 3, 5)
            ticker += Sorter.halfCoverStandardSize

        elif str({object['itemId']}).find("-234187719") == True:
            #Primitive Cone
            objTranslation(sorted_item_list[ticker:Sorter.primCone+ticker], ticker, listLength, low_performance, position_only, 10, 2, 1)
            ticker += Sorter.primCone

        elif str({object['itemId']}).find("728515706") == True:
            #Primitive Cylinder
            objTranslation(sorted_item_list[ticker:Sorter.primCylinder+ticker], ticker, listLength, low_performance, position_only, 10, 3, 1)
            ticker += Sorter.primCylinder

        elif str({object['itemId']}).find("1189747031") == True:
            #Primitive Pyramid
            objTranslation(sorted_item_list[ticker:Sorter.primPyramid+ticker], ticker, listLength, low_performance, position_only, 10, 4, 1)
            ticker += Sorter.primPyramid

        elif str({object['itemId']}).find("-1706009392") == True:
            #Primitive Ring Eighth
            objTranslation(sorted_item_list[ticker:Sorter.primRingEighth+ticker], ticker, listLength, low_performance, position_only, 10, 5, 4)
            ticker += Sorter.primRingEighth

        elif str({object['itemId']}).find("-1190828000") == True:
            #Primitive Ring Full
            objTranslation(sorted_item_list[ticker:Sorter.primRingFull+ticker], ticker, listLength, low_performance, position_only, 10, 5, 5)
            ticker += Sorter.primRingFull

        elif str({object['itemId']}).find("-1298054065") == True:
            #Primitive Ring Half
            objTranslation(sorted_item_list[ticker:Sorter.primRingHalf+ticker], ticker, listLength, low_performance, position_only, 10, 5, 6)
            ticker += Sorter.primRingHalf

        elif str({object['itemId']}).find("1875914002") == True:
            #Primitive Ring Quarter
            objTranslation(sorted_item_list[ticker:Sorter.primRingQuarter+ticker], ticker, listLength, low_performance, position_only, 10, 5, 7)
            ticker += Sorter.primRingQuarter

        elif str({object['itemId']}).find("-457712308") == True:
            #Primitive Sphere
            objTranslation(sorted_item_list[ticker:Sorter.primSphere+ticker], ticker, listLength, low_performance, position_only, 10, 6, 1)
            ticker += Sorter.primSphere

        elif str({object['itemId']}).find("-1185205223") == True:
            #Primitive Triangle
            objTranslation(sorted_item_list[ticker:Sorter.primTriangle+ticker], ticker, listLength, low_performance, position_only, 10, 8, 1)
            ticker += Sorter.primTriangle

        elif str({object['itemId']}).find("1759788903") == True:
            #Primitive Cube
            objTranslation(sorted_item_list[ticker:Sorter.primCube+ticker], ticker, listLength, low_performance, position_only, 10, 1, 1)
            ticker += Sorter.primCube

        elif str({object['itemId']}).find("1635203824") == True:
            #Curved Railing Standard Size
            objTranslation(sorted_item_list[ticker:Sorter.curvedRailingStandardSize+ticker], ticker, listLength, low_performance, position_only, 8, 11, 1)
            ticker += Sorter.curvedRailingStandardSize
        
        elif str({object['itemId']}).find("902995208") == True:
            #Rock Half Cover A
            objTranslation(sorted_item_list[ticker:Sorter.rockHalfCoverA+ticker], ticker, listLength, low_performance, position_only, 8, 3, 6)
            ticker += Sorter.rockHalfCoverA
        
        elif str({object['itemId']}).find("2050581668") == True:
            #Rock Half Cover B
            objTranslation(sorted_item_list[ticker:Sorter.rockHalfCoverB+ticker], ticker, listLength, low_performance, position_only, 8, 3, 7)
            ticker += Sorter.rockHalfCoverB

        elif str({object['itemId']}).find("652937498") == True:
            #Single Doorway A
            objTranslation(sorted_item_list[ticker:Sorter.singleDoorwayA+ticker], ticker, listLength, low_performance, position_only, 8, 7, 6)
            ticker += Sorter.singleDoorwayA

        elif str({object['itemId']}).find("1989569474") == True:
            #Single Doorway B
            objTranslation(sorted_item_list[ticker:Sorter.singleDoorwayB+ticker], ticker, listLength, low_performance, position_only, 8, 7, 7)
            ticker += Sorter.singleDoorwayB

        elif str({object['itemId']}).find("1989569474") == True:
            #Single Doorway B
            objTranslation(sorted_item_list[ticker:Sorter.singleDoorwayB+ticker], ticker, listLength, low_performance, position_only, 8, 7, 7)
            ticker += Sorter.singleDoorwayB

        elif str({object['itemId']}).find("-1835432896") == True:
            #Eroded Terrain D
            objTranslation(sorted_item_list[ticker:Sorter.erodedTerrainD+ticker], ticker, listLength, low_performance, position_only, 3, 7, 2)
            ticker += Sorter.erodedTerrainD

    # Here is a new item template.
    # a, b, and c are how many downpresses needed to navigate to that object in the Forge Object Browser.
        #elif str({object['itemId']}).find("") == True:
            #Object
            #objTranslation(sorted_item_list[ticker:+ticker], ticker, listLength, low_performance, position_only, a, b, c)
            #ticker += 

        else:
            print("This object matches no profile!")
            ticker += 1
        sys.stdout.flush()
        time.sleep(low_performance + 0.05)
    print("Objects processed: {} / {}".format(ticker, listLength))
    print("-" * 20)
    print("Print Completed. Please check objects for placement, rotation, and scaling accuracy.")

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

def paste():
    time.sleep(.055)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('v')
    pydirectinput.keyUp('ctrl')
    print('Paste')
    sys.stdout.flush()

def save():
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('s')
    pydirectinput.keyUp('ctrl')
    print('Save batch')

def duplicate_Obj():
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('d')
    time.sleep(.02)
    pydirectinput.keyUp('ctrl')
    print('Duplicating Object')
    sys.stdout.flush()

def objTranslation(objects, ticker, listLength, low_performance, position_only, s1, s2, s3):
    subTick = ticker
    pydirectinput.PAUSE = low_performance
    moveToObject(s1,s2,s3, low_performance)
    for object in objects:
        print("Objects processed: {} / {}".format(subTick, listLength))
        resetRotation(low_performance, position_only)
        time.sleep(0.1)
        goToProperties(low_performance)
        time.sleep(0.1)
        giveProperties(object, low_performance, position_only)
        time.sleep(0.1)
        pydirectinput.press('z')
        subTick += 1
        if objects.index(object) != (len(objects)-1):
            time.sleep(0.2)
            replicateObject(low_performance)
    print("Returning Home...")
    time.sleep(0.15)
    goToObjBrowser(low_performance)
    revMoveToObject(s3,s2,s1, low_performance)
    sys.stdout.flush()

########################################## Start Workflow Efficiency Functions

def goToProperties(low_performance):
    pydirectinput.PAUSE = low_performance
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('2')
    pydirectinput.keyUp('ctrl')
    sys.stdout.flush()

def resetRotation(low_performance, position_only):
    pydirectinput.PAUSE = low_performance
    time.sleep(low_performance + 0.3)
    if position_only == False:
        pydirectinput.press('0')
        sys.stdout.flush()

def giveProperties(object, low_performance, position_only):
    zBump = 1000
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
        paste()
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Scale Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space']) 
        pyperclip.copy(str(object['scaleY']))
        paste()
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Scale Z
        pydirectinput.press(['down'])
        pydirectinput.press(['space']) 
        pyperclip.copy(str(object['scaleZ']))
        paste()
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
    pyperclip.copy(str(object['positionX']))
    paste()
    time.sleep(0.055)
    pydirectinput.press(['enter']) 

    #Position Y
    pydirectinput.press(['down'])
    pydirectinput.press(['space'])
    pyperclip.copy(str(object['positionY']))
    paste()
    time.sleep(0.055)
    pydirectinput.press(['enter']) 

    #Position Z
    pydirectinput.press(['down'])
    pydirectinput.press(['space'])
    object['positionZ'] = float(object['positionZ']) + zBump
    pyperclip.copy(str(object['positionZ']))
    paste()
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
        paste()
        time.sleep(0.055)
        pydirectinput.press(['enter']) 

        #Rotation Z
        pydirectinput.press(['up'],presses=2)
        pydirectinput.press(['space'])  
        pyperclip.copy(str(object['rotationZ']))
        paste()
        time.sleep(0.055)
        pydirectinput.press(['enter'])

        #Rotation Y
        pydirectinput.press(['down'])
        pydirectinput.press(['space']) 
        pyperclip.copy(str(object['rotationY']))
        paste()
        time.sleep(0.055)
        pydirectinput.press(['enter'])
        sys.stdout.flush()

def goToObjBrowser(low_performance):
    pydirectinput.PAUSE = low_performance
    time.sleep(low_performance + 0.05)
    pydirectinput.keyDown('ctrl')
    pydirectinput.press('1')
    pydirectinput.keyUp('ctrl')

def onetwozero(low_performance):
    pydirectinput.PAUSE = low_performance
    time.sleep(0.1)
    pydirectinput.press('1',presses= 2)
    time.sleep(0.1)
    pydirectinput.press('2',presses= 2)
    time.sleep(0.1)
    pydirectinput.press('0',presses= 2)

def moveToObject(stroke1, stroke2, stroke3, low_performance):
    pydirectinput.PAUSE = low_performance
    pydirectinput.press(['down'],presses= stroke1)
    pydirectinput.press(['space'])
    pydirectinput.press(['down'],presses= stroke2)
    pydirectinput.press(['space'])
    pydirectinput.press(['down'],presses= stroke3)
    pydirectinput.press(['space'])

def revMoveToObject(stroke1, stroke2, stroke3, low_performance):
    pydirectinput.PAUSE = low_performance
    pydirectinput.press(['up'],presses= stroke1)
    pydirectinput.press(['escape'])
    pydirectinput.press(['up'],presses= stroke2)
    pydirectinput.press(['space'])
    pydirectinput.press(['up'],presses= stroke3)

def setRotationAxis(low_performance):
    pydirectinput.PAUSE = low_performance
    sys.stdout.flush()
    print("Forcing Rotation Axis...")
    pydirectinput.press('ctrl', presses=2)
    pydirectinput.press(['up'],presses=2)
    pydirectinput.press(['space'])
    pydirectinput.press(['down'],presses=3)
    pydirectinput.press(['space'])
    pydirectinput.press(['down'],presses=3)
    pydirectinput.press(['space'])
    onetwozero(low_performance)
    goToObjBrowser(low_performance)
    pydirectinput.press(['up'],presses=3)
    pydirectinput.press(['escape'])
    pydirectinput.press(['up'],presses=3)
    pydirectinput.press(['space'])
    pydirectinput.press(['down'], presses=2)
    sys.stdout.flush()

def replicateObject(low_performance):
    pydirectinput.PAUSE = low_performance
    pydirectinput.press('ctrl')
    time.sleep(low_performance+0.20)
    ##pydirectinput.press('z')
    pydirectinput.press('q')
    pydirectinput.press(['space'])

########################################## End Workflow Efficiency Functions