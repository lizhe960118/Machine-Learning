class Solution:
    """
    @param grid: a 2D grid
    @return: An integer
    """
    def shortestDistance(self, grid):
        # 将所有房子作为起始点，对所有空地进行搜索，记录下他们到空地的距离，并相加，返回距离最短的点
        shortest_path = -1
        # 判断边界
        if grid is None:
            return shortest_path
        n = len(grid)
        if n == 0:
            return shortest_path
        m = len(grid[0]) 
        if m == 0:
            return shortest_path
            
        houses = [] 
        empty_area = {}        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    houses.append((i,j))
                if grid[i][j] == 0:
                    empty_area[(i,j)] = 0
        num_houses = len(houses)
        
        deltaX = [1,0,-1,0]
        deltaY = [0,1,0,-1]
        
        count_visit = [[0 for j in range(m)] for i in range(n)]
        for house in houses:
            q = collections.deque()
            q.append(house)
            
            # 标记是否访问过
            visited = [[False for j in range(m)] for i in range(n)]
            step = 0
            
            while q:
                level_size = len(q)
                step += 1
                for iter_num in range(level_size):
                    house = q.popleft()
                    x, y = house
                    
                    for i in range(4):
                        new_x = x + deltaX[i]
                        new_y = y + deltaY[i]
                        
                        if self.isEmptyArea(grid, new_x, new_y) and not visited[new_x][new_y]:
                            count_visit[new_x][new_y] += 1
                            empty_area[(new_x, new_y)] += step
                            q.append((new_x, new_y))
                            visited[new_x][new_y] = True
                        
        postOffice = None
        shortest_path = float("inf")
        for key, value in empty_area.items():
            x, y = key
            if count_visit[x][y] == num_houses:
                if value < shortest_path:
                    shortest_path = value
                    postOffice = (x, y)

        return shortest_path if shortest_path != float("inf") else -1
        
        
    def isEmptyArea(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])
        if (x >= 0) and (x < n) and (y >= 0) and (y < m) and grid[x][y] == 0:
            return True
        else:
            return False