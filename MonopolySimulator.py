import random

def game():
    location = 0
    shuffledCommunityChestCards = shuffle(1)
    shuffledChanceCards = shuffle(0)

    for i in range(100):
        location = turn(location, shuffledCommunityChestCards, shuffledChanceCards)
        squares[location] += 1

def diceRoll():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    total = dice1 + dice2
    if dice1 == dice2:
        return total, 1
    else:
        return total, 0
    
def turn(location, communityChestCards, chanceCards):
    roll, doubles = diceRoll()
    location += roll
    location = locationCheck(location, communityChestCards, chanceCards)
    if doubles == 1:
        roll, doubles = diceRoll()
        location += roll
        location = locationCheck(location, communityChestCards, chanceCards)
        if doubles == 1:
            roll, doubles = diceRoll()
            location += roll
            location = locationCheck(location, communityChestCards, chanceCards)
            if doubles == 1:
                location = 10
                return location
            else:
                location += roll
                location = locationCheck(location, communityChestCards, chanceCards)
                return location
        else:
            return location
    else:
        return location

def locationCheck(location, communityChestCards, chanceCards):
    if location > 79:
        location -= 80
    elif location > 39:
        location -= 40

    if location == 2 or location == 17 or location == 33:
        communityChest(location, communityChestCards)
    if location == 7 or location == 22 or location == 36:
        chance(location, chanceCards)
    return location

def shuffle(type):
    if type == 1:
        newDeck = [x for x in communityChestCards]
        random.shuffle(newDeck)
        return newDeck
    elif type == 0:
        newDeck = [x for x in chanceCards]
        random.shuffle(newDeck)
        return newDeck

def communityChest(location, cards):
    initialLocation = location
    if len(cards) == 0:
        cards = shuffle(1)
    if type(cards[0]) == int:
        location = cards[0]
    cards.pop(0)
    #print(f"Community Chest card picked, initial location: {initialLocation}, final location: {location}")
    return location, cards

def chance(location, cards):
    initialLocation = location
    if len(cards) == 0:
        cards = shuffle(0)
    if type(cards[0]) == int:
        location = cards[0]
    elif cards[0] == "Go back three spaces":
        location -= 3
    elif cards[0] == "Nearest Utility":
        if location > 12 and location < 28:
            location = 12
        else:
            location = 28
    elif cards[0] == "Nearest railroad":
        if location < 5 or location > 35:
            location = 5
        elif location < 15:
            location = 15
        elif location < 25:
            location = 25
        else:
            location = 35
    cards.pop(0)
    #print(f"Chance card picked, initial location: {initialLocation}, final location: {location}")
    return location, cards
    
communityChestCards = [0, 10, "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-", "-"]
chanceCards = [0,24,11,"Nearest Utility", "Nearest Railroad", "-", "-", "Go back three spaces", 10, "-", "-", 5, 39, "-", "-"]

squares = []
for i in range(40):
    squares.append(0.0)

for i in range(100000):
    game()

percentages = []
for i in squares:
    percentages.append(i/40000)
print(percentages)
percentages.sort()
print(percentages)