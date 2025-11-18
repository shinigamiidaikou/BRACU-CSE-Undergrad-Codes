def stateInitialize(grid):
    for r in grid:
        for h in r:
            h[1] = 0


def collectionDFS(grid, r, h):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    if r < 0 or r >= len(grid) or h < 0 or h >= len(grid[0]):
        return 0
    if grid[r][h][0] == '#' or grid[r][h][1] == 1:
        return 0
    grid[r][h][1] = 1
    diamond = 0
    if grid[r][h][0] == 'D':
        diamond = 1
    for move in directions:
        diamond += collectionDFS(grid, r+move[0], h+move[1])
    return diamond


def maxDiamonds(grid):
    R = len(grid)
    H = len(grid[0])
    stateInitialize(grid)
    highestCount = 0
    for r in range(R):
        for h in range(H):
            stateInitialize(grid)
            if grid[r][h][0] == '.':
                current = collectionDFS(grid, r, h)
                if current > highestCount:
                    highestCount = current
    return highestCount


in_file = open("input6_3.txt")
r, h= [int(num) for num in in_file.readline().split()]
grid = []

for line in in_file:
    grid.append([[cell,0] for cell in line.strip()])
in_file.close()

out_file = open("output6_3.txt", "w")
output = maxDiamonds(grid)
out_file.write(str(output))
out_file.close()
