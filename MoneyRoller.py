# Program by Jonathan Kleehammer 9-10-19
# Program is designed to simulate DnD 5e treasure hoards from pages 137-138 of the DMG
# Only simulates the gold because the other values are generated/picked elsewhere
# also takes in a number of players so that the money is evenly divisible

import random

# global variables of all the gems by value
gem10 = {'Azurite (opaque mottled deep blue)',
         'Banded agate (translucent striped brown, blue, white, or red)',
         'Blue quartz (transparent pale blue)',
         'Eye agate (translucent circles of gray, white, brown, blue, or green)',
         'Hematite (opaque gray-black)',
         'Lapis lazuli (opaque light and dark blue with yellow flecks)',
         'Malachite (opaque striated light and dark green)',
         'Moss agate (translucent pink or yellow-white with mossy gray or green markings)',
         'Obsidian (opaque black)', 'Rhodochrosite (opaque light pink)',
         'Tiger eye (translucent brown with golden center)',
         'Turquoise (opaque light blue-green)'}

gem50 = {'Bloodstone (opaque dark gray with red flecks)',
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
         'Zircon (transparent pale blue-green)'}

gem100 = {'Amber (transparent watery gold to rich gold)',
          'Amethyst (transparent deep purple)',
          'Chrysoberyl (transparent yellow-green to pale green)',
          'Coral (opaque crimson)',
          'Garnet (transparent red, brown-green, or violet)',
          'jade (translucent light green, deep green, or white)',
          'jet (opaque deep black)',
          'Pearl (opaque lustrous white, yellow, or pink)',
          'Spinel (transparent red, red-brown, or deep green)',
          'Tourmaline (transparent pale green, blue, brown, or red)'}

gem500 = {'Alexandrite (transparent dark green)',
          'Aquamarine (transparent pale blue-green)',
          'Black pearl (opaque pure black)',
          'Blue spinel (transparent deep blue)',
          'Peridot (transparent rich olive green)',
          'Topaz (transparent golden yellow)'}

# takes in a dice string (3d6, 4d8, 2d4, etc) and returns an integer for what was rolled
def diceroller(diceString):
    diceCount, diceType = diceString.split('d')

    diceCount = int(diceCount)
    diceType = int(diceType)

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

# returns a random gem with specified gp value
def getGemName(value):
    pass

# art or gems for treasure hoard 0 (CR 0-4)
def swag0():
    # s is our swag level, from 1-100
    s = diceroller('1d100')
    # should return (totalValue) (count) (type) (individualValue)
    if s <= 6:
        return 0, 0, 'nothing', 0
    elif s <= 16:
        # should return 2d6 10gp gems
        c = diceroller('2d6')
        iValue = convertToCopper('g', 10)
        tValue = c * iValue

        return tValue, c, '10gpGem', iValue


# take in user input to choice the CR of the hoard
# 0 : 0-4
# 1 : 5-10
# 2 : 11-16
# 3 : 17+
choice = 0

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

