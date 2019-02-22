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
    @param: graph: a list of Undirect graph node
    @param: mapping: (graph node, value)
    @param: node: Undirect node where we into it 
    @param: target: number to be found
    @return: found or not 
    """
    def SerachGraphNodes(self, mapping, node, target):
        if node is None:
            return False

        # 使用队列bfs，分层遍历
        node_queue = Queue()
        node_set = set()

        node_queue.put(node)
        node_set.put(node)

        while not node_queue.empty():
            cur_node = node_queue.get()

            # 判断
            if mapping[node] == target:
                return True
            for neighbor in cur_node.neighbors:
                if neighbor not in node_set:
                    node_set.add(neighbor)
                    node_queue.append(neighbor)

        return False
        