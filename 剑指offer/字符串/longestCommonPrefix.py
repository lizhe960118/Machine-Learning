class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        n_str = len(strs)
        if n_str <= 0:
            return ""
        com_str = strs[0]
        for i in range(n_str):
            com_str = ''.join(self.helper(com_str,strs[i]))
        return com_str
    def helper(self, str_a, str_b):
        n_min = min(len(str_a), len(str_b))
        flag = False
        for i in range(n_min):
            if str_a[i] != str_b[i]:
                flag = True
                break
        return str_a[:i] if flag else str_a[:n_min]