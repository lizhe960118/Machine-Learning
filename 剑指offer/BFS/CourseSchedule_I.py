from queue import Queue
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # 将所有的节点的入度算一下
        dict_indgree = {}
        
        for i in range(numCourses):
            dict_indgree[i] = 0
            
        for item in prerequisites:
            course = item[0]
            need_course = item[1]
            dict_indgree[course] += 1
            
        # 依次移除入度为零的节点
        q = Queue()
        
        for i in range(numCourses):
            if dict_indgree[i] == 0:
                q.put(i)
        
        while not q.empty():
            need_course = q.get()
            for item in prerequisites:
                if item[1] == need_course:
                    dict_indgree[item[0]] -= 1
                    if dict_indgree[item[0]] == 0:
                        q.put(item[0])
                    
        # 判别所有节点的入度，如果为零则可以
        for i in range(numCourses):
            if dict_indgree[i] != 0:
                return False
                
        return True

from queue import Queue
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # 将所有的节点的入度算一下
        # dict_indgree = [0 for course in range(numCourses)]
        
        # 用字典保存所有节点的对于关系
        dict_node = {}
        
        for course in range(numCourses):
            dict_node[course] = set()
            
        for item in prerequisites:
            course = item[0]
            need_course = item[1]
            dict_node[course].add(need_course)
            
        # 依次移除入度为零的节点
        q = Queue()
        
        for course in range(numCourses):
            if len(dict_node[course]) == 0:
                q.put(course)
        
        while not q.empty():
            need_course = q.get()
            for course, need_courses in dict_node.items():
                if need_course in need_courses:
                    dict_node[course].remove(need_course)
                    if len(dict_node[course]) == 0:
                        q.put(course)
                    
        # 判别所有节点的入度，如果为零则可以
        for course in range(numCourses):
            if len(dict_node[course]) != 0:
                return False
                
        return True

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # 用字典保存所有节点的对应关系
        dict_node = {}
        
        for course in range(numCourses):
            dict_node[course] = set()
            
        for item in prerequisites:
            course = item[0]
            need_course = item[1]
            # 先修1，再修0，图中是1指向0
            dict_node[need_course].add(course) # 相当于指向出的方向
        
        # 计算每个节点的入度
        indegrees = [0 for course in range(numCourses)]
        
        for need_course, courses in dict_node.items():
            for course in courses:
                indegrees[course] += 1

        # 找到入度为0的节点，并移除它关联的节点
        # 假设每次移除一个节点，循环numCourses次
        for iter_num in range(numCourses):
            
            # 查找
            course = 0
            while course < numCourses:
                if indegrees[course] == 0:
                    break
                course += 1
            
            if course == numCourses:
                return False
            
            # 查找过，下次不再查找
            indegrees[course] = -1
            # 在图中，将所有相关点的入度减一
            for neighbor in dict_node[course]:
                indegrees[neighbor] -= 1
            
        return True

class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def __init__(self):
        self.visit = []

    def canFinish(self, numCourses, prerequisites):
        # 相当于查找是否有环，dfs
        # 建立图
        graph = [set() for course in range(numCourses)]
        
        for item in prerequisites:
            course = item[0]
            need_course = item[1]
            graph[need_course].add(course)
            
        # 建立visit表,说明是否访问过
        self.visit = [0 for course in range(numCourses)]
        
        # dfs 搜索是否有环，有环则返回False
        for course in range(numCourses):
            if not self.dfs(graph, course):
                return False
        
        return True
        
    def dfs(self, graph, course):
        # 单次访问之时标记为-1
        self.visit[course] = -1
        
        # 访问course的邻近节点
        for neighbor in graph[course]:
            # 如果在单次遍历已经访问过，说明有环，返回false
            if self.visit[neighbor] == -1:
                return False
            
            # 如果之前访问过，并且此neighbor不构成环，不必继续
            if self.visit[neighbor] == 1:
                continue
            
            # 没有访问则继续dfs相邻节点
            if not self.dfs(graph, neighbor):
                return False
        
        # 如果单次遍历没有问题，将course标记为1
        self.visit[course] = 1
        
        return True

import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        
        graph = {i:[] for i in range(numCourses)}
        in_degree = [0 for i in range(numCourses)]
        
        for i,j in prerequisites:
            graph[j].append(i)
            in_degree[i] += 1

        # 找到入度为0的节点
        queue = collections.deque([i for i in range(numCourses) if in_degree[i] == 0])
        count = 0 
        
        # bfs
        while queue:
            node = queue.popleft()
            count += 1 
            for neighbor in graph[node]:
                in_degree[neighbor] -= 1 
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
                    
        return count == numCourses

if __name__ == '__main__':
    print(Solution().canFinish(2, [[1, 0]]))

from queue import Queue 
class Solution:
    """
    @param: numCourses: a total of n courses
    @param: prerequisites: a list of prerequisite pairs
    @return: true if can finish all courses or false
    """
    def canFinish(self, numCourses, prerequisites):
        # 将所有的节点的入度算一下
        indgrees = [0 for course in range(numCourses)]
        
        # 用字典保存所有节点的对于关系
        dict_node = {}
        
        for course in range(numCourses):
            dict_node[course] = []
            
        for item in prerequisites:
            course = item[0]
            need_course = item[1]
            dict_node[need_course].append(course)
            indgrees[course] += 1
            
        # 依次移除入度为零的节点
        q = Queue()
        
        for course in range(numCourses):
            if indgrees[course] == 0:
                q.put(course)
        
        count = 0
        while not q.empty():
            need_course = q.get()
            count += 1
            
            for course in dict_node[need_course]:
                indgrees[course] -= 1 
                if indgrees[course] == 0:
                    q.put(course)
                
        return count == numCourses