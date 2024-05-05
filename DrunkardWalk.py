import numpy as np
import random
import math
from utils import printLevels

def genDungeon(level):
  maxRooms = int(random.randint(0, 3) + 7 + level * 3)
  dungeon = np.zeros((8, 8))
  dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  roomQ = [(random.randint(0, 7), random.randint(0, 7))]

  roomsLeft = maxRooms
  current = roomQ[0]
  while roomsLeft > 0:
    dx, dy = random.choice(dirs)
    x, y = current
    current = (x + dx, y + dy)

    if current[0] < 0 or current[0] >= len(dungeon) or current[1] < 0 or current[1] >= len(dungeon):
      current = roomQ[0]
      continue

    if current not in roomQ:
      roomQ.append((current))
      roomsLeft -= 1

  for room in roomQ:
    dungeon[room] = 1

  return dungeon, roomQ

print("Dungeon Algorithm: Drunkard Walk")
printLevels(genDungeon)





