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
    # should return (s) (totalValue) (gem|art) (gemType|artType) (individualValue)
    if s <= 6:
        return
    elif s <= 16:
        # should return 2d6 10gp gems
        return


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

