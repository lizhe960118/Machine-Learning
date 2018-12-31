class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        count = 0
        n = len(M)
        visited = [False for i in range(n)]
        for i in range(n):
            if visited[i] == False:
                self.discard(M, i, visited)
                count += 1
        return count
    
    @classmethod
    def discard(self, M, k, visited):
        visited[k] = True
        n = len(M[0])
        for i in range(n):
            if(visited[i] or M[k][i] == 0):
                continue
            else:
                self.discard(M, i, visited)