# Program by Jonathan Kleehammer 9-10-19
# Program is designed to simulate DnD 5e treasure hoards from pages 137-138 of the DMG
# Only simulates the gold because the other values are generated/picked elsewhere
# also takes in a number of players so that the money is evenly divisible

import random
import sys

# global variables of all the gems by value
gem10 = ('Azurite (opaque mottled deep blue)',
         'Banded agate (translucent striped brown, blue, white, or red)',
         'Blue quartz (transparent pale blue)',
         'Eye agate (translucent circles of gray, white, brown, blue, or green)',
         'Hematite (opaque gray-black)',
         'Lapis lazuli (opaque light and dark blue with yellow flecks)',
         'Malachite (opaque striated light and dark green)',
         'Moss agate (translucent pink or yellow-white with mossy gray or green markings)',
         'Obsidian (opaque black)', 'Rhodochrosite (opaque light pink)',
         'Tiger eye (translucent brown with golden center)',
         'Turquoise (opaque light blue-green)')

gem50 = ('Bloodstone (opaque dark gray with red flecks)',
         'Carnelian (opaque orange to red-brown)',
         'Chalcedony (opaque white)',
         'Chrysoprase (translucent green)',
         'Citrine (transparent pale yellow-brown)',
         'Jasper (opaque blue, black, or brown)',
         'Moonstone (translucent white with pale blue glow)',
         'Onyx (opaque bands of black and white, or pure black or white)',
         'Quartz (transparent white, smoky gray, or yellow)',
         'Sardonyx (opaque bands of red and white)',
         'Star rose quartz (translucent rosy stone with white star-shaped center)',
         'Zircon (transparent pale blue-green)')

gem100 = ('Amber (transparent watery gold to rich gold)',
          'Amethyst (transparent deep purple)',
          'Chrysoberyl (transparent yellow-green to pale green)',
          'Coral (opaque crimson)',
          'Garnet (transparent red, brown-green, or violet)',
          'jade (translucent light green, deep green, or white)',
          'jet (opaque deep black)',
          'Pearl (opaque lustrous white, yellow, or pink)',
          'Spinel (transparent red, red-brown, or deep green)',
          'Tourmaline (transparent pale green, blue, brown, or red)')

gem500 = ('Alexandrite (transparent dark green)',
          'Aquamarine (transparent pale blue-green)',
          'Black pearl (opaque pure black)',
          'Blue spinel (transparent deep blue)',
          'Peridot (transparent rich olive green)',
          'Topaz (transparent golden yellow)')

gem1000 = ('Black opal (translucent dark green with black mottling and golden flecks)',
           'Blue sapphire (transparent blue-white to medium blue)',
           'Emerald (transparent deep bright green)',
           'Fire opal (translucent fiery red)',
           'Opal (translucent pale blue with green and golden mottling)',
           'Star ruby (translucent ruby with white star-shaped center)',
           'Star sapphire (translucent blue sapphire with white star-shaped center)',
           'Yellow sapphire (transparent fiery yellow or yellow· green)')

gem5000 = ('Black sapphire (translucent lustrous black with glowing highlights)',
           'Diamond (transparent blue-white, canary, pink, brown, or blue)',
           'Jacinth (transparent fiery orange)',
           'Ruby (transparent clear red to deep crimson)')

art25 = ('Silver ewer',
         'Carved bone statuette',
         'Small gold bracelet',
         'Cloth-of-gold vestments',
         'Black velvet mask stitched with silver thread',
         'Copper chalice with silver filigree',
         'Pair of engraved bone dice',
         'Small mirror set in a painted wooden frame',
         'Embroidered silk handkerchief',
         'Gold locket with a painted portrait inside')

art250 = ('Gold ring set with bloodstones',
          'Carved ivory statuette',
          'Large gold bracelet',
          'Silver necklace with a gemstone pendant',
          'Bronze crown',
          'Silk robe with gold embroidery',
          'Large well-made tapestry',
          'Brass mug with jade inlay',
          'Box of turquoise animal figurines',
          'Gold bird cage with electrum filigree')

