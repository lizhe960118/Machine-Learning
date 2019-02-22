"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from queue import Queue
class Solution:
    """
    @param: node: A undirected graph node
    @return: A undirected graph node
    """
    def cloneGraph(self, node):
        if node is None:
            return None
        
        # print(node.label)
        # for neighbor in node.neighbors:
        #     print(neighbor.label)
        # 使用bfs得到所有的节点
        nodes = self.getNodes(node)
        
        map_node = {}
        # 对于每个节点进行复制
        for node_iter in nodes:
            map_node[node_iter] = UndirectedGraphNode(node_iter.label)
            
        # 对于每个节点的邻接节点进行复制
        for node_iter in nodes:
            new_node = map_node[node_iter]
            for neighbor in node_iter.neighbors:
                # 复制neighbor
                # 由于自己可以连成环，所以这里不能重新定义节点neighbor
                # new_neighbor = UndirectedGraphNode(neighbor.label)
                # neighbor由map得到，保证每次访问还是原来的节点，只是把它加在了new_node的相邻中而已
                new_neighbor = map_node.get(neighbor)
                new_node.neighbors.append(new_neighbor)
        
        # 返回字典中初始node对于复制的节点 
        return  map_node.get(node)
        
    def getNodes(self, node):
        q = Queue()
        node_set = set()
        
        q.put(node)
        node_set.add(node)
        while not q.empty():
            node_iter = q.get()
            for neighbor in node_iter.neighbors:
                if neighbor not in node_set:
                    q.put(neighbor)
                    node_set.add(neighbor)
                    
        return node_set