# Program by Jonathan Kleehammer 9-10-19
# Program is designed to simulate DnD 5e treasure hoards from pages 137-138 of the DMG
# Only simulates the gold because the other values are generated/picked elsewhere
# also takes in a number of players so that the money is evenly divisible

import random

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
def simplifyCurrency(copper):
    if copper > 100:
        return copper/100
    pass
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
        return random.choice()
    elif value == 1000:
        return random.choice(gem100)
    elif value == 2500:
        return random.choice()
    elif value == 5000:
        return random.choice(gem100)
    elif value == 7500:
        return random.choice(gem100)


# art or gems for treasure hoard 0 (CR 0-4)
# return (count) (type) (individualValue)
def swag0():
    # s is our swag level, from 1-100
    s = diceroller('1d100')
    c = 0
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

# take in user input to choice the CR of the hoard
# 0 : 0-4
# 1 : 5-10
# 2 : 11-16
# 3 : 17+
choice = 0

playerCount = 5

# actually rolling the money and gems
copperSum = 0
gemType = ''
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

    print (str(copperSum) + ' including ' + str(swagCount) + ' (' + str(swagValue) + 'gp) ' + str(swagType))
    print('Split evenly between ' + str(playerCount) + ' players:')

    # splitting the copper evenly between players
    copperSum /= playerCount

    # converting the copper into an appropriately formatted amount of gold
    print(copperSum)