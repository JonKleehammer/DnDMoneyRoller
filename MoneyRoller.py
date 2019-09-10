# Program by Jonathan Kleehammer 9-10-19
# Program is designed to simulate DnD 5e treasure hoards from pages 137-138 of the DMG
# Only simulates the gold because the other values are generated/picked elsewhere
# also takes in a number of players so that the money is evenly divisible

import random

# takes in a dice string (3d6, 4d8, 2d4, etc) and returns an integer for what was rolled
def diceroller(diceString):
    diceCount, diceType = diceString.split('d')

    diceCount = int(diceCount)
    diceType = int(diceType)

    rollSum = 0
    for i in range(diceCount):
        rollSum += random.randrange(1, diceType)

    return rollSum


def convertToGold(coinType, amount):
    pass

# take in user input to choice the CR of the hoard
# 0 : 0-4
# 1 : 5-10
# 2 : 11-16
# 3 : 17+
choice = 0

# actually rolling the money and gems
goldSum = 0
gemType = ''
if choice == 0:
    copper = diceroller('6d6') * 100