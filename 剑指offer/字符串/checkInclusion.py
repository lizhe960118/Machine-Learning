class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        # 使用一个count数组来辅助记录s1字符出现次数
        # solution2：使用两个数组来记录，最后比较他们是否相等，空间换时间
        count = [0 for i in range(26)]
        l1 = len(s1)
        l2 = len(s2)
        if l1 > l2:
            return False
        for i in range(l1):
            count[ord(s1[i:i+1]) - ord('a')] += 1
            count[ord(s2[i:i+1]) - ord('a')] -= 1
        if self.all_zero(count):
            return True
        for i in range(l1, l2):
            count[ord(s2[i:i+1]) - ord('a')] -= 1
            count[ord(s2[(i-l1):(i-l1+1)]) - ord('a')] += 1
            if self.all_zero(count):
                return True
        return False
    
    def all_zero(self, count):
        len_count = len(count)
        for i in range(len_count):
            if count[i] != 0:
                return False
        return True