# Given a 2D grid, each cell is either a wall 2, a zombie 1 or people 0 (the number zero, one, two).
# Zombies can turn the nearest people(up/down/left/right) into zombies every day, but can not through wall.
# How long will it take to turn all people into zombies? Return -1 if can not turn all people into zombies.
# Given a matrix:
"""
    0 1 2 0 0
    1 0 0 2 1
    0 1 0 0 0
    return 2
"""
import collections
class Solution:
    """
    @param grid: a 2D grid
    @return: integer, the days need to trun all people into zombies
    """
    def daysNeed(self, grid):
        n = len(grid)
        if n == 0:
            return 0
        m = len(grid[0])
        if m == 0:
            return 0

        q = collections.deque()

        people = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    q.append((i, j))
                if grid[i][j] == 0:
                    people += 1

        deltaX = [0, 1, 0, -1]
        deltaY = [1, 0, -1, 0]
        days = 0
        # bfs,但是之中还要层序遍历
        while q:
            level_size = len(q)

            for iter_num in range(level_size):
                x, y = q.popleft()

                for i in range(4):
                    new_x = x + deltaX[i]
                    new_y = y + deltaY[i]

                    if not self.canTurn(grid, new_x, new_y):
                        continue

                    q.append((new_x, new_y))
                    grid[new_x][new_y] = 1
                    people -= 1

            days += 1
            if people == 0:
                return days

        return -1
                    
    def canTurn(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        if (x < n) and (x >= 0) and (y < m) and (y >= 0) and grid[x][y] == 0:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().daysNeed([[0,1,2,0,0],[1,0,0,2,1],[0,1,0,0,0]]))


