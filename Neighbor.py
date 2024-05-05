import numpy as np
import random
import math
from utils import genNeighbors, printLevels

"""
Procedural Generation for 2D dungeon in the style of "The Binding of Isaac".

Adapted from: "https://www.boristhebrave.com/2020/09/12/dungeon-generation-in-binding-of-isaac/"

"""

# Generate rooms based on rules
def getNewRooms(dungeon, room, currRooms, maxRooms, roomQ):
    neighbors = genNeighbors(dungeon, room, None)
    
    newRooms = []
    for n in neighbors:
        roomValid = True
        # Room limit has been reached
        if currRooms + len(newRooms) > maxRooms:
            roomValid = False
        # Current cell already has a room
        if dungeon[n] == 1:
            roomValid = False
        
        # Check if neighbors of current cell have rooms
        cellNeighbors = genNeighbors(dungeon, n, room)
        cN = 0
        for c in cellNeighbors:
            if dungeon[c] == 1:
                cN += 1
        # Random chance to give up based on number of neighbors
        if cN != 0 and random.randint(0, 3 - cN) == 0:
            roomValid = False
        # Random 40% chance to give up creating room
        if random.randint(0, 5) < 2:
            roomValid = False
        if roomValid:
            newRooms.append(n)
    return newRooms
        
# Generate single dungeon
def genDungeon(level):
    dungeon = np.zeros((8, 8))
    maxRooms = int(random.randint(0, 3) + 7 + level * 3)
    roomQ = [(3, 3)]

    roomsLeft = maxRooms - len(roomQ)

    while roomsLeft > 0:
        newRooms = []
        for room in roomQ:
            newRooms += getNewRooms(dungeon, room, len(roomQ), maxRooms, roomQ)
        toAdd = min(roomsLeft, len(newRooms))
        roomQ += newRooms[:toAdd]
        roomsLeft = maxRooms - len(roomQ)
        for room in roomQ:
            dungeon[room] = 1

    return dungeon, roomQ

print("Dungeon Algorithm: Neighbor")
printLevels(genDungeon)

    
    
    
