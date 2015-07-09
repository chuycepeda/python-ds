# 1 - Make a minesweeper of size LxW with M amount of mines distributed randomly
# 2 - Where no mine is found give away the sum of mines around the cell.



import random

def try_ex(x,y,grid):
	try:
		if grid[x][y] == -1 and x>=0 and y>=0:
			return 1
		else:
			return 0
	except:
		return 0


def mines(L,W,M):
	zero_grid = [ [0] * W for j in range(L) ]
	while M>0:
		random_row = random.randint(0,W-1)
		random_col = random.randint(0,L-1)
		if zero_grid[random_row][random_col] == 0:
			zero_grid[random_row][random_col] = -1
			M-=1
	grid = zero_grid
	for x in range(0,W):
		for y in range(0,L):
			if grid[x][y] == 0:
				_sum = 0
				_sum += try_ex(x,y-1,grid)
				_sum += try_ex(x,y+1,grid)
				_sum += try_ex(x-1,y,grid)
				_sum += try_ex(x+1,y,grid)
				_sum += try_ex(x-1,y-1,grid)
				_sum += try_ex(x+1,y+1,grid)
				_sum += try_ex(x+1,y-1,grid)
				_sum += try_ex(x-1,y+1,grid)
				grid[x][y] = _sum

	return grid


if __name__ == '__main__':
	print mines(4,4,9)