art750 = ('Silver chalice set with moonstones',
          'Silver-plated steellongsword with jet set in hilt',
          'Carved harp of exotic wood with ivory inlay and zircon gems',
          'Small gold idol',
          'Gold dragon comb set with red garnets as eyes',
          'Bottle stopper cork embossed with gold leaf and set with amethysts',
          'Ceremonial electrum dagger wit~ a black pearl in the pommel',
          'Silver and gold brooch',
          'Obsidian statuette with gold fittings and inlay',
          'Painted gold war mask')

art2500 = ('Fine gold chain set with a fire opal',
           'Old masterpiece painting',
           'Embroidered silk and velvet mantle set with numerous moonstones',
           'Platinum bracelet set with a sapphire',
           'Embroidered glove set with jewel chips',
           'jeweled anklet',
           'Gold music box',
           'Gold circlet set with four aquamarines',
           'Eye patch with a mock eye set in blue sapphire and moonstone',
           'A necklace string of small pink pearls')

art7500 = ('Jeweled gold crown',
           'jeweled platinum ring',
           'Small gold statuette set with rubies',
           'Gold cup set with emeralds',
           'Gold jewelry box with platinum filigree',
           'Painted gold child\'s sarcophagus',
           'jade game board with solid gold playing pieces',
           'Bejeweled ivory drinking horn with gold filigree')

# takes in a dice string (3d6, 4d8, 2d4, etc) and returns an integer for what was rolled
def diceroller(diceString):
    diceCount, diceType = diceString.split('d')

    diceCount = int(diceCount)
    diceType = int(diceType) + 1 #adding 1 for when when we choose a random number

    rollSum = 0
    for i in range(diceCount):
        rollSum += random.randrange(1, diceType)

    return rollSum


# coin types are either 's' for silver 'g' for gold 'p' for platinum, we're not using e for electrum
def convertToCopper(coinType, amount):
    if coinType == 's':
        return amount * 10
    elif coinType == 'g':
        return amount * 100
    elif coinType == 'p':
        return amount * 1000

# takes in an amount of copper then returns a string value of the formatted currency
def simplifyCurrency(copperSum):
    copperSum = str(copperSum)

    copper = int(copperSum[-1])
    silver = 0
    gold = 0
    platinum = 0

    if len(copperSum) > 1:
        silver = int(copperSum[-2])
    if len(copperSum) > 2:
        gold = int(copperSum[:-2])
        if gold > 500:
            platinum = int(gold / 500) * 50
            gold -= platinum * 10

    simpleString = ''
    if platinum > 0:
        simpleString += str(platinum) + 'pp'
    if gold > 0:
        if len(simpleString) > 0:
            simpleString += ' '
        simpleString += str(gold) + 'gp'
    if silver > 0:
        if len(simpleString) > 0:
            simpleString += ' '
        simpleString += str(silver) + 'sp'
    if copper > 0:
        if len(simpleString) > 0:
            simpleString += ' '
        simpleString += str(copper) + 'cp'
    return simpleString
# returns a random gem with specified gp value
def getSwagType(value):
    if value == 10:
        return random.choice(gem10)
    elif value == 25:
        return random.choice(art25)
    elif value == 50:
        return random.choice(gem50)
    elif value == 100:
        return random.choice(gem100)
    elif value == 250:
        return random.choice(art250)
    elif value == 500:
        return random.choice(gem500)
    elif value == 750:
        return random.choice(art750)
    elif value == 1000:
        return random.choice(gem1000)
    elif value == 2500:
        return random.choice(art2500)
    elif value == 5000:
        return random.choice(gem5000)
    elif value == 7500:
        return random.choice(art7500)


