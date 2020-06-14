import random
import numpy as np
def gen(m, n, start):
	maze = [['#'] * n for _ in range(m)]
	maze[start[0]][start[1]] = ' '
	deltas = [(0,1), (0,-1), (1,0), (-1,0)]

	def is_valid(i, j):
		return 0 <= i < m and 0 <= j < n and maze[i][j] == '#'

	def find_next(i, j):
		random.shuffle(deltas)
		for di, dj in deltas:
			ni, nj = i + 2 * di, j + 2 * dj
			if is_valid(ni, nj):
				maze[i + di][j + dj] = ' '
				maze[ni][nj] = ' '
				find_next(ni, nj)
	find_next(*start)
	return maze

def print_maze(maze):
	for line in maze:
		print(line)
	# print('\n'.join([''.join(line) for line in maze]))

# print_maze()
# print(np.array(gen(39, 15, (0,0))))
maze = gen(41, 31, (0,0))
file = open('/Users/YifeiTang/Desktop/maze.txt', 'w')
file.write('\n'.join([''.join(line) for line in maze]))
file.close()



