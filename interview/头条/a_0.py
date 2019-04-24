# n = int(input())

# grid = [n][m]

# for i in range()

import collections

grid = []
while True:
    try:
        i = input()
    except EOFError:
        break
    tmp = [int(a) for a in i.split()]
    grid.append(tmp)

def step_need(grid):
    n = len(grid)
    if n == 0:
        return 0
    m = len(grid[0])
    if m == 0:
        return 0

    # print(m, n)
    q = collections.deque()

    chan_pin = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 2: # 程序员
                q.append((i, j))
            if grid[i][j] == 1: # 产品
                chan_pin += 1

    deltaX = [0, 1, 0, -1]
    deltaY = [1, 0, -1, 0]
    steps = 0
    # bfs,但是之中还要层序遍历
    while q:
        level_size = len(q)
        for iter_num in range(level_size):
            x, y = q.popleft()
            for i in range(4):
                new_x = x + deltaX[i]
                new_y = y + deltaY[i]
                if not canTurn(grid, new_x, new_y):
                    continue
                q.append((new_x, new_y))
                grid[new_x][new_y] = 2 # 为了把产品变成程序员
                chan_pin -= 1
        steps += 1
        if chan_pin == 0:
            return steps
    return -1
                    
def canTurn(grid, x, y):
    n = len(grid)
    m = len(grid[0])
    if (x < n) and (x >= 0) and (y < m) and (y >= 0) and grid[x][y] == 1:
        return True
    else:
        return False

print(step_need(grid))