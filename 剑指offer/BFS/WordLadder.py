class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: An integer
    """
    def ladderLength(self, start, end, wordList):
        
        def find_neighbors(word, wordList, end):
            # 对于s替换一个字母之后,看是否在wordList中，或者是否等于end
            neighbors = []
            for i in range(len(word)):
                for j in range(26):
                    chi = chr(ord("a") + j)
                    if chi == word[i]:
                        continue
                    s = word[:i] + chi + word[i+1:]
                    if s in wordList or s == end:
                        neighbors.append(s)
            return neighbors
            
        def bfs(start, end, wordList):
            if start == end:
                return 1 
                
            q = collections.deque()
            q.append(start)
            
            # 定义是否访问过
            visited = set()
            visited.add(start)
            
            step = 1
            
            while q:
                level_size = len(q)
                step += 1 
                
                for iter_num in range(level_size):
                    word = q.popleft()
                    
                    for neighbor in find_neighbors(word, wordList, end):
                        if neighbor == end:
                            return step
                        if neighbor in visited:
                            continue
                        q.append(neighbor)
                        visited.add(neighbor)
                        
            return 0
        
        return bfs(start, end, wordList)