class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: the course order
    """
    def findOrder(self, numCourses, prerequisites):
        # 定义图
        graph = [[] for i in range(numCourses)]
        # 定义入度
        indegrees = [0 for i in range(numCourses)]
        
        # 填充
        for i, j in prerequisites:
            graph[j].append(i) # 由j指向i
            indegrees[i] += 1 
            
        q = collections.deque([i for i in range(numCourses) if indegrees[i] == 0])
        
        result = []
        # bfs
        while q:
            node = q.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1 
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        return result if len(result) == numCourses else []