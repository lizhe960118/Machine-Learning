class Solution:
    """
    @param: start: a string
    @param: end: a string
    @param: dict: a set of string
    @return: a list of lists of string
    """
    def findLadders(self, start, end, wordList):
        wordList.add(start)
        wordList.add(end)
        
        d = self.construct_dict(wordList)
        
        # bfs构建start到每个单词的距离
        distance = {}
        self.bfsHelper(start, end, wordList, distance, d)
        
        # dfs搜索所有的答案
        result = []
        tmp = []
        tmp.append(start)
        self.dfsHelper(start, end, distance, d, tmp, result)
        
        return result
      
    def construct_dict(self, wordList):
        d = {}
        for word in wordList:
            for i in range(len(word)):
                s = word[:i] + '_' + word[i+1:]
                d[s] = d.get(s, []) + [word]
        return d 
    
    def get_next_words(self, word, d):
        next_words = []
        for i in range(len(word)):
            s = word[:i] + '_' + word[i+1:]
            for next_word in d.get(s, []):
                if next_word not in next_words:
                    next_words.append(next_word)
        return next_words
        
    def bfsHelper(self, start, end, wordList, distance, d):
        q = collections.deque()
        q.append(start)
        
        distance[start] = 0
        while q:
            word = q.popleft()
            for next_word in self.get_next_words(word, d):
                if next_word not in distance:
                    distance[next_word] = distance[word] + 1
                    q.append(next_word)
        return 
    
    def dfsHelper(self,cur_word, end, distance, d, tmp, result):
        # 出口
        if cur_word == end:
            result.append(tmp.copy())
            return
        # 递归
        for next_word in self.get_next_words(cur_word, d):
            # print(next_word)
            if distance[next_word] != distance[cur_word] + 1:
                continue
            tmp.append(next_word)
            # print(tmp)
            self.dfsHelper(next_word, end, distance, d, tmp, result)
            tmp.pop()
        return