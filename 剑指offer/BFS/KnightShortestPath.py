# Given a knight in a chessboard (a binary matrix with 0 as empty and 1 as barrier) with a source position, 
# find the shortest path to a destination position, return the length of the route. 
# knight 走“日”字

import collections
"""
Definition for a point
"""
class Point:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

class Solution:
    """
    @param grid: a chessboard included 0 (false) and 1 (true)
    @param source, destination: a point
    @return the shortest path 
    """
    def shortestPath(self, grid, source, destination):
        shortest_path = -1
        # 判断边界
        if grid is None:
            return shortest_path
        n = len(grid)
        if n == 0:
            return shortest_path
        m = len(gird[0]) 
        if m == 0:
            return shortest_path

        # 将节点加入队列
        q = collections.deque()
        q.append(source)

        deltaX = [1,1,-1,-1,2,2,-2,-2]
        deltaY = [2,-2,2,-2,1,-1,1,-1]
        # 节点出队，每次出队搜索8个方向
        shortest_path = 0
        # 求最短路径长度，层次遍历
        while q:
            level_size = len(q)
            shortest_path += 1

            for iter_size in range(level_size):
                point = q.popleft()
            
                for i in range(8):
                    new_x = x + deltaX[i]
                    new_y = y + deltaY[i]

                    new_point = Point(new_x, new_y)
                    if notCrossBoundary(gird, new_x, new_y):
                        if new_point == destination:
                            return shortest_path
                        if grid[new_x][new_y] == 0:
                            q.append(new_point)
                            # 访问过标记为1
                            gird[new_x][new_y] = 1
        return -1

    # 写一个函数判断是否越界
    def notCrossBoundary(self, grid, x, y):
        n = len(grid)
        m = len(grid[0])

        if (x < n) and (x >= 0) and (y < m) and (y >= 0):
            return True
        else:
            return False