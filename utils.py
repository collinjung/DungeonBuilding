import random
import math

# Find "ends" in dungeon (Rooms with 3 empty neighbors)
def findEnds(dungeon):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maxX = len(dungeon[0])
    maxY = len(dungeon)
    endRooms = []
    for x in range(len(dungeon[0])):
        for y in range(len(dungeon)):
            if dungeon[x, y] == 1:
                end = 0
                for i, j in dirs:
                    if x + i < 0 or x + i >= maxX:
                        continue
                    elif y + j < 0 or y + j >= maxY:
                        continue
                    elif dungeon[x + i, y + j] == 0:
                        end += 1
                if end >= 3:
                    endRooms += [(x, y)]
    return endRooms

# Generate neighbor coordinates in 4 cardinal directions
def genNeighbors(dungeon, room, original):
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    maxX = len(dungeon[0])
    maxY = len(dungeon)
    
    neighbors = []
    (x, y) = room

    for i, j in dirs:
        if x + i < 0 or x + i >= maxX:
            continue
        elif y + j < 0 or y + j >= maxY:
            continue
        elif original != None and (x + i, y + j) == original:
            continue
        else:
            neighbors.append((x + i, y + j))
            
    return neighbors

# Validate dungeon and find start/end cells. If not enough end cells or distance between start and end is too small, regenerate.
def genValidDungeon(level, genDungeon): 
  dungeon, rooms = genDungeon(level)
  foundEnds = False
  while True:
      while len(findEnds(dungeon)) < 2:
          dungeon, rooms = genDungeon(level)
      mapEnd = findEnds(dungeon)[-1]

      mapStart = random.choice(rooms)
      for _ in range(3):
          if math.dist(mapStart, mapEnd) < 3 or mapStart[0] == mapEnd[0] or mapStart[1] == mapEnd[1]:
              mapStart = random.choice(rooms)
          else:
              foundEnds = True
              break
      if foundEnds:
          break

  dungeon[mapStart] = 2
  dungeon[mapEnd] = 3
  return dungeon, mapStart, mapEnd

# Print dungeon
def printDungeon(dungeon, mapStart, mapEnd):
    print("| Start box 🟨: {}        |".format(mapStart))
    print("| End box 🟩: {}          |".format(mapEnd))
    for y in range(len(dungeon)):
        toPrint = "|      "
        for x in range(len(dungeon[0])):
            if dungeon[x, y] == 0:
                toPrint += "🟫"
            elif dungeon[x, y] == 1:
                toPrint += "🟪"
            elif dungeon[x, y] == 2:
                toPrint += "🟨"
            else:
                toPrint += "🟩"
        print(toPrint + "       |")

# Generate dungeons level 1 to 3
def printLevels(genDungeon):
  for i in range(1, 4):
    print("===============================")
    print("| Generating dungeon level {}  |".format(i))
    dungeon, s, e = genValidDungeon(i, genDungeon)
    printDungeon(dungeon, s, e)
    print("===============================")
    print()