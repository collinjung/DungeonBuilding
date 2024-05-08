extends Node
from utils import genNeighbors, printLevels

"""
Procedural Generation for 2D dungeon in the style of "The Binding of Isaac".
By Collin Jung, CS 247G Spring 2024

Adapted from: "https://www.boristhebrave.com/2020/09/12/dungeon-generation-in-binding-of-isaac/"
"""

# Generate rooms based on rules
func getNewRooms(dungeon, room, currRooms, maxRooms, roomQ):
    var neighbors = genNeighbors(dungeon, room, null)
    var newRooms = []

    for n in neighbors:
        var roomValid = true
        # Room limit has been reached
        if currRooms + len(newRooms) > maxRooms:
            roomValid = false
        # Current cell already has a room
        if dungeon[n.x][n.y] == 1:
            roomValid = false
        
        # Check if neighbors of current cell have rooms
        var cellNeighbors = genNeighbors(dungeon, n, room)
        var cN = 0
        for c in cellNeighbors:
            if dungeon[c.x][c.y] == 1:
                cN += 1
        # Random chance to give up based on number of neighbors
        if cN != 0 and randi() % (4 - c_n) == 0:
            roomValid = false
        # Random 40% chance to give up creating room
        if randi() % 6 < 2:
			roomValid = false
		if roomValid:
			newRooms.append(n)
    return newRooms
        
# Generate single dungeon
def genDungeon(level):
    var dungeon = []

    # Loop to create an 8x8 grid
    for i in range(8):
        dungeon.append([0] * 8)

    var maxRooms = rand_range(0, 4) + 7 + level * 3
    var roomQ = [Vector2(3, 3)]

    var roomsLeft = maxRooms - len(roomQ)

    while roomsLeft > 0:
        var newRooms = []
        for room in roomQ:
            newRooms += getNewRooms(dungeon, room, len(roomQ), maxRooms, roomQ)
        var toAdd = min(roomsLeft, len(newRooms))
        roomQ += new_rooms.slice(0, to_add)
        roomsLeft = maxRooms - len(roomQ)
        for room in roomQ:
            dungeon[int(room.x)][int(room.y)] = 1

    return dungeon, roomQ

func _ready():
    print("Dungeon Algorithm: Neighbor")
    printLevels(genDungeon)

    
    
    
