# Dungeon Procedural Generation

# TODO

(1) Convert these files to GDScript  
(2) Figure out how to view the room generations in Godot  
(3) Pick room dimensions. All of our rooms will be the same size, which should make things easier. Since our algorithm returns coordinates in a grid, we could just multiply these coordinates by a set amount based on room size. For example, if our rooms are 100 pixels by 200 pixels and we have rooms at cell (0, 0), (1, 0), and (0, 1), we would convert our coordinates to be (x * 100, y * 200). In this case, (0, 0), (100, 0) and (0, 200) would be the top-left corner of our room components.  

Useful resources:
- https://www.youtube.com/watch?v=G2_SGhmdYFo Introduction into dungeon procgen in Godot. The algorithm/process they use is different but once our files are written in GDScript, it should be essentially the same
- https://www.youtube.com/watch?v=mwk_8Q-jz90 This is probably closer to what we are looking for, at least for visualizing our dungeon rooms before we actually draw them full size.



# Files

utils.py: This holds utility functions used in both algorithms. Mostly QOL functions like printing the dungeon generations in a pretty way and regenerating dungeons until a valid one comes up.
Neighbor.py: Dungeon generation file based on neighbor-based algorithm
DrunkardWalk.py: Dungeon generation file based on Drunkard Walk algorithm

# Terminology

Dungeon/Grid: The dungeons are currently represented by a 8 x 8 grid, where 0s represent empty cells and 1s represent rooms. I use 2 to denote the start room and 3 to denote the end room.

Cell: Term for each space in the grid (e.g. (0, 0) and (0, 8) would be top-left and top-right cells respectively)

Room: Term for an occupied cell that will hold a room.

Level: Each dungeon generation function takes in an integer level parameter. This is because of the following line in the functions -> random.randint(0, 3) + 7 + level \* 3, which is used to generate the number of max rooms per level. Essentially, at level 1, you start off with around 10-13 rooms. Then, there should be around 3 additional rooms per level. The random integer is used for some variation (Which means some levels may have the same number of rooms). This function is adapted from the Binding of Isaac code which uses some different values.

# Toy example:

Dungeon grid:  
[[0, 2, 0],  
 [1, 1, 1],  
 [0, 3, 0]]

In this dungeon, the start room would be at cell (0, 1) and the end room would be at cell (2, 1). The shape of the dungeon is a plus (+) shape. The middle cell (1, 1) has doors on all cardinal directions while the start room and end room each have only 1 door.

# Algorithm 1:

Neighbor-based generation. Based on "The Binding of Isaac". Link to algorithm: "https://www.boristhebrave.com/2020/09/12/dungeon-generation-in-binding-of-isaac/"

In this algorithm, you set a point in the center of the grid, then randomly generate in each cardinal direction based on how many neighbors each cell has. Repeat until you reach the number of rooms needed.

Notes:

- From what I've noticed, this algorithm results in more compact dungeons centered around the middle of the grid. This is probably due to the recursive BFS-style stepping.
- Due to the more uniform, pattern-like results, this algorithm would probably be good for the first world/stage in the cave.

# Algorithm 2:

Drunkard Walk generation. Link to algorithm: "http://pcg.wikidot.com/pcg-algorithm:drunkard-walk"

In this algorithm, you pick a random point on the grid. Then, for each step, you pick a random cardinal direction and "walk" to that cell. If the cell is empty, add it to the list of rooms. If not, do nothing. Repeat until you reach the number of rooms needed.

Notes:

- This algorithm tends to give generations that are more "stretched out". This is probably because the algorithm relies on more of a DFS-style stepping process (Pick one direction, then keep going instead of checking all other neighbors).
- Based on the theme of our game, this might be nice to use for second world/stage in the forest.
