import json
#python "C:\Users\bsher\Downloads\Halo-forge-Bot-1.1.9.2\Halo-forge-Bot-1.1.9.2\Test_Halo_Bot\Main\Bot.py" "C:\Users\bsher\Downloads\qqqhip.DCjson" False False 0.012 3
##Execution of Top Level Functions

key_count = 0
key_to_count = 'itemId'
low_performance=0.012
start_index = 0

##### Item Count Dictionary Start
#A
arenaColumnA = 0
arenaCornerCover = 0
arenaCoverA = 0
arenaOctagonCover = 0
angledCornerWallStandard = 0
angledDoubleDoorway = 0
angledSingleDoorway = 0
angledWallDoubleWindowA = 0
angledWallDoubleWindowB = 0
angledWallDoubleWindowC = 0
angledWallStandardA = 0
angledWallStandardB = 0
angledWallWindowA = 0
angledWallWindowB = 0
angledWallWindowC = 0
angleWallHalf = 0
ankleCoverHalfSize = 0
ankleCoverQuarterSize = 0
#B
barrelClosed = 0
barrelClosedRustyStriped = 0
barrelClosedRustyStripedMP = 0
barrelClosedStriped = 0
barrelClosedStripedMP = 0
barrelClosedWorn = 0
barrelClosedWornMP = 0
barrelOpen = 0
booksA = 0
booksAMP = 0
boosterAntenna = 0
#C
cellularAntenna = 0
cornerRampEighthA = 0
cornerRampEighthB = 0
cornerWallStandard = 0
curvedDoubleDoorway = 0
curvedDoubleWindowWallA = 0
curvedDoubleWindowWallB = 0
curvedRailingHalfSize = 0
curvedRailingStandardSize = 0
curvedRampStandardRight = 0
curvedWallDouble = 0
curvedWallStandard = 0
curvedWallTriple = 0
#D
dirtyBucket = 0
dirtyBucketMP = 0
doubleDoorway = 0
#E
eightByeightCrate = 0
eightBysixteenCrate = 0
erodedTerrainD = 0
#F
fixedSatelliteDish = 0
floorAngledStandardA = 0
floorAngledStandardB = 0
floorHalfA = 0
floorHalfB = 0
floorQuadrupleSize = 0
floorStandard = 0
forerunnerDoorway = 0
forerunnerDoorwayWide = 0
fourByeightCrate = 0
fourDotFivebyEightCrate = 0
fourByfourCrate = 0
fourByfourRoundColumnC = 0
fourByfourRoundColumnD = 0
fourByfourSquareColumnA = 0
fourByfourSquareColumnB = 0
fourWayRampEighth = 0
fullCoverHalfSize = 0
fullCoverStandardSize = 0
#G
#H
halfCoverHalfSize = 0
halfCoverStandardSize = 0
#I
#J
#K
#L
largeSatelliteDish = 0
#M
metallicFuelCanisterMP = 0
#N
#O
oneOverThreeRampEighthA = 0
oneOverThreeRampEighthB = 0
oneOverThreeRampHalfA = 0
oneOverThreeRampHalfB = 0
oneOverThreeRampHalfC = 0
oneOverThreeRampQuarter = 0
oneOverThreeRampSixteenth = 0
oneOverThreeRampStandardA = 0
oneOverThreeRampStandardB = 0
oneOverFourRampHalfA = 0
oneOverFourRampHalfB = 0
#P
playerScaleObject = 0
plasticFuelCanisterMP = 0
plasticLiquidCanisterMP = 0
portableSatelliteDish = 0
primCone = 0
primCube = 0
primCylinder = 0
primPyramid = 0
primRingEighth = 0
primRingFull = 0
primRingHalf = 0
primRingQuarter = 0
primSphere = 0
primTriangle = 0
#Q
#R
radarBall = 0
radarBallMP = 0
radarTowerSmall = 0
radarTowerSmallMP = 0
ramp = 0
rampTransition = 0
rockHalfCoverA = 0
rockHalfCoverB = 0
#S
shutterDoorsMP = 0
signalAntenna = 0
singleDoorwayA = 0
singleDoorwayB = 0
sixBysixRoundColumnC = 0
sixBysixRoundColumnD = 0
sixBysixSquareColumnA = 0
sixBysixSquareColumnB = 0
#T
tireBald = 0
tireBaldMP = 0
tireBaldwWheel = 0
tireBaldwWheelMP = 0
tirewTread = 0
tirewTreadMP = 0
tirewWheel = 0
tirewWheelMP = 0
twoBytwoRoundColumnC = 0
twoBytwoRoundColumnD = 0
twoBytwoSquareColumnA = 0
twoBytwoSquareColumnB = 0
#U
uhfAntenna = 0
uhfAntennaMP = 0
unscAntennaBoom = 0
unscAntennaBoomMP = 0
unscBarrel = 0
unscBarrelMP = 0
unscDuffleBagMP = 0
unscRadarUnit = 0
unscSatelliteDishMounted = 0
unscSatelliteDishMountedMP = 0
unscSatelliteDishPortable = 0
unscSatelliteDishPortableMP = 0
unscSatelliteDishTrailer = 0
#V
#W
wallCubeAngled = 0
wallCubeCornerAngled = 0
wallCubeStandard = 0
wallDoubleWindowA = 0
wallDoubleWindowB = 0
wallHalf = 0
wallStandardA = 0
wallStandardB = 0
wallWindowA = 0
wallWindowB = 0
waterBarrel = 0
wheel = 0
wheelMP = 0
#X
#Y
#Z
##### Item Count Dictionary Start

