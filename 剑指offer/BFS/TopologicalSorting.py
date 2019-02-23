"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from queue import Queue

class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # 获取每个点的入度
        indegrees = self.countIndgree(graph)
        
        # 将入度为0的节点添加到result
        order = []
        q = Queue()
        
        for node in graph:
            if indegrees[node] == 0:
                q.put(node)
                order.append(node)
        
        # 将入度为0的点添加到result后，所有由此节点出发到达的点的入度减一
        while not q.empty():
            node_iter = q.get()
            for neighbor in node_iter.neighbors:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    order.append(neighbor)
                    q.put(neighbor)
        
        return order
    
    def countIndgree(self, graph):
        # bfs
        indegrees = {}
        
        for node in graph:
            indegrees[node] = 0
    
        for node in graph:
            for neighbor in node.neighbors:
                indegrees[neighbor] += 1
                
        return indegrees
                
                    