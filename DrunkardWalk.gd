extends Node

#from utils import printLevels

"""
Procedural Generation for 2D dungeon with Drunkard Walk algorithm.
By Collin Jung, CS 247G Spring 2024

Adapted from: "http://pcg.wikidot.com/pcg-algorithm:drunkard-walk"
"""

func genDungeon(level):
  var maxRooms = rand_range(0, 3) + 7 + level * 3
  var dungeon = Array()
  for i in range(8):
    dungeon.append([0,0,0,0,0,0,0,0])
  var dirs = [Vector2(-1, 0), Vector2(1, 0), Vector2(0, -1), Vector2(0, 1)]

  var roomQ = [Vector2(rand_range(0, 7), rand_range(0, 7))]

  roomsLeft = int(maxRooms)
  current = roomQ[0]
  while roomsLeft > 0:
    # Pick a random cardinal direction
    var direction = dirs[randi() % dirs.size()]
	var newX = current.x + direction.x
	var newY = current.y + direction.y
		
	# New cell
	current = Vector2(newX, newY)

    # If cell is out of bounds, return to starting position
    if current.x < 0 or current.x >= len(dungeon) or current.y < 0 or current.y>= len(dungeon):
      current = roomQ[0]
      continue
      
    # If cell is not in list of rooms, add it and repeat
    if not roomQ.has(current):
      roomQ.append(current)
      roomsLeft -= 1

  # Update dungeon grid
  for room in roomQ:
    dungeon[int(room.x)][int(room.y)] = 1

  return dungeon, roomQ

func _ready():
    print("Dungeon Algorithm: Drunkard Walk")
    printLevels(genDungeon)