def initSorter(parentPath):
    path = parentPath

    with open(path, "r") as f:
        response = f.read()
        response_json = json.loads(response)

    item_List = response_json['itemList']

    #A
    global angledCornerWallStandard
    global angledDoubleDoorway
    global angledSingleDoorway
    global angledWallDoubleWindowA
    global angledWallDoubleWindowB
    global angledWallDoubleWindowC
    global angledWallStandardA
    global angledWallStandardB
    global angledWallWindowA
    global angledWallWindowB
    global angledWallWindowC
    global angleWallHalf
    global ankleCoverHalfSize
    global ankleCoverQuarterSize
    #B
    #C
    global cornerRampEighthA
    global cornerRampEighthB
    global cornerWallStandard
    global curvedDoubleDoorway
    global curvedDoubleWindowWallA
    global curvedDoubleWindowWallB
    global curvedRailingHalfSize
    global curvedRailingStandardSize
    global curvedRampStandardRight
    global curvedWallDouble
    global curvedWallStandard
    global curvedWallTriple
    #D
    global doubleDoorway
    #E
    global eightByeightCrate
    global eightBysixteenCrate
    global erodedTerrainD
    #F
    global floorAngledStandardA
    global floorAngledStandardB
    global floorHalfA
    global floorHalfB
    global floorQuadrupleSize
    global floorStandard
    global forerunnerDoorway
    global forerunnerDoorwayWide
    global fourByeightCrate
    global fourDotFivebyEightCrate
    global fourByfourCrate
    global fourByfourRoundColumnC
    global fourByfourRoundColumnD
    global fourByfourSquareColumnA
    global fourByfourSquareColumnB
    global fourWayRampEighth
    global fullCoverHalfSize
    global fullCoverStandardSize
    #G
    #H
    global halfCoverHalfSize
    global halfCoverStandardSize
    #I
    #J
    #K
    #L
    #M
    #N
    #O
    global oneOverThreeRampEighthA
    global oneOverThreeRampEighthB
    global oneOverThreeRampHalfA
    global oneOverThreeRampHalfB
    global oneOverThreeRampHalfC
    global oneOverThreeRampQuarter
    global oneOverThreeRampSixteenth
    global oneOverThreeRampStandardA
    global oneOverThreeRampStandardB
    global oneOverFourRampHalfA
    global oneOverFourRampHalfB
    #P
    global playerScaleObject
    global primCone
    global primCube
    global primCylinder
    global primPyramid
    global primRingEighth
    global primRingFull
    global primRingHalf
    global primRingQuarter
    global primSphere
    global primTriangle
    #Q
    #R
    global ramp
    global rampTransition
    global rockHalfCoverA
    global rockHalfCoverB
    #S
    global singleDoorwayA
    global singleDoorwayB
    global sixBysixRoundColumnC
    global sixBysixRoundColumnD
    global sixBysixSquareColumnA
    global sixBysixSquareColumnB
    #T
    global twoBytwoRoundColumnC
    global twoBytwoRoundColumnD
    global twoBytwoSquareColumnA
    global twoBytwoSquareColumnB 
    #U
    #V
    #W
    global wallCubeAngled
    global wallCubeCornerAngled
    global wallCubeStandard
    global wallDoubleWindowA
    global wallDoubleWindowB
    global wallHalf
    global wallStandardA
    global wallStandardB
    global wallWindowA
    global wallWindowB
    #X
    #Y
    #Z

    for object in item_List:
        if str({object['itemId']}).find("-612639225") == True:
            angledCornerWallStandard += 1

        if str({object['itemId']}).find("-1843159215") == True:
            angledDoubleDoorway += 1

        if str({object['itemId']}).find("-2102390651") == True:
            angledSingleDoorway += 1

        if str({object['itemId']}).find("691693133") == True:
            angledWallDoubleWindowA += 1

        if str({object['itemId']}).find("1103502387") == True:
            angledWallDoubleWindowB += 1

        if str({object['itemId']}).find("1383537765") == True:
            angledWallDoubleWindowC += 1

        if str({object['itemId']}).find("-41069292") == True:
            angledWallStandardA += 1

        if str({object['itemId']}).find("1361150846") == True:
            angledWallStandardB += 1

        if str({object['itemId']}).find("-979944560") == True:
            angledWallWindowA += 1

        if str({object['itemId']}).find("-147813598") == True:
            angledWallWindowB += 1

        if str({object['itemId']}).find("1416644323") == True:
            angledWallWindowC += 1

        if str({object['itemId']}).find("1168502040") == True:
            angleWallHalf += 1

        if str({object['itemId']}).find("-1804795714") == True:
            ankleCoverHalfSize += 1

        if str({object['itemId']}).find("-157703089") == True:
            ankleCoverQuarterSize += 1

        if str({object['itemId']}).find("1969407375") == True:
            cornerRampEighthA += 1

        if str({object['itemId']}).find("1451712685") == True:
            cornerRampEighthB += 1

        if str({object['itemId']}).find("-173471027") == True:
            cornerWallStandard += 1

        if str({object['itemId']}).find("1760817474") == True:
            curvedDoubleDoorway += 1

        if str({object['itemId']}).find("-936420252") == True:
            curvedDoubleWindowWallA += 1

        if str({object['itemId']}).find("1662288531") == True:
            curvedDoubleWindowWallB += 1

        if str({object['itemId']}).find("2140930404") == True:
            curvedRailingHalfSize += 1

        if str({object['itemId']}).find("-191674833") == True:
            curvedRampStandardRight += 1

        if str({object['itemId']}).find("-341801782") == True:
            curvedWallDouble += 1

        if str({object['itemId']}).find("-960331706") == True:
            curvedWallStandard += 1

        if str({object['itemId']}).find("-1332366101") == True:
            curvedWallTriple += 1

        if str({object['itemId']}).find("759775548") == True:
            doubleDoorway += 1

        if str({object['itemId']}).find("-89276352") == True:
            eightByeightCrate += 1

        if str({object['itemId']}).find("355942414") == True:
            eightBysixteenCrate += 1
        
        if str({object['itemId']}).find("-1835432896") == True:
            erodedTerrainD += 1 

        if str({object['itemId']}).find("2119916132") == True:
            floorAngledStandardA += 1

        if str({object['itemId']}).find("471557513") == True:
            floorAngledStandardB += 1

        if str({object['itemId']}).find("-1554062464") == True:
            floorHalfA += 1

        if str({object['itemId']}).find("-319219211") == True:
            floorHalfB += 1

        if str({object['itemId']}).find("1561437000") == True:
            floorQuadrupleSize += 1

        if str({object['itemId']}).find("796754322") == True:
            floorStandard += 1

        if str({object['itemId']}).find("-983151539") == True:
            forerunnerDoorway += 1

        if str({object['itemId']}).find("492327815") == True:
            forerunnerDoorwayWide += 1
        
        if str({object['itemId']}).find("-1137520810") == True:
            fourByeightCrate += 1

        if str({object['itemId']}).find("491753301") == True:
            fourDotFivebyEightCrate += 1

        if str({object['itemId']}).find("253727975") == True:
            fourByfourCrate += 1

        if str({object['itemId']}).find("-1422631181") == True:
            fourByfourRoundColumnC += 1

        if str({object['itemId']}).find("1947532949") == True:
            fourByfourRoundColumnD += 1

        if str({object['itemId']}).find("2083372609") == True:
            fourByfourSquareColumnA += 1

        if str({object['itemId']}).find("1607542385") == True:
            fourByfourSquareColumnB += 1

        if str({object['itemId']}).find("1150132444") == True:
            fourWayRampEighth += 1

        if str({object['itemId']}).find("2115878081") == True:
            fullCoverHalfSize += 1

        if str({object['itemId']}).find("-2030691315") == True:
            fullCoverStandardSize += 1

        if str({object['itemId']}).find("286176533") == True:
            halfCoverHalfSize += 1

        if str({object['itemId']}).find("1040169826") == True:
            halfCoverStandardSize += 1

        if str({object['itemId']}).find("-588839424") == True:
            oneOverThreeRampEighthA += 1

        if str({object['itemId']}).find("908393824") == True:
            oneOverThreeRampEighthB += 1

        if str({object['itemId']}).find("-1844206092") == True:
            oneOverThreeRampHalfA += 1

        if str({object['itemId']}).find("707549041") == True:
            oneOverThreeRampHalfB += 1

        if str({object['itemId']}).find("715160887") == True:
            oneOverThreeRampHalfC += 1

        if str({object['itemId']}).find("-1765693041") == True:
            oneOverThreeRampQuarter += 1

        if str({object['itemId']}).find("-984668480") == True:
            oneOverThreeRampSixteenth += 1

        if str({object['itemId']}).find("468997533") == True:
            oneOverThreeRampStandardA += 1

        if str({object['itemId']}).find("1765455307") == True:
            oneOverThreeRampStandardB += 1

        if str({object['itemId']}).find("1461903299") == True:
            oneOverFourRampHalfA += 1

        if str({object['itemId']}).find("-152113334") == True:
            oneOverFourRampHalfB += 1

        if str({object['itemId']}).find("-234187719") == True:
            primCone += 1
            
        if str({object['itemId']}).find("1759788903") == True:
            primCube += 1
            
        if str({object['itemId']}).find("728515706") == True:
            primCylinder += 1
            
        if str({object['itemId']}).find("1189747031") == True:
            primPyramid += 1
            
        if str({object['itemId']}).find("-1706009392") == True:
            primRingEighth += 1
            
        if str({object['itemId']}).find("-1190828000") == True:
            primRingFull += 1
            
        if str({object['itemId']}).find("-1298054065") == True:
            primRingHalf += 1
            
        if str({object['itemId']}).find("1875914002") == True:
            primRingQuarter += 1
            
        if str({object['itemId']}).find("-457712308") == True:
            primSphere += 1
            
        if str({object['itemId']}).find("-1185205223") == True:
            primTriangle += 1
            
        if str({object['itemId']}).find("1635203824") == True:
            curvedRailingStandardSize += 1
            
        if str({object['itemId']}).find("631526139") == True:
            ramp += 1
            
        if str({object['itemId']}).find("1530590479") == True:
            rampTransition += 1
            
        if str({object['itemId']}).find("902995208") == True:
            rockHalfCoverA += 1
            
        if str({object['itemId']}).find("2050581668") == True:
            rockHalfCoverB += 1
            
        if str({object['itemId']}).find("652937498") == True:
            singleDoorwayA += 1
            
        if str({object['itemId']}).find("1989569474") == True:
            singleDoorwayB += 1
            
        if str({object['itemId']}).find("1553385688") == True:
            sixBysixRoundColumnC += 1
            
        if str({object['itemId']}).find("222107335") == True:
            sixBysixRoundColumnD += 1
            
        if str({object['itemId']}).find("-446137873") == True:
            sixBysixSquareColumnA += 1
            
        if str({object['itemId']}).find("727360123") == True:
            sixBysixSquareColumnB += 1
            
        if str({object['itemId']}).find("-1108230827") == True:
            twoBytwoRoundColumnC += 1
            
        if str({object['itemId']}).find("-885874693") == True:
            twoBytwoRoundColumnD += 1
            
        if str({object['itemId']}).find("2096053754") == True:
            twoBytwoSquareColumnA += 1

        if str({object['itemId']}).find("-1294229133") == True:
            twoBytwoSquareColumnB += 1

        if str({object['itemId']}).find("101094355") == True:
            wallCubeAngled += 1
            
        if str({object['itemId']}).find("-2128852445") == True:
            wallCubeCornerAngled += 1
            
        if str({object['itemId']}).find("-1168178900") == True:
            wallCubeStandard += 1
            
        if str({object['itemId']}).find("1662815138") == True:
            wallDoubleWindowA += 1
            
        if str({object['itemId']}).find("-2011335511") == True:
            wallDoubleWindowB += 1
            
        if str({object['itemId']}).find("-1513962159") == True:
            wallHalf += 1
            
        if str({object['itemId']}).find("1047093426") == True:
            wallStandardA += 1
            
        if str({object['itemId']}).find("-1459663496") == True:
            wallStandardB += 1
            
        if str({object['itemId']}).find("-725006759") == True:
            wallWindowA += 1
            
        if str({object['itemId']}).find("1064263013") == True:
            wallWindowB += 1

        if str({object['itemId']}).find("2062928760") == True:
            playerScaleObject += 1

    if (angledCornerWallStandard) > 0:
        print("Found number of Angled Corner Wall Standard(s): {}".format(angledCornerWallStandard))
    if (angledDoubleDoorway) > 0:
        print("Found number of Angled Double Doorway(s): {}".format(angledDoubleDoorway))
    if (angledSingleDoorway) > 0:
        print("Found number of Angled Single Doorway(s): {}".format(angledSingleDoorway))
    if (angledWallDoubleWindowA) > 0:
        print("Found number of Angled Wall Double Window A(s): {}".format(angledWallDoubleWindowA))
    if (angledWallDoubleWindowB) > 0:
        print("Found number of Angled Wall Double Window B(s): {}".format(angledWallDoubleWindowB))
    if (angledWallDoubleWindowC) > 0:
        print("Found number of Angled Wall Double Window C(s): {}".format(angledWallDoubleWindowC))
    if (angledWallStandardA) > 0:
        print("Found number of Angled Wall Standard A(s): {}".format(angledWallStandardA))
    if (angledWallStandardB) > 0:
        print("Found number of Angled Wall Standard B(s): {}".format(angledWallStandardB))
    if (angledWallWindowA) > 0:
        print("Found number of Angled Wall Window A(s): {}".format(angledWallWindowA))
    if (angledWallWindowB) > 0:
        print("Found number of Angled Wall Window B(s): {}".format(angledWallWindowB))
    if (angledWallWindowC) > 0:
        print("Found number of Angled Wall Window C(s): {}".format(angledWallWindowC))
    if (angleWallHalf) > 0:
        print("Found number of Angle Wall Half(s): {}".format(angleWallHalf))
    if (ankleCoverHalfSize) > 0:
        print("Found number of Ankle Cover Half Size(s): {}".format(ankleCoverHalfSize))
    if (ankleCoverQuarterSize) > 0:
        print("Found number of Ankle Cover Quarter Size(s): {}".format(ankleCoverQuarterSize))
    if (cornerRampEighthA) > 0:
        print("Found number of Corner Ramp Eighth A(s): {}".format(cornerRampEighthA))
    if (cornerRampEighthB) > 0:
        print("Found number of Corner Ramp Eighth B(s): {}".format(cornerRampEighthB))
    if (cornerWallStandard) > 0:
        print("Found number of Corner Wall Standard(s): {}".format(cornerWallStandard))
    if (curvedDoubleDoorway) > 0:
        print("Found number of Curved Double Doorway(s): {}".format(curvedDoubleDoorway))
    if (curvedDoubleWindowWallA) > 0:
        print("Found number of Curved Double Window Wall A(s): {}".format(curvedDoubleWindowWallA))
    if (curvedDoubleWindowWallB) > 0:
        print("Found number of Curved Double Window Wall B(s): {}".format(curvedDoubleWindowWallB))
    if (curvedRailingHalfSize) > 0:
        print("Found number of Curved Railing Half Size(s): {}".format(curvedRailingHalfSize))
    if (curvedRailingStandardSize) > 0:
        print("Found number of Curved Railing Standard Size(s): {}".format(curvedRailingStandardSize))
    if (curvedWallStandard) > 0:
        print("Found number of Curved Wall Standard(s): {}".format(curvedWallStandard))
    if (curvedWallDouble) > 0:
        print("Found number of Curved Wall Double(s): {}".format(curvedWallDouble))
    if (curvedWallTriple) > 0:
        print("Found number of Curved Wall Triple(s): {}".format(curvedWallTriple))
    if (doubleDoorway) > 0:
        print("Found number of Double Doorway(s): {}".format(doubleDoorway))
    if (eightByeightCrate) > 0:
        print("Found number of 8x8 Crate(s): {}".format(eightByeightCrate))
    if (eightBysixteenCrate) > 0:
        print("Found number of 8x16 Crate(s): {}".format(eightBysixteenCrate))
    if (floorAngledStandardA) > 0:
        print("Found number of Floor Angled Standard A(s): {}".format(floorAngledStandardA))
    if (floorAngledStandardB) > 0:
        print("Found number of Floor Angled Standard B(s): {}".format(floorAngledStandardB))
    if (floorHalfA) > 0:
        print("Found number of Floor Half A(s): {}".format(floorHalfA))
    if (floorHalfB) > 0:
        print("Found number of Floor Half B(s): {}".format(floorHalfB))
    if (floorQuadrupleSize) > 0:
        print("Found number of Floor Quadruple Size(s): {}".format(floorQuadrupleSize))
    if (floorStandard) > 0:
        print("Found number of Floor Standard(s): {}".format(floorStandard))
    if (forerunnerDoorway) > 0:
        print("Found number of Forerunner Doorway(s): {}".format(forerunnerDoorway))
    if (forerunnerDoorwayWide) > 0:
        print("Found number of Forerunner Doorway Wide(s): {}".format(forerunnerDoorwayWide))
    if (fourByeightCrate) > 0:
        print("Found number of 4x8 Crate (s): {}".format(fourByeightCrate))
    if (fourDotFivebyEightCrate) > 0:
        print("Found number of 4x5x8 Crate(s): {}".format(fourDotFivebyEightCrate))
    if (fourByfourCrate) > 0:
        print("Found number of 4x4 Crate(s): {}".format(fourByfourCrate))
    if (fourByfourRoundColumnC) > 0:
        print("Found number of 4x4 Round Column C(s): {}".format(fourByfourRoundColumnC))
    if (fourByfourRoundColumnD) > 0:
        print("Found number of 4x4 Round Column D(s): {}".format(fourByfourRoundColumnD))
    if (fourByfourSquareColumnA) > 0:
        print("Found number of 4x4 Square Column A(s): {}".format(fourByfourSquareColumnA))
    if (fourByfourSquareColumnB) > 0:
        print("Found number of 4x4 Square Column B(s): {}".format(fourByfourSquareColumnB))
    if (fourWayRampEighth) > 0:
        print("Found number of Four Way Ramp Eighth(s): {}".format(fourWayRampEighth))
    if (fullCoverHalfSize) > 0:
        print("Found number of Full Cover Half Size(s): {}".format(fullCoverHalfSize))
    if (fullCoverStandardSize) > 0:
        print("Found number of Full Cover Standard Size(s): {}".format(fullCoverStandardSize))
    if (halfCoverHalfSize) > 0:
        print("Found number of Half Cover Half Size(s): {}".format(halfCoverHalfSize))
    if (halfCoverStandardSize) > 0:
        print("Found number of Half Cover Standard Size(s): {}".format(halfCoverStandardSize))
    if (oneOverThreeRampEighthA) > 0:
        print("Found number of 1/3 Ramp Eighth A(s): {}".format(oneOverThreeRampEighthA))
    if (oneOverThreeRampEighthB) > 0:
        print("Found number of 1/3 Ramp Eighth B(s): {}".format(oneOverThreeRampEighthB))
    if (oneOverThreeRampHalfA) > 0:
        print("Found number of 1/3 Ramp Half A(s): {}".format(oneOverThreeRampHalfA))
    if (oneOverThreeRampHalfB) > 0:
        print("Found number of 1/3 Ramp Half B(s): {}".format(oneOverThreeRampHalfB))
    if (oneOverThreeRampHalfC) > 0:
        print("Found number of 1/3 Ramp Half C(s): {}".format(oneOverThreeRampHalfC))
    if (oneOverThreeRampQuarter) > 0:
        print("Found number of 1/3 Ramp Quarter(s): {}".format(oneOverThreeRampQuarter))
    if (oneOverThreeRampSixteenth) > 0:
        print("Found number of 1/3 Ramp Sixteenth(s): {}".format(oneOverThreeRampSixteenth))
    if (oneOverThreeRampStandardA) > 0:
        print("Found number of 1/3 Ramp Standard A(s): {}".format(oneOverThreeRampStandardA))
    if (oneOverThreeRampStandardB) > 0:
        print("Found number of 1/3 Ramp Standard B(s): {}".format(oneOverThreeRampStandardB))
    if (oneOverFourRampHalfA) > 0:
        print("Found number of 1/4 Ramp Half A(s): {}".format(oneOverFourRampHalfA))
    if (oneOverFourRampHalfB) > 0:
        print("Found number of 1/4 Ramp Half B(s): {}".format(oneOverFourRampHalfB))
    if (primCone) > 0:
        print("Found number of Primitive Cone(s): {}".format(primCone))
    if (primCube) > 0:
        print("Found number of Primitive Cube(s): {}".format(primCube))
    if (primCylinder) > 0:
        print("Found number of Primitive Cylinder(s): {}".format(primCylinder))
    if (primPyramid) > 0:
        print("Found number of Primitive Pyramid(s): {}".format(primPyramid))
    if (primRingEighth) > 0:
        print("Found number of Primitive Ring Eighth(s): {}".format(primRingEighth))
    if (primRingFull) > 0:
        print("Found number of Primitive Ring Full(s): {}".format(primRingFull))
    if (primRingHalf) > 0:
        print("Found number of Primitive Ring Half(s): {}".format(primRingHalf))
    if (primRingQuarter) > 0:
        print("Found number of Primitive Ring Quarter(s): {}".format(primRingQuarter))
    if (primSphere) > 0:
        print("Found number of Primivite Sphere(s): {}".format(primSphere))
    if (primTriangle) > 0:
        print("Found number of Primitive Triangle(s): {}".format(primTriangle))
    if (rockHalfCoverA) > 0:
        print("Found number of Rock Half Cover A(s): {}".format(rockHalfCoverA))
    if (rockHalfCoverB) > 0:
        print("Found number of Rock Half Cover B(s): {}".format(rockHalfCoverB))
    if (singleDoorwayA) > 0:
        print("Found number of Single Doorway A(s): {}".format(singleDoorwayA))
    if (singleDoorwayB) > 0:
        print("Found number of Single Doorway B(s): {}".format(singleDoorwayB))
    if (sixBysixRoundColumnC) > 0:
        print("Found number of 6x6 Round Column C(s): {}".format(sixBysixRoundColumnC))
    if (sixBysixRoundColumnD) > 0:
        print("Found number of 6x6 Round Column D(s): {}".format(sixBysixRoundColumnD))
    if (sixBysixSquareColumnA) > 0:
        print("Found number of 6x6 Square Column A(s): {}".format(sixBysixSquareColumnA))
    if (sixBysixSquareColumnB) > 0:
        print("Found number of 6x6 Square Column B(s): {}".format(sixBysixSquareColumnB))
    if (twoBytwoRoundColumnC) > 0:
        print("Found number of 2x2 Round Column C(s): {}".format(twoBytwoRoundColumnC))
    if (twoBytwoRoundColumnD) > 0:
        print("Found number of 2x2 Round Column D(s): {}".format(twoBytwoRoundColumnD))
    if (twoBytwoSquareColumnA) > 0:
        print("Found number of 2x2 Square Column A(s): {}".format(twoBytwoSquareColumnA))
    if (twoBytwoSquareColumnB) > 0:
        print("Found number of 2x2 Square Column B(s): {}".format(twoBytwoSquareColumnB))
    if (wallCubeAngled) > 0:
        print("Found number of Wall Cube Angled(s): {}".format(wallCubeAngled))
    if (wallCubeCornerAngled) > 0:
        print("Found number of Wall Cube Corner Angled(s): {}".format(wallCubeCornerAngled))
    if (wallCubeStandard) > 0:
        print("Found number of Wall Cube Standard(s): {}".format(wallCubeStandard))
    if (wallDoubleWindowA) > 0:
        print("Found number of Wall Double Window A(s): {}".format(wallDoubleWindowA))
    if (wallDoubleWindowB) > 0:
        print("Found number of Wall Double Window B(s): {}".format(wallDoubleWindowB))
    if (wallHalf) > 0:
        print("Found number of Wall Half(s): {}".format(wallHalf))
    if (wallStandardA) > 0:
        print("Found number of Wall Standard A(s): {}".format(wallStandardA))
    if (wallStandardB) > 0:
        print("Found number of Wall Standard B(s): {}".format(wallStandardB))
    if (wallWindowA) > 0:
        print("Found number of Wall Window A(s): {}".format(wallWindowA))
    if (wallWindowB) > 0:
        print("Found number of Wall Window B(s): {}".format(wallWindowB))
    if (playerScaleObject) > 0:
        print("Found number of Player Scale Object(s) {}".format(playerScaleObject))


def sortItems(item_List):

    for object in item_List:
        if str({object['objectName']}).find("Playspace") == True:
            del item_List[item_List.index(object)]
        if str({object['objectName']}).find("Global Reflection Position") == True:
            del item_List[item_List.index(object)]
        if str({object['itemId']}).find("666") == True:
            del item_List[item_List.index(object)]

    if len(item_List) <= 1:
        return item_List
    else:
        sortedList = sorted(item_List, key= lambda k: k["itemId"])
    return sortedList