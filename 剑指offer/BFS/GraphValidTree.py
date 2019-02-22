from queue import Queue
class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        # 图是树，无环就可以
        if len(edges) != n - 1:
            return False
        # 定义一个字典，每个节点保存它的邻居
        dict_graph = self.initial_graph(n, edges)
        # 定义一个集合hash，遍历每个节点，如果邻居neighbor在不在集合中，则在集合中添加，否则跳过
        hash_set = set()

        # 初始化节点，从0开始
        q = Queue()
        q.put(0)
        hash_set.add(0) # 0已经访问到

        # bfs搜索
        while not q.empty():
            node = q.get()
            for neighbor in dict_graph[node]:
                if neighbor in hash_set:
                    continue
                hash_set.add(neighbor)
                q.put(neighbor)

        return True if len(hash_set) == n else False

    def initial_graph(self, n, edges):
        dict_graph = {}
    
        for i in range(n):
            dict_graph[i] = []
            
        num_e = len(edges)
        for i in range(num_e):
            u = edges[i][0]
            v = edges[i][1]
            dict_graph[u].append(v)
            dict_graph[v].append(u)

        return dict_graph