# art or gems for treasure hoard 0 (CR 0-4)
# return (count) (type) (individualValue)
def swag0():
    # s is our swag level, from 1-100
    s = diceroller('1d100')
    c = 0 #count of swag
    iValue = 0
    if s <= 6:
        pass
    elif s <= 16:
        # should return 2d6 10gp gems
        c = diceroller('2d6')  # count of how many of these objects were returned
        iValue = 10 # individual value = 10 gp value
    elif s <= 26:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 36:
        c = diceroller('2d6')
        iValue = 50
    elif s <= 44:
        c = diceroller('2d6')
        iValue = 10
    elif s <= 52:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 60:
        c = diceroller('2d6')
        iValue = 50
    elif s <= 65:
        c = diceroller('2d6')
        iValue = 10
    elif s <= 70:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 75:
        c = diceroller('2d6')
        iValue = 50
    elif s <= 78:
        c = diceroller('2d6')
        iValue = 10
    elif s <= 80:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 85:
        c = diceroller('2d6')
        iValue = 50
    elif s <= 92:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 97:
        c = diceroller('2d6')
        iValue = 50
    elif s <= 99:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 100:
        c = diceroller('2d6')
        iValue = 50

    swagType = getSwagType(iValue)
    return c, swagType, iValue

def swag1():
    # s is our swag level, from 1-100
    s = diceroller('1d100')
    c = 0 # count of swag
    iValue = 0 # individual value
    if s <= 4:
        pass
    elif s <= 10:
        # should return 2d6 10gp gems
        c = diceroller('2d4')  # count of how many of these objects were returned
        iValue = 25 # individual value = 25 gp value
    elif s <= 16:
        c = diceroller('3d6')
        iValue = 50
    elif s <= 22:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 28:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 32:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 36:
        c = diceroller('3d6')
        iValue = 50
    elif s <= 40:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 44:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 49:
        c = diceroller('2d4')
        iValue = 24
    elif s <= 54:
        c = diceroller('3d6')
        iValue = 50
    elif s <= 59:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 63:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 66:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 69:
        c = diceroller('3d6')
        iValue = 50
    elif s <= 72:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 74:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 76:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 78:
        c = diceroller('3d6')
        iValue = 50
    elif s <= 79:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 80:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 84:
        c = diceroller('2d4')
        iValue = 25
    elif s <= 88:
        c = diceroller('3d6')
        iValue = 50
    elif s <= 91:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 94:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 96:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 98:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 99:
        c = diceroller('3d6')
        iValue = 100
    elif s <= 100:
        c = diceroller('2d4')
        iValue = 250

    swagType = getSwagType(iValue)
    return c, swagType, iValue

def swag2():
    # s is our swag level, from 1-100
    s = diceroller('1d100')
    c = 0  # count of swag
    iValue = 0  # individual value
    if s <= 3:
        pass
    elif s <= 6:
        # should return 2d6 10gp gems
        c = diceroller('2d4')  # count of how many of these objects were returned
        iValue = 250  # individual value = 25 gp value
    elif s <= 9:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 12:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 15:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 19:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 23:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 26:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 29:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 35:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 40:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 45:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 50:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 54:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 58:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 62:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 66:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 68:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 70:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 72:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 74:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 76:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 78:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 80:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 82:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 85:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 88:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 90:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 92:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 94:
        c = diceroller('2d4')
        iValue = 250
    elif s <= 96:
        c = diceroller('2d4')
        iValue = 750
    elif s <= 98:
        c = diceroller('3d6')
        iValue = 500
    elif s <= 100:
        c = diceroller('3d6')
        iValue = 1000

    swagType = getSwagType(iValue)
    return c, swagType, iValue

