import numpy as np
import random
import math
from utils import printLevels

"""
Procedural Generation for 2D dungeon with Drunkard Walk algorithm.
By Collin Jung, CS 247G Spring 2024

Adapted from: "http://pcg.wikidot.com/pcg-algorithm:drunkard-walk"
"""

def genDungeon(level):
  maxRooms = int(random.randint(0, 3) + 7 + level * 3)
  dungeon = np.zeros((8, 8))
  dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

  roomQ = [(random.randint(0, 7), random.randint(0, 7))]

  roomsLeft = maxRooms
  current = roomQ[0]
  while roomsLeft > 0:
    # Pick a random cardinal direction
    dx, dy = random.choice(dirs)
    x, y = current

    # New cell
    current = (x + dx, y + dy)

    # If cell is out of bounds, return to starting position
    if current[0] < 0 or current[0] >= len(dungeon) or current[1] < 0 or current[1] >= len(dungeon):
      current = roomQ[0]
      continue
      
    # If cell is not in list of rooms, add it and repeat
    if current not in roomQ:
      roomQ.append((current))
      roomsLeft -= 1

  # Update dungeon grid
  for room in roomQ:
    dungeon[room] = 1

  return dungeon, roomQ

print("Dungeon Algorithm: Drunkard Walk")
printLevels(genDungeon)





