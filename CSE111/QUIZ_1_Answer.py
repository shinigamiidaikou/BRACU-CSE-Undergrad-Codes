start_num = int(input())
lock_grid = [[1,2,3],[4,5,6],[7,8,9]]
r=c=0
num_found = False
for i in range(3):
	for j in range(3):
		if start_num == lock_grid[i][j]:
			r = i
			c = j
			num_found = True
			break
	if num_found is True:
		break


def changeDirection(direction):
	global r, c
	if direction == 'U':
		r -= 1
	elif direction == 'D':
		r += 1
	elif direction == 'L':
		c -= 1
	elif direction == 'R':
		c += 1
	elif direction == 'DDL':
		r += 1
		c -= 1
	elif direction == 'DDR':
		r += 1
		c += 1
	elif direction == 'UDL':
		r -= 1
		c -= 1
	elif direction == 'UDR':
		r -= 1
		c += 1


direction_list = list(input().split())
print(start_num, end=' ')
for direction in direction_list:
	changeDirection(direction)
	print(lock_grid[r][c], end=' ')