def swag3():
    # s is our swag level, from 1-100
    s = diceroller('1d100')
    c = 0  # count of swag
    iValue = 0  # individual value
    if s <= 2:
        pass
    elif s <= 5:
        # should return 2d6 10gp gems
        c = diceroller('3d6')  # count of how many of these objects were returned
        iValue = 1000  # individual value = 25 gp value
    elif s <= 8:
        c = diceroller('1d10')
        iValue = 2500
    elif s <= 11:
        c = diceroller('1d4')
        iValue = 7500
    elif s <= 14:
        c = diceroller('1d8')
        iValue = 5000
    elif s <= 22:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 30:
        c = diceroller('1d10')
        iValue = 2500
    elif s <= 38:
        c = diceroller('1d4')
        iValue = 7500
    elif s <= 46:
        c = diceroller('1d8')
        iValue = 5000
    elif s <= 52:
        c = diceroller('3d6')
        iValue = 2500
    elif s <= 58:
        c = diceroller('1d10')
        iValue = 1000
    elif s <= 63:
        c = diceroller('1d4')
        iValue = 7500
    elif s <= 68:
        c = diceroller('1d8')
        iValue = 5000
    elif s <= 69:
        c = diceroller('3d6')
        iValue = 2500
    elif s <= 70:
        c = diceroller('1d10')
        iValue = 1000
    elif s <= 71:
        c = diceroller('1d4')
        iValue = 7500
    elif s <= 72:
        c = diceroller('1d8')
        iValue = 5000
    elif s <= 74:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 76:
        c = diceroller('1d10')
        iValue = 2500
    elif s <= 78:
        c = diceroller('1d4')
        iValue = 7500
    elif s <= 80:
        c = diceroller('1d8')
        iValue = 5000
    elif s <= 85:
        c = diceroller('3d6')
        iValue = 1000
    elif s <= 90:
        c = diceroller('1d10')
        iValue = 2500
    elif s <= 95:
        c = diceroller('1d4')
        iValue = 7500
    elif s <= 100:
        c = diceroller('1d8')
        iValue = 5000

    swagType = getSwagType(iValue)
    return c, swagType, iValue
# take in user input to choice the CR of the hoard
# 0 : 0-4
# 1 : 5-10
# 2 : 11-16
# 3 : 17+
# default is whatever my players are at currents but we'll take sys argv
choice = 2
playerCount = 5
if len(sys.argv) == 3:
    choice = int(sys.argv[1])
    playerCount = int(sys.argv[2])
elif len(sys.argv) != 1 and len(sys.argv) != 3:
    print("Invalid input! Either use no arguments or 2 arguments (choice followed by playerCount)")
    exit()

# actually rolling the money and gems
copperSum = 0
swagCount = 0
swagType = ''
swagValue = 0

# Treasure Hoards 0-4
if choice == 0:
    # rolling basic coin amounts
    copper = diceroller('6d6') * 100
    silver = diceroller('3d6') * 100
    gold = diceroller('2d6') * 10

    # converting them all to copper
    copperSum += copper
    copperSum += convertToCopper('s', silver)
    copperSum += convertToCopper('g', gold)

    swagCount, swagType, swagValue = swag0()
    # swag value is in gold pieces, convert it to copper
    copperSum += convertToCopper('g', swagCount * swagValue)
# Treasure Hoards 5-10
elif choice == 1:
    copper = diceroller('2d6') * 100
    silver = diceroller('2d6') * 1000
    gold = diceroller('6d6') * 100
    platinum = diceroller('3d6') * 10

    copperSum += copper
    copperSum += convertToCopper('s', silver)
    copperSum += convertToCopper('g', gold)
    copperSum += convertToCopper('p', platinum)

    swagCount, swagType, swagValue = swag1()
    # swag value is in gold pieces, convert it to copper
    copperSum += convertToCopper('g', swagCount * swagValue)
elif choice == 2:
    gold = diceroller('4d6') * 1000
    platinum = diceroller('5d6') * 100

    copperSum += convertToCopper('g', gold)
    copperSum += convertToCopper('p', platinum)

    swagCount, swagType, swagValue = swag2()
    # swag value is in gold pieces, convert it to copper
    copperSum += convertToCopper('g', swagCount * swagValue)

print('Grand Total of: ' + str(copperSum) + 'cp including ' + str(swagCount) + ' (' + str(swagValue) + 'gp) ' + str(swagType))
print('Split evenly between ' + str(playerCount) + ' players:')

# splitting the copper evenly between players
copperPerPlayer = int(copperSum / playerCount)

# converting the copper into an appropriately formatted amount of gold
simpleCoins = simplifyCurrency(copperPerPlayer)
print(simpleCoins)
