extends Node

# Find "ends" in dungeon (Rooms with 3 empty neighbors)
func findEnds(dungeon):
    var dirs = [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
    var maxX = len(dungeon[0])
    var maxY = len(dungeon)
    endRooms = []
    for x in range(maxX):
        for y in range(maxY):
            if dungeon[x][y] == 1:
                var end = 0
                for dir in dirs:
                    var dx = dir.x + x
                    var dy = dir.y + y
                    if dx < 0 or dx >= maxX or dy < 0 or dy >= maxY:
                        continue
                    elif dungeon[dy][dx]:
                        end += 1
                if end >= 3:
                    endRooms.append[Vector2(x, y)]
    return endRooms

# Generate neighbor coordinates in 4 cardinal directions
func genNeighbors(dungeon, room, original):
    var dirs = [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]
    var maxX = len(dungeon[0])
    var maxY = len(dungeon)
    
    var neighbors = []
    var x = room.x
    var y = room.y

    for dir in dirs:
       var dx = dir.x + x
        var dy = dir.y + y
        if dx < 0 or dx >= maxX or dy < 0 or dy >= maxY:
            continue
        elif original != null and Vector2(dx, dy) == original:
            continue
        else:
            neighbors.append(Vector2(dx, dy))
            
    return neighbors

# Validate dungeon and find start/end cells. If not enough end cells or distance between start and end is too small, regenerate.
func genValidDungeon(level, genDungeon): 
  var dungeon, rooms = genDungeon(level)
  var foundEnds = false

  while true:
      while len(findEnds(dungeon)) < 2:
          dungeon, rooms = genDungeon(level)
      var mapEnd = findEnds(dungeon)[-1]

      var mapStart = rooms[randi() % len(rooms)]
      for i in range(3):
          if mapStart.distance_to(mapEnd) < 3 or mapStart.x == mapEnd.x or mapStart.y == mapEnd.y:
              mapStart = rooms[randi() % len(rooms)]
          else:
              foundEnds = true
              break
      if foundEnds:
          break

  dungeon[mapStart.y][mapStart.x] = 2
  dungeon[mapEnd.y][mapEnd.x] = 2
  return dungeon, mapStart, mapEnd

# Print dungeon
func printDungeon(dungeon, mapStart, mapEnd):
    print("| Start box 🟨: {}        |".format(mapStart))
    print("| End box 🟩: {}          |".format(mapEnd))

    var maxY = len(dungeon)
    var maxX = len(dungeon[0])

    for y in range(maxY):
        var toPrint = "|      "
        for x in range(maxX):
            match dungeon[y][x]:
                0:
                    to_print += "🟫"
                1:
                    to_print += "🟪"
                2:
                    to_print += "🟨"
                3:
                    to_print += "🟩"
        print(to_print + "       |")

# Generate dungeons level 1 to 3
func printLevels(genDungeon):
  for i in range(1, 4):
    print("===============================")
    print("| Generating dungeon level {}  |".format(i))
    var dungeon, s, e = genValidDungeon(i, genDungeon)
    printDungeon(dungeon, s, e)
    print("===============================")
    print()