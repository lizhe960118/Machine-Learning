class Solution:
    """
    @param grid: a boolean 2D matrix
    @return: an integer
    """
    def numIslands(self, grid):
        count = 0
        n = len(grid)
        if n == 0:
            return count
            
        m = len(grid[0])
        if m == 0:
            return count
            
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    self.bfs(grid,i,j)
                    count += 1 
        return count
        
    def bfs(self, grid, x, y):

        deltaX = [1, 0, -1, 0]
        deltaY = [0, 1, 0, -1]
        
        q = collections.deque()
        q.append((x, y))
        
        grid[x][y] = 0
        
        while q:
            x, y = q.popleft()
            
            for i in range(4):
                newX = x + deltaX[i]
                newY = y + deltaY[i]
                if not self.isValid(grid, newX, newY):
                    continue
                q.append((newX, newY))
                # 此时将newX, newY位置置为0
                grid[newX][newY] = 0
        return
    
    def isValid(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        if (x < n) and (x >= 0) and (y < m) and (y >= 0) and grid[x][y] == 1:
            return True
        else:
            return False
        