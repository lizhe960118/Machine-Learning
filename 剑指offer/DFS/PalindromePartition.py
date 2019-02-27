class Solution:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        if s is None:
            return None 
        
        tmp = []
        result = []
        # startIndex = 0
        
        # dfs时s在变，所以不需要startIndex
        self.dfsHelper(s, tmp, result)
        
        return result
    
    def dfsHelper(self, s, tmp, result):
        # 3.出口
        if len(s) == 0:
            result.append(tmp.copy())
            return
        
        # 2.递归
        for i in range(0, len(s)):
            if not self.isPalindrome(s[:i+1]):
                continue
            
            # print(s[:i+1])
            tmp.append(s[:i+1])
            self.dfsHelper(s[i+1:], tmp, result)
            tmp.pop()
            
        return
    
    # 判断子串是否为回文串
    def isPalindrome(self, s):
        return s == s[::-1]
        
        # s_len = len(s)
        # middle = s_len // 2
        # for i in range(middle):
        #     a = s[i:i+1]
        #     b = s[s_len - (i + 1) : s_len - i]
        #     if a != b:
        #         return False
        # return True

class Solution2:
    """
    @param: s: A string
    @return: A list of lists of string
    """
    def partition(self, s):
        if s is None:
            return None 
        
        tmp = []
        result = []
        startIndex = 0
        
        self.dfsHelper(s, startIndex, tmp, result)
        
        return result
    
    def dfsHelper(self, s, startIndex, tmp, result):
        if startIndex == len(s):
            result.append(tmp.copy())
            return
        
        
        for i in range(startIndex, len(s)):
            substr = s[startIndex:i+1]
            if not self.isPalindrome(substr):
                continue
            tmp.append(substr)
            self.dfsHelper(s, i+1, tmp, result)
            tmp.pop()
            
        return
    
    def isPalindrome(self, s):
        return s == s[::-1]