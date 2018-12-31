class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 深度优先遍历，访问过之后将此节点标为0
        n = len(grid)
        m = len(grid[0])
        ans = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] == 1:
                    ans = max(self.dfs(grid,x,y), ans)
        return ans
    
    def dfs(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        count = 1
        grid[x][y] = 0
        g_next = [[0, 1],[0, -1], [1, 0],[-1, 0]]
        for i in range(4):
            x_n = x + g_next[i][0]
            y_n = y + g_next[i][1]
            if (x_n > -1 and x_n < n and y_n > -1 and y_n < m and grid[x_n][y_n] == 1):
                count += self.dfs(grid, x_n, y_n)
        return count