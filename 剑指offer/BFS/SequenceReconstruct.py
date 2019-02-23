class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        graph = {}
        indegrees = {}
        
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
                    indegrees[node] = 0
        
        for seq in seqs:
            for i in range(len(seq) - 1):
                graph[seq[i]].add(seq[i+1])
                
        for node, neighbors in graph.items():
            for neighbor in neighbors:
                indegrees[neighbor] += 1
        
        q = collections.deque([node for node, indegree in indegrees.items() if indegree == 0])
        
        result = []
        while q:
            if len(q) != 1:
                return False
            node = q.popleft()
            result.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1 
                if indegrees[neighbor] == 0:
                    q.append(neighbor)
        
        return result == org